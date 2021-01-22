

label day3start:
    scene black with dissolve
    with Pause(2)
    show text "Day 3 - Monday" with dissolve
    with Pause(2)
    show text "The morning" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(2)


    off "I wake up late this morning."


    if ep2drinkgamecounter > 3 or ep2sisfingered == True or ep2sisabused == True or ep2sisrejected == True or ep2sismoviekiss == True:
        scene ep3_sc1_mcr_0
    else:
        scene ep3_sc1_mcr_2


    if ep2drinkgamecounter > 3:
        off "My head hurts."
        off "I'm pretty sure it's about to explode."
        off "I shouldn't have drunk that much."
        off "I'm now paying the price."
    else:
        off "I managed to avoid ending drunk despite last night's drinking game."
        off "No hangover for me."
        off "I wonder if the girls are as lucky as me."

    if ep2sisfingered == True or ep2sisabused == True or ep2sisrejected == True or ep2sismoviekiss == True or ep2kissedsf == True or ep2footmassage == True:
        off "Yesterday was crazy."

    if ep2sismoviekiss == True:
        off "I kissed [sis_name]."
        off "And it was not a brotherly kiss."
        off "I know it's wrong, but I liked it."
        off "Her lips were soft and sweet. I remember it clearly."
        off "I think she enjoyed it too."
        off "The alcohol probably helped us. One can do silly things when drunk."
        off "I don't know how we came to that."
        off "Two days ago we were ready to kill each other and now we are kissing like lovers."
        off "That's a pretty fast development."
        off "Sure, I fantasized a bit about her, but I didn't expect that to become a reality."
        off "This is so weird."
        off "When I think of it, I'm as disgusted as I'm excited."
        off "I'm nauseous and I have a boner at the same time."
        off "And I can feel my heart pounding in my chest."
        off "What should I do?"
        off "Can I just act as if nothing happened?"
        off "Should we talk about it?"
        off "We should talk. At least I should apologize or something."
        off "I kissed [sf_name] too."
        off "Does that mean I'm her boyfriend?"
        off "We didn't talk about it."
        off "Shit. Did I already cheat on [sf_name] with [sis_name]?"
        off "I didn't even think of her while kissing [sis_name]."
        off "What kind of douchebag am I?"
        off "This whole situation is a total mess."

    elif ep2sisrejected == True:
        off "That was weird."
        off "[sis_name] clearly wanted me to kiss her, and not in a brotherly way."
        off "I rejected her but honestly, I wanted it too."
        off "I don't know how we came to that."
        off "Sure, I fantasized a bit about her, but I didn't expect that to become a reality."
        off "This is so weird."
        off "What should I do?"
        off "Can I just act as if nothing happened?"
        off "Should we talk about it?"
        off "We should talk. At least I should apologize or something."
        off "She seemed curious, maybe even jealous of my kiss with [sf_name]."
        off "Should I talk to [sf_name] about that?"
        off "That would be even weirder..."
        off "I have yet to talk to her about our own kiss."
        off "I was pretty sure she would reject me but it clearly went better than expected."
        off "I need to know what we are to each other."

    elif ep2sismovie == True and ep2sisrejected == False and ep2sismoviekiss == False:
        off "That improvised movie night was nice."
        off "I'm pretty sure [sis_name] enjoyed the company, still, I have the feeling I missed something."
        off "Like if she wanted something more from me."
        off "The way she has left the room was a bit weird."
        off "Maybe I'm imagining things."

    if ep2sisfingered == True:

        off "I fingered [sis_name] while she gave me a handjob."

        off "My fingers were inside her pussy."
        off "That was incredible."
        off "I don't know where I've found the balls to propose that kind of thing to her, but she accepted it."
        off "And even crazier, I'm sure she liked it."
        off "It was a bit like if she was submitting to me."
        off "That was ... nice."
        off "It felt empowering."
        off "I was the one in control."
        off "I know it's wrong to do that kind of thing with [sis_name] but it felt so good..."
        off "Just like when I fap thinking of her."

        off "It feels even better because she's my childhood friend."

        off "I must be crazy. Or at least a pervert. But it sure was enjoyable."

    elif ep2sismasturbate:
        off "Maybe I should have joined her watching that porn."
        off "It would have been weird but maybe would it have honed our relationship."
        off "Who knows, if she's into that kind of thing..."

    if ep2sisabused == True:
        off "I put my dick in my sleeping friend's mouth."

        off "It's crazy, and wrong, I should probably go to jail for that, but fuck that felt good."
        off "The thrill of the danger..."
        off "That was so exciting that I barely lasted a minute between her lips."
        off "She'll never know what happened."
        off "It should be ok."

    if ep2sisfingered == True or ep2sisabused == True:
        off "And there's more."

    if ep2kissedsf == True and ep2sisrejected == False and ep2sismoviekiss == False:
        off "I kissed [sf_name]."
        off "I was pretty sure she would reject me but it clearly went better than expected."
        off "I'll have to talk to her about that."
        off "I need to know what we are to each other."

    if ep2footmassage == True:
        off "Who would have known that I was so good at massaging feet?"
        off "It was my first time ever touching a girl and I managed to give her an orgasm."
        off "At least it looked like an orgasm."
        off "I've never seen a real one so I can't be sure, but still, it was a pretty good move for a virgin wasn't it?"
        off "What should I do next?"

    if ep2sisfingered == True or ep2sisabused == True or ep2sisrejected == True or ep2sismoviekiss == True or ep2kissedsf == True or ep2footmassage == True:
        off "I'll have to tell Steve about that."
        off "Or maybe not."
        off "Maybe it's better to keep it a secret."

    off "Anyway, I need to pee."

    scene black with dissolve
    with Pause(2)
    scene ep3_sc1_c_4

    off "Half an hour later I have peed and showered."
    off "I'm on my way to my room when I hear the girls entering the house and climbing the stairs."
    off "I'm quickly surrounded."
    if ep2sisfingered == True or ep2sisrejected == True or ep2sismoviekiss == True:
        scene ep3_sc1_c_1
    else:
        scene ep3_sc1_c_2
    off "I remember [sf_name] saying that she exercises every day."
    off "The girls are probably coming back from running or something like that."
    off "I'm baffled by their endurance. Even with a hangover, even in the middle of a heatwave, they're going out exercising."
    off "I suddenly feel shamefully lazy."

    if ep2sisfingered == True or ep2sisrejected == True or ep2sismoviekiss == True:
        $ ep3sisashamed = True
        off "[sis_name] refuses to make eye contact."
        off "She's probably still confused and ashamed of what happened last night."

    sf "Hello [mc_name]."
    mc "Hello [sf_name]."
    sis "Hey."
    mc "Hey Princess."
    sf "How are you?"
    mc "Fine, thank you. How about you?"
    sf "I've seen better mornings."
    sf "I drank too much last night, but I'll be alright."
    mc "I'm glad to hear it."
    sis "We're taking the bathroom."
    sis "It's your turn to make breakfast."
    mc "I never cooked anything in my life!"
    scene ep3_sc1_c_3
    sis "Well, here is your chance to shine."
    mc "Great."
    sis "We'll be in the kitchen in thirty minutes."
    sf "We're hungry!"
    mc "Wonderful."
    sis "If it's not edible, I'll kill you!"
    mc "Of course, you will..."

    off "They disappear into the bathroom."
    off "Thirty minutes to prepare breakfast. That shouldn't be that hard."

    if ep2cameraset == True:
        off "I should hurry."
        off "I'll watch them on my phone while cooking."
        off "Finally, I'll see what they're doing together in this bathroom."

    if ep2cameraset == True:
        $ ep3breakfastfailed = True
        scene ep3_sc1_k_0_cam
        off "I put on some clothes and get to the kitchen while trying to connect my phone to the camera."
        off "Connecting... Loading... Connecting... Downloading update..."
        off "Shit."
        scene ep3_sc1_k_1_cam
        off "I throw some bacon and eggs in a pan."
        off "Installing... Connecting... Loading..."
        off "Come on! I'm going to miss the show!"
        off "Loading... "
        off "Fuck you, technology, you're supposed to work fast and easy."
        off "Finally!"
        scene ep3_sc1_k_2_cam
        $ UnlockThat("ep3/ep3_sc1_br_0")
        off "My smartphone connected, my screen shows me the shower."
        off "Holy shit."
        off "Well... I clearly fucked up the camera angle."
        off "And the steam and the water jets prevent me from seeing the most interesting parts."
        off "It's mostly a failure."
        off "I'm a bit disappointed."
        off "I expected some hot lesbian action but they're just showering."
        off "No kissing, no touching each other."
        off "I hoped for more action."
        off "I'm still getting a boner anyway."
        off "What is that smell? Is something burning?"
        scene ep3_sc1_k_3
        off "Fuck, the bacon!"
        off "And the eggs!"
        off "What the hell happened?"
        off "It was totally fine 5 minutes earlier."
        off "And now it's totally burnt!"
        off "Shit, I fucked up again."
        off "The girls are already getting out of the bathroom."
        off "It'll have to do."
        off "Let's put that on plates."
        off "... Shit... I forgot the toast."
        scene ep3_sc1_k_4_cam
        off "Five minutes later I've set up the table with what I managed to salvage."
    else:
        scene ep3_sc1_k_0
        off "I put on some clothes and get to the kitchen."
        off "Bacon, eggs, toast, coffee."
        off "It can't be that difficult."
        scene ep3_sc1_k_1
        off "Just don't let it burn [mc_name]."
        off "Coffee, check."
        scene ep3_sc1_k_2
        off "Bacon and eggs, check."
        off "Toast, check."
        off "That's actually quite easy."
        off "It smells good at least."
        scene ep3_sc1_k_4
        off "I put everything on plates, the breakfast is ready as the girls take place around the table."

    if ep3sisashamed == True:
        if ep3breakfastfailed == True:
            scene ep3_sc1_k_6_f
        else:
            scene ep3_sc1_k_6
        off "[sis_name] is still trying to avoid eye contact in a pretty childish manner."
        off "[sf_name] seems to have noticed that something was off."
        if ep3breakfastfailed == True:
            scene ep3_sc1_k_8_f
        else:
            scene ep3_sc1_k_8
        sf "Did you two have a fight or something?"
        if ep3breakfastfailed == True:
            scene ep3_sc1_k_7_f
        else:
            scene ep3_sc1_k_7
        mc "No, we didn't."
        mc "I think we're actually getting along very well at the moment."
        if ep3breakfastfailed == True:
            scene ep3_sc1_k_9_f
        else:
            scene ep3_sc1_k_9
        mc "As incredible as it seems."
        mc "Why would you think that?"
        sf "I don't know."
        sf "It's just an impression."
        if ep3breakfastfailed == True:
            scene ep3_sc1_k_7_f
        else:
            scene ep3_sc1_k_7
        sis "We didn't have a fight."
        sis "I just have a minor headache."
        sis "I guess I drank too much last night."
        mc "We all went a bit overboard."
        sis "I guess so."
        if ep3breakfastfailed == True:
            scene ep3_sc1_k_5_f
        else:
            scene ep3_sc1_k_5
        off "She quickly corrects her attitude to be more like her usual self."

    if ep3breakfastfailed == True:
        scene ep3_sc1_k_10_f
        off "She looks at her plate and frowns."
        sis "Did you even try?"
        sis "Dude, I know you're not good in the kitchen but still, it's just breakfast."
        sis "Can't you even cook some eggs and bacon?"
        sis "And the coffee is cold."
        sis "Wait."
        sis "Is that yesterday's pot?"
        sis "And I think you forgot the toast."
        sis "There's no more orange juice?"
        menu:
            "Hey. I did my best ok? [hatePath]":
                scene ep3_sc1_k_11_f
                $ ProcessStat(-1, "sis_affection")
                $ ProcessStat(-1, "sis_submission")
                $ ProcessStat(-1, "sf_affection")
                $ DumpNotStack()
                mc "I've told you I never cooked anything. How did you want me to make a decent breakfast?"
                sis "Come on. It's breakfast. You don't need any skills for that."
                sf "It's no big deal. It's still edible."
            "Maybe can you do better? [gr]\[Challenged\]":
                scene ep3_sc1_k_11_f_2
                $ ep3sischallenged = True
                sis "I failed miserably at cooking dinner last night, but I'm sure I can make a decent breakfast."
                mc "Tomorrow?"
                sis "Tomorrow."
                sf "Is that a competition?"
                sis "It is now. And you will be the judge."
                sf "I'm not sure I want to be a part of this."
            "Sorry. I'm really bad at this. [sisLovePath] [sfLovePath]":
                scene ep3_sc1_k_11_f_3
                $ ProcessStat(1, "sis_affection")
                $ ProcessStat(1, "sf_affection")
                $ DumpNotStack()
                sis "Well, it's still edible."
                sis "And it's not worse than my last attempt at dinner."
                sf "Let us say you can both progress in that matter."

        scene ep3_sc1_k_12_f
        sf "Anyway, I'm starving."
        sf "Let's try to eat that thing."
    else:

        scene ep3_sc1_k_10
        sis "Well... I'm honestly quite surprised."
        sis "That sure looks pretty nice for a first try."
        scene ep3_sc1_k_11
        mc "Thank you."
        mc "I'm as surprised as you."
        mc "I don't know if it was really easy or if I aced it by pure luck."
        scene ep3_sc1_k_12
        sf "It's really easy."
        sf "But some still manage to flunk it."
        sf "My dad wouldn't be able to cook an egg even if his life depended on it."
        mc "So... you're the one making breakfast every morning at home?"
        sf "Yes, I am. But most of the time I'm only cooking for myself."
        sf "My dad isn't a breakfast person."
        off "[sf_name] never talks about her mother."
        off "She died while [sf_name] was still an infant."
        off "She barely has any memories of her."
        off "She probably learned to cook alone."
        sf "Anyway, I'm starving."
        sf "Let's eat before it gets cold."

    scene black with dissolve
    with Pause(2)

    off "Twenty minutes later, breakfast is over."
    off "We get up from the table and quickly take care of the dishes."
    scene ep3_sc1_k_13
    mc "Oh! I think we forgot to talk about something."
    sis "What are you talking about?"
    mc "Mom called yesterday."
    scene ep3_sc1_k_14
    mc "She knows you're here, [sf_name]."
    mc "She said you are welcome to use their bedroom."
    mc "It will be more comfortable than sharing [sis_name]'s bed."
    sf "Really? It's very kind of her... but I'm a bit embarrassed to use your parent's bedroom."
    sf "It feels a bit like I'm invading their space and their lives..."
    sf "And honestly, I'm fine with sharing [sis_name]'s bed."
    sis "I was fine with this idea too, until you start snoring like a bear."
    scene ep3_sc1_k_15
    sf "I beg your pardon? I do not snore."
    sis "Oh yes, you do. "
    sf "I don't snore. I would know."
    mc "I could hear you through the door last night."
    sf "You're not being serious."
    sis "We are!"
    sf "Oh my God. I'm so sorry."
    mc "Don't be, it's no big deal."
    sf "It's so unladylike..."
    mc "Don't stress over it. It's not like you can do something about it."
    sf "I'm ashamed."
    sis "You can feel as embarrassed as you want, I'm showing you the room."

    scene black with dissolve
    with Pause(2)

    if ep3breakfastfailed == True:
        off "The girls leave the room and I go back thinking of these images of them showering together."
        off "It definitely deserves a fap."
    else:
        off "The girls leave the room."
        off "I can clearly hear [sis_name] snoring loudly in the stairs."


label ep3sc2:
    scene black with dissolve
    with Pause(2)
    show text "Half an hour later."
    with Pause(2)
    if ep3breakfastfailed == True:
        scene ep3_sc2_mcr_0
        off "I'm having a good time by myself."
        mc "Oh, that pussy, I want that pussy, it smells so good."
        mc "I'm sure it's tight and moist."
        scene ep3_sc2_mcr_1
        mc "I'll fuck you till you get addicted to my dick, bitches."
        mc "I'll make you my sluts."
        mc "Oh shit, it's coming good!"
        scene ep3_sc2_mcr_2
        $ UnlockThat("ep3/ep3_sc2_mcr_2")
        sis "[mc_name]? We have something to..."
        off "They barge in without knocking."
        off "I'm wondering why I didn't lock this door."
        off "The moment lasts only a second."
        off "Probably the longest second in the world."
        off "We look at each other in surprise and silence."
        off "I can feel the adrenaline rushing to my spine."
        off "My dick goes almost flat in an instant."
        sis "...Holy shit!"
        sf "Oh my God."
        scene ep3_sc2_mcr_3
        off "In one motion, I close my laptop et hide myself, sitting on the other side of the bed."
        mc "What the fuck? Can't you knock?"
        scene ep3_sc2_mcr_4
        sis "I'm sorry! We should have announced ourselves."
        mc "Get out!"
        sf "We're leaving you alone, we're sorry, [mc_name]!"
        sis "We'll speak when you're finished, you'll find us in my room..."
        off "The tone of her voice suddenly changes."
        scene ep3_sc2_mcr_5
        sis "Wait."
        off "I fucked up. I'm dead."
        sis "Are those my panties?"
        scene ep3_sc2_mcr_6
        $ ProcessStat(-5, "sis_affection")
        $ ProcessStat(-5, "sis_submission")
        $ ProcessStat(-5, "sf_affection")
        $ DumpNotStack()
        $ ep3caughtfapping = True
        mc "It's not ... what you think..."
        sis "Really?"
        mc "I found those..."
        sis "In my room maybe?"
        mc "No, I would never set foot in your room."
        mc "I found those in the bathroom!"

        sis "And you thought it was fair game to take those and cover them in semen because you have no problem jerking off with my panties."

        mc "I didn't know they were yours!"
        sis "Who else?"
        mc "Well..."
        sf "Are you having... that kind of thought about [sis_name]?"
        mc "No! No, I'm not! I'm sorry, it's a misunderstanding!"
        scene ep3_sc2_mcr_7
        sis "Alright, listen to me carefully, you goddamn pervert."
        sis "You can keep those panties."
        sis "Now that you soiled them, I don't want to touch them anymore."
        sis "You can do whatever you want with those, I don't care."
        sis "But it's the last time you mess with my stuff."

        sis "Get on my nerves and I'll tell your mom about this."

        sis "She will be delighted to learn that you love me so much that you're using my underwear to please yourself."
        sis "You are a creep."
        sis "Let's go, [sf_name]."
        off "They leave my room and close the door behind them."
        off "I'm pretty sure my relationship with those two has worsened by a good bit."
        off "What a moron."
        off "Why didn't I lock this door?"
        off "At least they didn't see the bathroom footage..."
        scene black with dissolve
        with Pause(2)
        jump ep3sc7
    else:
        scene ep3_sc2_mcr_8
        off "I'm losing my time, doing research on the web."
        if ep2sismoviekiss == True or ep2sisrejected == True:

            off "\"The psychological implications of sexing your friends.\", \"How to seduce your friend.\", \"My friend loves my cock.\"."

            off "I've been searching for advice for 20 minutes now and I only found heavy psychological articles I don't understand a word of, made up erotic \"true\" stories or hardcore porn sites."
            off "Fuck you, internet. You're not helping me at all."
            off " I'm totally lost."
            if ep2kissedsf == True:
                off "Between [sf_name] and [sis_name], what should I do?"
                off "Being obsessed with [sf_name]'s lips is pretty normal, but why can't I stop thinking about [sis_name] like this?"

            if ep2sismoviekiss == True:
                off "I want to kiss her again."
                off "Maybe more...."
                off "It's so fucked up."
                off "I can't stop thinking about it."
                off "I know it's wrong but I can't fucking stop thinking about it."
            if ep2sisrejected == True:
                off "I should have kissed her."
                off "I can't stop thinking about it."
                off "I know it's wrong but I can't fucking stop thinking about it."

                menu:
                    "I should try it at least. [sisLovePath]":
                        $ ep3sisloveok = True
                        off "It's crazy but... I want it."
                        off "Maybe I will see things differently if I kiss her."
                    "I should forget about it.":
                        off "It's [sis_name], damn it."
                        off "Childhood friends don't do that kind of thing."

        elif ep2sisfingered == True:
            off "I've been searching for advice on how to get her to trust me and accept my authority for 20 minutes now and I haven't found anything of value."
            off "Be manly, be gentle but firm, be confident..."
            off "All of that seems so obvious."
            off "I'm on my own here."
        else:
            off "I've been searching for advice on how to seduce a girl for 20 minutes now and I haven't found anything of value."
            off "Be kind, be gentle, be manly, don't be a cunt, please tell me something I don't know, or at least something not so obvious."
            off "I'm on my own here."
            if ep2kissedsf == True:
                off "I can't stop thinking about that kiss I shared with [sf_name]."
                off "I'm going crazy."
                off "I have to do something"

        off "It was a waste of time."
        off "The only information I found that wasn't totally worthless is that most of the girls love kittens."
        off "How the hell am I supposed to use this information?"
        off "I can look at some cute kittens memes while I'm at it."

        off "Knock, Knock"
        mc "Come in!"
        scene ep3_sc2_mcr_9
        sf "Hey, [mc_name]."
        mc "Hey, [sf_name]."
        sf "I hope I'm not disturbing you."
        scene ep3_sc2_mcr_10
        mc "You never disturb me, [sf_name]."

        menu:
            "I was browsing the web for some kittens. [sfLovePath]":
                $ ProcessStat(1, "sf_affection")
                $ DumpNotStack()
                mc "Do you want to see some?"
                sf "Kittens? Are you serious?"
                mc "You don't like kittens?"
                sf "Everyone likes kittens."
                sf "They're cute."
                sf "It's just that you, looking for kittens on the web seems so random..."
                sf "I'm a bit surprised."
                mc "Come sit next to me and take a look."
                scene ep3_sc2_mcr_15
                off "She sits on the arm of the sofa and leans over my shoulders."
                off "I can almost feel her breasts right next to me."
                off "I manage to repress my urge to look at them and concentrate on my screen."
                sf "Oh my God. This one is so cute. And this one!"
                mc "Do you like animals, [sf_name]?"
                sf "I do. But I don't have any."
                sf "We live in an apartment downtown."
                sf "It's not a place for either a cat or a dog."
                sf "Look at these tiny paws!"
                sf "Isn't it adorable!"
                mc "Yes, it is."
                mc "So... What can I help you with?"
                sf "Oh, right, I almost forgot."
                scene ep3_sc2_mcr_10
                off "She gets up and stands in front of me."
                sf "[sis_name] and I talked about going shopping this afternoon."
                jump ep3sc2_discussionpoint
            "What can I do for you?":

                sf "Well, [sis_name] and I talked about going shopping this afternoon."
                label ep3sc2_discussionpoint:
                sf "We thought that you may want to join us."
                mc "Me? Shopping? I'm not sure I'll fit nicely in your plans."
                sf "You will."
                sf "Besides, you don't want to leave us girls alone in the big city."
                sf "Who knows what could happen."
                sf "And we need someone to drive the car and carry our bags."

                menu:
                    "Well, I'm not sure about carrying your bags but.. that could be fun. [sfLovePath]":
                        scene ep3_sc2_mcr_16
                        $ ProcessStat(1, "sf_affection")
                        $ DumpNotStack()
                        mc "Count me in."
                        sf "Great! Convincing you was easier than I anticipated."
                        mc "I needed to be convinced?"
                        sf "[sis_name] was thinking that you wouldn't be interested."
                        mc "Well, you presented things so nicely... I didn't really have the choice, did I?"
                        scene ep3_sc2_mcr_14
                        off "She laughs lightly."
                        sf "See you later then."
                        if ep2kissedsf == True:

                            mc "Wait, [sf_name], please..."
                            mc "Can we talk about what happened yesterday?"
                            sf "A lot happened yesterday."
                            mc "Our kiss."
                            scene ep3_sc2_mcr_13
                            sf "What about it?"
                            mc "Well ... I wonder .. What are we now?"
                            mc "Are we together? Are we a couple?"
                            sf "I'm sorry [mc_name], I'm not sure I want to talk about that right now."
                            sf "I... think I need time."
                            sf "I'm interested, truly, but I'm not sure it's a good idea..."
                            mc "Why? If you are interested..."
                            mc "What prevents us from trying?"
                            sf "I'm sorry [mc_name], I can't talk about it."
                            sf "Please forgive me I just need time."
                            sf "I'm very sorry."
                            off "She leaves the room, closing the door behind her."
                            off "She needs time... ok."
                            if ep2sisrejected == True or ep2sismoviekiss == True:
                                off "But I need answers."
                    "I'm sorry, I have something else to do.":


                        scene ep3_sc2_mcr_17
                        $ ProcessStat(-1, "sf_affection")
                        $ DumpNotStack()
                        sf "Come on [mc_name], It will be fun!"
                        mc "Maybe next time..."
                        scene ep3_sc2_mcr_11
                        sf "Maybe wasn't I clear enough."
                        sf "You want to come, [mc_name]."
                        sf "Really."
                        mc "I want to come?"
                        scene ep3_sc2_mcr_12
                        $ UnlockThat("ep3/ep3_sc2_mcr_12")
                        sf "Trust me."
                        sf "You want it."
                        sf "What are you going to do otherwise?"
                        mc "Well..."
                        sf "Nothing. So it's settled."
                        sf "You're coming."
                        mc "Ok..."
                        sf "We're departing in a couple hours."
                        scene ep3_sc2_mcr_14
                        sf "See you later then."


                    "Shopping is not really my thing, I think I'll stay here... [sfDomPath]" if ep2footmassage == True:
                        $ ProcessStat(1, "sf_dominance")
                        $ DumpNotStack()
                        scene ep3_sc2_mcr_11
                        sf "Oh. I think there is a misunderstanding."
                        sf "You're coming with us, [mc_name]."
                        sf "It's not open to discussion."
                        mc "What?"
                        scene ep3_sc2_mcr_12
                        $ UnlockThat("ep3/ep3_sc2_mcr_12")
                        sf "You heard me, [mc_name]."
                        sf "You will drive the car and carry our bags."
                        sf "You know you want to."
                        off "What a view..."
                        mc "Well.. I..."
                        sf "We're departing in a couple hours."
                        scene ep3_sc2_mcr_16
                        mc "Ok..."
                        scene ep3_sc2_mcr_14
                        sf "Good. See you later then."
                        off "She leaves the room, closing the door behind her."
                        off "What the hell just happened?"
                        off "Did she just order me to drive them and carry their bags?"
                        off "Why the hell did I accept?"

    scene black with dissolve
    with Pause(2)

label ep3sc3:
    scene black with dissolve
    with Pause(2)
    show text "Two hours later"
    with Pause(2)
    off "We're downtown, running from shop to shop."
    off "The girls try a lot of clothes but buy none."
    off "The \"carry our bags\" thing turns to be a joke as there is no bag to carry at all."
    scene ep3_sc3_shop_1
    mc "Ok, I'm not sure this is a place for me."
    sf "What's bothering you?"
    mc "This is a lingerie store."
    sis "So what?"
    mc "Are guys even allowed in here?"
    sf "Of course they are. Why would they not?"
    mc "I don't know..."
    mc "Feminine underwear everywhere, posters of almost naked women on the walls."
    mc "I'm uncomfortable."
    mc "I feel like everyone's looking at me thinking I'm some kind of pervert."
    sis "Come on, you're able to endure that much."
    sis "If it's too much pressure for you, you can go take care of yourself in the restroom, Mr Pervert."
    mc "I think I'll be okay but I'll keep that in mind, just in case."
    sis "You naughty boy."
    sf "Is this your first time in a lingerie store?"
    mc "Obviously, yes, I had no reason to visit one before..."
    mc "It's my first time following girls on their shopping spree."
    sf "It's hardly a spree. We haven't bought anything yet."
    sis "We're just having fun."
    mc "I could see that."
    mc "You seemed to have a lot of fun simply trying clothes."
    mc "I supposed that buying was optional in the shopping thing."
    sf "Shopping is a complex and serious matter."
    sf "I'm not sure a guy can understand what it truly means."
    mc "Oh, you mysterious women."
    mc "Anyway, if you don't mind me, I'll just seat myself on this couch and wait for you here."
    scene ep3_sc3_shop_2
    off "The girls stick together for a while, talking about colors and fabrics, before each going her own way through the shop."
    off "The sofa isn't as comfortable as I hoped."



    if (ep2sismoviekiss == True or ep3sisloveok == True ) and ep2kissedsf == True:
        off "[sis_name] and [sf_name] are now each in a different corner of the store."
        off "Maybe now is the time to have a discussion with one or another."
        scene ep3_sc3_shop_x
        off "Who will I try to talk to?"
        menu:
            "[sf_name] [sfLovePath]":
                call ep3sc3_breakpoint_1 from _call_ep3sc3_breakpoint_1
            "[sis_name] [sisLovePath]":
                call ep3sc3_breakpoint_2 from _call_ep3sc3_breakpoint_2
    elif ep2kissedsf == True:
        off "[sis_name] and [sf_name] are now each in a different corner of the store."
        off "Maybe now is the time to have a discussion with [sf_name]."
        menu:
            "Go talk to her [sfLovePath]":
                call ep3sc3_breakpoint_1 from _call_ep3sc3_breakpoint_1_1
            "Don't":
                off "She told me she needed time."
                off "I should not bother her."
    else:
        off "I briefly think about my options and finally get my phone out of my pocket and start playing some shitty games."
        off "Time flies when you play."
        off "Or at least it's supposed to. I'm bored."

    scene ep3_sc3_shop_2
    off "10 minutes later, the sofa is still as uncomfortable as ever."
    off "During the last two minutes [sis_name] and [sf_name] each entered a fitting room."
    off "They're still inside."




    if ep2sisfingered == True and ep2footmassage == True:
        "Maybe this is the right time to have a discussion with my dear childhood friend."
        off "[sis_name] has entered the left room."
        off "[sf_name] is in the right one."
        scene ep3_sc3_shop_42
        off "I'm approaching the fitting room when a text notification makes my phone vibrate."
        scene ep3_sc3_shop_53
        off "I don't even know this number."
        uk "I want to talk to you. Can you come?"
        off "Who the fuck is that?"
        mc "Who? Where? When?"
        sf "It's [sf_name]. In the fitting room. Now."
        off "I don't remember giving her my phone number."
        off "What should I do?"
        menu:
            "I'm on my way. [sfDomPath]":

                off "I'll talk to [sis_name] later."
                sf "I'm waiting."
                $ ProcessStat(1, "sf_dominance")
                $ DumpNotStack()
                call ep3sc3_breakpoint_4 from _call_ep3sc3_breakpoint_4
            "I'm sorry I have something else ongoing.":
                mc "I'll come as soon as I'm finished."
                sf "You shouldn't make a lady wait."
                menu:
                    "You're no lady.":
                        sf "And you're obviously no gentleman. Don't come, ever."
                        mc "That's sounded a bit harsh. Did I offend her?"
                        $ 0
                        $ ProcessStat(-5, "sf_affection")
                        $ DumpNotStack()
                        $ ep3sfdomrejected = True
                    "I can only hope for your forgiveness. [sfLovePath] [sfDomPath]":
                        sf "We'll discuss it later."
                        mc "I'm looking forward to it."

                call ep3sc3_breakpoint_3 from _call_ep3sc3_breakpoint_3


    elif ep2sisfingered == True:

        off "Maybe this is the right time to have a discussion with my dear childhood friend."
        off "[sis_name] has entered the left room."
        scene ep3_sc3_shop_42
        call ep3sc3_breakpoint_3 from _call_ep3sc3_breakpoint_3_1

    elif ep2footmassage == True:
        scene ep3_sc3_shop_54
        off "I'm patiently waiting on the sofa when a text notification makes my phone vibrate."
        off "I don't even know this number."
        uk "I want to talk to you. Can you come?"
        off "Who the fuck is that?"
        mc "Who? Where? When?"
        sf "It's [sf_name]. In the fitting room. Now."
        off "I don't remember giving her my phone number."
        off "This could be interesting."
        mc "I'm on my way."
        off "I'll talk to [sis_name] later."
        sf "I'm waiting."
        $ ProcessStat(1, "sf_dominance")
        $ DumpNotStack()
        call ep3sc3_breakpoint_4 from _call_ep3sc3_breakpoint_4_1

    scene black with dissolve
    off "I patiently wait for another 20 minutes before they finally get out of their fitting room."
    off "They also make me wait outside while they go to the checkout."
    off "I obviously do not have the right to know what has been bought."
    jump ep3sc4

label ep3sc3_breakpoint_1:
    scene ep3_sc3_shop_3
    off "Ok, what do I say?"
    off "First I need to know what's bothering her."
    off "I can't do anything if I don't know what's bugging her."
    off "Then maybe we can talk it out."
    off "Ok, you got this, [mc_name]."
    off "Be confident, don't be a moron."
    scene ep3_sc3_shop_4
    mc "Found anything you like, [sf_name]?"
    sf "A lot, actually."
    sf "The challenge is not to find something but to choose the right one."
    mc "I guess so..."
    mc "Listen, I don't want to pressure you, [sf_name]."
    scene ep3_sc3_shop_5
    mc "But.. I really need to talk about our kiss, and what we are to each other."
    sf "[mc_name],..."
    mc "I know you told me you needed some time to think about it and I'm okay with that."
    mc "But the way you said it, I understood that you wanted to go further with me but something was hindering you from doing so."
    mc "Am I mistaken?"
    sf "Well..."
    scene ep3_sc3_shop_6
    off "She looks around her."
    off "I can only suppose she checks that [sis_name] is far enough not to hear us."
    scene ep3_sc3_shop_7
    sf "Listen,... I... don't know why, but I think I... like you."
    sf "I can't deny it."
    sf "I flirted with you and I'm probably still doing it unconsciously."
    sf "But I'm not sure I want to go further."
    mc "May I ask why? Did I do something?"
    scene ep3_sc3_shop_8
    sf "No, you didn't do anything. Or maybe you did. I don't know how to say it..."
    mc "I'm ready to hear anything."
    mc "It's not my first time being rejected."
    sf "Oh, I'm not rejecting you, [mc_name]."
    $ ep3sfshoptalk = True

    if sis_affection > 13:
        $ ep3sfsislovechat = True
        scene ep3_sc3_shop_9
        sf "The situation is complicated. It's about [sis_name]..."
        sf "I talked to her, about you, and our kiss."
        sf "I wanted her approval."
        sf "And she told me to do as I wish, that she was happy for me."
        sf "But her tone wasn't that of a happy one."
        sf "It felt like I was hurting her by thinking of being with you."
        mc "You mean that she doesn't want us to be together?"

        if ep2sisrejected == True or ep2sismoviekiss == True:
            off "My heart is pounding in my chest."
            off "Is this related to what happened last night with [sis_name]."

        scene ep3_sc3_shop_10
        sf "It's a bit more complex than that."
        sf "I thought a lot about this, although, in the end, I'm just making deductions based on my observations..."
        mc "I still want to hear it."
        sf "I think [sis_name] is jealous."
        mc "Like in she wants to keep you for herself?"
        scene ep3_sc3_shop_11
        sf "[sis_name] and I are very close, but we don't have that kind of relationship."
        sf "No. She wants to keep you for herself."
        mc "You think that [sis_name] has romantic feelings for me?"
        sf "Somehow, yes."
        mc "How is that possible?"
        mc "Two days ago we were still ready to kill each other."
        sf "Well, we can agree you've been a total asshole to her for three years, can we?"

        menu:
            "I've been, yes, undeniably. [sfLovePath]":
                $ ProcessStat(1, "sf_affection")
                $ DumpNotStack()
            "It wasn't totally my fault you know...":
                $ ProcessStat(-1, "sf_affection")
                $ DumpNotStack()
                sf "It doesn't matter who's fault it was."
                sf "You were an asshole."

        scene ep3_sc3_shop_9
        sf "During that whole time, [sis_name] kept telling me that you were a moron and all that kind of thing."
        sf "But from time to time, I could see her, gazing over you from a distance."
        sf "And there was no hate in her eyes."
        sf "More like pain and sadness."
        sf "I'm pretty sure she never actually hated you."
        sf "She just acted that way so she could somehow hide her pain."
        scene ep3_sc3_shop_10
        sf "Do you remember how it was between you before high school?"
        mc "I do remember, yes."
        sf "She told me that at that time, you were more than just a good friend."
        sf "You were kind and protective, you were calling her princess and treated her as such."
        sf "She didn't have to be strong, because you were there for her."

        menu:
            "Please stop. [sfLovePath]":
                $ ProcessStat(2, "sf_affection")
                $ DumpNotStack()
                mc "Do you want to make me cry or something?"
                mc "I remember everything, and it makes me feel even more guilty."
                sf "Crying isn't necessarily a bad thing."
                mc "In a lingerie shop, I'm pretty sure it is."
            "It was a while ago.":
                $ ProcessStat(-1, "sf_affection")
                $ DumpNotStack()
                sf "Yes. I guess things and people change over time..."

        sf "Anyway. You two were really close."
        sf "You were the one she could trust."
        sf "And suddenly you weren't supporting her anymore."

        sf "During those three years, she has been missing her friend."

        sf "But while you were being an asshole to her, she couldn't get to really hate you."

        sf "She kept remembering the loving friend who took care of her before."

        scene ep3_sc3_shop_11
        sf "That would explain two things: why your behavior hurt her so much, and why she accepted your apologies so easily."
        mc "Ok... so.."
        sf "I'm not finished."
        mc "Sorry, I'm listening."
        sf "I think that right now, [sis_name] is very confused about your relationship."
        sf "For three years you pretty much grown apart, separated by a wall of animosity."
        sf "She's somehow rediscovering you right now."

        sf "You're not the friend she loved when you were younger, but you're not the asshole that betrayed her in high school anymore either."

        scene ep3_sc3_shop_10
        sf "You are something new."
        sf "And I think she doesn't exactly know how she feels about you nor how to behave with you."


        mc "You're telling me that [sis_name] currently hesitates between loving me as a friend or as a man."
        sf "I think she doesn't make a difference between loving you as a friend or as a man."

        mc "And if you and I were to grow closer, it would hurt her."
        mc "Like a rejected lover."


        sf "Worse. It would probably hurt her as a lover, as a friend."

        mc "That would basically leave her with nothing."
        sf "You understand."
        mc "I don't know what to say."
        mc "Is there even anything we can do about it?"
        sf "Stay away from one another, I guess."

        menu:
            "I don't want to hurt her anymore. [sfLovePath]":
                $ ProcessStat(2, "sf_affection")
                $ DumpNotStack()
                mc "But I don't want to lose you either."
                mc "There must be something else we can do."
                mc "Can't we talk it out with her?"
                scene ep3_sc3_shop_9
                sf "I don't know, [mc_name]."
                sf "To be honest with you, I'm so afraid of hurting her that I'm afraid of doing anything."
                sf "That's why I told you I needed time."
                sf "I need to think this through."
                sf "It may seem very selfish but... I'm not rejecting you for now."
                mc "Well, honestly, it's much easier to wait for you, now that I know what bothers you."
                sf "I'm sorry, I should have told you sooner."
                scene ep3_sc3_shop_10
                mc "It's okay."
                mc "Don't worry about me."
                mc "I'll return to my seat."
                mc "I have a lot to think through."
                off "I return to the sofa."
                scene ep3_sc3_shop_2
                off "I'm totally lost."
                off "[sf_name] is interested in me, but won't do anything because [sis_name] also as romantic feelings towards me."
                off "Talk about a weird situation."
                off "I'm a virgin who just got his first kiss yesterday."
                off "I am not equipped to deal with that kind of thing, at least not in an adult manner."
                off "What should I do?"
            "Ok. So what?":

                scene ep3_sc3_shop_12
                off "She looks surprised."
                sf "So what?"
                mc "Yes. So what? It's about us, not about her."
                sf "Are you serious?"
                sf "Don't you have any emotion? No feeling?"
                scene ep3_sc3_shop_13
                sf "I'll tell you what."
                sf "Maybe I was wrong about you."
                sf "You are an insensitive and stupid idiot."
                sf "Kissing you was a mistake."
                sf "Forget everything I said."
                mc "What the heck? What did I say? What did I do?"
                off "She quickly gets away from me."
                off "The discussion is clearly over and I have no idea what has caused her anger."
                off "I may have ruined my chance to get into her pants."
                $ ProcessStat(-4, "sf_affection")
                $ DumpNotStack()
                $ ep3sfshopanger = True
    else:
        sf "Not yet, at least."
        mc "That's not a very promising start..."
        scene ep3_sc3_shop_9
        sf "I'm sorry, [mc_name]."
        sf "The truth is I'm very conflicted about you."
        sf "I like you but at the same time, I can't stand the way you treat [sis_name]."
        sf "[sis_name] is my best and only friend."
        sf "If you can't get along with her, we don't stand a chance as a couple."
        sf "You've been nicer to her lately."
        sf "When I told you I needed time it was to see if you were honest about it or if your efforts were a one-time thing only."
        menu:
            "I can understand that. [sfLovePath]":
                $ ProcessStat(1, "sf_affection")
                $ DumpNotStack()
                scene ep3_sc3_shop_10
                mc "I mean... I haven't been the nicest of brothers and you don't want to be in a relationship with an asshole."
                mc "It's understandable."
                mc "But my efforts are real."
                mc "I'm really trying to repair my bond with [sis_name]."
                mc "It will probably take some time tho."
                mc "Give me a chance. I'll show you."
                sf "I guess we'll talk about that again."
                sf "I really hope you're serious about that."
                mc "I am."
            "I don't understand.":
                $ ProcessStat(-1, "sf_affection")
                $ DumpNotStack()
                scene ep3_sc3_shop_12
                mc "I'm trying my best not to be that asshole you described anymore."
                mc "What more can I do?"
                mc "Am I supposed to mindlessly submit to her?"
                scene ep3_sc3_shop_13
                sf "No, you are just supposed to behave like an adult."
                mc "I'm trying. But you know, there's more than one person in a relationship."
                sf "I know that very well."

        off "An awkward silence leads to us slowly getting away from each other."
        off "She quickly resumes her exploration of the shop while I go back to the sofa."
    return

label ep3sc3_breakpoint_2:
    scene ep3_sc3_shop_14
    off "That's crazy."

    "I'm about to try to convince [sis_name] to give me her lips again."
    off "How do I do that?"
    off "Ok, first, let's talk about last night and then try to move forward."
    off "The best way is probably to be blunt about it."
    off "Fuck. I have no idea how to open the conversation."
    off "I'll have to improvise."
    scene ep3_sc3_shop_15
    mc "Hey."
    sis "Hey..."
    off "She looks around only to notice that we are alone in that corner of the shop, [sf_name] is nowhere to be seen."
    off "She seems nervous."

    if ep2sismoviekiss == True:

        menu:
            "Hey, is something wrong? [sisLovePath]":
                mc "You seem worried."
                scene ep3_sc3_shop_16
                off "She turns her back on me and starts rummaging into the nearest display of underwear."
                sis "... You want to talk about last night."
                mc "Yes. I want to talk about last night."
                sis "There is nothing to talk about."
                sis "I was a bit drunk, I don't know what's gotten into me."
                sis "It'll never happen again."
                sis "I think I've already told you I was sorry."
                mc "Why are you apologizing?"
                mc "We can agree that you asked for it, but I was the one who kissed you."
                mc "And I did it because I wanted it."
                mc "You didn't force me or anything."
                sis "I... We shouldn't..."
                off "She's practically shaking while nervously messing with some panties."
                off "I grab her hands."
                scene ep3_sc3_shop_17
                off "She turns to me and I look her in the eyes."
                mc "Stop. Please."
                mc "Calm down, Princess."
                mc "You have nothing to be afraid of."
                mc "We're going to talk about it, honestly, and say everything we have to say."
                mc "I won't judge you, you won't judge me."
                mc "Please."
                sis "Okay..."
                scene ep3_sc3_shop_18
                mc "I'll talk first if you don't mind."
                mc "Our relationship is fairly messed up."
                mc "And I'm the one to blame for that."
                mc "I know we almost have to restart from scratch and it will take some time before you can trust me like before."
                mc "I'm lost. I don't know what we are to each other."
                mc "I don't know what you want me to be for you and I don't know what I want to be."
                mc "But last night, I've realized that there are a few things I am truly sure of."
                mc "First, I care about you."
                mc "I want to be there for you. I want to protect you. "
                mc "Second, I like having you in my arms."
                mc "When I hug you, I can feel your warmth and your heartbeat."
                mc "It's like we were two parts finally reunited."
                mc "It feels right."
                mc "Third, when you turned to me, I didn't even try to resist my desire to kiss you."
                mc "I wanted it."
                mc "Four, I liked that kiss."
                mc "Sure, it was weird, and it felt a bit wrong, to begin with, but after an instant, all of that disappeared."
                mc "I was just kissing you and I liked it."
                mc "I can't stop thinking about it since then."
                mc "I'm not sure how I feel about it."
                mc "Was it right? Was it wrong? Wasn't it just a kiss?"
                mc "I don't know, but it's not something we'll resolve without talking about it."
                $ ProcessStat(3, "sis_affection")
                $ DumpNotStack()
                $ ep3sislovespeech = True
                off "She stares at me in silence for a couple of seconds before looking away."
                off "She speaks with a trembling voice. She sounds fragile, like she's about to break."
                scene ep3_sc3_shop_19
                sis "I won't lie to you."
                sis "I'm as lost as you are."
                sis "I liked it too, being in your arms, kissing your lips."
                sis "It felt wrong and I liked it."
                sis "I can't stop thinking about it either."
                sis "It felt wrong, and it will never stop feeling wrong."
                sis "We're not supposed to do that kind of thing together."

                sis "We're friends. We can love each other, but not in that way."

                sis "I'm sorry, [mc_name]. I fucked up everything."
                sis "I asked for that kiss because I was jealous of [sf_name]."
                sis "It was stupid."
                sis "Doing so, I feel like I've probably broken our last chance to get along as when we were younger."
                off "I can feel my heart slowly being crushed by each of her words."
                off "She doesn't want to go further."
                off "She's right. I know it."
                off "What was I hoping for?"
                off "She doesn't look convinced by her own speech."
                off "She seems to be in pain."
                off "Let's get it over with."
                off "Do the right thing, [mc_name]."
                mc "You don't have to worry."
                mc "You haven't broken anything."
                mc "We'll be what you want us to be."
                mc "There's nothing time can't wash away."
                mc "We were just drunk. Don't overthink it. Ok?"
                sis "Ok..."
            "I liked it.":
                $ ep3sislovejoke = True
                scene ep3_sc3_shop_20
                sis "What?"
                off "I managed to surprise her."
                mc "The kiss. I liked it."
                mc "I want to do it again."
                scene ep3_sc3_shop_21

                sis "Are you crazy? We're friends!"

                sis "We were drunk and we made a mistake."
                sis "There's no way it happens again."
                sis "That's disgusting!"
                off "That's a pretty brutal response. Maybe was I too blunt about it?"
                off "Did I fuck up everything again?"
                off "I need an exit. Maybe can I turn this into a joke?"
                mc "Oh? My loss then. It's too bad."
                mc "I can't stop thinking about those sexy lips of yours."
                sis "Are you out of your mind? Wait. You are mocking me."
                scene ep3_sc3_shop_22
                off "I try to smile."
                mc "Well, it was pretty obvious that you were trying to avoid me since this morning."
                mc "I thought it was because of what happened last night and that a little joke could perhaps boost your mood a bit."
                sis "That was so lame."
                mc "I know, sorry about that."
                mc "But listen. It's just as you said."
                mc "We were drunk, we made a mistake, that's all."
                mc "Don't overthink it. We're clear about it."
                mc "You don't have to be ashamed, avoid me or anything."
                mc "Ok?"
                scene ep3_sc3_shop_23
                sis "Okay..."
                off "She sighs deeply."
                sis "You scared me."
                mc "I know, it's the kind of thing us brothers do sometimes."
                mc "But you feel better now, don't you?"
                sis "I guess so..."
    else:
        $ ep3sisrejectedspeech = True
        scene ep3_sc3_shop_24
        mc "So... about last night..."
        sis "I don't want to talk about it."
        mc "But I do."
        sis "There is nothing to say."
        mc "There is a lot to say actually, but a few words may suffice."
        sis "Like what?"
        mc "Like I'm sorry."
        sis "Sorry?"
        mc "Yes. I'm sorry I rejected you."
        scene ep3_sc3_shop_25
        off "She looks at me with incredulity."
        sis "What are you talking about?"
        sis "You did the right thing."
        sis "I was drunk."

        sis "I don't know why I did that but I'm sure as hell it's not something friends should do."

        off "Fuck. Looks like last night was just the alcohol messing with us."
        off "She has zero interest in kissing me now."
        off "I have to found an exit to this conversation."
        off "Let's end it without looking like an idiot."
        mc "I know."
        mc "But I was afraid I've been a bit too blunt about it."
        mc "You seemed a bit embarrassed this morning, I thought it was about last night."
        mc "You have nothing to be ashamed of."
        mc "It was just the alcohol messing with us."
        sis "Of course, it was just the alcohol. What else?"
        mc "Yeah, what else?.. So, we're clear?"
        sis "We're clear."
        $ ProcessStat(2, "sis_affection")
        $ DumpNotStack()

    scene ep3_sc3_shop_26
    off "That's a total fail."
    off "Let's change the subject and hide my disappointment."
    mc "So... Have you found something you like?"
    scene ep3_sc3_shop_27
    off "She looks at me, a bit suspicious."
    sis "I have seen some interesting articles..."
    mc "I didn't know you were into that kind of underwear."
    mc "I never saw you wearing anything like that."
    scene ep3_sc3_shop_28
    sis "Probably because I don't have anything like that."
    sis "And if I had, I wouldn't show it to you."
    mc "I... yeah, of course. That's not what I meant."
    mc "You don't have any problems walking the house in a t-shirt and panties but I guess this is different."
    sis "Very different."
    mc "What are you going to buy?"
    sis "You're really curious. Why do you care?"
    mc "... I'm bored. The sofa isn't even comfortable and I thought that maybe.. you wouldn't mind if I spent that moment with you..."
    sis "After our discussion about last night, you want to stay with me?"
    off "Ok, now that I think of it, maybe I should have left her alone."
    mc "Sorry, I'm not really gifted to... read the mood... If you want me to leave you alone, I'll just go."
    sis "...No, it's fine... I don't mind... You can stay."
    mc "Ok then..."
    scene ep3_sc3_shop_29
    mc "Are we still looking at underwear?"
    mc "This looks more like some S/M enthusiast's outfit."
    off "She laughs lightly."
    sis "You're not wrong."
    mc "To be honest, it doesn't even look sexy to me."
    sis "It probably depends on the person wearing it."
    mc "Do you like it?"
    scene ep3_sc3_shop_30
    sis "Are you crazy? No!"
    mc "Well, That's a relief."
    mc "If you don't buy it you won't have to hide it from mom."
    mc "I imagine her reaction after finding this thing in your laundry."
    sis "She would kill me right on spot I guess."
    sis "But I don't have to worry about that, I won't buy it."
    sis "I won't buy anything."
    mc "Really? Why? You said you saw some interesting articles."
    scene ep3_sc3_shop_31
    sis "You know I don't have any money. I'm just looking."
    mc "You're that poor?"
    sis "I have something like a hundred $ for the next 20 days."
    mc "Well.. That's not much."

    menu:
        "Do you want me to buy something for you? [sisLovePath]":
            $ ProcessStat(1, "sis_affection")
            $ DumpNotStack()
            scene ep3_sc3_shop_32
            sis "What?"
            mc "I can buy something for you if you want."

            sis "You want to buy lingerie, for me?"

            sis "Don't you think it's weird?"
            sis "And by the way I already told you, I don't want you to buy me anything."
            sis "It gives me the impression you're trying to buy me with some gift."
            sis "I'm not like that."
            mc "Well, said like that, it's weird, indeed, but it's a misunderstanding, I misspoke."
            mc "What I meant is that I can lend you money."
            mc "You can buy something and you'll repay me next month."
            sis "Are you serious?"
            mc "I am, Princess."
            sis "Did you look at the price tag on these things?"
            sis "I found an outfit that I like on the other side of the shop."
            sis "It's 160 $ and it's actually one of the cheaper ones."
            mc "160 $!"
            mc "What do you have for that amount?"
            mc "Is it woven with gold or something?"
            sis "Not even."

            menu:
                "That doesn't matter anyway. [sisLovePath]":
                    $ ProcessStat(3, "sis_affection")
                    $ DumpNotStack()
                    $ ep3sislovedebt = True
                    scene ep3_sc3_shop_33
                    mc "Take what you want, I'll pay for it."
                    mc "You'll pay me back when you can."
                    sis "Are you sure about that?"
                    sis "I may not be able to repay you for a couple months at least."
                    mc "No problem."
                    off "She seems to hesitate and looks around her."
                    scene ep3_sc3_shop_35
                    off "She grabs my arm and my face and draws me to her."
                    off "She softly kisses my cheek."
                    off "I can feel her breasts pressed against my shoulder."
                    off "My heart pounds like crazy."
                    sis "... Thank you, [mc_name]."
                    mc "You're welcome."
                    scene ep3_sc3_shop_36
                    sis "I'll go see what's on the other side of the shop."
                    sis "See you later."
                    off "She said that with a playful tone."
                    off "It's very pleasing to hear."
                "Will you be able to repay me back?":
                    $ ProcessStat(-2, "sis_affection")
                    $ DumpNotStack()
                    $ ep3sislovedebtfail = True
                    scene ep3_sc3_shop_37
                    sis "Keep your money, [mc_name]. I don't need that kind of help."
                    mc "I just need you to say it"
                    scene ep3_sc3_shop_38
                    sis "Maybe it's too soon to trust each other. I don't need your charity."
                    sis "I'll go see what's on the other side of the shop."
                    scene ep3_sc3_shop_39
                    sis "See you later."
                    off "She sounds a bit sad."
                    off "I probably said something I shouldn't have."
                    off "Girls are complicated."
        "[sf_name] doesn't seem to have that kind of problem.":

            scene ep3_sc3_shop_40
            sis "She doesn't have the same pocket money as us."
            mc "Her father gives her more than 150 $ a month?"
            sis "Way more."
            sis "She's actually the one paying for most of our expenses when we go out together."
            sis "Her dad isn't home much."
            sis "Perhaps he thinks he can compensate with money."
            mc "That's ... a bit sad..."
            sis "I think so."
            sis "I'll go see what's on the other side of the shop."
            scene ep3_sc3_shop_41
            sis "See you later."
            mc "We part ways and I return to my sofa, wondering how much more time the girls are willing to spend in that pinkish hell."



    return
label ep3sc3_breakpoint_3:
    scene ep3_sc3_shop_43
    off "Fuck this is crazy."
    off "She's going to kill me."
    off "It's obvious."
    off "She was probably drunk, she regrets it and just doesn't want to talk about it."
    off "I'm just going to make her uncomfortable and she will hate me for that."
    off "Breathe, [mc_name]."

    if ep3sfsislovechat == True:
        off "[sf_name] told me that [sis_name] has a thing for me. "
        off "I'll have to check that, one way or another."

    off "If she gets mad, you can at least pretend you feel bad about it."
    off "Only one cabin is occupied."
    off "She's alone in that room."
    off "Let's close the door for some added privacy."
    scene ep3_sc3_shop_44
    mc "[sis_name]?"
    sis "[mc_name]?"
    mc "We need to talk."
    sis "...I don't think so."
    mc "I've liked it."
    sis "I don't know what you're talking about."
    mc "Come on. There's no point in denying it."
    mc "You liked it too."
    sis "No, I didn't."
    mc "You're a very bad liar."
    mc "Open that door, look me in the eye and tell me you didn't like it."
    sis "I'm trying on lingerie. I'm half-naked."
    sis "I'm not going to open the door, moron."
    off "I don't even know why I try to open the door myself."
    off "Not even for a second do I think she would have let it unlocked."
    scene ep3_sc3_shop_45
    off "I'm as surprised as her when the door to the cabin open itself."
    sis "[mc_name]! What the fuck?!"

    menu galleryScene4:
        "Holy shit!":
            $ ep3siswalkinfail = True
            mc "I'm sorry!"
            sis "Close the fucking door, moron!"
            mc "Why wasn't it locked?"
            sis "I don't know! Why did you open it?"
            mc "That's the second time you've played that trick on me within two days."
            sis "I'm going to kill you for real!"
            mc "I'm so sorry, [sis_name]. I .. I'll wait outside."
            sis "Moron!"
            scene ep3_sc3_shop_61
            off "That was a total replay of what happened yesterday."
            off "She's going to kill me when she gets out of this fitting room."
            off "I fucked up again. I should really stop being an idiot."
            off "I can forget the idea of touching her again..."
            $ ProcessStat(-5, "sis_submission")
            $ DumpNotStack()
        "Hello, Princess. [sisSubPath]":

            $ ep3siswalkinsuccess = True
            off "I don't know where I find the balls to act."
            off "I enter the cabin and close the door behind me."
            scene ep3_sc3_shop_46
            $ UnlockThat("ep3/ep3_sc3_shop_46")
            off "My boldness leaves her speechless."
            $ ProcessStat(2, "sis_submission")
            $ DumpNotStack()
            mc "Look me in the eye."
            mc "Tell me you didn't like when I fingered your pussy."
            off "Her voice is barely a whisper."
            scene ep3_sc3_shop_47
            sis "Lower your voice, please!"
            sis "Someone could hear us."
            mc "You can't even look at me."
            mc "You liked it. You liked it so much you can't stop thinking about it since it happened."
            sis "You're crazy. This is not a place to talk about that."
            sis "We'll talk at home."
            mc "No, we won't. We'll talk here and now."
            scene ep3_sc3_shop_46
            off "The cabin is pretty spacious but in the heat of the moment, I cornered her without thinking about it."
            off "Her breathing is heavy and loud."
            sis "I don't want to answer that."
            off "Only now I realize that she hasn't even told me to get out of the cabin."
            mc "I'll say it for you."
            mc "You liked it."
            mc "You enjoyed it."
            mc "You want it to happen again."
            sis "You're crazy."
            mc "Yeah, maybe I'm crazy. But still. You haven't said no."
            off "She refuses to look at me and stays silent."
            mc "That's an interesting answer."

            menu:
                "Touch her. [sisSubPath]" if sis_submission > 15:
                    $ ep3siswalkintouched = True
                    $ ProcessStat(3, "sis_submission")
                    $ DumpNotStack()
                    scene ep3_sc3_shop_48
                    $ UnlockThat("ep3/ep3_sc3_shop_48")
                    off "Gently, I put my hand on her hips and caress her."
                    off "I can feel her tense under my touch."
                    off "Her mouth slightly opens. She gasps heavily."
                    off "She doesn't protest otherwise."
                    mc "You seem rather excited by this discussion."
                    sis "I'm not excited at all."
                    mc "Really? Should I check by myself?"
                    off "Her breathing intensifies."
                    off "I slowly move my fingers towards her pussy."
                    off "I play with her panties a bit."
                    scene ep3_sc3_shop_49
                    $ UnlockThat("ep3/ep3_sc3_shop_49")
                    off "She doesn't protest when I slowly insert two fingers in her underwear."
                    off "I'm about to reach her pussy when we hear knocking on the door of the room."
                    sf "[sis_name], are you here?"
                    off "Closing that door really was a genius idea."
                    off "I get out of the cabin and seat on the nearest sofa."
                    scene ep3_sc3_shop_50
                    mc "You can come in, [sf_name]."
                    sf "You're in here, [mc_name]?"
                    off "She seems a little bit confused by my presence in this room."
                    mc "I am. [sis_name] is in this cabin."
                    sis "We were chatting."
                    sis "I'm almost done. Give me a couple minutes."
                    sf "Sure. You found anything you like?"
                    sis "Not really. What about you?"
                    sf "I'll show you at home."
                    mc "I'll leave you girl to your chatting."
                    scene ep3_sc3_shop_52
                    mc "I get out of the fitting room and return to my sofa."
                    mc "That was hot... And I can only imagine what would have happened if we hadn't been interrupted by [sf_name]."
                "Don't.":

                    off "The silence between us lasts long enough to become awkward."
                    scene ep3_sc3_shop_51
                    $ UnlockThat("ep3/ep3_sc3_shop_51")
                    off "She looks at me and seems to wait for something."
                    mc "So..."
                    sis "... I need to get dressed. You should get out."
                    off "I lose the initiative and the mood changes drastically. "
                    off "The game is over."
                    mc "Indeed. I'll wait for you outside, Princess."

                    scene ep3_sc3_shop_52
                    off "I leave her be and go back to my sofa."
                    off "Things could have gone better but it's still a success for Mr. Pervert."

    $ renpy.end_replay()


    return

label ep3sc3_breakpoint_4:

    scene ep3_sc3_shop_55
    mc "[sf_name]?"
    sf "I'm here, [mc_name]."
    mc "You want to talk to me?"
    sf "Yes, please close the door behind you."
    sf "We want some privacy."
    mc "Ok... So... What do you want to talk about?"
    scene ep3_sc3_shop_56
    sf "It's a bit embarrassing."
    sf "It's about the foot massage you gave me yesterday."
    mc "Do you want another one?"
    sf "Well, I wonder. Could you provide the same performance as the last time?"

    menu:
        "I'll be honest with you. [sfLovePath]":
            $ ep3massagehonesty = True
            $ ProcessStat(1, "sf_affection")
            $ DumpNotStack()
            mc "Yesterday was my first time massaging anyone."
            mc "I had no idea what I was doing."
            mc "I'm really glad it pleased you and I'll be happy to massage you whenever you feel like, but I'm not sure I can reproduce... that... level of success."
            scene ep3_sc3_shop_57
            sf "I appreciate your sincerity."
        "Yes! Yes of course! [sfDomPath]":
            $ ProcessStat(1, "sf_dominance")
            $ DumpNotStack()
            sf "You seem so confident."
            sf "That's very reassuring."
            sf "Because, as you may already know, I don't like being disappointed."
            off "Her tone is very strange."
            off "It's playful but in the meantime, you can feel she means every word."
            off "She's not kidding. If I deceive her, there will be consequences."
            mc "... Well... I'll do my best at least..."
            sf "Will it be enough?"
            mc "... I hope so..."
            off "Why do I feel like a child lying to his schoolmistress?"

    sf "I really enjoyed your touch."
    sf "It was gentle yet firm."
    sf "As you probably noticed, you managed to press the right spots."
    mc "I'm happy you liked it."
    sf "I won't lie, [mc_name]. It got me interested in you."
    sf "As you may know, I haven't had many relationships until now."
    sf "If it happens, it would pretty much be my first one."
    sf "So you may understand that I want my partner to be perfect."
    sf "And I can be very difficult to please."
    sf "I think you have potential but I'm not sure you'll be up to the task."
    off "That's a very strange way to talk about a possible relationship."
    off "It sounds like I'm having some kind of job interview..."
    off "What kind of act are we playing here?"

    menu:
        "Well, I'm ready to try. [sfDomPath]":
            sf "Trying is not good enough."
            sf "Trying means you can fail."
            sf "Are you planning on failing me, [mc_name]?"
            mc "Of course not. I'm only aiming to please you..."
            sf "That's what I wanted to hear."
            $ ProcessStat(1, "sf_dominance")
            $ DumpNotStack()
        "Excuse me, [sf_name], I'm a little bit confused.":
            sf "Which part of our discussion confuses you, [mc_name]?"
            scene ep3_sc3_shop_58
            off "There's no way she doesn't know the curtain is half-open."
            off "Is she showing off for me...?"
            sf "Do you want us to be in a relationship or not?"

            menu:
                "I do, yes. [sfDomPath]":
                    sf "Then, are you willing to prove yourself worthy of me?"
                    mc "I ... guess so..."
                    sf "Good."
                    $ ProcessStat(1, "sf_dominance")
                    $ DumpNotStack()
                "The way you talk about it is a little bit disturbing.":
                    sf "I'm sorry, I may be a little clumsy with my words."
                    sf "As I said this is an embarrassing subject for me."
                    sf "I'm not used at all of discussing that kind of thing."
                    sf "I don't know how to proceed. If there's even a correct way to proceed in that matter."
                    sf "Am I that weird?"
                    scene ep3_sc3_shop_59
                    $ UnlockThat("ep3/ep3_sc3_shop_59")
                    off "Holy shit."
                    off "Dear, not only are you weird, I'm pretty sure you're also totally socially unadapted."
                    off "I don't know what you think you're doing but you clearly have no idea how to behave with a guy."
                    off "That said, your ass is to die for."
                    scene ep3_sc3_shop_60
                    $ UnlockThat("ep3/ep3_sc3_shop_60")
                    $ ep3sflingerieshow = True
                    mc "A bit, but.. weird can be charming in its own way..."
                    $ ProcessStat(1, "sf_affection")
                    $ DumpNotStack()
                    sf "I'm glad to hear it."
                    sf "I hope I didn't scare you or anything..."
                    mc "No, not at all."
                    sf "Then... about that relationship?"
                    scene ep3_sc3_shop_56

                    menu:
                        "Of course, I'm all yours. [sfDomPath]":
                            sf "Good!"
                        "I don't know how to say that, [sf_name].":
                            $ ep3sfdomrejected = True
                            mc "But right now is not a very good time for me."
                            mc "With all that happened yesterday and the things you told me about [sis_name]..."
                            mc "I need time to clear my head... and think about all of that..."
                            mc "I'm not sure I can give you the attention you deserve right now."
                            sf "... Are you.. rejecting me?"
                            off "She sounds so sad. She's probably about to cry."
                            mc "I can't believe it myself but .. I guess I am... I'm sorry, [sf_name]."
                            sf "So this is how it feels like..."
                            sf "Thank you for your honesty, [mc_name]."
                            sf "Can you please leave me alone?"
                            mc "Of course [sf_name]. I'm sorry."
                            mc "I hope we can still be friends."
                            sf "Friends, that sounds nice."
                            sf "Thank you, [mc_name]."
                            off "I just rejected the girl I fantasized about for the last three years or so."
                            off "I must be crazy."
                            return

    mc "So .. you're my girlfriend now?"
    sf "Oh God no. Not yet, [mc_name]."
    mc "Not yet?"
    sf "Let's say you are on a trial right now."
    mc "What do you mean?"
    sf "That we'll keep it a secret for a week or so."
    sf "Just the time to investigate our compatibility."
    mc "I'm your secret boyfriend, for the week..."
    sf "You are, dear. [sis_name], especially, mustn't know about us."
    mc "Ok..."
    sf "You may go now, we don't want her to find us out."
    if ep3sflingerieshow == True:
        sf "Oh, and before you go, [mc_name], did you like the show?"
        off "You naughty girl."
        mc "I did yes."
        sf "I'm glad to hear it."
    sf "See you later, [mc_name]."
    mc "... See you later..."
    $ ProcessStat(1, "sf_dominance")
    $ DumpNotStack()
    $ ep3sfdomrelationship = True
    scene ep3_sc3_shop_61
    off "What. The. Fuck?"
    off "Isn't that beyond crazy?"
    off "I now have a secret girlfriend I didn't even kiss... and I feel very strange about it."
    off "That girl is definitely crazy."
    off "And I'm probably a fool to play her game."
    return

label ep3sc4:
    scene black with dissolve
    with Pause(2)
    show text "Half an hour later."
    with Pause(2)
    scene ep3_sc4_cs_0
    sf "Come on, you've never drank an iced coffee?"
    sf "You have to try it."
    mc "I'm pretty sure I can live without it."
    mc "Besides, [sis_name] seems to think that they're not that good."
    sis "It's not bad, it's just not to my liking."
    sf "You can't take her word on that, you need to taste it."
    mc "Are you denying me the freedom to choose my drink?"
    sf "Yes, I am. You will thank me later."
    sf "Three iced coffee, please. Milk and no sugar."
    sis "Mine with sweetened condensed milk, please."
    mc "Milk and no sugar. Sweetened condensed milk."
    mc "Alright."

    off "We were on our way home when we passed by this coffee shop."
    off "[sf_name] insisted that we stop to drink some iced coffee. "
    off "I didn't even know that thing was drinkable."
    off "As per all the shops we visited today, the coffee is almost empty."
    off "I'm not surprised."
    off "We're on a Monday afternoon and still in the middle of a heatwave."
    off "If they're not at work, smart people stay at home."
    off "We order our drinks and choose a table to settle on."
    scene ep3_sc4_cs_1
    sf "So, [mc_name], did you like shopping with us?"
    mc "It was fine."
    sf "Really? Are you planning on shopping with us again?"
    mc "Maybe not..."
    mc "If I can be honest about it..."
    mc "It wasn't the greatest time of my life, but it wasn't that bad either."
    sf "And about that iced coffee?"
    menu:
        "It's delicious. [sfLovePath]":
            $ ep3icedcoffeeliked = True
            $ ProcessStat(1, "sf_affection")
            $ DumpNotStack()
            sf "See? I told you."
            sf "Next time you should try with some cream."
            mc "I'll keep that in mind but the cream isn't usually my thing."
            sf "You may be surprised."
            mc "I am already surprised."
        "I'm not crazy about it. [sisLovePath]":
            $ ProcessStat(1, "sis_affection")
            $ DumpNotStack()
            sf "It's not for everyone, but at least you know what to think of it now."
            sis "Like he said, he could have lived without it."
            mc "At least I know how it tastes."
            sis "Sugar and milk helps a lot to deal with it."
            mc "Hence the Sweetened condensed milk."
            sis "Cream works fine too"
            mc "I may try that next time."

    scene ep3_sc4_cs_2
    sis "What do you want to do tonight, [sf_name]?"
    sf "I don't know, I'm a bit tired."
    sf "I thought we could just chill on the couch, maybe watch a couple movies, get to bed at a reasonable time without being drunk..."
    sis "Sounds like a plan."
    sf "Great! Are you joining us, [mc_name]?"
    mc "Of course I am."

    if ep2sismovie == True or ep2sisfingered == True:
        mc "I liked the movie last night by the way."
        mc "I was thinking about proposing some kind of movie night myself."

        if ep2sismoviekiss == True or ep2sisfingered == True:
            scene ep3_sc4_cs_3
            off "[sis_name] is looking at me with fear and surprise."

        sf "The movie last night?"
        mc "Yes. I got up last night, [sis_name] was watching an old black and white movie in the living room."
        mc "I joined her. It was nice."
        mc "And the movie was good. I enjoyed it."
        mc "What about you [sis_name]? Did you like it?"
        sis "I guess... I... enjoyed it too..."
        sf "Are you guys having secret meetings while I'm sleeping?"
        scene ep3_sc4_cs_4
        sis "It was totally fortuitous."
        scene ep3_sc4_cs_5
        sis "And by the way, at that time, you were sleeping and snoring like a chainsaw."
        sis "That's what got me up in the first place."
        sf "I'm so sorry about that."
        sf "It's the first time it happened to me."
        scene ep3_sc4_cs_4
        sis "We'll know about that tonight for sure..."
        mc "Don't stress too much over it."
        mc "Chances are it was alcohol-related."
        sf "I hope so."

    scene ep3_sc4_cs_4
    sis "So it's settled, tonight is movie night."
    sis "Now, what about the food?"
    sis "Honestly, I already know I will be starving in a couple hours."
    sis "Pizza? Or maybe we can stop by a grocery store and buy a bunch of hot pockets?"
    mc "I'm okay with both."
    sf "Come on, I can't believe it."
    sf "Your dad is a doctor, how can you eat so badly? "
    mc "Dad is probably the unhealthiest eater out of the family."

    sis "His Mom is the reason we sometimes eat vegetables."

    sf "I'll do something."
    sf "Let's stop by a grocery store on our way back home."
    sf "I'll probably only make sandwiches but at least they'll be healthy ones."
    mc "Do you hear that, Princess?"
    mc "We're eating healthy tonight."
    sis "I hope we will not have a fat deficiency or something."
    scene ep3_sc4_cs_6
    sf "You little rascals, I will teach you respect..."
    mc "If you'll excuse me, ladies, I have to visit the restroom."
    off "I leave them laughing and head to the men's room."
    scene black with dissolve
    with Pause(2)
    off "5 minutes later I'm about to head back to our table when my phone softly buzz."
    scene ep3_sc4_cs_7
    off "It's a text message. From Steve."
    off "Holy shit."
    scene ep3_spe_01
    $ UnlockThat("ep3/ep3_spe_01")
    mf "She wanted me to send you this."
    mf "She is crazy!"
    off "He looks like he's having quite some fun."
    off "The lucky bastard."
    scene ep3_sc4_cs_7
    off "I quickly message him back."
    mc "It's nice to keep me updated, thank you."
    mc "I guess we'll talk later."
    scene ep3_sc4_cs_8
    off "I wonder if Steve will get the ironic tone of my reply."
    off "Who is this guy?"
    scene ep3_sc4_cs_9
    lk "You should have told me!"
    lk "I could have helped you."
    sf "I don't think so."
    off "[sf_name] sounds like she's not happy to see him."
    lk "You're suspicious of me, I can understand that..."
    lk "After all, we barely know each other."
    scene ep3_sc4_cs_10
    mc "Ladies, is there a problem?"
    sf "[mc_name], this is Luke."
    lk "Hello, [mc_name]. It's a pleasure to meet you."
    scene ep3_sc4_cs_11
    menu:
        "Shake his hand.":
            scene ep3_sc4_cs_13
            menu:
                "A pleasure to meet you too.":
                    $ ep3handshaked = True


                    lk "I understand you are [sis_name]'s little friend?"
                    mc "Little friend? Really?"
                    mc "I'm taller."

                    lk "I can see that."
                    lk "I was explaining to [sis_name] and [sf_name] that my brother and I have nothing to do with what happened to her on Saturday night."
                    lk "I understand you first believed we were the ones who drugged her."
                    lk "We're basically strangers."
                    lk "But we're totally innocent."
                    lk "Honestly, I'm ashamed."
                    lk "I saw nothing."
                    lk "I thought she was tired and drunk."
                    lk "I was about to propose her a ride home when [sf_name] took the matters in her own hands."
                    scene ep3_sc4_cs_21
                    mc "I'm glad she was there."
                    lk "I guess we all are."
                    lk "Anyway, I'm happy I could clear this misunderstanding."
                    lk "[sis_name], I think you have my phone number, if you need anything, please let me now."
                    lk "I hope we'll meet again soon."
                    sis "Yeah... sure..."
                    off "He leaves the coffee shop with a smile on his face."
                    $ ProcessStat(-5, "sf_affection")
                    $ ProcessStat(-5, "sis_affection")
                    $ DumpNotStack()
                    scene ep3_sc4_cs_22
                    mc "Well, that was pretty awkward, wasn't it?"
                    sf "A pleasure to meet you too? Really?"
                    mc "What? I was trying to be civilized."
                    sf "The man drugged [sis_name] to rape her, why would you even try to be civilized?"
                    mc "I don't know... It just came out like that."
                    sis "Guys, it's ok. Let's just go back home, please."
                    mc "You're sure you're alright, [sis_name]?"
                    sis "I'm ok. I just want to go home."
                    mc "Let's go then..."

                "So, you're the guy from Saturday night, hu?" if ep2brutalbreakfast == True:
                    $ ep3facebroken = True
                    scene ep3_sc4_cs_14
                    $ UnlockThat("ep3/ep3_sc4_cs_14")
                    off "I kick him so hard that I almost lift him in the air. "
                    off "The girls scream."
                    scene ep3_sc4_cs_15
                    sf "Oh my God!"
                    sis "[mc_name]!"
                    mc "So you're pleased to meet me, motherfucker?"
                    scene ep3_sc4_cs_16
                    mc "How do you like my company, hu?"
                    scene ep3_sc4_cs_17
                    sf "[mc_name]! Stop! Please!"
                    sis "Are you crazy?"
                    scene ep3_sc4_cs_18
                    off "I can hear the staff of the coffee shop ordering us to leave before they call the police."
                    mc "You approach them again and I'll break both your legs, you fucking rapist."
                    mc "Am I clear?"

                    mc "If [sis_name] or [sf_name] complain about you again, I will find you and I will put you in a wheelchair for the rest of your life."

                    mc "Do you hear me?"


                    $ ProcessStat(3, "sf_affection")
                    $ ProcessStat(3, "sis_affection")
                    $ ProcessStat(3, "sis_submission")
                    $ DumpNotStack()
                    sf "[mc_name]! We have to go!"
                    sf "We're sorry! We're leaving!"
                    scene black with dissolve
                    off "The girls quickly drag me out of the coffee shop and onto the car."
                    off "[sis_name] keeps saying that someone will call the cops on us while Cassie is about to laugh."
                    off "I'm surprisingly calm."
                    off "I have no idea where I've found the strength to hit that guy so hard."
                    off "I'm pretty sure that I wouldn't be able to do it again even if I wanted to."
                    off "Maybe it was a bit extreme."
                    off "I've hit him without even thinking of the consequences."
                    off "A true gentleman would probably have chosen discussion over brawl."
        "[gr]Don't shake it.":

            $ ep3scaredluke = True


            mc "You intended to rape my friend and you think I'm going to shake your hand?"

            scene ep3_sc4_cs_12
            lk "Listen, as I just said to [sis_name] and [sf_name], I have nothing to do with that incident."
            lk "I understand your suspicions as we are basically strangers to you, but my brother and I are totally innocent."
            mc "Really, that is good news."
            mc "I'm glad we can discuss this matter as two civilized men."
            mc "I have a proposition for you."
            mc "You never approach [sis_name] or [sf_name] again and I don't break your face."
            mc "What do you think?"
            lk "I'm sorry, I don't want to cause any problems."
            mc "What are you doing here then?"
            lk "I had no idea what happened, I was simply worried as she wasn't well when she left the club."
            mc "Sure, that's why you followed them home?"
            scene ep3_sc4_cs_12_more
            lk "I don't know what you're talking about."
            lk "We followed no one, nowhere."
            mc "How did you obtain our address then, your flowers didn't find us by magic."
            lk "A friend of [sis_name] saw us at the club, she noticed I was worried, she gave me your address."
            mc "[sis_name] has no friend."
            mc "What's her name?"
            mc "Are you one of those cunts who tried to hurt her?"
            lk "I think I'd better go, I'm obviously not wanted here."
            lk "I can understand that you need to be angry at someone for what happened."
            lk "We'll all laugh about that in a couple days once we all have calmed down..."
            mc "No, we won't, we won't see you again."
            mc "What is so hard to understand in my sentence?"
            mc "What the fuck are you still doing here?"
            mc "Why does it take you so long to get the fuck out?"
            scene ep3_sc4_cs_19
            lk "I'm leaving! I'm leaving right now!"
            lk "I'm sorry, I didn't want to impose myself."
            mc "But you did anyway."
            $ ProcessStat(4, "sf_affection")
            $ ProcessStat(4, "sis_affection")
            $ ProcessStat(4, "sis_submission")
            $ DumpNotStack()
            scene ep3_sc4_cs_20
            mc "Are you alright?"
            sis "We're ok. I just want to go home, if you don't mind."
            mc "Let's go. We'll talk in the car."

    scene black with dissolve
    with Pause(2)


label ep3sc5:
    scene black with dissolve
    if ep3facebroken == True:
        scene ep3_sc5_car_00
        sis "Are you crazy?!"
        sf "Why did you do that?"
        sis "They're going to call the cops!"
        sf "What are we going to do?!"
        sis "You almost killed him!"
        sf "You think he's dead?"
        sis "Oh my God!"
        mc "Ok, enough! Calm down!"
        mc "He's not dead, I've barely hit him."
        mc "He'll probably have a little bruise, nothing more."
        mc "And he won't call the cops, he's too afraid of us talking to them about Saturday night."
        mc "He drugged you, he harassed you, and he annoyed you today too."
        mc "He deserved to take a beating."
        mc "I've been pretty nice not to hit him some more."
        scene ep3_sc5_car_01
        sf "We have no proof, [mc_name]."
        sf "You assaulted him."
        sf "You could be sent in jail for that."


        sis "We have to call your mom."

        mc "No, we don't. You're the one who didn't want to call her."
        mc "It'll be fine. We'll manage. We're adults."
        sis "Yeah sure. And when the cops come for you, what will we do?"
        mc "Well, if they come, you will call her."
        mc "But they won't come. They won't even know what happened."
        scene ep3_sc5_car_02
        sis "I hope you're right."
        mc "Don't worry, we'll be fine."
        sf "I still can't believe you could be so violent, [mc_name]."

        menu:
            "I can't believe it myself. [sisLovePath] [sfLovePath]":
                $ ProcessStat(1, "sf_affection")
                $ ProcessStat(1, "sis_affection")
                $ DumpNotStack()
                scene ep3_sc5_car_03
                mc "It's the first time I've hit someone."
                mc "I wasn't even sure I could do it."
                sis "No, it's not your first time."
                mc "What are you talking about?"
                sis "You don't remember?"
                sis "I think we were 10, maybe 11 years old."
                sis "There was this boy who kept annoying me by lifting my skirt."
                sis "He made me cry."
                sf "What happened?"
                sis "[mc_name] headbutted him and broke the boy's nose."
                sis "There was blood everywhere."
                sf "Oh my God."

                sis "Yeah, his Mom was pretty pissed off, his Dad was... proud somehow."

                mc "I don't remember it... "
                sis "Well.. I do."
            "What can I say?":

                scene ep3_sc5_car_03
                $ ProcessStat(-1, "sis_affection")
                $ ProcessStat(-1, "sf_affection")
                $ DumpNotStack()
                mc "I'm just defending my turf."
                sis "Your turf?"
                sf "Are you serious right now? We are your turf?"
                mc "Well ... It sure doesn't sound too good .. but .. I mean... it's just a way of speaking..."
                sf "I certainly hope so..."

    elif ep3handshaked == True:
        scene ep3_sc5_car_08
        sf "I can't believe you shook hands with him."
        mc "What did you want me to do? Punch him in the face?"
        sf "Anything would have been better than licking his ass like you did."
        mc "I didn't lick his ass, I was simply polite."
        mc "He wasn't aggressive, I had no reason to be an asshole to him."
        sf "No reason? Are you kidding me?"

        sf "He tried to rape [sis_name]. Isn't that sufficient enough?"

        mc "It is... but we have no proof."
        scene ep3_sc5_car_00
        sis "It's ok [sf_name], [mc_name] is right, we have no proof."
        sis "There's nothing we can do."
        sf "There's a lot we can do."
        sf "We can go to the police."
        sf "It's probably too late to find the drug in your blood but this guy is clearly stalking you!"
        mc "There is no evidence of that."
        scene ep3_sc5_car_01
        sf "Whose side are you on, [mc_name]?"
        mc "I'm on [sis_name]'s side."
        mc "And I agree with you, we should go to the police. But [sis_name] doesn't want that."
        sis "No, I don't want that."

    elif ep3scaredluke == True:
        scene ep3_sc5_car_00
        sf "I'm glad you were there, [mc_name]."
        sf "We asked him to leave us alone but he didn't bother listening."
        mc "I doubt he would have done anything to you in public, besides talking, but the man is undoubtedly annoying."
        sf "And persistent."
        sis "At one point, I thought you were going to punch him."
        sf "The look on his face when he left. I think you scared him."
        mc "I hope so. He will probably think again before coming back at you."

    scene ep3_sc5_car_02
    mc "Anyway, can you tell me what happened while I was in the restroom?"
    sis "Not much."
    sis "He entered the coffee shop just after you were gone."
    sis "He came directly to us."
    sf "He said he was glad to see us, that he was worried."
    sf "He asked why [sis_name] didn't call him."
    sf "I told him what someone drugged [sis_name], that we have a strong suspicion it was his doing and that we have no desire to see him again."
    sf "He said he was sorry, that he understood, that he was going to leave us alone."
    sf "But instead of leaving, he casually sat on the sofa arm and started talking about how he and his brother are nice guys, that they didn't do anything."
    sis "And then you came back."
    off "On the dashboard, my phone suddenly buzzes."
    scene ep3_sc5_car_04
    sis "I'll give it a look for you."
    off "She grabs it before I could even respond."
    sis "It's your girlfriend."
    sf "You have a girlfriend, [mc_name]?"
    mc "No, I don't. It's probably from Steve."
    off "He's probably sending me something classy again."
    off "I'm glad my phone is locked."
    off "At least until [sis_name] casually unlocks it."
    off "How the fuck does she know my code?"
    scene ep3_sc5_car_05
    off "The car is suddenly filled with the voice of Steve and the moans of an unknown girl."
    sis "Oh my god."
    mf "Holy fuck, [mc_name], this girl is crazy!"
    mf "She wants me to send you this clip."
    mf "I hope you'll enjoy it!"
    mf "Oh, baby, you're so tight!"
    off "Of course, it had to be that kind of message."
    mc "Great. I'm so glad we can share this moment. Together."
    off "At least it will lighten the mood."
    scene ep3_sc5_car_06
    $ UnlockThat("ep3/ep3_spe_02")
    sf "Is that Steve?"
    sis "I think so..."
    sf "Oh my god, is it in her ass?"
    sis "No, no, he's fucking her pussy. Look."
    sf "She seems pretty. I wonder how Steve managed to seduce her."
    off "Are they commentating Steve's performances or am I dreaming?"
    off "Does this video ever end?"
    scene ep3_sc5_car_06_plus
    sf "Oh my God, she's taking it all so easily."
    sis "I'm not sure it's that impressive."
    sf "What do you mean?"
    sis "I don't think he's.. that big..."
    sf "Well he's not as big as a porn star for sure."
    sf "But normal human beings aren't supposed to be hung like a horse."
    sis "I don't know... [mc_name] is much bigger."
    sf "Really?"
    if ep2goodsexposed == True:
        off "Holy shit. Is she going to talk about that?"
    else:
        off "What the fuck...?"
        off "How can she know that?"
        off "Last time we saw each other naked we were probably 6 years old or something like that."

    mc "Excuse me, ladies? I'm here! Could you stop that?"
    sis "It's not over yet."
    mc "Oh God, could you please, at least, stay seated?"
    off "It's useless."
    off "They don't care about anything I say."
    sf "Oh my God, did he..."
    sis "He just came... inside her...?"
    sf "They're not even using a condom!"
    scene ep3_sc5_car_07
    off "The video ends and [sis_name] puts my phone back on the dashboard."
    sis "That's crazy."
    sis "They were fucking on the beach."
    sis "Anyone could have seen them."
    mc "Looks like it wasn't enough for them as he had to send me that video."
    sis "Does he send you things like that often?"
    mc "No. It's a new thing. He says she's the one who wants to .. communicate."
    sis "Who is she?"
    mc "I don't know. He met her on the beach a few days ago."
    sis "A few days ago and they're already fucking?"
    mc "I thought it was one of his made-up stories."
    sis "It looked pretty real to me just now."
    sf "How is this possible?"
    mc "What do you mean?"
    sf "It's Steve, how did he manage to get a girl to do that with him?"
    mc "You don't like him very much, do you?"
    mc "He's a nice guy when you know him."
    sf "He's clearly not a bad guy, but he's also a moron."
    sf "Last semester he tried to impress me by stuffing his nose with French fries."
    mc "He sometimes acts.. impulsively..."
    sis "Maybe she likes French fries more than you do."
    sf "He ate those fries afterward."
    sis "That's disgusting."
    off "A short silence marks the end of this discussion."
    mc "So ... what kind of movie are we watching tonight?"
    scene ep3_sc5_car_09
    sf "Wait. You said that [mc_name] is bigger?"
    off "Great."
    sf "How do you know? Have you seen it recently?"
    mc "Hey Ladies, I'm in this car with you."
    sis "I ... walked in on him in the bathroom.... last year."
    sis "By accident."
    sf "And you saw his dick..."
    sf "Which turns out to be... much bigger..."
    sis "Yes..."
    if ep2goodsexposed == True:
        off "Well, that's not totally a lie... but still."
    else:
        off "I have no idea what she's talking about."
        off "I don't remember her walking in on me like that."

    mc "Please, can you not discuss the size of my dick in my presence?"
    mc "I'm very uncomfortable with the idea of the two of you talking about that."
    off "The silence that follows is beyond awkward and long enough for us to reach home."



label ep3sc6:
    scene black with dissolve
    with Pause(2)
    scene ep3_sc6_mcr_0
    off "As soon as we arrive, the girls disappear in [sis_name]'s room."
    off "I don't know what they're doing in there but I can hear them laughing hysterically."
    off "The Steve incident lightened the mood of the day."
    off "Weirdly, but it's still better than focusing on what happened at the coffee shop."
    off "We forgot to stop by the grocery store."
    off "The healthy sandwiches will be for another day."
    scene ep3_sc6_mcr_1
    off "I quickly look at the video Steve send me."
    off "They are crazy."
    off "I should call him back but what am I going to say?"

    if ep2sismoviekiss == True:
        off "That I kissed [sis_name], and that she somehow rejected me when I came for another round?"
    if ep2kissedsf == True:
        off "That I kissed [sf_name] but I can't be with her because she's afraid of [sis_name]'s reaction?"
    if ep2sisfingered == True:
        off "That I fingered [sis_name] while she was giving me a handjob?"
    if ep3sfdomrelationship == True:
        off "That I gave [sf_name] a feet massage and that she is now my .. secret... crazy... girlfriend?"
    if ep2sisabused == True:

        off "That I've put my dick in the mouth of my sleeping childhood friend?"

    off "I'm not sure telling him any of this would be wise."


    off "Someone knocks on my door."
    mc "Come in."
    scene ep3_sc6_mcr_2
    sis "Hey, [mc_name]."
    mc "Hey."
    sis "We're sorry but we're actually going to leave you alone tonight."
    sis "Something... came up."
    mc "Oh... no problem. Don't worry about me."
    mc "I'll just hit the sofa by myself with a pizza and everything will be fine."
    mc "May I ask where you're going?"
    sis "There's a girl who has been a total cunt to us for the last three years."
    sis "She just invited us to some kind of barbecue party at her house."
    sis "We are .. curious."
    mc "Really? Doesn't it smell like a trap to you? It's pretty obvious..."
    sf "We're pretty sure it's some kind of bad joke, indeed."
    sf "But we're still curious."
    mc "And you want to go and see... Ok... Just be careful, ok?"
    sf "We will. Movie night tomorrow, we promise!"
    mc "Don't worry about that."
    scene ep3_sc6_mcr_3
    off "The girls hit the shower as soon as they leave my room."
    off "An hour later they take the car and leave the house."
    off "Left alone I spend some time daydreaming and thinking, lying on my bed."
    off "Fantasizing about [sf_name] is pretty standard, but all this stuff with [sis_name] is turning to an obsession."
    off "I can't stop thinking about it and it makes me crazy."
    off "It wasn't like that before this weekend."
    off "That discussion with Steve probably was the starting point of everything."
    off "That bastard made me see things differently and I feel like I can't go back."
    off "I'm stuck with these thoughts about [sis_name]."
    off "My phone rings."
    scene ep3_sc6_mcr_4
    mc "Hey, Steve."
    mf "Hey, [mc_name]! How is it going?"
    mf "Did you watch the video?"
    mf "I would have thought you would call me right after you received it but I guess you were too busy to do so."
    mf "Did you like it?"
    mc "Yeah, I watched it. And so did [sis_name] and [sf_name]."
    mf "What? You've shown them? That's .. unexpected..."
    mf "But also pretty hot. Did it turn them on?"
    mc "They've seen it themselves without me being able to do anything."
    mc "I was driving."
    mc "They've .. commentated a lot, but I don't think they've been turned on as you say."
    mf "Maybe next time."

    menu:
        "[gr]Wait. Next time?":
            mc "You're going to send me more and you want me to show them?"
            mf "Why not? If they're interested."
            mf "I have nothing to hide, and their reaction may be fun to observe."
            mf "And it could give them ideas you could... build on."
            $ ep3stevepicsok = True
        "I certainly hope not.":
            mc "That was embarrassing enough."
            mf "Embarrassing? For who?"
            mf "Certainly not for me."
            mf "I'm fucking a hot girl on the beach."
            mf "I have nothing to be ashamed of."
            mf "I'm proud of it."
            mc "You can be proud as much you want."

            mc "I just don't want my friend to watch your exploits on the beach."

            mf "Why not? Are you jealous?"
            mf "Or maybe you're afraid I'd seduce her that way?"
            mc "Neither."
            mf "Chill out, dude."

            mf "I've already sworn, a long time ago, not to touch your dear [sis_name]."

            mf "But you know, my performances could give her ideas you could... build on."

    mc "It can't be that easy. We're not living in one of your porn games."
    mf "You'd be surprised."
    mf "That aside, I can see you're not protesting anymore."
    mf "You've totally accepted the idea of fucking [sis_name], haven't you?"
    mf "You've embraced it."
    mc "Fuck you."
    mf "Oh, oh, oh! Tell me, my dude."
    mf "Tell me everything. What have you done?"
    scene ep3_sc6_mcr_5
    mc "I don't even know where to start..."
    mf "Try the beginning."
    mc "Well ... two days ago, [sis_name] and I were almost ready to kill each other."
    mc "[sf_name] joined us, and she seemed determined to have [sis_name] and I getting along better."
    mc "On top of that, our last conversation completely fucked up my brain."
    mc "I'm now constantly fantasizing about [sf_name], which is normal, and [sis_name], which is not normal."
    mf "Dude, talking with me hasn't fucked up anything."
    mf "I don't have that kind of power."
    mf "You were already having these thoughts."
    mf "I just made you acknowledge it."
    mf "You seem to be searching for excuses."
    scene ep3_sc6_mcr_4
    mc "Yeah, sure. Anyway."
    mc "[sf_name] explained to me that all the stories of them sucking dicks in the toilets, fucking half the school and so on are total bullshit."
    mc "Nothing is true. Can you believe it?"
    mf "[mc_name]. Everyone knows that."
    mc "What?"
    mf "Everyone knows it's bullshit."
    mc "Are you kidding me? Are you telling me that I'm the only one who believed it?"
    mf "Well, I'm pretty sure that most of the people think that there is no smoke without a fire."
    mf "But no one can believe it all."
    mf "For my part, I always supposed there was a bit of truth in it but it was obvious that the majority of it was pure crap."
    mf "Like, maybe they sucked a couple of dicks, but there's no way they sucked every dick in school but ours."
    mf "Did you honestly buy all that was said about them?"
    mc "Fuck me."
    mc "I'm so lame."
    mc "Now that you say it, it's so obvious."
    mf "I always assumed you were like the rest of us, aka knowing it was bullshit."
    mc "Well, I was not. Fuck."
    mf "So?"
    mc "Well, now we are getting along better. It's .. pleasant."
    mf "Sounds good to me. What is weird then?"
    mc "Dude, have you listened to anything I've said? I'm confused as fuck."

    mc "[sis_name] and I have gone from sworn enemies to like brother and sister in a couple of days."

    mc "Can you imagine that?"

    scene ep3_sc6_mcr_5
    mc "I'm having a good time with them."
    mc "I'm sharing moments and jokes with [sis_name] while flirting with [sf_name]."
    mc "I try to be a nice guy and at the same time... I'm constantly thinking about fucking them both like crazy."
    mf "Well, to fuck them you first have to get along with them so..."
    mf "I would say you made some good progress towards your goal."
    mc "Excuse me, I don't know why I told you that."
    mc "Obviously, you can't understand what I'm going through."
    mf "You're overthinking. I already told you it wasn't good for you."

    menu:
        "I don't think I am. [sisLovePath] [sfLovePath]":
            mf "You are. You always are. And that's why you're still a virgin."
            mc "You were a virgin to no so long ago."
            mf "And then I took the YOLO road."
            mf "If you don't try, you can't fail, but you can't succeed either."
            mc "I'll keep that in mind."
            $ ep3yoloroad = True
        "You may be right. [sisSubPath]":
            mf "Of course I am. I may be a moron, but I'm a wise one."
            mc "Wise.. isn't the term I would have used."
            mf "You know what I mean."
            mc "I'll keep that in mind."

    scene ep3_sc6_mcr_6
    mc "There's more."
    mf "Like what?"
    mc "Someone drugged [sis_name] in a club, Saturday."
    mc "Probably to rape her. [sf_name] managed to bring her back home safely."
    mf "Shit! Do you know who did this?"
    mc "Probably a guy she has just met at the club."
    mc "That creep also sent her flowers, the day after that."
    mc "And he casually found us today in a coffee shop."
    mf "That's some serious shit. What did you do?"

    if ep3facebroken == True:
        mc "I kicked his balls before knocking him to the floor with a punch."
        mf "Seriously?"
        mc "Yup. I still don't know where I've found the strength to do that."
        mc "Anger probably."
        mc "Anyway, I think I made myself clear that he should not approach [sis_name] and [sf_name] again."

    if ep3scaredluke == True:
        mc "I asked him to get the fuck out before I broke his face."
        mc "He left a bit afraid I think."
        mf "Good."
        mc "Yeah, I think I made myself clear that he should not approach [sis_name] and [sf_name] again."

    if ep3handshaked == True:
        mc "We talked a bit."
        mc "He seemed .. strangely nice... I don't know what to think anymore."
        mf "You think he may not be the one who did it?"
        mc "I don't know anymore."

    mf "You didn't go to the police?"
    mf "That's not something you're supposed to handle on your own."
    mc "No, we didn't go. [sis_name] didn't want to. She has her reasons."
    off "I can hear a feminine voice speaking over the phone."
    off "Someone is talking to him."
    mf "Dude, I'm sorry, I have to go."
    mf "I'll call you again soon."
    mf "In the meantime, don't overthink things too much."
    mf "The brain has very little to do with desire, love and all that shit."
    mc "You're telling me to go YOLO. Again."
    mf "More or less, yes."
    mf "Just don't burn the house, don't kill anybody and you should be fine."
    mc "Well... I'll try to restrain myself."
    mf "Great. Bye, [mc_name]!"
    mc "Bye, Steve."

    off "Don't burn the house, what kind of advice is that?"
    off "At least he's having fun."

    jump ep3sc9

label ep3sc7:
    scene black with dissolve
    with Pause(2)
    show text "In the afternoon."
    with Pause(2)
    scene ep3_sc8_living_0
    off "The girls leave the house early in the afternoon without saying a word."
    off "I guess it means I fucked up big time with that \"jerking off with [sis_name]'s panties\" event."
    off "I'm so lucky they didn't notice the video of them in the shower."
    off "I spend my time on the sofa looking at TV."
    off "I'm bored."
    if ep2kissedsf == True:
        off "I've also totally fucked my chances with [sf_name]."
        off "If I really had any."
        off "That kiss probably meant nothing to her."
    off "I wonder if I still have a chance to reconcile with [sis_name]."
    off "At least enough to get her to talk to me again."
    off "Maybe should I text her?"
    off "I'm going to text her."
    scene ep3_sc8_living_1
    off "What do I say?"

    menu:
        "I'm sorry, Princess.":
            $ ep3textscore += 1
            $ ep3replyone = "Really? I have a hard time believing you."
        "Hey, Princess. [assholePath]":
            $ ep3replyone = "You got some nerves, Perv."


    off "What next?"

    menu:
        "I didn't think that pantie thing would upset you so much. [assholePath]":
            $ ep3replytwo = "You don't even realize what you've done."
        "What I did was wrong, I know it.":

            $ ep3textscore += 1
            $ ep3replytwo = "At least you realize what you did."

    scene ep3_sc8_living_2
    off "So far so good. What next?"

    menu:
        "I don't know what's gotten into me...":
            mc "... It was like I couldn't control myself."
            $ ep3textscore += 1
            $ ep3replythree = "If you do something like that again, I kill you."
        "I won't do it again, I promise. [assholePath]":
            if ep3textscore > 1:
                $ ep3replythree = "I'm not sure I can trust you."
            else:
                $ ep3replythree = "You don't promise shit. You'll do it again as soon as I'll look elsewhere. I know it."


    off "Sounds nice, doesn't it? What next?"

    menu:
        "I really hope we can get along better. [assholePath]":

            $ ep3replyfour = "Why don't you go fap with your mom's underwear instead of mine, Perv?"
        "You're probably right, I'm a perv...":

            mc "... and I don't know if I can do anything about it. I may need help."
            $ ep3textscore += 1
            $ ep3replyfour = "I don't care you fap like crazy. Just don't steal more of my panties."

    scene ep3_sc8_living_1
    off "Ok. And finally..."

    menu:
        "I'm truly sorry.":
            $ ep3textscore += 1
            if ep3textscore > 3:
                $ ep3replyfive ="Everyone deserves a second chance I guess. Just stop fucking everything up."
            else:
                $ ep3replyfive ="You're sorry you've been caught. I can't see how I could forgive you."
        "Can we make peace? [assholePath]":
            if ep3textscore > 3:
                $ ep3replyfive ="I can't believe I'm forgiving you after what you've done. You don't deserve it. I hope you know how lucky you are."
            else:
                $ ep3replyfive ="You've stolen and soiled my panties, you damn pervert. How could we make peace after that?"




    off "Looks good. Let's send that message."

    if ep3textscore > 3:
        off "I have to wait at least 10 minutes for a reply from her."
        off "Maybe she's taking some time to think it carefully?"
    else:
        off "Her reply reaches me in less than 2 minutes."

    sis "[ep3replyone]"
    sis "[ep3replytwo]"
    sis "[ep3replythree]"
    sis "[ep3replyfour]"
    sis "[ep3replyfive]"

    if ep3textscore > 3:
        scene ep3_sc8_living_3
        $ ProcessStat(5, "sis_affection")
        $ DumpNotStack()
        off "Well, it definitely turned out better than I expected."
        off "I'll probably still have to prove myself, but at least that panties thing won't totally tear us apart."
        off "Let's go rub one out to celebrate."
        $ ep3sisforgive = True
    else:
        scene ep3_sc8_living_4
        off "Fuck you."
        off "That bitch deserves a lesson."
        off "I'm trying my best to be nice and she's nothing but a cunt to me."
        off "Just fall asleep on this sofa again, Princess."
        off "I'll show you who's the boss."
        $ ep3sishatred = True

label ep3sc8:
    scene black with dissolve
    with Pause(2)
    scene ep3_sc8_mcr_0
    off "I fapped like a madman."
    off "My balls are as empty as possible."
    off "I'm about to doze off when my phone buzzes."
    scene ep3_sc8_mcr_1
    off "Steve."
    off "It's a text message with a picture."
    scene ep3_sc8_mcr_2
    off "Holy shit."
    scene ep3_sc8_mcr_3
    off "Is that .. Steve.. getting a blowjob?"
    mf "She wanted me to send you this."
    mf "She is crazy!"
    off "That crazy fucker really got himself a girl."
    off "I can't believe they're doing it on the beach, anyone could have seen them."
    off "Let's call him."
    scene ep3_sc8_mcr_4
    mf "Hey, dude!"
    off "His breathing is loud."
    off "I can hear the moans of a girl."
    off "Are they at it right now?"
    mc "Hey, Steve. Am I bothering you?"
    mc "I can call you later if you want."
    mf "No, no, actually I was about to make a little clip for your enjoyment."
    mc "A little clip?"
    mf "Oh, baby, you're so tight!"
    mf "Yes, Jane like that kind of thing."
    mf "I guess you received the picture."
    mc "I did yes... Are you really .. fucking her as we speak?"
    mf "Oh yes. Holy shit, that pussy is unbelievable."
    mf "Yes, sure. Hey [mc_name], she wants to talk to you."
    scene ep3_sc8_mcr_5
    mc "What?"
    ja "Haaaan!"
    ja "Nice to meet you, [mc_name]."
    ja "Harder baby, harder!"
    ja "Did you like the picture, [mc_name]?"
    off "His voice is interspersed by moans."
    mc "Well.. yes ..."
    ja "Do you want more?"
    mc "I .. surely do yes..."
    ja "Will you jerk off to my picture?"
    ja "Deeper! Hit me deeper! Oh, Yeeeeeeeeeees!"
    mc "I don't know .. but I'm thinking about it right now."
    ja "Don't stop! don't stop!"
    ja "Right there, yes! Oh my Goooood! Haaaaan!"
    mf "I'm coming, baby! Holy shit! Haaan!"
    off "I can't believe what just happened."
    off "This is totally crazy."
    off "I can only hear loud breathings for almost a full minute."
    scene ep3_sc8_mcr_6
    mc "Guys? are you... alright?"
    mf "Yeah, sorry [mc_name]. It was a bit intense."
    mc "No shit."
    mf "So, how are you?"
    mc "Well .. fine I guess."
    mc "You seem to be having .. a lot of fun."
    mf "You have no idea."
    mf "We're fucking like animals, anywhere, anyplace."
    mf "Last night we did it right under her dad's window."
    mf "She didn't even try to lower her voice."
    mc "Are you kidding me?"
    mf "I've never been harder."
    mf "She makes me discover things I would never have thought I would like."
    off "I can hear her talking to Steve."
    off "I don't understand what she's saying."
    mf "Dude, I have to go. I'll call you later!"
    off "He hangs up immediately."
    off "I think I'm going to fap one more time."


label ep3sc9:
    scene black with dissolve
    with Pause(2)
    show text "Later."
    with Pause(2)

    if ep3caughtfapping == True:
        scene ep3_sc9_living_0
    else:
        scene ep3_sc7_living_0

    off "After half a pizza, I've set myself on the sofa and watched a couple TV shows and a wildlife documentary."
    off "Turns out squirrels have no problem boning their relatives."
    off "The night has come. I wonder what the girls are doing."






    if ep2cameraset == True or ( ep2sissleepingmovie == True and ep3handshaked == True ):
        pass
    else:
        call ep3sc9_breakpoint_1 from _call_ep3sc9_breakpoint_1

    off "It's almost 11 pm."
    off "I'm about to go to my room to play some games when I hear the car on the driveway."
    off "The girls are back."

    jump ep3sc10


label ep3sc9_breakpoint_1:
    off "My phone buzzes."
    scene ep3_sc7_living_1
    off "It's a text message."
    off "I don't know this number."
    uk "Hello, [mc_name]."
    mc "Hello. Who are you?"
    uk "This is Kelly."
    mc "Hello, Kelly. Do I know you?"
    kf "You don't know me, but I do know you, somehow."
    scene ep3_sc7_living_2
    off "How did she get my number?"
    kf "We were in the same school but we didn't have any class in common."
    kf "I've noticed you anyway."
    mc "You've noticed me?"
    kf "I'm at a party right now, and I'm a little drunk."
    kf "I wouldn't have found the courage to text you without that."
    kf "I hope it doesn't sound creepy but... I had a crush on you for years."
    off "Is she serious?"
    off "Who is this girl?"
    off "This must be a joke."
    mc "Seriously?"
    kf "I was afraid you would reject me so I haven't told you anything."
    kf "A friend convinced me to try my luck tonight."
    kf "She said that high school was over and that it was probably my last and only chance to talk to you, that I didn't have anything to lose anyway."
    kf "So here I am."
    scene ep3_sc7_living_3
    off "Holy shit."
    off "I waited for something like this during all of my time at high school."
    off "Why does it have to happen now?"
    mc "You should have told me sooner!"
    mc "How can you know I would have rejected you?"
    kf "I'm not very pretty and I wasn't the kind of girl you were looking at."
    kf "Give me a moment, I'll have my friend take a picture of me."
    off "Fuck, is my life getting even more complicated than it already is?"
    kf "Here it is. I hope you're not too disgusted."
    scene ep3_sc7_living_4
    off "Holy shit, she's cute as fuck."
    mc "Are you kidding me?"
    mc "You're beautiful!"
    kf "You really think so?"
    kf "I was afraid you would find me ugly or something."
    mc "You're definitely not ugly."
    kf "Thank you."
    kf "So... Do you want to meet?"
    kf "So we can talk and .. maybe get to know each other better?"
    off "What do I do? What do I say?"
    scene ep3_sc7_living_5
    if ep3sfdomrelationship == True:
        off "Even if no one knows about it I'm supposed to be [sf_name]'s boyfriend..."
        off "Even if I haven't kissed her yet..."
        off "Wait, could it be a trap?"
    elif ep3sfshoptalk == True and ep3sfshopanger == False:
        off "Even if I'm not her boyfriend, there is something going on between [sf_name] and me."
        off "She hasn't really rejected me."
    else:
        off "If [sis_name] and [sf_name] know that I'm meeting a girl, will there be consequences?"
        off "It could be seen as treason of some kind, couldn't it?"

    menu:
        "I'm sorry Kelly. I have a girlfriend." if ep3sfdomrelationship == True or ( ep3sfshoptalk == True and ep3sfshopanger == False ):
            $ ep3kfgftold = True
            kf "Oh..."
            mc "I'm really sorry."
            mc "If you would have called me last week I would have met you gladly."
            kf "I understand."
            kf "That said, I've been longing for you for so long now that I think I wouldn't mind sharing you..."
            mc "Are you suggesting I cheat on my girlfriend?"
            kf "No! Yes, I don't know."
            kf "I mean .. we could still meet, maybe date, and then you will decide, or not, as you see fit."
            off "Holy shit."
            kf "I'm sorry, I'm drunk."
            menu:
                "I'm the one being sorry, Kelly.":
                    $ ep3kfgfrejected = True
                    mc "I can't do that to my girlfriend."
                    mc "You're beautiful, and you seem like a kind person."
                    mc "I'm sure you will find another guy and he will be lucky."
                    kf "I understand."
                    kf "Sorry to have bothered you."
                    kf "If you change your mind, you can call me."
                    mc "You haven't bothered me."
                    mc "Have a good night."
                    kf "Good night, [mc_name]."
                "Well... I guess it won't hurt anyone to just meet and talk. [kellyPath]":
                    $ ep3kfgfmeetaccepted = True
                    kf "It's just to know each other better."
                    mc "Why not then."
                    kf "Great! Maybe tomorrow?"
                    kf "I'm free the whole day."
                    mc "Sure..."
                    kf "I'll think of a place and text you tomorrow."
                    kf "If it's ok with you."
                    mc "It is. I'll wait for your message."
                    kf "See you tomorrow then!"
                    kf "Have a good night! xoxoxo"
                    mc "Have a good night."
        "Well, I'll be glad to meet you. [kellyPath]":
            $ ep3kfmeetaccepted = True
            kf "Great! Maybe tomorrow?"
            kf "I'm free the whole day."
            mc "Sure..."
            kf "I'll think of a place and text you tomorrow."
            kf "If it's ok with you."
            mc "It is. I'll wait for your message."
            kf "See you tomorrow then."
            kf "Have a good night! xoxoxo"
            mc "Have a good night."
        "I'm sorry Kelly, I'm not interested.":
            $ ep3kfrejected = True
            kf "Oh..."
            mc "You're beautiful, and you seem like a kind person."
            mc "I'm sure you will find another guy and he will be lucky."
            kf "I understand."
            kf "Sorry to have bothered you."
            kf "If you change your mind, you can call me."
            mc "You haven't bothered me."
            mc "Have a good night."
            kf "Good night, [mc_name]."

    scene ep3_sc7_living_6

    if ep3kfgfmeetaccepted == True or ep3kfmeetaccepted == True:
        off "Holy shit."
        off "I don't have a clue of what the fuck I've just done."
        off "I have the feeling that I've just dived headfirst into a pool of shit."
        off "She's so cute."
        off "She seems a bit shy."
        off "I like that."

    if ep3kfgfrejected == True or ep3kfrejected == True:
        off "Well, that was weird."
        off "I feel like I just avoided some kind of trap."
        off "She was cute tho."
        off "And she looked a bit shy."
        off "I liked that."

    return

label ep3sc10:
    scene black with dissolve
    with Pause(2)




    if ep2cameraset == True or ( ep2sissleepingmovie == True and ep3handshaked == True ):
        if ep2cameraset == True:
            scene ep3_sc10_ent_0
        else:
            scene ep3_sc10_ent_0_alt
        $ ep3sisluked = True
        off "I join them at the entrance."
        off "They are arguing."
        sis "You are not my mother."
        sis "It's my life and I do what I want with it."
        sf "You do what you want, yes, but it's my right and my duty to tell you when you're doing something stupid."
        sf "And you are!"
        if ep2cameraset == True:
            scene ep3_sc10_ent_1
        else:
            scene ep3_sc10_ent_1_alt
        mc "Hey girls, what's going on?"
        mc "Is there a problem?"
        sis "Nothing that concerns you."

        mc "You're my friend so... if it concerns you it concerns me."

        sis "It's a bit late to play that card, [mc_name]."
        mc "Morons are always late to the game, but they play it nonetheless."
        sf "[sis_name] is going to tell you why I'm upset."
        sf "Aren't you, [sis_name]?"
        if ep2cameraset == True:
            scene ep3_sc10_ent_2
        else:
            scene ep3_sc10_ent_2_alt
        sis "I'm going to bed. Goodnight."
        mc "... Good night..."
        if ep2cameraset == True:
            scene ep3_sc10_ent_3
        else:
            scene ep3_sc10_ent_3_alt
        mc "So... what happened?"
        mc "You seem angry at her."
        sf "I am."

        sf "[sis_name] has found herself a boyfriend today."

        sf "And you know who it is?"
        sf "The guy who drugged her at the club, of course."
        mc "What? Are you serious?"
        sf "I am."
        sf "I insisted we left the party when I saw her letting him explore her mouth with his disgusting tongue while groping her breasts."
        mc "Fuck, is she crazy?"
        sf "I tried to talk her out of it but it's useless."
        mc "I'll try."
        if ep2cameraset == True:
            scene ep3_sc10_ent_4
        else:
            scene ep3_sc10_ent_4_alt
        sf "You? [mc_name], be serious."
        sf "You are a moron and a pervert."
        sf "You're probably one of the reasons she turned to this guy."
        sf "Had she felt safer at home chances are none of this would have happened."
        mc "I did nothing!"
        sf "You did plenty, and you did it wrong."
        sf "I'm going to bed. Good night [mc_name]."
        mc "Good night [sf_name]..."
    else:
        scene ep3_sc10_ent_5
        off "I join them at the entrance."
        sf "I'm exhausted but I don't know if I'll be able to sleep."
        sf "I don't know what to think of what happened."
        sis "Me neither."
        sf "I'm not sure we can trust either of them."
        sf "It smells so fishy."
        scene ep3_sc10_ent_6
        mc "Hey, ladies. What's going on? Is there a problem?"
        sf "Hey, [mc_name]."
        sis "Hey."
        sf "There's no problem. The evening has just been, very weird."
        sis "There's a lot to tell."
        sis "Let's get comfy first."
        sis "We'll meet you in the living room in 5 minutes."
        mc "As you wish..."
        scene black with dissolve
        scene ep3_sc11_living_0
        sf "I don't know where to start."
        sis "The girl who invited us tonight, she's pretty much the person we owe all our problems from the last few years."
        sis "It was her who started spreading the rumours about us."
        sis "Needless to say, she has never invited us to her parties before today."
        sf "It was very weird."
        sf "When we arrived at her place she was nowhere to be seen and her friends received us very... coldly."
        sf "We were about to leave, less than 15 minutes after we got there when she finally showed herself."
        sis "I don't really know what I expected but certainly not what happened next."
        scene ep3_sc11_living_1
        sf "She apologized."
        sf "First for not having been there to welcome us, and then for... all she did to us."
        sf "That was very strange."
        sf "It was like a full confession."
        sis "She told us that she was indeed the one who spread the first rumours about us."
        sis "She said she was... sorry about it."
        sis "That she was driven by jealousy."
        sis "She also said that she had spread several other rumours over the years but most of the time it wasn't her doing, the stories just kept coming by themselves."
        scene ep3_sc11_living_2
        mc "Wait."
        mc "After 3 years, that girl suddenly has remorse, invites you to her party and apologizes?"
        mc "It's way too easy."
        mc "I hope you sent her sucking dicks in hell."
        sf "Actually, we didn't..."
        sis "She told us that she was seeing a therapist and that apologizing was a part of it."
        sis "She said that she understood that forgiving her was very hard, or even impossible, but that her remorse was real."
        sf "She almost got to her knees to ask for our forgiveness..."
        sf "It was painful."
        sf "All her friends were looking at her like she was crazy."
        sf "Obviously, they didn't have a clue what was going on."
        sis "She then gave .. a speech to everyone, explaining the same thing to the assembly."
        sis "It must have been so humiliating for her..."
        scene ep3_sc11_living_0

        menu:
            "I don't understand. [sisLovePath] [sfLovePath]":
                mc "The way you talk about it.. it sounds like you forgave her."
                sis "Well, it's not like it gonna change anything."
                sis "We already have a shitty reputation, and obviously, there's no way we can be friends."
                sis "I would not say that we forgave her, but at least we agreed to talk to her."
            "You forgave her? For real? Are you crazy?":
                scene ep3_sc11_living_2
                $ ProcessStat(-1, "sis_affection")
                $ ProcessStat(-1, "sf_affection")
                $ DumpNotStack()
                sis "I've also forgiven you somehow, if I'm not mistaken."
                sis "Are you criticizing my gentleness?"
                mc "Come on, it's not the same thing, I haven't told the entire school you were sucking dicks in the restroom."
                sis "No, you didn't, you were the one who believed it."
                mc "And I apologized for that!"
                sis "And I forgave you for that, do you see where we're going?"
                mc "Ok, I get it. I'm sorry. Please continue."

        scene ep3_sc11_living_1
        sf "After that, the evening has been pretty weird."
        sf "She came back to us regularly to repeat her apologies."
        sf "In the meantime, everyone was avoiding us while still looking at us."
        sis "And then, they arrived."
        mc "Who arrived?"
        sf "Luke and his brother, Ray."

        if ep3facebroken == True or ep3scaredluke == True:
            scene ep3_sc11_living_3
            mc "The motherfucker."
            mc "Our talk this afternoon wasn't enough for him?"
            mc "I'm going to find him and break his fucking legs."
            mc "Did they try anything?"
            mc "Did they touch you?"
            mc "I'm going to kill them."
            sf "Calm down, [mc_name]. You don't need to get all fired up like that."
            scene ep3_sc11_living_0
            sis "They tried to talk to us again."
            sis "We told them we weren't interested."
            sis "They insisted and that's when our host came to our rescue."
            sis "We explained the situation and she was a bit surprised."
            sis "She told us that she has known Luke and his brother for years now and that he wasn't that kind of guy, or at least she didn't think so."
            sis "Nonetheless, she asked them to leave us alone, and they did."

            if ep3facebroken == True:
                sf "You should have seen Luke. His face was covered by a bruise."

            sis "I think you made a .. great impression on him."
            mc "That hasn't prevented him from coming back to you still."
            sf "No, but he wasn't so confident this time."

        if ep3handshaked == True:
            scene ep3_sc11_living_4
            mc "Oh... What happened? Did they do anything?"
            sis "They came and spoke to us directly and tried to flirt."
            sis "We told them to fuck off but they insisted."
            sis "That's when our host came to our rescue."
            sis "We explained the situation and she was a bit surprised."
            sis "She told us that she has known Luke and his brother for years now and that he wasn't that kind of guy, or at least she didn't think so."
            sis "Nonetheless, she asked them to leave us alone, and they did."
            sf "And she did it way more firmly than you this afternoon."
            menu:
                "Ok, next time I see him I'll punch first and talk later.":
                    scene ep3_sc11_living_5
                    $ ep3cowardsarcasm = True
                    $ ProcessStat(-3, "sf_affection")
                    $ ProcessStat(-3, "sf_dominance")
                    $ DumpNotStack()
                    sf "You didn't even talk this afternoon."

                    sf "You barely avoided to give him your benediction to rape your friend."

                    sf "And I'm pretty sure you wouldn't be able to punch anything."
                    mc "Violence is not my thing ok?"
                    if ep2brutalbreakfast == True:
                        sf "You weren't that much of a pacifist yesterday morning."

                    sf "I bet seeing him bigger and taller than you helped you finding your inner Gandhi."
                    mc "Are you calling me a coward?"
                    sf "Yes, I am."
                    if ep2brutalbreakfast == True:
                        sf "And being a coward is alright if you can at least be honest about it."
                        sf "You are a coward and a liar."
                    sis "Ok guys, that's enough."
                    sis "Let's move forward please."
                "I'm sorry about that. [sisLovePath] [sfLovePath]":
                    scene ep3_sc11_living_6
                    $ ep3cowardsorry = True
                    $ ProcessStat(1, "sf_affection")
                    $ ProcessStat(1, "sis_affection")
                    $ DumpNotStack()
                    mc "When he was stood in front of me, I suddenly thought that we may be wrong about him."
                    mc "The idea of hurting someone who may be innocent totally dissipated my anger."
                    mc "I'm not proud of it."
                    sf "It's ok."
                    sf "Besides, punching someone is not that easy."
                    sf "It takes a lot to hurt someone."
                    mc "I'm sorry anyway, I kind of failed you..."
                    sis "Nobody's perfect."
                    sis "Let's move forward, [mc_name]."

        scene ep3_sc11_living_0
        sis "Fifteen minutes later we were leaving the party."
        sis "We were still discussing the sincerity of hour host when you found us at the entrance."
        sf "Even now, I don't know what to think about it."
        mc "If I can give you my point of view, I think you should be careful."
        mc "That therapy excuse is a bit easy."
        sis "You don't need to tell us."
        sis "We don't plan on trusting her so easily."
        scene ep3_sc11_living_1
        sf "We don't plan to trust her at all."
        sf "But still, it was very confusing."
        sf "When she told the two guys to stay away from us, I appreciated her help."
        scene ep3_sc11_living_7
        sis "Anyway, we'll probably think and talk about it more in the days to come."
        sis "For now, I'm tired and I'm going to crawl to my bed."
        sis "If you'll excuse me, I wish you a good night."
        sf "I need some sleep too. Good night, [mc_name]."
        mc "Good night ladies."

    scene black with dissolve

label ep3sc11:
    scene black with dissolve
    with Pause(2)
    show text "Later that night."
    with Pause(2)

    scene ep3_sc12_mcr_0
    off "I can't sleep."

    if ep3caughtfapping == True:
        off "I can't stop thinking about what [sf_name] told me."
        off "[sis_name] got herself a boyfriend, and it's the guy who tried to rape her."
        off "That's crazy."
        off "How can she be that dumb?"
        off "Maybe I should call mom and let her know everything that happened."
        off "That would serve her right."
    else:
        off "I can't stop thinking about what happened today."
        off "Every time I close my eyes I see the lingerie store or the coffee shop."
        off "I imagine things I should have said or done to get a different outcome."

    scene ep3_sc12_mcr_1
    off "There is some light coming from the pool."
    off "Is someone taking a midnight swim?"
    off "It's [sf_name]."
    off "I could go check if she needs anything."
    off "That could be a good occasion to talk..."
    off "Who knows?"

    scene black with dissolve

    scene ep3_sc12_pool_0
    $ UnlockThat("ep3/ep3_sc12_pool_0")
    off "One minute later I'm joining her by the pool."
    mc "Hey, [sf_name]."
    off "She looks surprised."
    scene ep3_sc12_pool_1
    $ UnlockThat("ep3/ep3_sc12_pool_1")
    sf "[mc_name]!"
    off "She's naked!"
    off "Holy shit."
    if ep3caughtfapping == True:
        off "How lucky am I?"
        off "Can it get better than that?"

    sf "I'm sorry, I'm naked."
    sf "I was alone so I thought it was ok."
    sf "Could you..."

    menu:
        "Don't worry about that.":
            scene ep3_sc12_pool_3
            $ ep3pooldickmove = True
            $ ProcessStat(-5, "sf_affection")
            $ ProcessStat(-5, "sis_affection")
            $ DumpNotStack()
            off "I get rid of my boxers in one move."
            off "Tonight is my lucky night, I can feel it."
            off "I'm going to fuck her in the pool, Steve won't believe it when I'll tell him."
            sf "Oh my God, [mc_name]!"
            mc "The two of us are naked now, you don't need to be embarrassed anymore."
            sf "You cannot be serious."
            mc "What's the problem?"
            sf "Come on [mc_name]."
            sf "I had hoped you would leave, or at least turn around whilst I get out of the pool and put my clothes back on."
            sf "Aren't you ... ashamed?"
            scene ep3_sc12_pool_4
            $ UnlockThat("ep3/ep3_sc12_pool_4")
            off "She acts offended but she sure looks at my cock a lot."
            mc "Ashamed of what?"
            sf "You're definitely not a gentleman."
            mc "Come on, [sf_name]."
            mc "It's just a dick."
            mc "I'm sure you've already seen a lot."
            sf "I beg your pardon?"
            mc "I'm talking about porn."
            mc "You're not going to tell me that you've never watched porn?"
            sf "I've... seen some, but it's not something I'm actively searching for."
            mc "So, this is my dick."
            mc "There's nothing to be ashamed or afraid of."
            mc "Do you want to touch it?"
            scene ep3_sc12_pool_5
            sf "What? No! I don't want to touch it!"
            sf "I don't even want to see it, [mc_name]!"
            mc "Then don't look at it!"
            mc "It's that easy!"
            sf "I can't believe it."
            mc "I'm coming in."
            sf "No please! Don't come near me!"
            mc "Come on, you can't be that shy."
            sf "You really are an asshole."
            off "Fuck, did I misread the situation?"
            off "Maybe I took the joke a bit to far."
            mc "Sorry, I didn't want to offend you or anything."
            scene ep3_sc12_pool_6
            sis "WHAT THE FUCK ARE YOU DOING?"
            off "Shit."
            off "She seems .. angry."
            scene ep3_sc12_pool_7
            $ UnlockThat("ep3/ep3_sc12_pool_7")
            sis "Get the fuck out of here [mc_name]."
            sis "I can't believe you're that stupid."
            mc "Honestly, I didn't mean to.."
            sis "I don't fucking care!"
            mc "Ok, ok, I'm sorry."
            mc "It wasn't ill-intended. I promise. Good night."
            sis "Fucking pervert."
            off "I grab my shorts and go back into the house."
            off "Fuck."
            off "I did nothing wrong and I get yelled at like I'm a child."
            off "Don't get naked in my pool if you don't want to turn me on, bitch."
        "Turn yourself. [sfLovePath] [sfDomPath]":
            scene ep3_sc12_pool_8
            $ ProcessStat(3, "sf_affection")
            $ ProcessStat(3, "sf_dominance")
            $ DumpNotStack()
            mc "I'm the one who should be sorry, [sf_name]."
            mc "I hadn't noticed you were naked until you turned around."
            mc "I'm sorry."
            mc "I just wanted to check if you needed anything."
            mc "I'll leave you alone."
            mc "Goodnight [sf_name]."

            if sf_affection > 25 and (( ep2kissedsf == True or ep3sfshoptalk== True ) and ep3sfshopanger == False and ep3handshaked == False ):
                scene ep3_sc12_pool_8_love
                sf "Wait, [mc_name], please."
                mc "[sf_name]?"
                sf "Could you... wait for me in the living room?"
                sf "I want to .. talk to you."
                sf "I'm getting out of the pool and I'll join you."
                mc "I'll wait for you there."
                sf "Thank you, [mc_name]."
                off "I would have preferred having that talk in the pool with you but the living room will do fine I guess."

                scene black with dissolve
                call ep3sc12 from _call_ep3sc12

            elif ep3sfdomrelationship == True:
                scene ep3_sc12_pool_8_dom
                sf "Wait."
                mc "Yes?"
                sf "Where do you think you're going?"
                mc "Back to my bedroom..."
                sf "Wait for me in the living room."
                sf "I'm getting out of the pool and I'll meet you there in a minute."
                sf "We need to have a discussion."
                mc "Ok..."
                mc "Are things getting interesting, finally?"
                mc "It's damn time!"
                scene black with dissolve
                call ep3sc13 from _call_ep3sc13
            else:
                sf "Thank you, [mc_name]. Goodnight."
                $ ep3leftpool = True


    scene black with dissolve
    jump ep3sc14


label ep3sc12:

    scene black with dissolve
    scene ep3_sc13_living_00
    off "I wonder what she wants to talk about."
    off "It's probably related to [sis_name]."
    off "[sf_name] seems to have some kind of .. obsession for [sis_name]'s well being."

    off "It's a bit like if the only thing that mattered for her was my childhood friend's happiness."

    scene ep3_sc13_living_01
    off "I get up from the sofa as she comes in the room."
    off "Shit. That body..."
    off "Try not to look at her, [mc_name], I can feel the embarrassing boner coming a long way."
    off "She seems nervous."
    sf "Sorry to make you wait."
    mc "It's nothing. What do you want to talk about?"
    sf "It's a bit embarrassing for me..."

    if ep3sfshoptalk == False:
        sf "It's about our kiss."
    else:
        sf "It's about the discussion we had at the lingerie shop this afternoon."

    mc "Have you thought about it some more?"
    sf "I have..."
    sf "[mc_name], I have to ask you."
    sf "You don't intend to play me, do you?"
    mc "What are you talking about?"
    sf "If you just want to fuck me, I'm not interested."
    mc "I'm not that kind of guy."
    mc "I have feelings for you."
    mc "I don't know how deep and how far these feelings are running and therefore I can't tell you that I love you."
    mc "I simply don't know."
    mc "But I like you, and I care for you."
    mc "More than I would care for a friend."
    mc "Of course, I'm also thinking about sex."
    mc "I think sex is part of a relationship."
    mc "And that's what I'm looking for: exploring a possible relationship."
    off "She silently looks at me in the eye for a few seconds."
    sf "I guess I can work with that..."
    $ ep3sflove = True
    label galleryScene5:
    scene ep3_sc13_living_02
    $ UnlockThat("ep3/ep3_sc13_living_02")
    off "She suddenly closes the distance between us and kisses me."
    off "That's so sudden that I don't know what to do."
    off "I keep my hand hanging in the air, wondering where I can put them."
    off "I can feel her hand and her breast pressing against my chest."
    off "Our lips stay locked for a long time before slowly opening."
    off "Our tongues meet and play with each other."
    scene ep3_sc13_living_03
    $ UnlockThat("ep3/ep3_sc13_living_03")
    off "I decide that I can touch her and put my hands on her hips and waist."
    off "A little voice inside of me is screaming that I'm almost touching her ass and that she's going to slap me for going too far but it's too late."
    off "My hands are on her."
    off "It feels unreal."
    off "Am I dreaming?"
    off "I don't know how much time we spend like that but it's not enough."
    off "Our lips separate but our bodies remain glued together."
    scene ep3_sc13_living_05
    if ep3sfsislovechat == True:
        mc "So... What happened to the \"stay away from each other\"?"
        sf "I thought that we could just try to keep it a secret..."
        sf "I know it's very egoistic."
        sf "I couldn't stop thinking about it since the coffee shop."
        sf "After what happened, I thought that you deserved better than my hesitations and .. let's be honest, I also wanted more."
        mc "I'm as glad as surprised."
        mc "Even if you didn't completely reject me this afternoon, I wasn't very optimistic."
    else:
        sf "We'll have to keep it a secret."
        sf "I don't want [sis_name] to know for now."
        sf "I'm afraid she doesn't like that idea..."
        mc "I won't say a word to anyone."

    sf "I hope I'm not giving you the impression that I'm toying with you."
    sf "This kind of relationship is new to me."
    sf "I'm just a bit lost and... I'm not sure I'm handling it well."
    mc "It's new for me as well."

    if ep2virginlie == True:
        scene ep3_sc13_living_06
        sf "Really? But last night, you said that.."
        menu:
            "I lied. [sfLovePath]":
                $ ProcessStat(2, "sf_affection")
                $ DumpNotStack()
                mc "I'm sorry."
                mc "I was .. ashamed to be a virgin."
                mc "I know it's stupid."
                mc "I understood it right after [sis_name] and you answered the same question."
                mc "I'm as inexperienced as you are."
                scene ep3_sc13_living_07
                sf "Well... I have to say that I prefer it that way..."
            "I mean... I'm not.. very experienced...":
                $ ep3sfangrylove = True
                $ ProcessStat(-3, "sf_affection")
                $ DumpNotStack()
                mc "I only did it one time... besides, being with you feels like the first time .. so .."
                scene ep3_sc13_living_08
                sf "Are you lying to me right now?"
                mc "Absolutely not."
                sf "You know you just could have told me the truth and it would have been alright."
                mc "I'm not lying."
                sf "You are, obviously."
                off "The mood seems to be gone."
                mc "Ok, I'm sorry, it's just that I was ashamed."
                scene ep3_sc13_living_09
                sf "Ashamed of what?"
                mc "Ashamed of being a virgin."
                sf "There's nothing shameful in being a virgin."
                sf "You really are an idiot sometimes."
                scene ep3_sc13_living_10
                sf "I'm going back to bed."
                off "I guess it means I fucked up."
                off "She leaves the room."
                off "Come on, it was just a little lie."
                off "Does it really matter?"
                return

    scene ep3_sc13_living_04
    $ UnlockThat("ep3/ep3_sc13_living_04")
    off "We kiss again."
    off "She seems so small and fragile in my arms."
    off "My first kiss was almost sensationless."
    off "I was so nervous that I couldn't really appreciate it."
    off "The second was a surprise, it was nice, but it can't compare to this one."
    off "It's like slowly discovering each other through exchanging warmth and saliva."
    off "I wonder if she feels the same."
    scene ep3_sc13_living_06
    sf "I'm sorry, I... can feel your thing..."
    mc "Oh..."
    off "I got hard without noticing it."
    off "My shorts fail to keep my erection under control."
    scene ep3_sc13_living_11
    sf "Oh, my God."
    mc "I'm sorry. I can't do much about it."
    scene ep3_sc13_living_12
    $ UnlockThat("ep3/ep3_sc13_living_12")
    off "I'm actually horny as fuck."
    off "No one should be able to blame me for that in this situation."
    off "I'm ready to lick every part of her skin and fuck her on this couch but I'm sure she prefers me to behave like a gentleman or something like that."
    off "She seems to like that word."

    if ep3sfsislovechat == False and sf_affection < 40:
        scene ep3_sc13_living_07
        sf "I guess it's ok."
        sf "I'm actually exhausted."
        sf "I'm going to sleep."
        sf "For good this time."
        scene ep3_sc13_living_10_alt
        sf "See you tomorrow [mc_name]."
        mc "Good night [sf_name]."
        off "She leaves the room while I can't stop thinking that I have a girlfriend."
        off "I finally have a girlfriend!"
        off "O virginity, your days are numbered!"
    else:
        $ ep3sfhandjob = True
        mc "I'm sorry, I can't really avoid touching you with it."
        sf "It's ok."
        scene ep3_sc13_living_11
        sf "It looks so... big, and hard..."
        sf "Is it painful?"
        mc "No, not for now but it can be if I stay like that for too long."
        sf "You mean, if you don't..."
        mc "Yes."
        scene ep3_sc13_living_06
        sf "[mc_name], I'm not ready to... give you more... I'm sorry."
        mc "Don't be sorry [sf_name], I hadn't any intention to ask you to go further."
        sf "Maybe I can still help you?"
        mc "You want to help me?"
        scene ep3_sc13_living_07
        sf "Don't get your hopes too high, I won't suck on it."
        sf "But I can use my hand."
        sf "If you want me to, of course."
        off "I can't believe it."
        off "Play it safely [mc_name]."
        off "Be a gentleman."
        mc "I appreciate the proposition."
        mc "But you don't have to do anything you don't want to."
        sf "I want to. I'm... a bit curious... Can I...?"
        mc "It's yours, as am I, if I may say."
        scene ep3_sc13_living_13
        $ UnlockThat("ep3/ep3_sc13_living_13")
        off "She slowly inserts her fingers in my shorts and takes a look at my package."
        off "She seems to be totally absorbed by what she's looking at."
        off "She pushes me on the sofa after having sent my shorts to my ankles."
        off "I must be dreaming."
        scene ep3_sc13_living_14
        $ UnlockThat("ep3/ep3_sc13_living_14")
        off "She slowly caress my dick."
        off "A single touch from her and I'm already about to come."
        off "We're both looking at her hand gently grabbing my cock."
        off "She begins stroking my penis."
        scene ep3_sc13_living_14_alt
        sf "Am I doing alright?"
        mc "You're doing perfect."
        scene ep3_sc13_living_14_alt_2
        sf "I can't believe I'm doing this. It's actually... exciting..."
        off "She doesn't even look at me."
        off "She focuses her whole attention on my dick."
        off "We're both breathing heavily."
        scene ep3_sc13_living_14
        off "I barely last more than a couple minutes."
        scene ep3_sc13_living_15
        $ UnlockThat("ep3/ep3_sc13_living_15")
        off "I let out a groan of pleasure while I ejaculate."
        sf "Oh my God! There's so much!"
        off "She's still slowly stroking my dick."
        off "I can feel my own cum on my stomach."
        scene ep3_sc13_living_16
        $ UnlockThat("ep3/ep3_sc13_living_16")
        sf "Is it over? Should I stop?"
        mc "It is, yes. You can let it go."
        sf "Was it.. nice?"
        mc "Honestly, I think I've never had so much pleasure doing it myself before."
        sf "That's.. flattering, I guess. I'm glad I could be of assistance."
        scene ep3_sc13_living_17
        $ UnlockThat("ep3/ep3_sc13_living_17")
        off "She gives me a little kiss before she gets up from the couch."
        scene ep3_sc13_living_18
        sf "I'm going to wash my hands. Have a good night, [mc_name]."
        mc "Have a good night, [sf_name]."
        off "I can feel my face smiling uncontrollably."
        off "I'm pretty sure I look like a moron."
        off "I'm not sure I care."
        off "She seems happy."
        scene ep3_sc13_living_19
        $ UnlockThat("ep3/ep3_sc13_living_19")
        off "I take some time alone on the sofa."
        off "That handjob completely emptied me."
        off "I need to wipe my cum from my stomach but I can't move an inch for now."
        off "I can't stop smiling."
        off "I can't believe what happened."
        off "She gave me a handjob!"
        off "Holy shit."
        off "I'm hard again just thinking about it."
        off "I have a girlfriend!"
        off "Steve won't believe me when I'll tell him."
        $ renpy.end_replay()
    return

label ep3sc13:
    scene ep3_sc13_living_00

    off "I wonder what she wants to talk about."
    off "It's probably related to [sis_name]."
    off "[sf_name] seems to have some kind of .. obsession for [sis_name]'s well being."


    off "It's a bit like if the only thing that mattered for her was my childhood friend's happiness."

    scene ep3_sc13_living_20
    off "I get up from the sofa as she comes in the room."

    off "Shit. That body..."
    off "Try not to look at her, [mc_name], I can feel the embarrassing boner coming a long way."
    sf "So tell me, [mc_name]."
    sf "How much of me did you see in the pool?"
    mc "Not much. I saw your silhouette, nothing more..."
    sf "Really? You wouldn't lie to me, would you?"
    mc "Of course not."
    sf "Good. That makes me happy."
    scene ep3_sc13_living_21
    $ UnlockThat("ep3/ep3_sc13_living_21")
    off "She sits in the armchair."
    sf "Now could you please take off your shorts and stand right there?"
    off "She shows me a spot right in front of her."
    off "Did I hear that right?"
    off "Is that my lucky night or something?"

    menu:
        "You want me to take off my shorts?":
            $ ep3domquestionone = True
            $ ProcessStat(-1, "sf_dominance")
            $ DumpNotStack()
            sf "Yes, and I want you to stand in front of me."
            sf "Am I not clear enough?"
            mc "You are, I'm just surprised."
            sf "What are you waiting for?"
            scene ep3_sc13_living_22
            $ UnlockThat("ep3/ep3_sc13_living_22")
            off "I quickly get rid of my shorts and stand right where she wants me to be."
            off "She looks at my cock with severity."
        "Sure. [sfDomPath]":
            $ ProcessStat(1, "sf_dominance")
            $ DumpNotStack()
            scene ep3_sc13_living_22
            $ UnlockThat("ep3/ep3_sc13_living_22")
            off "I quickly get rid of my shorts and stand right where she wants me to."
            off "She looks at my cock with severity."


    off "I have no idea what to expect."
    off "My erection is barely starting to kick in."
    off "She's a bit direct."
    off "Is she going to suck me?"
    off "That would be great."
    off "Holy shit, I'm getting a blowjob."
    scene ep3_sc13_living_23
    sf "It's a bit down, isn't it?"
    mc "Well..."
    sf "Make it hard."
    menu:
        "You want me to masturbate?" if ep3domquestionone == True:
            $ ep3domquestiontwo = True
            $ ProcessStat(-2, "sf_dominance")
            $ DumpNotStack()
            sf "Yes."
            sf "I don't understand."
            sf "Do you want to do this or not?"
            sf "Why do you always make me repeat myself?"
            mc "I'm sorry, I'm simply.. a bit surprised."
            scene ep3_sc13_living_24
            $ UnlockThat("ep3/ep3_sc13_living_24")
            off "I grab my dick and stroke it gently."
            off "Less than a minute later I am hard as a rock."
            scene ep3_sc13_living_25
            $ UnlockThat("ep3/ep3_sc13_living_25")
            off "She looked at my cock the whole time."
        "As you wish my lady. [sfDomPath]":
            $ ProcessStat(2, "sf_dominance")
            $ DumpNotStack()
            scene ep3_sc13_living_24
            $ UnlockThat("ep3/ep3_sc13_living_24")
            off "I grab my dick and stroke it gently."
            off "Less than a minute later I am hard as a rock."
            scene ep3_sc13_living_25
            $ UnlockThat("ep3/ep3_sc13_living_25")
            off "She looked at my cock the whole time."

    sf "Good."
    scene ep3_sc13_living_26
    $ UnlockThat("ep3/ep3_sc13_living_26")
    sf "Tell me, [mc_name], how do you feel about your day?"
    sf "Have you been a good boy?"
    off "A good boy? Am I a dog or something?"
    off "I'm not sure I like the way she's talking to me."
    off "It's way too patronizing."
    off "But hey, if I have to endure that kind of talk to get a blowjob, she can call me what she wants."
    mc "I think so, yes..."
    sf "Really? Move this table a bit and sit on the ground. Right there."
    off "What the hell is this game?"
    off "I'm not sure I like where this is going."
    off "This is definitely weird."
    off "I'm not so sure I'm about to get a blowjob anymore."
    scene ep3_sc13_living_27
    $ UnlockThat("ep3/ep3_sc13_living_27")
    off "She takes her time looking at my cock and starts caressing it with her toes."
    off "She grasps my dick with her toes and plays with it."
    scene ep3_sc13_living_28
    off "Holy shit! It's a footjob!"
    off "I'm getting a footjob!"
    off "This girl is unbelievable!"
    sf "You seem to like that, [mc_name]. Am I doing it well?"
    mc "Oh yes! I don't know if you're doing well or not but I sure like it a lot!"
    sf "Do you want me to continue?"
    mc "Yes! Please!"
    sf "I'm not very agile with my feet and this is my first time, I hope you'll pardon me for my... roughness..."
    mc "It's good! You're doing great!"
    sf "I'm glad you like it."
    scene ep3_sc13_living_29
    $ UnlockThat("ep3/ep3_sc13_living_29")
    sf "What about that?"
    off "She pushes my shaft against my belly and rubs it with her foot."
    off "Her sole strokes my whole shaft while her toes stimulate my glans."
    off "It's a mix of pleasure and pain."

    if ep3handshaked == True:
        $ ep3ballscrushed = True
        sf "I'm a bit disappointed by the way you behaved at the coffee shop."
        sf "I would have hoped for you to be more... manly in that kind of situation."
        sf "I like guys who are strong, brave."
        sf "After what I saw in the coffee shop, I really doubt you're a good fit for me."
        off "I don't even know what she's talking about."
        off "I'm focused on her foot and the things she's doing on my dick."
        scene ep3_sc13_living_30
        $ UnlockThat("ep3/ep3_sc13_living_30")
        off "I've never imagined that one could hold a cock so firmly with her toes."
        sf "Do you have something to say?"
        mc "I'm sorry! I'll do better! I promise!"
        sf "Really? Can I trust you?"
        mc "Yes! Yes, you can!"
        sf "You wouldn't lie to me, would you?"
        mc "No! I wouldn't lie!"
        off "I'm about to come."
        sf "I'm sorry, [mc_name], but I have the feeling that you need to be taught a lesson or else you won't be able to learn anything."
        scene ep3_sc13_living_31
        $ UnlockThat("ep3/ep3_sc13_living_31")
        off "She crushes my balls under her foot as I was about to ejaculate."
        off "A mixture of pain and pleasure submerges my body, radiating from my crotch."
        mc "It hurts!"
        scene ep3_sc13_living_32
        sf "Tell me, [mc_name]."

        sf "The next time [sis_name] needs your help, will you behave like a man? Or like a pussy?"

        mc "Like a man! "
        sf "Can I believe you?"
        sf "You failed us once. You'll fail us again."
        mc "I promise I won't!"

        if ep2virginlie == True:
            sf "I can't trust you, [mc_name]. You've already lied to me."
            sf "You never had sex with Sandy, [mc_name]."
            sf "You never had sex with anyone."
            sf "Am I right?"
            mc "Yes! Yes, you are right!"
            sf "Why did you lie?"
            mc "I was ashamed!"
            sf "Ashamed to be a virgin?"
            mc "Yes!"

        sf "You are pitiful."
        sf "Open your mouth."
        scene ep3_sc13_living_33
        $ UnlockThat("ep3/ep3_sc13_living_33")
        off "She lets go of my crotch and inserts her toes in my mouth."
        scene ep3_sc13_living_34
        $ UnlockThat("ep3/ep3_sc13_living_34")
        off "She touches herself."
        sf "I'm going to give you one more chance, [mc_name]. Do not waste it."
        off "Her big toe is playing with my tongue."
        sf "I hope you understand that this is your last chance."
        scene ep3_sc13_living_35
        off "She suddenly pushes me aside and gets up."
        sf "I'm going to sleep now. Good night [mc_name]."
        off "I grab my balls, hoping to ease the pain."
        off "She leaves the living room."
        off "I lay on the ground, holding my testicles."
        off "What the fuck was that?"
        off "Why did I let her do that to me?"
        off "Well... that wasn't so bad, actually."
        off "The footjob was damn nice."
        off "The balls crushing wasn't."
        if ep2virginlie == True:
            off "How did she know I lied about not being a virgin?"
    else:
        $ ep3goodboy = True
        if ep3facebroken == True:
            sf "I'm very pleased with the way you behaved at the coffee shop."
            sf "I don't condone violence but I have to confess that seeing you like this was ... exciting."
            sf "You looked so strong, so confident... I wet my panties a bit."
        if ep3scaredluke == True:
            sf "I'm very pleased with the way you behaved at the coffee shop."
            sf "You did well."
            sf "You looked so strong, so confident... That's the kind of thing I like to see in a man."

        scene ep3_sc13_living_30
        off "She manages to grab my dick with her toes and slowly strokes my shaft."
        sf "You were brave. And I think you deserve a reward."
        sf "What do you think, [mc_name]?"
        sf "Is this a reward fitting of your feats?"
        mc "Yes!"
        sf "You seem to enjoy that."
        mc "I enjoy it a lot!"
        sf "I'm glad you like it."
        sf "I was a bit afraid of hurting you as it's my first time doing that."
        off "I've never imagined that one could hold a cock so firmly with her toes."
        off "Her strokes progressively become more vigorous."
        scene ep3_sc13_living_36
        $ UnlockThat("ep3/ep3_sc13_living_36")
        off "I can't contain myself anymore."
        mc "Haaaaaannnn!"
        scene ep3_sc13_living_37
        $ UnlockThat("ep3/ep3_sc13_living_37")
        off "I ejaculate, mostly on myself, but a few drops manage to land on her foot."
        sf "I'm a bit disappointed, [mc_name]."
        sf "Did I give you permission to cum?"
        sf "Furthermore, to cum on me?"
        mc "I'm sorry, I couldn't control myself."
        sf "I can see that."
        sf "For this time, and this time only, I will forgive you for having this orgasm but you have to do something with the cum that is covering me."
        scene ep3_sc13_living_37_bis
        $ UnlockThat("ep3/ep3_sc13_living_37_bis")
        sf "Use your tongue."

        menu:
            "Do it. [sfDomPath]":
                $ ProcessStat(3, "sf_dominance")
                $ DumpNotStack()
                off "I don't know why, I don't even think of refusing her."
                off "I'm a bit disgusted by the idea of licking my own semen but hell, I'm going to lick [sf_name]'s body."


            "Propose alternative." if ep3domquestiontwo == True:
                $ ep3domquestionthree = True
                $ ProcessStat(-1, "sf_dominance")
                $ DumpNotStack()
                mc "I.. can also go search for wipes..."
                sf "No, you can't. Lick it."


        scene ep3_sc13_living_38
        $ UnlockThat("ep3/ep3_sc13_living_38")
        off "I change my position and grab her foot with my two hands."
        off "I try to hold it as gently as possible as I lick her skin."
        off "I surprise myself thinking that the taste of my cum is not that bad."
        off "And it's my own."
        off "Girls swallow that thing all the time."

        off "I finish licking her foot clean when she pushes me back and quickly gets up."
        off "I'm a bit surprised by this abrupt ending."

        if ep3facebroken == True and ep3domquestionone == False:
            $ ep3dompleased = True
            scene ep3_sc13_living_40
            $ UnlockThat("ep3/ep3_sc13_living_40")
            off "She stands in front of me, so close that her pussy is barely a few centimeters from my face."
            off "I can smell her."
            off "She smells delicious."
            off "I'm pretty sure she's doing this on purpose."
            sf "If you continue to behave like this, I may consider rewarding you more.. consistently."
            sf "Will you be the man I want you to be, [mc_name]?"
            mc "I will be! Yes!"
            sf "I like that answer."

        scene ep3_sc13_living_41
        $ UnlockThat("ep3/ep3_sc13_living_41")
        sf "Will you dream of me, [mc_name]?"
        mc "Without a doubt."
        sf "I'm glad to hear it."
        sf "I wish you a good night, [mc_name]."
        mc "Good night [sf_name]..."
        off "She leaves the room and I slowly begin to realize what happened."

        if ep3facebroken == True:
            off "[sf_name] gave me a footjob, I licked and swallowed my own semen on her skin and she finally let me smell her pussy."
        else:
            off "[sf_name] gave me a footjob and I licked and swallowed my own semen on her skin."

        off "This is crazy."
        off "Steve will never believe me."
        off "Actually, I'm not sure I want him to know all of that."
    $ renpy.end_replay()
    return

label ep3sc14:
    scene black with dissolve
    with Pause(2)
    show text "Later that night."
    with Pause(2)
    scene ep3_sc15_mcr_0
    off "I still can't sleep."
    off "My brain has gone totally wild after my encounter with [sf_name]."

    if ep3pooldickmove == True:
        off "[sis_name] totally ruined my move."
        off "Ok, I've may have misread the situation a bit."
        off "And [sf_name] probably wasn't about to suck my dick."
        off "But without [sis_name] I could have, at least, apologized and cleared the misunderstanding."
        off "That bitch yelled at me for no reason."

    if ep3ballscrushed == True:
        off "What the fuck was that?"
        off "She almost destroyed my balls."
        off "Fuck, I don't even know if I disliked it or not."
        off "Sure it was painful, but her foot on my dick felt... nice."
        off "That was so strange."
        off "God, my crotch is still burning, it's like the worst blue balls of my life."

    if ep3goodboy == True:
        off "I can't believe it. How could I do that?"
        off "I licked my own cum off her skin."
        off "The footjob was so fucking good."
        off "Fuck, I licked cum. That's sick."
        off "That was so fucking hot."
        off "I licked cum! Shit!"

    if ep3sfhandjob == True:
        off "That was simply unbelievable."
        off "She gave me a handjob!"
        off "This afternoon she was almost rejecting me and tonight, she made me come with her hand."
        off "Talk about a turnaround!"


    if ep3sisluked == True:
        $ ep3sisphonenight = True
        off "And [sis_name], that slut, she has let that son of a bitch slide his tongue down her throat."
        off "Next time it will be his dick, I'm sure."
        off "Why the fuck is she giving herself to that motherfucker?"
        off "He even touched her breasts. Fuck!"
        off "I have to do something or she'll let him fuck her pussy before the end of the week."
        off "I can picture it now."
        off "Why the fuck is my dick so hard right now?"
        off "I'm sure his cock is humongous."
        off "He's going to destroy her tight virgin pussy."
        off "He'll pound her so hard she won't be able to walk for a month."
        off "That bitch will like it of course."
        off "He'll make her scream and ask for more."
        off "He'll fill her to the brim."
        off "FUCK! I can't let that happen."
        scene ep3_sc15_mcr_1
        off "I'm horny as fuck."
        off "I need to jerk off or something."
        off "Now that I think about it, [sf_name] is sleeping in the master bedroom tonight."
        off "That means that [sis_name] is alone."
        off "I could go check if she's sleeping."
        off "If she is, I could find a way to relieve myself far more pleasantly than just jerking off."
        off "Yesterday, my dick felt just right in her mouth."
        scene ep3_sc15_c_0
        off "The hallway is dark, let's keep it that way."
        off "I can hear [sf_name] lightly snoring in her room."
        scene ep3_sc15_c_1
        $ UnlockThat("ep3/ep3_sc15_c_1")
        off "I reach [sis_name]'s bedroom only to hear her talking."
        off "I can't understand what she's saying but she's clearly talking to someone."
        off "She's probably on the phone."
        off "She's talking to him."
        off "That slut hasn't had enough, she's already planning to suck him dry."
        off "What the fuck is wrong with her?"
        off "The guy tried to rape her and she's now lusting for his dick?"
        off "I can't believe it!"
        scene ep3_sc15_c_2
        off "I go back to my room even more enraged than when I left it."
        off "I jerk off angrily, thinking about [sis_name] being fucked by a big cock."
        off "I need to find a solution."

    if ep2sisfingered == True and sis_submission > 15:
        call ep3sc15 from _call_ep3sc15

    if ep2sismoviehug == True and sis_affection > 20:
        call ep3sc16 from _call_ep3sc16



    jump ep3end

label ep3sc15:
    scene ep3_sc15_mcr_1
    off "I'm suddenly thinking about that leftover pizza slice from my tonight meal."
    off "I want to eat it."
    off "It's stupid, I'm not even hungry."
    off "But I'm thirsty."
    off "There should be some iced tea in the fridge."
    off "That would be nice."
    scene ep3_sc16_kitchen_00
    off "Less than a minute later, I'm entering the kitchen."
    off "[sis_name] is there."

    if ep3siswalkintouched == True:
        off "Seeing her like that, I can't help thinking about what happened in the fitting room this afternoon."
    else:
        off "Seeing her like that, I can't help thinking about what happened last night."


    off "Maybe it's time to try something."
    off "Careful, [mc_name]."
    off "Don't ruin things by being a moron."
    off "Be a man, be confident."
    label galleryScene6:
    scene ep3_sc16_kitchen_1
    mc "Hey."
    sis "Hey."
    mc "Can't sleep?"
    sis "Can't sleep."
    mc "Me neither."
    off "I'm about to reach the fridge when I realize what she's doing."
    scene ep3_sc16_kitchen_2
    off "Eating."
    off "My pizza."
    scene ep3_sc16_kitchen_3
    off "Drinking."
    off "My iced tea."
    scene ep3_sc16_kitchen_4
    $ UnlockThat("ep3/ep3_sc16_kitchen_4")
    mc "Wait, did you just eat my last slice of pizza?"
    sis "Oh. It was yours?"
    mc "Who else? Did you order a pizza this evening?"
    scene ep3_sc16_kitchen_5
    off "She stuffs the entire slice in her mouth."
    off "She tries to say something but her mouth is so full that she's incomprehensible."
    off "She provokes me."
    mc "Are you kidding me right now?"
    off "She swallows."
    sis "Well, sorry, I couldn't read your name on it."
    mc "And you also finished the iced tea?"
    sis "Well, I've found it in the fridge and I needed to drink something with that pizza slice."
    mc "Girl, you're looking for trouble."
    scene ep3_sc16_kitchen_6
    off "She puts the pizza box in the trashcan and wash her empty glass in the sink."
    sis "You left it in the fridge."
    sis "It was fair game for anybody to grab it."
    sis "And I was hungry."
    mc "I'm hungry too, and there's no more pizza."
    mc "What are you going to do about that?"
    scene ep3_sc16_kitchen_7
    sis "I don't have to do anything."
    mc "I disagree."
    mc "Do I have to punish you?"
    sis "Punish me?"

    if ep3handshaked == True:
        scene ep3_sc16_kitchen_8
        $ ep3sissubrejected = True
        $ ProcessStat(-3, "sis_submission")
        $ DumpNotStack()
        sis "Who the fuck do you think you are?"
        sis "You can't punish shit."
        sis "You're the one who should be punished."
        sis "You're a disgrace."
        sis "Did you see yourself at the coffee shop?"
        sis "You were almost ready to suck his dick."

        sis "Where did the \"overprotective friend\" go, I wonder?"

        sis "For a day I thought you had become a man... but you're still just a kid."
        off "Ok, our domination game seems to be over."
        off "This is just a good old dispute."
        mc "Hey, you weren't so cocky last night when my fingers were giving you pleasure."
        scene ep3_sc16_kitchen_9
        sis "You didn't give me anything."
        sis "If anything, it was disappointing and a mistake."
        mc "What?!"
        sis "You heard me."
        sis "Now, if you don't mind, I'm going back to bed."
        mc "I do mind!"
        scene ep3_sc16_kitchen_10
        sis "And I don't care. Goodnight, loser."
        scene ep3_sc16_kitchen_11
        off "She gets out of the room and leaves me alone as I struggle with anger and shame."
        off "That bitch! How dares she speak to me like that!"
        return

    sis "Who do you think you are?"
    mc "The guy who fingered your pussy last night."
    scene ep3_sc16_kitchen_12
    sis "Hey, lower your voice."
    sis "I don't want [sf_name] to hear about that."
    sis "That was a mistake, ok?"

    if ep3siswalkinsuccess == True:
        sis "I told you I was drunk."
    else:
        sis "I was drunk."

    scene ep3_sc16_kitchen_13
    $ UnlockThat("ep3/ep3_sc16_kitchen_13")
    $ ProcessStat(3, "sis_submission")
    $ DumpNotStack()
    if ep3siswalkintouched == True:
        mc "As you were drunk this afternoon, in the fitting room?"
    else:
        mc "Bullshit."

    mc "You wanted it then, and you want it now."
    sis "I don't want anything from you."

    sis "We're just friends, for god sake!"

    sis "And you won't be fingering me ever again, that I can promise you."
    mc "You will ask me for it. You will ask me for more."
    sis "You're crazy."

    menu:
        "You're thirsty for my cum. Admit it.":
            scene ep3_sc16_kitchen_15
            $ ProcessStat(-2, "sis_submission")
            $ ProcessStat(-2, "sis_affection")
            $ DumpNotStack()
            $ ep3sissubrejected2 = True
            mc "You want me to fuck you so hard it'll make you forget everything else."
            mc "You want me to make you my slut."
            mc "You want me to plunge my meat pole so deep inside you that I'll burn my mark on your ovaries."
            scene ep3_sc16_kitchen_16
            sis "That's disgusting."
            sis "What the fuck are you talking about?"
            sis "Do you want to hurt me or something?"
            sis "I'm not interested."
            scene ep3_sc16_kitchen_17
            sis "I don't know what the hell is going on in that twisted mind of yours but you can take it and stuff it up your ass."
            sis "You'll never plunge anything in me and you'll never burn anything on my ovaries."

            sis "I am just your friend, you damn pervert, and you disgust me."

            sis "Is that clear?"
            scene ep3_sc16_kitchen_18
            sis "No, you don't need to answer that, just get the fuck out of this kitchen and go back to the gutter you're taking your ideas from."
            mc "But..."
            sis "GET OUT"
            scene ep3_sc16_kitchen_19
            off "I leave the place faster than I would admit it."
            off "That was a fail."
            off "I don't understand what I did wrong."
            off "Was I too blunt?"
            $ renpy.end_replay()
            return

        "I bet you can't think of anything else. [sisSubPath]" if sis_submission > 20:

            $ ProcessStat(3, "sis_submission")
            $ DumpNotStack()
            mc "First, there was your hand on my cock."
            mc "You felt it twitching under your touch You could felt the pleasure you were giving me, and you liked that."
            mc "Then my fingers reached your pussy and I entered you."
            mc "You probably thought it was wrong, and you liked it."
            mc "You shivered as I massaged your clitoris."
            mc "You felt shame when you came, because of the pleasure you experienced."
            mc "And you felt shame later because you wanted more."
            sis "You're talking nonsense."
            sis "I barely remember a thing!"
    scene ep3_sc16_kitchen_14
    mc "You're lying."
    mc "You know what I did after you left me in the living room last night?"
    mc "I licked my fingers clean."
    mc "They were full of you."
    mc "It tasted delicious."
    mc "You tasted delicious."
    mc "I'm thinking about tasting you some more."
    mc "Do you want me to lick your pussy?"
    sis "What? No! You're crazy!"
    mc "You already said that."
    mc "And I know you want it."
    mc "I'm sure your sweet little pussy is already drenched by the idea of me licking it."
    mc "You're thinking about it."
    mc "You thought about it all day."
    scene ep3_sc16_kitchen_20
    if ep3siswalkintouched == True:
        mc "Even more after the fitting room."
        mc "You couldn't help yourself to fantasize about all the things I could have done to you if [sf_name] hadn't interrupted us."

    mc "Because it's what you want don't you?"
    mc "You want me to do things to you."
    sis "Don't even think about..."
    scene ep3_sc16_kitchen_21
    $ UnlockThat("ep3/ep3_sc16_kitchen_21")
    off "She tenses up and gasp as I touch her pussy."
    mc "Oh, my. It's so hot and wet down there."
    mc "Something is burning, for sure."
    mc "I gonna have to investigate further."
    sis "You're crazy! Listen, I..."
    scene ep3_sc16_kitchen_22
    $ UnlockThat("ep3/ep3_sc16_kitchen_22")
    mc "You keep saying that, but you know what is really crazy?"
    mc "You haven't asked me to let you go."
    mc "I'm caressing your pussy right now, and you don't push me away."
    scene ep3_sc16_kitchen_23
    $ UnlockThat("ep3/ep3_sc16_kitchen_23")
    off "I grab her and easily lift her in the air."
    off "She's as light as a feather."
    off "She seems fragile and vulnerable."
    sis "[mc_name]?!"
    sis "[mc_name], please!"
    scene ep3_sc16_kitchen_24
    off "My hands are about to grip on her panties when [sis_name] intercepts them."
    mc "She's not even looking at me but I can guess she's about to refuse to go further, for real."

    menu:
        "I'm going to lick your pussy.":
            $ ProcessStat(2, "sis_submission")
            $ DumpNotStack()
            mc "I'll grab your breasts, I'll touch you and you will like it."
            mc "I'll make you come so hard you will ask for more."
        "I know that I've hurt you. That I've betrayed you. [sisSubPath]" if sis_submission > 25:
            $ ProcessStat(3, "sis_submission")
            $ ProcessStat(3, "sis_affection")
            $ DumpNotStack()
            $ ep3subtrust = True
            mc "But I'm not the moron I was three days ago anymore."
            mc "Do you know what we're doing here, you and me?"
            mc "It's about desire and trust."
            mc "You can trust me now."
            mc "I'm the only one you can trust."
            mc "I'll satisfy your desire."
            mc "I'll never hurt you again."
            mc "I'll only do to you what you want me to, even if you don't admit it."
            mc "I'll take care of you."
            mc "I'll protect you."
            mc "You want this."
            mc "Trust me."
            mc "You can let go."

    scene ep3_sc16_kitchen_25
    sis "If you tell anyone, I'll kill you..."
    off "Her voice is nothing but a frail whisper."
    menu:
        "No one will know.":
            mc "I won't say anything, to anyone."
        "It will be our secret. [sisSubPath]" if ep3subtrust == True:
            $ ep3subsecret = True
            $ ProcessStat(1, "sis_submission")
            $ ProcessStat(1, "sis_affection")
            $ DumpNotStack()
            mc "We'll keep it together."

    off "She lets go of my hand and lies down on the counter."
    scene ep3_sc16_kitchen_26
    $ UnlockThat("ep3/ep3_sc16_kitchen_26")
    off "This is it."
    off "Holy shit."
    off "I take her panties off and move her to a more comfortable position."
    off "I can't believe that this worked."
    off "What do I do now?"
    off "I promised to make her come but I'm not sure I know how."
    off "If I don't deliver, I can say goodbye to future developments."
    off "Her naked pussy is right there and I'm going to lick it."
    off "I want to fuck her so hard that I can barely think."
    off "I have to restrain myself."
    off "I don't want to scare her."
    off "Lick her, [mc_name]."
    off "Make her come."
    off "And then let her go."
    scene ep3_sc16_kitchen_27
    $ UnlockThat("ep3/ep3_sc16_kitchen_27")
    off "My hands run down her legs and I fondle her tights a bit before focusing on her pussy."
    off "Her smell is intoxicating."
    off "I'm going to lick my first pussy."
    scene ep3_sc16_kitchen_28
    $ UnlockThat("ep3/ep3_sc16_kitchen_28")
    off "My tongue barely touches her and [sis_name] is already moaning."
    off "I have no idea what I'm doing."
    off "But I'm giving it my best shot."
    off "I lick every part of her pussy before finding a spot that she seems to like better."
    off "Her skin burns under my tongue."
    off "I can feel the heat coming out of her vagina."
    off "She's dripping wet."
    off "She tastes salty and sweet at the same time."
    off "I like it."
    scene ep3_sc16_kitchen_29
    $ UnlockThat("ep3/ep3_sc16_kitchen_29")
    off "My hands explore her body while my tongue penetrates her."
    off "I've already seen her breasts but never touched them."
    off "I grope them through her shirt."
    off "They feel unreal and perfect."
    off "I want to play with them more."
    off "I should have asked her to remove her clothes."
    off "My dick is hard as a rock."
    scene ep3_sc16_kitchen_30
    $ UnlockThat("ep3/ep3_sc16_kitchen_30")
    off "I have lost track of time when she arches herself and begins shaking."
    sis "Oh my God. Oh my God! Oh my God!"

    menu:
        "Stop here.":
            $ ProcessStat(1, "sis_submission")
            $ DumpNotStack()
            $ ep3sissoloorgasm = True
            scene ep3_sc16_kitchen_31
            $ UnlockThat("ep3/ep3_sc16_kitchen_31")
            off "I stand up and look at her."
            off "She curls up and hides her face in the crook of her arms."
            mc "Your pussy is first class."
            mc "You taste like heaven."
            sis "How could I accept that. I'm crazy."
            off "Her pussy is wide open and fully exposed."
            off "I just have to pull my shorts down and I can penetrate her."
            off "Fuck, I can't do that."
            off "I'm having a hard time controlling myself."
            off "I'd better get out before I fuck up bad."
            mc "You know where to find me when you'll want more."
            scene ep3_sc16_kitchen_31_bis
            off "I leave the room, leaving her resting on the counter."
            off "Tomorrow, I'm certain that she'll beg me to let her suck on my dick."
            off "I'm already savouring the moment."
            $ renpy.end_replay()
            return
        "Continue. [sisSubPath]" if ep3subsecret == True:
            $ ProcessStat(5, "sis_submission")
            $ ProcessStat(1, "sis_affection")
            $ DumpNotStack()
            $ ep3sisdoubleorgasm = True
            scene ep3_sc16_kitchen_32
            $ UnlockThat("ep3/ep3_sc16_kitchen_32")
            off "The lower part of my face is completely drenched in her fluids."
            off "It's obvious she just came from my cunnilingus but I don't stop."
            off "The show starts now."
            scene ep3_sc16_kitchen_33
            $ UnlockThat("ep3/ep3_sc16_kitchen_33")
            off "It takes a few more minutes to give her another orgasm."
            off "Stronger, longer, deeper."
            scene ep3_sc16_kitchen_34
            $ UnlockThat("ep3/ep3_sc16_kitchen_34")
            off "She grabs my head and forces it against her pussy."
            off "I'm eating it gladly."
            off "My dick is screaming that I should lift her and impale her on my shaft, but I find the strength to restrain myself."
            scene ep3_sc16_kitchen_35
            off "Her whole body twists under the wave of pleasure that overwhelms her."
            off "She loses control of her legs that frantically tremble."
            off "She lets out a moan so loud that there's no chance [sf_name] doesn't hear it."
            off "I don't care."

    scene ep3_sc16_kitchen_36
    mc "You taste like heaven, Princess."
    mc "I could eat you all night long."
    off "Her legs still shake uncontrollably."
    off "She stays on the counter for some time, trying to get a hold on her breath."
    scene ep3_sc16_kitchen_37
    $ UnlockThat("ep3/ep3_sc16_kitchen_37")
    off "She tries to stand up but falls to the ground."
    off "Her legs can't carry her anymore."
    off "She looks exhausted."
    scene ep3_sc16_kitchen_38
    $ UnlockThat("ep3/ep3_sc16_kitchen_38")
    off "I move to help her but she stops me."
    off "She looks away and grabs me by my hips before lowering my shorts."
    scene ep3_sc16_kitchen_39
    $ UnlockThat("ep3/ep3_sc16_kitchen_39")
    off "Holy shit."
    off "Shyly, she takes my dick in her hand and began stroking it."
    off "I haven't asked for anything and here she is, giving me a handjob."
    off "She stops after a minute."
    scene ep3_sc16_kitchen_40
    $ UnlockThat("ep3/ep3_sc16_kitchen_40")
    off "Oh my God."
    off "Her mouth is warm and moist, just like her pussy."
    off "I can sometimes feel her teeth on my shaft."
    off "She's doing great even if it's her first time sucking a dick."
    off "Well, it's also my first time receiving a blowjob so I don't have any point of comparison anyway. "
    off "She softly sucks on my cock while her tongue plays with my glans."
    scene ep3_sc16_kitchen_41
    off "It's driving me crazy."
    off "I can't hold more than a minute."
    off "I try my best to contain myself but there's nothing I can do."
    off "Her mouth is simply that good."

    menu:
        "Tell her. [sisLoveSubPath]":
            $ ep3perfectsub = True
            $ ProcessStat(3, "sis_submission")
            $ ProcessStat(1, "sis_affection")
            $ DumpNotStack()
            mc "I'm about to come."
            off "She's doesn't even flinch and keeps on sucking my dick."
            scene ep3_sc16_kitchen_43
            $ UnlockThat("ep3/ep3_sc16_kitchen_43")
            off "I unload my balls in her mouth and she takes every drop of it."
            mc "Haaaaaannnn!"
            off "I can guess she struggles a bit with it but she finally swallows it all."
            off "Holy shit."
            off "Everything got way better than I expected."
            scene ep3_sc16_kitchen_44
            $ UnlockThat("ep3/ep3_sc16_kitchen_44")
            sis "Can I go?"
            off "Did she really ask for my permission?"
            mc "Yes, you can go."
            mc "Goodnight, Princess."
            sis "Goodnight, [mc_name]."
            scene ep3_sc16_kitchen_45
            off "She grabs her panties and leaves the room."
            off "I'm dizzy."
            off "I should get to my room before I collapse or something like that."
            off "Calm down, [mc_name]."
            off "I have the feeling that the realization of what just happened is about to hit me like a truck."
        "Don't tell her. [sisSubPath]":
            $ ep3subdork = True
            $ ProcessStat(-1, "sis_submission")
            $ ProcessStat(-1, "sis_affection")
            $ DumpNotStack()
            scene ep3_sc16_kitchen_42
            $ UnlockThat("ep3/ep3_sc16_kitchen_42")
            off "I let out everything I have in her mouth."
            off "She seems surprised and chokes before quickly getting away from me."
            mc "Princess, you suck like a queen."
            scene ep3_sc16_kitchen_46
            off "I put my shorts back up and leave her washing her mouth at the sink."
            off "I'm dizzy."
            off "I should get to my room before I collapse or something like that."
            off "Calm down, [mc_name]."
            off "I have the feeling that the realization of what just happened is about to hit me like a truck."

    $ renpy.end_replay()

    return

label ep3sc16:
    off "Someone knocks on my door."
    scene ep3_sc15_mcr_1
    off "The sound is so faint that I'm wondering if it was real or if I dreamed it."
    mc "Come in?"
    sis "[mc_name]?"
    scene ep3_sc17_mcr_0
    off "She enters my room and close the door."
    mc "[sis_name]? What's the matter? Is everything alright?"
    scene ep3_sc17_mcr_1
    off "I quickly get up to welcome her."
    sis "Yeah, nothing to worry about."
    sis "Did I wake you up? I'm sorry."
    mc "No you haven't."
    mc "I can't sleep."
    mc "Can I help you?"
    mc "You can turn on the lights."
    sis "It's okay that way... It's easier."
    off "Easier?"
    sis "It's... you said I could have a hug.. anytime..."
    off "She's asking for a hug?"
    off "In the middle of the night."
    off "Is this a joke?"
    mc "I said that, yes. You want a hug?"
    sis "I do..."
    off "Ok... She's crazy."
    off "Or something is not alright as she says it is."
    off "Maybe she's a bit shocked by today's events."
    off "She got harassed by that asshole again."
    if ep3facebroken == True:
        off "And I knocked him down before her."
    off "And that strange party with their apologetic sworn enemy..."
    mc "I'll hug you anytime."
    scene ep3_sc17_mcr_2
    off "I take her into my arms."
    off "I can feel her relaxing against me and we stay like that for a while."
    mc "Are you sure everything is alright?"
    mc "You can talk to me."
    sis "It's nothing."
    sis "With everything that happened the last few days, the club, you, this afternoon, and so on..."
    sis "It's a lot to take in..."
    sis "I'm feeling... lost."
    sis "And I thought I could use some... affection."

    menu:
        "As I said, you can come to me, anytime you want. [sisLovePath]":
            $ ProcessStat(1, "sis_affection")
            $ DumpNotStack()
            mc "I told you that you don't have to be alone anymore."
            mc "I'm here for you."
            sis "It's... hard to believe."
            mc "I know. And it's my fault."
            mc "Honestly, I'm happy you've given me a second chance."
            mc "I feel like I don't deserve it."
        "You're the toughest girl I know.":
            mc "It's going to be alright."
            sis "I'm sorry, I shouldn't have come."
            mc "Don't be silly. You're always welcome."


    scene ep3_sc17_mcr_3
    off "We finally break free from each other."
    sis "I already feel better... Thank you."
    mc "Are you sure? If you ever need more, I'll be happy to provide."
    sis "I'll be alright."
    sis "I'm .. going back to my room."

    if sis_affection < 25:
        sis "Goodnight, [mc_name]"
        mc "Goodnight, [sis_name]"
        scene ep3_sc17_mcr_5
        off "She leaves my room."
        off "I can't help but think she wanted something more, something she hasn't dared to ask for."
        return

    off "She hesitates."
    off "There's a lot of uneasy silence between her sentences."
    off "She waits for something."
    off "No, she does not simply wait."
    off "She hopes something will happen."

    menu:
        "Are you sure you don't need anything?":
            $ ProcessStat(2, "sis_affection")
            $ DumpNotStack()
            sis "I.. I'm good, thank you."
            sis "Goodnight [mc_name]."
            mc "Goodnight [sis_name]."
            scene ep3_sc17_mcr_5
            off "She leaves my room."
            off "I can't help but think she wanted something more, something she hasn't dared to ask for."
            return
        "Wait... [sisLovePath]" if sis_affection > 30:
            $ ep3sisstayed = True
            $ ProcessStat(2, "sis_affection")
            $ DumpNotStack()
            mc "Do you want to .. stay with me tonight?"
            sis "Stay with you?"
            scene ep3_sc17_mcr_4
            off "Ok, maybe that was a bit too bold..."
            off "Think fast, [mc_name]."

    mc "I mean, sleep, with me, in the same bed."
    mc "Like when we were children."
    mc "When we watched some really scary movies .. you couldn't sleep after that and you would come to sleep with me..."
    mc "Do you remember?"
    sis "I do... We're grown-ups now, you know?"
    mc "Sorry, what was a silly idea, I thought that..."
    sis "Okay."
    sis "Okay?"
    sis "Okay."
    off "The silence that ensues is so long and so awkward that I feel and hear my blood pulsating in my veins."
    scene ep3_sc17_mcr_6
    off "We both lie on the bed."
    off "We stay silent, in the dark, for a while."
    mc "Can I ask you a question?"
    sis "Yes?"
    mc "I still don't understand why you didn't fight more."
    mc "Why haven't you tried harder to convince us everything was lies and rumors?"
    mc "I don't blame you for that."
    mc "I'm just feeling that I'm missing something."
    off "Her answer takes some time to come."
    sis "There was that time, we were a month into high school or so."
    sis "It was just after the first phone call from the headmaster."
    sis "Boys were annoying me non stop."
    sis "Asking me to do .. I guess you get it."
    mc "I do."
    sis "I asked you to wait for me at the end of school, so we could go back home together."
    sis "I hoped your presence would prevent boys from annoying me."
    sis "Do you remember what you replied to me that day?"
    mc "I don't even remember you asking that..."
    sis "I wrote it down in my diary but I don't need to read it to remember it clearly."
    off "She takes a deep breath."
    sis "You told me that of course, you would wait for me."
    sis "That you were going to wait for me right in front of the restroom, so you can pick me up once I'm done sucking all those dicks."
    mc "... What a moron. I'm so sorry, [sis_name]."

    sis "When the headmaster called, do you remember how your dad reacted?"

    mc "No, I don't."

    sis "He didn't actually give a shit about me sucking dicks in the restroom."

    sis "He was only worried that if it became known at the hospital, it may cost him his promotion."
    sis "I also remember him casually calling me a whore."
    mc "I'm so sorry."

    sis "Your Mom was more subtle."

    sis "She took me to a gynecologist."
    sis "So that he could put me on the pill."
    sis "I told her I had no need for it."
    sis "She responded that it was fine, that whatever I do it was better to be protected."
    sis "She hasn't said a word but she treated me like the slut the headmaster told her I was."
    mc "[sis_name]..."
    sis "All that happened in a couple days."

    mc "I'll talk to my parents when they come back."

    mc "They must know."
    sis "Why would they believe you?"
    sis "Actually, why do you believe [sf_name]?"
    sis "You apologized to me only because she told you that everything was bullshit."
    sis "You didn't believe me when I told you, but you believed her."
    sis "Why?"

    menu:
        "I don't know.":
            scene ep3_sc17_mcr_8
            mc "Maybe I wanted to."
            mc "Maybe I've always known it and I only needed a reason to take that step toward you."
            mc "I've talked with Steve this afternoon, and he was surprised that I actually believed everything was true."
            mc "He said that most of the people, like him, were thinking that it was a bit of truth and a lot of lies."
            mc "Like, you've probably sucked some dicks in the restroom, but there was no way you've sucked all the dicks in school."
            sis "I haven't even sucked one."
            mc "I know."
            sis "You're not making any sense."
            mc "I know."
            off "I'm searching for something more to say but nothing comes to my mind."
            off "Silence envelops us."
            off "I finally vanish into sleep."
            return
        "I can't be sure but... [sisLovePath]":

            $ ProcessStat(2, "sis_affection")
            $ DumpNotStack()
            mc "Maybe it's the circumstances."
            mc "She first told me about what happened at the club."
            mc "That made me angry, worried, afraid."
            mc "I think it made me remember that... I care about you."
            mc "Then we talked about the rumours."
            mc "She was... very convincing... and maybe I was more receptive."
            sis "You're saying that I needed to get almost raped to wake you up?"
            mc "It could have been anything, anything strong enough to make me remember that .. I .. love you..."
            off "Did I say that? Did I really say that?"
            off "The silence that follows is a little too long to be comfortable."


    off "Her breathing is loud."
    off "She's nervous."
    scene ep3_sc17_mcr_7_bis
    sis "Are you playing me?"
    off "There is no anger in her voice."
    off "It's a true and honest question."
    mc "No. I'm not playing you."
    sis "If you're toying with me, I will kill you. For real."
    mc "I'm not playing you."
    sis "You should think carefully before saying things like that."

    menu:
        "Things like what?":
            $ ProcessStat(-1, "sis_affection")
            $ DumpNotStack()
            sis "That you love me."
        "I didn't have to think about it [sisLovePath]":
            $ ProcessStat(1, "sis_affection")
            $ DumpNotStack()
            mc "It just felt obvious."
            mc "Like... It's just how it is."

    scene ep3_sc17_mcr_7
    $ UnlockThat("ep3/ep3_sc17_mcr_7")
    sis "You don't know what you're talking about."

    menu:
        "But you know better, do you?":
            mc "Are you perhaps some kind of expert of the human mind and heart?"
            sis "Maybe not, but at least I'm not carelessly saying I love anyone."

            mc "I can't tell my friend that I love her?"

            sis "Not like that. It's too sudden."
            mc "We just need some time to get used to it."
            sis "Maybe. But if it's a joke it doesn't amuse me."
            mc "It's not a joke."
            scene ep3_sc17_mcr_8
            sis "Great. I need some sleep now. Good night [mc_name]"
            mc "Good night [sis_name]."
            off "The conversation ends abruptly."
            off "I can't help but think that she wanted something else."
            off "Maybe I'm too dumb to understand her."
            return
        "I'm as confused as you are. [sisLovePath]":
            $ ProcessStat(3, "sis_affection")
            $ DumpNotStack()
            mc "I know I love you."
            mc "And I think I've always loved you, even if I kind of forgot about it."
            sis "Were you loving me while asking me how many dicks I sucked?"
            mc "It may seem stupid but I'm pretty sure that I was also angry at you because I loved you."
            sis "And now, you are clear about it."
            sis "You love me. Isn't that a bit easy?"
            mc "Maybe, but it doesn't make it any less real."
            sis "If it's a joke it doesn't amuse me."
            mc "It's not a joke."

    scene ep3_sc17_mcr_9
    $ UnlockThat("ep3/ep3_sc17_mcr_9")
    off "The silence floods the room."
    off "[sis_name] stays motionless for a moment while."
    scene ep3_sc17_mcr_10
    off "It's hard to read her expressions in that semi-darkness."
    off "She kisses me."
    scene ep3_sc17_mcr_11
    $ UnlockThat("ep3/ep3_sc17_mcr_11")
    off "A brief, rather innocent kiss on the corner of my mouth."
    off "Another one, a bit longer with our lips intertwined."
    scene ep3_sc17_mcr_12
    off "On the third one, her tongue comes searching for mine."
    off "My heart skips a beat."
    off "I can sense her fear and excitement."
    off "I feel the same."
    off "I don't know how long we stay like this."
    off "We breathe like a couple of beasts who just finished running a 100m."
    scene ep3_sc17_mcr_13
    sis "I'm sorry, I.. I don't understand what's happening."
    sis "I know it's wrong but I can't stop thinking about it."
    mc "You don't have to be sorry."
    sis "But I am!"
    sis "And I'm so confused."
    sis "I feel disgusted and excited at the same time."
    sis "And it's like I can't do anything but come back to you."
    off "She pauses whilst looking at me."
    sis "You don't seem as conflicted as I am."
    sis "Do you... want... this?"
    off "Her voice sounds afraid, weak and frail as if it's about to break."

    menu:
        "Seriously? [sisLovePath]":
            $ ProcessStat(5, "sis_affection")
            $ DumpNotStack()
            $ ep3sislove = True
            mc "I'm terrified."
            mc "I don't know what to do."
            mc "I couldn't stop thinking about it since last night."

            mc "I've just found that I still deeply care about you and I can't stop thinking that I want more from you."

            scene ep3_sc17_mcr_14
            sis "You want more."
            mc "I want more."
            sis "But we can't..."
            mc "I know. And I don't care. I want more."
            off "We look at each other in the semi-darkness without saying a word for a time."
            off "Did I go too far?"
            off "I don't want to frighten her."
            off "I try to find something reassuring to say, like, that I'm not a monster or that I'm not going to rape her or something like that."
            scene ep3_sc17_mcr_15
            $ UnlockThat("ep3/ep3_sc17_mcr_15")
            off "She finally makes the first move."
            off "Her hand on my shoulder and my neck feel unreal."
            off "She took a decision."
            scene ep3_sc17_mcr_19
            $ UnlockThat("ep3/ep3_sc17_mcr_19")
            off "That kiss is so different than the previous ones."
            off "It's full of resolve and confidence."

            off "We're not simply like brothers and sisters anymore."

            return
        "What's \"this\"?":
            $ ep3sisloverejected = True
            sis "You really want me to say it out loud?"
            mc "I don't want to risk any misunderstanding."
            off "She takes a deep breath."
            sis "You, and me... being .. in love."
            sis "Do you want it?"
            off "Love."
            off "Shit. This is serious."
            off "She doesn't want to just fool around with me."
            off "It's like a life sentence."
            off "With any other girl I could have just say yes and get by later."
            off "But this is [sis_name]."
            off "I can't just fuck her and abandon her."
            off "I have to reject her."
            off "Fuck. How do I get myself out of this?"
            off "Maybe not tell her that I just hoped I could fuck her without consequences."
            scene ep3_sc17_mcr_16
            mc "[sis_name], I have to be honest with you."
            mc "I don't know what I want."
            mc "I may not seem conflicted but I'm totally lost."
            mc "Kissing you is damn nice but I'm afraid to lose something else if we go this way."

            mc "I've just got you back and my feelings are a total mess."

            mc "I'm confused."
            mc "I don't know if what I feel is love, or guilt, or something else."
            mc "If it's love I'm not sure what kind of love, and I'm not even sure that I'm not just overreacting to my guilt and shame."
            mc "I can't stop thinking about you but I think we should... take time."
            mc "We shouldn't do anything we could regret as long as we are not completely sure we want to go down this path."
            sis "You're.. rejecting me."
            mc "No, I'm not."
            scene ep3_sc17_mcr_17
            sis "You are... and you're right, of course. You're right."
            sis "I'm sorry, I ... I 'll go back to my room."
            sis "I shouldn't have come, I'm so sorry."
            mc "[sis_name], wait."
            sis "Goodnight, [mc_name]."
            mc "[sis_name]."
            off "She leaves the room and closes the door behind her before I could make a move."
            scene ep3_sc17_mcr_18
            off "What a moron I am."
            off "Why do I keep fucking up everything?"



    return
label ep3end:



    jump day4start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
