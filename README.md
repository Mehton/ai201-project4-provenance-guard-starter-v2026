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

**My limits:** **_ per minute, _** per day

**Why those numbers and not others:**

<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
| --------- | ------ | ----- | ----- | ----- | ------- |
| 1.        |        |       |       |       |         |
| 2.        |        |       |       |       |         |
| 3.        |        |       |       |       |         |
| 4.        |        |       |       |       |         |
| 5.        |        |       |       |       |         |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

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
