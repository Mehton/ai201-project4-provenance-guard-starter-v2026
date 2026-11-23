#!/usr/bin/env python3
"""
Criterion 4 (the appeal path) and criterion 5's log check, three trials each.

    python app.py                               # in one terminal
    python run_appeals.py --label before        # in another

`run_eval.py` only ever calls POST /submit, so it can't test an appeal, and it
can't see whether a rejected request left a decision in the log. This does
both, the same way: three trials, nothing changed in between, real output
saved to results/.

Criterion 4: 10 real submissions, each appealed. Every appeal must come back
200 with status "under_review" and add an appeal entry with the same
content_id to /log. Then one appeal on a made-up content_id must come back 404
and add nothing to the log.

Criterion 5 (log half): the five bad bodies from scenarios.py must not return a
content_id and must not add a decision entry — only "rejected" ones.

This sends and records, and counts what's plainly countable. The verdict is
still yours to write in the README.
"""

import argparse
import datetime as dt
import json
import sys

import requests

import config
import scenarios

DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"

# Ten ordinary submissions to appeal. Each goes out under its own creator_id so
# the rate limiter (5 a minute per creator) never gets involved.
APPEAL_TEXTS = [
    "I spent the weekend repainting the kitchen. The old colour was a tired yellow and the new one is a pale green that my partner picked. It took three coats.",
    "Our team switched to a new ticket tracker this month. Half of us like it and half of us keep forgetting to move cards. The stand-ups are shorter, at least.",
    "My grandmother taught me to make dumplings when I was nine. I still fold them badly, but they taste right, and that is the part she cared about.",
    "The bus was late again this morning, so I walked. It was cold but clear, and I noticed a bakery I had never seen before. I will go back on Saturday.",
    "I finally finished the novel my friend lent me in the spring. The ending was quieter than I expected. I keep thinking about the last chapter.",
    "We tried a new hiking trail near the lake. The map said two hours; it took us almost four because we kept stopping to look at birds.",
    "The library changed its opening hours, which wrecked my study routine. I now work from a cafe that plays music slightly too loud.",
    "I started learning the guitar in October. My fingers hurt for the first two weeks. Now I can play three songs, badly, and I am proud of all three.",
    "Our neighbour's dog escaped twice this week. Both times it came straight to our garden and sat by the back door, as if it had been invited.",
    "I cooked dinner for eight people on Friday. Nothing burned, the rice was soft, and nobody noticed that the dessert came from a shop.",
]


def log_entries(url):
    return requests.get(f"{url}/log", timeout=30).json()["entries"]


def run_trial(url, trial):
    appeals = []
    for i, text in enumerate(APPEAL_TEXTS, 1):
        creator = f"appeal_t{trial}_{i}"
        submitted = requests.post(f"{url}/submit",
                                  json={"text": text, "creator_id": creator},
                                  timeout=90)
        content_id = submitted.json().get("content_id")
        appealed = requests.post(f"{url}/appeal", json={
            "content_id": content_id,
            "reasoning": f"I wrote this myself (criterion 4, trial {trial}, appeal {i}).",
        }, timeout=30)
        body = appealed.json()
        logged = [e for e in log_entries(url)
                  if e.get("content_id") == content_id and e.get("event") == "appeal"]
        appeals.append({
            "content_id": content_id,
            "submit_status": submitted.status_code,
            "appeal_status": appealed.status_code,
            "appeal_response": body,
            "appeal_entries_in_log": len(logged),
            "passed": (appealed.status_code == 200
                       and body.get("status") == "under_review"
                       and len(logged) == 1),
        })

    before = len(log_entries(url))
    fake = requests.post(f"{url}/appeal", json={
        "content_id": "00000000-made-up-not-real",
        "reasoning": "This id was never issued.",
    }, timeout=30)
    after = len(log_entries(url))
    made_up = {
        "status": fake.status_code,
        "response": fake.json(),
        "log_entries_added": after - before,
        "passed": fake.status_code == 404 and after == before,
    }

    bad_bodies = next(s for s in scenarios.SCENARIOS if s.get("criterion") == 5)["bodies"]
    rejections = []
    for body in bad_bodies:
        # Own creator_id per trial, so these never collide with run_eval.py's
        # sends of the same bodies under the 5-a-minute limit.
        body = {**body, "creator_id": f"{body['creator_id']}_appeals_t{trial}"}
        before_entries = log_entries(url)
        response = requests.post(f"{url}/submit", json=body, timeout=30)
        new = log_entries(url)[len(before_entries):]
        payload = response.json()
        rejections.append({
            "sent": {k: (v if not isinstance(v, str) or len(v) < 60 else f"<{len(v)} chars>")
                     for k, v in body.items()},
            "status": response.status_code,
            "response": payload,
            "new_log_entries": [{k: e.get(k) for k in ("event", "status", "reason")}
                                for e in new],
            "passed": (response.status_code == 400
                       and "error" in payload
                       and "content_id" not in payload
                       and all(e.get("status") == "rejected" for e in new)),
        })

    return {"appeals": appeals, "made_up_id": made_up, "bad_input_log_check": rejections}


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=DEFAULT_URL)
    args = parser.parse_args()

    try:
        requests.get(f"{args.url}/health", timeout=5)
    except Exception:  # noqa: BLE001
        print(f"Nothing answering at {args.url}. Start it:  python app.py", file=sys.stderr)
        sys.exit(1)

    trials = []
    for trial in range(1, args.trials + 1):
        result = run_trial(args.url, trial)
        trials.append(result)
        print(f"trial {trial}: appeals {sum(a['passed'] for a in result['appeals'])}/10, "
              f"made-up id {'ok' if result['made_up_id']['passed'] else 'FAILED'}, "
              f"bad input {sum(r['passed'] for r in result['bad_input_log_check'])}"
              f"/{len(result['bad_input_log_check'])}")

    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"appeals_{stamp}{label}.md"
    lines = [f"# Appeal path and bad-input log check{f' — {args.label}' if args.label else ''}",
             "", "- Produced by: `run_appeals.py::run_trial`",
             "- Service: `app.py::appeal`, `app.py::submit`",
             f"- {args.trials} trials · {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}", ""]
    for n, result in enumerate(trials, 1):
        lines += [f"## Trial {n}", "", "```json", json.dumps(result, indent=2), "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
