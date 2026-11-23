"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

# ── My own writing (criterion 1, and the human half of criteria 2 and 3) ─────
#
# Everything in these two lists is mine. Nothing here is AI text or copied
# from the web.

# Deliberately plain: short sentences, common words, little punctuation. The
# writer my Milestone 1 trace says this service is most likely to accuse.
MY_PLAIN_WRITING = [
    "When I was goping to college in my hometown. I used to study every day in the library. I miss the pizza place in the collage where I used to eat pizza with my friends.",
    "Patti Smith contributed to her group as a lyricist and a performer. She mostly sang her songs using a guitar on the stage. Patti Smith performed in the punk rock music genre.",
    "Some of the charts that are provided are a bit hard to read due to font sizes being too small and being pressed together. Explain the terms that are specific to chess that most normal people wouldn't understand. Overall, they had nice charts that told an interesting story.",
]

# The rest of my writing, in my usual voice.
MY_OTHER_WRITING = [
    "s When i was in the collage I used to go to library everyday. I miss going to pizza place and chatin with friends. how was your collage life",
    "Joan Armatrading first performed at a concert at Birmingham University at the age of sixteen.1 She sang “The Sound of Silence” a song by American singers Simon & Garfunkel. In 1985 she performed in sold-out concerts at the Red Rocks Amphitheater in Denver, and another concert in Arizona with Cook da Books.1 Her all-time hit albums are Me Myself, Walk Under Ladders, and The Key in both the UK and the US. “Armatrading has been nominated three times for a Grammy Award and twice for a Brit Award as best female vocalist. She received an Ivor Novello Award for the Outstanding Contemporary Song Collection in 1996. She has received honorary degrees from the Liverpool John Moores University",
    "Bryan and his group vis 12 have a dataset that is 16gbs and our critique to them is to filter the data down for each of the categories that they have. They don’t have their ten questions yet that are more specific to the categories that they have so they will need to develop the questions and then wrangle each data set they already filtered to the specific question.",
    "The team gave feedback about its deliverables when it was released. The team may find out if the deliverables' functionality and performance fulfill the requirements of the clients. Helping people realize that adding extra work that is not on the board contributes to the WIP and lengthens cycle time. It is conceivable that a Product Owner or team member does not understand how to slip features into small parts so a team can offer interim value. This indicates that the team has fewer ideas about its estimations and its potential completion date.",
    "Joan Anita Barbra Armatrading is a Kittitian-English singer-songwriter and guitarist. She was born on December 9, 1950 “in the town of Basseterre in what was then the British colony Saint Christopher and Nevis.” 1 Her family moved to Birmingham in England when she was three years old. Joan Armatrading had to drop out of school to support her family financially at the age of fifteen.",
    "Joan Armatrading did not mention anything about the dominance of whiteness in rock music; however, she did talk about male dominance in the music industry. She said in an interview, “I didn’t feel I had a struggle as such. Maybe I did, but I didn’t notice it.” She suspects it would have been harder if she’d needed someone else to write her songs.” 2",
    "Patti Smith was a poet and singer. She was a well-known poet before she formed the band named after her name “The Patti Smith Group” in 1974. (28). The club Country, Blues Grass, Blues also known as CBGB was the center of the “New York Punk” (Punk Rock) music genre, and The Patti Smith Group started their career in CBGB club. Patti Smith embraced gender non-conformity in her songs like “Gloria.” “Gloria for example is a song from a male point of view, and Smith embraced the discomfort or anger that listeners might experience when hearing the song performed by a woman.” (28).",
]

# ── AI-generated text (criteria 2 and 3) ─────────────────────────────────────
#
# Generated by Claude for this test, before any of these runs. Unedited.
AI_TEXTS = [
    "Effective time management is essential for success in both academic and professional settings. By prioritizing tasks, setting clear goals, and minimizing distractions, individuals can significantly improve their productivity. Additionally, regular breaks help maintain focus and prevent burnout. Ultimately, developing strong time management skills can lead to reduced stress and a better work-life balance.",
    "Climate change represents one of the most pressing challenges facing our planet today. Rising global temperatures are contributing to more frequent extreme weather events, rising sea levels, and disruptions to ecosystems. Addressing this issue requires coordinated action from governments, businesses, and individuals. By investing in renewable energy and sustainable practices, we can work toward a healthier future.",
    "Reading offers numerous benefits for personal growth and development. It expands vocabulary, improves concentration, and exposes readers to new ideas and perspectives. Furthermore, reading fiction has been shown to enhance empathy by allowing individuals to experience the world through the eyes of others. Incorporating regular reading into daily life can be a valuable habit.",
    "Remote work has transformed the modern workplace in significant ways. Employees now enjoy greater flexibility and the ability to work from virtually anywhere. However, this shift also presents challenges, such as maintaining clear communication and fostering a sense of team cohesion. Organizations that invest in the right tools and practices can successfully navigate these changes.",
    "Regular physical activity plays a crucial role in maintaining overall health and well-being. Exercise strengthens the cardiovascular system, supports healthy weight management, and boosts mental health by reducing symptoms of anxiety and depression. Experts recommend at least 150 minutes of moderate activity per week. Finding an enjoyable form of exercise can make it easier to stay consistent.",
]

# Criterion 3's borderline text: one of the AI texts above, edited by hand.
MY_EDITED_AI = "Effective time management is important for success in both academic and professional life. By prioritizing tasks, setting clear goals, and minimizing distractions, individuals can improve their productivity. Additionally, regular breaks help maintain focus and prevent burnout. Overall, developing strong time management skills could lead to reduced stress and a better work-life balance."


SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # 10 pieces: 3 plain + 7 others. Target: at most 1 of 10 gets "ai",
        # and none of the 3 plain ones does, in each of 3 trials.
        "texts": MY_PLAIN_WRITING + MY_OTHER_WRITING,
    },
    {
        "name": "score spread",
        "criterion": 2,
        # First 5 are mine (none plain), last 5 are AI. Target: median AI
        # confidence at least 0.30 above median human confidence, each trial.
        "texts": MY_OTHER_WRITING[:5] + AI_TEXTS,
    },
    {
        "name": "label coverage",
        "criterion": 3,
        # In order: should get "ai", "human", "unsure" — in every trial.
        "texts": [AI_TEXTS[1], MY_OTHER_WRITING[0], MY_EDITED_AI],
    },
    {
        "name": "bad input",
        "criterion": 5,
        # Every one must return 400 with an error code and no content_id.
        # run_appeals.py re-sends these to check no decision entry is logged.
        "bodies": [
            {"creator_id": "eval_bad_missing"},                       # text missing
            {"text": None, "creator_id": "eval_bad_null"},            # text null
            {"text": "", "creator_id": "eval_bad_empty"},             # text empty
            {"text": "   	  ", "creator_id": "eval_bad_whitespace"}, # whitespace only
            {"text": "word " * 2001, "creator_id": "eval_bad_huge"},   # 10,005 chars
        ],
    },
    # Criterion 4 (appeals) can't be tested by sending text to /submit alone,
    # so it lives in run_appeals.py, which submits, appeals, and reads /log.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
