"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics

# Words per window for the moving-average type-token ratio.
TTR_WINDOW = 40

# Everything but the full stop: commas, semicolons, colons, dashes, brackets,
# quotes, question and exclamation marks. A run of dots ("...") counts once.
PUNCTUATION = r"\.\.\.|…|[,;:!?()\[\]\"“”—–]|(?<=\s)-(?=\s)|--"

# How much each measure counts toward style_signal. See style_signal for why
# the type-token ratio gets nothing.
STYLE_WEIGHTS = {"spread": 0.75, "punctuation": 0.25, "ttr": 0.0}


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies.

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.

    My choice: standard deviation of sentence lengths (in words) divided by the
    mean — the coefficient of variation. 0.0 means every sentence is the same
    length; higher means lumpier, more human. Fewer than two sentences returns
    0.0, and `style_signal` treats that as "no evidence" rather than as AI.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    return round(statistics.stdev(lengths) / statistics.mean(lengths), 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words.

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.

    My fix for that: a moving-average TTR. Take every window of 40 words, work
    out unique/total inside each, and average. A 60-word and a 600-word text
    are then measured on the same footing. Shorter than one window, it's the
    plain ratio.
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    window = TTR_WINDOW
    if len(tokens) <= window:
        return round(len(set(tokens)) / len(tokens), 4)
    ratios = [
        len(set(tokens[i:i + window])) / window
        for i in range(len(tokens) - window + 1)
    ]
    return round(statistics.mean(ratios), 4)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length.

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.

    My choice: every mark except the full stop, per word. Full stops only
    count sentences, which the spread already sees. Higher means more
    punctuation in the middle of sentences.
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    marks = re.findall(PUNCTUATION, text)
    return round(len(marks) / len(tokens), 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.

    My rule: each measure is mapped onto 0–1 "AI-likeness" with a straight
    line between two anchor values I read off my calibration texts, then the
    three are averaged with STYLE_WEIGHTS.

      spread       0.20 or below -> 1.0 (AI),  0.60 or above -> 0.0 (human)
      punctuation  0.03 or below -> 1.0 (AI),  0.09 or above -> 0.0 (human)
      ttr          weight 0 — on my calibration texts it pointed the wrong
                   way (AI text had the MOST varied vocabulary, plain human
                   writing the least), so it is measured and logged but not
                   scored.

    Fewer than two sentences means the spread has nothing to measure, so it
    counts as 0.5 — no evidence either way — instead of as perfectly even.
    """
    parts = style_parts(text)
    score = sum(STYLE_WEIGHTS[name] * parts[name] for name in STYLE_WEIGHTS)
    return round(min(max(score, 0.0), 1.0), 4)


def _ai_likeness(value: float, ai_at: float, human_at: float) -> float:
    """Straight line from ai_at (1.0) to human_at (0.0), clipped to 0–1."""
    scaled = (human_at - value) / (human_at - ai_at)
    return min(max(scaled, 0.0), 1.0)


def style_parts(text: str) -> dict:
    """Each measure as 0–1 AI-likeness, before weighting. Handy for diagnosis."""
    if len(sentences(text)) < 2:
        spread = 0.5
    else:
        spread = _ai_likeness(sentence_length_spread(text), ai_at=0.20, human_at=0.60)
    return {
        "spread": round(spread, 4),
        "punctuation": round(_ai_likeness(punctuation_density(text), ai_at=0.03, human_at=0.09), 4),
        "ttr": round(_ai_likeness(type_token_ratio(text), ai_at=0.60, human_at=0.85), 4),
    }


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"as AI-likeness           {style_parts(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
