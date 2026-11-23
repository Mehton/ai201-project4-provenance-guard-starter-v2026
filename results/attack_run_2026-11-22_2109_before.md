# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-22 21:09
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `cdfa88c8-fb19-4414-9bbc-c705eb001d87` | unsure | 0.571 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `bf10e250-655d-4f5d-96ff-8d62b77960f8` | unsure | 0.416 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `4a7f9842-2a49-4732-88eb-b254846d9b81` | unsure | 0.530 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `76ce148e-8fef-4c0c-a85a-7ed419aee8f4` | ai | 0.795 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `db31acdd-a60f-4091-b69e-150b13d5609c` | human | 0.221 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `b8167c37-055b-4831-8de9-157327e09b42` | unsure | 0.406 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `404a10cc-b0e3-4792-9625-ab1bd5214abc` | unsure | 0.481 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `1438884b-92f2-49bb-9f2f-9935b71aebba` | unsure | 0.545 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `011422d2-f073-4db2-aef1-e98a0a253d37` | unsure | 0.570 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `f1f02b04-b9a1-4bda-9388-b7b20f49d014` | ai | 0.808 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `6be165da-83b9-4731-9ff4-2ff182ac6d45` | unsure | 0.567 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `7656c500-c05e-4c29-a124-bed582bc0a21` | ai | 0.832 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `916936f7-2308-4cab-88f4-24fcd6c6d462` | ai | 0.782 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `6e789145-4227-4335-a34e-a0cd6808f30d` | ai | 0.760 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `0dafc97d-1116-440f-9b8d-9c661a57b769` | ai | 0.828 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `55b41a08-8a72-483b-99c9-072f374a16d7` | unsure | 0.641 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `78e61bb8-59d3-4d71-a7aa-ad434fad403d` | unsure | 0.558 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `c357dc1d-2c35-4a30-b72f-46b5e273f2d8` | unsure | 0.443 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `59d88dd1-83c6-4524-8d37-8370ddab0f9b` | human | 0.356 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `1322152d-4700-4bf7-a831-3f3b30012485` | human | 0.197 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `5fbc5ece-8762-48fe-bfe1-53aa42bbfe7d` | unsure | 0.612 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `8bbd7ca4-0a71-4d6a-8f96-9a0389ead95e` | unsure | 0.465 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `eb1e92cb-545d-4898-a786-a8a282a59db6` | unsure | 0.441 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `006f6862-81c0-40ad-8978-375e0b55b501` | unsure | 0.549 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `8701b18a-852b-4ab8-a830-0dad443b0809` | human | 0.188 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `3e22057b-fcb2-4980-9037-01abe4448f85` | unsure | 0.506 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `568a06e9-f834-466d-9dc0-069592eecb8c` | ai | 0.811 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `e9fdfe4a-acc5-4ace-8525-0fc8938ffa66` | ai | 0.811 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `bce2d1d6-960f-4618-9361-0b65ba7061b4` | ai | 0.766 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4ad70d13-2b61-49fc-841b-eb97319fbe45` | human | 0.327 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0bc333cc-5cd5-41f6-b19d-9e50697ac4a3` | human | 0.327 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3a83f430-8a4f-4d13-8074-6322b7fd75b8` | human | 0.327 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5ca6ff0b-fae1-466f-9c2d-7458228e283a` | human | 0.327 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1bd125e7-c126-4645-9952-455e367851f7` | human | 0.327 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "cdfa88c8-fb19-4414-9bbc-c705eb001d87",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.5707,
  "model_score": 0.1635,
  "style_score": 0.9779,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "bf10e250-655d-4f5d-96ff-8d62b77960f8",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4159,
  "model_score": 0.5943,
  "style_score": 0.2375,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "4a7f9842-2a49-4732-88eb-b254846d9b81",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5299,
  "model_score": 0.6662,
  "style_score": 0.3936,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "76ce148e-8fef-4c0c-a85a-7ed419aee8f4",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.7955,
  "model_score": 0.6114,
  "style_score": 0.9796,
  "label": "This writing closely matches patterns we often see in AI-generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "db31acdd-a60f-4091-b69e-150b13d5609c",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.221,
  "model_score": 0.3212,
  "style_score": 0.1208,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "b8167c37-055b-4831-8de9-157327e09b42",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4059,
  "model_score": 0.5727,
  "style_score": 0.2392,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "404a10cc-b0e3-4792-9625-ab1bd5214abc",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4806,
  "model_score": 0.5862,
  "style_score": 0.375,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "1438884b-92f2-49bb-9f2f-9935b71aebba",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.545,
  "model_score": 0.2452,
  "style_score": 0.8448,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "011422d2-f073-4db2-aef1-e98a0a253d37",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5701,
  "model_score": 0.7042,
  "style_score": 0.4359,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "f1f02b04-b9a1-4bda-9388-b7b20f49d014",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8078,
  "model_score": 0.9792,
  "style_score": 0.6365,
  "label": "This writing closely matches patterns we often see in AI-generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "6be165da-83b9-4731-9ff4-2ff182ac6d45",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5673,
  "model_score": 0.6175,
  "style_score": 0.5171,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "7656c500-c05e-4c29-a124-bed582bc0a21",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.8316,
  "model_score": 0.7387,
  "style_score": 0.9244,
  "label": "This writing closely matches patterns we often see in AI-generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "916936f7-2308-4cab-88f4-24fcd6c6d462",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7824,
  "model_score": 0.8051,
  "style_score": 0.7596,
  "label": "This writing closely matches patterns we often see in AI-generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "6e789145-4227-4335-a34e-a0cd6808f30d",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7601,
  "model_score": 0.8329,
  "style_score": 0.6874,
  "label": "This writing closely matches patterns we often see in AI-generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "0dafc97d-1116-440f-9b8d-9c661a57b769",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.8281,
  "model_score": 0.8005,
  "style_score": 0.8558,
  "label": "This writing closely matches patterns we often see in AI-generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "55b41a08-8a72-483b-99c9-072f374a16d7",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6414,
  "model_score": 0.8814,
  "style_score": 0.4015,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "78e61bb8-59d3-4d71-a7aa-ad434fad403d",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5577,
  "model_score": 0.8816,
  "style_score": 0.2338,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "c357dc1d-2c35-4a30-b72f-46b5e273f2d8",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4427,
  "model_score": 0.3223,
  "style_score": 0.5631,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "59d88dd1-83c6-4524-8d37-8370ddab0f9b",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3563,
  "model_score": 0.4625,
  "style_score": 0.25,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "1322152d-4700-4bf7-a831-3f3b30012485",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1972,
  "model_score": 0.2044,
  "style_score": 0.19,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "5fbc5ece-8762-48fe-bfe1-53aa42bbfe7d",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.6119,
  "model_score": 0.5943,
  "style_score": 0.6296,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "8bbd7ca4-0a71-4d6a-8f96-9a0389ead95e",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4647,
  "model_score": 0.4998,
  "style_score": 0.4295,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "eb1e92cb-545d-4898-a786-a8a282a59db6",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4406,
  "model_score": 0.6401,
  "style_score": 0.2411,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "006f6862-81c0-40ad-8978-375e0b55b501",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5491,
  "model_score": 0.5583,
  "style_score": 0.5399,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "8701b18a-852b-4ab8-a830-0dad443b0809",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.1875,
  "model_score": 0.0,
  "style_score": 0.375,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "3e22057b-fcb2-4980-9037-01abe4448f85",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5056,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or with help from AI. Our checks gave mixed results, which happens often with real writing, so we are not flagging it.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "568a06e9-f834-466d-9dc0-069592eecb8c",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8113,
  "model_score": 0.9976,
  "style_score": 0.625,
  "label": "This writing closely matches patterns we often see in AI-generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "e9fdfe4a-acc5-4ace-8525-0fc8938ffa66",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.811,
  "model_score": 0.9969,
  "style_score": 0.625,
  "label": "This writing closely matches patterns we often see in AI-generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "bce2d1d6-960f-4618-9361-0b65ba7061b4",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.7657,
  "model_score": 0.9064,
  "style_score": 0.625,
  "label": "This writing closely matches patterns we often see in AI-generated text. This is an automated estimate, not proof, and it can be wrong. If you wrote this yourself, you can appeal and a person will review it.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "4ad70d13-2b61-49fc-841b-eb97319fbe45",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3268,
  "model_score": 0.0287,
  "style_score": 0.625,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "0bc333cc-5cd5-41f6-b19d-9e50697ac4a3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3268,
  "model_score": 0.0287,
  "style_score": 0.625,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "3a83f430-8a4f-4d13-8074-6322b7fd75b8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3268,
  "model_score": 0.0287,
  "style_score": 0.625,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "5ca6ff0b-fae1-466f-9c2d-7458228e283a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3268,
  "model_score": 0.0287,
  "style_score": 0.625,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "1bd125e7-c126-4645-9952-455e367851f7",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3268,
  "model_score": 0.0287,
  "style_score": 0.625,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
