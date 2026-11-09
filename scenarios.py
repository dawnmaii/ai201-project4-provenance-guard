"""
`run_eval.py` runs everything here three times.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            "Unlike most Vietnamese immigrant families who are eager to assimilate into American culture via the latest trends and social events, my family eagerly clings on to the traditional Vietnamese way of life. They raised me as if we had never left Vietnam: no Netflix, no phones, and strict curfews. Growing up, I didn’t know what the YMCA was or even how to use a microwave. Things that every other American and even Asian-Americans knew.",
            "I will be moving out of the property at the latest by 11/01/2022. As of the day this letter was composed, I do not expect nor ask that the security deposit to be returned to me. If it can be returned to me, however, please reach out to me using the contact information above to discuss how it can be forwarded.",
            "To put this into perspective, I’ll use my position as a tutor at my school’s writing center, where I volunteered weekly. Tutors refer to students as “clients,” who come to the writing center to either find a place to work or seek help with their writing assignments (most commonly for English). Often when I work with clients, they tell me the concerns they have with their essay, their frustration about why the teacher gave them a certain grade for their paper, or their exhaustion from writer’s block. These are the “problems” that I’m expected to help them solve by telling them what to do. However, my goal is to help clients improve their writing while retaining their voice. So instead, I assist them in finding the errors for themselves by asking them questions about the assignment, encouraging them to clarify their writing, and guiding them in solidifying the ideas they’re trying to convey.",
            "Sexuality and gender identity were things I did not grasp nor was willing to learn about until high school. Wanting a healthy relationship with my parents, I started to agree with their conservative and traditional opinions about the queer community at a young age–that it wasn’t ok to be queer, it’s not normal and it’s against nature, that they were dangerous. Obviously, I entered high school homophobic and pretty ignorant about anything non-cishet. This was true until I met a friend who helped me navigate my first year. She was basically my only friend (I was pretty introverted and not as social), and she gave me many helpful pointers and companionship. Halfway through the school year, she came out to me as pansexual. I had no idea what that was. I only knew the terms “lesbian” and “gay” to describe the queer community at that point in time, so I asked for an explanation of what pansexual meant. She defined it as the fact that she could be attracted to anyone, regardless of any aspect of their identity. As long as their personality was compatible with hers, she was open to a romantic relationship with them. That didn’t mean, however, that she was willing to settle with anyone and had no standards (a popular misconception of the pansexual community).",
            "My biggest hope for my college experience at UW (as mentioned in the prompt above) is actually my greatest concern. I’m concerned that I won’t be able to find a community that “clicks” with me and accepts me for who I am, despite my efforts to actively find one. The decision to attend UW was one that was carefully thought out. College is what one makes of it, and UW was no exception. If anything, the size of campus and the abundance of resources make the challenge of finding connections even greater, and I understood how one can get lost in it all. But I’m not afraid of putting in the work. In the past, I’ve attended events and programs at UW such as Rising SEAS and YEOC, and they’ve paved the way for greater opportunities and a stronger sense of community. If I didn’t take advantage of those opportunities, I wouldn’t have felt as strongly for UW as I do now nor as excited about what the future has in store for me. Being fully committed for the next four years, I know that if I want to find a community at UW, I have to work for it. Which I don’t mind. I just hope that my efforts won’t be in vain. And I don’t think they will be. It’s just a matter of getting out of my comfort zone more often.",
            "I’d like to start this reflection by talking about my involvement with a cultural RSO on campus: the Vietnamese Student Association (VSA). The past three years I thought that I was obligated to join and stay involved in VSA whenever I could, as someone who identifies as Vietnamese. I was supposed to belong in that space. Yet I felt ostracized in the scenes VSA immersed me in. Watching the main character in the video “American male” (Rohrbaugh, 2016) was a huge mirror for me. I witnessed similar roles being followed in VSA with similar props: guys in dark colors that work out on a regular basis; girls in straight-leg jeans and skin-tight tops with oversized jackets in pastel colors; everyone invested in skincare and natural makeup and insane false eyelashes; also everyone getting together mainly to rave or pregame or get hyped up for the latest concerts from artists such as Keshi and Illenium; everyone somehow having the same pre-cut tone of voice and texting style–“lol”, “idk”, “bruh”, “omg”, *read*–people holding kandi, boba, a dab pen, or a red solo cup in every photo, or being decorated in black, sheer, and skimpy clothing with Instagram captions along the lines of “found my family!!! take me back <3.”",
            "The children’s book “A Different Pond” (Phi & Bui, 2017) honestly brought me to tears; it reminded me of how my mother would harvest watercress at a nearby (public) creek for soup near the end of the day (I remember being scared of being arrested for this, but fortunately no one picked on her for it) or eating that exact fried fish for dinner with fish sauce. My main fear when I was younger was not of the dark or monsters under my bed; it was of being homeless and having no money for a roof over my head (I was aware that I could not do anything about it). I think our apartment looking different from the typical American houses of the friends we visited–bare bulbs, stuff hoarded around “just in case”, old furniture and clothes collected from the garbage dump to reuse–highlighted that difference.",
            "Hi Dad, It’s been a while since I last saw you. I know we don’t speak as much as we used to, and last time we were in touch it wasn’t pretty. I wanted to take some time today to talk about how you influenced my life. I also just wanted to have the conversation about my life that we never got to really have in the past. There’s a lot to say, but I will focus on a couple of key moments.",
            "Walker stereotypes speakers of the Brooklyn accent as very blunt and casual. Compared to most accents that start with “hi” or “hello” or a “how are you doing”, she instead says, “What? ‘Cause I’m doing the thing. Sorry.” before introducing herself. Her facial expressions also indicate a bit of impatience, as if speakers of this language all hate to be interrupted but are in general polite (in a mean way) and are constantly pressed for time. I don’t think it’s an accurate representation of people that do live in Brooklyn; not everyone is that mean or blunt by default. It’s probably an exaggerated portrayal inspired by popular media, such as TV shows that are set in Brooklyn.",
            "Taking classes abroad with a lot of flexibility would give me the opportunity to focus on creating special memories, learn to take care of myself physically and emotionally as a young adult today, and confidently taking charge of my education by doing what works best for me. In this case, I believe a change of academic atmosphere and the ability to be completely independent without a predetermined structure is what I need to maximize my education in CS as a minority. I want to be an advocate for my own education and speak up about my concerns and needs for my academic future. I’m aware of my struggles and I’ve given them enough thought to know how to address them in the most effective way possible. Although study abroad is not the answer to the problems I currently face, it is a creative solution and challenge I am more than willing to take on, and I’m looking forward to where it will take me",
        ],
    },
    {
        "name": "score spread",
        "criterion": 2,
        "texts": [
            "Remote work has changed how many organizations think about productivity. It allows employees to set schedules that suit their lives, and it removes the commute for many workers. However, it also introduces challenges around communication and team cohesion. Successful remote teams tend to rely on clear documentation and regular check-ins. Ultimately, the right balance depends on the nature of the work and the needs of the people doing it.",
            "Water conservation is an important part of managing shared resources. Households can reduce consumption by fixing leaks, using efficient fixtures, and watering gardens at appropriate times. Communities benefit when these practices are supported by clear information and reasonable incentives. Long-term planning also plays a role, particularly in regions facing drought. By working together, individuals and institutions can make meaningful progress.",
            "Learning a second language requires consistent practice and patience. Regular exposure to the language, through conversation, reading, and listening, helps build vocabulary and fluency. Learners often benefit from setting specific goals and tracking their progress over time. Mistakes are a natural part of the process and can provide valuable feedback. With sustained effort, most people can reach a functional level of proficiency.",
            "First full week of work in the office! I met my peers in the cohort as well as those in earlier cohorts that I befriended much more quickly. After this week I'll try to live more frugally to get that credit card debt paid off. The reimbursement process sucks. Other than that I'm happy to be making big girl money at last",
            "Still a hard week but nevertheless rewarding; I met many more new people (and cats)! Am starting to establish some semblance of a routine but I know that will change again when I come to the office next week and get my first paycheck. Hopefully my studies go smoothly.",
            "I like to think of letter writing as sending a message to space, looking forward to a sign of life that's just as intellectual as mine and learning about their way of life on the same planet. It's nice to know that I am not so different and worthy of good surprises.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            "Urban gardens offer more than fresh produce. They give residents a shared space to meet neighbors, and they can help cool dense neighborhoods during hot summers. Maintaining a garden does require time, tools, and access to water, which can limit who participates. Many cities address this by offering plots at low cost and providing training for new gardeners. When these programs are well run, they strengthen community ties in lasting ways.",
            "Sleep plays a central role in memory and learning. During rest, the brain consolidates experiences from the day and strengthens the connections that matter most. Consistent sleep schedules tend to improve both mood and concentration. Limiting screens in the hour before bed is one common recommendation, since bright light can delay the onset of sleep. Small, steady habits often make a larger difference than occasional efforts.",
            "Public libraries have adapted well to a changing information landscape. Beyond lending books, many now offer digital catalogs, computer access, and workshops on topics ranging from job applications to financial planning. These services are especially valuable for people without reliable internet at home. Libraries also serve as quiet places for study and reflection. Their continued success depends on steady funding and strong partnerships with local organizations.",
            "Public libraries have always been an information hub. They offer digital catalogs, computer access, and workshops on topics ranging from job applications to financial planning, all which are valuable for people without reliable internet at home or cannot afford resources otherwise. Their continued success depends on steady funding and strong partnerships with local organizations.",
            "Urban gardens offer residents a shared space to meet neighbors and cool dense neighborhoods during hot summers. Maintaining a garden requires time, tools, and consistent access to water, which can limit who participates. This concern is addressed in many cities by offering plots at low cost and providing training for new gardeners.",
            "On Friday I bought tissue culture of a monstera albo from a local plant shop. Basically a lab-grown cutting mixed with god-knows-what. It was $25, but in theory if I can pull this off and it grows successfully in my apartment, I get a $200+ value plant for $25. The monstera albo is such a pretty plant to have and I need its variegation in my apartment.",
            "The things I need left in order to have people over my apartment are: a sofa bed, a coffee table, an extra rollaway bed, four bath towel sets of varying colors, a vacuum, four blankets, and four pillows. I hope to get the viral products from Tiktok that make a place super aesthetic. I also need to cook more. That all requires money. Ugh.",
            "Should I foster a cat? Pet fee is $250, followed by $30 a month. I would like to use my own litterbox because I don't want the foster cat to stink up my apartment. Then again, I'm scared what my family will think (even though they don't live with me anymore). Fostering is significantly cheaper than adopting because I don't have to pay for supplies or vet appointments. I'll get my own litterbox for free, scouring off Facebook Marketplace right now. All I need to do is pay $15 a month if my boyfriend agrees to help me pay half the pet rent. And if my coworkers continue to pay me for gas and groceries, I'm basically set.",
        ],
    },

    # Criterion 4 (appeals) isn't in this file. Test it by hand; see the README.
    
    {
        "name": "bad input",
        "criterion": 5,
        # Six bad-input requests run here, all to /submit. The other two — invalid
        # JSON and the 404 for an unknown content_id — are sent by hand, because
        # a bodies entry must be a dict and the 404 goes to /appeal.
        "bodies": [
            {"text": "Hello there."},                                      # no creator_id
            {"creator_id": "eval_bad_missing_text"},                      # no text field
            {"text": "", "creator_id": "eval_bad_empty"},                 # empty text
            {"text": "   ", "creator_id": "eval_bad_blank"},              # whitespace only
            {"text": "word " * 700, "creator_id": "eval_bad_long"},       # over 3,000 characters
            {"text": "Hello there.", "creator_id": "   "},                 # blank creator_id
        ],
    },
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
