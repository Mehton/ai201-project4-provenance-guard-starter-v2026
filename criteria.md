# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. _"The
detector is accurate"_ is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. _"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"_ is a criterion.

Under each, write a sentence or two on **why that target**. _"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"_ is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area            | A question it could answer                                    |
| --------------- | ------------------------------------------------------------- |
| False positives | How often may a human's writing get called AI?                |
| Score spread    | How far apart should clearly-AI and clearly-human text score? |
| Label coverage  | Is every one of your three labels actually reachable?         |
| The appeal path | Does an appeal always change status and always get recorded?  |
| Bad input       | What happens when `text` is missing, empty, or enormous?      |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---

## 1. My own writing is rarely called AI, and plain writing never is

Given 10 pieces I wrote myself, at least 3 of them deliberately plain and simple sentences, at most 1 of the 10 gets `guess: "ai"` and none of the 3 plain pieces does in each of 3 of 3 trials.

**Why this target:**

My Milestone 1 trace showed that plain writing is where both signals go wrong
together, so the writer most likely to be falsely accused is someone writing
simply, such as a second-language writer. A wrong accusation costs that person
far more than a missed detection costs the site. I allow one miss across all 10
because the model's score can vary, but none for the plain pieces because that
is the person this service is most likely to hurt.

---

## 2. Clearly-AI and clearly-human text score far apart

Given 5 of my own pieces from criterion 1 (none of the plain ones) and 5 AI texts I generate before building the service, the median `confidence` of the AI set is at least 0.30 higher than the median `confidence` of the human set in each of 3 of 3 trials.

**Why this target:**

My unsure band is between 0.35 and 0.65, which is 0.30 wide. A smaller gap would let both medians land inside "unsure", so the score would separate nothing a reader could actually see. A gap of 0.30 shows the score is useful for telling these groups apart, without pretending one score proves who wrote a piece.

---

## 3. All three labels are reachable

Given 3 texts picked before building (one clearly AI-generated, one clearly human-written, and one borderline: AI text I edited by hand), each text gets its intended label (`"ai"`, `"human"`, and `"unsure"` respectively) in each of 3 of 3 trials.

**Why this target:**

A label that no score can reach is dead code, and a reader should never be stuck with only two options. The unsure label is what lets the system avoid an overconfident call, so it has to actually show up for a text that really is mixed.

---

## 4. Every appeal is recorded and moves the item to review

Given 10 appeals on real `content_id`s, all 10 return HTTP 200 with `status: "under_review"` and add an appeal entry with the same `content_id` to `/log`. Given an appeal on a made-up `content_id`, the service returns 404 and adds nothing to the log in 10 of 10 tries, plus the 404 case.

**Why this target:**

An appeal is the only remedy a falsely accused writer has. If even one is lost, that writer is left with a wrong label and no record that they ever objected, so anything less than 10 of 10 is a failure. The 404 case matters because a typo that fails silently looks like a working appeal to the writer.

---

## 5. Bad input is rejected clearly, not crashed on

Given these 5 request bodies (`text` missing, `text` null, `text` empty, `text` whitespace-only, and `text` longer than 10,000 characters), the service returns HTTP 400 with a JSON body containing an `error` code, and returns no `content_id` and writes no decision entry in 5 of 5 cases. A `rejected` log entry is expected, so there is a trace.

**Why this target:**

Crashing on malformed input is one of the most common real failures. Rejecting unusable input clearly avoids confusing scores and wasted model work. The 10,000 character limit makes "enormous" testable, and logging rejections means an attack that only shows up as rejected requests can still be found.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
