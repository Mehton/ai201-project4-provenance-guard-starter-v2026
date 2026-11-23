# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. A writer sends text and creator_id as JSON to POST /submit.
2. The route checks that the JSON and fields are valid and that the text is no longer than 10,000 characters.
3. `detector.py` measures how predictable the text is to a local language model and returns model_score.
4. `stylometry.py` measures sentence-length variation, vocabulary variety, and punctuation per word, and turns them into style_score. Vocabulary variety is measured and logged but not scored.
5. `scoring.py::combine_signals` combines them 50/50. It only allows an AI score when both signals lean AI.
6. `scoring.py::score_to_label` maps the combined score to a guess and a full-sentence label: human (<= 0.40), unsure (between), or AI (>= 0.70).
7. The service logs the decision and returns the scores, label, confidence, and content_id. The writer can use that ID to appeal.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to a local language model (gpt2), as perplexity. `detector.py::model_signal` squashes perplexity onto 0–1 with a logistic curve centred at perplexity 45. Low perplexity gives a high score, which means more likely AI.

**Why that might differ between human and AI writing:** A language model writes by repeatedly picking a likely next word, so its output is text a model finds easy to predict. Human writing wanders more, with odd word choices, abrupt turns and specific details instead of typical ones.

**What it can't see:** Who wrote the text. It rewards common words in short, ordinary sentences, and plenty of real people write that way: second-language writers using vocabulary they're sure of, younger writers, and anyone writing plainly on purpose. Those people score about as machine-like as a machine does. It also fails the other way: AI text asked to use rare or ornate words scores as human, because rare words are exactly what the model can't predict. It reads at most 400 tokens, so it never sees the rest of a long piece.

### Signal two — the style signal

**What it measures:** The shape of the text, not its meaning. `stylometry.py::style_signal` computes three measures, maps each onto 0–1 "AI likeness" with a straight line between two anchor values, and takes a weighted average:

| Measure                | How it's computed                                                            | 1.0 (AI) at | 0.0 (human) at | Weight |
| ---------------------- | ---------------------------------------------------------------------------- | ----------- | -------------- | ------ |
| Sentence-length spread | standard deviation of sentence lengths ÷ mean                                | <= 0.20     | >= 0.60        | 0.75   |
| Punctuation density    | every mark except the full stop, per word                                    | <= 0.03     | >= 0.09        | 0.25   |
| Vocabulary variety     | moving-average type-token ratio (40-word windows, so length doesn't skew it) | —           | —              | **0**  |

I read the anchor values off my calibration texts. Vocabulary variety gets no weight because it pointed the _wrong way_: the AI texts had the most varied vocabulary (0.82–0.90) and my own plain paragraph had the least (0.66). Scoring "low variety = AI" would have accused the writer from my false-positive trace. It's still logged, under `style_parts`. A submission with fewer than two sentences gets a neutral 0.5 for spread, because "no spread to measure" isn't evidence of AI.

**Why that might differ between human and AI writing:** Models tend to produce even, medium-length sentences, safe repeated phrasing and tidy punctuation. People mix very short sentences with long ones, and they reach for dashes, asides and questions.

**What it can't see:** Meaning. It can't tell carefully edited human prose, a list, or a short answer from machine output, so even, plainly punctuated human writing looks AI-like here too. That's the same writer signal one already over-accuses. It is also easy to fool on purpose: chopping a few sentences short or adding a dash and a question mark moves the score without changing a word of the content. Type-token ratio falls as text gets longer, so length alone can look like a signal. Very short submissions (one or two sentences) give it almost nothing to measure. It also depends entirely on where it thinks sentences end: footnote markers like `sixteen.1 She` hide sentence breaks, and removing two of them moved my factual-bio test from style 0.19 to 0.75.

### Tracing the false positive

A second-language writer submits a 250-word essay they wrote themselves. They use words they're sure of, medium-length sentences, and mostly full stops.

1. **Model signal = 0.80.** Common words in ordinary sentences give low perplexity, which is signal one's blind spot.
2. **Style signal = 0.60.** Even sentence lengths, repeated vocabulary and little punctuation lean AI-like. That's the _same_ blind spot, so the two signals agree for the same wrong reason.
3. **Combined (planned 60/40):** 0.6 × 0.80 + 0.4 × 0.60 = **0.72**, which is past the 0.65 AI line. The writer gets the **high-confidence AI** label.
4. **What they can do:** send the `content_id` from the response to `POST /appeal` with their reasoning. The item moves to `under_review` and the appeal is logged. Nothing is re-scored automatically.

What this means for the build: with these numbers, a plain writer gets accused unless style pulls hard the other way. I'll check this with a plainly written human paragraph in Milestone 4. If it lands above the AI line, I'll raise the AI threshold or lower the model weight. The AI label also has to say how to appeal, because for this writer the appeal is the only way back.

**What happened in Milestone 4:** my own plain paragraph scored model 0.52 and style 0.63. That's AI-leaning on style, as predicted, because it has no punctuation at all. Under the original 60/40 plan it would have combined to 0.57; under my final rule it's 0.58, which is **unsure**, not AI. Formal, factual human writing turned out to be the bigger risk. The model scored my Joan Armatrading bio 0.59, and with its footnote markers removed both signals leaned AI (see the table below). That's why I moved to 50/50 and added the agreement rule below, instead of only raising the threshold.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** Average the two signals with equal weight. Then apply an agreement rule to the AI label only: if _either_ signal is below 0.5 (it leans human), the combined score is capped just under the AI threshold. So one signal on its own can make a piece "unsure", but it can never get it called AI. The cap is one-sided on purpose. A wrong accusation is the expensive mistake, and a missed detection is the cheap one.

**The numbers:** `WEIGHT_MODEL_SIGNAL = 0.5`, `WEIGHT_STYLE_SIGNAL = 0.5`, and `AGREEMENT_FLOOR = 0.5` (the cap is `AI_THRESHOLD − 0.01` = 0.69). All are in `config.py`.

Why 50/50 and not my planned 60/40: on my calibration texts each signal was wrong about a _different_ human. The model leaned AI on my factual bio (0.59) while the style signal called it human (0.19). On my plain paragraph it was the other way round: style leaned AI (0.63) while the model sat near the middle (0.52). Neither earned more weight than the other.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**My calibration run** (real `/submit` responses). "Before" uses the starter thresholds of 0.35 / 0.65; "Final" uses my thresholds of 0.40 / 0.70:

| Input                                                                                     | model_score | style_score | combined | Before | Final  |
| ----------------------------------------------------------------------------------------- | ----------- | ----------- | -------- | ------ | ------ |
| Clearly AI (generic paragraph about AI)                                                   | 0.9104      | 0.8375      | 0.8740   | AI     | AI     |
| Clearly human (my own casual message about college, typos and all)                        | 0.2861      | 0.5003      | 0.3932   | unsure | human  |
| **Formal human** (a factual bio of Joan Armatrading, report style, with footnote markers) | 0.5914      | 0.1910      | 0.3912   | unsure | human  |
| **Lightly edited AI** (the AI paragraph, reworded by hand)                                | 0.6473      | 0.6691      | 0.6582   | AI     | unsure |
| Plain human (my own college paragraph)                                                    | 0.5238      | 0.6327      | 0.5783   | unsure | unsure |
| _The same bio, footnote markers removed_                                                  | 0.6204      | 0.7532      | 0.6868   | **AI** | unsure |

**At 0.35 / 0.65, the human label was out of reach and a real writer was accused.** My casual message scored 0.39: the model read it as human (0.29), but its 29 words have no punctuation inside sentences, so style sat at 0.50. None of my human texts reached "human", which would fail criterion 3. Worse, the bio with its footnote markers removed scored 0.69 and was labelled AI. The markers have no space after the full stop (`sixteen.1 She`), so the splitter had merged two pairs of sentences. With them removed, the sentences are all similar in length, style jumps from 0.19 to 0.75, both signals pass 0.5, and the agreement rule doesn't apply. Nothing about who wrote it changed, only the formatting.

**So I moved the lines to 0.40 / 0.70.** Both human texts now reach "human", and the clean bio drops to "unsure". The price is the lightly edited AI text (0.66), which is now missed and lands in "unsure". I chose that trade on purpose: a missed detection costs the site a little, and a wrong accusation costs a writer a lot. The clean-bio case is still only 0.01 below the AI line, so I'm keeping it for unit 8.

**A case where my two signals split, and what my rule does with it:** My Joan Armatrading bio, as written. The model leans AI (0.59), because factual sentences like "She received an … Award … in 1996" are fairly predictable to GPT-2. The style signal says human (0.19), because its sentences, as the splitter sees them, swing from 11 words to 46. The average is 0.39, which is "human" with my final thresholds. Whatever the numbers do, the agreement rule guarantees it can never reach the 0.70 AI line while style is under 0.5. That's the behaviour I want: two methods disagreeing _is_ uncertainty, and a real writer shouldn't be accused on one method's word.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label                 | Score range            | The exact text a reader sees                                                                                                                                                                                    |
| --------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| high-confidence human | 0.00 – 0.40            | We think this was probably written by a person.                                                                                                                                                                 |
| unsure                | above 0.40, below 0.70 | We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.                                       |
| high-confidence AI    | 0.70 – 1.00            | This writing closely matches patterns we often see in AI generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it. |

Every score from 0 to 1 maps to exactly one label: <= 0.40 is human, >= 0.70 is AI, and everything in between is unsure. The text lives in `scoring.py` (`LABEL_HUMAN`, `LABEL_UNSURE`, `LABEL_AI`), and `scoring.py::score_to_label` picks one. I checked that all three are reachable with real submissions: my AI paragraph got AI (0.87), my casual message got human (0.39), and my college paragraph got unsure (0.58).

**Why I worded the "unsure" one this way:** The person reading it may well have written every word, so it says _we_ can't tell. That puts the uncertainty on the system, not on the writer. "Happens often with real writing" tells them this label isn't a polite way of saying "probably AI". "We are not flagging it" answers the question they're actually worried about: is anything going to happen to me? It deliberately doesn't mention appeals, because offering an appeal would imply there's something to fight. The AI label is the one that says "not proof" and explains how to appeal, because that's the reader who needs a way back.

<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

<!-- Final run, after Milestone 5. The service ran on port 5050 for this test
     (AI201_DEBUG=0, so responses came back compact; pretty-printed below). -->

```bash
$ curl -X POST http://127.0.0.1:5050/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "When I was goping to college in my hometown. I used to study every day in the library. I miss the pizza place in the collage where I used to eat pizza with my friends.", "creator_id": "bhupinder"}'
```

```json
{
  "confidence": 0.5783,
  "content_id": "1a5f48cf-fad5-4133-8d12-e77439c8accf",
  "creator_id": "bhupinder",
  "guess": "unsure",
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "model_score": 0.5238,
  "status": "decided",
  "style_score": 0.6327
}
```

**A rejected submission** (empty text)

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "   ", "creator_id": "t"}'
```

```json
{
  "error": "empty_text",
  "message": "text is empty."
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5050/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "1a5f48cf-fad5-4133-8d12-e77439c8accf", "reasoning": "I wrote this paragraph myself about my own college days. The typos are mine too."}'
```

```json
{
  "content_id": "1a5f48cf-fad5-4133-8d12-e77439c8accf",
  "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
  "status": "under_review"
}
```

An appeal on a made-up id gets `404 {"error": "unknown_content_id", ...}` and adds nothing to the log. A missing `reasoning` or `content_id` gets a 400.

**What the log shows afterwards**

The original decision is untouched, and the appeal sits right after it with the same `content_id` and `status: "under_review"`.

```bash
$ curl "http://127.0.0.1:5050/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.5783,
      "content_id": "1a5f48cf-fad5-4133-8d12-e77439c8accf",
      "creator_id": "bhupinder",
      "guess": "unsure",
      "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
      "model_score": 0.5238,
      "status": "decided",
      "style_parts": { "punctuation": 1.0, "spread": 0.5103, "ttr": 0.7716 },
      "style_score": 0.6327,
      "timestamp": "2026-11-09T07:14:41+00:00"
    },
    {
      "content_id": "1a5f48cf-fad5-4133-8d12-e77439c8accf",
      "creator_id": "bhupinder",
      "event": "appeal",
      "reasoning": "I wrote this paragraph myself about my own college days. The typos are mine too.",
      "status": "under_review",
      "timestamp": "2026-11-09T07:14:41+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1: reviewing my acceptance criteria**

- _What I asked for:_ After writing my five criteria in `criteria.md`, I asked Claude to double-check them and tell me what to improve.
- _What came back:_ Two real problems and three weaker spots. Criterion 4 expected the status `appealed`, but the service uses `under_review`, so it would have failed every appeal. Criterion 5 said a rejected request must leave no log entry, which contradicts unit 8's rule that rejections are logged. It also flagged that criterion 1 copied the example from the starter file, and that criteria 2 and 3 didn't say which texts they ran on.
- _What I changed:_ I had the fixes applied: the correct status, a 404 case for made-up ids, "no decision entry" instead of "no log entry", a 0.30 score gap tied to the width of my unsure band, and plain-writing pieces in criterion 1. Then I asked for all five to be rewritten in a "Given …, … in X of Y" format, which made each one easier to check.

**Moment 2: calibrating the style signal and thresholds**

- _What I asked for:_ To build the style signal and combining rule for Milestone 4 and test them on clearly-AI, clearly-human, formal-human and lightly-edited-AI inputs.
- _What came back:_ A working style signal, plus a surprise: vocabulary variety pointed the wrong way (the AI text had the _most_ varied vocabulary). It was given no weight, and the weights went from my planned 60/40 to 50/50 with an agreement rule. But the calibration texts it picked for "formal" and "clearly human" were famous public-domain passages, not mine.
- _What I changed:_ I replaced them with my own texts: a factual bio I wrote with footnote markers, and a casual message I'd typed. That exposed two things the borrowed texts hid. The bio was labelled AI once its footnotes were removed, a formatting-only false positive. And none of my human writing could reach the human label at 0.35. I chose to move the thresholds to 0.40 / 0.70, accepting that lightly edited AI now lands in "unsure".

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** **5 per minute, 50 per day**

<!-- (`config.py`: `RATE_LIMIT_PER_MINUTE`, `RATE_LIMIT_PER_DAY`) -->

**Why those numbers and not others:**

<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

- **A real writer** submits a piece, maybe fixes a typo and resubmits, maybe tries a second draft. That's a couple of requests a minute at most, and a few dozen on a heavy day. Five a minute leaves room to resubmit quickly without ever hitting the limit, and 50 a day is far more than anyone writes.
- **A script mapping my thresholds** needs to send hundreds or thousands of small variations, nudging a text until it slips from "AI" to "unsure" and learning where my 0.70 line is. At 50 a day, a thousand probes takes 20 days per `creator_id` instead of a few seconds. The per-minute cap stops a burst; the per-day cap stops a slow, patient script that stays under 5 a minute.
- **Why not tighter?** At 1–2 a minute, a writer fixing a typo would get a 429 for doing something normal, and the person hurt would be a real writer, not an attacker. **Why not looser?** The starter's 10 a minute and 200 a day would let one caller send 200 probes a day, enough to map the thresholds in under a week.

**What a caller counts as:** A **`creator_id`**, falling back to the IP address when the request has none (`app.py::rate_limit_key`). This fails in one specific way: `creator_id` is whatever the caller says it is, so a script can invent a new id for every request and never hit the limit. Per-address limiting fails differently: one script behind rotating proxies looks like a thousand callers, while a whole household or classroom on one Wi-Fi looks like one caller and shares a single quota. I chose per-creator because it never punishes writers for sharing a network. Its weakness, a script inventing ids, would need sign-in to close properly.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
$ python run_attacks.py --flood 15

15 submissions as 'flood_tester' against http://127.0.0.1:5000

============================================================
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
============================================================

10 of 15 were rate limited.
Wrote results\flood_2026-11-22_2041.md
```

Each 429 left a trace. `GET /log` shows 10 entries like this one, next to the 5 decisions that got through:

```json
{
  "creator_id": "flood_tester",
  "event": "rejected",
  "limit": "5 per 1 minute",
  "reason": "rate_limited",
  "status": "rejected",
  "timestamp": "2026-11-23T04:41:33+00:00"
}
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

`python run_attacks.py --set attack_set --label before` sent all 56 attacks through `POST /submit` before I changed anything. Full output: `results/attack_run_2026-11-22_2109_before.md`. No attack crashed the service and none got a 500. The script auto-marked 0 as BROKE; I judged all 56 by hand.

**How I marked them:**

- **Attacks hiding AI text** (evasion, and prompt injection wrapped around AI text): **held** only if the text still got the AI label. "Unsure" counts as **broke**, because my unsure label tells the reader "we are not flagging it". The AI text got through.
- **False positives** (real human writing): **broke** if it got the AI label.
- **Malformed input:** **held** if it was rejected with a 4xx. **Broke** if junk got a confident verdict and a `content_id`.
- **Hostile label / log injection:** **held** if the label text and the log line came out intact.
- **Flood:** **held** if the limiter cut it off.

**Totals: 36 held, 20 broke.**

| Family | Attacks | Held | Broke |
|---|---|---|---|
| evasion | 10 | 2 | **8** |
| false_positive | 8 | 4 | **4** |
| prompt_injection | 6 | 3 | **3** |
| malformed | 20 | 15 | **5** |
| flood_same_creator | 12 | 12 | 0 |
| **Total** | **56** | **36** | **20** |

| ID | Family | Going for | Status | Guess | Score | Verdict |
|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.571 | **BROKE** |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.416 | **BROKE** |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.530 | **BROKE** |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | ai | 0.795 | held |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.221 | **BROKE** |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.406 | **BROKE** |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.481 | **BROKE** |
| EV08 | evasion | signal one: text below the token window | 200 | unsure | 0.545 | **BROKE** |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.570 | **BROKE** |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.808 | held |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.567 | held |
| FP02 | false_positive | human writing in a formal register | 200 | ai | 0.832 | **BROKE** |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | ai | 0.782 | **BROKE** |
| FP04 | false_positive | a student essay written to a rubric | 200 | ai | 0.760 | **BROKE** |
| FP05 | false_positive | technical documentation written by a person | 200 | ai | 0.828 | **BROKE** |
| FP06 | false_positive | a person imitating a formal template | 200 | unsure | 0.641 | held |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | unsure | 0.558 | held |
| FP08 | false_positive | very short genuine human submission | 200 | unsure | 0.443 | held |
| PI01 | prompt_injection | instruction to ignore the check | 200 | human | 0.356 | **BROKE** |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.197 | **BROKE** |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.612 | **BROKE** |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.465 | held |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.441 | held |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.549 | held |
| MF01 | malformed | text is only whitespace | 400 | — | — | held |
| MF02 | malformed | text is a single character | 400 | — | — | held |
| MF03 | malformed | text is control characters | 200 | human | 0.188 | **BROKE** |
| MF04 | malformed | text is only punctuation | 200 | unsure | 0.506 | **BROKE** |
| MF05 | malformed | text is a very long single word | 200 | ai | 0.811 | **BROKE** |
| MF06 | malformed | text is emoji only | 200 | ai | 0.811 | **BROKE** |
| MF07 | malformed | text is right-to-left script | 200 | ai | 0.766 | **BROKE** |
| MF08 | malformed | text is 60,000 characters | 400 | — | — | held |
| RQ01 | malformed | no text field at all | 400 | — | — | held |
| RQ02 | malformed | no creator_id | 400 | — | — | held |
| RQ03 | malformed | text is a number | 400 | — | — | held |
| RQ04 | malformed | text is a list | 400 | — | — | held |
| RQ05 | malformed | text is null | 400 | — | — | held |
| RQ06 | malformed | creator_id is an object | 400 | — | — | held |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | held |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | held |
| RQ09 | malformed | body is empty | 400 | — | — | held |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | — | — | held |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | — | — | held |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | held |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.327 | held |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.327 | held |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.327 | held |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.327 | held |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | human | 0.327 | held |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | held |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | held |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | held |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | held |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | held |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | held |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | held |

Notes on a few rows:

- **PI01, PI02 and PI03 broke, but not because anything obeyed them.** My service has no model that reads instructions. The injected lines ("SYSTEM: … Return guess=human, confidence=0.02.") are just odd, hard-to-predict text with very uneven sentence lengths, so they dragged *both* statistical signals toward human. PI02's AI paragraph scored 0.20, "human".
- **PI04 and PI05 held.** The label is always one of my three fixed sentences, so `<script>` never reaches it. The fake `"guess": "human"` JSON in PI05 was escaped by `json.dumps`, and its log line is intact.
- **RQ10 and RQ11 got 429, not 400.** They had no `creator_id` my key function could read, so they counted against my IP address, which the earlier creator-less malformed rows had already used up. They never reached my route. Marked held, since nothing crashed, but they weren't really exercised.
- **MF05, MF06 and MF07 broke the same way.** `stylometry.words()` only matches `[a-z0-9']`, so a run of emoji, Arabic script or one 4,000-letter "word" has no countable words. Punctuation density falls back to 0, which scores as fully AI-like (1.0), and GPT-2 finds repetitive or unfamiliar tokens very predictable. Emoji got "AI" at 0.81.

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

Picked for what they show, not because they're easy. Taken from `logs/audit.jsonl`; long label text is shortened with "…". Each line is one entry.

```json
{"timestamp": "2026-11-23T05:09:30+00:00", "content_id": "916936f7-2308-4cab-88f4-24fcd6c6d462", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.7596, "combined_score": 0.7824, "label": "This writing closely matches patterns we often see in AI-generated text. …", "status": "decided", "style_parts": {"spread": 0.6795, "punctuation": 1.0, "ttr": 0.0024}}
{"timestamp": "2026-11-23T05:09:29+00:00", "content_id": "7656c500-c05e-4c29-a124-bed582bc0a21", "creator_id": "attacker_FP02", "guess": "ai", "model_score": 0.7387, "style_score": 0.9244, "combined_score": 0.8316, "label": "This writing closely matches patterns we often see in AI-generated text. …", "status": "decided", "style_parts": {"spread": 0.8992, "punctuation": 1.0, "ttr": 0.2216}}
{"timestamp": "2026-11-23T05:09:35+00:00", "content_id": "bce2d1d6-960f-4618-9361-0b65ba7061b4", "creator_id": "attacker_MF07", "guess": "ai", "model_score": 0.9064, "style_score": 0.625, "combined_score": 0.7657, "label": "This writing closely matches patterns we often see in AI-generated text. …", "status": "decided", "style_parts": {"spread": 0.5, "punctuation": 1.0, "ttr": 1.0}}
{"timestamp": "2026-11-23T05:09:34+00:00", "content_id": "e9fdfe4a-acc5-4ace-8525-0fc8938ffa66", "creator_id": "attacker_MF06", "guess": "ai", "model_score": 0.9969, "style_score": 0.625, "combined_score": 0.811, "label": "This writing closely matches patterns we often see in AI-generated text. …", "status": "decided", "style_parts": {"spread": 0.5, "punctuation": 1.0, "ttr": 1.0}}
{"timestamp": "2026-11-23T05:09:31+00:00", "content_id": "1322152d-4700-4bf7-a831-3f3b30012485", "creator_id": "attacker_PI02", "guess": "human", "model_score": 0.2044, "style_score": 0.19, "combined_score": 0.1972, "label": "We think this was probably written by a person.", "status": "decided", "style_parts": {"spread": 0.0, "punctuation": 0.76, "ttr": 0.0}}
{"timestamp": "2026-11-23T05:09:27+00:00", "content_id": "db31acdd-a60f-4091-b69e-150b13d5609c", "creator_id": "attacker_EV05", "guess": "human", "model_score": 0.3212, "style_score": 0.1208, "combined_score": 0.221, "label": "We think this was probably written by a person.", "status": "decided", "style_parts": {"spread": 0.0, "punctuation": 0.4833, "ttr": 0.0}}
{"timestamp": "2026-11-23T05:09:26+00:00", "content_id": "cdfa88c8-fb19-4414-9bbc-c705eb001d87", "creator_id": "attacker_EV01", "guess": "unsure", "model_score": 0.1635, "style_score": 0.9779, "combined_score": 0.5707, "label": "We can't tell whether this was written by a person or with help from AI. …", "status": "decided", "style_parts": {"spread": 1.0, "punctuation": 0.9117, "ttr": 0.0}}
{"timestamp": "2026-11-23T05:09:32+00:00", "content_id": "8701b18a-852b-4ab8-a830-0dad443b0809", "creator_id": "attacker_MF03", "guess": "human", "model_score": 0.0, "style_score": 0.375, "combined_score": 0.1875, "label": "We think this was probably written by a person.", "status": "decided", "style_parts": {"spread": 0.5, "punctuation": 0.0, "ttr": 0.0}}
{"timestamp": "2026-11-23T05:09:32+00:00", "content_id": "eb1e92cb-545d-4898-a786-a8a282a59db6", "creator_id": "attacker_PI05", "guess": "unsure", "model_score": 0.6401, "style_score": 0.2411, "combined_score": 0.4406, "label": "We can't tell whether this was written by a person or with help from AI. …", "status": "decided", "style_parts": {"spread": 0.3215, "punctuation": 0.0, "ttr": 0.0}}
{"timestamp": "2026-11-23T05:09:35+00:00", "creator_id": "attacker_flood", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
{"timestamp": "2026-11-23T05:09:35+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
{"timestamp": "2026-11-23T05:09:35+00:00", "creator_id": "attacker_MF08", "event": "rejected", "status": "rejected", "reason": "text_too_long", "length": 57639}
```

What they show, top to bottom:
1. **FP03:** a careful non-native English writer, called AI.
2. **FP02:** formal human writing, called AI at 0.83.
3. **MF07:** Arabic text, called AI, because none of its words are countable.
4. **MF06:** emoji only, called AI.
5. **PI02:** AI text with a fake "SYSTEM" line on top, called human.
6. **EV05:** AI text after a heavy human edit, called human.
7. **EV01:** typos make the two signals split hard (model 0.16, style 0.98), and the result lands in unsure.
8. **MF03:** control characters, called human.
9. **PI05:** a log-injection attempt; the line is intact.
10. **Three rejections:** the `flood_same_creator` 429; RQ10's 429, counted against my IP because it had no readable `creator_id`; and a 400 for 57,639 characters. The rejection entries carry fewer fields than decisions, which is expected.

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

**FP03, a non-native English speaker writing carefully, labelled high-confidence AI (0.78).** It's the exact writer from my Milestone 1 false-positive trace, and my system did exactly what that trace predicted. Short, correct sentences with safe vocabulary ("I did not expect the rain to continue for so many days") are predictable to GPT-2 (model 0.81). Using no commas, dashes or questions makes the style signal call it AI too (0.76; punctuation part 1.0). Both signals were above 0.5, so my agreement rule, built for this person, didn't step in. They'd be told their careful work "closely matches patterns we often see in AI-generated text", and the only thing between them and that label is an appeal they may not feel confident enough to write. MF07 (Arabic text called AI) is close behind: it accuses anyone who writes in a non-Latin script, for a reason that has nothing to do with how they write.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

`python run_eval.py --label before` ran criteria 1, 2, 3 and 5 from `scenarios.py`, three trials back to back, with nothing changed in between. `run_eval.py` only calls `POST /submit`, so I wrote `run_appeals.py` for criterion 4 (submit, appeal, then read `/log`) and for the log half of criterion 5 (no decision entry for bad input). It runs three trials the same way. Output: `results/run_2026-11-22_2210_before.md` and `results/appeals_2026-11-22_2210_before.md`.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
| --------- | ------ | ----- | ----- | ----- | ------- |
| 1. My own writing is rarely called AI, plain never | ≤ 1 of 10 `"ai"`, 0 of 3 plain | 0/10, plain 0/3 | 0/10, plain 0/3 | 0/10, plain 0/3 | **MET** |
| 2. Clearly-AI and clearly-human text score far apart | median gap ≥ 0.30 | 0.43 | 0.43 | 0.43 | **MET** |
| 3. All three labels are reachable | 3 of 3 get intended label | 2/3 | 2/3 | 2/3 | **MISSED** |
| 4. Every appeal is recorded and moves the item to review | 10 of 10 + made-up id → 404, nothing logged | 10/10 + 404 | 10/10 + 404 | 10/10 + 404 | **MET** |
| 5. Bad input is rejected clearly, not crashed on | 5 of 5 → 400, no `content_id`, no decision entry | 5/5 | 5/5 | 5/5 | **MET** |

All three trials returned identical scores to four decimal places, as expected: nothing in either signal is random.

- **Criterion 1:** none of my 10 pieces got "ai" in any trial; 4 got "human" and 6 got "unsure". It was closer than "0 of 10" makes it look. My plain Patti Smith paragraph scored **0.69**, right at the agreement cap: style was 1.0 (no inner punctuation, even sentences), and only the model's 0.41 kept the agreement rule in play. Without that rule it would have averaged 0.70 and been called AI.
- **Criterion 2:** the human median was 0.39 and the AI median was 0.83, a gap of 0.43. But one AI text (0.65) and one of my pieces (0.62) overlap in the unsure band.
- **Criterion 3 missed:** my clearly-AI text got "ai" (0.83) and my casual message got "human" (0.39), but my hand-edited AI paragraph got **"ai" (0.72) instead of "unsure"**, in all three trials. "Unsure" itself is reachable (6 of my criterion-1 pieces landed there), but this criterion named a specific text and target, and the target was missed.

**Real output from one trial**, pasted as text, naming the file and function
that produced it (long label text shortened with "…"):

**Criterion 1: my own writing** (`results/run_2026-11-22_2210_before.md`, produced by `run_eval.py::main`, trial 1):

```json
[
 {
  "status": 200,
  "guess": "unsure",
  "confidence": 0.5783,
  "model_score": 0.5238,
  "style_score": 0.6327,
  "label": "We can't tell whether … (unsure label)",
  "sent": "When I was goping to college in my hometown. …"
 },
 {
  "status": 200,
  "guess": "unsure",
  "confidence": 0.69,
  "model_score": 0.4068,
  "style_score": 1.0,
  "label": "We can't tell whether … (unsure label)",
  "sent": "Patti Smith contributed to her group as a lyr…"
 },
 {
  "status": 200,
  "guess": "unsure",
  "confidence": 0.5179,
  "model_score": 0.5058,
  "style_score": 0.53,
  "label": "We can't tell whether … (unsure label)",
  "sent": "Some of the charts that are provided are a bi…"
 },
 {
  "status": 200,
  "guess": "human",
  "confidence": 0.3932,
  "model_score": 0.2861,
  "style_score": 0.5003,
  "label": "We think this was probably written by a person.",
  "sent": "s When i was in the collage I used to go to l…"
 },
 {
  "status": 200,
  "guess": "human",
  "confidence": 0.3912,
  "model_score": 0.5914,
  "style_score": 0.191,
  "label": "We think this was probably written by a person.",
  "sent": "Joan Armatrading first performed at a concert…"
 },
 {
  "status": 200,
  "guess": "unsure",
  "confidence": 0.6151,
  "model_score": 0.2302,
  "style_score": 1.0,
  "label": "We can't tell whether … (unsure label)",
  "sent": "Bryan and his group vis 12 have a dataset tha…"
 },
 {
  "status": 200,
  "guess": "unsure",
  "confidence": 0.5356,
  "model_score": 0.3061,
  "style_score": 0.7652,
  "label": "We can't tell whether … (unsure label)",
  "sent": "The team gave feedback about its deliverables…"
 },
 {
  "status": 200,
  "guess": "human",
  "confidence": 0.3608,
  "model_score": 0.5039,
  "style_score": 0.2176,
  "label": "We think this was probably written by a person.",
  "sent": "Joan Anita Barbra Armatrading is a Kittitian-…"
 },
 {
  "status": 200,
  "guess": "unsure",
  "confidence": 0.5994,
  "model_score": 0.6136,
  "style_score": 0.5852,
  "label": "We can't tell whether … (unsure label)",
  "sent": "Joan Armatrading did not mention anything abo…"
 },
 {
  "status": 200,
  "guess": "human",
  "confidence": 0.2519,
  "model_score": 0.5038,
  "style_score": 0.0,
  "label": "We think this was probably written by a person.",
  "sent": "Patti Smith was a poet and singer. She was a …"
 }
]
```

**Criterion 2: score spread** (`results/run_2026-11-22_2210_before.md`, produced by `run_eval.py::main`, trial 1):

```json
[
 {
  "status": 200,
  "guess": "human",
  "confidence": 0.3932,
  "model_score": 0.2861,
  "style_score": 0.5003,
  "label": "We think this was probably written by a person.",
  "sent": "s When i was in the collage I used to go to l…"
 },
 {
  "status": 200,
  "guess": "human",
  "confidence": 0.3912,
  "model_score": 0.5914,
  "style_score": 0.191,
  "label": "We think this was probably written by a person.",
  "sent": "Joan Armatrading first performed at a concert…"
 },
 {
  "status": 200,
  "guess": "unsure",
  "confidence": 0.6151,
  "model_score": 0.2302,
  "style_score": 1.0,
  "label": "We can't tell whether … (unsure label)",
  "sent": "Bryan and his group vis 12 have a dataset tha…"
 },
 {
  "status": 200,
  "guess": "unsure",
  "confidence": 0.5356,
  "model_score": 0.3061,
  "style_score": 0.7652,
  "label": "We can't tell whether … (unsure label)",
  "sent": "The team gave feedback about its deliverables…"
 },
 {
  "status": 200,
  "guess": "human",
  "confidence": 0.3608,
  "model_score": 0.5039,
  "style_score": 0.2176,
  "label": "We think this was probably written by a person.",
  "sent": "Joan Anita Barbra Armatrading is a Kittitian-…"
 },
 {
  "status": 200,
  "guess": "ai",
  "confidence": 0.7201,
  "model_score": 0.7897,
  "style_score": 0.6506,
  "label": "This writing closely matches patterns … (AI label)",
  "sent": "Effective time management is essential for su…"
 },
 {
  "status": 200,
  "guess": "ai",
  "confidence": 0.8296,
  "model_score": 0.9175,
  "style_score": 0.7417,
  "label": "This writing closely matches patterns … (AI label)",
  "sent": "Climate change represents one of the most pre…"
 },
 {
  "status": 200,
  "guess": "unsure",
  "confidence": 0.6534,
  "model_score": 0.7691,
  "style_score": 0.5378,
  "label": "We can't tell whether … (unsure label)",
  "sent": "Reading offers numerous benefits for personal…"
 },
 {
  "status": 200,
  "guess": "ai",
  "confidence": 0.8277,
  "model_score": 0.7578,
  "style_score": 0.8977,
  "label": "This writing closely matches patterns … (AI label)",
  "sent": "Remote work has transformed the modern workpl…"
 },
 {
  "status": 200,
  "guess": "ai",
  "confidence": 0.8352,
  "model_score": 0.8149,
  "style_score": 0.8555,
  "label": "This writing closely matches patterns … (AI label)",
  "sent": "Regular physical activity plays a crucial rol…"
 }
]
```

**Criterion 3: label coverage** (`results/run_2026-11-22_2210_before.md`, produced by `run_eval.py::main`, trial 1):

```json
[
 {
  "status": 200,
  "guess": "ai",
  "confidence": 0.8296,
  "model_score": 0.9175,
  "style_score": 0.7417,
  "label": "This writing closely matches patterns … (AI label)",
  "sent": "Climate change represents one of the most pre…"
 },
 {
  "status": 200,
  "guess": "human",
  "confidence": 0.3932,
  "model_score": 0.2861,
  "style_score": 0.5003,
  "label": "We think this was probably written by a person.",
  "sent": "s When i was in the collage I used to go to l…"
 },
 {
  "status": 200,
  "guess": "ai",
  "confidence": 0.72,
  "model_score": 0.7827,
  "style_score": 0.6574,
  "label": "This writing closely matches patterns … (AI label)",
  "sent": "Effective time management is important for su…"
 }
]
```

**Criterion 4: appeals** (`results/appeals_2026-11-22_2210_before.md`, produced by `run_appeals.py::run_trial`, trial 1):

```json
{
 "appeals (first 2 of 10, all 10 passed)": [
  {
   "content_id": "08c87851-d516-4b76-9c63-dc4cb540880e",
   "submit_status": 200,
   "appeal_status": 200,
   "appeal_response": {
    "content_id": "08c87851-d516-4b76-9c63-dc4cb540880e",
    "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
    "status": "under_review"
   },
   "appeal_entries_in_log": 1,
   "passed": true
  },
  {
   "content_id": "45d15d89-8522-404d-8f86-2fd34c1003b9",
   "submit_status": 200,
   "appeal_status": 200,
   "appeal_response": {
    "content_id": "45d15d89-8522-404d-8f86-2fd34c1003b9",
    "message": "Thanks. Your appeal has been recorded and a person will review this decision.",
    "status": "under_review"
   },
   "appeal_entries_in_log": 1,
   "passed": true
  }
 ],
 "made_up_id": {
  "status": 404,
  "response": {
   "error": "unknown_content_id",
   "message": "We couldn't find a submission with that content_id."
  },
  "log_entries_added": 0,
  "passed": true
 }
}
```

**Criterion 5: bad input, responses** (`results/run_2026-11-22_2210_before.md`, produced by `run_eval.py::main`, trial 1):

```json
[
 {
  "status": 400,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "sent": "{\"creator_id\": \"eval_bad_missing\"}…"
 },
 {
  "status": 400,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}…"
 },
 {
  "status": 400,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "sent": "(empty text)…"
 },
 {
  "status": 400,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "sent": "   \t  …"
 },
 {
  "status": 400,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "sent": "word word word word word word word word word …"
 }
]
```

**Criterion 5: bad input, log check** (`results/appeals_2026-11-22_2210_before.md`, produced by `run_appeals.py::run_trial`, trial 1):

```json
[
 {
  "sent": {
   "creator_id": "eval_bad_missing_appeals_t1"
  },
  "status": 400,
  "response": {
   "error": "missing_text",
   "message": "text is required."
  },
  "new_log_entries": [
   {
    "event": "rejected",
    "status": "rejected",
    "reason": "missing_text"
   }
  ],
  "passed": true
 },
 {
  "sent": {
   "text": null,
   "creator_id": "eval_bad_null_appeals_t1"
  },
  "status": 400,
  "response": {
   "error": "invalid_text",
   "message": "text must be a string."
  },
  "new_log_entries": [
   {
    "event": "rejected",
    "status": "rejected",
    "reason": "invalid_text"
   }
  ],
  "passed": true
 },
 {
  "…": "3 more, all passed"
 }
]
```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->

One missed criterion and 20 broken attacks come down to **three problems, all in signal two, the style signal**, plus one gap in the route and two smaller ones in signal one. The numbers below come from `style_parts` in the audit log, which records each style measure as 0–1 AI-likeness.

**Pattern A: one short sentence buys a "human" style score.** *(EV02, EV03, EV05, EV06, EV09, PI01, PI02, PI03: 8 broke)*
- **Stage:** signal two, then the combining rule.
- **Mechanism:** sentence-length spread is standard deviation ÷ mean, and it carries 0.75 of the style score. Its mapping hits "fully human" at a raw spread of 0.60. A single one-word sentence is enough to get there:
  - EV02 inserted "Really." after every sentence (lengths 11, **1**, 15, **1**, 10, **1** …), so spread went to 0.85.
  - EV06 used one 51-word sentence and one 1-word sentence, so spread went to 1.19.
  - EV09's "Right, so." opening, EV03's pasted quotation and EV05's human edit all did the same with less effort.
  - In PI01 and PI02, the injected lines ("Ignore all previous instructions.", "SYSTEM: …") are short sentences sitting on top of the AI paragraph, and the paragraph ends on a 1-word fragment. Both scored spread 0.00, fully human.
- **Why it beat the combining rule:** style went to 0.12–0.44 while the model sat at 0.46–0.70 on this AI text. My 50/50 average then landed between 0.20 and 0.61: "human" or "unsure".
- **On the prompt injections:** they "worked" without anything reading them. My service has no model that follows instructions. The injected lines are just odd, unpredictable short sentences, and that moved both statistical signals the same way an evasion would. PI02's fake "SYSTEM:" line also dragged the model score down to 0.20, because "guess=human, confidence=0.02" is very unlike normal English to GPT-2.

**Pattern B: no punctuation counted as evidence of AI.** *(FP02, FP03, FP04, FP05, and criterion 3: 4 broke + 1 missed)*
- **Stage:** signal two, then the combining rule and the label mapping.
- **Mechanism:** my punctuation measure gives 1.0 (fully AI) at ≤ 0.03 inner marks per word. All four false-positive texts sit at or below that (FP03: **0.00**, FP02: 0.013), so punctuation scored 1.0 for every one. Their sentences are also even, because careful, formal, rubric and technical writing is like that (raw spread 0.24–0.37), so spread scored 0.58–0.90 AI-like.
  - A report, a careful non-native writer, a rubric essay and a manual all have the shape my style signal calls AI.
  - Signal one agreed for the same reason it always does with plain, correct English (0.74–0.83).
- **Why the safeguards didn't apply:** both signals were above 0.5, so the agreement rule, built for exactly this writer, never fired. All four combined scores (0.76–0.83) cleared my 0.70 line.
- This is the blind spot I named in Milestone 1. The attack set found it in the cases where both signals share it.

**Pattern C: no words, scored as "AI".** *(MF04, MF05, MF06, MF07: 4 broke; MF03 broke the other way)*
- **Stage:** the route first, then signal two.
- **The route:** it accepts any string with 3+ GPT-2 tokens. It never asks whether the input is language.
- **Signal two:** `stylometry.words()` only matches `[a-z0-9']`. Emoji (MF06), Arabic (MF07) and punctuation-only text (MF04) produce **zero words**, and a 4,000-letter "aaaa…" (MF05) produces one.
  - With no words, `punctuation_density` returns 0.0, which my mapping reads as fully AI (1.0). "Couldn't measure" turned into "AI".
  - MF04 also slipped past my one-sentence guard: its four zero-word "sentences" counted as four sentences with a spread of 0, which reads as perfectly even, so AI.
- **Signal one** finds repeated emoji and repeated letters extremely predictable (0.997), so MF05–07 combined to 0.77–0.81, "AI".
- **MF03** (control characters) broke the other way: GPT-2 found the escape codes so surprising that the model score was 0.00, giving "human".
- **The worst case is MF07:** anyone writing in Arabic, Chinese or any non-Latin script gets "AI" for a reason unrelated to how they write.

**Two smaller ones in signal one.** *(EV01, EV08: 2 broke)*
- **EV01**, typos: misspellings like "poistioned" and "thsi" split into rare sub-word pieces. That raised perplexity, so the model score fell to 0.16. Other lightly changed versions of the same paragraph (EV03, EV04, EV07) kept the model at 0.59–0.67.
  - Style stayed AI-like (0.98), because my word-variety measure carries no weight, so typos couldn't move signal two at all.
  - The 50/50 average (0.57) landed in "unsure". The combining rule let one fooled signal cancel one correct signal.
- **EV08**, two sentences and 10 words: too little text for GPT-2 to find patterns in (model 0.25). My route only rejects texts under 3 tokens, so it was scored anyway and landed at 0.55, "unsure".

**EV07** (punctuation padding) is Pattern C's mirror image. It swapped full stops for "; and, moreover,", so my splitter saw one 97-word sentence. Spread fell back to neutral (0.5), and punctuation density hit 0.22, which reads as fully human. Style dropped to 0.38. **Stage:** signal two's sentence splitter and punctuation measure.

**Criterion 3, missed: my hand-edited AI paragraph got "ai" (0.72), not "unsure".**
- **Stage:** both signals, then the label mapping.
- **Mechanism:** my edits were word swaps ("essential" → "important", "Ultimately" → "Overall", "can" → "could") plus one deleted word. I re-scored the unedited original through the service:

  | Version | model | style | combined | sentence lengths |
  |---|---|---|---|---|
  | AI original | 0.7897 | 0.6506 | 0.7201 | 13, 15, 9, 17 |
  | My edit | 0.7827 | 0.6574 | 0.7200 | 13, 14, 9, 17 |

- **Why the edit changed nothing:** swapping one common word for another leaves GPT-2's predictability, the sentence lengths and the commas exactly where they were. Neither signal can see a light edit, so the text kept the AI score it started with, and 0.72 is above my 0.70 line.
- **What it means:** my criterion assumed "edited by hand" would read as borderline, but my signals only notice an edit that changes sentence shape. That's why EV05 (a heavy rewrite) went all the way to "human" while mine stayed "AI".
- **Not a revision:** the criterion was measurable, and I got a clear verdict from it. It's a miss, not a broken criterion, so it stays as written.

**The pattern across all of it:** signal two decides most outcomes, and its two main measures both fail the same way. It reads *sentence shape and punctuation*, which an attacker can change in seconds, which careful human writers naturally keep tidy, and which non-Latin scripts don't produce at all. Patterns A, B and C (17 of the 20 broken attacks, plus the criterion 3 miss) are one problem: signal two treats "even and unpunctuated" as AI and "uneven or punctuated" as human, regardless of what the words are.

**Were my targets too easy?**
- **Criteria 4 and 5** test plumbing: the appeal endpoint and input validation. They held 10/10 and 5/5 in every trial and were always likely to.
- **Criterion 1 passed, but on writing that turned out to be safe.** My pieces were casual, cited or reflective, and none of them looked like FP02–FP05. The attack set's careful, formal and technical human writing was called AI 4 times out of 8. My plain Patti Smith paragraph only escaped at 0.69, because the agreement cap held it 0.01 under the line.
- **The criterion I'd tighten is criterion 1:** require that 3 of the 10 pieces be formal or technical, my own report or instructions, not just "plain". That's where this service accuses real people.

No criterion is revised: all five could be measured and gave a clear verdict.

---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [x] criteria.md has five numbered criteria, each naming a target
       [x] Each has a reason underneath
       [x] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [x] Two signals that measure DIFFERENT things, each with a named blind spot
       [x] Three label variants, all reachable, written out in full
       [x] POST /appeal changes status and writes to the log
       [x] Signals and Scoring names scoring.py::combine_signals
       [x] Sample Run: a submission AND an appeal, as pasted text
       [x] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN
           https://github.com/Mehton/ai201-project4-provenance-guard-starter-v2026

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
