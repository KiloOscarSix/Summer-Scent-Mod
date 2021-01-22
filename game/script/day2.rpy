

label day2start:

    scene black with dissolve
    with Pause(2)
    show text "Day 2 - Sunday" with dissolve
    with Pause(2)
    show text "The morning" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(2)

    if ep1mcsofasleep == True:
        show ep1px0060 with dissolve
    else:
        show ep1px0059 with dissolve

    off "I have no idea what time it is."
    off "I can smell the perfume of fresh-brewed coffee emanating from the kitchen."
    off "Let's see if I can grab a mug of that."
    scene ep2_sc1_m_k_1
    off "Pfewwww. Isn't that a pretty nice view?"
    off "You can't have enough of that ass."
    hide ep2_sc1_m_k_1
    show ep2_sc1_m_k_2
    off "Ok. New day, new occasions to shine."
    off "Don't be an idiot. Be a man. You can do it, [mc_name]. You can do it."
    mc "Hello, [sf_name]."
    hide ep2_sc1_m_k_2
    show ep2_sc1_m_k_3
    sf "Hi [mc_name]! How are you?"
    mc "I'm fine, thank you. What about you? How was the night?"
    if ep1mcsofasleep == True:
        sf "I slept ok. Your bed is very comfortable."
        sf "It was very nice of you. I must thank you for your gallantry."
        mc "You don't have to thank me. It was my pleasure."
    else:
        sf "I slept on the sofa but it was ok, it was pretty comfortable."
        mc "Ok... aren't you suppose to share [sis_name]'s bed?"
        sf "I am, yes, but in her condition... I thought it would be safer for me and better for her if I slept in the living room."
        mc "Well... I can understand that."

    sf "I'm sorry for my attire, I thought that everyone was still sleeping."
    mc "No need to be sorry. I'm also in my underwear in case you didn't notice..."
    mc "We already saw each other in a swimsuit, which often cover less skin so... I don't think there's a problem here."
    sf "I guess you're right."

    sf "Do you like coffee? I took the liberty to make some."
    mc "I do like coffee. And by the smell of it, I'm already sure I'll like yours."
    sf "Well, I hope so. What about a decent breakfast?"
    sf "I am by no means a chef but I can cook some bacon and eggs. Would that be alright?"

    hide ep2_sc1_m_k_3
    show ep2_sc1_m_k_4

    menu:
        "That's not what I'm used to but it will do just fine.":
            sf "I'll do my best."
        "My favorite breakfast. That will be perfect. [sfLovePath]":

            $ ProcessStat(1, "sf_affection")
            $ DumpNotStack()
            sf "I'll do my best."

    mc "But you don't have to do that [sf_name], you're not here to cook for us."
    sf "I'm not here to freeload either. I'll do my share and I'm happy with it."
    mc "Ok then."
    mc "So, what are your plans for the day?"
    sf "It's Sunday and Sunday is running day."
    sf "Other than that, we didn't plan anything. We'll probably just hang out by the pool."
    mc "You're running with [sis_name] every Sunday morning?"
    sf "More precisely, she runs and I try to follow her."
    sf "Even with a hangover, she's tougher and faster."
    sf "I don't know how she does that."
    hide ep2_sc1_m_k_4
    label galleryScene3:
    show ep2_sc1_m_k_4_closer
    off "With such an ass, it was obvious that she was exercising regularly."
    off "Holy Mother of God, look at these buttocks."
    off "It looks firm but not hard."
    menu:
        "Check her ass [blue]\[Recommended\]":
            $ ep2sfchecked = True
            hide ep2_sc1_m_k_4_closer
            show ep2_sc1_m_k_4_even_closer
            $ UnlockThat("ep2/ep2_sc1_m_k_4_even_closer")
            off "Its form is perfect, like designed by some lustful divinity."
            off "If only I could..."
            off "I would... using my tongue..."
            hide ep2_sc1_m_k_4_even_closer
            show ep2_sc1_m_k_5_closer
            $ UnlockThat("ep2/ep2_sc1_m_k_5_closer")
            off "And that pussy..."
            off "I'm sure it's tight and just rightly moist."
            off "I would lick it until she begs for mercy."
            hide ep2_sc1_m_k_5_closer
            show ep2_sc1_m_k_5
            off "Shit. Did she just catch me looking at her ass?"
            off "She sounds... angry..."

            $ ProcessStat(-1, "sf_affection")
            $ DumpNotStack()
            sf "Were you checking out my ass?"
            off "What can I say? Can I even save my ass in this situation?"
            off "I fucked up again. My mind is going blank."
            hide ep2_sc1_m_k_5
            show ep2_sc1_m_k_7
            off "Focus, [mc_name]. Focus!"
            menu:
                "I was. Sorry about that. [sfLovePath]":
                    hide ep2_sc1_m_k_7
                    show ep2_sc1_m_k_10
                    sf "Well, at least you're honest about it."
                    sf "Are you sorry for having looked at my ass so rudely or for having been caught?"
                    menu:
                        "I'm sorry I looked at your ass like I did.":
                            sf "And I do not believe you."
                        "For having been caught, of course.":
                            sf "You are an asshole."
                        "A bit of both. [sfLovePath]":

                            $ ProcessStat(1, "sf_affection")
                            $ DumpNotStack()
                            mc "I'm sorry, it was rude of me, but I must say that the show truly is spectacular."
                            off "She stays silent for a handful of seconds."
                "No, I wasn't...":


                    $ ProcessStat(-1, "sf_affection")
                    $ DumpNotStack()
                    sf "And you are a liar on top of that."
                    sf "At least be brave and admit what you did."

            sf "[mc_name], I'm very disappointed."
            sf "I thought you were a nice guy but it looks like I was very wrong about you."
            hide ep2_sc1_m_k_10
            show ep2_sc1_m_k_8
            off "Fuck, I want to look at her boobs so much..."
            off "No no no no. Don't look at her boobs. It's suicide."
            off "You already know her boobs are great, don't check them out. Don't do it!"

            menu:
                "Look at her boobs.":

                    $ ProcessStat(-1, "sf_affection")
                    $ DumpNotStack()
                    hide ep2_sc1_m_k_8
                    show ep2_sc1_m_k_8_closer
                    $ UnlockThat("ep2/ep2_sc1_m_k_8_closer")
                    off "Damn it."
                    sf "I can't believe it."
                    hide ep2_sc1_m_k_8_closer
                    show ep2_sc1_m_k_9
                    mc "I'm sorry, [sf_name]. I can't control myself. I'm so sorry."
                    mc "Steve put these ideas in my brain yesterday, and despite my efforts to get rid of it I keep thinking about... it.. and ... I'm sorry really."
                    sf "What are you talking about? You had a conversation with Steve?"
                    sf "About my ass and my breasts? How is it suppose to excuse you?"
                    mc "It wasn't about your ass, nor your breasts. It was a more general topic of conversation..."
                    mc "You're right, I have no excuses."
                    hide ep2_sc1_m_k_9
                    show ep2_sc1_m_k_11
                    sf "I'm so angry at you that I could slap you."
                    sf "But there's something important I need to talk to you about."
                    sf "You're gonna seat at the table and await your breakfast."
                    sf "Disrespect me again and I will spank you so hard you won't be able to sit for a week. Do you understand?"
                    mc "I do."
                    off "It's like I've just been scolded by my mother. She's right, I really am a moron."
                    $ ep2sfangryness="light"
                    $ ep2sfknowsteve=True
                "It's your fault.":

                    mc "You are so sexy that I didn't have a choice."
                    mc "I was mesmerized by your ass."

                    $ ProcessStat(-1, "sf_affection")
                    $ DumpNotStack()
                    hide ep2_sc1_m_k_8
                    show ep2_sc1_m_k_11
                    sf "Of course, I forced you into ogling my ass."
                    sf "It's confirmed. You're a moron."
                    sf "I'm so angry at you that I could slap you."
                    sf "But there's something important I need to talk to you about."
                    sf "You're gonna seat at the table and await your breakfast."
                    sf "Disrespect me again and I will spank you so hard you won't be able to sit for a week. Do you understand?"
                    mc "I do."
                    off "It's like I've just been scolded by my mother. She's right, I really am a moron."
                    $ ep2sfangryness="hard"
                "I'm sorry. I have no excuses. [sfLovePath]":

                    mc "I'll try my best not to disappoint you anymore."
                    hide ep2_sc1_m_k_8
                    show ep2_sc1_m_k_11
                    sf "I hope so. Your apology seems to be sincere."
                    sf "Get to the table, the breakfast is ready."
                    $ ep2sfangryness="light"
        "Don't [sfLovePath]":


            scene ep2_sc1_m_k_12
            off "Don't be a dork, [mc_name]. It's a girl, not a piece of meat."
            sf "It's almost ready. Please take a seat, I'll serve you in a minute."

    $ renpy.end_replay()
    scene black with dissolve
    with Pause(2)
    show text "A few minutes later."
    with Pause(2)
    hide text
    show ep2_sc1_m_k_13 with dissolve

    mc "It smells delicious."
    if ep2sfchecked == False:
        hide ep2_sc1_m_k_13
        show ep2_sc1_m_k_14
        sf "I hope it'll taste as good."
        mc "I'm sure it will."

        $ ProcessStat(1, "sf_affection")
        $ DumpNotStack()
    else:
        if ep2sfangryness == "hard":
            hide ep2_sc1_m_k_13
            show ep2_sc1_m_k_19
            sf "You do not deserve it, moron, but I couldn't let it go to waste."
        else:
            hide ep2_sc1_m_k_13
            show ep2_sc1_m_k_20
            sf "I'm not sure you deserve it, you little pervert."

        mc "Ok... Did I mention I was sorry? Because, well... I am."
        off "She takes a deep breath to get clean of her anger before continuing."


    scene ep2_sc1_m_k_15
    sf "Before we eat, there is something we need to talk about."
    mc "I'm all ears."



    sf "It's about [sis_name] and what happened last night."


    mc "Ok..."
    sf "In the second half of the evening, [sis_name] and I did go to a new club that just opened."
    sf "We did dance a bit and had a drink. Everything was going fine until two guys took an interest in us."
    sf "I wasn't interested at all but [sis_name] seemed more receptive."
    sf "I was quite surprised: [sis_name] isn't usually attracted to that kind of guy."
    mc "What kind of guy are we talking about?"
    sf "They are twins, but unlike you and [sis_name], they're identical twins."
    sf "Tall, muscular, handsome, well dressed, the kind of superficial playboys who display their wealth liberally."
    sf "It was obvious they weren't there for our conversation."
    mc "What happened next?"
    hide ep2_sc1_m_k_15
    show ep2_sc1_m_k_16
    sf "We spent an hour with these guys, one of them offered a couple drinks to [sis_name]."
    sf "From the start, I had a bad feeling about them but [sis_name] was having a good time."
    sf "At one point I had to go to the restrooms."
    sf "When I came back, [sis_name] was behaving like she was drunk and one of the twins was holding her very closely."
    sf "I immediately put an end to it by taking her outside."
    sf "By the time we got out of the club, she was barely standing on her legs."
    sf "A bouncer helped me carry her into the car and I drove us back home."
    sf "I didn't think much about it until later that night."
    sf "[sis_name] had no reason to be drunk. She only had something like 3 or 4 drinks."
    sf "There's no way she would have passed out like that."
    hide ep2_sc1_m_k_16
    show ep2_sc1_m_k_17
    sf "I think someone drugged her. One of the twins, probably both."

    menu:
        "They intended to rape her. I'm going to kill those sons of bitches. [sfLovePath]":

            $ ProcessStat(2, "sf_affection")
            $ DumpNotStack()
            $ ep2brutalbreakfast = True
            sf "Please, calm down. I only have some really strong suspicions."
            sf "Even if I'm convinced that it happened, I can't prove it."
            sf "And besides that, I'm not sure you have the muscle to take on two big guys like them."

            menu:
                "I'm confident in my Kung fu. These guys are dead.":
                    sf "You know Kung Fu?"
                    mc "Well, not exactly, but I've learned enough of it by watching all these Donnie Yen movies."
                    sf "Listen, [mc_name]. Either you are not serious or you are an idiot."
                    sf "Either way, it does not suit this conversation."
                    mc "... Sorry..."
                "I'm not afraid. Someone has to teach them a lesson.":

                    sf "That's not your job."
                    mc "Who will do it then?"
                    sf "How about the police?"
                    mc "The police will do nothing without evidence."
                    sf "And it's also their job to gather this."


            sf "Anyway, I m pleased to see that you care about what happened to [sis_name]."


            sf "She says that you hate her but she may be mistaken."


            menu:
                "She's like a sister to me. And I don't hate her. [sfLovePath]":

                    $ ProcessStat(1, "sf_affection")
                    $ DumpNotStack()
                    mc "She's the one who hates me. It makes cohabitation difficult."
                    sf "She doesn't hate you. That sounds like a misunderstanding."
                    sf "Don't you ever try to talk to each other?"
                    mc "She refuses to have a conversation."
                    mc "Every time the conversation isn't to her liking, she refuses to talk."
                    mc "All we can do is wait to learn afterward that she drank herself to oblivion, had sex with some random asshole or wrecked the car."
                    mc "We try to speak about it with her but she simply doesn't give a damn."
                    mc "My parents tried, I tried. She doesn't care."
                "She's a bitch. But I don't hate her.":




                    $ ProcessStat(-1, "sf_affection")
                    $ DumpNotStack()
                    sf "A bitch? What the hell are you talking about?"
                    mc "Well you know, all the things like being a drunkard, having sex with random boys, wrecking the car..."

            hide ep2_sc1_m_k_17
            show ep2_sc1_m_k_18
            sf "Ok, I've had enough of this bullshit."
            sf "I can't believe you're actually accepting these rumors as true"
            sf "She wouldn't want me to talk about that with you but I don't care anymore."
            sf "This situation is so preposterous I can't stand it anymore."
            sf "I don't understand how you came to it."

            sf "[sis_name] drinks, a beer here, a cocktail there, she's been drunk a couple times but she does not come back absolutely wasted every Friday or Saturday night."
            sf "Most of the time, she's perfectly sober."
            sf "She never wrecked your mom's car. Sandra bashed it with a baseball bat for having slept with her ex-boyfriend."
            sf "Which she didn't do, she didn't even know the guy."
            sf "As far as I know, [sis_name] barely kissed a guy or two in her entire life, I'm pretty sure the only dick she had seen until now is yours."
            sf "All these things you think she has done, it's bullshit and rumors spread by a gathering of cunts we endured during our time in high school."
            sf "How could you believe them?"
            hide ep2_sc1_m_k_18
            show ep2_sc1_m_k_20
            mc "You can't be serious."


            mc "I remember clearly the school headmaster calling my parents to tell them [sis_name] was sucking dicks in the restrooms."

            sf "So what? He didn't see it himself, someone just lied to him about witnessing it."
            sf "That's all it took. I'm serious. All of this, it's bullshit."
            mc "So... She didn't fuck Pete in P.E."
            sf "Bullshit. Pete asked her to suck his dick, she told him to suck it himself."
            mc "The threesome during last year's school trip..."
            sf "Bullshit. And she didn't sucked anyone to get her driver's license neither."
            sf "I don't understand."


            sf "They're the same kind of rumors about me and you don't seem to believe them, why are you believing those that target [sis_name]?"

            mc "I don't know... I never thought about it ..."
            sf "You are a moron."
            mc "How was I supposed to know that?"
            mc "She never talked about anything like that."
            sf "Really? Think hard."
            sf "The first time, you or your parents probably confronted her with her behavior and she denied it. Maybe she even tried to explain, but you still didn't believe her."
            sf "Maybe there was a second or a third time, and after that, why would she even try to deny anything."
            sf "You just wouldn't believe her."
            sf "You should be ashamed."


            sf "You are like a brother to her and you preferred to trust the rumours instead of her."

            sf "You failed her while she needed you the most."
            sf "I'm certain you didn't do it on purpose, you are just an idiot, and an imbecile."
            sf "Now that I've made sure you are aware of that, it's the last time you insult or disrespect her in my presence, or else I'll break your nose."
            sf "Are we clear?"
            hide ep2_sc1_m_k_20
            show ep2_sc1_m_k_19
            mc "I'm sorry. I didn't know."
            sf "But now you do."
            mc "How did it come to that?"
            hide ep2_sc1_m_k_19
            show ep2_sc1_m_k_18
            sf "3 years ago I was new in town and in school."
            sf "There was this girl, Kelly, she couldn't stand me."
            sf "I don't know why. I probably did something to upset her, I don't remember."
            sf "She and her many friends started to spread rumors about me."
            sf "I was a slut, a bitch, a whore. I was sick, I was crazy, I was a monster and I sucked dicks in the restrooms."
            sf "After that, the only ones who dared to approach me were boys hoping for a quick handjob or anything like that."
            sf "Needless to say, they were disappointed by my answer."
            sf "And then she came. [sis_name]. She had seen me alone and had decided to be my friend."
            sf "A week later rumors about her emerged as well. And it's still going on, to this day."
            mc "I can't believe I saw nothing. Why didn't she tell me?"
            sf "She did tell you. You didn't believe her."
            mc "I don't know what to say. No wonder she doesn't trust me."
            mc "I'm so sorry. I need to apologize to her."
            sf "Well, it's never too late."
            sf "You could stop being an asshole to begin with. It would be nice."
            mc "Yes, it could be a good start..."
        "Why would he drug her?":



            $ ProcessStat(-1, "sf_affection")
            $ DumpNotStack()
            sf "Are you serious? To rape her obviously."
            mc "I don't understand. You told me [sis_name] was ok to flirt with this guy."
            mc "No need to rape her if she is ok with it."
            hide ep2_sc1_m_k_17
            show ep2_sc1_m_k_18
            sf "What are you talking about? She was ok to flirt, not to have sex with him."



            sf "What? Do you think [sis_name] has sex with every guy who happens to flirt with her?"

            mc "Well, everyone at school knows that she..."
            sf "Are you kidding me?"
            sf "Ok, I've had enough of this bullshit."
            sf "I can't believe you're actually accepting these rumors as true"
            sf "She wouldn't want me to talk about that with you but I don't care anymore."
            sf "This situation is so preposterous I can't stand it anymore."
            sf "I don't understand how you came to it."


            sf "[sis_name] drinks, a beer here, a cocktail there, she's been drunk a couple times but she does not come back absolutely wasted every Friday or Saturday night."

            sf "Most of the time, she's perfectly sober."
            sf "She never wrecked your mom's car. Sandra bashed it with a baseball bat for having slept with her ex-boyfriend."
            sf "Which she didn't do, she didn't even know the guy."
            sf "As far as I know, [sis_name] barely kissed a guy or two in her entire life, I'm pretty sure the only dick she had seen until now is yours."
            sf "All these things you think she has done, it's bullshit and rumors spread by a gathering of cunts we endured during our time in high school."
            sf "How could you believe them?"
            hide ep2_sc1_m_k_18
            show ep2_sc1_m_k_20
            mc "You can't be serious."


            mc "I remember clearly the school headmaster calling my parents to tell them [sis_name] was sucking dicks in the restrooms."

            sf "So what? He didn't see it himself, someone just lied to him about witnessing it."
            sf "That's all it took. I'm serious. All of this, it's bullshit."
            mc "So... She didn't fuck Pete in P.E."
            sf "Bullshit. Pete asked her to suck his dick, she told him to suck it himself."
            mc "The threesome during last year's school trip..."
            sf "Bullshit. And she didn't sucked anyone to get her driver's license neither."
            sf "I don't understand."

            sf "They're the same kind of rumors about me and you don't seem to believe them, why are you believing those that target [sis_name]?"
            mc "I don't know... I never thought about it ..."
            sf "You are a moron."
            mc "How was I supposed to know that?"
            mc "She never talked about anything like that."
            sf "Really? Think hard."
            sf "The first time, you or your parents probably confronted her with her behavior and she denied it. Maybe she even tried to explain, but you still didn't believe her."
            sf "Maybe there was a second or a third time, and after that, why would she even try to deny anything."
            sf "You just wouldn't believe her."
            sf "You should be ashamed."

            sf "You are like a brother to her and you preferred to trust the rumours instead of her."
            sf "You failed her while she needed you the most."
            sf "I'm certain you didn't do it on purpose, you are just an idiot, and an imbecile."
            sf "Now that I've made sure you are aware of that, it's the last time you insult or disrespect her in my presence, or else I'll break your nose."
            sf "Are we clear?"
            hide ep2_sc1_m_k_20
            show ep2_sc1_m_k_19
            mc "I'm sorry. I didn't know."
            sf "But now you do."
            mc "How did it come to that?"
            hide ep2_sc1_m_k_19
            show ep2_sc1_m_k_18
            sf "3 years ago I was new in town and in school."
            sf "There was this girl, Kelly, she couldn't stand me."
            sf "I don't know why. I probably did something to upset her, I don't remember."
            sf "She and her many friends started to spread rumors about me."
            sf "I was a slut, a bitch, a whore. I was sick, I was crazy, I was a monster and I sucked dicks in the restrooms."
            sf "After that, the only ones who dared to approach me were boys hoping for a quick handjob or anything like that."
            sf "Needless to say, they were disappointed by my answer."
            sf "And then she came. [sis_name]. She had seen me alone and had decided to be my friend."
            sf "A week later rumors about her emerged as well. And it's still going on, to this day."
            mc "I can't believe I saw nothing. Why didn't she tell me?"
            sf "She did tell you. You didn't believe her."
            mc "I don't know what to say. No wonder she doesn't trust me."
            mc "I'm so sorry. I need to apologize to her."
            sf "Well, it's never too late."
            sf "You could stop being an asshole to begin with. It would be nice."
            mc "Yes, it could be a good start..."

    hide ep2_sc1_m_k_20
    show ep2_sc1_m_k_18
    mc "So... What do we do?"
    sf "First, we need to talk to her. We should try to convince her to go to the police."
    sf "Even without evidence, they may be able to do something."
    hide ep2_sc1_m_k_18
    show ep2_sc1_m_k_16
    mc "I'm not sure she'll like that idea. She doesn't like to be told what to do."
    sf "I know. I didn't say it would be easy."

    scene black with dissolve
    off "10 minutes later we have finished our breakfast."
    show ep2_sc1_m_k_22 with dissolve
    off "[sis_name] enters the room like a ghost, dragging herself painfully to the coffeepot."
    sf "Hello, [sis_name]."
    sis "Hello."
    sf "Are you ok?"
    hide ep2_sc1_m_k_22
    show ep2_sc1_m_k_23
    sis "I feel like my head is about to explode. And I'm a bit nauseous. I'll get better after the coffee."
    sis "You two had breakfast together?"
    mc "We did. [sf_name] cooked some eggs and bacon, and it was delicious. As good as mom's."
    sis "You made him breakfast?"
    hide ep2_sc1_m_k_23
    show ep2_sc1_m_k_24
    sf "I'll do some for you too, it'll be quick."
    sis "No, I'm ok. It's just eggs and bacon. If I want some I can cook some myself."
    mc "We have no doubt about it but..."
    sis "But what? Are you mocking me again?"
    hide ep2_sc1_m_k_24
    show ep2_sc1_m_k_25
    mc "No, I'm not. I know you can cook. I've seen you working in the kitchen with mom, so I can easily believe that you can cook."
    sis "I can cook a full meal."
    mc "I'm sure you can."
    sis "No, you're not. You don't believe me. I'll cook something tonight, you'll see."
    hide ep2_sc1_m_k_25
    show ep2_sc1_m_k_23
    sf "You have nothing to prove, [sis_name]. You don't have to do that."
    sis "I said I'll cook tonight."
    mc "Ok then."
    sis "So... What happened last night?"
    sis "And why am I wearing this old nightshirt I didn't use since 10th grade?"
    sf "Well, we actually want to talk to you about that."
    sis "We?"
    hide ep2_sc1_m_k_23
    show ep2_sc1_m_k_24
    sf "Do you remember anything from last night?"
    sis "I remember going to the club, drinking a couple cocktails and ... I don't know... Did I drink that much?"
    sf "No, you didn't. You drank a beer at the pub, and 2 or 3 cocktails at the club."
    mc "Do you remember the two guys who tried to pick you up?"
    hide ep2_sc1_m_k_24
    show ep2_sc1_m_k_26
    sis "Ok, what's going on? Why did you tell him what happened at the club?"
    sf "We think that one of these guys put something in your drink."
    hide ep2_sc1_m_k_26
    show ep2_sc1_m_k_27
    sis "What are you talking about?"
    mc "We think they drugged you."
    sis "Are you being serious right now? Are you telling me that those guys tried to rape me?"
    hide ep2_sc1_m_k_27
    show ep2_sc1_m_k_28
    sis "Of course, I should have known. I only attract crazies and perverts."
    sis "When I meet a guy he's obviously a rapist. Do I deserve that kind of thing?"
    sf "Of course not. You did nothing wrong."
    mc "[sis_name], listen. We should go to the police."
    sis "Absolutely not!"
    sf "Why? they may be able to do something."

    sis "If we go to the police, your parents will be involved! I don't want them to know."
    mc "But..."
    hide ep2_sc1_m_k_28
    show ep2_sc1_m_k_29
    off "She suddenly stands up from the table and leaves the room."
    sf "[sis_name], please!"
    sis "Leave me alone."
    hide ep2_sc1_m_k_29
    show ep2_sc1_m_k_30
    sf "I'll go talk to her."
    menu:
        "Thank you, [sf_name]. [assholePath]":
            hide ep2_sc1_m_k_30
            show ep2_sc1_m_k_31
            sf "It's my friend. It's natural."
            $ ep2sfgoneinstead = True
            scene black with dissolve
            off "I'm taking care of the dishes before going to my room."
            off "Half an hour of silence later I can hear voices coming from the corridor."
            off "They're on their way out for their running session."
            jump ep2sc3
        "No. I'll go.":

            $ ProcessStat(1, "sf_affection")
            $ DumpNotStack()
            hide ep2_sc1_m_k_30
            show ep2_sc1_m_k_31
            sf "Are you sure?"

            mc "Yes. I'll try being a good friend for once."
            jump ep2sc2

label ep2sc2:

    scene black with dissolve
    with Pause(2)
    show text "A few minutes later."
    with Pause(2)
    hide text
    scene ep2_sc2_cm_0 with dissolve

    off "I knock on [sis_name]'s bedroom door and wait a moment without getting any response."
    off "I can't hear any sound coming from inside."
    menu:
        "Enter [sisSubPath]":
            off "Maybe she's not inside? I should check."

            $ ProcessStat(-1, "sis_affection")
            $ DumpNotStack()
            $ ep2sissurprised = True
            hide ep2_sc2_cm_0
            show ep2_sc2_srm_1
            $ UnlockThat("ep2/ep2_sc2_srm_1")
            off "Holy shit."
            hide ep2_sc2_srm_1
            show ep2_sc2_srm_2
            $ UnlockThat("ep2/ep2_sc2_srm_2")
            sis "What the fuck? Did I tell you to come in?"
            sis "What are you waiting for? Do you want me to kill you?"
            sis "Get out! And close that door! Do you hear me?"
            mc "I'm sorry! I didn't know!"

            menu:
                "Be a moron. [sisSubPath]":

                    $ ProcessStat(-1, "sis_affection")
                    $ ProcessStat(1, "sis_submission")
                    $ DumpNotStack()
                    $ ep2sissurprisedstay=True
                    off "I don't even know why I do that."
                    hide ep2_sc2_srm_2
                    show ep2_sc2_srm_4
                    $ UnlockThat("ep2/ep2_sc2_srm_4")
                    off "I close the door only to realize that I somehow forgot to get out."
                    off "[sis_name] seems confused. She looks like she doesn't know how to react."
                    hide ep2_sc2_srm_4
                    show ep2_sc2_srm_15
                    $ UnlockThat("ep2/ep2_sc2_srm_15")
                    off "A long and awkward silence takes place between us as each of us struggles to find a way to react."
                    off "I'm so dead."
                    hide ep2_sc2_srm_15
                    show ep2_sc2_srm_3
                    sis "You are so dead. I'm going to kill you."
                    mc "I'm sorry I ... forgot to get out ..."
                    hide ep2_sc2_srm_3
                    show ep2_sc2_srm_16
                    $ UnlockThat("ep2/ep2_sc2_srm_16")
                    sis "Are you kidding me? You forgot to leave?"
                    sis "And what about now?"
                    sis "I promise you I won't forget to kill you, you damn little pervert!"
                    mc "I'm sorry, I don't know what happened!"
                    sis "GET OUT!"
                    mc "I'm sorry [sis_name], I didn't do it on purpose. Really!"
                    hide ep2_sc2_srm_16
                    show ep2_sc2_cm_1
                    off "I get out of the room and close the door as quickly as possible."
                "Get out. [sisLovePath]":

                    mc "I'm sorry [sis_name], I didn't do it on purpose. Really!"
                    hide ep2_sc2_srm_2
                    show ep2_sc2_cm_1
                    off "I get out of the room and close the door as quickly as possible."


            off "I can hear her screaming on the other side of the door."
            sis "You do that again and I'll kill you, you damn pervert!"
            off "Shit. I really fucked up, again."
            off "Nice body tho. Those boobs looked soft and firm."
            off "Fuck, what I am thinking about? I 'd better hide in my room for a while."
        "Knock again [sisLovePath]":


            mc "[sis_name]? Are you there?"
            sis "Don't come in! Can't you wait? I'm naked right now."
            sis "If you come in I'll kill you! Do you understand?"
            mc "Sure. I'm waiting. Tell me when I can come in."
            off "She let me in after a couple of minutes."
            hide ep2_sc2_cm_0
            show ep2_sc2_srm_5
            sis "What do you want?"
            hide ep2_sc2_srm_5
            show ep2_sc2_srm_6
            mc "We need to talk. And I want to hug you."
            hide ep2_sc2_srm_6
            show ep2_sc2_srm_7
            sis "Ok, you little pervert. It's out of the question that you touch me."
            sis "If you try anything funny I'll kill you."
            hide ep2_sc2_srm_7
            show ep2_sc2_srm_8
            mc "Please listen to me."

            menu:
                "I want to apologize to you. [sisLovePath]":

                    $ ProcessStat(5, "sis_affection")
                    $ DumpNotStack()
                    $ ep2apologizedtosis=True
                    mc "I talked with [sf_name] this morning and she told me all these things I wasn't aware of."
                    mc "She told me about the girls at school, about the rumors, about everything."
                    mc "And I am ashamed. I should have trusted you. I don't know why I choose to believe the rumors instead of you."
                    mc "I have truly been an asshole all these years. I should have been there for you."
                    mc "I can only be sorry and hope it's not too late to stop being an idiot."
                    mc "Aside from that, I want you to know that I do not hate you."

                    mc "You are like a sister to me, and I care about you."
                    hide ep2_sc2_srm_8
                    show ep2_sc2_srm_9
                    mc "I know, it's a bit strange coming from someone who has been a total imbecile for the last few years."
                    mc "But it's true. You're important to me and I care about you."
                    mc "And if you allow me, I want to be here for you."
                    mc "I'm sorry [sis_name]. You don't have to be alone."
                    sis "Dude, you're weird, you're making me uncomfortable."
                    mc "I'm going to hug you now."
                    hide ep2_sc2_srm_9
                    show ep2_sc2_srm_11
                    off "I grab her and hug her tightly."
                    off "She shows little to no resistance and quickly lets herself go in my arms."
                    mc "I'm sorry, I should have been there. Can you forgive me?"
                    sis "Can you shut up? I don't know what's gotten into you but this whole situation, it's weird."
                    mc "I'm almost finished."
                    mc "About last night, and this morning."
                    mc "I know you are a big girl, I know that you are strong and courageous but you don't have to go thru this alone."
                    mc "I'm here."
                    hide ep2_sc2_srm_11
                    show ep2_sc2_srm_12
                    mc "And despite what you seem to think, no one has any right to hurt you."
                    off "We stay like that for a long time."
                    off "She doesn't move nor make any noise. She doesn't show any will to break our embrace."
                    off "I can feel the warmth of her body flowing thru my skin."
                    off "Like last night, I can breathe her perfume. It smells like a mix of vanilla and sunscreen."
                    off "It's sweet and almost intoxicating."

                    menu:
                        "Go for her ass.":
                            sis "If you make a move to my ass, I'll break both your arms and I throw you thru the window."
                            mc "I didn't even think about it."
                            sis "Good."
                        "I like your smell. [sisLovePath]":

                            $ ProcessStat(2, "sis_affection")
                            $ DumpNotStack()
                            $ ep2sissmelled = True
                            mc "You smell like summer."
                            sis "What does that even mean? Summer is not a perfume."
                            mc "That doesn't forbid me from liking it."
                            sis "You're crazy. And you should take a shower."
                            mc "I'll think about that."

                    hide ep2_sc2_srm_12
                    show ep2_sc2_srm_13
                    off "She finally gets away from me and heads directly to her dressing room."
                    off "I have the impression she's trying to hide some tears."
                    sis "That's enough, please leave me alone now. I have to get ready."
                    mc "You're going to run with a hangover when it's already 30°c outside?"
                    sis "It's Sunday, and Sunday is running day. [sf_name] is coming with me."
                    sis "I'll allow you to care for me all you want, but for the hour to come, I'll be fine."
                    mc "Ok then. See you later then."
                    scene black with dissolve
                    off "Well, it went better than I expected."
                    off "I still wonder how could I have been so blind. What a moron."

                    off "Because I choose to believe that [sis_name] was a drunken slut, I treated her as such."
                    off "No wonder she responded to me in her ways."
                    off "I don't deserve her forgiveness."
                "I forgive you.":



                    $ ProcessStat(-1, "sis_affection")
                    $ DumpNotStack()
                    $ ep2failedapologize=True
                    mc "[sf_name] told me everything."
                    mc "I don't understand why you didn't tell us, and it doesn't really matter."
                    hide ep2_sc2_srm_8
                    show ep2_sc2_srm_10


                    mc "It's over now. Let stop being enemies, I forgive you, you forgive me and we can be like brother and sister again."

                    mc "What do you say? Can I have my hug?"
                    hide ep2_sc2_srm_10
                    show ep2_sc2_srm_14
                    sis "Then you can go fuck yourself."
                    sis "What? You've been an asshole for all this time and you think your shitty speech will be enough to erase the past?"
                    sis "I don't need your forgiveness, I have nothing to reproach myself."
                    sis "If you think I owe you an apology or something, you're even more of an asshole than I thought."
                    sis "Now, get the fuck out of my room!"
                    mc "I was trying to be nice! I'm sorry! Don't you understand?"
                    sis "Get out!"
                    hide ep2_sc2_srm_14
                    show ep2_sc2_cm_1
                    off "What did I do to deserve that?"
                    off "I try to be nice, and this is how she treats me. That bitch!"
                    off "She needs to be taught a lesson..."
    $ renpy.end_replay()
label ep2sc3:
    scene black with dissolve
    with Pause(2)
    show text "One hour later"
    with Pause(2)
    hide text
    show ep2_sc3_bm_1 with dissolve
    off "[sis_name] and [sf_name] have been gone running for one hour now. I'm taking a shower."
    off "I feel like my life got a lot more complicated since yesterday."


    off "Until this morning, I was pretty sure I was the good guy with the bitchy friend while I'm actually a total moron who trusted, and somehow even condoned the forged rumors of his friend being a whore."
    off "Goddammit. I even sometimes denounced her to my parents based on these rumors."

    off "Needless to say, I see her, and myself, very differently now."

    if ep2apologizedtosis == True:
        off "Apologizing to her was the only thing I could do for now but I have a lot of wrongs to right."

        off "Starting with my parents. I'll have to tell them."

        off "I'm feeling so much guilt right now that I'm ready to beg for punishment."

    if ep2failedapologize == True:
        off "I tried to make peace with her but she wasn't really receptive."
        off "I guess we are to far gone to be nice to each other again."

    if ep2sissurprised == True:
        off "I fucked up so much by surprising her almost naked."
        off "I was about to apologize and I ruined everything again."
        off "But hell... that body..."

        off "Maybe should I surprised her more often... like a good friend would do."

    off "On top of that, the conversation I had with Steve yesterday completely fucked up my brain."
    off "I can't think of anything but boobs, asses, and pussies."

    off "I even see my childhood friend as a sexual possibility."
    off "That's beyond fucked up. I'm a pervert."
    off "And that dream was crazy and frustrating. I'm still thinking about it."
    off "Maybe I should jerk off to exorcise it."

    menu:
        "[gr]Do it.":
            hide ep2_sc3_bm_1
            show ep2_sc3_bm_2
            $ ep2showerfap=True
            off "My dick is fully erect and hard as a rock in less than 5 seconds."
            menu:
                "Think of [sis_name].":
                    hide ep2_sc3_bm_1
                    show ep2_sc3_bm_7
                    $ UnlockThat("ep2/ep2_sc3_bm_7")


                    off "It's my friend, dammit! Why am I doing that? I can't refrain myself."
                    off "Fuck, I feel like it's even better because she's like a sister to me."


                    off "What kind of pervert am I?"
                    off "I want to lick those boobs, I want to fuck that pussy ... And that ass, oh that ass!"
                "Think of [sf_name].":
                    hide ep2_sc3_bm_1
                    show ep2_sc3_bm_8
                    $ UnlockThat("ep2/ep2_sc3_bm_8")
                    off "Steve is right, I have to try something."
                    off "You're making me crazy."
                    off "I want to play with your ass. I want it so bad!"

            off "Holy shit, I should have done that sooner."
            off "I'm almost ready to explode when I hear a strange noise coming from the hallway."
            scene ep2_sc3_bm_2
            off "I immediately stop and stay silent."
            off "Nothing. Was it my imagination?"
            off "Anyway, the mood is gone."
        "Don't.":


            off "I'll do that later."
            off "I'm about to get out of the shower when I hear a strange noise coming from the door."
            off "I stay silent and listen for a moment. Nothing."

    scene ep2_sc3_bm_3
    off "Maybe the girls are back. I should get out of the shower, they're probably going to need it."
    off "I'm stepping out of the shower and head to the towels."

    if ep2sissurprised==True:
        hide ep2_sc3_bm_3
        show ep2_sc3_bm_4
        off "The door suddenly opens and [sis_name] enters the bathroom."
        off "I try to cover myself with my hands."
        hide ep2_sc3_bm_4
        show ep2_sc3_bm_5_bis
        sis "Well, well, well, what do we have here? Isn't this Mr little pervert?"
        mc "[sis_name]! I'm naked! Give me a minute or so and I'll get out of the bathroom."
        sis "I'm well aware of your nakedness. I counted on it."
        sis "Tell me, you little pervert, how does it feel? Do you feel weak? Vulnerable? Violated?"
        mc "You are right. I saw you almost naked and this is only a just retribution."

        menu:
            "Show her the goods. [sisSubPath]":
                hide ep2_sc3_bm_5_bis
                show ep2_sc3_bm_5
                $ ep2goodsexposed=True

                $ ProcessStat(5, "sis_submission")
                $ DumpNotStack()
                off "I abandon the idea of hiding anything and I adopt a prouder stance before her."
                mc "To be honest I don't feel weak, nor vulnerable, nor anything like that."
                mc "I have no reason to."
                hide ep2_sc3_bm_5
                show ep2_sc3_bm_6
                sis "Holy shit..."
                off "I can feel her gaze plunging on my cock."
                off "It's an almost physical sensation. It excites me."
                if ep2showerfap==True:
                    off "My dick is still hard from my aborted wanking."
                    sis "Why is it already .. erect?"
                    mc "I jerked off a little earlier. It's still pretty hard."
                else:
                    off "My penis slowly hardens, motivated by her attention."
                    sis "It seems to be ... moving..."
                    mc "You are looking at it. It's getting excited."

                mc "To be honest I tried to hide it out of respect for you."
                mc "I didn't want to embarrass you."
                mc "But you're here to take a look at it so .. here you go. Look all you want."
                sis "..."
                mc "Do you want to touch it?"
                off "She doesn't answer, captivated by my cock."
                off "I give myself a couple of strokes"
                mc "[sis_name]? Do you want to touch it?"
                sis "No, thank you..."
                sis "You're not about to jerk off in front of me, are you?"
                mc "Not at all. Unless you want me too."
                sis "Why the heck would I want you to jerk off in front of me?"
                mc "I don't know... You seemed interested."
                sis "No, I'm not! And move your ass, we need the bathroom."
            "Apologize.":

                mc "I'm sorry but I told you, it was an accident."
                sis "Yeah, sure. And next time you will knock on the door before entering my room?"
                mc "But I knocked! You didn't answer!"
                sis "Because I didn't want you to enter!"
                mc "Ok, you're right, I shouldn't have entered your bedroom like I did. I'm sorry."
                sis "Good. And now, move your ass, we need the bathroom."

    off "I grab a towel and get out of the bathroom."
    scene ep2_sc3_cm_3
    off "I barely have set foot in the hallway when [sf_name] jumps in front of me from [sis_name]'s bedroom."
    sf "Hi there."
    mc "Hi [sf_name], how was the running?"
    sf "Hot, and painful."

    if ep2failedapologize==True:
        sf "As was the conversation."
        sf "You know, I have the feeling that I'm making a lot of effort to get the two of you to make peace while you give your all to ruin everything."
        sf "I don't know if you do it on purpose or if you are just bad with words."
        mc "I'm sorry. I still don't understand what went wrong."
        sf "I talked to her. She still thinks you are a moron yet she doesn't hate you."
        sf "She knows you came to apologize. She appreciated that."
        sf "We agreed that your choice of word was poor."
        mc "I'm sure it was. It's something I need to work on."
        sf "Indeed."
    elif ep2sissurprised==True:
        sf "As was the conversation."
        sf "You were supposed to talk to her."
        sf "You choose to surprised her naked instead. You little pervert."
        mc "I didn't choose anything!"
        mc "I just opened the door and she was there... wearing only her panties."
        sf "I sure hope it was unintentional."
        sf "She's very vulnerable right now, doing it on purpose would have been very, very mean of you."
        mc "I know. I'm not like that."
        sf "There again, I hope so. You're lucky she doesn't doubt it was just an accident."
        sf "She knows you came to apologize. She appreciated that."

    elif ep2apologizedtosis==True:
        sf "But the conversation was surprisingly nice."
        sf "She told me that you apologized to her and even hugged her."
        $ ProcessStat(1, "sf_affection")
        $ DumpNotStack()
        sf "Which you apparently didn't do since she was 12."
        sf "She is happy."
        mc "I'm glad to hear it."
        mc "I feel like apologizing isn't nearly enough."
        mc "I'm feeling so guilty. There must be something else I can do."
        sf "The past is behind us. You should concentrate on the future."

    hide ep2_sc3_cm_3
    show ep2_sc3_cm_4
    sf "Anyway, you already took your shower so.. I guess you won't join us this time either?"
    mc "Can I really say yes?"
    hide ep2_sc3_cm_4
    show ep2_sc3_cm_5
    sis "Not if you want to live."
    mc "Of course, I was only joking."
    sis "Mr pervert, if I caught you spying on us, I'll kill you."
    mc "That sounds a bit harsh, but it's crystal clear."
    hide ep2_sc3_cm_5
    show ep2_sc3_cm_6
    sis "Good. Oh, and by the way, you handle lunch."
    mc "What?"
    sis "You heard me."


    scene black with dissolve
    off "Lunch. Ok. I'll find something."
    off "..."
    off "They're showering together again."
    off "I don't know what they're doing in there but I'm dying to know."
    off "Perhaps I can find a way..."

label ep2sc4:
    scene black with dissolve
    with Pause(2)
    show text "One hour later"
    with Pause(2)
    hide text
    show ep2_sc4_kl_1 with dissolve
    off "Handle lunch she said. Well, handled the lunch I have."
    off "I call [sis_name] and [sf_name] very elegantly by yelling their names up the stairs."
    hide ep2_sc4_kl_1
    show ep2_sc4_kl_2
    off "They soon both arrive, ready for lunch."
    mc "Behold, ladies, the famous three cheese and pepperoni pizza from Don Giovanni."
    sis "It's his favourite pizza and Don Giovanni is the cheap Italian restaurant down the road."
    sis "Discounted pizza for 9$."
    mc "Hey! I know you like it too."
    sis "I do, but you won't impress [sf_name] with a 9$ pizza."
    hide ep2_sc4_kl_2
    show ep2_sc4_kl_3
    mc "You don't like pizza, [sf_name]?"
    sf "I actually love pizza. But my ass isn't ok with that."
    mc "Your ass doesn't like pizza?"


    sf "Not every girl is like [sis_name]."

    sf "She can feast on pizza and burgers without gaining weight, I can't."
    sis "Hey, I run my 10 km every week you know?"
    sf "I know, I run those same 10 km with you."
    sf "And I also exercise every day, and it's barely enough to keep my ass's fat in check."
    mc "Well, if it can comfort you, your ass looks pretty perfect to me."

    if ep2sfchecked==True:
        sf "I know, right? I trust you on that matter."
        sf "You must be an expert with the extended amount of time you took to carefully look at it this morning."
        mc "I'm still sorry about that..."
        sis "Did I miss something?"

        sf "I'm just messing with our friend. Don't worry [sis_name]."
    else:

        sf "Really? Thank you."
        sf "I'm sure you took a good look at it to appreciate it's fattiness."
        mc "That sounds like a trap conversation I shouldn't have engaged in."
        sf "I'm just messing with you, [mc_name]. Don't worry."

    sf "And the pizza will be fine."
    sis "Less talking, more eating guys. I'm starving."

    hide ep2_sc4_kl_3
    show ep2_sc4_kl_4
    with Pause(2)
    hide ep2_sc4_kl_4 with dissolve
    show ep2_sc4_kl_5 with dissolve

    off "Half an hour later, lunch is over. The pizza is almost finished."
    sf "I can feel the fat slowly migrating to my buttocks."
    sis "You'll lose it swimming in the pool this afternoon."
    mc "Ladies, I'm glad you enjoyed your lunch. I'll take care of the leftovers and the dishes."
    off "The doorbell rings loudly."
    sis "I'll go."
    sf "I'm coming with you."
    off "With the girls gone, I clean the table, put away the remaining slice and wash the dish."
    hide ep2_sc4_kl_5
    show ep2_sc4_kl_6
    sf "[mc_name]?"
    off "The girls are back."
    off "Something happened."
    off "[sf_name] looks worried, and [sis_name] seems a bit lost."
    hide ep2_sc4_kl_6
    show ep2_sc4_kl_7
    off "What the hell is that?"
    off "Where did she get these flowers?"
    hide ep2_sc4_kl_7
    show ep2_sc4_kl_6
    mc "What's the matter?"
    sf "The doorbell... It was a delivery boy... Someone sent flowers to [sis_name]."
    mc "Someone?"
    sf "One of the guys from last night."
    hide ep2_sc4_kl_6
    show ep2_sc4_kl_8
    mc "Well, that's unexpected..."
    sf "There's a note."
    sf "He says that he hopes that [sis_name] is feeling better as she was not looking so good when she left the club."
    sf "He also gave her his phone number, asking her to give him a call."
    hide ep2_sc4_kl_8
    show ep2_sc4_kl_9
    mc "[sis_name]? What do you think?"
    sis "I don't know what to think."
    sis "You told me that this guy drugged me, and honestly, you convinced me."
    sis "Now he's sending me flowers."
    sis "Maybe we're wrong, maybe he's not the one who drugged me."
    sis "Maybe I wasn't even drugged by anyone."
    sis "I can't be sure of anything anymore."
    sf "[mc_name]?"
    hide ep2_sc4_kl_9
    show ep2_sc4_kl_8
    mc "I think he drugged [sis_name] and you got her away from him."
    mc "I think he sent [sis_name] the flowers to cover his tracks, to make it harder for her to think that he drugged her."
    mc "So she won't go to the police."
    sf "That... makes sense."
    mc "Yeah... On the other hand ..."
    hide ep2_sc4_kl_8
    show ep2_sc4_kl_15
    mc "How did he find you? Did you give him your address?"
    sis "I don't remember."
    sf "You didn't, at least while I was with you."
    mc "Either way, I'm sure it's not something you tell a guy the first hour you met him."
    mc "That means he probably followed you here."
    sf "That's crazy. If it's true, he's a complete psychopath."
    sf "We have to go to the Police, [sis_name]."
    hide ep2_sc4_kl_15
    show ep2_sc4_kl_12
    sis "No!"


    sis "If I go to the police, your parents will know and I'm sure your mom will come back from their trip immediately."

    sis "It'll be the end of our week together and the beginning of my summer in hell."
    mc "Come on, Mom isn't going to punish you for being the victim."
    sis "I don't care."
    hide ep2_sc4_kl_12
    show ep2_sc4_kl_13
    sf "Ok, then ... Maybe are we overreacting a little."
    sf "Perhaps we can just ignore him and he will cease to harass you."
    mc "I'm sure it'll be fine."
    mc "He's just trying to make sure you do not denounce him."
    mc "By tomorrow it should be obvious to him that you didn't go to the police and he should simply let it go."
    mc "You'll probably never see him again."

    if ep2sfgoneinstead == True:
        sis "He may be innocent..."
        sis "You're talking about him like he is guilty but we objectively have no proof."
        sis "Maybe I was just drunk. Maybe he didn't do anything."
        sis "Maybe it's just... a misunderstanding."

        menu:
            "You can't be serious.":
                mc "[sf_name] told you, he was touching you like a creep just before she extracted you from the club."
                mc "He was clearly about to drag you onto the parking lot to rape you, maybe even worse."
                mc "The guy followed you here!"
                mc "You can't seriously think he's innocent!"
                hide ep2_sc4_kl_13
                show ep2_sc4_kl_11
                sis "Don't tell me what I can think."
                sis "I'm just saying that the guy isn't necessarily guilty."
                mc "He is. Trust me."
                sis "Trust you?"
                sis "Who the fuck do you think you are to ask for my trust?"
                sis "Why do you care in the first place?"

                mc "What do you mean? I'm your friend."
                mc "I'm just trying to protect you."
                hide ep2_sc4_kl_11
                show ep2_sc4_kl_10
                sis "How kind of you."
                sis "You didn't give a shit about me until now and you want to protect me?"
                sis "Mind your own business."
                sf "Please, calm down, both of you!"
                mc "Hey, I'm just trying to help!"
                sis "I don't need your help. Moron."
                hide ep2_sc4_kl_10
                show ep2_sc4_kl_11
                mc "Alright!"
                mc "Then why don't you give your friend a call so you can get yourself raped on a parking lot?"

                $ ProcessStat(-2, "sis_affection")
                $ ProcessStat(-2, "sf_affection")
                $ DumpNotStack()
                sis "Maybe I will, and maybe he won't need to rape me, asshole!"
                off "[sis_name] leaves the room. I'm angry at her and at myself."
                off "[sf_name] is looking at me, infuriated."
                hide ep2_sc4_kl_11
                show ep2_sc4_kl_16
                sf "Are you out of your mind?"
                off "Cooling down, I realize what I just said."
                mc "Well... I may have gone a bit overboard..."
                mc "I can't help her if she doesn't let me."
                sf "I'm not sure you can do anything for her anyway."
                sf "Tell me when you finally decide to behave like an adult."
                off "[sf_name] leaves the place, leaving me alone with my shame."
                $ ep2flowerfail = True
                jump ep2sc6
            "He may be. [sisLovePath] [sfLovePath]":
                mc "But honestly, the chance is low."
                mc "I'm pretty sure only a creep would follow two girls to their home like he did."
                sis "Maybe he didn't even do that."
                sis "He could have met someone who knows me and ask for my address."
                hide ep2_sc4_kl_13
                show ep2_sc4_kl_14
                mc "That's even worse. I'm sorry [sis_name]."

                $ ProcessStat(1, "sis_affection")
                $ ProcessStat(1, "sf_affection")
                $ DumpNotStack()
                sis "You don't have to be sorry."
                sis "You're probably right."
                sis "It doesn't matter anyway."
                sis "I wasn't planning on meeting him again. Creep or not."
                sis "I think I'm gonna take a nap. I'll be in my room."
                off "[sis_name] leaves the room."
                hide ep2_sc4_kl_14
                show ep2_sc4_kl_18
                sf "What are we going to do?"
                mc "If we don't go to the police there's nothing we can do besides waiting and avoiding that guy."
                mc "Don't worry. It's gonna be okay."
                sf "I hope so."
                sf "I'll join [sis_name]. See you later."
    else:
        sis "I hope so. But he knows my name, and where we live..."
        mc "It'll be okay. I'm here."

        mc "If he comes back, he'll be surprised to have a discussion with your overprotective friend."

        $ ProcessStat(2, "sf_affection")
        $ DumpNotStack()

        if ep2apologizedtosis == True:
            hide ep2_sc4_kl_13
            show ep2_sc4_kl_12
            sis "I didn't know I had one of those."
            mc "You have one now. He's brand new and motivated."

            $ ProcessStat(1, "sis_affection")
            $ DumpNotStack()

            sis "..."
            sis "I'm sorry, I'll have to get used to it."
            hide ep2_sc4_kl_12
            show ep2_sc4_kl_14
            sis "Right now, your change of heart is as comforting as weird."
            mc "I can understand that."
            sis "... Ok... I'll be in my room ..."
            off "[sis_name] leaves the room."
            hide ep2_sc4_kl_14
            show ep2_sc4_kl_17
            sf "Looks like you finally understood you don't have to be an imbecile..."
            mc "I'm still learning."
            sf "I'm sure you will continue to improve."
            sf "I'll be with [sis_name]."
            mc "See you later."
        else:

            hide ep2_sc4_kl_13
            show ep2_sc4_kl_12
            sis "Like I had one of those."
            mc "You have... me. Isn't it obvious?"
            sis "No, it's not."
            hide ep2_sc4_kl_12
            show ep2_sc4_kl_11
            sis "You couldn't even apologize properly to me, how could you possibly be of any assistance here?"
            sf "You're a bit rough, [sis_name]. He's doing his best."
            sis "I would like to see that."
            sis "I'll be in my room."
            off "[sis_name] leaves the room."
            hide ep2_sc4_kl_11
            show ep2_sc4_kl_17
            sf "She still doesn't fully trust you, but I least she acknowledges you tried."
            mc "I feel like it will be a long way to regain her trust."
            sf "Stop being a moron and it can happen faster than you think."
            sf "I'll be with her, See you later!"



label ep2sc5:
    scene black with dissolve
    with Pause(2)
    show text "Later that afternoon."
    with Pause(2)
    hide text
    scene ep2_sc5_mcr_0 with dissolve
    mc "Come on, he shot me through the damn wall!"
    mc "Can you stop throwing grenades at me, please? No no no no!"
    mc "Fuck you! Fuck that game. I have enough of this."
    off "I'm considering my options for my next activity and thinking about finally jerking off to my heart content when someone knocks on my door."
    sf "[mc_name]?"
    hide ep2_sc5_mcr_0
    show ep2_sc5_mcr_1
    mc "Come in, [sf_name]."
    sf "Hey."
    mc "Hey."
    sf "We're going to hang out by the pool. Don't you want to join us?"
    mc "Sure. I'll put my swimsuit on and meet you down there."
    sf "All right, see you at the pool then!"
    hide ep2_sc5_mcr_1
    show ep2_sc5_pa_1
    off "10 minutes later, I'm joining the girls."
    off "I should come by the pool more often."
    hide ep2_sc5_pa_1
    show ep2_sc5_pa_2
    $ UnlockThat("ep2/ep2_sc5_pa_2")
    off "I'd better be careful tho."
    off "I don't want to be embarrassed by an erection while socializing with the girls."
    off "If my dick was to pop out of my shorts, that would be quite the diplomatic incident."
    sis "So, how do you like my ass today?"
    off "I've been caught already."
    off "I can feel the breath of death on my neck."
    hide ep2_sc5_pa_2
    show ep2_sc5_pa_3
    mc "I beg your pardon?"
    sis "Yesterday, you told me that my swimsuit wasn't fitting my ass. How is it today? Look at it and tell me."
    off "What the hell is going on?"
    off "Is this a trap?"
    hide ep2_sc5_pa_3
    show ep2_sc5_pa_2
    off "She's turning on herself to show me her ass again."
    sis "So?"
    off "I'm taking a good look at it but I have trouble enjoying the view as I'm trying to find a way to survive this situation."
    hide ep2_sc5_pa_2
    show ep2_sc5_pa_3
    off "I should answer with something positive but... I'm not sure how it will be interpreted."


    menu:
        "Your ass is amazing. [sfLovePath] [sisSubPath]":
            hide ep2_sc5_pa_3
            show ep2_sc5_pa_5

            $ ProcessStat(1, "sis_affection")
            $ ProcessStat(2, "sis_submission")
            $ ProcessStat(1, "sf_affection")
            $ DumpNotStack()
            $ ep2assmagnificient = True
            sis "Amazing?"
            mc "Yes, It's magnificent."
            mc "This swimsuit suits you way better."
            mc "Your ass is now number one on my ass list."
            sis "Are you being sarcastic?"
            mc "You'll never know."


            mc "Maybe I'm joking, or maybe I'm a pervert who lusts on his childhood friend's ass."

            mc "Who knows. What do you prefer?"
            sis "You're crazy."
            mc "Crazy about your ass maybe."
            sis "You don't want to answer, I get it."
            mc "It's spectacular."
            sis "Thank you. You can stop now."
            mc "As you wish Princess."
        "I like it. [sisLovePath]":


            hide ep2_sc5_pa_3
            show ep2_sc5_pa_6

            $ ProcessStat(2, "sis_affection")
            $ ProcessStat(1, "sf_affection")
            $ DumpNotStack()
            $ ep2asslike = True
            sis "You like it? My ass? You're telling me that you like my ass?"
            mc "Yes..."
            sis "I was hoping for a somehow objective and neutral appreciation like: \"this swimsuit suits you better\"."


            sis "What kind of pervert tells his friend he likes her ass?"

            mc "I'm sorry, it's a misunderstanding."
            mc "What I meant to say was that I prefer your ass the way it is."
            mc "With that swimsuit. It suits you way better."
            sis "You're really bad with words."
            mc "I agree it's not my forte."
            sis "You should work on it."
            mc "It's on my list."
        "It's fine I guess.":

            hide ep2_sc5_pa_3
            show ep2_sc5_pa_4
            sis "Fine? Really? Is that all you have to say?"

            mc "Honestly, it's a great ass but I'm not sure it's something I'm supposed to say to a friend."

            sis "Thanks, but the actual question was: Does this swimsuit suit my ass better than the one I wore yesterday?"
            mc "Oh.. yes, it suits you way better."
            sis "I'm glad to hear it."

    off "She sits on her lounge chair and the incident seems to be over."
    off "Just like nothing happened."
    off "[sf_name] smiled the whole time."
    off "They're crazy. Both of them."
    off "But a little crazy is nice, isn't it?"
    scene ep2_sc5_pa_7
    off "I put my sunglasses on a table and spend the next twenty minutes floating in the pool."
    off "We have a friendly and innocent conversation about movies, books, and music."
    hide ep2_sc5_pa_7
    show ep2_sc5_pa_8
    sf "So, [sis_name], what are you cooking tonight?"
    sis "It's a secret. You'll know when you'll have it on your plate."
    sf "Don't you need help?"
    sis "No thank you. There's a couple of ingredients I'll just have to go buy."
    hide ep2_sc5_pa_8
    show ep2_sc5_pa_10
    off "She's looking at me."
    sis "I'll need to take the car to go buy what I need."


    menu:
        "You don't have to ask me, just take it. [sfLovePath]":

            $ ProcessStat(1, "sf_affection")
            if ep2apologizedtosis == True:
                $ ProcessStat(2, "sis_affection")
                $ DumpNotStack()
                sis "Really?"
                mc "Really. Now that I know that you didn't do the things that got you punished in the first place..."
                sis "I'll have to be honest with you. I do drink and drive."
                sis "But never when I'm that drunk. Which happened only a couple times maybe."
                mc "I decided to trust you anyway."
                sis "Thank you."
                off "An awkward silence takes place between us."
            else:
                $ ProcessStat(1, "sis_affection")
                $ DumpNotStack()
                sis "I wasn't asking. I was merely informing you."
                mc "Well, thank you for your kindness I guess..."
                sis "You're welcome."
        "You know you're not supposed to drive it for this summer.":

            sis "Do I look like I care?"
            mc "Look, I know you're being punished unfairly here, but I cannot lift the penalty myself."
            mc "Maybe we can phone to mom and explain the situation..."
            sis "We're not calling, and I'm taking the car."
            mc "Why? I'll support you, we'll talk to her together..."
            sis "You won't tell her anything, at least for the week."
            sis "I don't want to even risk having her coming back here before the end of their trip."
            sis "And I'm taking the car."
            mc "Ok. You'll do as you wish."
        "What will you give me for my silence? [sisSubPath]":


            $ ProcessStat(2, "sis_submission")
            $ DumpNotStack()
            sis "Your silence? Is this a trade or some kind of blackmail? What do you want?"
            mc "What do you have to offer?"
            sis "... How about I let you take a look at [sf_name]'s ass?"
            hide ep2_sc5_pa_10
            show ep2_sc5_pa_12
            sf "Hey! How can you sell my ass so cheaply?"
            sf "You can't sell what you don't own by the way."
            hide ep2_sc5_pa_12
            show ep2_sc5_pa_13
            sf "Don't buy it."
            sf "She's trying to con you."
            mc "Well, I'm interested, but the product seems a bit reluctant."
            hide ep2_sc5_pa_13
            show ep2_sc5_pa_10
            mc "How about this: you take the car and you'll owe me a favour."
            sis "Owing a favour to a pervert, that sounds dangerously foolish."
            $ ep2sisfavour = True
            mc "You like to live dangerously don't you?"
            sis "I'm already sure I'll regret it later. Ok."
            mc "It's a deal then."


    sf "I'll come with you, there're a couple things I need to buy too."
    hide ep2_sc5_pa_10
    show ep2_sc5_pa_9
    off "The girls continue to chat but I don't care anymore."
    off "I'm absorbed by my observation of [sis_name]'s ass again."
    off "For three years now I thought of her as a slut, I imagined her pussy ruined by countless guys while she actually still is a virgin."
    off "No one has gone there yet..."
    off "I'm hard. I'm so easily aroused that this is ridiculous."
    hide ep2_sc5_pa_9
    show ep2_sc5_pa_10
    off "She's looking at me. Did I just get caught again?"
    off "I can't read her expression with these glasses ... which happens to be mine."
    hide ep2_sc5_pa_10
    show ep2_sc5_pa_9
    off "Surprisingly, she turns back to [sf_name] without yelling at me."
    mc "Are those my glasses?"
    hide ep2_sc5_pa_9
    show ep2_sc5_pa_10
    sis "Yeah, I'll hand them back to you don't worry."
    mc "Why should I worry?"
    off "I realize that I haven't seen her with her own shades for a while now."
    mc "Didn't Mom get you some sunglasses too for our last birthday?"
    sis "She did. They got lost about a month ago."
    hide ep2_sc5_pa_10
    show ep2_sc5_pa_13
    sf "More exactly, they got stolen from the locker room at the school's gym."
    mc "What the heck? How is that possible?"
    sf "Fairly simply, someone forced her locker, took the glasses, her phone and got away with it."
    hide ep2_sc5_pa_13
    show ep2_sc5_pa_10
    mc "That's crazy. Why haven't you told us?"
    sis "You wouldn't have cared."
    mc "Come on [sis_name], you have to stop with that."
    mc "I know we failed you as a family by not believing you when this bullshit started, but you can't expect us to support you if you don't tell us anything."
    mc "Each time a rumour came to my ears, without you denying it looked like you were acknowledging it and just didn't care about what I was thinking."
    mc "You should have told us even if it looked pointless."
    sis "What, are you angry at me for that?"
    mc "No, I'm angry at the whole school for harassing you, and at myself, for having ignored it."
    hide ep2_sc5_pa_10
    show ep2_sc5_pa_13
    sf "Calm down, [mc_name]. It's in the past now. High school is over. We'll start a new life in college after this summer. We won't see any of these cunts anymore. Everything will be alright."
    mc "Really? She still has to graduate at the September session for that."
    hide ep2_sc5_pa_13
    show ep2_sc5_pa_10
    sis "I will graduate, I just need a couple more points."

    menu:
        "Oh yes, you will. [sisLovePath] [sfLovePath] [sisSubPath]":
            $ ProcessStat(1, "sis_affection")
            $ ProcessStat(1, "sis_submission")
            $ ProcessStat(1, "sf_affection")
            $ DumpNotStack()
            $ ep2workplanned = True
            mc "There's no way I let you go back to that shit hole."
            mc "You'd better prepare yourself, after this week I'll make you work your ass off to be sure you graduate."
            sis "Ok, hold on your horses here. You're taking it far too personally."

            sis "I appreciate your concern and your new motivation for being my friend but it's still my business, not yours."
            mc "You are my business. It concerns me."
            sis "...Ok... But you can still calm down."
            off "It was the kind of assertion that usually upset her."
            off "I'm quite surprised that she accepted it so easily."
        "I hope so.":

            mc "Because if you don't, you will stay here, alone."
            sis "I know. You don't need to remind me."
            sis "Starting next week, I'll work my ass off to graduate."
            sis "I don't have the slightest doubt."
            mc "Good."

    off "Awkward silence again."
    mc "So.. you like my sunglasses?"
    sis "Yes. They are pretty old school. I like their style."

    menu:
        "You can keep them. [sisLovePath] [sfLovePath]":
            $ ep2glassesoffered = True
            $ ProcessStat(2, "sis_affection")
            $ ProcessStat(2, "sf_affection")
            $ DumpNotStack()
            sis "What?"
            mc "I'm giving these shades to you."
            sis "You can't be serious. These are some 150$ sunglasses."
            sis "And I know you like them. I can't accept it."
        "I can buy you some if you want.":

            $ ProcessStat(1, "sis_affection")
            $ ProcessStat(1, "sf_affection")
            $ DumpNotStack()
            sis "What?"
            mc "I'll buy a new pair of sunglasses for you."
            sis "You can't be serious. These are some 150$ sunglasses."
            sis "I can't accept it."

    mc "Why not?"
    sis "You are going too far."
    sis "Listen, I understand that you have remorse and that you're feeling guilty, I'm actually somehow enjoying it, but you don't have to gift me anything."
    sis "Just stop being a moron and we will be fine."
    off "She gets up, put my sunglasses on the table and walks away."
    sis "Now, If you'll excuse me, I need to visit the bathroom."
    off "She disappears into the house."
    hide ep2_sc5_pa_10
    show ep2_sc5_pa_13

    sf "I like it when you are kind to [sis_name]."
    mc "Well, quite surprisingly, I think I like it too."
    off "She smiles at me before getting out of the pool."
    hide ep2_sc5_pa_13
    show ep2_sc5_pa_15
    off "She dries herself with a towel before applying some cream to her skin."
    sf "I had enough sun for the day. I need to hide in the shadows if I don't want to burn."
    mc "Like a vampire?"
    sf "Almost."
    sf "You see, my skin doesn't tan. It just becomes red and can slowly burn for several days."
    sf "This moisturizer truly is a lifesaver. I wouldn't be able to get out of the house during summer without it."
    mc "Don't you use sunscreen?"
    sf "I do sometimes but it doesn't really prevent me from burning."
    sf "Not exposing myself is the only thing that works."
    mc "That sounds like a pain."
    sf "It is. Do you want to try it?"
    mc "The pain?"
    sf "No, silly, the moisturizer!"
    sf "I'm sure you could use some. Your skin seems to need it."
    mc "Really?"
    sf "Come here, I'll apply some on your back."
    mc "Ok."
    hide ep2_sc5_pa_15
    show ep2_sc5_pa_16
    off "I seat before her and she slowly applies the cream on my back."
    off "Her touch is tender but firm as she massages my shoulders."
    hide ep2_sc5_pa_16
    show ep2_sc5_pa_17
    off "Suddenly, [sis_name] appears before us. She looks a little upset."
    sis "I barely leave you alone for 5 minutes and when I come back, I find you touching each other."
    hide ep2_sc5_pa_17
    show ep2_sc5_pa_18
    sf "I'm just applying some moisturizer on his back."
    sis "I know what you're doing young lady."
    sis "Anyway, let's get ready, we are going in 5 minutes."
    hide ep2_sc5_pa_18
    show ep2_sc5_pa_19
    sf "Already?"
    sis "Yes, already. It's Sunday and we'll probably have to go to the other side of the city to find an open grocery store."
    hide ep2_sc5_pa_19
    show ep2_sc5_pa_20
    sf "See you later [mc_name]!"
    mc "See you later..."

label ep2sc6:

    scene black with dissolve

    if ep2flowerfail == True:
        scene ep2_sc5_mcr_0
        off "I spend most of my afternoon playing video games in my room while the girls are enjoying the pool."
        off "After a while, they take the car and leave the house without a word."
        off "I fucked up pretty badly during our last conversation."
        off "Telling [sis_name] to go get raped on a parking lot was definitely a bad move."
        off "I really have to stop acting like a moron if I want to improve my relationship with them."
        mc "Fuck this game."
        off "I can't concentrate. Even the bots are making fun of me."
    else:
        off "After the girls departed on their quest for a grocery store, I'm left alone in the house."

    scene ep2_sc6_mcr_1
    off "I need to seriously think about what happened."

    off "A guy, or two, drugged my friend at a night club."
    off "We have no proof of that but it seems obvious."
    off "She hadn't drunk that much and [sf_name] had a bad feeling about these guys."
    off "I know it's a pretty shallow argument but... I trust her judgment."
    off "They drugged [sis_name] to rape her."
    off "Why else? Again, we don't have any proof, but I don't have any doubt about it."
    off "And finally one of these guys sent flowers to [sis_name]."
    off "He's trying to cover their tracks by laying doubt in [sis_name]'s mind."
    off "What can I do about that? Find the guy and give him a beating?"
    off "[sf_name] seems to thinks I'm not up to the task."
    off "She's probably right."
    off "There's two of them, and let's be honest, I'm not a brawler."
    off "I'm not good at violence."
    off "I can't go to the cops either, I have no proof, [sis_name] won't go along with me and it would make her even angrier."
    off "So .. There's really nothing I can do besides being there and watch over her... if she allows me to."
    off "I should gather information."
    off "[sf_name] said there was a note with the flowers. Let's find it."
    hide ep2_sc6_mcr_1
    show ep2_sc6_k_0
    off "[sis_name] has thrown the flowers into the trash, in the kitchen."
    off "But I can't find any notes there."
    off "Did she keep it?"
    if ep2flowerfail == True:
        off "Did she really think about giving him a call?"
        off "She's crazy!"
    else:
        off "Why?"
        off "I thought she was resolute not to see him again."

    off "It may be in her room, let's check it."
    hide ep2_sc6_k_0
    show ep2_sc6_sr_0
    off "I finally found the note on the table in her room."
    off "Let's see."
    off "[sis_name], you didn't seem so fine when you left the club last night and it's worrying me. I hope you're doing fine. You can call me at this number. I'd really like to see you again. Luke."
    off "Not much, but still I have his number now."
    off "I put the note back where it was and I'm about to leave the room when something catches my eye."
    hide ep2_sc6_sr_0
    show ep2_sc6_sr_1
    off "I wonder whose panties these are."
    off "Have they been worn?"
    off "I've never smelt a pussy in my life, this is an opportunity."
    off "Shall I?"

    menu:
        "Come on, I'm not a pervert. [sisLovePath] [sfLovePath] [sisSubPath]":
            off "Let's get out of here."
            hide ep2_sc6_sr_1
            show ep2_sc6_mcr_0
            if ep2glassesoffered == True:
                off "Back in my room, I'm thinking about what happened by the pool earlier this afternoon."
                hide ep2_sc6_mcr_0
                show ep2_sc6_mcr_1
                off "I proposed [sis_name] to have my sunglasses and she refused."
                off "But I can buy some for her."
                off "I know she doesn't have any money."
                off "Probably because she had to buy another cell phone to replace the one that has been stolen in her locker along her shades, now that I think of it."
                off "What should I do?"
                menu:
                    "She told me I don't have to gift her anything. [sisLovePath]":
                        off "Well, I'm not sure that I can gift her anything that will make her happy so it probably doesn't matter."
                        off "I'll have to find another way to show that I care for her now."
                    "Let's find some nice shades for my princess.":
                        hide ep2_sc6_mcr_1
                        show ep2_sc6_mcr_5
                        $ ep2shadesordered = True
                        off "These ones are nice..."
                        off "These ones not so much..."
                        off "Haaa, here they are, some old-school vibe-master sunglasses."
                        off "150$ tho."
                        off "I can afford it."
                        off "It's done. It should arrive the day after tomorrow."
                        hide ep2_sc6_mcr_5
                        show ep2_sc6_mcr_1

            off "My cellphone rings."
            off "It's mom."
            off "It's no surprise. She'll probably call us every day or so."
            hide ep2_sc6_mcr_1
            show ep2_sc6_mcr_2


        "Sniff it. [hatePath]" if ep2sfgoneinstead == False:
            hide ep2_sc6_sr_1
            show ep2_sc6_sr_2
            $ UnlockThat("ep2/ep2_sc6_sr_2")
            $ ep2pantiesniffed = True
            off "Holy shit."
            off "So, that's how it smells."
            off "If I was a pervert I probably wouldn't hesitate to steal it."
            off "But I'm not a pervert. Or at least not a thief."
            off "Sniffing it was fun, stealing it is something else."
            off "Remember, [mc_name], behave like an adult."
            off "Let's get out of here."
            hide ep2_sc6_sr_1
            show ep2_sc6_mcr_0
            if ep2glassesoffered == True:
                off "Back in my room, I'm thinking about what happened by the pool earlier this afternoon."
                hide ep2_sc6_mcr_0
                show ep2_sc6_mcr_1
                off "I proposed [sis_name] to have my sunglasses and she refused."
                off "But I can buy some for her."
                off "I know she doesn't have any money."
                off "Probably because she got to buy another cell phone to replace the one that has been stolen in her locker along her shades, now that I think of it."
                off "What should I do?"
                menu:
                    "She told me I don't have to gift her anything. [sisLovePath]":
                        off "Well, I'm not sure that I can gift her anything that will make her happy so it probably doesn't matter."
                        off "I'll have to find another way to show that I care for her now."
                    "Let's find some nice shades for my princess.":
                        hide ep2_sc6_mcr_1
                        show ep2_sc6_mcr_5
                        $ ep2shadesordered = True
                        off "These ones are nice..."
                        off "These ones not so much..."
                        off "Haaa, here they are, some old-school vibe-master sunglasses."
                        off "150$ tho."
                        off "I can afford it."
                        off "It's done. It should arrive the day after tomorrow."
                        hide ep2_sc6_mcr_5
                        show ep2_sc6_mcr_1

            off "My cellphone rings."
            off "It's mom."
            off "It's no surprise. She'll probably call us every day or so."
            hide ep2_sc6_mcr_1
            show ep2_sc6_mcr_2



        "Sniff it. [hatePath]" if ep2sfgoneinstead == True:
            hide ep2_sc6_sr_1
            show ep2_sc6_sr_2
            $ UnlockThat("ep2/ep2_sc6_sr_2")
            $ ep2pantiesniffed = True
            off "Holy shit."
            off "So, that's how it smells."
            off "I could take it... for ... further investigation."
            off "I'm sure it'll go unnoticed."
            menu:
                "Nope.":
                    off "Sniffing it was fun, stealing it is something else."
                    off "Remember, [mc_name], behave like an adult."
                    off "Let's get out of here."
                    hide ep2_sc6_sr_1
                    show ep2_sc6_mcr_0
                    if ep2glassesoffered == True:
                        off "Back in my room, I'm thinking about what happened by the pool earlier this afternoon."
                        hide ep2_sc6_mcr_0
                        show ep2_sc6_mcr_1
                        off "I proposed [sis_name] to have my sunglasses and she refused."
                        off "But I can buy some for her."
                        off "I know she doesn't have any money."
                        off "Probably because she got to buy another cell phone to replace the one that has been stolen in her locker along her shades, now that I think of it."
                        off "What should I do?"
                        menu:
                            "She told me I don't have to gift her anything. [sisLovePath]":
                                off "Well, I'm not sure that I can gift her anything that will make her happy so it probably doesn't matter."
                                off "I'll have to find another way to show that I care for her now."
                            "Let's find some nice shades for my princess.":
                                hide ep2_sc6_mcr_1
                                show ep2_sc6_mcr_5
                                $ ep2shadesordered = True
                                off "These ones are nice..."
                                off "These ones not so much..."
                                off "Haaa, here they are, some old-school vibe-master sunglasses."
                                off "150$ tho."
                                off "I can afford it."
                                off "It's done. It should arrive the day after tomorrow."
                                hide ep2_sc6_mcr_5
                                show ep2_sc6_mcr_1

                    off "My cellphone rings."
                    off "It's mom."
                    off "It's no surprise. She'll probably call us every day or so."
                    hide ep2_sc6_mcr_1
                    show ep2_sc6_mcr_2
                "No one will ever know. [hatePath]":
                    $ ep2pantietaken = True
                    off "I'll bring it back later, once I'm finished with my... research."
                    hide ep2_sc6_sr_2
                    show ep2_sc6_mcr_0
                    off "Speaking of which, I have an idea."
                    off "I have that broken drone somewhere, with a tiny camera on it."
                    off "I haven't used it for years but maybe I can use it to study what happens in the bathroom when the girls shower together."
                    off "If I can salvage the camera, it can even broadcast to my phone..."
                    off "..."
                    off "Ten minutes later, I finally found the drone in my closet and retrieve its camera."
                    hide ep2_sc6_mcr_0
                    show ep2_sc6_br_0
                    off "Ok, last chance to be a decent human being."
                    off "Do I really want to do that?"
                    menu:
                        "That's so wrong.":
                            off "They barely trust me."
                            off "I can't betray them like that."
                            off "Let's go back to my room."
                            hide ep2_sc6_br_0
                            show ep2_sc6_mcr_0
                            off "I can't believe I stole those panties tho."
                        "Fuck yes! [hatePath]":
                            $ ep2cameraset = True
                            off "Alright, I just need to find a place to hide it."
                            off "I want to see what happens in the shower so..."
                            hide ep2_sc6_br_0
                            show ep2_sc6_br_1
                            off "Maybe here... Yes... That should work."
                            off "If I set it that way..."
                            off "Let's see."
                            hide ep2_sc6_br_2
                            show ep2_sc6_br_2
                            off "That will do."
                            off "Great."
                            off "Let's go back to my room."
                            hide ep2_sc6_br_2
                            show ep2_sc6_mcr_0
                            off "I can't believe I did that."

                    off "If I get caught I'm dead."
                    off "I don't care. Be bold, be brave! Go forth! "
                    hide ep2_sc6_mcr_0
                    show ep2_sc6_mcr_3
                    off "Let's celebrate by using my newfound treasure now that I can finally fap to my hearts content."
                    off "Oh shit, oh shit, oh shit."
                    off "That pussy smells so good!"
                    off "I'm about to come when my phone rings."
                    off "Fuck you!"
                    off "The world has united to prevent me from successfully jerking off today."
                    off "Even better, it's mom calling."
                    hide ep2_sc6_mcr_3
                    show ep2_sc6_mcr_4





    mc "Hello."
    mom "Hello [mc_name], It's mom."
    mc "Hello mom."
    mom "How are things going at home?"
    off "I should be careful with what I say."
    off "I can't tell her what happened to [sis_name] or she will worry like hell and immediately come back."
    mc "We're doing fine mom."
    if ep2apologizedtosis == True:
        mc "We invited [sf_name] to stay with us for the week."
    else:
        mc "[sis_name] invited [sf_name] to stay with us for the week."
    mom "The whole week?"
    mc "Yes, Mom, don't worry. You know [sf_name], she's nice."
    mc "She seems determined to reconcile me with [sis_name]."

    if ep2flowerfail==False:
        if ep2apologizedtosis == True:
            mc "She may have succeeded."
        else:
            mc "She could succeed."

    mom "Well, if she can prevent you from killing each other at least, it will already be a great feat."
    mom "Anyway, where is she sleeping?"
    mc "She sleeps with [sis_name]."
    mom "It'll be more comfortable for her to sleep in our bedroom."
    mom "Tell her to be at ease."
    mc "Ok, mom, I'll tell her. How is your trip going?"
    mom "Well, it's going fine for now."
    mom "Your father's symposium starts only tomorrow in the morning."
    mom "We'll be back next Sunday as expected."
    mc "I hope you'll have fun."
    mom "I have to hang up now."
    mom "Take care [mc_name], you are the man of the house for this week."


    mom "Kiss [sis_name] for me."

    mc "Sure, mom... See you next Sunday..."

    scene black with dissolve

    off "I have barely hung up the phone when I hear the girls coming back."
    off "I should let [sis_name] know that mom has called."
    if ep2pantietaken == True:
        off "I'd better put my shorts back on before I talk to her."


label ep2sc7:
    scene black with dissolve

    off "I find [sis_name] alone in the kitchen."
    if ep2flowerfail == True:
        show ep2_sc7_k_3
    else:
        show ep2_sc7_k_2
    mc "Hey, [sis_name]."
    sis "What do you want?"
    if ep2flowerfail == True:
        menu:
            "Apologize [sisLovePath]":
                $ ep2flowersorry = True

                $ ProcessStat(1, "sis_affection")
                $ DumpNotStack()
                mc "I'm sorry. I didn't mean what I said this afternoon."
                sis "I know."
                mc "You know?"
                sis "Yes."


                sis "No one in its right mind would really wish his friend to go get raped on a parking lot."

                sis "Or at least I hope so."
                sis "But it doesn't dispense you of apologizing."
                mc "I'm doing it right now. I'm sorry."
                sis "Good."
                mc "Mom called while you were out."
            "Don't apologize":
                mc "Mom called while you were out."
        hide ep2_sc7_k_3
        show ep2_sc7_k_2
    else:
        mc "Mom called while you were out."
    sis "You told her."
    menu:
        "No, I didn't. [sisLovePath]":

            $ ProcessStat(1, "sis_affection")
            $ DumpNotStack()
            mc "I told her we were doing fine and that everything was alright."
            mc "I don't like lying to mom but I did it anyway."
            sis "Thank you, [mc_name]."
        "No, I didn't. For now. [sisSubPath]":

            $ ProcessStat(1, "sis_affection")
            $ ProcessStat(2, "sis_submission")
            $ DumpNotStack()
            mc "I told her we were doing fine and that everything was alright."
            mc "I lied to her for you."
            mc "I don't like that."
            mc "I don't know if I can do that again the next time she calls."
            sis "Please, [mc_name]."


            sis "If you tell her, she will come back immediately and your parents will probably never leave us alone here again."

            sis "You know that."
            mc "I know. I still don't like lying to mom."
            sis "Ok, what do you want me to do? Is there anything?"
            mc "Just be grateful."
            hide ep2_sc7_k_2
            show ep2_sc7_k_4
            sis "I am, I assure you I am grateful to you."
            mc "Well, that wasn't obvious."
            sis "...Ok, I'll try to be more explicit next time."

    scene ep2_sc7_k_1
    if ep2apologizedtosis == True:
        mc "I also told her that we invited [sf_name] for the week."
    else:
        mc "I also told her that you invited [sf_name] for the week."
    mc "She's ok with that."
    mc "She said that [sf_name] can sleep in their bedroom if she wants to."
    mc "It will be more comfortable for her."
    mc "As you see you could have asked her beforehand, she would have been ok with it."
    sis "I'm not sure about that."
    mc "Well, anyway, it's done."
    sis "Great. Anything else?"
    mc "I don't think so..."
    hide ep2_sc7_k_1
    show ep2_sc7_k_2
    sis "Then get out of the kitchen so I can cook."
    mc "Can I help you?"
    sis "No, you can't. Get out."
    mc "Ok, ok ..."

    scene black with dissolve
    show ep2_sc7_l_0
    off "Being banned from the kitchen, I go to the living room where [sf_name] is leisurely lying on the sofa, reading a book."
    mc "Hey [sf_name]."
    sf "Hey. Just let me finish this paragraph, please."
    mc "Of course. Sorry to disturb you."
    hide ep2_sc7_l_0
    show ep2_sc7_l_1
    sf "You're not disturbing me if you let me finish this paragraph."
    mc "I sit on a couch and wait patiently for a minute or so before she put the book aside and turns to me."
    hide ep2_sc7_l_1
    show ep2_sc7_l_2
    if ep2flowersorry == True:

        $ ProcessStat(1, "sf_affection")
        $ DumpNotStack()
        mc "I wanted to apologize."
        sf "To me?"
        mc "Yes. I already talked with [sis_name]."
        mc "You're right, I'm a moron and I need to grow up. I'm sorry."
        sf "The first step in solving any problem is recognizing there is one."
        sf "Maybe you're ready to move on."
        mc "I hope so."

    mc "So ... what are you reading?"
    sf "I doubt it'll interest you. it's just a girl's book."
    sf "Romance and stuff."
    mc "Oh... I see..."
    sf "No, you don't. I can see you're imagining things."
    sf "It's not that kind of book."
    mc "Really? The ones I have read were pretty explicit."
    hide ep2_sc7_l_2
    show ep2_sc7_l_3
    sf "Because you have read some? Why?"
    sf "They're not exactly marketed towards young guys."
    mc "Well, it was .. for research purposes. I know it's stupid."
    sf "I think I need some more details."
    sf "What kind of research?"
    mc "Well... I thought that by reading that kind of book I would be able to understand what girls like..."
    sf "Were you successful?"
    mc "Honestly? No."
    hide ep2_sc7_l_3
    show ep2_sc7_l_4
    sf "My poor [mc_name], I have the feeling you're not doing great with the ladies."
    mc "I'm doing great actually."
    mc "It's just that sometimes..."
    mc "Girls are hard to understand, sometimes they seem to like you and the next day they despise you."
    mc "It's hard to deal with someone who changes her mind at least once a day."
    mc "If you have some insight about how to behave with a girl, I will be grateful."
    sf "It's actually pretty simple, [mc_name]."
    sf "Just read the mood and behave accordingly."
    mc "But how do I read the mood?"
    hide ep2_sc7_l_4
    show ep2_sc7_l_5
    sf "Like with everyone else."
    sf "It's called empathy."
    sf "If you're a normal human being you're supposed to have empathy."
    mc "I think I can read guys easily but it's much harder with girls, almost impossible."
    sf "You may need some practice. Experience is important."
    sf "You try, you fail, you learn."
    sf "That's also part of the game: when in doubt, try."
    sf "What do you have to lose?"
    mc "That's funny. Steve told me something similar yesterday."
    sf "Even Steve is capable of saying sensible things sometimes."
    mc "Surprisingly. So... practice and experience."
    mc "When in doubt: try. Ok. I can do that."
    menu:
        "Kiss her. [sfLovePath] [sisLovePath]":
            off "I get up and take a step towards [sf_name]."
            off "I gently grab her by the shoulders."
            if ep2sfgoneinstead == False and sf_affection > 13:
                hide ep2_sc7_l_5
                show ep2_sc7_l_6_ak
                $ UnlockThat("ep2/ep2_sc7_l_6_ak")
                $ ep2kissedsf = True

                $ ProcessStat(5, "sf_affection")
                $ ProcessStat(2, "sis_affection")
                $ DumpNotStack()
                off "My lips join with hers."
                off "This is your first kiss, man, don't fuck this up."
                off "She looks a bit surprised but she seems to enjoy the kiss as much as I do."
                off "I'm actually so stressed out that I can't really appreciate the kiss."
                off "It lasts a handful of seconds."
                hide ep2_sc7_l_6_ak
                show ep2_sc7_l_7
                sf "Well, that was surprising... and a bit bold.... but not unpleasant."
                sf "And short, definitely too short."
                mc "Should we do it again?"
                off "[sis_name]'s voice interrupts us."
                sis "Dinner is served! Hurry before it gets cold!"

                sf "It looks like [sis_name] decided otherwise."
                hide ep2_sc7_l_7
                show ep2_sc7_l_16
                sf "We should resume this conversation later."
                mc "I'm looking forward to it."


                sf "You heard [sis_name]. We shouldn't make her wait."
            else:

                hide ep2_sc7_l_5
                show ep2_sc7_l_6_a
                $ ep2sfkissfail = True

                $ ProcessStat(1, "sf_affection")
                $ DumpNotStack()
                off "She stops me before I reach her lips."
                sf "You're moving too fast. Did you read the mood?"
                hide ep2_sc7_l_6_a
                show ep2_sc7_l_8
                mc "I was in doubt so ... I tried."
                sf "Well, you failed."
                sf "But it's not the end of the world."
                sf "It may just require a bit more work."
                mc "I'll keep that in mind..."
                off "[sis_name]'s voice interrupts us."
                sis "Dinner is served! Hurry before it gets cold!"
                off "Thank god, [sis_name]'s call put an end to my humiliation."
                hide ep2_sc7_l_8
                show ep2_sc7_l_16

                sf "You heard [sis_name]. We shouldn't make her wait."
        "Would you like a foot massage? [sisSubPath] [sfDomPath]":

            hide ep2_sc7_l_5
            show ep2_sc7_l_9

            $ ProcessStat(2, "sf_affection")
            $ ProcessStat(1, "sis_affection")
            $ ProcessStat(1, "sis_submission")
            $ DumpNotStack()
            $ ep2footmassage = True
            sf "A foot massage?"
            sf "Where does this idea come from?"
            sf "Do you often propose foot massage to girls?"
            mc "Not really."
            mc "I saw that you have adopted the habit of walking through the house barefoot."
            mc "I don't know why but I thought that you may enjoy a foot massage."
            mc "So I proposed it."
            sf "You are not one of those foot perverts or anything like that?"
            mc "No, I'm not."
            sf "... Why not then? To be honest I've never had my feet massaged."
            sf "Actually, I've never been massaged by a guy."
            hide ep2_sc7_l_9
            show ep2_sc7_l_10
            off "I get up and join her on the sofa where we quickly found a position comfortable for both of us."
            off "I start massaging her right foot. Slowly, softly."
            mc "Tell me if I do anything displeasing."
            mc "I don't want to cause any discomfort."
            hide ep2_sc7_l_10
            show ep2_sc7_l_11
            sf "It's alright. I didn't know you had experience in this kind of thing."
            mc "You'd be surprised."
            off "It's actually my first time touching a girl's body."
            off "I have absolutely no idea what I'm doing."
            sf "It's very relaxing."
            off "I move my thumb a little, apply a bit more strength."
            hide ep2_sc7_l_11
            show ep2_sc7_l_12
            sf "Oh god! Is that supposed to be so good?"
            off "I simply look at her face and massage her randomly."
            off "If she seems to like a spot, I press it a little harder."
            sf "Oooooooh, don't stop don't stop don't stop!"
            off "I barely understand what's happening when she starts yelling."
            off "I'm getting a boner."
            hide ep2_sc7_l_12
            show ep2_sc7_l_13
            $ UnlockThat("ep2/ep2_sc7_l_13")
            sf "Please, please, please don't stop!"
            sf "Right there! Yes! Yes! Yeeeeeees!"
            sf "Oh my goooood!"
            off "Is she having an orgasm?"
            off "Did I give her an orgasm by massaging her foot?"
            off "Holy shit."
            hide ep2_sc7_l_13
            show ep2_sc7_l_14
            sis "What the fuck are you pervs doing?"
            off "[sis_name] surprises us while [sf_name] is still moaning from pleasure."
            off "Her foot is still in my hands."
            off "My dick goes flat."
            sis "Come here, both of you."
            hide ep2_sc7_l_14
            show ep2_sc7_l_15
            sis "So? Care to explain what happened? Who do I have to spank?"
            sf "He was just massaging my feet..."
            sis "And you started yelling out of relaxation?"
            sf "Quite surprisingly... Yes."
            off "I realize that I feel like a child scolded by his mother."
            off "[sf_name] probably feels the same."
            sis "Listen to me pervs, if I find you again doing something naughty, I will spank you. Am I clear?"
            mc "Yes, ma'am."
            sis "Now get to the kitchen. Dinner is served."
        "Thank you.":
            mc "Well, thank you for your advice."
            mc "I'll try to make good use of it."
            sf "You're welcome."
            sf "I'm sure you'll do fine."
            off "[sis_name]'s voice interrupts our conversation."
            sis "Dinner is served! Hurry before it gets cold!"
            off "We diligently answer the call and head to the kitchen."

label ep2sc8:
    scene black with dissolve
    show ep2_sc8_k_0 with dissolve
    off "[sis_name] is excited."
    off "We approach the table with a bit of apprehension."
    off "Something has burnt in this kitchen."
    hide ep2_sc8_k_0
    show ep2_sc8_k_1
    sis "Tadaaa! Salmon à la printanière."
    sis "Or something like that, I don't remember the exact name. It's French."
    off "She looks happy."
    sis "Come on, don't be shy! Tell me what you think? Is it good?"
    hide ep2_sc8_k_1
    show ep2_sc8_k_3
    off "It looks awful."
    off "The salmon is almost black, and the whole thing doesn't smell so good."
    hide ep2_sc8_k_3
    show ep2_sc8_k_4
    off "[sf_name] takes a bite. It looks difficult to chew."
    sf "It's... How to put that? ... unconventional?"
    sis "You don't like it?"
    sf "I'm not used to French cuisine, but it's good."
    off "The fish is totally burnt, the sauce is so salty that I'm afraid for my heart and the vegetables manage to be crude and chewy at the same time."
    hide ep2_sc8_k_4
    show ep2_sc8_k_5
    sis "What about you? Do you like it?"
    mc "What did you put in that sauce?"
    sis "It's a secret."
    off "She finally taste her own plate."
    hide ep2_sc8_k_5
    show ep2_sc8_k_6
    off "Her attitude completely changes."
    off "She looks like she's about to cry."
    sis "Oh my god, it's disgusting. I failed everything."
    off "Here we are."
    off "What do I say? The truth will probably destroy her."
    menu:
        "You'll do better next time.":
            sis "There won't be a next time. I'm sorry."
            hide ep2_sc8_k_6
            show ep2_sc8_k_12
            off "She stands up and rushes out of the kitchen."
            hide ep2_sc8_k_12
            show ep2_sc8_k_14
            sf "I didn't know what to expect, but honestly, I didn't think she could be that bad in the kitchen."
            mc "Me neither. And she seemed surprised as well."
            sf "I'm gonna go talk to her. She was about to cry and I don't like that."
        "I don't know what you're talking about. [sisLovePath] [sfLovePath]":

            $ ProcessStat(2, "sf_affection")
            $ ProcessStat(2, "sis_affection")
            $ DumpNotStack()
            $ ep2mealeated = True
            hide ep2_sc8_k_6
            show ep2_sc8_k_7
            mc "It's delicious."
            off "She doesn't understand immediately."
            off "Both girls are looking at me, confused, while I stuff my mouth with the salmon."
            mc "I won't say it's the best salmon I ever had, but it's still pretty good."
            sis "You don't have to do that, [mc_name]."
            mc "Do what?"
            sis "Eating that disaster."
            mc "I told you I liked it."
            hide ep2_sc8_k_7
            show ep2_sc8_k_8
            mc "The vegetables are a bit chewy, but they are tasty."
            hide ep2_sc8_k_8
            show ep2_sc8_k_9
            mc "And the sauce is salty, but it's okay, I like salty."
            hide ep2_sc8_k_9
            show ep2_sc8_k_10
            off "I eat until my plate is totally empty."
            off "The girls also took a couple bit from their plate."
            hide ep2_sc8_k_10
            show ep2_sc8_k_11
            mc "That was good. I'm stuffed. That was exquisite."
            mc "You can do that again whenever you want, Princess."
            sis "As if. It's the last time I even try to cook."
            sf "Come on, it wasn't perfect, but at least you tried, and you learned, next time you will do better."
            mc "And I'll eat it anyway."
            sis "I'm sorry that you had to taste that thing."
            mc "Again, I don't know what you're talking about."
            mc "Now if you'll excuse me, I have some dishes to wash."


label ep2sc9:

    scene black with dissolve
    with Pause(2)
    show text "Later that evening."
    with Pause(2)
    hide text
    off "I have been watching TV for an hour now."
    off "I'm bored."
    off "I wonder how Steve is doing. His vacation seemed rather interesting."
    show ep2_sc9_l_0 with dissolve
    off "I'm about to go to my room when the girls invade the living room."
    sf "Hey [mc_name]."
    mc "Hey."
    sf "Are you doing something interesting?"
    mc "Not really."
    sf "[sis_name] and I were chatting upstairs when we had an idea."
    sf "We're going to spend the week together so we thought that it could be nice to know each other better."

    sf "Because, to be honest, I don't know you much, and [sis_name] doesn't know you better besides the fact that you are a moron."

    mc "Ok, can we stop with the moron thing? I thought we were past that."
    mc "If we all agree about that, maybe can we move on?"
    mc "I don't think you need to remind me every time we have a conversation."
    sis "I think we can make an effort."
    mc "Great."
    sf "So... back to our topic."
    sf "We don't really know you, and we are sure you don't really know us."
    sf "So we thought it would be nice to.. remedy the situation with a game."
    mc "Ok... can you be more explicit?"
    if ep1beer == True:
        sf "Well, we have these beers and we have questions so we thought that we could play a small drinking game."
    elif ep1vodka == True:
        sf "Well, we have this vodka and we have questions so we thought that we could play a small drinking game."
    else:
        sf "Well, we have this wine and we have questions so we thought that we could play a small drinking game."

    mc "A drinking game, really? Like truth or drink?"
    sf "Yes, somehow. You drink to ask, everyone answers, you drink if you don't want to answer."
    sf "No shame, no judgment, everything we say stays between us. What do you think?"
    off "That sounds awful."
    off "I can't see how this game can end well for me and yet I can't decline or I will look like I have tons of shameful things to hide."
    mc "That it sounds like a trap but ... why not?"
    if ep1beer == True:
        scene ep2_sc9_l_1_b_mc_sf
    elif ep1vodka == True:
        scene ep2_sc9_l_1_v_mc_sf
    else:
        scene ep2_sc9_l_1_w_mc_sf
    sf "Alright! Let's get comfortable and start with some innocent questions first."
    sf "The nasty ones shouldn't come before a couple drinks."
    mc "Of course."
    sf "I'll go first."
    if ep1beer == True:
        scene ep2_sc9_l_sf_beer
    elif ep1vodka == True:
        scene ep2_sc9_l_sf_vodka
    else:
        scene ep2_sc9_l_sf_wine
    off "She actually drinks quite a lot."
    if ep1beer == True:
        scene ep2_sc9_l_1_b_mc_sf
    elif ep1vodka == True:
        scene ep2_sc9_l_1_v_mc_sf
    else:
        scene ep2_sc9_l_1_w_mc_sf

    sf "So... What is .. your favourite movie?"
    sf "Mine is probably ... Lost in translation."
    sf "I don't really know why but .. that's my favourite."
    sf "What about you, [sis_name]?"
    sis "I like Casablanca."
    if ep1beer == True:
        scene ep2_sc9_l_1_b_sis_mc
    elif ep1vodka == True:
        scene ep2_sc9_l_1_v_sis_mc
    else:
        scene ep2_sc9_l_1_w_sis_mc
    mc "That old black and white movie?"
    sis "I like old movies. There's something about their rhythm that I really find appealing."
    sis "What about you?"
    menu:
        "[gr]Star Wars.":
            mc "I don't think it needs any further explanation."
            sf "I didn't think you were the nerd type."
            mc "Star Wars is not a nerd thing, it's universal."
            sis "Yeah sure..."
        "[gr]Fast and Furious Tokyo Drift.":
            mc "I don't think it needs any further explanation."
            sis "Actually, it needs a lot. Why this one?"
            mc "Cars, girls, drift."
            sf "No surprise there."
        "Drink.":
            $ ep2drinkgamecounter += 1
            if ep1beer == True:
                scene ep2_sc9_l_mc_beer
            elif ep1vodka == True:
                scene ep2_sc9_l_mc_vodka
            else:
                scene ep2_sc9_l_mc_wine
            sf "You choose to drink on such a trivial question?"
            mc "I'm actually thirsty."
            sf "It's your call."

    sis "My turn."
    if ep1beer == True:
        scene ep2_sc9_l_sis_beer
    elif ep1vodka == True:
        scene ep2_sc9_l_sis_vodka
    else:
        scene ep2_sc9_l_sis_wine
    off "The idea seems to drink a whole shot worth of alcohol every time."
    off "These girls are going to get me drunk."
    if ep1beer == True:
        scene ep2_sc9_l_1_b_sis_mc
    elif ep1vodka == True:
        scene ep2_sc9_l_1_v_sis_mc
    else:
        scene ep2_sc9_l_1_w_sis_mc
    sis "How many times did you get drunk? I mean really drunk."
    sis "I think I drank my first beer when I was 16 and since then I got drunk two times."
    sis "No wait, three actually, three times. I was with you every time, [sf_name]."
    if ep1beer == True:
        scene ep2_sc9_l_1_b_sf_mc
    elif ep1vodka == True:
        scene ep2_sc9_l_1_v_sf_mc
    else:
        scene ep2_sc9_l_1_w_sf_mc
    sf "I remember each of those."
    sf "I think I only got really drunk only once, it was not intentional."
    menu:
        "Not once (Lie). [hatePath]":

            $ ProcessStat(-1, "sf_affection")
            $ ProcessStat(-1, "sis_affection")
            $ DumpNotStack()
            mc "What did you expect? You know I don't drink much."
            mc "I drink occasionally but I always take care not to go too far."
            sis "That's some nice self-control."
            mc "Thank you. By the way, you are aware that you weren't supposed to drink before your eighteenth birthday, right?"
            sis "We said no judgment, remember?"
            mc "I do, I wasn't judging, just... merely informing you..."
            sis "Sure."
        "A couple times (Truth). [sisLovePath] [sfLovePath]":

            $ ProcessStat(1, "sf_affection")
            $ ProcessStat(1, "sis_affection")
            $ DumpNotStack()
            if ep1beer == True:
                scene ep2_sc9_l_1_b_sis_mc
            elif ep1vodka == True:
                scene ep2_sc9_l_1_v_sis_mc
            else:
                scene ep2_sc9_l_1_w_sis_mc
            sis "Really?"
            sis "I didn't think it had ever happened to you drinking more than a couple of beers in a row."
            mc "You'd be surprised."
            sis "I am already. Tell us more, please!"
            mc "There's not much to tell."
            mc "The nights we spend in Steve's garage are sometimes a bit wild."
            sis "Good to know."
        "Drink.":

            $ ep2drinkgamecounter += 1
            if ep1beer == True:
                scene ep2_sc9_l_mc_beer
            elif ep1vodka == True:
                scene ep2_sc9_l_mc_vodka
            else:
                scene ep2_sc9_l_mc_wine
            sf "We may never know if you have been drunk before but you will probably be tonight if you keep going on like this..."
    if ep1beer == True:
        scene ep2_sc9_l_1_b_sis_mc
    elif ep1vodka == True:
        scene ep2_sc9_l_1_v_sis_mc
    else:
        scene ep2_sc9_l_1_w_sis_mc
    sis "It's your turn, [mc_name]."
    $ ep2drinkgamecounter += 1
    if ep1beer == True:
        scene ep2_sc9_l_mc_beer
    elif ep1vodka == True:
        scene ep2_sc9_l_mc_vodka
    else:
        scene ep2_sc9_l_mc_wine
    mc "Ok..."
    if ep1beer == True:
        scene ep2_sc9_l_1_b_mc_sf
    elif ep1vodka == True:
        scene ep2_sc9_l_1_v_mc_sf
    else:
        scene ep2_sc9_l_1_w_mc_sf
    mc "So... Do you pee in the shower?"
    mc "I do sometimes..."
    sf "Like every guy probably."
    sis "I do it too."

    $ ProcessStat(1, "sis_affection")
    $ DumpNotStack()






    sf "Really? Please, tell me you are not doing it when I'm showering with you."
    sis "Well..."
    sf "This is the end of our friendship."
    sis "I know you secretly enjoy it."
    scene black with dissolve
    off "After a couple more turns of innocent questions and a couple more drinks, it's time to dive into some more serious waters."
    if ep1beer == True:
        scene ep2_sc9_l_sf_beer
    elif ep1vodka == True:
        scene ep2_sc9_l_sf_vodka
    else:
        scene ep2_sc9_l_sf_wine
    off "[sf_name] told us that she doesn't stand alcohol very well, yet, she drinks without hesitation."
    if ep1beer == True:
        scene ep2_sc9_l_2_b_sf_mc
    elif ep1vodka == True:
        scene ep2_sc9_l_2_v_sf_mc
    else:
        scene ep2_sc9_l_2_w_sf_mc
    sf "Are you a virgin? [mc_name]?"
    off "Here it goes."
    off "Shit."
    off "I can't drink this one out, there would be no difference with confessing I am indeed a virgin."
    menu:
        "I am (Truth). [sisLovePath] [sfLovePath]":

            $ ProcessStat(2, "sf_affection")
            $ ProcessStat(2, "sis_affection")
            $ DumpNotStack()
            sf "And I am too. What about you [sis_name]?"
            if ep1beer == True:
                scene ep2_sc9_l_2_b_sf_sis
            elif ep1vodka == True:
                scene ep2_sc9_l_2_v_sf_sis
            else:
                scene ep2_sc9_l_2_w_sf_sis
            sis "Of course, I'm a virgin."
            sis "What kind of girl do you think I am?"
            off "That was unexpected."
            off "What was I ashamed of? Everyone's a virgin."
            off "I'm pretty relieved to know that I'm not the only one in this house who has 0 experience in these matters."
        "I am not (Lie). [sisSubPath]":

            $ ProcessStat(-2, "sf_affection")
            $ ProcessStat(-2, "sis_affection")
            $ ProcessStat(2, "sis_submission")
            $ DumpNotStack()
            $ ep2virginlie = True
            if ep1beer == True:
                scene ep2_sc9_l_2_b_sf_mc_c
            elif ep1vodka == True:
                scene ep2_sc9_l_2_v_sf_mc_c
            else:
                scene ep2_sc9_l_2_w_sf_mc_c
            sf "Really?"
            off "They look surprised and confused."
            sis "Just to be sure, you're telling us that you had sex with another human being?"
            mc "That's what I said, yes."
            sf "We're going to need more details here."
            sis "We want to know everything."
            sf "With who, when?"
            off "What do I say? How am I gonna get out of this? Another lie?"
            menu:
                "Sandy, during the last school trip...":

                    $ ProcessStat(-1, "sf_affection")
                    $ ProcessStat(-1, "sis_affection")
                    $ DumpNotStack()
                    if ep1beer == True:
                        scene ep2_sc9_l_2_b_mc_sis
                    elif ep1vodka == True:
                        scene ep2_sc9_l_2_v_mc_sis
                    else:
                        scene ep2_sc9_l_2_w_mc_sis
                    sis "What?! Are you kidding us? Sandy, from our French class?"
                    mc "Yes..."
                    sis "How come I wasn't aware of you dating her?"
                    mc "We didn't date, it was ... a one-time thing..."
                    sf "A one-time thing?"
                    off "They look pretty sceptical about that, I may have gone too far with my lie."
                    off "I need a diversion."
                "[gr]Do I really have to answer that?":
                    $ ep2drinkgamecounter += 1
                    if ep1beer == True:
                        scene ep2_sc9_l_mc_beer
                    elif ep1vodka == True:
                        scene ep2_sc9_l_mc_vodka
                    else:
                        scene ep2_sc9_l_mc_wine
                    mc "I'll drink through it if you don't mind."
                    sf "Come on! You can't leave us hanging like that!"
                    mc "Oh yes, I can."

                    $ ProcessStat(-1, "sf_affection")
                    $ ProcessStat(-1, "sis_affection")
                    $ DumpNotStack()

            if ep1beer == True:
                scene ep2_sc9_l_2_b_sf_mc
            elif ep1vodka == True:
                scene ep2_sc9_l_2_v_sf_mc
            else:
                scene ep2_sc9_l_2_w_sf_mc
            mc "By the way, what about you ladies?"
            sf "Well, I am still a virgin."
            sis "And I am too, of course, what kind of girls do you think we are?"
            mc "Virtuous ones, of course."
            off "They answered with a kind of pride in their voice."
            off "I am ashamed of my lie."

    sis "Ok guys my turn."
    if ep1beer == True:
        scene ep2_sc9_l_sis_beer
    elif ep1vodka == True:
        scene ep2_sc9_l_sis_vodka
    else:
        scene ep2_sc9_l_sis_wine
    off "She's probably the one who drank the most and she seems to be the least drunk."
    off "She sure can handle her liquor better than I do."
    if ep1beer == True:
        scene ep2_sc9_l_2_b_mc_sis
    elif ep1vodka == True:
        scene ep2_sc9_l_2_v_mc_sis
    else:
        scene ep2_sc9_l_2_w_mc_sis
    sis "How often, do you masturbate? [mc_name]?"
    off "Great, another occasion to show myself as the glorious pervert I secretly am."
    menu:
        "One or two times a week I guess (Lie).":
            sis "You're telling us that a healthy 18-year-old man masturbate only once or twice a week?"
            mc "I don't know about the others but that's what I do."
            sis "Is your junk working correctly?"
            sis "I thought that young guys like you were supposed to be horny 24/7."
            mc "Well, some of us know.. self-control."
            if ep1beer == True:
                scene ep2_sc9_l_2_b_sis_sf
            elif ep1vodka == True:
                scene ep2_sc9_l_2_v_sis_sf
            else:
                scene ep2_sc9_l_2_w_sis_sf
            sis "What about you [sf_name]?"
            sf "I'll drink."
            sf "I do not want to damage the nice girl image I've been cultivating for so long with this kind of details."
            sis "You're doing it that much? You naughty girl."
            sf "You'll never know for sure."
            sis "There's nothing to be ashamed of here!"
            sis "I do it maybe 3 times a week? Sometimes more."
            sis "It depends on the mood."
        "[gr]4 to 5 times a week maybe (Truth).":

            $ ProcessStat(1, "sf_affection")
            $ ProcessStat(1, "sis_affection")
            $ ProcessStat(1, "sis_submission")
            $ DumpNotStack()
            $ ep2masturbatetruth = True
            mc "Sometimes more, sometimes less."
            sis "I'm not surprised. I can hear you through the walls."
            mc "What? Seriously? You can hear me jerking off?"
            sis "Among other things, yes."
            mc "Shit..."
            if ep1beer == True:
                scene ep2_sc9_l_2_b_sis_sf
            elif ep1vodka == True:
                scene ep2_sc9_l_2_v_sis_sf
            else:
                scene ep2_sc9_l_2_w_sis_sf
            sis "What about you [sf_name]?"
            sf "I'll drink."
            sf "I do not want to damage the nice girl image I've been cultivating for so long with this kind of details."
            sis "You're doing it that much? You naughty girl."
            sf "You'll never know for sure."
            sis "There's nothing to be ashamed of here."
            sis "I do it maybe 3 times a week? Sometimes more."
        "Drink.":
            mc "I'll keep that my shameful secret, if you don't mind."
            sf "I'll drink too."
            if ep1beer == True:
                scene ep2_sc9_l_2_b_sf_sis
            elif ep1vodka == True:
                scene ep2_sc9_l_2_v_sf_sis
            else:
                scene ep2_sc9_l_2_w_sf_sis
            sis "Oh, come on! There's nothing to be ashamed of here!"
            sis "I do it maybe 3 times a week? Sometimes more. It's healthy!"
            sf "You naughty girl."

    off "I'm about to ask my last question when [sf_name] stops the game."
    if ep1beer == True:
        scene ep2_sc9_l_3
    elif ep1vodka == True:
        scene ep2_sc9_l_3
    else:
        scene ep2_sc9_l_3
    sf "I think I've had enough for tonight, I'm almost drunk."
    sf "I should go to bed."
    sis "I'm almost gone too."
    mc "I guess it's time to call it a night then."
    off "[sis_name] takes [sf_name] by the arm to help her walk."
    if ep1beer == True:
        scene ep2_sc9_l_3_d
    elif ep1vodka == True:
        scene ep2_sc9_l_3_d
    else:
        scene ep2_sc9_l_3_d
    sis "I'll bed you, young lady."
    sf "I hope you won't abuse my body again, you despicable being."
    sis "I can't promise you anything."
    sf "Goodnight [mc_name]."
    mc "Goodnight [sf_name]."
    sis "Goodnight pervert."
    mc "Goodnight Princess."

    scene black with dissolve
    off "The girls leave the place together."
    off "I can hear them laughing on the stairs."
    off "The bottles are empty."
    if ep2drinkgamecounter > 3:
        off "I'm drunk."


label ep2sc10:
    scene black with dissolve
    with Pause(2)
    show text "Later that night."
    with Pause(2)
    hide text
    off "The need to pee wakes me up in the middle of the night."
    show ep2_sc10_cn_0 with dissolve
    off "I'm going through the hallway like a zombie."
    off "I'm still a bit drunk."
    off "A bear seems to snore in [sis_name]'s bedroom."
    off "I wonder which of the girls is capable of producing that kind of noise."
    off "[sis_name], probably. I can hardly imagine [sf_name] snoring at all."
    hide ep2_sc10_cn_0
    show ep2_sc10_cn_1
    if ep2goodsexposed == True:
        off "I take care of my business in the bathroom and I'm about to go back to bed when I hear some strange moans coming from downstairs."
    else:
        off "I take care of my business in the bathroom and I'm about to go back to bed when I hear voices coming from downstairs."
    off "Curiosity killed the cat."
    hide ep2_sc10_cn_1
    show ep2_sc10_ln_0
    off "I follow the voices back to the living room."

    if ep2goodsexposed == True:
        hide ep2_sc10_ln_0
        show ep2_sc10_ln_1
        off "Holy shit."
        off "It looks like a good choice of movie to relax that way."
        off "That's quite the show."
        off "The porn is playing silently on screen but she's moaning pretty loudly."
        off "She's wearing her headphones, she didn't hear me and she probably doesn't hear herself neither."
        off "What do I do?"
        menu:
            "I should leave her alone before she notices me. [sisLovePath]":
                $ ep2sismasturbate = True
                off "She deserves her privacy."
                off "Nice show tho."
                off "I let her enjoy herself and go back to bed."
                off "I can only hope for some sweet dreams with what I just saw."
                jump ep2end
            "Go to her. [sisSubPath]" if sis_submission > 10:
                jump ep2sc10subroad
    elif ep2apologizedtosis == True:
        hide ep2_sc10_ln_0
        show ep2_sc10_ln_28
        $ ep2sismovienight = True
        off "[sis_name] is watching an old black and white movie."
        off "She didn't hear me."
        off "What should I do?"
        menu:
            "I should leave her alone.":
                off "She probably doesn't want me to distract her from her movie."
                off "I'll go back to bed."
                jump ep2end
            "I should join her. [sisLovePath]":
                off "I didn't share that kind of moment with her since we were children."
                off "It could be nice."
                jump ep2sc10loveroad
    else:
        hide ep2_sc10_ln_0
        show ep2_sc10_ln_19
        $ ep2sissleepingmovie = True
        off "[sis_name] seems to be sleeping on the sofa."
        off "And old black and white movie is playing on the screen."
        off "What should I do?"
        menu:
            "I should leave her alone.":
                off "She's sleeping."
                off "What the heck do I have to do about that?"
                off "Let's go back to bed."
                jump ep2end
            "I should get closer. [assholePath]" if sis_affection < 5 or ep2cameraset == True:
                off "Just to be sure."
                jump ep2sc10creeproad

label ep2sc10subroad:
    off "This is crazy but this may be an occasion to hone our relationship."
    hide ep2_sc10_ln_1
    show ep2_sc10_ln_2
    off "I approach her without being noticed."
    off "My dick is hard."
    off "I can see her fingers plunging in her pussy."
    hide ep2_sc10_ln_2
    show ep2_sc10_ln_3
    $ UnlockThat("ep2/ep2_sc10_ln_3")
    off "She finally sees me."
    off "Her expression is priceless."
    hide ep2_sc10_ln_3
    show ep2_sc10_ln_3_b
    $ UnlockThat("ep2/ep2_sc10_ln_3_b")
    off "Between surprise, horror, and pleasure."
    off "She seems to be about to scream but finally only lets out an almost silent groan."
    hide ep2_sc10_ln_3_b
    show ep2_sc10_ln_4
    off "She discards her headphones and covers herself with a cushion."
    off "Her panties are out of her reach on the other side of the sofa."
    sis "What are you doing here?"
    mc "Well, I couldn't sleep, just like you probably."
    mc "I heard a noise coming from the living room."
    mc "I was intrigued and came to check."
    mc "I saw you enjoying yourself and it got me horny, so I thought.. why not join her?"
    hide ep2_sc10_ln_4
    show ep2_sc10_ln_5

    sis "Join me? Are you crazy? You're like a brother to me."

    mc "So what?"
    mc "I'm just going to sit on this sofa and masturbate just like you do."
    sis "And you don't think it's wrong?"
    sis "One doesn't usually masturbate with their siblings."
    mc "Why?"
    mc "You know I masturbate and I know you masturbate."
    mc "You saw my dick, I saw your pussy."
    mc "We have nothing to hide anymore."
    mc "Besides, you said it yourself, there's nothing to be ashamed of."
    sis "I don't think that... Wait ..."
    hide ep2_sc10_ln_5
    show ep2_sc10_ln_6
    sis "Is your dick trying to pop out of your underpants by itself."
    mc "I told you I was horny."
    mc "I need to jerk off before I explode."
    sis "What?"
    mc "If you don't mind..."
    sis "I do mind! I do mind!"
    hide ep2_sc10_ln_6
    show ep2_sc10_ln_7
    off "I take off my underpants and throw them on the other side of the sofa, with [sis_name]'s panties."
    sis "Oh my god."
    mc "Why so surprised? You already saw it."

    if ep2showerfap == False:
        sis "Last time it wasn't so... big..."
    else:
        sis "Last time it wasn't so... close..."

    mc "It wasn't as hard either. Do you want to touch it?"
    sis "No, I don't! Will you stop offering me to touch your dick, please?"
    mc "I don't mind."
    sis "But I do."
    mc "Nevermind then."
    hide ep2_sc10_ln_7
    show ep2_sc10_ln_8
    off "I sit next to her and turn my attention to the screen, while gently stroking my cock with my right hand."
    hide ep2_sc10_ln_8
    show ep2_sc10_ln_9
    off "[sis_name] is nervous at first."
    off "I can sense her biting her lips, hesitant."
    hide ep2_sc10_ln_9
    show ep2_sc10_ln_10
    off "After a couple minutes of doing nothing, then touching herself under the cushion, she finally gets rid of the pillow. She lets herself slide on the sofa, spreads her legs and fingers herself openly."
    off "Her pussy is soaking wet."
    hide ep2_sc10_ln_10
    show ep2_sc10_ln_11
    off "I'm sure I could slip in it in one go without effort."
    off "My dick is rock solid. I've probably never had a boner like that in my life."
    off "Damn, I know it's wrong, but I want to fuck her so bad..."
    off "I can feel her glance over at my cock."
    hide ep2_sc10_ln_11
    show ep2_sc10_ln_12
    $ UnlockThat("ep2/ep2_sc10_ln_12")
    off "She's looking at my dick as much as I look at her pussy."
    off "I want to touch her and I want her to touch me."
    hide ep2_sc10_ln_12
    show ep2_sc10_ln_13
    mc "Do you want to exchange?"
    sis "Exchange?"
    mc "You do me and I do you."
    sis "You're crazy..."
    mc "You want to try it, don't you?"
    mc "You're wondering how it feels like to handle a cock."
    mc "I can sense your eyes lingering on my dick."
    mc "It's your chance to try it with someone you can trust. Take it."
    off "In one move, I reduce the distance separating us and put my left arm behind her."
    off "I grab her right leg and place it upon my left one so she can be more comfortable."
    off "She doesn't even try to resist."
    mc "Take it."
    hide ep2_sc10_ln_13
    show ep2_sc10_ln_14
    $ UnlockThat("ep2/ep2_sc10_ln_14")
    off "She shyly grab my dick and begin stroking it slowly."
    off "Her touch alone is almost enough to make me cum."
    off "I barely manage to hold myself."
    mc "Holy shit, [sis_name], you've almost got me there."
    off "She seems to enjoy it."
    off "Her breath is heavier, her moans louder."
    off "I bring my left arm between her breast and go for her pussy."
    off "She's a bit reluctant at first then lets me insert my fingers inside her."
    hide ep2_sc10_ln_14
    show ep2_sc10_ln_15
    $ UnlockThat("ep2/ep2_sc10_ln_15")
    sis "Oh my god!"
    off "It's time to put into practice everything I've learned off the internet."
    off "I search for her clitoris, I press hit, massage it, I go inside, outside, up, down, slower, faster, harder, harder, harder."
    sis "Don't stop! Yes! Right there! Right there, yes, yes yes!"
    off "She's jerking me off so hard that it's almost painful."
    hide ep2_sc10_ln_15
    show ep2_sc10_ln_16
    $ UnlockThat("ep2/ep2_sc10_ln_16")
    off "[sis_name] is almost yelling while my cum springs furiously out of me."
    off "I'm still caressing her pussy as she strokes my dick when she seems to realize what we just did."
    hide ep2_sc10_ln_16
    show ep2_sc10_ln_17
    off "She bites her lips and looks me in the eyes."
    $ ep2sisfingered = True
    menu:
        "You did great. [sisSubPath]":

            $ ProcessStat(3, "sis_submission")
            $ DumpNotStack()
        "So... did you like it? [sisLovePath]":

            $ ProcessStat(1, "sis_affection")
            $ ProcessStat(1, "sis_submission")
            $ DumpNotStack()
    hide ep2_sc10_ln_17
    show ep2_sc10_ln_18
    off "She seems confused. She quickly gets up and puts on her panties."
    sis "I'm so sorry, we shouldn't have .. I shouldn't .. "
    sis "This never happened, do you hear me? Please."
    off "She doesn't even wait for an answer and leaves the room."
    off "The porn is over."
    off "My dick and my balls are covered with my semen."
    off "I should clean that mess before going to bed."
    $ renpy.end_replay()
    jump ep2end

label ep2sc10loveroad:
    hide ep2_sc10_ln_28
    show ep2_sc10_ln_29
    $ ep2sismovie = True
    mc "Hey [sis_name]."
    sis "Hey."
    mc "Can't sleep?"
    sis "Not with [sf_name] snoring like a bear beside me."
    mc "I heard her from the hallway."
    mc "The amount of noise she produces is impressive."
    sis "Yes, it is."
    mc "Can I join you?"
    sis "It's a free country."
    hide ep2_sc10_ln_29
    show ep2_sc10_ln_30
    off "I sit next to her and focus on the screen."
    hide ep2_sc10_ln_30
    show ep2_sc10_ln_32
    off "It's some kind of Hitchcock movie I've never heard of."
    off "I missed the beginning of the movie and have a hard time understanding what's going on in that old mansion."
    hide ep2_sc10_ln_32
    show ep2_sc10_ln_33
    sis "The hug was nice."
    hide ep2_sc10_ln_33
    show ep2_sc10_ln_34
    off "It came out of nowhere."
    off "I'm a bit stunned and take a couple seconds to react."
    mc "Really? To be honest I was afraid you would reject me and beat me to death."
    hide ep2_sc10_ln_34
    show ep2_sc10_ln_35
    sis "I thought about it."
    mc "I would have deserved it, but I'm glad you choose otherwise."
    mc "I'm sorry [sis_name]. I know the words are not enough."
    mc "I have been blind for so long. I failed you."
    sis "Stop that. I understood the first time you said it."
    sis "How do you expect us to move on if you keep apologizing over and over again?"
    mc "Alright, let's move on then."
    mc "One last thing, about the hug, if you liked it, you can have one anytime you want."
    mc "You don't even need to ask."
    sis "Careful not to go too far, I may still beat you to death."
    mc "I trust your judgment."
    hide ep2_sc10_ln_35
    show ep2_sc10_ln_32
    off "We go back to silence for a couple minutes."
    hide ep2_sc10_ln_32
    show ep2_sc10_ln_33
    sis "You know we're not kids anymore, aren't you?"
    hide ep2_sc10_ln_33
    show ep2_sc10_ln_34
    mc "So what?"
    off "She doesn't answer."

    if sis_affection > 13:
        hide ep2_sc10_ln_34
        show ep2_sc10_ln_36
        $ UnlockThat("ep2/ep2_sc10_ln_36")
        $ ep2sismoviehug = True
        off "A few minutes later, she slowly slides against me and I put my arm around her."
        off "Her warmth makes me strangely happy."
        off "I don't know how long we stay like that."
        if ep2kissedsf == True:
            hide ep2_sc10_ln_36
            show ep2_sc10_ln_37
            $ UnlockThat("ep2/ep2_sc10_ln_37")
            sis "I saw you kissing [sf_name]."
            mc "Does that bother you?"
            sis "I haven't decided yet."
            mc "Tell me when you have."
            sis "I will... So... Are you her boyfriend or something now?"
            mc "I don't know. We just kissed. We haven't talked about it."
            sis "How was it?"
            mc "The kiss? It was terrifying. I believe the next one will be better."
            hide ep2_sc10_ln_37
            show ep2_sc10_ln_39
            $ UnlockThat("ep2/ep2_sc10_ln_39")
            sis "I've never kissed anyone..."
            off "We look at each other's eyes, each other's lips."
            off "I can feel her breath on my nose."
            menu:
                "Kiss her. [sisLovePath]":

                    $ ProcessStat(5, "sis_affection")
                    $ DumpNotStack()
                    $ ep2sismoviekiss = True
                    hide ep2_sc10_ln_39
                    show ep2_sc10_ln_38
                    $ UnlockThat("ep2/ep2_sc10_ln_38")
                    off "Our lips join and we kiss."


                    off "I know it's not something I should do, but I'm not sure I care."

                    off "Her lips are soft and sweet."
                    off "It feels so wrong and so right at the same time that I'm lost."
                    off "I don't know what to think anymore."
                    off "It's like she's rewriting my reality with a kiss."
                    off "I like it."
                    hide ep2_sc10_ln_38
                    show ep2_sc10_ln_40
                    off "Our lips separate and we look at each other in silence."
                    off "I can read my own feelings in her eyes."
                    off "We liked it, we want more, but it's wrong."
                    off "We are afraid."
                    off "She breaks our embrace and gets up from the sofa."
                    hide ep2_sc10_ln_40
                    show ep2_sc10_ln_41
                    sis "I'm sorry, I shouldn't have done that..."
                    sis "I don't know why I did that... I'm sorry."
                    sis "This never happened. Please."
                    off "She leaves without waiting for my answer."
                    scene black with dissolve
                    off "I guess I'll go back to bed now."
                    off "But I'm not sure I can even sleep with what just happened."
                    jump ep2end
                "Reject her.":

                    $ ProcessStat(-5, "sis_affection")
                    $ DumpNotStack()
                    $ ep2sisrejected = True
                    hide ep2_sc10_ln_39
                    show ep2_sc10_ln_40


                    mc "I'm sorry [sis_name]... I don't think I should do that..."

                    sis "Of course, you're right."
                    off "She breaks our embrace and gets up from the sofa."
                    hide ep2_sc10_ln_40
                    show ep2_sc10_ln_41
                    sis "I'm sorry, it was the alcohol."
                    off "She leaves without waiting for my answer."
                    off "Left alone in the living room, I watch the end of the movie before going back to bed."
                    jump ep2end
        else:
            off "The movie comes to an end."
            off "Without a word, [sis_name] breaks our embrace and gets up."
            hide ep2_sc10_ln_36
            show ep2_sc10_ln_41
            sis "That was nice. We should do that again sometime."
            mc "Yes, it was nice. Whenever you want."
            sis "Goodnight."
            mc "Goodnight Princess."
            off "She leaves the room."
            off "I stay there alone for a few minutes thinking of what happened."

            $ ProcessStat(1, "sis_affection")
            $ DumpNotStack()
            jump ep2end
    else:
        hide ep2_sc10_ln_34
        show ep2_sc10_ln_30
        off "We watch the movie in silence, without exchanging a single word."
        off "I sometimes have the feeling that she's about to talk to me but nothing happens."
        off "The movie comes to an end ans she quickly gets up."
        hide ep2_sc10_ln_30
        show ep2_sc10_ln_41
        sis "That was nice. We should do that again sometime."
        mc "Yes, it was nice. Whenever you want."
        sis "Goodnight."
        mc "Goodnight Princess."
        off "She leaves the room."
        off "I stay there alone for a few minutes thinking of what could have happened if she had talked to me."

        $ ProcessStat(1, "sis_affection")
        $ DumpNotStack()
        jump ep2end

label ep2sc10creeproad:
    off "I take a few steps into the living room."
    hide ep2_sc10_ln_19
    show ep2_sc10_ln_20
    off "[sis_name] is asleep."
    off "She was probably as drunk as me, maybe even more."
    off "The little princess doesn't look so tough now does she?"
    menu:
        "Let her sleep.":
            off "I should leave her alone."
            off "I have nothing to do here."
            off "Let's go back to bed."
        "Play with her. [hatePath]" if ep2cameraset == True:
            $ ep2sisabused = True
            off "It's payback time Princess."
            off "I quickly get rid of my underpants and bring out my cock."
            hide ep2_sc10_ln_20
            show ep2_sc10_ln_21
            $ UnlockThat("ep2/ep2_sc10_ln_21")
            off "Careful not to wake her up now."
            off "You're going to kiss it, Princess."
            off "I get my dick to her mouth and slowly rub my glans against her lips."
            off "Holy shit. I'm already trembling with pleasure."
            hide ep2_sc10_ln_21
            show ep2_sc10_ln_22
            off "I gently insert my penis in her mouth."
            off "It's moist and hot."
            hide ep2_sc10_ln_22
            show ep2_sc10_ln_23
            off "The sensation is unreal."
            hide ep2_sc10_ln_23
            show ep2_sc10_ln_24
            $ UnlockThat("ep2/ep2_sc10_ln_24")
            off "She reflexively sucks my dick while I carefully move back and forth."
            hide ep2_sc10_ln_24
            show ep2_sc10_ln_25
            off ""
            hide ep2_sc10_ln_25
            show ep2_sc10_ln_24
            off ""
            hide ep2_sc10_ln_24
            show ep2_sc10_ln_25
            off "I slowly fuck her mouth."
            hide ep2_sc10_ln_25
            show ep2_sc10_ln_24
            off ""
            hide ep2_sc10_ln_24
            show ep2_sc10_ln_25
            off ""
            hide ep2_sc10_ln_25
            show ep2_sc10_ln_24
            off "I can feel her teeth lightly grinding on my shaft."
            hide ep2_sc10_ln_24
            show ep2_sc10_ln_25
            off ""
            hide ep2_sc10_ln_25
            show ep2_sc10_ln_24
            off ""
            hide ep2_sc10_ln_24
            show ep2_sc10_ln_25
            off ""
            hide ep2_sc10_ln_25
            show ep2_sc10_ln_24
            off ""
            hide ep2_sc10_ln_24
            show ep2_sc10_ln_26
            $ UnlockThat("ep2/ep2_sc10_ln_26")
            off "I don't last more than a minute, I cum in her mouth."
            off "She will probably swallow it in her sleep."
            off "I take my underpants and I'm about to leave when she moans and moves."
            hide ep2_sc10_ln_26
            show ep2_sc10_ln_27
            off "Fear propels me out of the room, running as silently as possible."
            off "Holy shit what have I done?"
            off "I'm fucking crazy."
            off "It felt amazing but damn, I'm disgusting."
            off "How could I do that? "
    $ renpy.end_replay()
    jump ep2end
label ep2end:


    jump day3start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
