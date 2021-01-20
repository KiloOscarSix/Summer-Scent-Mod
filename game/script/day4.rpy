

label day4start:


    if ep3sflove == True and ep3sfangrylove == False:
        $ sf_love_path = True

    if ep3sislove == True:
        $ sis_love_path = True

    if ep3sfdomrelationship == True:
        $ sf_dom_path = True

    if ep3sissoloorgasm == True or ep3sisdoubleorgasm == True:
        $ sis_sub_path = True
        if ep3perfectsub == True:
            $ sis_sub_love_path = True

    if ep3sisluked == True:
        $ sis_hate_path = True

    if sis_love_path == False and sf_love_path == False and sis_sub_path == False and sf_dom_path == False and sis_hate_path == False:
        $ full_neutral_path = True
    scene black with dissolve
    with Pause(2)
    show text "Day 4 - Tuesday" with dissolve
    with Pause(2)
    show text "The morning" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(2)

    if ep3sisstayed == True and ep3sisloverejected == False:
        jump ep4sc1
    else:
        jump ep4sc2


label ep4sc1:

    off "My bed feels unusually comfortable this morning."
    off "That pillow I'm holding against me is great."
    off "It's warm and soft. It smells nice too."
    off "It reminds me of something, I don't really know what."
    off "The pillow moved a bit, but I don't mind it."
    off "It's still a great pillow."
    off "Now that I think of it, were my pillows always that large?"
    off "It moved again."
    off "Did it just say my name?"
    scene ep4_sc1_mcr_01 with fade
    $ UnlockThat("ep4/ep4_sc1_mcr_01")
    sis "[mc_name]?"
    off "I slowly emerge from my slumbers."
    off "That was not a pillow."
    sis "Are you awake?"
    off "I suddenly remember what happened last night."
    off "I have a brief moment of panic thinking that we've done something wrong but I quickly relax."
    off "Holding her like that feels good and somehow more acceptable than it did yesterday."
    scene ep4_sc1_mcr_02
    $ UnlockThat("ep4/ep4_sc1_mcr_02")
    mc "I am yes."


    if ep3sislove == False:
        sis "You're squeezing my breast."
        sis "And I can feel your boner against my ass."
        $ ProcessStat(1, "sis_affection")
        $ DumpNotStack()
        off "Holy shit, she's going to kill me."
        scene ep4_sc1_mcr_04
        mc "I'm sorry!"
        mc "I guess I grabbed you while we were sleeping and..."
        sis "It's ok."
        sis "You're not responsible for what you're doing while you sleep."
        scene ep4_sc1_mcr_05
        $ UnlockThat("ep4/ep4_sc1_mcr_05")
        off "That's an unusually reasonable answer from her part."
        off "I should have squeezed it a bit more."
        off "She slowly gets up."
        sis "I'm going back to my room before [sf_name] wakes up."
        mc "Ok."
        sis "Thank you."
        scene ep4_sc1_mcr_06
        mc "I don't know what you're thanking me for but you're welcome."
        off "She awkwardly stands there for a few seconds before she gets out of the room and leaves me alone."
        scene ep4_sc1_mcr_07
        off "I lie back on my bed."
        off "That was a really strange night."
        off "But it was nice."




    if ep3sislove == True:
        sis "Having any second thoughts?"
        off "My left-hand holds one of her breasts and I have a raging boner pressed against her buttocks."
        off "She doesn't seem to mind."

        menu:
            "Kiss her spine":
                $ ProcessStat(1, "sis_affection")
                $ DumpNotStack()
                scene ep4_sc1_mcr_03
                $ UnlockThat("ep4/ep4_sc1_mcr_03")
                off "I kiss her back along her spine."
                off "I can sense her shivering in surprise under my lips."
                mc "None."
                mc "You?"
                sis "Neither."
                sis "I'm just ... I just have no idea where we're headed."
                sis "Probably nowhere good."
            "Hold her tighter":

                $ ProcessStat(1, "sis_affection")
                $ DumpNotStack()
                mc "None."
                mc "You?"
                sis "A bit."
                sis "You know that thing you're squeezing like crazy right now?"
                sis "It's one of my breasts."
                sis "It hurts."
                mc "Oh.. I'm sorry."
                sis "I'm not thinking about running away."
                sis "You can relax."
                sis "I'm just... I just have no idea where we're headed."
                sis "Probably nowhere good."


        scene ep4_sc1_mcr_02
        $ UnlockThat("ep4/ep4_sc1_mcr_02")
        menu:
            "I don't know where this is going either.":

                mc "But we're going together. [sisLovePath]"
                $ ProcessStat(1, "sis_affection")
                $ DumpNotStack()
            "Everything is going to be alright.":
                $ ep4unrealisticpromise = True
                $ ProcessStat(1, "sis_affection")
                $ DumpNotStack()

        off "She doesn't reply and the silence envelops us for a while."
        sis "You know we can't tell anyone about us."
        mc "I know."
        sis "I know you tell almost everything to Steve."
        sis "This, you can't."
        mc "I don't tell Steve everything."
        mc "And I won't talk about us with anyone."
        mc "You can't tell [sf_name] either."


        if ep3sflove == True or ep3sfdomrelationship == True:
            off "The instant I speak her name, I'm submerged by the memories of the moment I shared with her last night."


        sis "No, I won't."


        if ep3sflove == True or ep3sfdomrelationship == True:
            off "I'm knee-deep in shit."
            if ep3sflove == True:
                off "How will [sis_name] react if I tell her I'm supposed to be her best and only friend's boyfriend?"
            off "How do I get myself out of this mess?"

        sis "If anyone learns about us our lives are basically over."


        if ep3sflove == True and ep3sfangrylove == False:
            off "I have to tell [sis_name]."
            off "She's going to kill me."
            off "I should tell her."
            off "Fuck."
            off "I'm a complete jerk."
            off "I should have told her last night."


        if ep3sfdomrelationship == True:
            off "Calm down, [mc_name]."
            off "You're not even sure what your relationship with [sf_name] really is."
            off "I mean ... that was not classic lovey-dovey boyfriend and girlfriend stuff."
            off "I should keep it a secret until I find a solution."


        if ep3sfangrylove == True:
            off "Calm down, [mc_name]."
            off "Your story was dead on arrival."
            off "You don’t need to bother [sis_name] with that."

        off "What the fuck are we doing?"
        off "We’re crazy."
        off "Sooner or later, someone will know."
        off "It’s obvious."
        off "I know it."
        off "She probably knows it too."
        scene ep4_sc1_mcr_08
        sis "Are you listening to me?"

        menu:
            "I'm sorry, I zoned out a bit.":
                mc "But I was still listening."
                mc "We'll keep it a secret."
                mc "I'm not worried."
                mc "And if someone happens to find out .. well.. we'll just run away together."
                sis "You are awfully optimistic."
                mc "Some would have said romantic."
                sis "Or foolish."
                $ ep4runawaymention += 1
            "I love you. [sisLovePath]":

                $ ProcessStat(1, "sis_affection")
                $ DumpNotStack()
                mc "Whatever happens, I want you to know that I love you."
                sis "You... shouldn't... say that word so casually."
                sis "Let's be honest, we're not even sure of what we're truly feeling for each other."
                mc "You may be right."
                mc "But I still think it's love."

                sis "Says the horny one who rubbed his boner against his childhood friend's ass all night long."

                mc "Love can take many forms..."
                mc "And I'm sorry about that..."
                sis "Luckily for you... I don't mind."

        scene ep4_sc1_mcr_05
        $ UnlockThat("ep4/ep4_sc1_mcr_05")
        sis "I have to hurry back to my room before [sf_name] wakes up."
        sis "I hope it's not too late."
        sis "I have to go with her on a morning workout."

        scene ep4_sc1_mcr_06




        if ep3sflove == True and ep3sfangrylove == False:
            menu:
                "Tell her. [sisLovePath]":
                    $ ep4sismorningtold = True
                    mc "Wait."
                    mc "There is something we need to talk about."
                    sis "Can't it wait?"
                    mc "No, it can't."
                    scene ep4_sc1_mcr_09
                    mc "It's something important."
                    mc "I should have told you last night."
                    sis "Ok...?"
                    mc "Last night... before you came to me..."
                    mc "I was with [sf_name]."
                    $ ProcessStat(1, "sis_affection")
                    $ DumpNotStack()
                    off "She looks perfectly calm."
                    off "I wonder if I haven't been clear."
                    off "Maybe she didn't hear me."
                    off "After a few seconds, her expression finally changes."
                    scene ep4_sc1_mcr_11
                    sis "I know."
                    off "That's not the response I expected."
                    mc "You know?"
                    sis "I saw you."
                    mc "You saw us?"
                    scene ep4_sc1_mcr_12
                    $ UnlockThat("ep4/ep4_sc1_mcr_12")
                    sis "Yes I did, stop repeating what I say, it's annoying."
                    mc "I don't understand."
                    sis "I heard voices coming from the pool last night."
                    sis "I went down to check on it and I found you in the living room."
                    sis "You were kissing."
                    mc "Then you came to my room..."
                    scene ep4_sc1_mcr_11
                    sis "I thought that it was... my last chance to... you know..."
                    mc "I suppose I know... indeed."
                    sis "So ... what do we do know?"
                    scene ep4_sc1_mcr_13

                    menu:
                        "I have to tell her it's over. [sisLovePath]":
                            $ ep4mcwantitover = True
                            $ ProcessStat(1, "sis_affection")
                            $ DumpNotStack()
                            mc "But I have the feeling it won't go smoothly."
                            mc "And it'll be so awkward."
                            mc "I'm her boyfriend for an hour and the day after I tell her it's over."
                            mc "I'm not sure how to go about it."
                        "I don't know.":

                            $ ep4mcdontknow = True
                            mc "I don't know what to do."
                            scene ep4_sc1_mcr_14
                            sis "You could just not tell her and two-time us."
                            sis "Doesn't that sound nice?"
                            sis "With some time we could even arrange a threesome."
                            mc "You're being sarcastic."
                            sis "Of course I am."
                            scene ep4_sc1_mcr_13
                            sis "You have to choose, [mc_name]."
                            sis "I suggest you start thinking about it right now."

                    sis "Anyway, I don't have time for that."
                    sis "We'll talk about it when we return from the park."
                    sis "Until then, you are [sf_name]'s boyfriend."
                    mc "Are you sure about that?"
                    sis "I am."
                    off "I stop her one last time as she's about to open the door."
                    off "Wait."
                    sis "Again?"
                    off "I grab her as gently as I can."
                    off "I still feel a bit uneasy touching her."
                    off "I'm afraid she'll finally push me away and slap me in the face."
                    scene ep4_sc1_mcr_10
                    $ UnlockThat("ep4/ep4_sc1_mcr_10")
                    off "She hugs me back as our lips join."
                    off "Our tongues play with each other as we exchange saliva."
                    off "She wanted this as much as me."
                    mc "You know I choose you, don't you?"
                    $ ProcessStat(1, "sis_affection")
                    $ DumpNotStack()
                    sis "I know."
                    sis "I have to go."
                    sis "She's going to wake up any moment now."
                    off "She exits the room and leaves me alone."
                    scene ep4_sc1_mcr_07
                    off "I lie back on my bed."
                    off "All of this is fucking crazy."
                "Don't tell her":

                    off "I stop her as she's about to open the door."
                    scene ep4_sc1_mcr_09
                    mc "Wait."
                    sis "Yes?"
                    off "I grab her as gently as I can."
                    off "I still feel a bit uneasy touching her."
                    off "I'm afraid she'll finally push me away and slap me in the face."
                    scene ep4_sc1_mcr_10
                    $ UnlockThat("ep4/ep4_sc1_mcr_10")
                    off "She hugs me back as our lips join."
                    off "Our tongues play with each other as we exchange saliva."
                    off "She wanted this as much as me."
                    sis "I have to go."
                    sis "She's going to wake up any moment now."
                    off "She exits the room and leaves me alone."
                    scene ep4_sc1_mcr_07
                    off "I lie back on my bed."
                    off "All of this is fucking crazy."



        elif (ep3sflove == False and ep3sfangrylove == True) or (ep3sfdomrelationship == True):
            off "Of course, we don't want to get caught on our first day."
            off "I stop her as she's about to open the door."
            scene ep4_sc1_mcr_09
            mc "Wait."
            sis "Yes?"
            off "I grab her as gently as I can."
            off "I still feel a bit uneasy touching her."
            off "I'm afraid she'll finally push me away and slap me in the face."
            scene ep4_sc1_mcr_10
            $ UnlockThat("ep4/ep4_sc1_mcr_10")
            off "She hugs me back as our lips join."
            $ ProcessStat(1, "sis_affection")
            $ DumpNotStack()
            off "Our tongues play with each other as we exchange saliva."
            off "She wanted this as much as me."
            sis "I have to go."
            sis "She's going to wake up any moment now."
            off "She exits the room and leaves me alone."
            off "I lie back on my bed."
            off "All of this is fucking crazy."


        off "I have a feeling that this day is going to be very strange."


label ep4sc2:
    scene ep4_sc2_mcr_00
    if sis_love_path == True:
        off "I stay in my room for a while."
        off "I try to go back to sleep but I simply can't."
        off "I can hear the girls getting ready for their morning workout."
        off "Their voices reach me through the wall as an incomprehensible murmur."
        off "It makes me think that we should be more careful when we're talking about... sensitive things."
        off "I wait for [sis_name] and [sf_name] to leave the house before getting out of my room."
    else:
        off "I wake up hearing the girls getting ready to leave for their morning workout."
        off "By the time I get out of my bed, I'm alone in a silent house."

    scene ep4_sc2_br_01
    if sis_love_path == True and sf_love_path == True:
        off "I take a long and refreshing shower, spending all my time thinking about the mess my relationship with [sis_name] and [sf_name] has become."
        off "I have to set things right, but I have no idea how to do so without worsening the situation."
        off "I don't want to hurt [sf_name] and I can't risk having my thing with [sis_name] exposed."
        off "I can't find any solution."
        off "I am a moron."
        off "I shouldn't have put myself in this situation in the first place."
        off "I should try thinking with my head rather than with my dick."
    else:
        off "I take a long and refreshing shower, spending my time thinking about what happened last night."


    if ep3sisloverejected == True:
        off "I rejected [sis_name]."
        off "I can't help but think that it was the right thing to do even if my reason to do it was wrong."
        off "She desired love, I just wanted to fuck her."
        off "Shit, I can't believe it."

        off "How could I want to fuck [sis_name]? She's like a sister to me!"

        off "I must be some kind of crazy perverted jerk."
        off "I hope I can salvage our newly retrieved brother/sister relationship out of this mess."

    if ep3sisstayed == True and ep3sislove == False and ep3sisloverejected == False:
        off "[sis_name] coming to my room was very confusing."
        off "Spending the night with her was actually nice."
        off "There was some kind of tension between us."
        off "We probably still have to adapt to our newly retrieved brother/sister relationship."

    if sis_love_path == True:
        off "[sis_name] is right."
        off "If anyone found out about our relationship, it'll be the end of us."
        off "We're crazy."
        off "How did we get to that point?"
        off "Four days ago, we could barely stand each other..."
        off "I wonder if things would have been different without these three years of bullshit between us."
        off "Would we have fallen for each other sooner?"
        off "Or would we have just stayed like normal siblings?"

    if ep3sissoloorgasm == True:
        off "[sis_name] let me lick her pussy."
        if ep3sisdoubleorgasm == True:
            off "And the blowjob she gave me on her own accord... that was incredible."
        off "She submitted to me."
        off "Entirely."
        off "In fact, I had the impression that she wanted to submit."
        off "She needed it."
        off "She wanted me to exert my authority on her."
        off "Even if I didn't really have any real authority on her to start with, it looks like I have now."
        off "If she wants to be disciplined, I sure can help her with that."
        off "I have to be careful not to go too far or too fast, but I'll probably be able to get her to do anything I want."
        off "Holy shit, I can't wait."

    if ep3sissubrejected == True or ep3sissubrejected2 == True:
        off "I may have gone a little too far with [sis_name] last night."
        off "She was so pissed that I couldn't even protest when she kicked me out of the kitchen."
        off "Shaking this guy's hand was definitely a bad idea but what else could I have done?"
        off "The guy is twice my size, he would have smacked me down like an insect."
        off "There must be something I can do to fix this situation, but what?"

    if ep3sisluked == True:
        off "That slut spent the night on her phone with this asshole."
        off "She's crazy."
        off "The guy tried to rape her and she's about to give him her pussy, just like that."
        off "There must be something I can do."
        off "I have to save that bitch from herself."
        off "Come on [mc_name]. Find something."
        off "Maybe I should talk about that with [sf_name]."
        off "I'm pretty sure she's on my side on this one."


    if sf_love_path == True and sis_love_path == False:
        off "I'm [sf_name]'s boyfriend now."
        off "I still can't believe it."
        off "I can't wait to.. do things with her."
        off "We have to keep our relationship a secret from [sis_name] for now but I'm sure we can find some time to be together nonetheless."
        if ep3sfhandjob == True:
            off "The girl gave me a handjob."
            off "That was an unexpectedly fast development."
        off "I have the impression that this week will wield a lot of surprises."

    if ep3sfangrylove == True:
        off "I really fucked up with [sf_name] last night."
        off "She clearly overreacted but I could have avoided that situation."
        off "By being better at lying and not getting caught for example."
        off "Or by not lying in the first place..."
        off "That was totally ridiculous."
        off "That lie was useless."
        off "She was so pissed off..."
        off "For a second I thought she was about to slap me."

        if sis_love_path == False:
            off "I hope I can get her to forgive me."
            off "Fuck, I was about to get laid!"

        if sis_love_path == True:
            off "I should talk to her to apologize, at least."
            off "I'll have to think carefully about what I'll say."
            off "I'm with [sis_name]."
            off "I want [sf_name] to forgive me but I don't want to be her boyfriend anymore."
            off "And I can't just dump her."
            off "It has to come from her..."
            off "Talk about a weird situation."

    if sf_dom_path == True:
        off "I'm having trouble understanding what happened with [sf_name]."
        off "I'm supposed to be her boyfriend but... what we did last night .. wasn't classical couple stuff."
        off "The things she made me do ... I still can't believe I accepted that so easily."
        off "Am I into that kind of stuff?"
        if ep3ballscrushed == True:
            off "That was clearly a punishment."
            off "I can still feel her feet crushing my balls."
        off "She was so dominant..."
        if ep3ballscrushed == True:
            off "I'm a bit afraid of what could come next."
        else:
            off "I have to say that I'm curious to see what will come next."

    off "Seeing [sf_name] naked in the pool was damn nice."
    off "She looked so shy."
    if ep3pooldickmove == True:
        off "That was fun."
        off "If only [sis_name] hadn't come... she ruined everything."
    else:
        off "And a bit afraid."
        off "Luckily for her, I'm a gentleman."

    scene ep4_sc2_mcr_01
    if sis_sub_path == True or sis_love_path == True or sf_love_path == True or sf_dom_path == True or ep3sisluked == True:
        off "I feel like I'm going crazy."
        off "I can't think about anything else but the girls."
        off "It's an obsession."
        off "I need to clear my head."


    if ep3kfgftold == True or ep3kfmeetaccepted == True or ep3kfrejected == True:
        off "Holy shit."
        off "I totally forgot about Kelly."
        off "Maybe I should tell the girls about that?"
        if sis_sub_path == True or sis_love_path == True or sf_love_path == True or sf_dom_path == True:
            off "I feel like it’s no big deal but if I hide anything from them it may come back at me hard."
        else:
            off "I have no idea what will happen with this girl but there's a chance that things get interesting."
            off "We'll see!"
        scene ep4_sc2_mcr_01_bis

        if ep3kfgfmeetaccepted == True or ep3kfmeetaccepted == True:

            if sis_love_path == True or sf_love_path == True:
                off "I agreed to meet her today but..."
                off "My situation isn't exactly the same as it was when she asked me out, is it?"

            if sis_sub_path == True or sis_love_path == True or sf_love_path == True or sf_dom_path == True:
                menu:
                    "Should I text her to cancel?":
                        off "I'm not sure I have any interest in meeting her anymore."
                        off "And the girls could misinterpret it."
                        off "I should tell them about that phone call."
                        off "Honesty can't hurt, right?"
                        $ ep4showercancelquestion = True
                    "That doesn't change anything. [blue]\[Harem Path?\]":
                        off "I'm just going to meet her, not to cheat on..."
                        $ ep4showermeetingwill = True
                        menu:
                            "[sis_name]" if sis_love_path == True or sis_sub_path == True:
                                $ ep4showerchoice = "[sis_name]"
                            "[sf_name]" if sf_love_path == True or sf_dom_path == True:
                                $ ep4showerchoice = "[sf_name]"
                            "... The girls." if (sis_love_path == True or sis_sub_path == True ) and (sf_love_path == True or sf_dom_path == True ):
                                $ ep4showerchoice = "Both"


                        off "I should probably be careful to keep it a secret, though..."
                        off "..."
                        off "Am I really going to do that?"

    if ep2shadesordered == True:
        off "The doorbell rings loudly."
        scene ep4_sc2_ent_01
        off "I hurry across the house to open the door."
        off "It's a delivery man."
        off "He gives me a little package with my name on it."
        off "The shades I've ordered for [sis_name]."
        scene ep4_sc2_mcr_02
        $ UnlockThat("ep4/ep4_sc2_mcr_02")
        off "I manage to make an acceptable gift box and hide it in my room."
        off "I'll wait for the right time to gift her these."

    scene ep4_sc2_mcr_01
    off "I can hear the girls coming back."
    off "They laugh as they climb the stairs."
    off "Their mood seems pretty good."
    scene ep4_sc2_c_01
    off "I meet them in the hallway."


    if sf_love_path == True:
        mc "Hey."
        sis "Hey."
        scene ep4_sc2_c_07
        $ UnlockThat("ep4/ep4_sc2_c_07")
        off "To my surprise, [sf_name] immediately jumps on me."
        off "I barely manage to grab her."
        off "She vigorously kisses my lips."
        scene ep4_sc2_c_08_alt
        $ UnlockThat("ep4/ep4_sc2_c_08_alt")
        off "So much for keeping our relationship a secret then..."
        if sis_love_path == True:
            scene ep4_sc2_c_09_bis
            $ UnlockThat("ep4/ep4_sc2_c_09_bis")
        else:
            scene ep4_sc2_c_09
            $ UnlockThat("ep4/ep4_sc2_c_09")
        sf "I'm sorry, [mc_name]."
        sf "I couldn't resist."
        sf "She's my friend, I had to tell her."
        sf "She knows everything."
        off "Of course, you had to tell her."
        off "I should have known."

        if ep4sismorningtold == True:
            off "Luckily, I told her first."

        if sis_love_path == True and ep4sismorningtold == False:
            off "Shit. I'm dead."

        mc "Oh.... ok..."
        sis "Everything."
        off "[sis_name] isn't laughing anymore."

        if sis_love_path == False:

            off "She's looking away from me, avoiding my gaze."
            sis "Yeah, well."
            sis "Congratulations, or whatever."
            scene ep4_sc2_c_11
            $ UnlockThat("ep4/ep4_sc2_c_11")
            off "She quickly heads for the bathroom."
            sis "It's your life, you do what you want with it."
            sis "If you hurt her, I'll kill you."
            off "She can't stop saying she will kill me but the sadness in her voice clearly states otherwise."
            off "[sf_name] lightly gives me another kiss before getting away from me."
            sf "I'm joining her."
            sf "See you later!"
            off "She seems genuinely happy."
            mc "Sure."

        if sis_love_path == True:
            scene ep4_sc2_c_12
            $ UnlockThat("ep4/ep4_sc2_c_12")
            sis "We need to talk."
            sis "My room."
            sis "Now."
            off "Her tone is frighteningly hard."
            sf "I'll be in the bathroom."
            scene ep4_sc2_sr_01
            $ UnlockThat("ep4/ep4_sc2_sr_01")
            off "I follow [sis_name] into her room."
            off "She closes the door behind us."

            if ep4sismorningtold == False:
                sis "Do you have anything to say?"
                mc "I'm sorry."
                scene ep4_sc2_sr_02
                sis "Sorry you got caught, I guess."
                mc "No."
                mc "I hesitated to tell you this morning."
                mc "I didn't because I thought I could maybe talk with [sf_name] and find a way to end my relationship with her without hurting her or you."
                scene ep4_sc2_sr_03
                $ UnlockThat("ep4/ep4_sc2_sr_03")
                off "She sighs."
                sis "I knew it."
                sis "I saw you kissing in the living room last night."
                sis "I came to your room knowingly."
                mc "You knew?"
                sis "Yes. I thought it was my last chance to... approach you before it gets too serious between you two."
                mc "Ok..."
                scene ep4_sc2_sr_04
                sis "I hoped you would tell me this morning, but you didn't."
                mc "I'm sorry."
                mc "I should have."
                mc "I didn't know how to say it."
                mc "I was afraid."
                sis "Afraid I would kill you?"
                sis "Afraid I would lose you."
                off "She loses the angry face."
            else:
                off "She loses the angry face as soon as we're alone."

            scene ep4_sc2_sr_05
            $ UnlockThat("ep4/ep4_sc2_sr_05")
            sis "She told me almost immediately."
            sis "She was clearly uneasy and finally let it out a couple minutes after we've left the house."
            sis "She was apologetic at first."
            sis "She then spoke about you for the whole hour we spent exercising."
            sis "I'm pretty sure she has more to tell me under the shower."
            mc "That's flattering..."
            scene ep4_sc2_sr_06
            sis "You hooked her well, dumbass."
            mc "I don't even know how I did that."
            sis "She doesn't know either."
            sis "So... what do we do?"
            mc "I'll tell her we're making a mistake, something like that maybe."
            sis "A mistake?"
            sis "Get real, blockhead."
            sis "It's a miracle you actually seduced her."
            sis "You're a nerd, a bit of an imbecile and physically average while she's beautiful, smart and kind."
            sis "She's pretty much everything a guy could dream of."
            sis "How could you define your relationship as a mistake?"
            sis "If someone is making a mistake here, it's her, not you."
            scene ep4_sc2_sr_05
            mc "Well, thank you... it's very pleasing to know that you think so highly of me."
            sis "Don't you understand?"
            sis "She's falling for you, really."
            sis "I don't know how it's possible but she thinks she's in love with you."
            sis "You can't just dump her like that."
            sis "It would hurt her."
            sis "And she's not stupid."
            sis "She would understand that there is something else going on."
            scene ep4_sc2_sr_06
            mc "I can tell her that I'm afraid that being her boyfriend could hurt the brother/sister relationship we're trying to restart together..."
            mc "I'm sure she would understand that."
            sis "Great."
            sis "You want me to be the bad guy in your story?"
            sis "Is that it?"
            sis "It won't work..."
            sis "I .. gave her my blessing."
            scene ep4_sc2_sr_05
            mc "What? Why would you do that?"
            sis "What else could I do?"
            sis "Tell her \"Sorry, I'm secretly in love with him too\"?"
            sis "She asked for it!"
            sis "I didn't have any choice!"
            scene ep4_sc2_sr_07
            $ UnlockThat("ep4/ep4_sc2_sr_07")
            mc "Ok so, let me summarize the situation:"
            mc "We don't want to hurt her, she's clearly out of my league, we don't want her to know about us, and you gave her your blessing."
            mc "As a result, I can't end my relationship with her because I have no logical reason to do so without giving her some serious hint about you and me being more than siblings."
            mc "This is crazy, [sis_name]."
            mc "You're telling me that I should continue being her boyfriend while secretly being with you?"
            sis "No!"
            sis "I don't want to share you or anything like that!"
            sis "I just don't know how to resolve this situation."
            sis "I want you to be mine, and mine only, but I don't think we have a choice."

            if ep4sismorningtold == True:
                menu:
                    "Get closer. [sisLovePath]":
                        $ ep4sistalkkiss = True
                        $ ProcessStat(1, "sis_affection")
                        $ DumpNotStack()
                        scene ep4_sc2_sr_08
                        $ UnlockThat("ep4/ep4_sc2_sr_08")
                        sis "What are you doing?"
                        mc "I'm grabbing you."
                        mc "I'm going to kiss you."
                        sis "Great."
                        sis "Do you think this is an appropriate moment?"
                        sis "We're talking about your girlfriend, the one you're cheating on."
                        sis "With me."
                        sis "I'm stealing my best friend's boyfriend."
                        sis "I'm so awful I deserve to die."
                        mc "You know it's not as simple as that."
                        mc "I think that it's one of these situations where you don't really have a choice."
                        mc "Destiny, fate, things like that."
                        sis "I tried not to come to you. I couldn't..."
                        mc "We'll find a solution."
                        mc "Everything will be alright, Princess."
                        sis "It's not a fairy tale."
                        sis "Chances are it won't end well."
                    "Stay where you are.":
                        pass

            mc "I think she's your friend."
            mc "We should tell her everything."
            mc "Maybe it will hurt her, but I'm sure that she loves you enough to keep our thing a secret."
            mc "We should be honest about it."
            mc "We should... trust her."
            sis "I think so."
            sis "But will you risk it?"
            sis "If we're wrong we'll lose everything."
            sis "Not only each other, everything."
            sis "We should think about it very carefully."
            sis "You can manage another day?"
            if ep4sistalkkiss == True:
                scene ep4_sc2_sr_09
                $ UnlockThat("ep4/ep4_sc2_sr_09")
            mc "You understand that if I'm her boyfriend, I may have to be intimate with her."
            sis "Yeah, I'm sure it bothers you a lot."
            mc "It actually does."
            mc "I feel bad about it, for you and for her."
            sis "If you fuck her, I will kill you."
            mc "I won't do that."
            sis "I'm serious."
            mc "I know."

            if ep4sistalkkiss == True:
                $ ProcessStat(1, "sis_affection")
                $ DumpNotStack()
                scene ep4_sc2_sr_10
                $ UnlockThat("ep4/ep4_sc2_sr_10")
                off "I can feel her gasping breath on my face."
                off "I suddenly realize I'm panting myself."
                scene ep4_sc2_sr_11
                $ UnlockThat("ep4/ep4_sc2_sr_11")
                off "Lips meet."
                off "Mouths open."
                off "Tongues interweave."
                off "I can feel something building between us."
                off "Both of us want more than just a kiss."
                off "It's exciting and frightening at the same time."
                scene ep4_sc2_sr_10

            sis "Get out now, I need a shower."
            mc "As you wish, Princess."
    else:
        if ep3pooldickmove == True:
            mc "Hey."
            scene ep4_sc2_c_02
            $ UnlockThat("ep4/ep4_sc2_c_02")
            sis "Hey, perv."
            sf "Hey, [mc_name]."
            off "Obviously, my last night stunt by the pool hasn't been forgotten yet."
            mc "I wanted to apologize for last night... I don't know why I thought it would be funny."
            mc "I hadn't planned to embarrass you or anything..."
            sf "It's ok."
            sf "Just don't do it again."
            mc "I won't, I promise."
            off "Apologizing truly makes wonders."
        else:

            mc "Hey."
            scene ep4_sc2_c_02_alt
            $ UnlockThat("ep4/ep4_sc2_c_02_alt")
            sis "Hey, perv."
            sf "Hello, [mc_name]."

        mc "So ... How did your morning exercise go?"
        sis "Nicely."
        sis "But it's still too hot out there."
        sis "It's actually so hot that I can feel the sweat evaporating on my skin."
        sf "Luckily for us, the park is full of shadows."
        sis "I feel like I'm radiating heat."
        sis "Cooling down in the shower will be nice."
        sis "Time to hit the bathroom, babe."

        if ep3sisluked == True:
            scene ep4_sc2_c_03
            sf "I'm joining you in a minute."
            off "[sis_name] disappears in the bathroom."
            off "[sf_name] turns back to me with a totally different expression on her face."
            scene ep4_sc2_c_04
            $ UnlockThat("ep4/ep4_sc2_c_04")
            off "She quickly closes the distance separating us."
            sf "We need to talk."
            off "She lowers her voice."
            off "We're conspirators now."
            sf "About [sis_name] and this guy."
            mc "I know..."
            sf "We have to do something."
            mc "Obviously, but what?"
            sf "Think about it."
            scene ep4_sc2_c_05
            sf "Find something."
            mc "She's not even rational, I doubt we can resort to logical arguments."
            sf "There must be something we can say or do."
            sf "She's doing this bullshit for a reason."
            sf "And I'm pretty sure it's you."
            mc "What, she's dating this rapist because of me now?"
            sf "I don't know for sure, but you'd better find a way to get her out of this."
            sf "I have to join her."
            sf "We'll talk later."
            scene ep4_sc2_c_06
            $ UnlockThat("ep4/ep4_sc2_c_06")
            off "She doesn't even wait for my reply."
            off "I can't help but think there was something of a threat in [sf_name]'s tone."
        else:
            scene ep4_sc2_c_03_alt
            sf "I'm right behind you, love."
            mc "See you later, I guess."

        if ep2cameraset == True:
            off "Anyway... It's shower time, baby!"
            scene ep4_sc2_mcr_03
            off "Come on girls, I'm sure you can give me a better show than last time."
            off "Shit, what's wrong?"
            off "My phone can't connect to the camera?"
            off "Is it broken?"
            off "Fuck, the battery must be empty."
            scene ep4_sc2_mcr_04
            $ UnlockThat("ep4/ep4_sc2_mcr_04")
            off "What a moron."
            off "Of course, it's down."
            off "I'm failing even as a perv."
        else:
            off "The discussion went unexpectedly fast."
            off "They seemed pretty eager to get to the bathroom together..."
            off "I wonder if all girls shower with their friends like that."
            off "I sure would never shower with Steve."


label ep4sc3:
    scene black with dissolve
    with Pause(2)
    show text "Half an hour later."
    with Pause(2)
    scene ep4_sc3_k_0 with fade
    $ UnlockThat("ep4/ep4_sc3_k_0")
    off "The smell of the bacon, sizzling in the pan, dragged me to the kitchen."
    off "I'm hungry."
    mc "Hey."
    scene ep4_sc3_k_1
    sis "Hey."
    mc "You're making breakfast?"
    sis "No, I'm just pretending."
    mc "Nice."
    mc "I'm counting on you, Princess."
    mc "I'm starving."
    sis "I'm glad to know it."
    scene ep4_sc3_k_2
    $ UnlockThat("ep4/ep4_sc3_k_2")
    menu:
        "Do you need any help? [gr]\[BreakfastHelp\]":
            $ ep4breakfasthelpoffered = True
            sis "Oh, because I look like I can't handle cooking eggs and bacon?"
            sis "Get out of this kitchen."
            sis "I'll call you when it's ready."
        "Do you have any idea what you're doing?":

            sis "Yeah, I'm poisoning your breakfast so you will die eating this crap?"
            sis "Happy?"
            sis "Now get the fuck out of here."

    mc "Alright, alright, I'm leaving."
    scene ep4_sc3_k_3

    menu:
        "Just don't burn the bacon, please...":
            scene ep4_sc3_k_4
            $ UnlockThat("ep4/ep4_sc3_k_4")
            sis "You get out of here now or I'll kill you."
            sis "I swear."
            mc "I leave the kitchen laughing."
            mc "I like making her mad."

        "I wasn't mocking you. [sisLovePath]" if ep4breakfasthelpoffered == True:
            $ ProcessStat(1, "sis_affection")
            $ DumpNotStack()
            mc "I just genuinely wanted to help you."
            off "She sighs."
            scene ep4_sc3_k_4_alt
            $ UnlockThat("ep4/ep4_sc3_k_4_alt")
            sis "I know... And I want to do it all by myself."
            mc "Alright."
            off "I'm about to leave the kitchen when she stops me."
            sis "[mc_name]."
            mc "Yes?"
            sis "Thank you."
            mc "You're welcome."

    scene black with fade
    with Pause(2)
    scene ep4_sc3_l_0 with fade
    $ UnlockThat("ep4/ep4_sc3_l_0")

    off "I head to the living room to wait comfortably on the sofa."
    off "I haven't reached the couch when I hear someone lightly running in the hallway."


    if sf_love_path == True:
        scene ep4_sc3_l_1
        $ UnlockThat("ep4/ep4_sc3_l_1")
        off "[sf_name] joins me."
        sf "Hey, [mc_name]."
        mc "Hey, [sf_name]."
        scene ep4_sc3_l_2
        off "She comes closer and snuggles into my arms."
        scene ep4_sc3_l_2_alt
        $ UnlockThat("ep4/ep4_sc3_l_2_alt")
        off "The smile on her face is disarming."
        off "She's literally sparkling with happiness."

        menu:
            "Give her a quick kiss.":
                scene ep4_sc3_l_3
                $ UnlockThat("ep4/ep4_sc3_l_3")
                off "Our lips quickly meet."
                off "I have the feeling she hoped for more."
            "Give her a proper kiss. [sfLovePath]":
                scene ep4_sc3_l_4
                $ UnlockThat("ep4/ep4_sc3_l_4")
                $ ProcessStat(2, "sf_affection")
                $ DumpNotStack()
                off "She hugs me tighter as our lips meet."
                off "I feel like she desired this kiss for a long time."
                off "She blossoms into my arms."
                off "Growing even happier."

        if sis_love_path == True:
            off "I hate myself."
            off "I should take her to the kitchen, with [sis_name], and tell her what is happening."
            off "She deserves the truth."
            off "But I can't say it."
            scene ep4_sc3_l_5
            $ UnlockThat("ep4/ep4_sc3_l_5")
            sf "I hope [sis_name] wasn't too harsh on you."
            mc "She wasn't."
            sf "I'm curious about what she told you..."
            mc "Essentially... that she would kill me if I happened to hurt you."
            sf "She's a bit overprotective."
            sf "Probably just as I am towards her."
            mc "You're fairly close to each other."
            mc "So I don't think there's anything strange in that behavior."
        scene ep4_sc3_l_6
        sf "I'm sorry, [mc_name]."
        sf "I asked you to keep it a secret but I couldn't do it myself."
        sf "She's my best and only friend."
        sf "The instant I saw her this morning, I knew I had to tell her about us."

        if sis_love_path == True:
            off "[sis_name] must be going through hell right now."
            off "She can't tell [sf_name] about what's happening and she has to endure looking at [sf_name] and me."
            off "That situation is so shitty."

        sf "And I was so happy once I'd told her."

        if ep3sfsislovechat == True:
            off "She seems totally oblivious to what she told me yesterday about [sis_name]'s feelings towards me."
            off "She drowns completely in her own joy."

        sf "I was a bit afraid of her reaction at first but she was really supportive, she even gave me her blessing."
        mc "I'm glad it turned out so well."
        mc "To be honest, I'm a bit relieved too."
        mc "I'm not sure we would have been able to hide anything from her."

        sf "I thought about you, and us, a lot."
        sf "The more I think about us, the better I feel."
        sf "I don't know what's happening to me."
        sf "It's the first time I feel that way for someone."
        sf "Being with you... I think it makes me happy."
        mc "What makes you happy, makes me happy."
        off "It's like she's letting go of a mask she was wearing until now."
        off "[sf_name] usually shows a very different personality."
        off "Confident, independent, strong, kind but cold."
        off "But right now, in my arms, she seems fragile, small, she gives into me completely because she trusts me."
        off "I suddenly understand that these three years of pain [sis_name] endured, [sf_name] experienced them too."
        off "The rumors weren't as harsh on her as they were on [sis_name], most of that bullshit wouldn't stick."
        off "But still, that doesn't mean it was a pleasing experience."
        scene ep4_sc3_l_6_alt

        menu:
            "I'm sorry. [sfLovePath]":
                $ ep4sfmorningsorry = True
                mc "I just realized that you more or less lived the same thing [sis_name] did these past three years."
                mc "And it pains me to know that you have suffered."
                mc "I'm ashamed I didn't do anything."
                sf "We barely knew each other, [mc_name], there was nothing you could have done for me."
                sf "Besides, it didn't hit me as hard as it did [sis_name]."
                sf "I had my way to deal with it, and my dad believed and trusted me, even if he wasn't there to support me..."
                mc "That sounds so lonely."
                sf "It was."
                mc "But it's over now."
                mc "You don't have to be lonely anymore."
                scene ep4_sc3_l_7
                $ UnlockThat("ep4/ep4_sc3_l_7")
                off "She hides her head in my shoulder."
                off "Wait."
                off "Is she crying?"
                off "Holy shit."
                mc "Hey... What's the matter? Did I say something?"
                sf "Oh, no, no, I'm sorry."
                sf "It's just.. It's nothing."
                mc "Really?"
                mc "It doesn't look like it's nothing to me."
                sf "I told you, it's new to me."
                sf "I'm not sure I'm handling it well."
                sf "You could say I'm just crying with happiness."
                $ ProcessStat(2, "sf_affection")
                $ DumpNotStack()

                scene ep4_sc3_l_8

                menu:
                    "You keep saying that. [sfLovePath]":
                        $ ep4sfcontrollove = True
                        mc "But I'm not sure there's anything to handle."
                        mc "You don't have to control everything."
                        mc "You can just let go."
                        sf "She lets out a shy laugh."
                        sf "Easier said than done."
                        sf "I haven't been raised that way."
                        sf "My nanny wouldn't be pleased seeing me like that."
                        mc "She has nothing to say about it."
                        mc "It's your life, and you live it as you want."
                        mc "Especially when it comes to love."
                        $ ProcessStat(2, "sf_affection")
                        $ DumpNotStack()
                        sf "Love. That sounds nice."
                        mc "It does, yes."
                    "If you say so...":
                        mc "I can only trust you on that."
                        mc "I hope you'll tell me if I ever say or do anything wrong."
                        off "She lets out a shy laugh."
                        sf "I will. You can trust me with that too."

                scene ep4_sc3_l_9
                $ UnlockThat("ep4/ep4_sc3_l_9")
                sis "Guys? Didn't you hear me?"
                off "As soon as I hear [sis_name]'s voice, I know what's going to happen."
                sis "Breakfast is served, guys."
                mc "We're coming, right away."
                off "[sis_name]'s expression changes when she sees the tears on [sf_name]'s face."
                off "She quickly gets to her while yelling at me."
                scene ep4_sc3_l_10
                sis "What the fuck did you do to her?"
                sf "I'm alright!"
                sf "He didn't do anything."
                sf "I just got emotional, for no reason."
                sis "Are you sure?"
                sis "No reason, really?"
                sis "If this dumbass hurts you, I..."
                scene ep4_sc3_l_11
                $ UnlockThat("ep4/ep4_sc3_l_11")
                sf "Calm down, please, you don't have to worry."
                sf "He didn't do anything."
                sf "He's been sweet to me, nothing else."
                sis "You're crying because he's sweet?"
                sf "I know it's ridiculous, let's just stop talking about that ok?"
                sf "It's kind of humiliating."
                scene ep4_sc3_l_12
                $ UnlockThat("ep4/ep4_sc3_l_12")
                off "I sigh as I let them leave the room without me."
                off "I begin to realize that I'm definitively not equipped to deal with psychologically damaged girls."
                off "I think I liked the moron role better."
                off "It was simpler."
                off "Trying to be a decent human being is much more difficult."
                off "And it's painful."
            "So... How was the shower?":
                scene ep4_sc3_l_6
                sf "Refreshing, and relaxing."
                mc "As expected from a shower, I guess."
                mc "But I wonder... what are you doing with [sis_name] in that bathroom?"
                sf "Well, showering, mostly."
                sf "What else?"
                mc "I don't know, I'm just not used to see people taking showers together..."
                mc "Wait, mostly?"
                scene ep4_sc3_l_13
                sf "You'll never know."
                off "She laughs as she gets away from me and runs to the kitchen."
                scene ep4_sc3_l_13_alt
                $ UnlockThat("ep4/ep4_sc3_l_13_alt")
                off "She's definitely playing me."

    elif ep3sisluked == True:
        scene ep4_sc3_l_19
        $ UnlockThat("ep4/ep4_sc3_l_19")
        off "[sf_name] joins me."
        sf "Hey, [mc_name]."
        mc "Hey, [sf_name]."
        off "She slowly gets closer."
        off "I have no idea how to behave."
        scene ep4_sc3_l_20
        sf "[mc_name], I think we need to talk."
        mc "I'm all ears."
        off "She briefly checks behind her to be sure [sis_name] isn't about to surprise us."
        sf "Did you think about what I told you earlier?"
        mc "Of course, I did."
        mc "To be honest, I can't think about anything else."
        mc "You are obviously right."
        mc "We have to do something."
        mc "We can't let her give into this guy."
        scene ep4_sc3_l_21
        sf "I'm glad you're agreeing with me but we already know that."
        sf "Do you have any idea how to do so?"
        mc "Not really..."
        off "She sighs"
        sf "Listen to me, [mc_name]."
        sf "I think it's some kind of act of rebellion."
        sf "She wants to prove you wrong."
        sf "I told you this morning it was because of you."
        sf "You don't seem to understand that."
        mc "Because I've done nothing!"
        sf "You've done enough."
        sf "I've asked you to listen, not to speak."
        sf "You're rejecting each other, and she will do anything to show you that you have no right to say anything about her life."

        sf "I'll be brutally clear: if you don't improve your relationship with [sis_name] to a point where she can listen to you and consider your advice enough to dump this guy, you will lose her definitely."

        sf "She will probably destroy herself and it will completely fuck up your family and your life."
        sf "Do you understand what I just said?"
        mc "No, I don't!"
        mc "What the hell am I suppose to do?"
        scene ep4_sc3_l_22
        $ UnlockThat("ep4/ep4_sc3_l_22")
        sf "Stop being a moron, show her you care about her, be understanding, treat her like a human being."
        sf "Apologizing would be nice."

        sf "You have to show her that you're are still like a brother to her, that she can count on you to help her, not to continuously judge her."

        sf "She needs, at least, to feel safe with you."
        sf "Can you do it?"

        menu:
            "You're asking me to lick the floor under her feet.":
                mc "I'm not that kind of guy."
                off "There's no way I submit to this bitch."
                sf "Whatever you are doesn't change a thing."
                sf "Either you try to reconcile with [sis_name] or you lose everything."
                sf "It's up to you."
                mc "Yeah, yeah, it's up to me."
            "I'm not the only one to blame for our shitty relationship. [sfDomPath]":
                mc "She has her share of responsibility in this mess!"
                sf "That's probably true."
                sf "But someone has to take the first step."
                sf "Are you mature enough to understand that?"
                off "I keep silent for a few seconds, thinking about what to do, and what to say."
                off "[sf_name] may be right."
                $ ProcessStat(2, "sf_dominance")
                $ DumpNotStack()

        scene ep4_sc3_l_21
        sf "You want her to respect you."
        sf "Fair enough, you'll have to show her that you respect her first."
        mc "I'll think about that."
        sf "Think fast then, because I have the feeling that this is your last chance."
        off "She turns back and leaves the room as [sis_name]'s voice hurls through the house."
        sis "Breakfast is ready!"

        off "My last chance."
        off "Do I want to take it or not?"
    elif sf_dom_path == True:
        scene ep4_sc3_l_14
        $ UnlockThat("ep4/ep4_sc3_l_14")
        off "[sf_name] joins me."
        sf "Hey, [mc_name]."
        mc "Hey, [sf_name]."
        off "She slowly gets closer to me."
        off "I don't know what to do."
        off "I didn't have the time to think about it."
        off "Should I tell [sf_name] that I'm not interested in this relationship anymore?"
        off "How?"
        if sis_love_path == True:
            off "How to do so without hurting her or making her curious about why?"
        else:
            off "How to do so without hurting her?"
        off "I have no idea how to behave."
        off "I have yet to decide if I'm interested or afraid of her dominant thing."
        scene ep4_sc3_l_15
        sf "I've slept like a baby."
        sf "Your parent's bed is really comfortable."
        mc "I'm glad to hear it."
        off "She quickly looks behind her, probably to be sure that [sis_name] isn't about to surprise us."
        if ep3ballscrushed == False:
            sf "I'm really happy that you accepted to be my partner."
            sf "I thought a lot about what we did last night."
            sf "You behaved so well that I came to think that I have failed to reward you properly."
            sf "You deserve something more... consistent."
            off "Holy shit."
            off "That's it."
            off "She's talking about her pussy!"
            off "Play your cards well, my boy, and you're getting laid!"
            menu:
                "I'm glad you acknowledge my merits.":
                    sf "I wonder if you can maintain this level of commitment."
                    sf "This is only the beginning of our relationship."
                    sf "I want this to go far beyond what happened last night."
                    sf "Do you wish to pursue?"
                    sf "I can promise you, you won't be disappointed."
                "I only crave to please you, my lady. [sfDomPath]":
                    $ ProcessStat(2, "sf_dominance")
                    $ ProcessStat(1, "sf_affection")
                    $ DumpNotStack()
                    sf "As it should be."
                    sf "But hearing it is very satisfying."
                    sf "Tonight, we'll try something new."
                    sf "I know you will perform greatly."
                    sf "And I can promise you that you will like your reward."
            scene ep4_sc3_l_16
            $ UnlockThat("ep4/ep4_sc3_l_16")
            off "She puts her fingers under my nose."
            off "What the fuck is she doing?"
            off "Wait, that smell..."
            off "Is that...?"
            off "Did she...?"
            off "Her pussy?"
            scene ep4_sc3_l_17
            $ UnlockThat("ep4/ep4_sc3_l_17")
            off "She inserts her fingers in my mouth and play with my tongue as I'm completely struck with astonishment."
            off "She's making me taste her pussy!"
            off "Holy shit, I want more!"
        else:
            sf "You know, [mc_name], I'm kind of sorry about last night."
            sf "I had to punish you for what you did and I really hope it won't happen again."
            sf "But I'm afraid I have been too harsh on you."
            sf "It pains me to think that the punishment that I inflicted upon you may have been a bit disproportionate."
            sf "I want to be fair."
            sf "That's why I want you to know that if you behave well today, I'll reward you with something you will like."
            scene ep4_sc3_l_17
            $ UnlockThat("ep4/ep4_sc3_l_17")
            off "I'm about to tell her that I'm not sure I want to continue our relationship when she suddenly put her finger across my lips."
            sf "Think carefully, [mc_name]."
            off "What's that smell?"
            off "Holy shit?"
            off "Is that her pussy?"
            off "Did she just finger herself or something like that?"
            off "She inserts her fingers in my mouth and play with my tongue as I'm completely struck with astonishment."
            off "She's making me taste her pussy!"
            off "Holy shit, I want more!"
            off "This girl is crazy but I can feel it, she's about to give me her pussy!"
            off "Tonight is your night, [mc_name]!"

        scene ep4_sc3_l_17_plus
        $ UnlockThat("ep4/ep4_sc3_l_17_plus")
        off "She removes her fingers and begins to slowly lick my saliva while looking me straight in the eyes."
        menu:
            "I...":
                pass
            "You...":
                pass
        sf "Shhhh. You don't need to reply."
        sf "Just be a gentleman, and you'll get your reward."
        scene ep4_sc3_l_18
        $ UnlockThat("ep4/ep4_sc3_l_18")
        off "She kisses me on the cheek and quickly leaves the room."
        off "I'm still not sure what's her kink and I doubt I'm into it, but if it can get me this fine pussy..."
        off "I sure can be a gentleman."
        off "How the fuck am I going to get out of this mess?"
        off "Am I even sure I want to get out of it by the way?"
    elif ep3sfangrylove == True:
        scene ep4_sc3_l_23
        $ UnlockThat("ep4/ep4_sc3_l_23")
        off "[sf_name] joins me."
        sf "Hey, [mc_name]."
        mc "Hey, [sf_name]."
        scene ep4_sc3_l_23_bis
        mc "[sf_name], I wanted to apologize."
        mc "I shouldn't have lied in the first place."
        mc "And I shouldn't have tried to cover it."
        mc "It was stupid."
        sf "Yes, it was."
        mc "I hope you can forgive me."
        scene ep4_sc3_l_24
        off "She seems embarrassed."
        sf "I'll be honest [mc_name]..."
        sf "You disappointed me."
        sf "You told me that I could trust you only to lie to me a few minutes later."
        sf "That made me... reconsider."

        if sis_love_path == True:
            off "Ok..."
            off "It's actually... good..."
            off "Let's try to salvage a friendship out of this, and no more."
        else:
            off "There goes my chance of fucking her."
            off "Shit. What do I say?"
            off "If I don't have a brilliant idea to get her back I can say goodbye to this nice piece of ass."

        mc "Reconsider?"
        sf "I'm sorry [mc_name], you and me... I think it was a mistake."

        menu:
            "Wait.":
                scene ep4_sc3_l_25
                $ UnlockThat("ep4/ep4_sc3_l_25")
                mc "That lie was insignificant."
                mc "It was nothing!"
                mc "I would never lie to you for something important!"
                sf "It's maybe nothing for you, but it means a lot to me."
                mc "It's not fair!"
                mc "I've been stupid, ok."
                mc "But I don't deserve this!"
                mc "I thought we cared for each other!"
                sf "I thought it too, [mc_name]."
                sf "But it seems that you didn't care about me enough to be honest with me."
                mc "Come on, give me another chance."
                mc "[sf_name], please."
                sf "I'm sorry, [mc_name]. It's over."
                off "She leaves the room quickly without giving me a chance to reply."
                off "Her voice actually sounded pretty sad."
            "I understand. [sisLovePath]":
                scene ep4_sc3_l_26
                $ UnlockThat("ep4/ep4_sc3_l_26")
                $ ProcessStat(1, "sf_affection")
                $ DumpNotStack()
                mc "I'm sorry, [sf_name]."
                mc "I didn't mean to hurt you, in any way."
                sf "I know you weren't ill-intended."
                mc "No, but I was stupid."
                mc "At least, can we still... be friends?"
                sf "... I think so..."
                sf "Just give me a bit more time..."
                mc "Of course."
                if sis_love_path == True:
                    off "Well, it was way easier than expected."
                scene ep4_sc3_l_27
                $ UnlockThat("ep4/ep4_sc3_l_27")
                off "She's about to leave the room when she stops."
                sf "You know [mc_name], I'm quite surprised."
                sf "I'd thought you would try to convince me to give you another chance but you accepted my decision... effortlessly."
                mc "I thought it was useless, that begging for your mercy would have just upset you more."
                mc "That way, at least, we're still friends."
                mc "Was I wrong?"
                sf "I don't know, [mc_name]."
                off "She disappears in the hallway and leaves me with some mixed feelings."
                if sis_love_path== True:
                    off "Maybe I haven't played it as well as I thought."
                    off "She was surprised I didn't fight her decision much."
                    off "I hope I haven't triggered her suspicion or anything like that..."
    else:
        off "That's probably [sf_name] joining [sis_name] in the kitchen."
        off "I wait, watching the weather forecast."
        off "The heat wave's gonna continue until the end of the week."
        off "They're predicting a storm this weekend."



label ep4sc4:
    scene black with fade
    with Pause(2)
    scene ep4_sc4_k_00 with fade
    $ UnlockThat("ep4/ep4_sc4_k_00")
    off "The girls are already seated when I join them for breakfast."
    off "They stop talking when I enter the room."
    sis "What are you waiting for?"
    sis "It's gonna get cold."
    if sis_love_path == True or sis_sub_love_path == True:
        scene ep4_sc4_k_01
        $ UnlockThat("ep4/ep4_sc4_k_01")
    else:
        scene ep4_sc4_k_01_w
        $ UnlockThat("ep4/ep4_sc4_k_01_w")
    off "I was ready for the worst but the food actually looks perfect."
    off "Bacon, eggs, toasts, everything is just properly cooked."

    if sis_love_path == True or sis_sub_love_path == True:
        off "And .. she even made waffles?"
        $ ep4morningwaffles = True

    scene ep4_sc4_k_02
    menu:
        "You did all that by yourself?":
            scene ep4_sc4_k_03
            $ UnlockThat("ep4/ep4_sc4_k_03")
            sis "What's with that question?"
            sis "Of course, I did it by myself."
            sis "Did you see anyone helping me?"
            mc "I agree it's a silly question but honestly, this breakfast looks so perfect..."
            sis "You can't believe I cooked it?"
            sis "If it's your way of complimenting me, you're failing at it."
            mc "Ok, I'm sorry."
            mc "Let me rephrase: I'm impressed and I thank you for this meal."
            scene ep4_sc4_k_05
            $ UnlockThat("ep4/ep4_sc4_k_05")
            sis "Well, you're welcome."
            $ ProcessStat(1, "sis_affection")
            $ ProcessStat(1, "sf_affection")
            $ DumpNotStack()

        "[gr]Holy shit, Princess." if sis_sub_path == True or sis_love_path == True:
            mc "That smells really good."
            mc "And I'm pretty sure it tastes just as nice."
            mc "You nailed the breakfast thing."
            scene ep4_sc4_k_04
            $ UnlockThat("ep4/ep4_sc4_k_04")
            sis "I just threw some eggs and some bacon in a pan... It's no big deal."
            sf "Being modest is nice, but you should accept the praise when it's rightfully deserved."
            sis "Yeah, yeah. Don't let it get cold. Eat it."
            $ ProcessStat(1, "sis_affection")
            $ ProcessStat(1, "sis_submission")
            $ ProcessStat(1, "sf_affection")
            $ DumpNotStack()

        "I must admit defeat. [assholePath]" if ep3sisluked == True:
            mc "You win. No doubt about that."
            scene ep4_sc4_k_05
            $ UnlockThat("ep4/ep4_sc4_k_05")
            sis "That wasn't a competition."
            mc "It was, and you know it."
            sis "If you say so..."
            sf "If it was a competition, there must be a prize."
            scene ep4_sc4_k_02
            sis "I like the sound of that."
            sis "What did I gain?"
            mc "How about nothing?"
            sis "How about you become my servant for 24 hours."
            mc "Great. You know we're not ten years old anymore, don't you?"
            sis "I do."
            scene ep4_sc4_k_05
            sis "Would you have agreed, I wouldn't have asked anything from you."
            sis "I'm obviously more mature than you think."
            sis "I don't want anything from you."
            sis "Eat your breakfast before it gets cold."
            if sis_affection < 5:
                off "That bitch."
            off "I try to be nice and here's how I'm treated."
            off "That being said, this breakfast is damn nice."

    if sis_love_path == True or sis_sub_love_path == True:
        scene ep4_sc4_k_06
        $ UnlockThat("ep4/ep4_sc4_k_06")
        mc "Wait..."
        mc "What about the waffles?"
        mc "These aren't the frozen waffles from the freezer."
        scene ep4_sc4_k_07
        mc "Did you make those?"
        sf "That's why they smell so good."
        sis "They smell like waffles, no more."
        scene ep4_sc4_k_08
        sf "But why did you make those?"
        sis "He said he was starving."
        sis "What was I supposed to do?"
        sis "Let him starve to death?"
        scene ep4_sc4_k_09
        sf "You're starving?"
        mc "I may have said that, at some point..."
        sf "And so you made some extra, home-cooked, self-made waffles."
        sis "What's the problem with that?"
        sf "It just seems a little bit extreme..."
        mc "I'm not complaining."
        mc "I like waffles."
        scene ep4_sc4_k_10
        $ UnlockThat("ep4/ep4_sc4_k_10")
        sf "Of course, you like waffles."
        off "[sf_name]'s voice seems loaded with undertones that make me uncomfortable."
        off "Does she suspect anything?"
        off "Or maybe that was nothing."
        off "I'm probably getting a bit paranoid..."
        off "Either way, this conversation needs to end."
        mc "I'm truly starving now, so if you don't mind, ladies, let's eat."

    scene black with fade
    with Pause(2)
    off "Twenty minutes later, breakfast is over and dishes are in the sink."

    scene ep4_sc4_k_11
    $ UnlockThat("ep4/ep4_sc4_k_11")

    menu:
        "That was fantastic. [sisLovePath] [sfLovePath]" if sis_love_path == True or sis_sub_love_path == True:
            sis "I appreciate the compliment, but you're overdoing it."
            sis "It was just breakfast."
            sf "Will you be alright, [mc_name]? You ate so much..."
            mc "No problem."
            mc "These waffles didn't stand a chance."
            mc "They fought valiantly but I was famished."
            $ ProcessStat(2, "sis_affection")
            $ ProcessStat(2, "sf_affection")
            $ DumpNotStack()
            off "Actually, I wasn't that hungry, but I had to finish the plate nonetheless."
            off "[sis_name] made these for me."
        "Best breakfast, ever. [sisSubPath]":

            $ ProcessStat(1, "sis_submission")
            $ ProcessStat(1, "sf_dominance")
            $ DumpNotStack()
            mc "We should do that more often."
            sis "We? I did everything, you just sat and ate!"
            mc "And it was perfect."
            mc "I'll think of an appropriate reward for this nice moment you offered me."
            sis "Yeah, whatever..."
        "Well, that was good.":

            $ ProcessStat(1, "sis_affection")
            $ ProcessStat(1, "sf_affection")
            $ DumpNotStack()
            mc "I have to admit it."
            mc "As a consequence, I'll retire indefinitely from cooking breakfast."
            sis "I see what you're trying to do here."
            sf "And it won't work."
            mc "Well, I had to try..."

    scene ep4_sc4_k_12
    mc "So... what's your program for today?"
    mc "Have you planned anything?"
    sf "I have to go home to get some clothes."
    sf "Aside from that, I'm pretty sure that relaxing by the pool will be the main event of our day."
    sis "That sounds like my kind of day."

    if ep3kfgftold == True or ep3kfmeetaccepted == True or ep3kfrejected == True:
        off "I suddenly remember my discussion with Kelly."
        off "Should I tell the girls?"
        off "I have no idea how they're going to react."
        off "I feel like I should tell them the truth but at the same time, I'm afraid they'll get angry at me for... nothing."
        off "Because I've done nothing wrong, right?"
        off "What do I do?"

        menu:
            "Keep it a secret.":
                $ ep4morningkfsecret = True
                off "They don't need to know."
                off "Let's avoid a painful misunderstanding and keep it a secret."
                mc "Let us know when you want to hop home, [sf_name], we'll come along you."
                sf "Thank you, [mc_name]."
                mc "You're welcome."
                off "After a few minutes of mundane blabbering, the girls stop caring about me and leave the room, talking about kittens fooling around in a viral video."
                off "The dishes are apparently mine to deal with."
            "[gr]Tell them.":
                $ ep4morningkftold = True
                off "I have to tell them."
                off "It's obvious."
                off "Now, How do I do that?"
                off "Where do I start?"
                scene ep4_sc4_k_13
                menu:
                    mod "{i}Choice is remember, consequence unknown."
                    "Something strange happened to me yesterday.":
                        $ ep4morningspooky = True
                        mc "I feel like I should tell you about it."
                        sf "What kind of strange?"
                        sis "Spooky stuff?"
                        mc "No, nothing spooky."
                        mc "While you were away at this party last night, a girl messaged me."
                    "Hey, something funny happened yesterday.":
                        $ ep4morningfun = True
                        mc "You won't believe it!"
                        sf "What kind of funny?"
                        sf "Steve's kind of funny?"
                        sis "Did he send you some more videos?"
                        mc "No! no!"
                        mc "He didn't send me anything, and my story has nothing to do with him."
                        off "They seem disappointed."
                        off "It's very disturbing."
                        mc "Anyway, while you were away at this party last night, a girl messaged me."


                scene ep4_sc4_k_14
                sf "A girl messaged you?"
                mc "Yeah. We exchanged a few texts."
                mc "She said she had been infatuated with me for a long time."
                mc "She was basically asking me out."
                sis "Are you serious?"
                sis "A girl asked you out?"
                sf "Do you know her?"
                mc "I don't know her."
                mc "She said we were in the same school and her face is a bit familiar to me, but I don't remember her in the least."
                mc "Our school was quite big so..."
                sf "Her face? Do you have a picture?"
                mc "She sent me one, yes."
                off "I take out my phone and quickly find Kelly's photo."
                mc "Here."
                scene ep4_sc4_k_15
                $ UnlockThat("ep4/ep4_sc4_k_15")
                sis "What in the name of fuck is happening?"
                off "[sis_name]'s reaction surprises me."
                off "I was ready for mockery, or anger, but she seems genuinely confused."
                mc "Do you know her?"
                sf "[mc_name], this is Kelly."
                mc "That's the name she gave me."
                sf "The girl who invited us and apologized to us last night."
                sf "It's her."
                mc "Oh..."
                sf "What else did she tell you?"
                mc "Not much."
                mc "She told me she had longed for me for a long time, that she was trying her luck asking me out because she was a bit drunk."
                sis "That can't be a coincidence."
                mc "You think she apologized to you so she could have a chance with me?"
                mc "Or something like that?"
                sis "Yeah sure."
                off "Here comes the mocking."
                mc "What?"
                scene ep4_sc4_k_16
                sis "[mc_name], Kelly is the cheerleader queen kind of girl."
                sis "The one who's going out with the captain of the football team or whatever popular guys."
                sis "Not with .. a guy like you."
                off "I try to hide my disappointment."
                off "This girl was nothing to me but I feel soiled nonetheless."
                off "She sought to use me."
                sis "So... what are our hypotheses?"
                sf "Either she tried to use [mc_name] to get to you and me, or she apologized to us to get to him."
                sf "Most likely the first."
                sf "Maybe she tried to seduce him to separate us."
                sis "What the hell does she want from us?"
                sf "I don't know, but we can fairly assume that her apology was nothing but an act."
                sf "Obviously, she means us no good."
                mc "She knows the guy who tried to drug you and his brother."
                mc "She's probably colluding with them."
                mc "She may even have hired them to rape you."
                mc "What do we do?"
                scene ep4_sc4_k_17
                sf "We go to the police?"
                sis "We already talked about that."
                sis "We're not going to the police."
                mc "You're sure you don't want to reconsider?"
                mc "She tried to get you raped and she obviously still actively tries to hurt you."
                mc "Like [sf_name], I think we should go to the police."
                sis "Guys, nothing has changed."
                sis "We still have no proof."
                sis "No one will believe us, and I will get in trouble with mom."
                sis "No police, please."
                mc "Then there's nothing to do, aside from avoiding the three of them."
                mc "They can't do anything to you if you don't have any contact with them."
                sf "We didn't have any contact with Kelly, starting high school, that didn't prevent her from messing with us."
                mc "You have a point."
                mc "But hopefully, she won't be able to do worse than that."
                mc "I wonder what you did to anger her like that."
                mc "Did you even do anything?"
                mc "She may just be batshit crazy."
                sf "I don't know."
                sf "I don't even remember talking to her before yesterday."
                scene ep4_sc4_k_16
                sis "Batshit crazy it is."
                sis "I didn't do anything to her either."
                off "The mood has definitely gone dark."
                off "I should try to enlighten it a bit."
                mc "It'll be alright."
                mc "We'll stay together and avoid them."
                mc "They may try to contact us again."
                mc "Just politely tell them you don't want to have anything to do with them."
                mc "In a couple days they'll get tired of this bullshit."
                off "I managed to say that with a confident voice but if Kelly is really that crazy, chances are she won't let go that easy."
                off "Shit is going to hit the fan sooner or later."
                off "I should find myself a weapon."
                off "A good old heavy wrench may do the trick."
                off "I'd better keep my eyes open and be ready for anything."
                off "Be careful, [mc_name]."
                off "You're not the hero of an action movie or anything like that."
                off "This is the real life. Don't fuck this up."
                scene ep4_sc4_k_18
                sf "I suppose that's mostly what we were going to do for the rest of the week anyway, but still..."
                sf "I feel kind of robbed of my liberty."
                sis "Likewise."
                mc "It's no big deal."
                mc "You can still do whatever you want, we'll just do it together and we'll keep an eye open."
                mc "Nothing more."

                menu:
                    "Don't let it bring you down, ok? [sisLovePath] [sfLovePath]":
                        mc "It'll be over soon. I swear."
                        $ ProcessStat(1, "sis_affection")
                        $ ProcessStat(1, "sf_affection")
                        $ DumpNotStack()
                    "I promise you everything will be alright. [sisSubPath] [sfDomPath]":
                        mc "Nothing will happen while I'm around here."
                        mc "Trust me."
                        $ ProcessStat(1, "sis_affection")
                        $ ProcessStat(1, "sis_submission")
                        $ ProcessStat(1, "sf_dominance")
                        $ DumpNotStack()

                sf "You're right."
                sf "Besides, worrying too much about that mess would be letting her win."
                sf "And we don't want that."
                sis "No, we want her to go fuck herself as far from us as possible."
                scene ep4_sc4_k_18_plus
                $ UnlockThat("ep4/ep4_sc4_k_18_plus")
                off "[sf_name] laughs lightly ."
                sf "She could get some pleasure out of it."
                sis "I would prefer her to suffer if you don't mind."
                sf "I don't mind at all."
                off "I don't really know why nor how, but we're laughing."
                off "There's nothing funny but we're laughing nonetheless."
                off "I can feel the stress and the anger leaving us in a matter of seconds."
                off "Let's take this opportunity to change the subject."
                mc "Ladies, I'm going to take care of the dishes."
                mc "Let us know when you want to hop home, [sf_name], we'll come along you."
                sf "Thank you, [mc_name]."
                mc "You're welcome."

                off "I head to the sink while the girls leave the room."
                off "[sf_name]'s voice takes me by surprise."
                scene ep4_sc4_k_19
                $ UnlockThat("ep4/ep4_sc4_k_19")
                sf "By the way, [mc_name]... What did you reply?"
                off "They both look at me very seriously."
                off "They seem to be highly interested in my response."
                mc "To what?"
                sf "When Kelly asked you out, what did you reply to her?"
                off "Here comes the tricky question."
                off "Whatever you answer [mc_name], don't hesitate, or they will think you're lying."
                # if ep3kfgfmeetaccepted == True or ep3kfmeetaccepted == True:
                #     $ dynamicChoice1 = " {color=#0f0}[MorningLie]"
                # else:
                #     $ dynamicChoice1 = ""
                menu:
                    mod "{i}Choice is remember, consequence unknown."
                    "I told her I wasn't interested.":
                        sf "Weren't you tempted to meet her?"
                        sf "She's pretty cute."
                        mc "No, I wasn't."
                        sf "She suddenly looks a bit sad and guilty."
                        sf "I'm sorry she tried to use you, [mc_name]."
                        mc "I'm not. I think I can even say that I'm grateful."
                        sf "Grateful?"
                        mc "Yeah. I feel like, in some way, it gets me closer to you both."
                        mc "And I like it."
                        off "[sf_name] and [sis_name] seem to hesitate a second before leaving the room together."
                        if ep3kfgfmeetaccepted == True or ep3kfmeetaccepted == True:
                            $ ep4kfmorninglie = True

                    "I told her I would meet her." if ep3kfgfmeetaccepted == True or ep3kfmeetaccepted == True:
                        $ ep4kfmeettold = True
                        mc "You know, I have been rejected several times myself, and it's pretty painful..."
                        mc "So I thought that I may just meet her to tell her directly that I was sorry, and not interested..."
                        sf "Of course, you're so kind..."
                        off "There's something in [sf_name]'s voice that makes me uncomfortable."
                        off "I should say something but I have the feeling that whatever that comes out of my mouth will only worsen the situation."
                        off "At least I have been honest. Almost."
                        off "They seem to hesitate a second then leave the room for good."
    else:


        off "After a few minutes of mundane blabbering, the girls stop caring about me and leave the room, talking about kittens fooling around in a viral video."
        off "The dishes are apparently mine to deal with."


label ep4sc5:
    scene black with dissolve
    with Pause(2)
    show text "Half an hour later."
    with Pause(2)
    off "The girls enclosed themselves in the master bedroom."
    off "I'm back in my own room."
    scene ep4_sc2_mcr_01_bis with fade
    if ep4morningkfsecret == True and ( ep3kfgfmeetaccepted == True or ep3kfmeetaccepted == True ):
        off "Time passes as I try to decide what to do."
        off "I haven't told the girls about Kelly."
        if sis_sub_path == True or sis_love_path == True or sf_love_path == True or sf_dom_path == True:
            off "It was obviously a wise move."
            off "What do I do now?"
            off "Do I still want to meet her?"
        off "She's supposed to call me today to set up a date."
        off "My phone can ring anytime."

        if full_neutral_path == True:
            off "Maybe I should call her first."
            off "Yeah, let's do that."
            $ ep4kfmeetingok = True
            scene ep4_sc5_mcr_00
            $ UnlockThat("ep4/ep4_sc5_mcr_00")
            off "I'm going to call her and ask her out immediately."
            off "Like, right now."
            scene ep4_sc5_mcr_01
            $ UnlockThat("ep4/ep4_sc5_mcr_01")
            kf "[mc_name]?"
            mc "Hello, Kelly."
            $ ProcessStat(5, "kf_affection")
            $ DumpNotStack()
            kf "Hello, [mc_name]!"
            kf "I'm so happy you called me!"
            off "Her voice is sweet and clear."
            mc "I was getting impatient so I decided to take the initiative."
            mc "I hope you don't mind."
            kf "I'm actually delighted to hear your voice."
            mc "I could say the same thing."
            mc "I like your voice."
            mc "It's just how I have been imagining it."
            kf "I'm glad you like it."
            kf "So... Tell me... Do you still want to meet?"
            mc "More than ever, Kelly."
            mc "I thought that maybe we could have a drink, or whatever, somewhere?"
            kf "That would be great!"
            scene ep4_sc5_mcr_01_plus
            mc "Do you have any preference?"
            kf "Can you wait a second [mc_name]?"
            mc "Sure..."
            off "The line goes totally silent for a few seconds."
            kf "[mc_name]?"
            mc "Yes."
            kf "I'm a very simple girl."
            kf "I don't need anything fancy."
            kf "There's a coffee shop I like."
            kf "I'll send you the address if you're okay..."
            mc "That would be perfect."
            kf "Great!"
            kf "I'm gonna hit the bathroom to get decent and I'll see you there."
            kf "At noon?"
            mc "At noon."
            kf "I hope you won't be disappointed."
            kf "I'm really looking forward to meeting you."
            mc "That's my line."
            kf "See you later!"
            mc "See you later Kelly."
            off "She hangs up."
            off "That was easy."
            off "How come I didn't manage to get a single girlfriend during high-school?"
        else:

            scene ep4_sc2_mcr_01
            menu:
                "Why the fuck am I doing that? [kellyPath]":
                    $ ep4kfmeetingok = True
                    off "I'm buried so deep, that I can barely see the light and I'm going to seek trouble with yet another girl."
                    scene ep4_sc5_mcr_00
                    $ UnlockThat("ep4/ep4_sc5_mcr_00")
                    off "I'm going to call her and ask her out immediately."
                    off "Like, right now."
                    scene ep4_sc5_mcr_01
                    $ UnlockThat("ep4/ep4_sc5_mcr_01")
                    kf "[mc_name]?"
                    mc "Hello, Kelly."
                    kf "Hello, [mc_name]!"
                    kf "I'm so happy you called me!"
                    off "Her voice is sweet and clear."
                    mc "I was getting impatient so I decided to take the initiative."
                    mc "I hope you don't mind."
                    kf "I'm actually delighted to hear your voice."
                    mc "I could say the same thing."
                    mc "I like your voice."
                    mc "It's just how I have been imagining it."
                    kf "I'm glad you like it."
                    kf "So... Tell me... Do you still want to meet?"
                    mc "More than ever, Kelly."
                    mc "I thought that maybe we could have a drink, or whatever, somewhere?"
                    kf "That would be great!"
                    scene ep4_sc5_mcr_01_plus
                    mc "Do you have any preference?"
                    kf "Can you wait a second [mc_name]?"
                    mc "Sure..."
                    off "The line goes totally silent for a few seconds."
                    kf "[mc_name]?"
                    mc "Yes."
                    kf "I'm a very simple girl."
                    kf "I don't need anything fancy."
                    kf "There's a coffee shop I like."
                    kf "I'll send you the address if you're okay..."
                    mc "That would be perfect."
                    kf "Great!"
                    kf "I'm gonna hit the bathroom to get decent and I'll see you there."
                    kf "At noon?"
                    mc "At noon."
                    kf "I hope you won't be disappointed."
                    kf "I'm really looking forward to meeting you."
                    mc "That's my line."
                    kf "See you later!"
                    mc "See you later Kelly."
                    off "She hangs up."
                    off "That was easy."
                    off "How come I didn't manage to get a single girlfriend during high-school?"

                    off "Shit, I’m so dumb."
                    off "Now, let’s be careful."
                    off "If the girls ever know anything about this, it will be the end of me."
                "I have totally lost interest in dating her.":

                    $ ep4kfmeetingcanceledgently = True
                    off "The idea was seductive yesterday but now, it's a different story."
                    off "It may be harsh to say but I don't care about her in the slightest."
                    scene ep4_sc5_mcr_02
                    $ UnlockThat("ep4/ep4_sc5_mcr_02")
                    off "I should text her to let her know. How about that :"
                    mc "Hi, Kelly. I'm sorry but I won't meet you today."
                    mc "I weighed it some more and I honestly don't think that it would be a good idea."
                    mc "I'm sorry if I gave you false hope."
                    off "Sounds good."
                    off "Her reply comes faster than I anticipated."
                    off "I hoped she would just let it go silently."
                    off "It looks like I was wrong."
                    kf "Hi, [mc_name]. May I ask what made you reconsider our date?"
                    kf "Is it something I said?"
                    kf "You said I was cute..."
                    off "I hate this situation. Poor girl."
                    mc "You're one of the cutest girl I've ever seen, Kelly, don't doubt that."
                    mc "It's not your fault."
                    mc "It's just me. I'm sorry."
                    off "She keeps silent long enough for me to wonder if the conversation is over or not."
                    kf "I understand."
                    kf "I'm sorry [mc_name]."
                    kf "I guess I deserve this."
                    kf "I won't bother you any further."
                    kf "Goodbye, [mc_name]."
                    mc "Goodbye, Kelly."
                    off "Her texts sounded so sad and lonely."
                    off "I feel like I hurt her."
                    off "I'm such an asshole..."

    elif ep4morningkftold == True and ( ep3kfgfmeetaccepted == True or ep3kfmeetaccepted == True ):
        $ ep4kfknown = True
        if ep4kfmorninglie == True:
            off "I lied to the girls."
            off "What the fuck was I thinking?"

        off "Dating Kelly was a seductive idea yesterday but now, it's a different story."
        off "She's the bitch who ruined [sis_name] and [sf_name]'s high school life."
        off "She's obviously crazy and was clearly ill-intended contacting me."
        off "I have to cancel my date with Kelly before she calls me."
        off "Let's text her."

        scene ep4_sc5_mcr_02
        $ UnlockThat("ep4/ep4_sc5_mcr_02")

        menu:
            "I should be careful with what I say. [gr]\[CanceledGently\]":
                $ ep4kfmeetingcanceledgently = True
                off "Don't let her know we're aware she's a cunt."
                off "How about that :"
                mc "Hi, Kelly. I'm sorry but I won't meet you today."
                mc "I weighed it some more and I honestly don't think that it would be a good idea."
                mc "I'm sorry if I gave you false hope."
                off "Sounds good."
                off "Her reply comes faster than I anticipated."
                off "I hoped she would just let it go silently."
                off "It looks like I was wrong."
                kf "Hi, [mc_name]. May I ask what made you reconsider our date?"
                kf "Is it something I said?"
                kf "You said I was cute..."
                off "Yeah, you're cute. The cutest evil bitch."
                mc "You're one of the cutest girl I've ever seen, Kelly, don't doubt that."
                mc "It's not your fault."
                mc "It's just me. I'm sorry."
                off "She keeps silent long enough for me to wonder if the conversation is over or not."
                kf "I understand."
                kf "I'm sorry [mc_name]."
                kf "I guess I deserve this."
                kf "I won't bother you any further."
                kf "Goodbye, [mc_name]."
                mc "Goodbye, Kelly."
                off "Her texts sounded so sad and lonely."
                off "I feel like I hurt her."
                off "Maybe we misjudged her?"
                off "Fuck, why does it have to be so complicated?"
            "Lets be as clear as possible with that bitch. [gr]\[CanceledAsshole\]":

                $ ep4kfmeetingcanceledasshole = True
                mc "Hey, bitch."
                mc "Our date is canceled."
                mc "I just learned who you really are."
                mc "Don't bother replying."
                off "Sounds good."
                off "Her reply comes faster than I anticipated."
                off "I hoped she would just let it go silently."
                off "It looks like I was wrong."
                kf "Excuse me?"
                kf "[mc_name], I don't understand."
                kf "What happened?"
                off "Oh, you don't understand, bitch, let me explain."
                mc "Turns out [sf_name], [sis_name] and I are talking to each other."
                mc "They told me everything."
                mc "Whatever you're scheming, it won't work."
                off "Her next reply takes some time to reach me."
                kf "I'm sorry, [mc_name]."
                kf "I wanted to tell you everything during our date."
                kf "It was a mistake, I should have told you yesterday."

                kf "Yes, I know [sis_name] and [sf_name]."

                kf "And yes, I did terrible things, I lied and peddled rumors to hurt their reputations."
                kf "You don't have to believe me but I swear, I was about to confess everything and apologize to you today."
                kf "That's also why I wanted to meet you."
                kf "Apologizing is something I prefer to do face to face rather than over the phone."
                kf "I know it's hard to believe but I'm not the person who did all these things anymore."
                kf "I've changed."
                kf "I'm trying to be better."
                off "Ok... It's hard to believe, but it's plausible."
                off "I could even say it's pretty convincing."
                off "But she's lying. Obviously."
                off "I still feel bad for insulting her."
                off "Come on [mc_name], she's lying, you know it."
                off "It's a trap."
                mc "Kelly, I want to believe you, but it's very hard for me to trust you."
                mc "I apologize for calling you names, it wasn't very mature of me."
                mc "However, I won't meet you."
                mc "Your personality adjustment is nice but still a bit too fresh.. I'm sorry."
                mc "Have a nice day."
                off "She keeps silent long enough for me to wonder if the conversation is over or not."
                kf "I understand."
                kf "I'm sorry [mc_name]."
                kf "I guess I deserve this."
                kf "I won't bother you any further."
                kf "Goodbye, [mc_name]."
                mc "Goodbye, Kelly."
                off "Her texts sounded so sad and lonely."
                off "I feel like I hurt her."
                off "Maybe we misjudged her?"
                off "Fuck, why does it have to be so complicated?"
                off "Why do I feel so bad?"
            "Wait a minute. [kellyPath]":

                $ ep4kfmeetingok = True
                off "This could be an opportunity."
                off "Maybe I can learn something by meeting Kelly and having her talk to me?"
                off "She probably has no idea I know who she is."
                off "That means I have the advantage."
                scene ep4_sc5_mcr_00
                $ UnlockThat("ep4/ep4_sc5_mcr_00")
                off "Let's call her."
                scene ep4_sc5_mcr_01
                $ UnlockThat("ep4/ep4_sc5_mcr_01")
                kf "[mc_name]?"
                mc "Hello, Kelly."
                $ ProcessStat(5, "kf_affection")
                $ DumpNotStack()
                kf "Hello, [mc_name]!"
                kf "I'm so happy you called me!"
                off "Her voice is sweet and clear."
                mc "I was getting impatient so I decided to take the initiative."
                mc "I hope you don't mind."
                kf "I'm actually delighted to hear your voice."
                mc "I could say the same thing."
                mc "I like your voice."
                mc "It's just how I have been imagining it."
                kf "I'm glad you like it."
                kf "So... Tell me... Do you still want to meet?"
                mc "More than ever, Kelly."
                mc "I thought that maybe we could have a drink, or whatever, somewhere?"
                kf "That would be great!"
                scene ep4_sc5_mcr_01_plus
                mc "Do you have any preference?"
                kf "Can you wait a second [mc_name]?"
                mc "Sure..."
                off "The line goes totally silent for a few seconds."
                kf "[mc_name]?"
                mc "Yes."
                kf "I'm a very simple girl."
                kf "I don't need anything fancy."
                kf "There's a coffee shop I like."
                kf "I'll send you the address if you're okay..."
                mc "That would be perfect."
                kf "Great!"
                kf "I'm gonna hit the bathroom to get decent and I'll see you there."
                kf "At noon?"
                mc "At noon."
                kf "I hope you won't be disappointed."
                kf "I'm really looking forward to meeting you."
                mc "That's my line."
                kf "See you later!"
                mc "See you later Kelly."
                off "She hangs up."
                off "That was easy."
                off "How come I didn't manage to get a single girlfriend during high-school?"
                off "Shit, I’m so dumb."
                off "If the girls ever know anything about this, it will be the end of me."
                off "I will have a hard time explaining to them that I'm actually going to date their... cute... arch-enemy... for their own sake."

    scene black with dissolve
    with Pause(2)
    scene ep4_sc5_mcr_03
    off "I spend some time trying to get my thoughts in order, with little to no success."

    if sf_love_path == True:
        if ep4sfmorningsorry == True:
            off "[sf_name] crying on my shoulder was very... moving..."
            off "This girl is so much more than she seems to be."
            off "I wasn't expecting her to be so demonstrative..."
            off "It was a bit surprising and embarrassing when she jumped on me this morning."
            off "But it was totally different later, in the living room."
            off "It was... pleasing."
            off "When I've told her that what makes her happy makes me happy, it was just a figure of speech."
            off "But I realize now that... Seeing her happy really pleased me..."
            off "And then she cried..."
            off "Her tears broke my heart."
            off "Fuck, it's so cliché."
            off "That was a very strange moment."
            off "She said she was crying out of happiness."
            off "Did I make her that happy?"
            off "She may look tough, cold, maybe even a bit elitist, but in the end, she's just like [sis_name], a girl who has been harassed and abused for three years."
            off "I flirted with her because she's beautiful, attractive, her body is to die for and so on... But now I feel like... things are different."
            off "Am I falling for her? Like, truly?"
            if sis_love_path == True:
                off "What the fuck [mc_name]?"
                off "You're about to break up with her because you want to be with [sis_name]."
                off "Now is not the time to fall for her."
                off "I feel so weird saying that."
                off "Things already weren't easy, and they just got even more complicated."
                off "I'm so dumb."
        if sis_sub_path:
            off "[sis_name] hasn't said a thing but she looked pretty desperate when [sf_name] jumped on me in the hallway."
            off "We haven't talked about it yet but I guess we'll have to."
            off "I'll eventually have to make a decision."
            off "Do I want to... cultivate what's growing between [sis_name] and me?"
            off "Or do I prefer to focus on my relationship with [sf_name]?"
            off "Fuck."
            off "Why is it so difficult to simply imagine making a choice?"
    if sis_sub_path == True:
        off "What happened last night in the kitchen... that has gone way behind my wildest expectations."
        off "I mean... masturbating with [sis_name] on Sunday night was great but that Monday, we simply took it to a whole new level."
        off "I licked her pussy!"
        if ep3sisdoubleorgasm == True:
            off "And she sucked my dick!"
        if ep3perfectsub == True:
            off "She even swallowed my cum!"
        off "And not only that, but the way it occurred..."
        off "She completely submitted to me."
        off "I still have trouble understanding how we come to that, where I've found the balls to suggest it and why did she agree to it..."
        off "However, something seems pretty clear: Sunday, we were just playing a weird game but last night... we initiated a relationship."

    if sf_dom_path == True:
        off "I'm such a failure."
        if ep3ballscrushed == True:
            off "I should have told [sf_name] that I wasn't interested in playing her games."
        else:
            off "I should have told [sf_name] that I wasn't sure I liked her games..."
        off "My mind has gone completely blank when she made me smell her pussy."
        off "Holy shit, that was hot."
        off "And a bit gross."
        off "But shit it was so hot!"
        off "She'll give me her pussy if I behave well!"
        off "She may be crazy but it clearly worth a shot."
        off "I can't wait!"

        if sis_love_path == True:
            off "Fuck, [mc_name]!"
            off "Listen to yourself."
            off "You were about to break up with her because you want to be with [sis_name]."
            off "Have you lost your mind?"
            off "The situation with [sis_name] is already weird enough."
            off "You can't just fuck [sf_name] under her nose hoping she won't notice anything."
            off "First, it's totally fucked up."
            off "Only the king of assholes would do something like that."
            off "Second ... you won't get away with this, it's obvious..."
            off "You have to choose, [mc_name]."
            off "Do you truly want to be with [sis_name]?"
            off "Or do you want to play [sf_name]'s Games?"
            off "Fuck."
            off "Why is it so difficult to answer that question?"

        if sis_sub_path == True:
            off "However, I should be especially careful."
            off "If [sf_name] discovers what I'm doing with [sis_name]..."
            off "It could quickly get.. Complicated..."
            off "I'll eventually have to make a decision."
            off "Do I want to... cultivate what's growing between [sis_name] and me?"
            off "Or do I prefer to focus on my relationship with [sf_name]?"
            off "Shit."
            off "It’s actually difficult to simply imagine making a choice."

    if ep3sisluked == True:
        off "Fuck."
        off "He’s going to destroy her tight little pussy."
        off "Find something [mc_name], find something!"
        off "Come on, you’re a smart guy, you must find something."
        off "[sf_name] seems to think that I just have to be nice with [sis_name] to get her to listen to me but I don’t see how it could even be possible."
        off "She doesn’t give a shit about what I say."
        off "I could apologize."
        off "I’m pretty sure I already tried that at some point."
        off "And it didn’t work."
        off "I could try again, but aside from hurting my self-esteem, I don’t think it’ll do anything."
        off "But at least, I can try."
        off "I can tell her I’m sorry for..."

        off "Not being a good friend."

        off "Ask for another chance?"
        off "This is silly."
        off "She’s gonna laugh at me."
        off "Maybe I can do something."
        off "But what?"
        off "Buying her a gift or something?"
        off "Maybe some flowers?"
        off "That’s ridiculous."
        off "Come on, [mc_name]."
        off "What do you know about her?"
        off "What does she like?"
        off "I have actually no idea..."
        off "I know she enjoys spending time with [sf_name]."
        off "I know she fancies having a drink."
        off "I also know what kind of beer she likes."
        off "What can I do with that?"
        off "Offer her to drink her stupidity into oblivion?"
        off "This is hopeless."
        off "Maybe should I call mom."
        off "I could say that I’m worried, tell everything that happened..."
        off "She will come back immediately without a doubt."
        off "[sis_name] will be pissed off."
        off "She’ll probably be confined to the house until the end of summer."
        off "It’ll be difficult to explain why I didn’t call sooner, though."
        off "I should have done it sooner."
        off "Crap."
        off "If I call mom now I may very well end having problems myself."

    if full_neutral_path == True:
        off "That date with Kelly will be my first ever date with a girl."
        off "I have no idea how to behave."
        off "I guess I'll just try to... be myself."


    scene ep4_sc5_mcr_04
    if sis_hate_path == True:
        off "[sis_name] enters my room as I’m still trying to prevent my brain from overheating."
        sis "[mc_name], we’re leaving."
        mc "You’re leaving?"
        off "She stares at me as I lie on the bed."
        off "I must look like crap for her to give me that kind of look."
        sis "Are you ok?"
        off "Why do you care?"
        scene ep4_sc5_mcr_04_plus
        $ UnlockThat("ep4/ep4_sc5_mcr_04_plus")
        menu:
            "Why wouldn't I be?":
                $ ep4siswgoodanswer = True
                sis "I don't know."
                sis "You're lying here, holding your head like you're in pain..."
                mc "I'm not in pain."
                mc "I was just ... thinking about things."
                sis "Ok..."
                sis "So..."
                sis "We're going to [sf_name]'s home."
                sis "We're taking the car."
            "I'm fine. [assholePath]":
                mc "I'm just trying to... solve a problem."
                sis "Ok..."
                sis "So..."
                sis "We're going to [sf_name]'s home."
                sis "We're taking the car."

        off "Remember, [mc_name]. It's your last chance."

        menu:
            "Yeah, yeah. Take it.":
                mc "It's not like you're going to listen to what I have to say anyway."
                mc "Just take it."
                $ ProcessStat(-1, "sis_affection")
                $ DumpNotStack()
                off "She doesn't even reply and leaves the room."
                off "Just as I expected."
                off "I'm kind to her and she doesn't give a fuck."
            "Sure. [sisLovePath]" if ep4siscargoodanswer == True:
                mc "Call me if you have any problem, ok?"
                off "That's ridiculous."
                off "What problem could she encounter?"
                off "She seems to thinks the same as she seeks something to reply."
                $ ProcessStat(1, "sis_affection")
                $ DumpNotStack()
                sis "Ok... See you later then."
                mc "Yup."
                off "She hesitates for a few seconds."
                scene ep4_sc5_mcr_05
                sis "You're sure you're alright?"
                off "Do I look sick or something?"
                mc "I'm fine, I told you. Don't worry."
                sis "Ok..."
                off "She leaves the room and I go back to my thoughts."
                off "How can I repair my relationship with her?"

        jump ep4sc8
    else:

        off "[sis_name] enters my room as I’m still trying to prevent my brain from overheating."
        sis "[mc_name], we’re leaving."
        mc "You’re leaving?"
        off "She stares at me as I lie on the bed."
        off "I must look like crap for her to give me that kind of look."
        sis "Are you ok?"
        off "I can hear [sf_name] right behind her, waiting in the hallway."
        scene ep4_sc5_mcr_04_plus
        $ UnlockThat("ep4/ep4_sc5_mcr_04_plus")
        mc "I'm fine."
        mc "Don't worry."
        mc "Steve would say I just spend too much time thinking."
        sis "Ok then..."
        sis "Are you coming with us?"
        mc "Where to?"
        sis "[sf_name]'s house."
        sis "We talked about this during breakfast."
        sis "Are you sure you're alright?"
        scene ep4_sc5_mcr_05
        off "I almost forgot."
        if ep4kfmeetingok == True:
            mc "I remember."
            mc "I'm sorry, something else has come up."
            mc "I'll see you later."
            off "She seems a little bit surprised."
            sis "Ok... Something important?"
            off "Fuck. Am I going to lie to her?"
            if sis_sub_path == True:
                off "It's like a direct breach of the contract I implicitly formed with her last night."
            off "What the hell am I doing?"
            off "Why am I doing that?"
            mc "Not really, but I have to do it anyway..."
            sis "Ok..."
            off "She hesitates."
            off "She obviously wants to know more but doesn't dare to ask."
            off "I'd better prepare myself answering those questions later."
            sis "So... We wanted to take the car..."
            sis "Do you need it?"
            off "If they take the car, I'll have to use the bus to go meet Kelly."
            mc "I'll take the bus, or maybe I'll call an uber or something."
            mc "Don't worry."
            mc "Call me if you have any problem, ok?"
            sis "See you later then."
            mc "Yup."
            off "She hesitates for a few seconds."
            sis "You're sure you're alright?"
            off "Do I look sick or something?"
            mc "I'm fine, I told you."
            mc "Don't worry."
            sis "Ok..."
            off "She leaves the room and I go back to my thoughts."
            off "Without the car, I'll have to leave immediately if I don't want to be late."
            jump ep4sc7
        else:
            mc "Yeah, sure."
            mc "Let's go."
            mc "And I'm alright, you don't need to worry."
            off "I get up from the bed and stretch a bit."
            off "I need to focus on the moment."
            off "Steve is actually right."
            off "If I think too much, I can't enjoy the moment."
            off "Let's YOLO this for a bit."
            mc "Let me grab my wallet and my phone and I'm ready to go."


label ep4sc6:
    scene black with fade
    with Pause(2)
    show text "Half an hour later."
    with Pause(2)
    scene ep4_sc6_c_00 with fade
    $ UnlockThat("ep4/ep4_sc6_c_00")
    $ ep4gonewithgirls = True
    off "[sf_name] lives in a relatively small house in a very pricey neighborhood."
    off "The house itself is an old building, fully renovated."
    off "It’s not big but it's luxurious."
    off "My dad being a doctor and my mom a paralegal, they make a pretty good living."
    off "But [sf_name]’s dad seems to be playing on a whole different level."
    off "The girls prepare a bag of clothes while I wait in the living room."
    off "[sf_name] actually called it a reading nook."
    scene ep4_sc6_c_01
    $ UnlockThat("ep4/ep4_sc6_c_01")
    sis "Hey."
    mc "Hey."
    sis "[sf_name] is on the phone with her father."
    mc "Ok."

    if sf_love_path == True:
        if ep4sfmorningsorry == True:
            scene ep4_sc6_c_02
            $ UnlockThat("ep4/ep4_sc6_c_02")
            sis "So, wanna seize this moment to tell me what the fuck you did to her this morning?"
            sis "What did you tell her to have her crying like that?"
            mc "Nothing."
            mc "She was happy, we kissed and suddenly she was crying."
            mc "I swear, I didn't do anything."
            scene ep4_sc6_c_03
            sis "You must have said something."
            sis "I've known her for three years, I haven't seen her cry once."
            mc "I don't know..."
            mc "She said that this kind of relationship was new to her and that she wasn't sure how to handle it well."
            off "[sis_name] and [sf_name] have a very strange relationship."
            off "They seem to care for each other more than friends should."
            off "Like if they were family."
            off "Or more."

        if sis_love_path == True:
            scene ep4_sc6_c_04
            $ UnlockThat("ep4/ep4_sc6_c_04")
            sis "When I saw her crying I thought for a moment that you might have said something to her... about us."
            mc "No, I didn't."
            mc "Did you find a way to tell her?"
            sis "No. You?"
            mc "Me neither."

            menu:
                "But I still think we should simply tell her.":
                    $ ep4choosenone = False
                    mc "As soon as we can."
                    sis "You're crazy."
                    sis "We can't tell anyone."
                    mc "Listen, if we don't tell her everything, we'll have to hide it from her, and as you said, she's not stupid."
                    mc "She'll find out."
                    mc "If we tell her... There's a chance she'll understand us."
                    mc "She may even be supportive."

                    sis "Oh, you think she'll support you cheating on her, with me, her best friend?"

                    mc "Of course not..."
                    mc "But I'm sure there's a possibility that she'll understand that... all of that is just... a bad combination of circumstances."
                    sis "That's crazy..."
                    sis "I don't know..."
                    sis "You may be right but... I just ... have no idea how to tell her."
                    sis "I'm so afraid she'll hate me afterward..."
                    mc "She'll hate us even more if we wait too long."
                    mc "I can tell her that you didn't know, that everything is my fault."
                    sis "Well, that's very considerate of you, but we can't do that."
                    sis "I can't lie to her."
                    sis "It's already hard enough not telling her everything, I don't want to add another lie on top of that."
                    scene ep4_sc6_c_05
                    mc "Hey, it's not easy for me neither."
                    mc "She was so happy this morning... I felt like trash just looking at her."
                    mc "I'm betraying her."
                    sis "I know that."
                    sis "Just give me some time, please, I need to tell her myself."
                    mc "We'll do what you want."
                    sis "Thank you."
                "This morning was very difficult to handle. [blue]\[Harem Path?\]":

                    $ ep4choosenone = True
                    mc "She was so happy..."
                    mc "I felt like trash just looking at her."
                    mc "And it was so... strange... I don't know how to explain it.. but I hate myself at so many levels..."
                    scene ep4_sc6_c_06
                    $ UnlockThat("ep4/ep4_sc6_c_06")
                    sis "I hate myself too."
                    sis "She's my only friend, and I'm deceiving her."
                    sis "I'm a monster."
                    mc "No, you're not. Or maybe we're both monsters."
                    off "She stays silent for quite a few seconds before speaking with a very faint voice."
                    sis "I've thought of a fairly simple solution."
                    mc "I'm listening."
                    sis "You could... choose her."
                    mc "What do you mean?"
                    sis "You choose her... and we forget I came to your room."
                    mc "You're not serious."
                    sis "I am."
                    mc "Then I have a very simple solution myself."
                    mc "I can choose none."
                    mc "That would be even better."

            scene ep4_sc6_c_07
            $ UnlockThat("ep4/ep4_sc6_c_07")
            off "I try to reach out to her but she immediately gets away from me."
            sis "What do you think you're doing?"
            mc "I just wanted to hug you..."
            sis "Yeah, sure. I know exactly what you're trying to do, perv."
            sis "[sf_name] can come back anytime."
            sis "Don't do anything foolish."
            mc "Alright... I'll hug you later then."
            sis "Yeah... Later."
            scene ep4_sc6_c_13
            $ UnlockThat("ep4/ep4_sc6_c_13")
            off "A few minutes later, [sf_name] joins us."
            sf "I'm ready guys."
            sf "I hope you didn't wait too long."
            sis "Don’t worry about it."
            sis "Let's go. I’m hungry."

        elif sis_sub_path == True or ep3sissubrejected == True or ep3sissubrejected2 == True:
            scene ep4_sc6_c_02
            $ UnlockThat("ep4/ep4_sc6_c_02")
            sis "I warned you that I would kill you if you hurt her."
            sis "It still stands."
            mc "Of course it does."
            mc "Don't you have anything else to tell me?"
            sis "Me? What do you mean?"
            mc "I feel like I owe you an explanation."

            if sis_sub_love_path == True:
                mc "Maybe even an apology."

            sis "Oh, I'm eager to ear that..."
            mc "What are your thoughts about [sf_name] and me?"
            sis "I already told you."
            sis "It's your life."
            sis "You do what you want."
            sis "If you hurt her I'll kill you."
            mc "Yeah, I think I already heard that."
            mc "However, you seemed a bit depressed this morning when [sf_name] kissed me in the hallway..."
            sis "I don't know what you're talking about."

            menu:
                "It doesn't change anything for you and me.":
                    if ep3sissubrejected == True or ep3sissubrejected2 == True:
                        $ ep4subbadfail = True
                        scene ep4_sc6_c_08
                        sis "What the fuck are you talking about?"
                        sis "There is no you and me."
                        sis "I told you last night: that thing we've done, it was a mistake and it'll never happen again."
                        sis "Is there something you don't understand?"

                        sis "I'm your father's ward, you goddamn pervert."

                        sis "Whatever your kink is, I'm not into it."
                        off "Ok... Obviously, she still holds a grudge towards me."
                        mc "So I guess you're still mad at me?"
                        scene ep4_sc6_c_09
                        $ UnlockThat("ep4/ep4_sc6_c_09")
                        sis "You bet I am."
                        mc "What can I..."
                        sis "This discussion is over."
                        mc "Come on Princess..."
                        sis "I said, this discussion is over!"
                        scene ep4_sc6_c_31
                        $ UnlockThat("ep4/ep4_sc6_c_31")
                        off "She leaves the room."
                        off "I definitely fucked up yesterday."
                        off "It'll be hard to convince her to do anything with me now..."
                    else:
                        $ ProcessStat(1, "sis_submission")
                        $ DumpNotStack()
                        scene ep4_sc6_c_08
                        sis "You're right, it doesn't change anything: there is no you and me."
                        mc "Are you mad at me?"
                        sis "About what?"
                        mc "Not telling you about [sf_name]."
                        sis "Why should I be?"
                        mc "You know why."
                        scene ep4_sc6_c_09
                        $ UnlockThat("ep4/ep4_sc6_c_09")
                        sis "Ok. Listen to me, perv."
                        sis "That was fun."
                        sis "Disturbing, but fun."
                        sis "And as far as I'm concerned, it never happened."
                        sis "Do you understand?"
                        mc "Come on Princess, you can't deny that something is going on between us."
                        mc "Something strong."
                        sis "Nothing is going on."
                        sis "Nothing."
                        scene ep4_sc6_c_31
                        $ UnlockThat("ep4/ep4_sc6_c_31")
                        off "She gets up from the sofa and leaves the room."
                        off "She's mad at me."
                        off "And probably a bit jealous."
                        off "That sounded like a break-up but I didn't feel any anger in her voice, more like sadness."
                        off "The game is still on."

                "I should have told you last night. [sisLovePath] [sisSubPath]" if sis_sub_love_path == True:
                    $ ep4subgentletalk = True
                    sis "You don't have to tell me anything"
                    mc "I have to."
                    mc "I asked you to trust me."
                    mc "You can't trust me if I don't tell you everything."
                    $ ProcessStat(1, "sis_affection")
                    $ ProcessStat(1, "sis_submission")
                    $ DumpNotStack()
                    sis "Then go ahead, and tell me."
                    scene ep4_sc6_c_10
                    $ UnlockThat("ep4/ep4_sc6_c_10")
                    off "I move closer to her and put a hand on her leg."
                    off "My fingers slowly slide between her thighs."
                    off "She doesn't protest."
                    off "I can feel she even hesitates to open her legs more to make way for me."
                    mc "Last night, hours before I met you in the kitchen, I shared a moment with [sf_name]."
                    mc "We like each other."
                    mc "We kissed."

                    if ep3sfhandjob == True:
                        mc "She gave me a handjob."

                    mc "I should have told you as soon as I've seen you but the truth is I just forgot about it."
                    mc "You were there, sitting on the counter and once I saw you, nothing else was important, nothing else existed."
                    mc "Just you."
                    mc "And I wanted you."
                    $ ProcessStat(1, "sis_affection")
                    $ ProcessStat(1, "sis_submission")
                    $ DumpNotStack()
                    mc "You know it's difficult to think straight when... you're aroused..."
                    mc "And you have that effect on me."
                    mc "I don't know why, but you're arousing me, to the point that my mind goes completely blank."
                    mc "I can only think of one thing."
                    mc "You."
                    sis "You're telling me that you were so horny seeing me sitting on the counter that you forgot to tell me about you and [sf_name]?"
                    sis "If this is supposed to be a compliment, you may reconsider your arguments."
                    mc "No, it's not a compliment."
                    mc "It's just how it is."
                    scene ep4_sc6_c_11
                    $ UnlockThat("ep4/ep4_sc6_c_11")
                    off "My fingers are getting closer to her crotch as my other hand gently strokes her back."
                    off "She doesn't even tense under my touch."
                    off "She accepted it."
                    off "Her breathing accelerates."
                    sis "Are you trying to make me responsible for that?"
                    mc "No, I'm not trying anything besides telling you the naked truth."
                    mc "It may not be pretty, it may not be nice, but it's the truth."
                    mc "I didn't tell you about [sf_name] because I simply didn't think about her when I was with you."
                    mc "Does that make me a monster?"
                    off "She hesitates and looks away."
                    sis "I don't know..."
                    mc "Do you regret what we did last night?"
                    sis "I... don't know..."
                    mc "Did you enjoy it?"
                    sis "... I don't want to answer that."
                    scene ep4_sc6_c_12
                    $ UnlockThat("ep4/ep4_sc6_c_12")
                    off "She leans against the sofa and stops my hand as I reach her pussy."
                    off "She doesn't push me away but rather keeps my fingers where they are: in the best position to massage her more intimates parts."
                    mc "Well, let me tell you something, Princess."
                    mc "Tonight, I will call you, and you will come to me."
                    mc "And the things I'll do to you and your sweet tight pussy will leave you drenched and exhausted."
                    mc "I'll take care of you and you will like it."
                    mc "Whatever happens, Princess, I'll be there for you."
                    mc "You can rely on me."
                    off "I can feel her pussy radiating heat through the denim of her shorts."
                    off "She’s literally burning."
                    off "I know she's wet."
                    off "If we keep going like this, she'll be drenching her shorts."
                    mc "I can still feel your lips around my dick."
                    mc "That gift you gave me last night, I liked it very much."
                    mc "I have to repay you for that."
                    mc "You'd better prepare yourself, Princess, I'll make you come so hard that you won't be able to walk for a while."
                    off "She lets out a moan."
                    off "I can feel that something is about to happen when the noise of [sf_name]'s footsteps in the hallway forces us to part."
                    scene ep4_sc6_c_13
                    $ UnlockThat("ep4/ep4_sc6_c_13")
                    off "She barely has the time to separate from me and get up from the sofa."
                    sf "I'm ready guys."
                    sf "I hope you didn't wait too long."
                    sis "It's ok! It's ok!"
                    sis "Let's go. I... I’m hungry."
                    off "Her eagerness is almost comical."
                    off "We'll talk again later, Princess, Don’t worry."
        else:

            scene ep4_sc6_c_02
            $ UnlockThat("ep4/ep4_sc6_c_02")
            sis "I warned you that I would kill you if you hurt her."
            sis "It still stands."
            mc "Of course it does."
            mc "Don't you have anything else to tell me?"
            sis "Me? What do you mean?"
            mc "What are your thoughts about [sf_name] and me?"
            sis "I already told you."
            sis "It's your life."
            sis "You do what you want."
            sis "If you hurt her I'll kill you."
            mc "Yeah, I think I already heard that."
            mc "However, you seemed a bit depressed this morning when [sf_name] kissed me in the hallway..."
            sis "I don't know what you're talking about."
            mc "Ok..."
            scene ep4_sc6_c_13
            $ UnlockThat("ep4/ep4_sc6_c_13")
            off "A few minutes later, [sf_name] joins us."
            sf "I'm ready guys."
            sf "I hope you didn't wait too long."
            sis "Don’t worry about it."
            sis "Let's go. I’m hungry."
    else:

        if sis_love_path == True:
            scene ep4_sc6_c_07
            $ UnlockThat("ep4/ep4_sc6_c_07")
            off "I try to reach out to her but she immediately gets away from me."
            sis "What do you think you're doing?"
            mc "I just wanted to hug you..."
            sis "Yeah, sure."
            sis "I know exactly what you're trying to do, perv."
            sis "[sf_name] can come back anytime."
            sis "Don't do anything foolish."
            mc "Come on, we'll hear her footsteps at least."
            sis "I don't care, I don't want to take the risk."
            sis "We'll have plenty of time... later."
            mc "Does that mean you will come to my room tonight?"
            sis "Will you shut up?"
            sis "[sf_name] could hear us!"
            mc "Maybe I should come to yours?"
            scene ep4_sc6_c_14
            $ UnlockThat("ep4/ep4_sc6_c_14")
            sis "Whatever you wish, as long as you stop talking about it."
            off "We keep silent for a few seconds."
            off "The mood of the conversation changes."
            mc "We'll have to hide it forever."
            sis "As long as there is an us, yes."

            menu:
                "Unless we run away.":
                    $ ep4runawaymention += 1
                    $ ProcessStat(1, "sis_affection")
                    $ DumpNotStack()
                    sis "What?"
                    sis "Come on, let's be serious."
                    sis "We won't run away."
                    mc "I am very serious."
                    mc "Or should I say, we should think about it thoughtfully if we are serious about having this kind of relationship."
                    sis "[mc_name]..."
                    sis "You can't let me be the realistic one here."
                    sis "Right now, we don't even know what really is going on between us."
                    sis "We may think it's love but..."
                    sis "Let's face it, we could be mistaking..."
                    sis "We're eighteen, this could be love, this could be .. pure hormonal rage or something like that."
                    sis "That could be some kind of psychological disorder, that could even be... just a phase."
                    sis "You don't run away for that kind of thing."

                    sis "You run away with the one you'll spend your life with, not with that girl you just kissed and hold in your arms for one night."

                    sis "In two weeks from now, we may very well be fed up with each other and go back to some... more... normal behavior..."
                    mc "You sound awfully pessimistic..."
                    scene ep4_sc6_c_15
                    sis "I'm not, really."
                    sis "We should take what we can, while we can... and be happy with it."
                    sis "It can't last forever."
                    mc "That way of thinking is so sad..."
                    sis "I'm not sad, I'm just trying not to hope too high."
                    sis "And you're not helping."
                    mc "Well, I'm sorry I guess..."
                    mc "You seemed more determined this morning..."
                    sis "And I still am."
                    sis "Don't doubt it."
                    off "I can hear [sf_name]'s footsteps in the hallway."
                    scene ep4_sc6_c_13
                    $ UnlockThat("ep4/ep4_sc6_c_13")
                    sf "I'm ready guys."
                    sf "I hope you didn't wait too long."
                    sis "Don’t worry about it."
                    sis "Let's go. I’m hungry."
                    off "I'm not sure how I feel about this conversation."
                    off "I don't know if it's pessimism or realism, but [sis_name] clearly seems way more mature than I am, at least on that subject."
                    off "She's probably right."
                    off "When did I become this foolish?"
                "It's exciting, don't you think? [sisLovePath] [sisSubPath]":

                    $ ProcessStat(1, "sis_affection")
                    $ ProcessStat(1, "sis_submission")
                    $ DumpNotStack()

                    sis "Exciting?"
                    mc "Yeah, the thrill of getting caught."
                    mc "Doing something forbidden..."
                    scene ep4_sc6_c_16
                    sis "I don't know... You're talking like a pervert."
                    mc "I didn't think about it before now but... I may want you.. even more.. because you're forbidden."
                    mc "That would explain why you're so irresistible to me."
                    sis "Because I'm irresistible?"
                    mc "You are."
                    mc "I think of you all the time, I want you all the time, anywhere, I want you here, and now."
                    $ ProcessStat(1, "sis_affection")
                    $ ProcessStat(1, "sis_submission")
                    $ DumpNotStack()
                    sis "Ok, perv, this discussion is getting very strange."
                    sis "I don't know how I should take it."
                    scene ep4_sc6_c_17
                    $ UnlockThat("ep4/ep4_sc6_c_17")
                    mc "Don't you feel it?"
                    sis "What?"
                    mc "That urge, to kiss you, to touch you, right here, right now."
                    mc "I mean, I always want to touch you, but it's stronger because we may get caught."
                    sis "You are crazy."
                    sis "You should calm down."
                    sis "There’s nothing we can do here."
                    sis "Save it for later."
                    mc "Really?"
                    scene ep4_sc6_c_18
                    $ UnlockThat("ep4/ep4_sc6_c_18")
                    off "We suddenly kiss, passionately, as I knock her over on the sofa."
                    off "I lie on her while we clutch each other."
                    off "She grabs my butt, I seize her breast."
                    off "It's perfectly shaped, firm and yet so soft."
                    off "I would want to appreciate it more but I can't."
                    off "My mind has just gone blank."
                    off "I'm nothing more than a beast."
                    off "My tongue invades her mouth, I can sense saliva dripping from our lips, mine, hers, it doesn't matter."
                    off "She pulls me by the hips until our crotches meet."
                    off "And then she pulls harder as if she wanted to force our bodies to merge into one, right here, right now."
                    off "I’m so hard that shorts are getting uncomfortably tight."
                    off "I grind my cock against her pussy."
                    off "Would we have been naked, I would have tried to penetrate her, and she would have accepted me."
                    off "She knows it."
                    sis "You're crazy!"
                    mc "You already said that."
                    scene ep4_sc6_c_19
                    $ UnlockThat("ep4/ep4_sc6_c_19")
                    off "I'm about to make my way under her shirt when she pushes me away."
                    off "I fall from the sofa and hit the table with my head."
                    off "She looks at me, trying to control her fear while wiping the saliva dripping from her chin."
                    off "I can hear [sf_name]'s footsteps in the hallway."
                    sis "Get up! Quick!"
                    off "I sit and try to act as if nothing happened."
                    off "I can feel my erection dripping precum like crazy."
                    off "I've never been that horny before."
                    off "I can feel the blue balls coming."
                    scene ep4_sc6_c_13
                    $ UnlockThat("ep4/ep4_sc6_c_13")
                    sf "I'm ready guys."
                    sf "I hope you didn't wait too long."
                    sis "It's ok! It's ok!"
                    sis "Let's go. I... I’m hungry."
                    off "Her eagerness is almost comical."
                    off "We'll talk again later, Princess, Don’t worry."

        elif ep3sissubrejected == True or ep3sissubrejected2 == True:
            $ ep4subgoodfail = True
            scene ep4_sc6_c_20
            off "She takes an open book on the table and randomly reads it."
            off "I take some time to contemplate her body."
            scene ep4_sc6_c_20_plus
            $ UnlockThat("ep4/ep4_sc6_c_20_plus")
            off "The more I look at her the more I think of what I'll do with her."
            off "Tonight, for sure, I'll make her moan and cry of pleasure."
            scene ep4_sc6_c_21
            off "I'm about to serve her my best naughty line when she brutally interrupts me without even giving me a look."
            sis "Don't."
            mc "Excuse me?"
            sis "You're about to say something, like that you want to destroy my pussy or something like that."
            sis "It wasn't funny last night, it's not funny today either."
            sis "I'm sorry if I wasn't clear enough: I don't want you to touch me, I don't want you to talk to me about that kind of thing, I don't want to have that kind of relationship with you."

            sis "I am your goddamn friend, nothing more."

            sis "We made a one time mistake, and it won't go any further."
            sis "You may not be happy with it but you'll have to deal with it."
            sis "I don't want to have anything to do with your sick fantasies."
            sis "Do you understand?"
            off "Her tirade completely takes me by surprise."
            mc "I .. I think so..."
            scene ep4_sc6_c_22
            sis "Great."

            sis "Now, just to be even clearer: I'm ok with being your friend, or even your sister."

            sis "I'm ok with you being my brother, and maybe we can even love each other as family."
            sis "I'm ready to make efforts on my side but it's now your responsibility to make this works."
            sis "You stop coming at me asking to empale my genitals on yours, you prevent yourself from annoying me with your sexual innuendos and we'll be cool."
            sis "Do you get it?"
            mc "Yeah..."
            sis "Perfect, bro."
            scene ep4_sc6_c_23
            $ UnlockThat("ep4/ep4_sc6_c_23")
            sis "I'm happy we cleared that up."
            off "Her smile completely obliterates my velleity of response."
            off "I'm not even sure of what just happened."
            scene ep4_sc6_c_24
            off "I have the impression I've been beaten to a pulp."
            off "Obviously, I won't fuck her..."
            off "But she's ok to have me as her brother.. if I refrain from bullshitting her."
            off "I don't know if it's a good deal or not."
            off "I don't feel like I have a choice anyway."
            scene ep4_sc6_c_13
            $ UnlockThat("ep4/ep4_sc6_c_13")
            off "A few minutes later, [sf_name] joins us."
            sf "I'm ready guys."
            sf "I hope you didn't wait too long."
            sis "Don’t worry about it."
            sis "Let's go. I’m hungry."

        elif sis_sub_path == True:
            scene ep4_sc6_c_20
            off "She takes an open book on the table and randomly reads it."
            scene ep4_sc6_c_20_plus
            $ UnlockThat("ep4/ep4_sc6_c_20_plus")
            off "I look at her for a while and can't help but focus on her exposed navel."
            off "I want to touch it."
            off "I want to play with it."
            off "I want to lick her."
            off "I remember the taste of her pussy on my tongue."
            off "It was delicious."

            if ep3sisdoubleorgasm == True:
                off "And the blowjob she gave me after that."
                off "It was magical."
                off "You gave me my first blowjob, Princess."
                off "That deserves a reward."

            off "After a while, she finally realizes I'm gazing over her."
            scene ep4_sc6_c_25
            sis "What?"
            mc "I'm remembering the taste of your pussy."
            sis "Great."
            sis "Could we avoid talking about that when [sf_name] could be back any moment now?"
            sis "I don't want her to know... what we did last night..."
            mc "You're right, it's better if we keep it a secret."
            mc "However, I need you to do something for me."
            mc "Now."
            off "She anxiously look at the door by which [sf_name] could come back."
            mc "Don't worry, Princess."
            mc "I just want you to rest on my lap."
            sis "To rest on your lap?"
            mc "That's what I said."
            mc "I want you to lie there and put your head on my lap."
            off "She hesitates."
            off "She bites her lips and closes her book before slowly taking the position."
            scene ep4_sc6_c_26
            $ UnlockThat("ep4/ep4_sc6_c_26")
            off "She obeys me."
            off "Her expression is still this mixture of fear and shame."
            off "And a bit of desire."
            mc "Isn't that comfortable?"
            off "She nods."
            mc "Great."
            off "I gently stroke her chin with the back of my fingers."
            off "Her skin is softer than silk."
            mc "Princess, you are beautiful."
            off "Her complexion subtly changes."
            sis "Oh... Ok..."
            scene ep4_sc6_c_27
            $ UnlockThat("ep4/ep4_sc6_c_27")
            off "I reach for her belly and slowly caress her."
            off "She tenses immediately as she gasps."
            off "Her breathing accelerates."
            off "I barely touch her with my fingertips, drawing circles around her navel."
            off "She shivers."
            mc "You like when I touch you, don't you?"
            off "She turns her head away from me."
            off "She may have accepted my touch but she's not ready to talk about it openly."
            mc "I like to touch you, Princess."
            mc "You have that effect on me."
            mc "I'm thinking about you, all the time."
            mc "About the things I want to do to you."

            menu:
                "Soon, I'll fuck your pussy. [sisSubPath]":
                    $ ProcessStat(2, "sis_submission")
                    $ DumpNotStack()
                    scene ep4_sc6_c_30
                    $ UnlockThat("ep4/ep4_sc6_c_30")
                    mc "I'll insert myself inside you."
                    mc "I'll fuck you so hard that your hips will crumble."
                    mc "Then, I'll take your ass."
                    mc "I'm sure you'll love anal."
                    mc "I'll destroy that tight little asshole."
                    mc "And once I'm done with it, I'll start over, again and again, and again."
                    mc "Until you beg me to stop."
                    off "She suddenly gets up from the sofa."
                    scene ep4_sc6_c_31
                    $ UnlockThat("ep4/ep4_sc6_c_31")
                    sis "I heard [sf_name]."
                    off "I didn't hear anything."
                    sis "I'll go see what she's doing."
                    off "She leaves the room immediately."
                    off "There's no point in trying to retain her."
                    off "Obviously, she didn't like what I just told her."
                    off "Or more likely, she didn't like the way I said it."
                    off "I'll have to be more careful next time."

                "I know there are things you're not ready to do, yet. [sisLovePath] [sisLoveSubPath]" if sis_sub_love_path == True:
                    $ ProcessStat(2, "sis_affection")
                    $ ProcessStat(2, "sis_submission")
                    $ DumpNotStack()
                    $ ep4subgentletalk = True
                    mc "You don't have to worry."
                    mc "You will be the one to ask me."
                    mc "You will beg me to enter you."
                    mc "You will feel every centimeter of my dick as I'll slowly penetrate you."
                    mc "Close your eyes."
                    scene ep4_sc6_c_28
                    mc "I want you to imagine it."
                    mc "My cock, hard as a rock, kindly sliding inside you."
                    mc "I'll give you it all."
                    mc "I will fill you completely."
                    mc "You can already feel it, can't you?"
                    mc "I'll be gentle at first, then I’ll pound you harder once you'll be used to it."
                    mc "You will love both."
                    scene ep4_sc6_c_29
                    $ UnlockThat("ep4/ep4_sc6_c_29")
                    off "She grabs her crotch and starts massaging it through her shorts."
                    mc "You naughty girl."
                    off "I move my hand towards her breast when the sound of [sf_name]'s footsteps in the hallway separates us."
                    mc "We'll pursue our discussion later, Princess."
                    mc "I promise you."
                    off "She looks away from me in shame."
                    scene ep4_sc6_c_13
                    $ UnlockThat("ep4/ep4_sc6_c_13")
                    sf "I'm ready guys."
                    sf "I hope you didn't wait too long."
                    sis "It's ok! It's ok!"
                    sis "Let's go. I... I’m hungry."
                    off "Her eagerness is almost comical."
                    off "We'll talk again later, Princess, Don’t worry."
        else:


            scene ep4_sc6_c_20
            off "She takes an open book on the table and randomly reads it."
            off "I'm searching for a subject to chat about but I can't find anything interesting enough to say."
            off "We end up waiting silently until [sf_name]'s return."
            scene ep4_sc6_c_13
            $ UnlockThat("ep4/ep4_sc6_c_13")
            sf "I'm ready guys."
            sf "I hope you didn't wait too long."
            sis "Don’t worry about it."
            sis "Let's go. I’m hungry."

    jump ep4sc9


label ep4sc7:
    scene black with fade
    with Pause(2)
    show text "An hour later."
    with Pause(2)
    $ ep4gonetokf = True
    scene ep4_sc7_c_00 with fade
    $ UnlockThat("ep4/ep4_sc7_c_00")
    off "The rendezvous is in a small coffee shop in the old center of the city."
    off "Small streets, shitty traffic, no place to park."
    off "Going there by car would already take me at least half an hour."
    off "Taking the bus would be faster if I didn't have to walk 10 minutes to reach the bus stop and 10 more to get to the place."
    off "I'm sweating like a dork when I enter the Coffee shop."
    off "And it's empty."
    off "I didn't mess up the address but I'm a few minutes late."
    off "Did I fuck up my first date by being late?"
    off "Maybe I should text her?"
    off "Ok, Calm down [mc_name]."
    off "Maybe she's late too."
    off "You should just wait a few more minutes, then eventually text her."
    off "Don't panic."
    scene ep4_sc7_c_01
    $ UnlockThat("ep4/ep4_sc7_c_01")
    off "I sit at a table and wait for about 10 minutes, playing with my phone under the gaze of a barista getting more and more impatient for me to order something."
    off "I'm about to text her when she finally enters the shop."
    scene ep4_sc7_c_02
    $ UnlockThat("ep4/ep4_sc7_c_02")
    off "Holy shit."
    off "She's actually a bit more than cute."
    off "She comes straight over to me with a shy smile on her face."
    scene ep4_sc7_c_03
    $ UnlockThat("ep4/ep4_sc7_c_03")
    kf "Hello, [mc_name]."
    kf "I'm sorry I'm late."
    kf "I took the bus thinking it would be easier not to have to search for a place to park, but in the end, it didn't work out so well."
    kf "I hope you didn't wait too long..."
    mc "It's ok, I also took the bus and was a couple of minutes late myself."
    scene ep4_sc7_c_04
    off "She sits at the table and the waiter immediately takes our order."
    kf "Thank you for coming. I wasn't sure you would be there."
    $ ProcessStat(5, "kf_affection")
    $ DumpNotStack()
    mc "I was the one to call you back, remember?"
    mc "That would have been a hell of a bad joke to call you and not be here to meet you."
    kf "Maybe."
    kf "But I wasn't talking about that."
    off "She hesitates a moment."
    kf "I haven't been totally honest with you, [mc_name]."
    kf "I was afraid that you would refuse to see me me otherwise."
    off "Is it revelations time already?"
    mc "Ok... Should I be upset? Or intrigued?"
    kf "I'll tell you everything, [mc_name]."
    kf "I could have told you over the phone but..."
    kf "It wouldn't have had the same weight."
    mc "I'm all ears..."
    kf "[mc_name]... I know [sf_name] and [sis_name]."
    kf "Three years ago, I was the one who started spreading rumors about them."
    kf "I'm sorry, I probably hurt you and your family doing so."
    kf "I wanted to apologize... for everything."

    if ep4kfknown == True:
        off "This is so weird."
        off "Obviously, she had no intention of hiding her identity."
        off "I should have known."
        off "She gave me her real name after all..."
    else:
        off "Well... This is unexpected."


    mc "[sis_name], And [sf_name], told me about you."
    mc "They were at your place last night."
    mc "You apologized to them too."
    off "She seems a bit surprised."
    kf "Ah, yes."
    kf "I finally found the courage to talk to them."
    kf "It wasn't easy."
    scene ep4_sc7_c_05
    kf "I'm so... ashamed of what I've done..."
    off "I don't know what to think."
    off "Last night, when [sf_name] and [sis_name] told me about this girl and her apology, I was adamant this was bullshit."
    off "But now that she's in front of me, this isn't so easy."
    mc "That's quite the radical change."
    mc "What made you... reconsider your position?"
    off "She seems more and more embarrassed."
    kf "Well... I... I'm in therapy but..."
    kf "Listen.. what I'm going to tell you..."
    kf "I'm not telling you this to make you feel sorry for me, or anything like that, ok?"
    kf "I've only told my therapist about this..."
    kf "I don't know what I should begin with..."
    off "She takes a sip of her iced chocolate then a deep breath."
    kf "Ok..."
    scene ep4_sc7_c_06
    $ UnlockThat("ep4/ep4_sc7_c_06")
    kf "I entered high school three years ago, just like you, I guess."
    kf "For maybe the first two years, I thought I was... the popular girl."
    kf "You know, the girl that everyone envies."
    kf "My dad had money, I had a large group of friends, plenty of boys longing for me."
    kf "I was invited to every party, every event, that kind of thing."
    kf "The last year should have been even greater."
    kf "I was the captain of the cheerleaders, my boyfriend, Brandon, was the captain of the football team..."
    kf "For many, it was probably the high school dream..."
    off "I get it, you were on top of the high school food chain, what else?"
    kf "But I finally realized that was only lies."
    kf "I had some problems last year."
    kf "My father left us and my mother felt ill."
    kf "Suddenly, I wasn't as wealthy as before."
    kf "I missed some time at school."
    kf "I also had problems with keeping my grades up and I asked my friends to help me with it."
    kf "I was... more upset than surprised, I think, when it became obvious that none of my friends even had a minute to spare."
    kf "In the meantime, I understood that [sf_name] and [sis_name] had what I was missing."
    scene ep4_sc7_c_07
    kf "I mean: their friendship is real."
    kf "They were there for each other."
    kf "Whoever needs it, the other is there to help."
    kf "I realized that I didn't have any of this."
    kf "I didn't have any real friends."
    kf "They were more like followers, tailing me only to take my place whenever I would fall."
    kf "And I was falling."
    kf "I started to have regrets."
    off "Isn't that called Karma?"
    mc "It must have been hard."
    mc "But you weren't alone, you had your boyfriend."
    kf "Kind of."
    kf "I turned to him and relied on him for a time."
    kf "It was ok for a while."
    scene ep4_sc7_c_08
    $ UnlockThat("ep4/ep4_sc7_c_08")
    kf "Just before the end of the year, he asked me to... fuck the entire football team... to show my support."
    mc "Oh..."
    off "What a fine gentleman."
    off "I'm not really surprised though."
    off "Brandon is the king of assholes."
    kf "I refused."
    kf "He simply dumped me and replaced me with a girl I once thought was a friend."
    kf "As far as I know, he fucked her a couple times before sharing her with the team."
    kf "She was ok with it."
    kf "I... I had a breakdown."
    off "Hence the therapy, I guess."
    mc "I'm sorry to hear this."
    kf "You have to understand."
    kf "I'm not complaining."
    kf "I know that this is probably just what I deserve."
    kf "I've been in therapy for almost two months now."
    scene ep4_sc7_c_06
    kf "I'm already feeling better."
    kf "I know that my life was basically crap."
    kf "I had no friends, I was probably the meanest of the cunts and I've hurt many people."
    kf "I wasn't a good person."
    kf "Everything is so different now that I'm trying to be a decent human being..."
    off "I have to admit that this is the kind of experience that could change your life and lead you to... rethink your priorities."
    off "It's far more convincing than the simple therapy explanation."
    off "But still..."
    mc "So .. you're basically starting a new life?"
    kf "Pretty much yes."
    kf "Yesterday I also invited my old... friends... as some kind of test."
    kf "I may be a bit harsh but... The more I see them, the more they disgust me."
    kf "Thinking I was one of them not so long ago makes me feel very uncomfortable."
    kf "But it's okay."
    kf "I don't really have any friends anymore, I'm basically alone."
    kf "I would have wanted to.. know better and maybe befriend [sis_name] and [sf_name], but I know it's impossible after what I've done to them."
    scene ep4_sc7_c_09
    kf "I'll wait to start anew next year in college."


    off "That sounds sad and lonely."

    menu:
        "But she deserves this. [gr]\[Kelly Compassion\]":
            off "It's payback for having been a cunt."
            $ ep4kfnocompassion = True
        "No one deserves this. [red]\[Kelly Compassion\]":

            "Not even after what she has done to [sf_name] and [sis_name]."
            $ ep4kfcompassion = True

    mc "It seems that you've been through a lot."
    mc "You seem to be strong and have good intentions now..."
    mc "I'm sure everything will be alright."
    kf "I... hope so..."
    mc "You didn't say any of that to [sf_name] or [sis_name]."
    kf "No."
    kf "As I said, I don't want anyone to pity me."
    mc "I can understand that..."
    mc "So..."
    mc "You said you had a crush on me..."
    mc "Was it just to have me coming here?"
    scene ep4_sc7_c_08
    kf "Ok, this is the moment where it becomes really embarrassing for me..."
    kf "Last year... at some point..."
    kf "Brandon briefly bullied a friend of yours."
    kf "You intervened."
    kf "Brandon is twice your size but you didn't seem to care."
    kf "I knew that Brandon was bluffing, but you didn't."
    kf "You called his bluff and he retreated, bragging he would break you next time but carefully avoiding you afterward."
    kf "That's when I understood that he was a coward."
    mc "I remember this happening."
    mc "To be honest, I was bluffing myself, Brandon would probably have crushed me easily."
    off "Actually, I was hiding a wrench in my sleeves in case things had gone south a bit too fast for my taste."
    off "And I also almost pissed myself."
    off "But hey, what she doesn't know doesn't hurt her, right?"
    scene ep4_sc7_c_09
    kf "That doesn't matter."
    kf "You were there for your friend."
    kf "I didn't fall for you just like that, however."
    kf "It's not that simple."
    kf "Later when.. my world started to fall apart, as I thought about [sf_name] and [sis_name], I also thought about you, and I observed you from time to time."
    kf "You seemed like a nice guy."
    kf "A bit of a doofus, too."
    kf "But a nice guy."
    kf "And you were the kind of guy who cared about his friends."

    kf "I was also aware that... I had destroyed your relationship with [sis_name]."

    kf "Again, I'm really sorry about that..."
    scene ep4_sc7_c_06
    kf "Now that I'm apologizing to almost everyone for having been the queen of cunts, I thought that I should apologize to you too.... and maybe see what happens."
    kf "Honestly, though, I doubt anything is possible after what I've done."
    kf "I understand it."
    mc "I don't know what to say, Kelly."
    mc "I'm a bit overwhelmed by all this."
    mc "I'm not really sure how to react."
    kf "I guess it's understandable."


    off "I'm searching for something smart and spiritual to say but nothing comes out."
    mc "So ... I guess you know that... [sis_name] had some problems with some of your friends..."
    kf "I'm so sorry about this."
    kf "It's not like them."
    scene ep4_sc7_c_07
    kf "Luke and Ray are a bit dumb and superficial, but I wouldn't say that they're bad or anything like that."
    kf "I've known them since I was a child."
    kf "Our fathers were working in the same company."
    kf "[sf_name] explained to me what happened, and Ray pleaded that it was a misunderstanding and that they did nothing."
    kf "I don't know what to do."
    kf "I was about to believe Luke and Ray but... they asked me a lot of questions about [sf_name] and [sis_name] after they've left the party."
    kf "I found it was weird and kind of an unhealthy obsession."
    kf "I refused to answer their questions."
    scene ep4_sc7_c_08
    kf "I... think it would be better if [sf_name] and [sis_name] avoided those two."
    kf "I'm so ashamed and confused to imagine that they could do something like that."
    mc "Well, it's not your fault I guess."
    mc "You're not responsible for their doing, are you?"
    mc "We intended to avoid them anyway."
    kf "I guess it's for the better."
    scene ep4_sc7_c_10
    off "She looks at her phone and sighs."
    kf "Time passes too quickly."
    kf "I'm sorry, I have to go."
    kf "My mom is in the hospital."
    kf "I'm going to visit her."

    off "Her dad is gone, her mother is hospitalized... is she living alone?"
    off "Her situation is even sadder than I thought."
    scene ep4_sc7_c_11
    $ UnlockThat("ep4/ep4_sc7_c_11")
    kf "Thank you for listening to me, [mc_name]."
    mc "You don't have to thank me for that."

    off "She seems to wait for something that I obviously fail to serve her."
    scene ep4_sc7_c_11_plus
    kf "I ... If .. If you want to see me again... Or just want to talk, or anything, really... You have my number, [mc_name]..."
    mc "Well... I really don't know what to think of all this."
    mc "But I'll keep that in mind."
    scene ep4_sc7_c_11
    mc "I'm pretty sure I won't be able not to think about you at some point in the coming days."
    kf "Goodbye, [mc_name]."
    kf "Goodbye, Kelly."
    scene ep4_sc7_c_12
    off "I look at her leaving the place."
    off "I've spent almost an hour talking with her, mostly listening actually, and I don't know what to think."
    off "She seemed sincere."
    off "Yet, she's a liar, good enough to convince an entire high-school that [sis_name] was sucking dicks in the restrooms."


    off "I'll have to think about that carefully."
    off "Should I talk with the girls about it?"
    off "They're going to kill me when they learn I've lied and come here without telling them."
    off "Kelly has barely left the coffee shop when my phone starts vibrating."
    scene ep4_sc7_c_13
    off "It's a text from [sis_name]."
    sis "We're going back home."
    sis "Will you eat with us?"
    sis "We're ordering at Royal Burger on our way back."
    mc "Sure. Get me a Royal Bacon menu please."
    sis "Ok. We'll be home in 30 minutes."
    mc "Thank you"
    sis "You're welcome."

    if sis_love_path == True:
        mc "I love you."
        $ ProcessStat(1, "sis_affection")
        $ DumpNotStack()
        sis "Hey! Don't write this!"
        sis "Anyone could've read my text."
        sis "[sf_name] could read this."
        mc "It's your phone, no one should read this."

        mc "Besides, I'm like a brother to you."

        mc "Your reaction is more suspicious than me loving you."
        sis "Yeah, yeah, whatever. Just stop, please."
        mc "As you wish Princess."
    elif sis_sub_path == True:
        mc "I'll reward you for this, Princess."
        mc "Do you prefer my tongue or my fingers?"
        $ ProcessStat(1, "sis_submission")
        $ DumpNotStack()
        mc "Maybe something else?"
        sis "You're crazy."
        mc "The whole package, then."
        sis "..."


    off "I should hurry."
    off "I'll have to run if I want to get on the next bus."

    jump ep4sc9


label ep4sc8:
    scene black with fade
    with Pause(2)
    show text "Half an hour later."
    with Pause(2)
    $ ep4mcalonehome = True
    scene ep4_sc8_mcr_00 with fade
    $ UnlockThat("ep4/ep4_sc8_mcr_00")
    off "The girls have been gone for half an hour now."
    off "I fapped to release some pressure hoping it would help me think more clearly but it wasn't a success."

    if ep2pantietaken == True:
        off "Turns out that jerking off using [sis_name]'s panties only makes me angrier."

    if ep2cameraset == True:
        off "I changed the camera's battery."
        off "I should be able to watch their next shower."

    off "I'm thinking about playing some games but I know I won't be able to focus."
    off "I still don't know what to do about this situation."
    off "I have to find something quick if I don't want this guy to fill up [sis_name]'s pussy."
    off "For all I know he's going to double team her with his brother."
    off "That slut will enjoy it for sure."
    off "I can't let that happen."
    off "Ok, calm down, [mc_name]."
    off "Once again. What are my options?"
    off "I can be nice to her."

    off "Maybe if I turn into that sweet loving friend [sf_name] wants me to be..."

    off "I don't know if it will be enough to convince her to behave better but I could give it a try, at least for a few hours..."
    off "Oh come on, I'm not gonna play [sis_name]'s kind little puppy even for a minute."
    off "I ain't submitting to that bitch."
    off "No way."
    off "What else? Come on [mc_name]!"
    off "I have this guy's phone number."
    off "I can call him."
    off "To do what?"
    off "To threaten him?"
    off "He won't give a shit about me."
    scene ep4_sc8_mcr_01
    off "I'm obviously not someone you fear."
    off "So what?"

    off "Am I going to beg him not to fuck [sis_name]?"

    off "Again, they won't give a shit about me."
    off "They're persistent."
    off "I would even say determined."
    off "They want something."
    off "Something else than just fucking [sis_name]..."
    off "But what?"
    off "Maybe if they get what they want they'll let us alone..."

    off "Yeah, let's do that, I'm going to call them, have a nice chat, ask them what they want to leave us alone and see if I can help them get it so that they disappear from [sis_name]'s life."

    off "If only it was so simple..."
    off "Fuck... maybe it is..."
    off "If I can bluff them a bit... they could..."
    off "That's impossible..."
    off "Nobody is that dumb..."
    off "Well, he was dumb enough to send her flowers and give her his phone number after failing to rape her..."

    off "So... What do I do?"
    menu:
        "I'll try to be nice to her.":
            $ ep4niceasshole = True
            off "I don't really have a choice here."
            off "It's the only valid option."
            off "Maybe I can even start right now."
            scene ep4_sc8_mcr_04
            $ UnlockThat("ep4/ep4_sc8_mcr_04")
            off "I can show her I care by sending her a text."
            off "Let's see, something simple."

            menu:
                "Hey Princess, how are you doing? [sisLovePath]":
                    mc "Is everything alright?"
                    sis "Everythings alright."
                    sis "Why do you ask?"
                    sis "Is there a problem?"
                    $ ep4gtext1 = True
                "Hey Princess, tell me you didn't crash the car.":


                    sis "Nope."
                    sis "I sold it to buy my meth."
                    sis "Is there a problem?"


            menu:
                "Nope.":
                    mc "Everything's good."
                    mc "See you later then."
                    sis "Yeah... later..."
                    $ ep4gtextexit == True

                "I just wanted to know. [sisLovePath]" if ep4gtext1 == True:
                    mc "Despite what you think, I care about you."
                    sis "Why are you telling me this right now?"
                    sis "Are you high or something?"
                    $ ProcessStat(1, "sis_affection")
                    $ DumpNotStack()
                    scene ep4_sc8_mcr_06
                    $ ep4gtext2 = True

                "... Great." if ep4gtext1 == False:
                    mc "I'm happy to know you're having fun."
                    sis "This time at least I didn't have to let the dealer fuck me in the ass to get my dose."
                    scene ep4_sc8_mcr_05

            if ep4gtextexit == False:
                menu:
                    "I'm just trying to be nice.":

                        sis "It's useless if you're not sincere."
                        scene ep4_sc8_mcr_05

                    "I know I can be an asshole... sometimes. [sisLovePath]" if ep4gtext2 == True:
                        mc "I'm sorry about that."
                        sis "What's gotten into you?"
                        sis "You're freaking me out."
                        $ ProcessStat(1, "sis_affection")
                        $ DumpNotStack()
                        scene ep4_sc8_mcr_06
                        $ ep4gtext3 = True

                    "Nice." if ep4gtext2 == False:
                        mc "So you won't have to suck his shitty dick either then."
                        sis "Glad to see you're as fun as ever."
                        sis "See you later, Perv."
                        scene ep4_sc8_mcr_05
                        $ ep4gtextexit = True

            if ep4gtextexit == False:
                menu:
                    "I just.. don't want to lose you completely. [sisLovePath]" if ep4gtext3 == True:
                        sis "This is so weird."
                        sis "You're making me uncomfortable."
                        $ ProcessStat(1, "sis_affection")
                        $ DumpNotStack()
                        scene ep4_sc8_mcr_06
                        $ ep4gtext4 = True
                    "Hey, I'm trying my best, ok?":

                        sis "I can see that."
                        sis "I appreciate the effort."
                        scene ep4_sc8_mcr_05

                menu:
                    "I may be a cunt, but I love you. [sisLovePath]" if ep4gtext4 == True:
                        sis "This is not funny."
                        sis "This discussion is over."
                        $ ProcessStat(2, "sis_affection")
                        $ DumpNotStack()
                        scene ep4_sc8_mcr_06
                        $ ep4textlove = True
                    "See you later, Princess.":

                        sis "Yeah... Later..."

            off "I... may have gone a bit overboard..."
            menu:
                "Being nice wasn't so hard, though. [sisLovePath]" if ep4textlove == True:
                    scene ep4_sc8_mcr_07
                    $ UnlockThat("ep4/ep4_sc8_mcr_07")
                    off "Telling her that I love her may even have been... kind of liberating..."
                    off "Not sure how she took, though."
                "That bitch.":
                    scene ep4_sc8_mcr_05
                    off "I tried as hard as I could."
                    off "Not sure it will be enough."

            off "Fuck, I'm going crazy with this shit."
            off "Let's play some games to change my mind."
        "This is completely crazy. [assholePath]":

            $ ep4lukephoned = True
            scene ep4_sc8_mcr_03
            off "What do I tell them?"
            off "Come on, [mc_name]."
            off "You'll improvise something."
            off "You have nothing to lose anyway."
            off "Ok, here is his number."
            off "Let's call it."
            scene ep4_sc8_mcr_08
            $ UnlockThat("ep4/ep4_sc8_mcr_08")
            off "Fuck, I can feel my guts liquefying."
            off "I may very well shit my pants soon."
            lk "Hey?"
            off "Someone picked up the phone on the other side."
            mc "Hey, I'm [mc_name]."
            lk "[mc_name] who? Do I know you?"

            mc "I'm [sis_name]'s friend."

            lk "Oh... Ok. What can I do for you, [mc_name]?"
            off "Alright, [mc_name]."
            off "You got this."
            off "Find something to say, quick."
            off "Confident tone."
            mc "I'm trying to decide what I should do about you."
            lk "About me?"
            mc "Yes."
            mc "[sis_name] may be naive as fuck, I'm not."
            mc "I know that you drugged her."
            mc "I know you want something."
            mc "I just don't know what."
            off "Not bad, [mc_name]."
            off "Keep up the firm and manly voice."
            lk "I don't know what you're talking about, [mc_name]."
            lk "[sis_name] is a nice girl, I like her very much."
            mc "Yeah, sure."
            mc "Listen, the only reason we didn't go to the police Sunday morning, is because [sis_name] wants my mother to see her as an independent and autonomous grown-up."
            mc "I played nicely until now but I'm fed up with this shit."
            mc "Surely, you know that my mom works with the police."
            mc "I'm going to hang up that phone and give her a call."
            mc "Before jumping on the first plane to come back here, she will give a few calls herself."
            mc "That means that in less than thirty minutes, you will have a bunch of officers looking for you in the streets."
            mc "Trust me, they will find you and they will put you in a tiny jail with some other rapists until they know for sure what your intentions are."
            off "My mom doesn't actually work with the police, and I highly doubt the rapist and tiny jail stuff is a decent description of how things work but..."
            off "That's the definition of a bluff, isn't it?"
            lk "You don't have any proof..."
            scene ep4_sc8_mcr_09
            off "Did I hear doubt or fear in his voice?"
            mc "That's the beauty of it."
            mc "I don't need any."
            mc "Finding evidence is the police's job."
            off "Still bluffing. But it seems to be working."
            off "The line stays silent for a few seconds."
            lk "What do you want?"
            off "Holy shit."
            off "It worked."
            off "I can't believe it worked."
            off "What do I say now?"
            off "Shit shit shit!"
            mc "I want to know your intentions."
            off "A few seconds of silence again."
            off "He's probably considering his options or speaking with his brother."
            lk "Why?"
            mc "Curiosity."
            off "Silence."

            lk "Why don't you just call the police, or your mom already?"
            off "Fuck."
            off "They're calling my bluff."
            off "You'd better find something incredibly smart to say, [mc_name]..."

            menu:
                "I'm interested in human psychology.":
                    scene ep4_sc8_mcr_10
                    mc "Depending on your motivations, I may call my mom, or simply ask you to get the fuck away from my family."
                    mc "I'm giving you a chance to get away before it's too late, don't miss it."
                    off "A longer silence."
                    off "Are they still on the line?"
                    lk "Listen, [mc_name]."
                    lk "I don't know what you're talking about."
                    lk "I think you should call your mother."
                    lk "I'll be glad to talk this out with her."
                    lk "I think I'll see you soon."
                    lk "Goodbye."
                    off "He hangs up without giving me a chance to reply."
                    scene ep4_sc8_mcr_12
                    off "Fuck."
                    off "This cunt saw through my bluff."
                    off "Now, they're clearly aware that I know they're up to no good and that I can't do anything against them."
                    off "Shit!"
                "I want to fuck her too. [assholePath]":
                    scene ep4_sc8_mcr_10
                    $ ep4lukephonedsuccess = True
                    lk "What?"
                    off "This is so fucking messed up."
                    mc "I want to fuck her too."
                    mc "So depending on your answers, I might denounce you or I might join you."
                    off "I'm so fucking stupid."
                    off "Am I going to gang-rape [sis_name]?"

                    lk "You're telling me that you would join us so you could fuck your friend?"

                    mc "Depending on what you want to do."
                    mc "And I want to be the first to fuck her."
                    lk "Are you serious?"
                    lk "Do I sound like I'm kidding?"
                    off "A longer silence."
                    off "Are they still on the line?"
                    lk "[mc_name], we won't answer your question, but we're interested."
                    lk "You'll have to prove your... sincerity first."
                    lk "If you do, we have no problem helping you get what you want."
                    mc "You want me to do something?"
                    lk "You will understand later."
                    lk "We'll see you soon, [mc_name]."
                    lk "Take care."
                    mc "... Ok..."
                    scene ep4_sc8_mcr_11
                    $ UnlockThat("ep4/ep4_sc8_mcr_11")
                    off "What the fuck did I just do?"
                    off "How am I going to get out this shithole?"
                    off "Why the fuck did I say that?"
                    off "How dumb can I be?"


    scene black with fade
    with Pause(2)
    show text "Half an hour later."
    with Pause(2)
    scene ep4_sc8_mcr_13
    off "My phone vibrates."
    off "It's a text from [sis_name]."
    sis "We're going back home."
    sis "Will you eat with us?"
    sis "We're ordering at royal burger on our way back."
    off "I'm actually quite surprised she cares to ask me."
    off "Maybe she doesn't hate me as much as I thought, after all."
    mc "Sure. Get me a Royal Bacon menu please."
    sis "Ok. We'll be home in 30 minutes."
    off "Is she... trying to be nice?"

    if ep4niceasshole == True:
        mc "Thank you, Princess."
        sis "You're welcome."

    off "30 minutes... Enough time to rub one I guess."


label ep4sc9:
    scene black with fade
    with Pause(2)
    show text "One hour later."
    with Pause(2)
    scene ep4_sc9_k_00 with fade
    $ UnlockThat("ep4/ep4_sc9_k_00")
    if ep4gonewithgirls == True:
        off "We stopped by the Royal burger on our way back home."
        off "[sis_name] was hungry."
    elif ep4gonetokf == True:
        off "The girls and I got back home almost at the same time."
    else:
        off "The girls came back with the promised food."

    off "The mood is good."
    off "The girls are joking about things I don't even understand."
    off "Matching shoes and underwear?"
    off "Who jokes about that?"
    off "I really can't understand them."

    off "That reminds me that we're not really a group of three."

    if sis_love_path == True or sis_sub_path == True:
        off "Three days ago, [sis_name] and I couldn't stand each other."
        off "Things... have changed."
        off "What is very disturbing is to think this is all because someone tried to rape her..."
        off "Maybe I should thank the guy."

    scene black with fade
    with Pause(2)
    show text "The middle of the afternoon."
    with Pause(2)

    scene ep4_sc9_pool_00 with fade
    $ UnlockThat("ep4/ep4_sc9_pool_00")
    off "It's something like 40°c outside, but it doesn't prevent the girls from chatting while lazily floating in the pool."

    if ep4niceasshole == True:
        off "I need to be nice to [sis_name]."
        off "I can't do it if I stay away from her."
        off "Let's create a situation where my kindness can shine."
        off "This idea of setting up a party for the three of us wasn't that bad."
        off "Let's try this."

    scene ep4_sc9_pool_01
    mc "Hey girls. How's the water?"
    sf "Hot. It's barely refreshing."
    mc "I figured as much."
    scene ep4_sc9_pool_03
    $ UnlockThat("ep4/ep4_sc9_pool_03")
    off "I do my best not to phase out into some sexual fantasy but it's so damn hard not to get some perverted thoughts."
    off "I mean... come on..."
    scene ep4_sc9_pool_02
    $ UnlockThat("ep4/ep4_sc9_pool_02")
    off "There's not a guy on this planet who wouldn't fantasize like crazy seeing this."
    off "The more I think about it, the less guilty I feel."
    off "That's just normal behavior for a normal human being."
    off "Now that I think of it, the girls themselves are probably fantasizing about my body, right now..."
    off "Ok, let's be honest, my body may not be as... perfect as theirs."
    off "But still..."
    off "I'm a decent specimen of the opposite sex."
    off "Alright, alright, [mc_name]."
    off "You're as fit as a shrimp."
    off "You should work out more."
    scene ep4_sc9_pool_01
    if ep4mcalonehome == True:
        mc "So girls..."
        mc "Do you have anything planned for tonight?"
        mc "I was thinking about buying a couple beers, maybe a bottle of syrah..."
        scene ep4_sc9_pool_04
        $ UnlockThat("ep4/ep4_sc9_pool_04")
        off "That expression on [sis_name]'s face, I don't know if it's incredulity, suspicion, maybe a bit of surprise..."
        sis "Are you serious?"
        sis "What's gotten into you?"
        mc "What do you mean?"
        sis "You're offering us to get drunk, on your money?"
        scene ep4_sc9_pool_05
        sf "He said nothing about getting drunk, he just talked about having a drink."
        sis "It's not like him anyway."

        menu:
            "I'm just trying to be nice and friendly. [sisLovePath] [sfLovePath]":
                mc "Sunday evening was fun so I thought that... we could do something like that again."
                $ ProcessStat(1, "sis_affection")
                $ ProcessStat(1, "sf_affection")
                $ DumpNotStack()
            "Well, maybe I'm not the asshole you think I am. [sisSubPath]":
                mc "I'm sure we can get along."
                $ ProcessStat(1, "sis_submission")
                $ DumpNotStack()

        sf "He just wants us to have fun together."
        sf "I don't think it's a bad idea."
        sf "A couple drinks won't hurt."
        sis "Yeah... I suppose so..."
        sf "We were thinking of spending the evening watching movies on the sofa."
        sf "You're welcome to join us, [mc_name]."
        scene ep4_sc9_pool_06
        $ UnlockThat("ep4/ep4_sc9_pool_06")
        mc "Great!"
        mc "I'll go to buy drinks and snacks later."
        mc "What are we watching?"
        sf "Well.. we were supposed to choose each one movie and make it a surprise for the other."
        sf "Why don't we play it boy vs girls?"
        sf "You choose a movie, we choose one."
        mc "That sounds fun."
        sis "I already know how it's going to turn out."
        sf "Did you hear the lady, [mc_name]?"
        sf "She thinks you're going to disappoint her."
        sf "It may be your chance to prove her wrong."
        mc "I'll do my best..."
        off "Like I even have a chance."
        off "She thinks I'm an asshole."
        off "Nothing will change her mind."
        off "It's obvious that whatever I do, it'll never be good enough for her."
        scene ep4_sc9_pool_07
        $ UnlockThat("ep4/ep4_sc9_pool_07")
        off "I spend some time in the pool."
        off "I try to partake in their discussion but with little success."
        off "[sf_name]'s obviously trying to help me but they're talking about things so stupid that I don't really know how to participate in their debate."
        off "They're talking about some girls books with unrealistic romance shit, like the modern charming prince coming to save a not so passive princess or something like that."
        off "I mean, seriously, who reads that kind of stuff?"
        off "However, I manage to feign interest."
        off "The girls leave the pool without incident."
        off "I'm pretty sure I've been a good boy."
        jump ep4sc11
    else:

        scene ep4_sc9_pool_05
        mc "So... Are we still up for that movie night?"
        sis "You bet we are."
        mc "Great. What are we watching?"
        sf "We were just talking about it."
        sf "We thought it could be fun to play it boy vs girls."
        sf "We choose a movie, you choose another one."
        mc "Sounds interesting."
        sis "I can feel that fast and furious movie coming hard."
        off "Fuck, she's reading me like an open book."
        sf "I'm sure he'll find something nice."
        sis "I have no problem watching an action movie once in a while by the way..."
        sis "I'm just saying that the outcome is obvious."
        mc "Who knows? I may surprise you."
        sis "I'm sure you'll do your best."
        mc "I'll go get a couple beers, and maybe a bottle of Syrah?"
        scene ep4_sc9_pool_04
        $ UnlockThat("ep4/ep4_sc9_pool_04")
        off "That expression on [sis_name]'s face, I don't know if it's incredulity, suspicion, maybe a bit of surprise..."
        sis "Do you want to get us drunk or something?"

        menu:
            "Absolutely. [sisSubPath] [sfDomPath]":
                mc "I'll get you both drunk and then abuse your body all night long."
                mc "I can't wait."
                mc "Maybe two bottles of syrah then?"
                $ ProcessStat(2, "sis_submission")
                $ ProcessStat(1, "sf_affection")
                $ ProcessStat(1, "sf_dominance")
                $ DumpNotStack()
                scene ep4_sc9_pool_06
                $ UnlockThat("ep4/ep4_sc9_pool_06")
                sf "One will be enough."
                sf "Thank you, [mc_name]."
            "Absolutely not. [sisLovePath] [sfLovePath]":
                mc "I was merely offering to have a drink or two."
                mc "But I can get some juice instead."
                $ ProcessStat(1, "sis_affection")
                $ ProcessStat(1, "sf_affection")
                $ DumpNotStack()
                mc "Or maybe some soda?"
                sis "No, it's okay... Beers will do fine."

        scene ep4_sc9_pool_08
        $ UnlockThat("ep4/ep4_sc9_pool_08")
        mc "Alright then."
        mc "I'll drop by the grocery store later."
        mc "I'll grab some snacks too."

        if sf_love_path == True:
            sf "It's settled then."
            scene ep4_sc9_pool_09
            $ UnlockThat("ep4/ep4_sc9_pool_09")
            off "[sf_name] approaches me with her heartbreaking smile once again."
            off "She's so beautiful when she's happy."
            off "If I wasn't really in love with her before today, seeing her smiling like that definitely crushed my doubts."
            scene ep4_sc9_pool_09_bis
            off "It's like my heart is torn to shreds then reassembled pieces by pieces."
            off "As she touches me, I can feel like I'm falling in a bottomless pit."
            off "I'm happy and sad at the same time."
            off "I'm afraid and impatient to kiss her as if it was the first time."
            scene ep4_sc9_pool_10
            $ UnlockThat("ep4/ep4_sc9_pool_10")
            off "She puts her sunglasses away and gently removes mine."
            off "My mouth gets suddenly dry, my throat tightens."

            if sis_love_path == True:
                off "Fuck."
                off "I'm in love with her."
                off "I'm in love with [sis_name] AND with [sf_name]."

            scene ep4_sc9_pool_11
            $ UnlockThat("ep4/ep4_sc9_pool_11")
            off "Her lips are so sweet and soft."
            off "Our tongues meet and cuddle but the kiss is somehow pure and innocent."
            off "At that very moment, I can feel it."
            off "She loves me."
            scene ep4_sc9_pool_11_bis
            off "A pure, strong and genuine first love, as bright as her smile."
            off "I don't have any choice but to love her in return."

            if sis_love_path == True or sis_sub_path == True:
                scene ep4_sc9_pool_12
                $ UnlockThat("ep4/ep4_sc9_pool_12")
                off "I sense [sis_name] getting away from us."
                off "I can feel her sadness and some kind of anger."

            if sis_love_path == True:
                off "I hurt her and it kills me."

            if sis_sub_path == True:
                off "Is this... jealousy?"

            if sis_love_path == True:
                off "What the fuck am I doing?"
                off "This is all my fault."
                off "Only now do I really understand that I'll have to choose one or the other and what that means."
                off "Whoever I choose, I'll end up destroying their friendship and my relationship with them."
                off "It can't end well."

            scene ep4_sc9_pool_13
            $ UnlockThat("ep4/ep4_sc9_pool_13")
            off "The kiss ends."
            off "I wanted it to last longer but we both needed to breathe."
            off "I don't know how we came to this position but [sf_name] basically climbed onto me and I have both hands on her ass, I hold her as tight as possible."
            off "Her legs are wrapped around me."
            off "I can feel her breasts pressed against my chest and our crotch connected."
            off "My boner is out of control but she doesn't seem to be aware of it."
            scene ep4_sc9_pool_14
            $ UnlockThat("ep4/ep4_sc9_pool_14")
            off "She whispers in my ear."
            sf "Don't drink too much tonight."
            sf "I have things I want to share with you.. and I want you to be sober to enjoy it fully."
            off "Holy shit."
            scene ep4_sc9_pool_15
            $ UnlockThat("ep4/ep4_sc9_pool_15")
            sis "You know guys, it's very disturbing to watch you getting all lovey-dovey touchy-feely right in front of me."
            sis "Can we agree on a safety distance between the two of you?"
            sis "By the way, [mc_name], I can see your boner from here, and [sf_name], you have saliva dripping from your chin."
            sis "Shame on you, young lady."
            sis "This is disgusting."

            off "She tries to use a joking tone but I can feel her bitterness."
            if sis_sub_path == True or sis_love_path == True:
                off "And her Jealousy."
                off "I wonder if [sf_name] hears it as well."

            sf "Sorry, sorry! We'll try to be more discreet."
            off "[sf_name] puts my shades back in place and gets away from me, laughing brightly."
            off "I'm speechless, happy, shameful, sad."

        scene black with fade
        with Pause(2)
        show text "Half an hour later."
        with Pause(2)
        scene ep4_sc9_pool_16 with fade
        $ UnlockThat("ep4/ep4_sc9_pool_16")
        off "The girls are talking about their morning exercise sessions."
        sis "You think we'll encounter the two morons again?"
        sf "We've seen them 2 days in a row, they're probably regulars at that park."
        off "I don't know what they're talking about but I immediately imagine them being harassed by the two psycho twins."
        scene ep4_sc9_pool_17
        mc "What are you talking about?"
        mc "Did you have any problems in the park?"
        sis "It's nothing, [mc_name]."
        sis "You don't need to worry."
        sf "Two guys tried to pick us up."
        sf "Yesterday, and also this morning."
        sf "And no, before you imagine things, it wasn't the guys from the club."
        sis "It's just two random guys."
        sis "As I said, you don't have to worry."
        mc "Really?"
        mc "You seemed to say that they were somehow harassing you."
        sf "They tried to talk to us at a fountain yesterday, you know.. classic pick up lines..."
        scene ep4_sc9_pool_18
        $ UnlockThat("ep4/ep4_sc9_pool_18")
        sis "Hey, beautiful, whatcha doing alone here?"
        off "[sis_name]'s impersonation is completely ridiculous."
        off "[sf_name] laughs."
        sis "Your eyes broke my heart, beautiful."
        sis "It's so hot out there, wanna come to drink some refreshment?"
        scene ep4_sc9_pool_19
        sf "He actually sounded that ridiculous."
        sf "She's doing it perfectly."
        mc "Ok..."
        sf "It didn't go much further."
        sf "We refused and resumed our running."

        sf "They tried to follow us but they couldn't keep up with [sis_name]'s pace for even a minute."

        sis "I didn't even try to lose them."
        sis "We saw them again this morning."
        sis "They were coming towards us while [sf_name] was going through her exercises."
        scene ep4_sc9_pool_20
        sis "I think they got scared when she started with her Bruce Lee thing."
        sf "That's not a Bruce Lee thing."
        sis "Yeah, yeah, I know what I saw, girl."
        sis "Bruce Lee thing."
        mc "Hold on, I imagining it."
        mc "Bruce Lee things you said?"
        mc "With the little screams and all?"
        off "[sis_name] nods affirmatively."
        scene ep4_sc9_pool_21
        sf "It's called Tai Chi."
        sf "It's not a Bruce Lee thing."
        sf "And I don't make little screams!"
        sis "You should see her."
        mc "Well, I'm curious now, would you show me?"
        sf "Right now? Certainly not."
        sis "She's shy about it."
        sis "I don't understand it by the way."
        sis "You're practicing in a park were anyone can see you, but you don't want to show some moves in private."
        sf "I'm a complicated girl, ok?"
        mc "Anyway, if you think these two guys can be a problem..."
        sf "They're not."
        sf "However, if you're so worried, you could come with us."
        scene ep4_sc9_pool_22
        $ UnlockThat("ep4/ep4_sc9_pool_22")
        off "[sis_name] literally bursts out laughing."
        sis "Him?"
        sis "He wouldn't be able to follow us even if his life depends on it."

        menu:
            "I'll be honest. [sfDomPath]":
                $ ep4runninghonesty = True
                scene ep4_sc9_pool_23
                $ ProcessStat(1, "sis_affection")
                $ ProcessStat(1, "sf_affection")
                $ ProcessStat(-1, "sf_dominance")
                $ DumpNotStack()
                mc "She's right."
                mc "I'll probably die from exhaustion before reaching the park entrance."
                sf "Well, that's too bad then."
                sf "It could have been fun."
                sis "Or painful."
                sis "We would have had to wait for him."
                mc "And that's without even mentioning the heat."
                mc "I don't know how you can go exercising with this scorching weather."
                sf "It's not that hot in the morning."
                sf "We usually manage to get out of the sun right when the heat really starts."
                sis "Speaking of the heat, if we're not going back in the pool, I suggest we move inside before the sun burns us to a crisp."
            "Hey! I can run! [sisLovePath] [sfLovePath]":

                $ ep4runningjoke = True
                scene ep4_sc9_pool_24
                $ UnlockThat("ep4/ep4_sc9_pool_24")
                off "At least I think..."
                off "It's just running after all."
                off "It's like walking, but faster, isn't it?"
                sis "No, you can't."
                sis "You never run nor workout."
                sis "You'll be out of breath before we even reach the park entrance."
                off "The park entrance being barely 200 meters from our home."
                off "This is clearly a provocation."
                mc "I can run!"
                sf "[mc_name], you don't have to prove anything."
                sf "It's alright."
                sf "You don't have to accompany us."
                mc "I said I can run ok?"
                mc "And I'm working out all the time, you just don't see me exercising."
                off "Both girls are totally incredulous."
                sis "All the time?"
                sis "Really?"
                sis "What kind of exercise do you do?"
                off "Fuck. Why did I have to lie about something so stupid?"
                mc "Push-ups. And abs."
                sis "Show us."
                off "Shit."
                mc "No problem."
                off "Don't panic [mc_name]. You can do a couple push-ups."
                scene ep4_sc9_pool_25
                $ UnlockThat("ep4/ep4_sc9_pool_25")
                sis "1"
                scene ep4_sc9_pool_26
                sf "2"
                scene ep4_sc9_pool_25
                sis "3"
                scene ep4_sc9_pool_26
                sf "4"
                scene ep4_sc9_pool_25
                sis "5"
                off "Fuck it! My muscles are already burning like hell!"
                scene ep4_sc9_pool_26
                sf "6"
                scene ep4_sc9_pool_25
                sis "7"
                scene ep4_sc9_pool_26
                sf "8"
                sis "Come on [mc_name] you can do it. Two more."
                scene ep4_sc9_pool_25
                sis "9"
                sf "One more."
                scene ep4_sc9_pool_26
                sf "10!"
                scene ep4_sc9_pool_25
                off "Fuck."
                off "10 push-ups and I'm done."
                off "How the fuck is it even possible."
                scene ep4_sc9_pool_27
                $ UnlockThat("ep4/ep4_sc9_pool_27")
                mc "It's the heat."
                mc "Usually, I do many more."
                mc "I think I'm weak to the heat or something..."
                off "They're laughing."
                off "My excuse is so absurd that I'm laughing too."
                off "It may be a bit of an humiliation but I have the feeling that we're not laughing at me, but rather simply laughing together."
                off "We're having fun."
                $ ProcessStat(3, "sis_affection")
                $ ProcessStat(3, "sf_affection")
                $ DumpNotStack()
        jump ep4sc10


label ep4sc10:
    scene black with fade
    with Pause(2)
    show text "Later."
    with Pause(2)
    scene ep4_sc10_s_00 with fade
    $ UnlockThat("ep4/ep4_sc10_s_00")
    if sf_love_path == True:
        off "I can't stop thinking about what [sf_name] whispered in my ear."
        off "She wants us to stay reasonably sober so we can enjoy something she wants to share with me."
        off "Does that mean what I think it is?"
        off "Does she want to have sex?"
        off "Calm down [mc_name], she wasn't ready yesterday, there's no way she can be today."
        off "Or can she?"
        off "I don't understand girls."
        off "Is that possible?"
        off "She probably just desires some foreplay, maybe a bit further, but I don't think she'll want to go all the way."
        off "It's too soon."
        if sis_love_path == True:
            off "I'm in deep shit, otherwise."
            off "I can't have sex with her."
            off "I mean..."
            off "Fuck, I want to have sex with her, but that would be betraying [sis_name]..."
            off "Dumbass, you're already deceiving [sf_name], with [sis_name]..."
            off "You should hurry up and find a way to solve this situation."
            off "As if there was such a thing as a solution."
            off "It's just gonna explode and mess everything up."

    off "Beers, ok, I'm gonna take some wine too..."
    off "What we won't drink tonight we'll drink another day."
    off "That sounds like Steve's perverted philosophy."
    off "I wonder what he is doing right now."
    off "He sure seemed to have fun yesterday."
    uk "I don't give a fuck."
    uk "We have to do it."
    uk "We've already gone that far, there's no way we stop now..."
    uk "I say we ask her for help."
    uk "Come on, we have known this little slut for years."
    uk "She can't refuse us."
    scene ep4_sc10_s_01
    $ UnlockThat("ep4/ep4_sc10_s_01")
    off "I hate this kind of moron who talks on their phones without concerns about their surroundings..."
    off "Furthermore, he sounds like a true gentleman."
    off "Holy shit."
    off "It's him."
    off "Either he didn't saw me or he didn't recognize me."
    if ep3facebroken == True:
        off "He doesn't seem to have neither bruises nor marks on his face."
        off "It must be the other brother."
        off "He probably doesn't know my face."
    else:
        off "Or perhaps it's the other brother and he simply doesn't know my face."

    scene ep4_sc10_s_02
    off "Let's keep a low profile either way."
    ry "Take it easy."
    ry "We'll get her."
    ry "She won't stay in that house forever."
    off "This jerk isn't even trying to be discreet."
    off "Is he talking about [sis_name]?"
    off "Or someone else?"
    scene ep4_sc10_s_03
    ry "I know."
    ry "I would have preferred to do it gently to, but the bitch can't stand me, you saw it."
    ry "There's no way I can fuck her legit."
    ry "We'll have to find another way."
    off "Holy fucking shit."
    ry "Yeah. I know."
    ry "I have the booze."
    ry "I'm coming back."
    scene ep4_sc10_s_04
    off "I'm very confused."
    off "How many different girls were they talking about?"
    off "Were they even talking about [sis_name]?"
    off "What was this guy even doing in a convenience store near our house?"
    off "I pay my due and return home as quickly as possible."
    scene black with fade
    with Pause(2)
    show text "10 minutes later."
    with Pause(2)
    scene ep4_sc10_l_00 with fade
    $ UnlockThat("ep4/ep4_sc10_l_00")
    off "I found the girls in the living room, watching something on the TV."
    mc "Girls, we need to talk."
    sis "About what?"
    mc "I've seen one of the twins at the convenience store."
    scene ep4_sc10_l_01
    off "I immediately have their full attention and explain what happened and what I heard."
    sis "So... they're not done."
    mc "Well, it was actually very weird."
    mc "I'm not even sure they were talking about you."
    mc "I mean, I immediately thought that they were talking about you, but he said they've known her for years..."
    mc "So it can't be you."
    mc "Or not only you."
    scene ep4_sc10_l_03
    $ UnlockThat("ep4/ep4_sc10_l_03")
    sf "They were probably talking about several different girls."
    sf "However, it's obvious they don't have the best intentions."
    sf "And what was he doing so close to your house?"
    mc "I don't know."
    mc "But we should be extra careful."
    mc "And... I'm sorry [sis_name], but we should go to the police."
    mc "We're not going to wait for them to assault and rape you."
    scene ep4_sc10_l_02
    sis "What do you want to tell them?"
    sis "That we have suspicions that someone may not be well-intended toward us?"
    sis "You were right, ok?"
    sis "We should have gone to the police Sunday morning... but now..."
    sis "It's too late."
    mc "Come on..."
    scene ep4_sc10_l_04
    sis "If something else happens... We'll go."
    sis "Besides... it's not like there's anything actually new, isn't it?"
    sis "We already knew they were still lurking somewhere."
    off "She's as obstinate as a brick."
    mc "You're as stubborn as ever, Princess."

    if ep4kfmeetingok == True:
        off "Should I tell them about Kelly?"
        off "It could help convince her."
        off "And I'll have to come clean about it sooner or later."
        off "Better do it on my timing rather than being exposed otherwise."

        menu:
            "Tell them. [gr]\[KellyLateTold\]":
                $ ep4kflatetold = True
                mc "However... there is something else I need to tell you."

                if ep4morningkftold == False:
                    mc "Yesterday... A girl texted me."
                    sf "A girl?"
                    mc "Yes. You know her."
                    mc "Her name's Kelly."
                    sis "What the fuck?"
                    mc "She gave me her name but didn't tell me who she was."
                    sis "What did she want from you?"
                    sis "How did she get your number?"
                    off "Ok, maybe they don't need to know that she has a crush on me..."
                    mc "She wanted us to meet, so we could talk..."
                    sis "She wanted to talk?"
                    sis "Really?"
                else:
                    mc "It's about Kelly..."
                    sis "What about her?"
                scene ep4_sc10_l_05
                $ UnlockThat("ep4/ep4_sc10_l_05")
                mc "We met earlier today, at noon."
                sis "Are you serious?"
                sis "Why the fuck would you do that?"
                off "This is it, the moment everything goes to shit if I don't find a good excuse."
                mc "I'm sorry."
                mc "I choose not to tell you about that."
                mc "I knew that you wouldn't like this idea."
                mc "But I was curious."
                mc "The timing was strange, I thought it might be related to our psycho twins problem."
                mc "I thought I could get some information."
                mc "And as a matter of fact, I did."
                sis "Oh, and you think it's a good excuse?"
                mc "No, this is not an excuse, this is just what I did."
                scene ep4_sc10_l_06
                $ UnlockThat("ep4/ep4_sc10_l_06")
                sf "So... you just talked...?"
                mc "Yeah."
                mc "When she arrived, she immediately explained to me who she was."
                mc "She apologized to me, for what she did to both of you."
                mc "We talked a bit."
                mc "More precisely, she talked a lot, and I mostly listened."
                mc "I asked her about her friends."
                mc "And she said that she was very confused."
                mc "Once you left the party, last night, they did go to her and asked a lot of questions about both of you."
                mc "Kelly thought that it was weird and refused to answer them."
                mc "She used the term unhealthy obsession."
                mc "She thinks we should be careful."
                off "[sis_name] sighs loudly."
                off "[sf_name] stays uncomfortably silent."
                scene ep4_sc10_l_05
                sis "I can't believe you went to meet her."
                mc "I'm not proud of it, ok?"
                mc "But if I had told you, you wouldn't have let me go."
                mc "And we wouldn't have learned that."
                scene ep4_sc10_l_06
                sf "The way you talk about it.. you seem to trust her."
                sf "You think she has nothing to do with the twins?"
                mc "Honestly..."
                menu:
                    "I believe she's sincere. [gr]\[KellySincere\]":
                        $ ep4kfsincerity = True
                        mc "She told me about her life and some stuff..."
                        mc "I don't know why but I believe her."
                        mc "I think she's sincere with her apologies, and with her warning."
                    "I don't know.":
                        mc "But if she was working with them she wouldn't have any interest in warning us."
                scene ep4_sc10_l_05
                sis "Well, that doesn't change a thing."
                sis "We were already supposed to be careful."
                mc "True, but..."
                sis "No but."
                scene ep4_sc10_l_07
                $ UnlockThat("ep4/ep4_sc10_l_07")
                sis "We're mad at you, [mc_name]."
                sis "You fucked up."
                sis "You should have told us."
                off "[sis_name] quickly leaves the room."
                off "[sf_name] follows her without even looking at me."
                off "The mood obviously darkened a bit."
                jump ep4sc12
            "They wouldn't understand. [gr]\[Kelly Secret\]":


                $ ep4kfsecret = True
                off "What they don't know can't hurt them, right?"

    scene black with fade
    off "The mood obviously darkened."
    off "However, [sis_name] is right."
    off "We were already suspecting this."
    off " This doesn't really change a thing."
    off "I can feel that [sis_name] slowly accept the idea of going to the police."
    off "I should talk about that again later, or tomorrow..."
    jump ep4sc12


label ep4sc11:
    scene black with fade
    with Pause(2)
    show text "Later."
    with Pause(2)
    scene ep4_sc10_s_00 with fade
    if ep4niceasshole == True:
        off "I made a quick hop by the convenience store and took a generous amount of beers and wine."
        off "If the ladies want to get drunk, there will be enough beverages to do so a couple of times."
        off "Let's concentrate on making this evening fun for everyone."
        off "It may be my last chance to hone my relationship with [sis_name]."

        off "She may be a bitch, but that slut is still my friend."

        off "I have to do all I can to prevent her from making the mistake of her life."
        off "And... well... If they're drunk enough..."
        off "There may be some... Benefits..."
    scene black with fade
    off "Someone shouts my name from the hallway. [sf_name]."
    off "I get out of my room and make way to the ground floor."
    off "What's happening here?"
    scene ep4_sc11_ent_00 with fade
    $ UnlockThat("ep4/ep4_sc11_ent_00")
    $ ep4sobcome = True
    if ep3breakfastfailed == True:
        off "Is that... [sis_name]'s boyfriend?"
    else:
        off "The son of a bitch."

    off "[sf_name] seems ready to rip his throat open."

    if ep3breakfastfailed == True:
        sf "[mc_name], this is Luke."

    sf "He came to take [sis_name] for the night."

    scene ep4_sc11_ent_01
    lk "Hello, [mc_name]. How are you?"
    off "Fuck."

    if ep3breakfastfailed == True:
        off "I didn't expect to meet him so soon."
    else:
        off "I didn't expect to meet him again so soon."

    if ep4lukephonedsuccess == True:
        off "He said he was going to test me. This is it, isn't it?"
        off "I have to choose quickly."
        off "Do I try to play their game?"
        off "Or do I try to stand up?"


    menu:
        "Shake his hand. [gr]\[HandShaked\]" if ep4lukephonedsuccess == True:
            scene ep4_sc11_ent_02
            $ UnlockThat("ep4/ep4_sc11_ent_02")
            $ ep4handshaked = True
            mc "Hello, Luke."
            off "I can sense [sf_name]'s disappointment."
            off "I'm clearly betraying her."
            mc "So... you and [sis_name].. are going out tonight?"
            lk "We're going to a little party."
            lk "You're invited too by the way."
            lk "Along with [sf_name], of course."
            lk "We really want you to join us."
            lk "The party wouldn't be the same without you."
            mc "Nice. Where are we going?"
            scene ep4_sc11_ent_02_alt
            sf "What the hell, [mc_name]?"
            off "[sf_name] pushes me aside and takes a step towards [sis_name]."
        "Don't shake his hand. [gr]\[DecisiveTry\]":

            $ ep4decisivetry = True
            if ep4lukephonedsuccess == True:
                $ ep4sobbetrayed = True
                off "This is sick."
                off "I can't do that."
                off "He understands immediately that I won't join them."
                off "I failed their test."

            off "Now, [mc_name], it's time to do something if you don't want him to take your friend for good."

            off "Man up, [mc_name]."
            off "Say something for god sake."

            lk "You won't shake my hand?"
            mc "No, I won't."
            sis "[mc_name]! You're so rude!"
            lk "It's okay, [sis_name]."

            lk "I get that your friend doesn't approve of our relationship."


            mc "I don't approve of it, indeed."
            sis "My life is none of your business, Perv."
            scene ep4_sc11_ent_06
            $ UnlockThat("ep4/ep4_sc11_ent_06")
            mc "Actually, it is."
            sis "I beg your pardon?"
            mc "Just listen to me, please."

            menu:
                "I'm sorry. [sisLovePath] [sfLovePath]":
                    $ ep4dst1 = True
                    $ ep4dsc += 1
                    mc "I know I'm a moron."
                    mc "I've probably already told you this a couple of times, and each time I've managed to fuck things up right afterward."

                    mc "I'm a moron, I'm a dumbass, that's what I am, but that doesn't change the fact that I'm also your friend and that I care about you."


                    $ ProcessStat(1, "sis_affection")
                    $ ProcessStat(1, "sf_affection")
                    $ DumpNotStack()
                "Don't go with him, please.":

                    mc "He's a scumbag, ok?"
                    mc "He will only hurt you."
                    mc "I don't know what the fuck made you choose him but this has to stop."
                    mc "He tried to rape you for god sake!"
                    lk "I never did anything like that!"
                    mc "You shut the fuck up."

                    mc "I'm talking to [sis_name]."

                    sis "He never did that [mc_name]."
                    sis "You don't have any proof."
                    mc "And he doesn't have any proof he didn't do it either."

            menu:
                "I've failed to properly apologize to you... [sisLovePath] [sfLovePath]" if ep4dst1 == True:
                    $ ep4dst2 = True
                    $ ep4dsc += 1
                    mc "... for my behavior and my mistakes."
                    mc "I hurt you and some stupid pride prevented me from assuming that."
                    mc "But I love you."
                    mc "I may not show it, but I love you."
                    $ ProcessStat(1, "sis_affection")
                    $ ProcessStat(1, "sf_affection")
                    $ DumpNotStack()
                    mc "I also know that if you go with that guy, you will suffer."
                    lk "Hey!"
                    mc "You shut the fuck up."

                    mc "I'm talking to [sis_name]."

                    mc "He will hurt you."
                    mc "There is no doubt about it."
                    mc "I don't know why you choose him."
                    mc "Maybe it's to express your rebellion or maybe you have genuine feelings towards him."
                    mc "I don't know."
                    mc "The only thing I know is that he will hurt you badly."
                    mc "And I don't want you to be hurt again."
                "Don't make that mistake.":
                    mc "There's plenty of guys nicer than him that are waiting for you."
                    mc "This one is even worse than all the dumbass who asked you to suck their dicks during the last three years."
                    mc "He doesn't love you."
                    mc "He doesn't even like you."
                    mc "He just wants to hurt you."

            menu:
                "What you'll do is yours to decide. [sisLovePath] [sfLovePath]":
                    $ ep4dsc += 1
                    mc "But you have to know that I love you and I really care about you."
                    $ ProcessStat(1, "sis_affection")
                    $ ProcessStat(1, "sf_affection")
                    $ DumpNotStack()
                "You can still walk back from that.":
                    $ ep4dsc += 1
                    mc "You say a word and I throw this asshole out of the house."

            menu:
                "Tomorrow, I may very well be an asshole again. [sisLovePath] [sfLovePath]" if ep4dst1 == True and ep4dst2 == True and ep4textlove == True:
                    $ ep4dsc += 3
                    $ ep4dstlove = True
                    mc "I'll probably fuck everything up again, that's just what I do."
                    mc "But it doesn't change the fact that I love you."
                    $ ProcessStat(2, "sis_affection")
                    $ ProcessStat(1, "sf_affection")
                    $ DumpNotStack()
                    mc "Ok?"
                "Please, [sis_name].":
                    $ ep4dsc -= 1
                    mc "Don't fuck this up."

            if ep4dsc > 2 and sis_affection > 9:
                $ ep4decisivesuccess = True
            else:
                $ ep4decisivefail = True

            if ep4decisivesuccess == True:
                scene ep4_sc11_ent_07
                $ UnlockThat("ep4/ep4_sc11_ent_07")
                sis "Are you finished?"
                off "She's crying."
                off "I don't know if it's a good thing or not."
                sis "You really are a dumbass."
                $ ProcessStat(1, "sis_affection")
                $ DumpNotStack()
                off "She almost runs out of the entrance."
                sf "I don't know what you're after, but this means you can leave, and never return."
                off "[sf_name]'s tone is as cold as ice."
                off "Luke doesn't even try to reply and disappears without a word."
                scene ep4_sc11_ent_08
                sf "[mc_name], if you thought only half of what you said, you may be a moron, but you're not a bad guy."
                off "She gives me a smile."
                if sf_dom_path == True:
                    sf "I'll make sure to reward you properly."
                else:
                    sf "Thank you."
                sf "I'll go to see [sis_name]."
                sf "See you later."
                scene black with fade
                off "Alone, I can finally breathe."
                off "That wasn't so hard to let out."
                off "I think I managed to get her to see me as her brother again... or at least I hope."

                if ep4dstlove == True:
                    off "Did I really tell her I love her again?"
                    off "Twice a day may be a bit too much."
                    off "Damn, I hope she won't get all cocky with that now."

            elif ep4decisivefail == True:
                scene ep4_sc11_ent_07_alt
                $ UnlockThat("ep4/ep4_sc11_ent_07_alt")
                sis "Are you finished?"
                off "She doesn't look to even gives a fuck about what I just said."
                sis "I appreciate your concern, but as I said, my life is none of your business."
                off "It was useless."
                off "That slut is so eager to suck this dick that whatever I could have said wouldn't have had any effect on her."
                off "It's hopeless."
                sis "Will you give me a minute to get ready?"
                lk "Sure. I'll wait right here"
                off "[sf_name] suddenly pushes me aside and takes a step towards [sis_name]."


    if ep4handshaked == True or ep4decisivefail == True:
        scene ep4_sc11_ent_03
        $ UnlockThat("ep4/ep4_sc11_ent_03")
        sf "Tell me you're not going to do that."
        sis "To do what?"
        sf "You're going to leave me alone here?"
        sis "Luke told you."
        sis "You're invited too."
        sis "Just get ready and join us."
        sf "No, I won't, I can't stand him nor his brother."
        sf "Seeing you with him hurts me and you know it."
        sf "Therefore you'll have to choose, here and now."
        sf "It's either him or me."
        sf "If you care so little about me that you can imagine leaving me alone here, choosing will be easy."
        sis "Are you serious right now?"
        sf "I've never been more serious."
        off "[sis_name] seems to hesitate, she actually seems pretty desperate."
        off "I don't really understand what's going on."
        off "If [sf_name] knew she would have that much impact on her, why did she even bother asking me to do something?"
        scene ep4_sc11_ent_04
        sis "I... I'm sorry Luke... I'll call you later."
        lk "It's ok babe, I understand."
        lk "Don't worry."
        off "A few seconds later, he's gone and a heavy silence hangs in the room."
        off "I can sense the tension between [sis_name] and [sf_name]."
        off "This is so weird."
        sis "I'm sorry if I hurt you."
        off "She leaves the place without waiting for a reply."

    if ep4decisivefail == True:
        scene ep4_sc11_ent_08
        $ UnlockThat("ep4/ep4_sc11_ent_08")
        off "[sf_name] looks at me with some kind of disappointed smile."
        sf "You're really bad with words. But at least you tried."
        if sf_dom_path == True:
            sf "And that deserves a reward."
        mc "I don't know what more I could have said."
        sf "That you love her."
        if ep4textlove == True:
            mc "I'm pretty sure I did that..."
            sf "Obviously, you haven't insisted enough."
        mc "You're kidding. That can't be so simple."
        sf "[mc_name], you're definitely not fit to interact with women."
        sf "You should work on that."
        sf "I'll go to see [sis_name]."
        sf "See you later."

    if ep4handshaked == True:
        scene ep4_sc11_ent_05
        $ UnlockThat("ep4/ep4_sc11_ent_05")
        off "[sf_name] looks at me with anger, and possibly even hatred."
        sf "Maybe I already told you I thought that you may be a moron, but not a bad guy."
        sf "I was wrong."
        sf "I don't know what you tried to achieve but let me tell you this: if you hurt her in any way, I will find a way to hurt you back."
        if sf_dom_path == True:
            sf "Consider our contract void."
            $ ep4domcontractvoid = True
        off "I'm practically shivering as she leaves me."
        off "Her voice was calm and cold."
        off "She meant it and she has no doubt she will be able to end me if necessary."
        off "I fucked up so much."




label ep4sc12:
    scene black with fade
    with Pause(2)
    show text "Later."
    with Pause(2)

    if ep4handshaked == True:

        scene ep4_sc12_l_29 with fade
        $ UnlockThat("ep4/ep4_sc12_l_29")
        off "I don't even know why I joined them on their movie night after what happened in the late afternoon."
        off "They both ignore me completely."
        off "I guess I'm paying the price of failure."
        off "I don't know what I hoped siding with these psychos."
        off "If the girls ever learn about it I'm dead."
        off "And that's not a figure of speech."
        off "I don't know why but I have a very strong feeling that [sf_name]'s threats are not empty words."
        off "Aside from that, the evening is pretty uneventful."

        scene ep4_sc12_l_30
        $ UnlockThat("ep4/ep4_sc12_l_30")
        off "The movies are boring, at some point, [sis_name] lies onto [sf_name]'s lap."
        off "Obviously, their friendship is not ordinary."
        off "[sf_name] plays with [sis_name]'s hairs like a mother would do with her young daughter."
        off "It's not friendship."
        off "It's love."
        off "Maybe not something physical, but love nonetheless."
        off "I have the intuition that they have something I'll never have."
        off "And it pains me."
        jump ep4dispatch
    else:
        off "The evening comes to an end slowly."
        off "The girls stay a long time in [sis_name]'s room."
        off "I don't know what they talk about."
        off "The night gently envelops the house."
        off "I feared that the atmosphere would be crippled by the events of the late afternoon, but the mood has gradually improved with time."

        scene ep4_sc12_l_00 with fade
        $ UnlockThat("ep4/ep4_sc12_l_00")

        if ep3sisluked == False and sis_affection > 15 and sf_affection > 15:

            off "I find them in the living room, talking about [sis_name]'s studies for her catch up sessions."
            sis "I'll be okay."
            sis "I told you I only miss one point."
            sis "It's no big deal."
            sf "I hope so."
            sf "I don't want to go to college without you."

            scene ep4_sc12_l_01
            $ UnlockThat("ep4/ep4_sc12_l_01")

            menu:
                "She'll be there. [sisSubPath] [sfDomPath]":
                    mc "Once this week is over, I'll work her hard."
                    mc "She'll study harder than she ever has."
                    if sis_sub_love_path == True:
                        $ ProcessStat(1, "sis_affection")
                    $ ProcessStat(1, "sis_submission")
                    $ ProcessStat(1, "sf_affection")
                    $ ProcessStat(1, "sf_dominance")
                    $ DumpNotStack()
                    sis "Easy, cowboy, I never said I was okay with you to making me study."
                    sis "I don't think you're qualified, you don't know which class I failed."
                    $ ep4studyhard = True

                    menu:
                        "English literature. [sisLovePath] [sfLovePath]":
                            scene ep4_sc12_l_04
                            sis "You couldn't be more wrong."
                            sis "I aced that class."
                            mc "History maybe?"
                            sis "Nope"
                            mc "Astrophysics?"
                            sis "Was there an astrophysics class in our high school?"
                            mc "I don't think so."
                            scene ep4_sc12_l_02
                            sis "Then why do you even ask?"
                            sis "It's Spanish, Ok? I failed Spanish."
                            mc "I was about to say that."
                            sis "No, you weren't."
                            mc "Oh yes, I was."
                            scene ep4_sc12_l_08
                            $ UnlockThat("ep4/ep4_sc12_l_08")
                            off "[sf_name] bursts out laughing."
                            sf "You guys are too cute."
                            $ ProcessStat(1, "sis_affection")
                            $ ProcessStat(3, "sf_affection")
                            $ DumpNotStack()
                            sis "Yeah, cute, whatever."
                        "Spanish [sisSubPath] [sfDomPath]":

                            scene ep4_sc12_l_03
                            sis "How the fuck do you know that?"
                            $ ProcessStat(1, "sis_affection")
                            $ ProcessStat(1, "sis_submission")
                            $ DumpNotStack()
                            mc "Brothers know that kind of thing."
                            sis "Yeah, right. You were lucky."
                            mc "You got an E."
                            sis "How the...?"
                            mc "You aced English literature, as expected from a girl who likes to read those old books and write poetry."
                            mc "You weren't as good in history but managed to get it anyway."
                            sis "Did you see my report card?"
                            mc "Not even."
                            mc "I just know you better than you think."
                            $ ProcessStat(1, "sis_affection")
                            $ ProcessStat(1, "sis_submission")
                            $ DumpNotStack()
                            scene ep4_sc12_l_04
                            sis "If you say so... but you don't speak Spanish either."
                            mc "Actually, I can speak some."
                            mc "But there's no need to speak it to make you study it."
                            mc "Believe me, Princess."
                            mc "You're going to study it until you speak it fluently."
                            mc "I won't leave you any other choice."
                            mc "It's simple: If you get good at it, you'll get a reward."
                            mc "If you don't get good at it, you'll get a punishment."
                            scene ep4_sc12_l_07
                            sis "What? Wait... I didn't agree to anything."
                            sis "Do you think you were going to convince me by promising me punishment?"
                            mc "I also promised rewards."
                            scene ep4_sc12_l_05
                            sis "Yeah... what kind of rewards?"
                            if sis_sub_path == True:
                                off "I run my tongue over my lips before answering her."
                            mc "The kind you will like."
                            if sis_sub_love_path == True:
                                $ ProcessStat(2, "sis_affection")
                                $ ProcessStat(2, "sis_submission")
                                $ ProcessStat(1, "sf_dominance")
                                $ DumpNotStack()
                            elif sis_sub_path == True:
                                $ ProcessStat(2, "sis_submission")
                                $ ProcessStat(1, "sf_dominance")
                                $ DumpNotStack()
                            else:
                                $ ProcessStat(1, "sis_submission")
                                $ ProcessStat(1, "sf_dominance")
                                $ DumpNotStack()
                            sis "...I'll think about it..."
                            $ ep4studyhardreward = True
                "She can do it. [sisLovePath] [sfLovePath]":

                    $ ProcessStat(1, "sis_affection")
                    $ ProcessStat(1, "sf_affection")
                    $ DumpNotStack()
                    $ ep4studytrust = True
                    mc "I trust her."
                    mc "She's motivated."
                    mc "She doesn't want to stay in high school without you either."
                    scene ep4_sc12_l_06
                    sis "These words sounds very strange coming out of your mouth."
                    sis "But you're right."
                    sis "There's no way I'm going back there."
                    sf "I'm not doubting that."
                    sf "If you need any help, I'll be happy to provide."
                    mc "I can help you too."
                    sis "You don't speak Spanish."
                    sis "She does."
                    mc "What does that have to do with helping you?"
                    scene ep4_sc12_l_04
                    sis "I failed Spanish, dumbass."
                    sis "So I need to study Spanish for the catch-up session."
                    sis "Therefore you can't help me."
                    sis "She can."
                    mc "Oh..."
                    sis "But I appreciate your faith in me."

                    menu:
                        "[gr]Thinking about it...":
                            mc "Maybe you just need some additional motivation."
                            sis "Going to college is already motivating enough."
                            sis "I don’t want to spend another year in that high school."
                            mc "Sure..."
                            mc "I just thought that it could be fun to plan something special for your graduation."
                            sis "Like what?"
                            mc "I don’t know..."
                            mc "We could go on a trip for a few days..."
                            mc "In someplace where you could speak Spanish."
                            $ ep4studytrustreward = True
                            $ ProcessStat(4, "sis_affection")
                            if sis_sub_love_path == True:
                                $ ProcessStat(4, "sis_submission")
                            $ ProcessStat(4, "sf_affection")
                            $ DumpNotStack()
                            sf "That would be great!"
                            sf "The three of us could go and share in an adventure."
                            scene ep4_sc12_l_02
                            sis "Hold on your horses, there."
                            sis "This kind of thing cost money..."
                            mc "I’m sure it wouldn’t cost that much."
                            mc "I’ll take care of the expenses."
                            sis "Are you serious?"
                            sis "Since when were you so willing to spend your money?"
                            mc "Well, it wouldn’t be a gift or a reward if you had to pay for it so..."
                            sf "I’ll help too!"
                            sf "I can afford it!"
                            sf "Come on, [sis_name]!"
                            scene ep4_sc12_l_05
                            sis "Well, it’s not like there’s anything I can refuse..."
                            sis "I'll ace it anyway..."
                            sis "But some more motivation can't hurt, I guess..."
                            sis "I hope it's not one of these situations where we end up being raped, ripped of our organs and sold as slaves, though."
                            sf "That sounds fun!"
                            sf "I can’t wait!"
                            sf "You'll pass it."
                            sf "I may have to disguise myself and take it in your stead, but you'll pass it."
                            sis "... I could want to see that..."
                        "I actually can speak a bit of Spanish...":

                            mc "I learned some while working at the garage."
                            mc "I have a coworker who barely speaks English..."
                            mc "Well... It’s probably not the kind of Spanish you need anyway..."
                            scene ep4_sc12_l_07
                            sis "Probably not, indeed."
                            mc "If I can help you, or if you need anything..."
                            $ ProcessStat(1, "sis_affection")
                            $ ProcessStat(1, "sf_affection")
                            $ DumpNotStack()
                            mc "You know where to find me..."
                            sis "Yeah, I know."
                            sis "The door next to mine."
                            sis "Thank you."
                            mc "You’re welcome."

            scene ep4_sc12_l_09
            $ UnlockThat("ep4/ep4_sc12_l_09")
            sf "By the way, [mc_name], where are you going next year?"
            sf "Are you going to college?"
            mc "I believe I am."
            mc "We won't be going to the same university but we'll be in the same city."
            sf "Oh! What are you going to study?"
            mc "Engineering science. Mainly."
            sf "And... where are you going to live?"
            mc "I'm not sure."
            mc "My parents talked about renting an apartment for [sis_name] and me... But..."
            mc "I wasn't really excited about it... "
            sf "Are you now?"
            mc "I think I wouldn't mind."
            mc "But this option is not on the table anymore isn't it?"
            mc "Aren't you girls going to share a place?"

            if sf_love_path == True or sf_affection > 20:
                sf "We've talked about it."
                sf "But you know, all three of us could share."

                mc "Are you offering me to share an apartment with you and [sis_name]?"
                sf "Do you have any other option?"
                mc "Nothing confirmed yet..."
                sf "You wouldn't mind?"
                scene ep4_sc12_l_10
                mc "No, I wouldn't mind. Would you?"
                scene ep4_sc12_l_11
                $ UnlockThat("ep4/ep4_sc12_l_11")
                sis "...I'm ok with it."
                mc "Well... I'm interested then..."

                if sf_love_path == True and sis_love_path == True:
                    off "Providing we're still on good terms after what's about to come, of course..."

                scene ep4_sc12_l_12
                $ UnlockThat("ep4/ep4_sc12_l_12")
                sf "Great! I'm going to scout for a place next week."
                sf "I'll keep you updated."
                off "Things are evolving a bit quickly."
                off "I don't know if I should be excited or afraid."
            else:

                sf "We've talked about it."
                sf "Don't worry, [mc_name], you'll find a place."
                mc "I'm not worried."


        scene ep4_sc12_l_13
        off "[sf_name] already has a glass of wine. Two beers await on the other side of the table."
        off "I join them on the sofa."
        mc "Ladies. Are we ready for that movie night?"
        sis "I think we are."
        sf "I hope you choose something nice to start with because we found the perfect movie to end the night."
        off "Crap. I forgot to choose a movie. Ok, don't panic [mc_name]."
        mc "I guess that means we watch my movie first?"
        sis "Indeed. What is it?"
        mc "I'll show you."
        off "I hope I'll find something good on NaughtyFlix. Ok. Let's see..."
        scene ep4_sc12_l_14
        off "I start searching through my options as [sf_name] shut down the lights."
        off "Oh.. Look what I’ve found... It’s just perfect..."

        menu:
            "Casablanca. [sisLovePath] [sfLovePath]":
                scene ep4_sc12_l_15
                $ ep4chosenmovie = "Casablanca"
                $ ProcessStat(2, "sis_affection")
                $ ProcessStat(2, "sf_affection")
                $ DumpNotStack()
                off "This can be good."
                off "I remember [sis_name] talking about it."
                sis "Really?"
                sis "You wanna watch Casablanca?"
                sis "I don't mind watching it, but, you know, [sf_name] and I have seen it like a dozen times."
                sis "It's my favorite movie..."
                sis "If you choose it thinking to please me... well, I'm pleased, but you don't have to."
                mc "Actually I've never watched it."
                mc "So I thought it would be a good occasion, but, if you've seen it so often, I understand you're not interested."
                mc "I'll choose something else."
                sis "You've never seen it?"
                sis "Let's watch it then."
                sis "I told you I don't mind."
                sis "If [sf_name]'s ok of course."
                sf "I am. I like that movie."
                mc "Ok then..."
            "Lost in translation. [sfDomPath]":

                $ ProcessStat(2, "sf_affection")
                $ ProcessStat(2, "sf_dominance")
                $ DumpNotStack()
                scene ep4_sc12_l_15
                $ ep4chosenmovie = "Lost in translation"
                off "Isn't this [sf_name]'s favorite movie?"
                off "That may be a good choice."
                sf "Lost in translation?"
                sf "I didn't know you liked that kind of movie, [mc_name]."
                mc "I..."
                sis "He's choosing this only to please you."
                mc "I've never watched it."
                mc "You said it was good so..."
                sf "It is. It's my favorite movie."
                sf "I don't mind watching it again."
                sf "If [sis_name] is ok with it..."
                sis "Sure. Whatever. Anything."
                mc "Ok then..."
            "Big trouble in little China [sisSubPath]":

                $ ProcessStat(2, "sis_submission")
                $ DumpNotStack()
                $ ep4chosenmovie = "Big trouble in little China"
                scene ep4_sc12_l_15
                off "Holy shit. That's the best film in the world."
                sis "Well, I'm surprised."
                sis "But I can't say I'm thrilled."
                sf "It seems to have very good ratings..."
                mc "Ladies, this is probably one of the best movies ever made."
                sis "I'm already regretting this."
                sf "Oh, come on. It can't be that bad."
                sf "I'm actually intrigued."
                sf "Let's watch it."

        if sf_love_path == True:
            if sis_love_path == True or sis_sub_path == True:
                scene ep4_sc12_l_17
                $ UnlockThat("ep4/ep4_sc12_l_17")
            else:
                scene ep4_sc12_l_17_bis
                $ UnlockThat("ep4/ep4_sc12_l_17_bis")
            off "The movie as barely started that [sf_name] comes to me smiling and quickly sticks to me as close as possible."
            off "Just as this afternoon, I can sense her happiness."
            off "I want to take her in my arms and protect her, keep her safe."
            off "I want her to be mine."
            off "On her side of the sofa, [sis_name] focuses on the movie."
            off "However, even if she does her best not to show it, I can feel her jealousy in reaction to my promiscuity with [sf_name]."
            if sis_love_path == True:
                off "I have thought about it a lot throughout the day and still haven't found a way to solve this situation without hurting someone."
            if sis_sub_path == True:
                off "The talk I'll have with her later will be... memorable..."

        scene black with fade
        with Pause(2)
        show text "One movie later."
        with Pause(2)

        off "The movie ends."

        if ep4chosenmovie == "Casablanca":
            scene ep4_sc12_l_18
            off "[sis_name] turns to me with a very weird smirk."
            sis "So?"
            sis "What do you think, [mc_name]?"
            sis "Did you like it?"
            menu:
                "That wasn't my kind of movie.":
                    mc "It was nice but... a bit slow... and the black and white... it's not for me."
                    sis "I knew you wouldn't like it."
                    sis "I mean, it's so far from what you usually like... there was no way you could appreciate it."
                    sis "But you tried."
                    sis "I appreciate that."
                "I liked it very much. [sisLovePath]":

                    $ ProcessStat(2, "sis_affection")
                    $ DumpNotStack()
                    mc "And I may want to rewatch it very soon."
                    mc "I have probably missed a lot of things."
                    sis "Really?"
                    sis "You're mocking me, right?"
                    mc "No! I'm serious!"
                    mc "The relationship between Rick and Louis is fascinating."
                    mc "I want to see more."
                    mc "You'll have to show me more movies like this one."
                    sis "Ok... I'm a bit surprised, though..."
                    sis "I didn't expect you to enjoy it that much..."

        if ep4chosenmovie == "Lost in translation":
            scene ep4_sc12_l_19
            off "[sf_name] turns to me with a light of hope in her eyes."
            sf "You liked it, didn't you?"
            menu:
                "It was so strange...":
                    mc "I'm not sure how I really feel about this movie."
                    mc "Were they in love or not?"
                    mc "I don't think I understood everything... are they going to see each other again?"
                    mc "He could be like... her grandfather."
                    mc "I'm sorry, I feel like there's too much left unsaid for me to really enjoy that kind of movie."
                    sf "Maybe you need to watch it again to get it."
                    sf "I really like it."
                    sf "It's love, but it's complex and mostly impossible and they know it."
                    mc "It's very bitter..."
                    sf "That depends how you see it, I guess..."
                "I think I liked it... [sfLovePath]":

                    $ ProcessStat(2, "sf_affection")
                    $ DumpNotStack()
                    mc "But I'll need time to think about it..."
                    mc "I'm not used to that kind of... cerebral movies..."
                    mc "I have the feeling that I missed a lot of things, I may need to watch it again."
                    sf "I think having mixed feelings about it is quite normal, it's the complexity of it that makes the movie great."
                    sis "And boring. Definitely, boring."
                    sf "You won't fool me."
                    sf "I know you secretly love this movie as much as I do."
                    sis "Maybe in your most twisted fantasy, young lady, but not in this reality."

        if ep4chosenmovie == "Big trouble in little China":
            scene ep4_sc12_l_18
            off "[sis_name] sighs loudly."
            off "[sf_name] stays silent."
            sis "Well, it wasn't bad."
            sis "Actually, it was pretty good."
            scene ep4_sc12_l_19
            sf "It was a very strange .. mix of things."
            sf "I'm not sure it deserves the title of the greatest movie ever made, but it sure isn't a bad one."
            mc "I'm glad you liked it."
            mc "But I'm not surprised."
            mc "I was very sure of my choice."
            scene ep4_sc12_l_18
            sis "That ending, though... Is there a sequel?"
            mc "No, there's no sequel."
            sf "That's very disturbing not to know what happens next."
            mc "I think it's intended."


        off "We spend a few minutes to talk about the movie we just saw and refill our beverage stock."
        off "After a quick passage to the restroom, everyone is back in the living room, ready for the second movie."
        scene ep4_sc12_l_20
        mc "The Shining?"
        sf "It's a classic horror movie."
        mc "I've heard of it."
        sis "We thought it could be interesting, as [sf_name] and I have never seen it."
        mc "I'm not a big fan of horror movies but... why not."
        off "We take our respective places back as the movie starts."

        if sf_love_path == True:
            if sis_sub_path == True or sis_love_path == True:
                scene ep4_sc12_l_21
                $ UnlockThat("ep4/ep4_sc12_l_21")
            else:
                scene ep4_sc12_l_21_bis
                $ UnlockThat("ep4/ep4_sc12_l_21_bis")
            off "[sf_name] snuggles under my arm."
            off "She takes my hand and holds it on her belly."
            off "I can feel the jealous gaze of [sis_name] over us but she avoids making eye contact with me when I look at her."

            if sis_love_path == True:
                scene ep4_sc12_l_22
                $ UnlockThat("ep4/ep4_sc12_l_22")
                off "We're around the middle of the movie when, without any subtility, she grabs my arm, lifts it and sticks herself against me and throws my hand around her."
                off "I can feel the cold sweat running down my spine."
                off "I should move."
                off "I should say something."
                off "But I’m completely paralyzed."
                off "[sf_name] raises her head."
                off "I can't get a good look at her expression, but I can guess her eyebrows frowning."
                scene ep4_sc12_l_23
                $ UnlockThat("ep4/ep4_sc12_l_23")
                sf "What are you doing?"
                sis "What? Can't I cuddle too?"
                sf "Are you serious?"
                sis "Why wouldn't I be?"
                sf "He's my boyfriend."

                sis "And he's my childhood friend."


                off "Silence."
                off "The tension is so dense that I can barely breathe."
                sf "Fair enough."
                scene ep4_sc12_l_24
                $ UnlockThat("ep4/ep4_sc12_l_24")
                off "Both girls go back to watching the movie as if nothing happened."
                off "Neither of them even gave me a look."
                off "I don't understand what's happening."
                off "They just had a problem and settled it between them with a few words."
                off "I haven't been consulted."
                off "They obviously weren't even interested in my opinion."
                off "I suddenly feel like I'm some kind of object."
                off "Something that can be shared, maybe even lent."
                off "It's very disturbing."
                off "I spend the rest of the movie completely tetanized."
                off "Not moving an inch and barely breathing."
                off "I'm not sure either of us really enjoys the moment."
                off "I'm not even really watching the movie."
                off "My eyes are focused on it but my mind is elsewhere."

        scene black with fade
        with Pause(2)
        show text "Another movie later."
        with Pause(2)

        if sf_love_path == True and sis_love_path == True:
            scene ep4_sc12_l_25
            $ UnlockThat("ep4/ep4_sc12_l_25")
            off "The movie ends and ... Nothing happens."
            off "The girls simply talk about the movie."
            off "I can't help but silently scream inside me, what the fuck just happened?"
            off "I try to take part in the discussion but my interventions are ridiculous."
            off "Yes, the bathroom scene was disgusting."
            off "I wouldn't spend my holidays in that hotel neither."
            off "They discuss the movie as critics would do."
            off "Maybe they should make a career out of it."
            off "Ten minutes later, however, their drinks are empty and the discussion ends."
        else:
            scene ep4_sc12_l_19
            sf "Well, that was interesting."
            sis "More disturbing than horrifying I would say."
            sf "I think it's because it's an old movie."
            sf "It doesn't work on the same mechanics as modern movies."
            sf "There's no jump scare and the pace is pretty slow."
            mc "In the eighties, this film was probably terrifying."
            sf "That bathroom scene was disgusting."
            scene ep4_sc12_l_18
            sis "And the little girls.. that was very disturbing."
            off "They discuss the movie as critics would do."
            off "Maybe they should make a career out of it."
            off "Ten minutes later, however, their drinks are empty and the discussion ends."

        if sf_love_path == True:
            sf "It's getting late."
            sf "I think it's time to go to bed."
            scene ep4_sc12_l_26
            $ UnlockThat("ep4/ep4_sc12_l_26")
            off "She approaches my ear and whisper."
            sf "I'll wait for you."
            off "She kisses me on the cheek and leaves the room."

            if sis_love_path == True:
                off "[sis_name] waits a few seconds, just to be sure that [sf_name] is away."
                scene ep4_sc12_l_27
                $ UnlockThat("ep4/ep4_sc12_l_27")
                sis "If you fuck her, I'll kill you."
                mc "[sis_name]..."
                sis "If you fuck her, I will know."
                sis "She will tell me."
                sis "And I will kill you."
                sis "Is that clear?"
                off "Her voice leaves no place for discussion."
                off "She sounds angry and desperate."
                menu:
                    "I had no intention of doing such a thing, to start with... [sisLovePath]":
                        $ ep4neverwould = True
                        $ ProcessStat(2, "sis_affection")
                        $ DumpNotStack()
                    "It is.":
                        $ ep4mcunderstood = True
                        $ ProcessStat(1, "sis_affection")
                        $ DumpNotStack()
                        "I won't do that."
                sis "Great. Now go."
                sis "She's waiting for you."
                mc "Are you sure?"
                sis "It’s either that or I go talk to her..."
                sis "And I’m not ready yet."
                off "I try to make a move toward her but she pushes me away immediately."
                off "I head to [sf_name]'s bedroom with very mixed feelings."
                jump ep4dispatch

            elif sis_sub_path == True:
                off "I wait a few seconds, just to be sure that [sf_name] is away."
                scene ep4_sc12_l_28
                $ UnlockThat("ep4/ep4_sc12_l_28")
                off "I turn to [sis_name] and whisper."
                menu:
                    "I won't fuck her. [sisLovePath] [sisLoveSubPath]" if sis_sub_love_path == True:
                        mc "Do you know why?"
                        off "She nods negatively."
                        sis "Because I want to fuck you first."
                        $ ProcessStat(1, "sis_affection")
                        $ ProcessStat(1, "sis_submission")
                        $ DumpNotStack()
                    "Don't worry, Princess. [sisSubPath]":
                        mc "You are next."
                        $ ProcessStat(2, "sis_submission")
                        $ DumpNotStack()

                off "She doesn't reply but I'm pretty sure she shivers hearing these words."
                off "I slowly kiss her cheek and leave her alone while I head to [sf_name]'s bedroom."
                jump ep4dispatch
            else:
                scene ep4_sc12_l_27_bis
                off "I turn to [sis_name], a bit embarrassed."
                off "She obviously knows what [sf_name] just told me."
                mc "I guess it's good night then."
                sis "Yeah good night, perv."
                sis "I hope you remember I will kill you if you hurt her in any way."
                mc "I... remember that."
                sis "Good."
                sis "Because she's very serious about it."
                sis "If you're not, you should back out before you do something stupid."
                sis "Do you understand?"
                mc "I do."
                mc "I understand."
                sis "Great. Don't make her wait."
                off "I leave her alone and head to [sf_name]'s bedroom."
                jump ep4dispatch
        else:

            scene ep4_sc12_l_31
            off "[sis_name] and [sf_name] seem to agree that it's a good time to go to bed."
            off "They wish me goodnight and leave the room."
            off "I take care of the glasses and bottles and head to my own bedroom."
            jump ep4dispatch


label ep4dispatch:

    if sf_love_path == True:
        call ep4sc13 from _call_ep4sc13
    elif sf_dom_path == True and ep4domcontractvoid == False:
        call ep4sc14 from _call_ep4sc14

    if sis_love_path == True:
        call ep4sc15 from _call_ep4sc15
    elif sis_sub_path == True:
        call ep4sc16 from _call_ep4sc16

    if ep3sisluked == True:
        call ep4sc17 from _call_ep4sc17

    if full_neutral_path == True:
        call ep4neutralend from _call_ep4neutralend

    jump ep4end



label ep4sc13:
    scene black with fade
    with Pause(2)
    scene ep4_sc13_c_00 with fade
    off "I take a few seconds in front of [sf_name]’s door."
    off "I’m nervous as hell."
    off "You should calm down, [mc_name]. Take it easy."

    if ep4sfmorningsorry == True:
        off "You love the girl, [mc_name]."
        off "You can’t deny it now."
        if sis_love_path == True:
            off "That makes what you have to do even more difficult."

    off "Calm down."
    off "She doesn’t want to have sex with you, there’s no way she’s ready for that."
    off "She’s a virgin."
    off "She’s not the kind of girl who would throw her virginity away on the first or second day."
    off "You can relax."
    off "She wants to flirt, to fool around."
    off "You’re gonna lay on the bed kissing, maybe touching a bit for a time, it’s gonna be great."
    off "If you’re lucky, you will get a handjob."

    if ep3sfhandjob == True:
        off "Like yesterday."

    off "If you’re very lucky, you will get to finger her."
    off "Her breasts?"
    off "Maybe I’ll can touch her breasts."
    off "Yeah, for sure."
    off "Just don’t be a dumbass, be a gentleman."
    off "Be gentle."
    off "I’m a gentleman, ok."
    off "My dick is already so hard that keeping it in my shorts is very uncomfortable."

    if sis_love_path == True:
        off "Shit, I can’t do this."
        off "I can’t do this to [sis_name]."
        off "And to [sf_name]."
        off "I can't enter that room if I know that our relationship will end tomorrow."
        off "But am I sure I want to end this relationship?"
        off "Fuck."
        off "Everything was so obvious last night with [sis_name]."
        off "I had to choose one and it was [sis_name]."
        off "But today... [sf_name] made me doubt that."
        off "And... I’m pretty sure I love her too."
        off "It’s different, but it’s love too."
        off "I love both [sis_name] and [sf_name]."
        off "I don’t think they would like to hear that."
        off "Come on, [mc_name]."
        off "Do you hear yourself?"
        off "You're a moron."
        off "You don't even know what love is."
        off "Stop using a word you don't understand."
        off "You're thinking too much."
        off "Just YOLO this."
        off "What the fuck are you thinking, [mc_name]?"
        off "You need to stop listening to Steve's advice."
        off "This is serious."
        off "Maybe not life or death serious but... almost."

    off "You have to enter, [mc_name]."

    if sis_love_path == True:
        off "There’s nothing bad in cuddling and kissing."
        off "Just don’t go further."

    off "Control yourself and everything will go nicely."
    label galleryScene7:
    scene ep4_sc13_c_01
    off "I raise my hand and knock on the door."
    off "A faint voice reply from the other side."
    sf "Yes?"
    mc "It’s [mc_name]."
    sf "You can come in [mc_name]."
    off "This is it, [mc_name]."
    off "Don’t fuck this up."
    scene ep4_sc13_mbr_00
    $ UnlockThat("ep4/ep4_sc13_mbr_00")
    off "I open the door and get inside."
    off "She's changed into her night attire."
    off "She looks as terrified as I am."
    mc "Hey."
    sf "Hey."
    off "We stay like that for a while without saying a word."
    sf "[mc_name]... I’m sorry, I didn’t want to mislead you..."
    sf "I really wanted to do it with you tonight but... I just..."
    sf "I don’t know anymore..."
    off "Holy crap."
    off "Ok [mc_name]. Manage."
    off "You’re not disappointed, you’re a gentleman."
    off "Make her feel comfortable."
    off "She’s right."
    mc "It’s ok, [sf_name]."
    mc "We don’t have to do anything."
    mc "You know, I’m happy just to be with you."
    scene ep4_sc13_mbr_01
    sf "But you expected..."
    mc "I didn’t expect anything."
    off "Nicely said, [mc_name]."

    menu:
        "Except maybe cuddling a bit and having a nice talk. [sfLovePath]" if ep4sfcontrollove == True and sf_affection > 44:
            $ ProcessStat(5, "sf_affection")
            $ DumpNotStack()
            $ ep4sflovetalked = True
            sf "A talk? Really?"
            scene ep4_sc13_mbr_02
            $ UnlockThat("ep4/ep4_sc13_mbr_02")
            mc "Well, I won’t be mad if we add a kiss or two in the process."
            sf "Let’s not get restricted by unfair numbers."
            scene ep4_sc13_mbr_03
            $ UnlockThat("ep4/ep4_sc13_mbr_03")
            off "She throws her arms around my neck and kisses me."
            off "It’s a slow and tender kiss."
            off "It says thank you for not being a dork."
            off "Her body, pressed against mine is really tempting."
            off "I have a hard time controlling myself."
            off "She takes my hand and leads me to the bed."
            sf "Let’s get comfy..."
            scene ep4_sc13_mbr_36
            $ UnlockThat("ep4/ep4_sc13_mbr_36")
            off "We quickly agree on a comfortable position and she cuddles against me, smiling."
            off "She seems relieved and happy."
            sf "I was so afraid that you wouldn’t understand..."
            mc "It’s alright [sf_name]."
            mc "This isn’t something you do lightly."
            sf "And it’s so different from what I thought it would be like."
            mc "What do you mean?"
            sf "You know... Like that..."
            mc "Not really... I’m afraid you’ll have to be more explicit."
            off "Her expression changes."
            scene ep4_sc13_mbr_37
            sf "I don’t know how to say that."
            sf "I think you should know but I’m also afraid you'll see me differently afterward..."
            off "She talks like she has some kind of dark secret or something."
            off "It makes me curious."
            mc "You don’t have to tell me anything you don’t want to, [sf_name]."
            mc "But I can hear anything."
            mc "Also, anything you’ll tell me will stay between us."
            sf "I know."
            sf "I feel very comfortable with you."
            sf "I wouldn’t even think to talk about that otherwise..."
            sf "I can’t believe I’m about to tell you this."
            sf "You promise you won’t tell anyone?"
            mc "Of course."
            mc "It goes without saying."
            mc "I promise."
            sf "Well... I... for a long time..."
            sf "I thought that any relationship between a man and a woman has to be... very different from that I’m living with you."
            sf "It’s... I’ve been told... that the woman has to be more... assertive."
            mc "Assertive?"
            mc "I don’t think there’s anything bad in being assertive."
            sf "Assertive may be a bit weak... to describe..."
            sf "I’m talking about..."
            off "She has a hard time finding appropriate words and she sounds very embarrassed."
            mc "[sf_name], I’m not going to judge you or anything you will say."
            mc "You can just say it with the most brutal words that come to your mind, it will be ok."
            mc "Unless you need to say it that way, of course, you don’t have to take the gloves off and you don’t need to be embarrassed."
            scene ep4_sc13_mbr_38
            $ UnlockThat("ep4/ep4_sc13_mbr_38")
            off "She takes a deep breath."
            sf "I’ve been told that, in a relationship, if the woman doesn’t want to be reduced to an object or a toy, she has to dominate her partner, and that the domination itself can be satisfying."
            mc "Are you talking about BDSM or something like that?"
            sf "No! I mean, it can be, but it’s not like that."
            sf "It’s just... There’s the one who dominates, and the one who submits."
            sf "The one who dominates gives orders, the one who submits executes and he may, or may not receive rewards or punishment..."
            sf "But pain is optional."
            sf "I mean... Every contract is different."
            mc "A contract?"
            sf "... Yes... it’s... You need to formalize it, just to be sure."
            sf "Submission needs to be voluntary."
            sf "There shouldn’t be any constraints."
            sf "Unless the contract says so..."
            mc "Ok so.. You thought that your first relationship would of that kind?"
            mc "That you would find someone who would submit to you?"
            sf "More like I would have to make my partner submit for our relationship to be... safe for me..."
            sf "And if he didn't agree to a contract with me... to simply search someone else."
            mc "Ok... so... you want me to submit?"
            sf "No! I’m happy as we are now!"
            mc "Ok... Can I ask why you thought that every relationship had to be like that?"
            off "She doesn’t reply immediately."
            off "I can guess her carefully choosing her words."
            scene ep4_sc13_mbr_39
            sf "When I was three, my mom died."
            sf "I was alone with my dad, and he was working a lot."
            sf "Working sixty hours a week isn’t very compatible with raising a daughter, even if you love her."
            sf "He had to make a choice, to stop working and raise me or continue working and hire someone to take care of me."
            sf "Of course, we needed money to live so he choose to continue working."
            sf "He hired a nanny."
            sf "The job was a special one."
            sf "As I said, my dad works a lot, but his job also requires us to move every three or four years, often to another city, sometimes to another country."
            sf "As so, the nanny had to live with us full time and follow us when we would have to move."
            off "I can imagine the job offer : abandon your life to become a substitute mother..."
            sf "You would think it would be difficult to find someone willing to take that kind of job, but dad actually found someone pretty quickly."
            sf "And he hired her."
            off "Silence."
            scene ep4_sc13_mbr_38
            off "Does it pain her to talk about her nanny?"
            sf "I came to understand later that she was a very special person, but to me, she simply was my nanny."
            sf "She raised me."
            sf "And I loved her like a mother."
            off "She talks about her in the past tense."
            off "Did she pass away?"
            sf "She was Asian in origins but talked like an old English lady."
            sf "She would only wear those tight Asian dresses, as black as night, with bright red half-heeled pumps."
            sf "She taught me a lot of things, about life, and about people."
            sf "To not let other people hurt me in any way, to be strong, to be the one to decide for myself."
            sf "She was very strict but I have no doubt that she loved me like her own daughter, even if she never said so."
            off "It looks like she was quite a singular nanny for a singular little girl."
            scene ep4_sc13_mbr_39
            sf "I never talked about that with him and I don’t know either when or how it started, but she also came to... form some kind of relationship with my father."
            sf "Of course, I wasn’t supposed to witness that, but I did... multiple times."
            sf "The first time was an accident but in the end... I was just spying on them."
            sf "She was the dominant one, he was the submissive one."
            sf "She did things to him, and it was obvious that he liked every second of it."
            sf "I don’t think I need to describe it further."
            sf "After that I... documented myself."
            off "Holy shit."
            off "Watching your parents doing the naughty is already pretty fucked up, but when they're into that kind of kinky stuff..."
            off "Ok [mc_name], say something."
            off "Show her you don’t judge her or anything."
            scene ep4_sc13_mbr_37
            mc "How old were you at the time?"
            sf "You mean when I saw them?"
            mc "Yes."
            sf "I was twelve I think. Maybe thirteen."
            off "A nice way to fuck up your incoming puberty."
            mc "You’re talking about her in the past tense..."
            sf "She left us three years ago."
            sf "Just as we were about to move to this town, she just left a letter saying she had to go, and disappeared."
            off "Her story is as strange as it is sad."
            off "It sounds like something out of a novel or a movie."
            off "Who does that in real life?"
            mc "It must have been hard for you..."
            sf "I still think about her a lot."
            off "She turns to me."
            sf "So.. You don’t think I’m a deviant or something?"
            mc "What? No! Why would I?"
            mc "I told you I wouldn’t judge you."
            mc "Actually, I think that you wouldn’t be you without everything you lived until now."
            mc "And I like the you who’s here with me right now."
            mc "However, I understand your apprehensions a lot better ."
            scene ep4_sc13_mbr_40
            $ UnlockThat("ep4/ep4_sc13_mbr_40")
            off "She smiles."
            sf "Thank you."
            mc "I don’t know why you’re thanking me but you’re welcome."
            mc "By the way... You just told me a lot about yourself and I feel like I should reciprocate but... I don’t really see what’s to be said about me..."
            off "She laughs."
            sf "Don’t worry about that."
            sf "I already know a lot."
            mc "Really?"

            sf "Really. For the last three years, your childhood friend couldn’t shut up about you."

            mc "Are you kidding me?"
            sf "Of course she often told me that you were an asshole and so on, but also how you were strong with this or that, that you’ve done this or liked that."
            scene ep4_sc13_mbr_36
            sf "As a consequence, I’m pretty confident in my knowledge of you."
            mc "I don’t know how I should feel about that."
            sf "Proud. Girls talk about you."
            sf "A lot of boys would like that."
            mc "I have no doubt about that."
            off "We talk a bit more about insignificant things and exchange a couple of kiss before I respectfully take my leave."
            scene ep4_sc13_c_03 with fade
            off "Her story about her nanny was... touching."
            off "The way she talked about her..."
            off "She seemed so vulnerable..."
            off "That woman was obviously very important to her."
            off "She’s not exaggerating when she says that she loved her like a mother."
            off "Losing her must have been devastating."
            off "Also, the kind of education she received probably doesn’t favor a classic love relationship."
            off "I understand why she keeps telling me that all of this is new, and she doesn’t know how to manage."
        "Except maybe a kiss or two.":

            $ ProcessStat(3, "sis_affection")
            $ DumpNotStack()
            $ ep4sflovelicked = True
            off "She smiles."
            off "The fear evacuates the room."
            scene ep4_sc13_mbr_02
            $ UnlockThat("ep4/ep4_sc13_mbr_02")
            sf "That, I can do."
            scene ep4_sc13_mbr_03
            $ UnlockThat("ep4/ep4_sc13_mbr_03")
            off "She throws her arms around my neck and kisses me."
            off "It’s a slow and tender kiss."
            off "It says thank you for not being a dork."
            off "Her body, pressed against mine is really tempting."
            off "I have a hard time controlling myself."
            scene ep4_sc13_mbr_04
            sf "You can... touch me if you want."
            off "She felt it."
            off "Holy fucking shit."
            off "Focus, [mc_name], don’t just grope her like some disgusting pig would do."
            mc "I didn’t want to make you... Uncomfortable."
            off "Her ass is just there and I have permission to touch it."
            off "What the fuck am I waiting for?"
            off "I can grab her boobs, dammit!"
            off "Why the fuck am I still talking!"
            off "Cool the fuck down, dude!"
            off "Be gentle at least!"
            sf "It’s ok. And actually... I want to touch you too."
            off "I go for another kiss."
            scene ep4_sc13_mbr_06
            $ UnlockThat("ep4/ep4_sc13_mbr_06")
            off "My hands quickly crawl to her ass."
            off "I try to be as gentle as firm while grabbing it but I'm not sure I'm in complete control of my actions."
            off "The animal side of my brain is slowly but surely getting the upper hand."
            scene ep4_sc13_mbr_05
            $ UnlockThat("ep4/ep4_sc13_mbr_05")
            off "Of course, I overdo it."
            off "I grab her ass with both hands."
            off "I grope her mercilessly."
            off "God, that ass is unreal."
            off "Ok, it’s the first one I’m touching, but it’s so perfect!"
            off "She lets out a little scream and laughs."
            scene ep4_sc13_mbr_07
            mc "I’m sorry, I’ve gone too far."
            sf "It’s ok, [mc_name]."
            sf "I just wasn’t expecting so much passion."
            sf "Do you really like my ass that much?"
            mc "How can you doubt it?"
            mc "I thought it was .. Obvious."
            sf "It is, now."
            sf "By the way... I’m at a disadvantage here."
            sf "You’re wearing so many clothes."
            off "That doesn’t need any further discussion."
            off "I take a step back and 3 seconds later, my t-shirt and my shorts are lying on the ground."
            scene ep4_sc13_mbr_08
            $ UnlockThat("ep4/ep4_sc13_mbr_08")
            off "I’ve just got rid of my underwear when I suddenly have a flash of decency and remember I’m actually not some perverted beast about to jump on his innocent prey."
            off "Her eyes are locked on my crotch."
            off "My cock is proudly erect."
            off "It’s ridiculous."
            sf "You’re already..."
            mc "Well... Being with you is very... stimulating."
            off "She seems to hesitate for a few seconds."
            off "Did my dick freak her out?"

            if ep3sfhandjob == False:
                sf "Last night I... chickened out when I saw you were... hard. I’m sorry."
                mc "You don’t have to be sorry, [sf_name]."
                sf "The truth is I couldn’t stop thinking about it afterward."
                sf "I’m... curious about it."
                sf "I’m a bit ashamed."
                mc "[sf_name], there’s nothing to be embarrassed about."
                mc "You can ask whatever you want."

            sf "It’s as big as in a porn movie."
            mc "I... don’t think so."
            sf "To be honest I hoped it would be a little smaller."
            mc "Really? I thought that most of the girls liked it .. Bigger... To be honest, I was afraid not to be... large enough."
            sf "Oh, you’re large enough, without a doubt."
            scene ep4_sc13_mbr_09
            off "She looks at me with a shy and embarrassed expression."
            sf "I don’t want you to misunderstand me."
            sf "I’m still not ready to have sex..."
            mc "I’m not misunderstanding anything."
            sf "Good."
            scene ep4_sc13_mbr_10
            $ UnlockThat("ep4/ep4_sc13_mbr_10")
            off "Holy shit."
            off "She just..."
            scene ep4_sc13_mbr_11
            $ UnlockThat("ep4/ep4_sc13_mbr_11")
            off "Holy shit."
            off "Oh my God."
            off "Holy shit."
            scene ep4_sc13_mbr_12
            $ UnlockThat("ep4/ep4_sc13_mbr_12")
            off "Holy fucking shit."
            off "I’m hyperventilating."
            scene ep4_sc13_mbr_13
            $ UnlockThat("ep4/ep4_sc13_mbr_13")
            off "Holy mother of god."
            off "Holy shiiiiit!"
            scene ep4_sc13_mbr_14
            $ UnlockThat("ep4/ep4_sc13_mbr_14")
            off "Calm down, [mc_name]."
            off "Keep breathing like that and you're gonna pass out."
            off "Calm the fuck down!"
            off "My dick is pulsating on her own."
            off "I’m about to blow my load just from seeing her undressing."
            off "Say something, [mc_name]."
            off "Come on."
            scene ep4_sc13_mbr_15
            $ UnlockThat("ep4/ep4_sc13_mbr_15")
            sf "Are you... disappointed?"
            off "Say something or she’s going to freak out!"
            mc "I’m sorry, [sf_name]... I’m not disappointed at all."
            mc "I’m a bit overwhelmed right now."
            mc "How could I be disappointed?"
            mc "You’re so beautiful."
            scene ep4_sc13_mbr_16
            $ UnlockThat("ep4/ep4_sc13_mbr_16")
            sf "You really think so?"
            sf "You don’t think I’m fat or something like that?"
            mc "What? No! You’re not fat."
            mc "How can you think that?"
            off "How a girl so perfect can be so insecure about her body is totally beyond me."
            mc "I’m sorry [sf_name], I can’t help but stare at... you."
            mc "I’m having a really hard time controlling myself right now."
            sf "I guess I’ll take that as a compliment."
            sf "What... Would you do if you weren’t... Controlling yourself?"
            mc "Well... I would lay you on this bed and..."
            mc "I would probably spend some time touching and kissing you..."
            off "She looks at the bed for a few seconds."
            off "She’s going to freak out."
            off "I should have shut the fuck up."
            scene ep4_sc13_mbr_17
            sf "You’re talking about this bed?"
            off "What’s with that question?"
            mc "I don’t see any other one here..."
            sf "You don’t have any problem doing that kind of thing on your parents’ bed?"
            mc "To be honest I didn’t even think about it... and I don’t think it matters to me right now."
            sf "Do you want me to lay on my back? Or on my stomach?"
            off "Did I hear that right?"
            off "Oh, my god"
            mc "You could start on your stomach... And then..."
            scene ep4_sc13_mbr_18
            $ UnlockThat("ep4/ep4_sc13_mbr_18")
            off "She slowly gets on the bed."
            off "She looks at me."
            off "She seems as afraid as eager for me to do something."
            off "Calm down [mc_name], you’re breathing like a degenerate again."
            scene ep4_sc13_mbr_19
            off "I join her on the bed and try to find a position comfortable that will allow me to explore her."
            off "I want to go straight to kneading her ass like my life depends on it, but I manage to control myself."
            off "I try to gently touch her back and caress her."
            off "I have no idea what I’m doing or how to do it."
            off "I feel clumsy and ridiculous as hell."
            off "My god, her skin is so soft."
            off "Her breathing accelerates as my hand slowly slides on her back."
            scene ep4_sc13_mbr_20
            $ UnlockThat("ep4/ep4_sc13_mbr_20")
            off "I contort myself and kiss her spine."
            off "She shivers."
            off "I struggle to restrain myself."
            scene ep4_sc13_mbr_21
            $ UnlockThat("ep4/ep4_sc13_mbr_21")
            off "My left hand crawls to her ass and I gently grab one of her cheeks."
            off "My fingers are slipping between her buttocks."
            off "I’m losing it."
            off "I get behind her and try to spread her thighs but she resists."
            scene ep4_sc13_mbr_22
            off "She tries to turn her head towards me but she can't really see what I'm doing."
            sf "[mc_name]... please..."
            off "Her voice..."
            off "She sounds completely terrified."
            off "She probably thought I was about to rape her ass or something."
            mc "I'm sorry [sf_name], I didn't want to frighten you."
            mc "I... want to lick you."
            sf "To lick me?"
            mc "Yes. Do you want me to stop?"
            mc "I'm sorry if I did anything wrong."
            sf "It's... It's ok. I thought... I'm sorry."
            mc "Don't be. You sure, you want me to continue?"
            sf "Yes..."
            off "She relaxes a bit but she's still a bit tense."
            scene ep4_sc13_mbr_23
            $ UnlockThat("ep4/ep4_sc13_mbr_23")
            off "She spreads her legs herself."
            sf "Is that... Ok?"
            off "Oh my God."
            off "What a view."
            off "Say something [mc_name] or she going to freak out again."
            mc "It’s great, [sf_name]."
            off "I try to go down on her from my position but I quickly understand that it will be difficult and uncomfortable."
            mc "I’m going to drag you to a more comfortable position."
            sf "O... Ok..."
            off "I get down from the bed and grab her legs."
            off "She lets out a little scream of surprise when I drag her to me."
            scene ep4_sc13_mbr_24
            $ UnlockThat("ep4/ep4_sc13_mbr_24")
            off "I clutch her buttocks with both hands."
            scene ep4_sc13_mbr_25
            off "God, I like this ass."
            scene ep4_sc13_mbr_26
            $ UnlockThat("ep4/ep4_sc13_mbr_26")
            off "I spread her butt as tenderly as I can."
            off "I was about to play with her pussy when I notice that her butthole looks exceptionally clean."
            off "I wonder if everyones butthole is that clean or if she takes special care of it."
            off "I have never thought of it but..."

            menu:
                "Lick her butthole. [sfDomPath]":
                    $ ProcessStat(1, "sf_affection")
                    $ ProcessStat(1, "sf_dominance")
                    $ DumpNotStack()
                    $ ep4sfbuttholelicked = True
                    off "Fuck it, you only live once."
                    scene ep4_sc13_mbr_27
                    $ UnlockThat("ep4/ep4_sc13_mbr_27")
                    off "I go for her ass hole like there's no tomorrow."
                    off "She suddenly tenses up."
                    sf "[mc_name]? That isn’t my... Oh my god."
                    off "She shivers."
                    sf "It tickles... Are you sure?"
                    off "It doesn’t taste nor smell bad."
                    off "Actually, it tastes pretty nice."
                    off "Like the rest of her."
                    off "I let my tongue run wild on her."
                    off "[sf_name] moans lightly."
                    off "It doesn’t seem to tickle anymore."
                    off "I try to push further but her hole is so tightly closed that I quickly understand I don’t have any chance to get my tongue inside her ass."
                    scene ep4_sc13_mbr_28
                    off "I continue eating her ass and bring my fingers to her pussy."
                    off "She instantly gasps and starts moaning louder when I start playing with her clitoris."
                    sf "[mc_name]... Oh my god!"
                    off "I make it gently roll under my thumb."
                    off "She was already wet when I got down on her, but she’s now properly dripping."
                    off "I may have to wash those sheets before my parents return."
                    scene ep4_sc13_mbr_29
                    $ UnlockThat("ep4/ep4_sc13_mbr_29")
                    off "I slide my thumb inside her."
                    sf "Haaaaan!"
                    off "She moans a lot, sometimes louder than others, but I can’t be sure I've made her come."
                    off "I don’t know if I’m simply failing at it or if she’s so stressed out that she just can’t give in."
                    off "I really have a strange impression that she’s trying to endure it more than to enjoy it."
                    off "I don’t know how long I stay like that, working on her butthole and her pussy."
                    off "I stop when my tongue gets numb."
                "Lick her pussy. [sfLovePath]":

                    $ ProcessStat(2, "sf_affection")
                    $ DumpNotStack()
                    $ ep4sfpussylicked = True
                    scene ep4_sc13_mbr_30
                    $ UnlockThat("ep4/ep4_sc13_mbr_30")
                    off "I go for her pussy like there’s no tomorrow."
                    off "She suddenly tenses up and gasps."
                    sf "Oh my God..."
                    off "A little too late I understand that this position is not ideal for the job."
                    off "My nose is pushing against her butt hole."
                    off "It doesn’t smell bad nor anything, it’s just a bit disturbing."
                    off "I should have asked her to lay on her back."
                    off "It’s too late now."
                    sf "Oh my Goooood..."
                    scene ep4_sc13_mbr_31
                    off "I try licking various parts of her pussy, slowly, gently, harder, faster."
                    off "I try everything, with various results."
                    scene ep4_sc13_mbr_32
                    $ UnlockThat("ep4/ep4_sc13_mbr_32")
                    off "She moans a lot, sometimes louder than others, but I can’t be sure I've made her come."
                    off "I don’t know if I’m simply failing at it or if she’s so stressed out that she just can’t give in."
                    off "I really have a strange impression that she’s trying to endure it more than to enjoy it."
                    off "I don’t know how much time I spend liking her."
                    off "I stop only when my tongue is completely numb."

            scene ep4_sc13_mbr_33
            $ UnlockThat("ep4/ep4_sc13_mbr_33")
            off "I crawl back on the bed and lay next to her."
            off "I grab a couple cushions to get more comfortable and we lay there."
            off "She seems exhausted."
            off "My penis is going mostly flaccid."
            mc "I hope I didn’t go too far..."
            scene ep4_sc13_mbr_34
            $ UnlockThat("ep4/ep4_sc13_mbr_34")
            if ep4sfbuttholelicked == True:
                sf "No, [mc_name]. It’s ok."
                sf "I was just... Really surprised."
                sf "It’s the first time someone has licked that part of me."
                sf "It felt very strange."
                sf "That wasn’t unpleasant though."
                mc "That was a first for me too."
                mc "I don’t really know how I got this idea, I just saw your butthole and... I found it very... seducing."
                sf "Seducing? My butthole?"
                off "She laughs."
                mc "Next time I’ll try something more conventional."
            if ep4sfpussylicked == True:
                sf "No, [mc_name]. It’s ok."
                sf "I was just... a bit too stressed out to really enjoy it fully."
                sf "When you got behind me I kind of panicked."
                sf "I’m sorry, I should have trusted you."
                mc "I should have told you what I was doing."
                mc "However, I don’t really understand how you came to think I could rape you."
                sf "I never thought you could rape me... but.. Fear isn’t rational."
                mc "I guess so."
                mc "Next time will be better."

            sf "I’m looking forward to it."
            sf "Now I think I’m going to get some sleep and I don’t think I can even close my eyes if you stay here with me."
            mc "I wouldn’t either."
            mc "I’ll let you rest."
            scene ep4_sc13_mbr_35
            $ UnlockThat("ep4/ep4_sc13_mbr_35")
            mc "Good night [sf_name]."
            sf "Good night [mc_name]."
            off "I quickly put my underwear on and grab my other clothes before leaving for my own room."
            scene ep4_sc13_c_02 with fade

            if sis_love_path == True:
                off "What the fuck have I done?"
                off "I didn’t think about [sis_name], not even for a second."
                off "What kind of asshole am I?"
            else:
                off "Damn, I didn’t touch her breasts."
                off "I’ll have to take extra care of them, next time."
                off "I can’t believe how lucky I am."
    return


label ep4sc14:
    scene black with dissolve
    with Pause(2)
    show text "Later that night."
    with Pause(2)
    scene ep4_sc13_mcr_01 with fade
    off "[sf_name] promised me that she would reward me tonight but she probably changed her mind."
    off "That was so bizarre, this morning in the living room."
    off "I somehow can still feel her fingers in my mouth."
    off "She managed to make me forget my doubts."
    off "I can’t believe I’m so weak to girls."
    off "I didn’t tell her I wasn’t interested anymore."
    off "She barely suggests we could eventually have sexual intercourse and I’m ready to get on all fours and lick her feet."
    off "I’m pathetic."
    off "I’ll tell her tomorrow that I’m not interested in her games anymore."

    if sis_love_path == True or sis_sub_love_path == True:
        off "I just hope it won't trigger her suspicion."
        off "I don't want her to uncover what's going on between [sis_name] and me."
    elif sis_sub_path == True and sis_sub_love_path == False:
        off "Besides, I don’t need [sf_name] to get laid."
        off "[sis_name] will be ready soon."
        off "I’ll tease her until she begs for my cock."
        off "She will impale herself on my dick soon enough."
        off "It’s a matter of days I just have to be patient."

    if sis_love_path == True or sis_sub_path == True:
        off "I’ve been waiting for [sf_name] to snore for half an hour now."
        if sis_love_path == True:
            off "I can’t join [sis_name] unless I’m sure [sf_name] is sleeping."
        if sis_sub_path == True:
            off "I can’t go and play with [sis_name] unless I’m sure [sf_name]’s sleeping."

        off "Will she even snore?"
        off "She didn’t drink much."
        off "Barely a couple glass in nearly four hours."
        off "She was perfectly sober when she left for bed."
        off "Maybe she’s already sleeping and simply won’t snore."
        off "I’ll have to take my chance or I may end up waiting all night long for nothing."

    scene ep4_sc13_mcr_00
    off "The vibration of my smartphone on my bedside table almost startled me. What the fuck is wrong with you people texting me in the middle of the night?"
    off "Fuck. It’s [sf_name]."
    sf "Don’t make me wait any longer."
    sf "Come. Now."
    off "So... She didn’t forget..."
    off "And she’s summoning me."
    off "Does she really think I’m her dog or something?"

    off "I should tell her immediately that I won’t come and that I want to end our... contract."
    off "However, I have the feeling that it may not go smoothly."
    off "What if she makes a scene about it?"
    off "I don’t want [sis_name] to learn about what I’ve done with her friend last night."

    off "I can’t believe I’m really considering obeying her."

    if ep3ballscrushed == False:
        off "She gave me a footjob, ok."
        off "But she also made me lick my own cum."
        off "And barely treated me like a human being."
        off "That was so humiliating..."
    else:
        off "She crushed my balls and treated me like shit."
        off "How could I be so forgetful about that?"

    off "But she kind of promised me her pussy..."
    off "Come on, dude."
    off "You can’t be that dumb."
    off "She promised you shit."
    off "She just made sure you would answer her call."
    off "I can’t be sure about that."
    off "Maybe she’s really about to let me fuck her."
    off "I’ll go see her, just this time."
    scene ep4_sc15_c_01
    $ UnlockThat("ep4/ep4_sc15_c_01")
    off "Fuck, I’m doing this."
    off "You only live once."
    off "Steve wouldn’t even hesitate."

    off "I mostly immediately regret knocking on her door, but it’s too late."
    sf "Come in."
    label galleryScene8:
    scene ep4_sc15_mbr_00
    $ UnlockThat("ep4/ep4_sc15_mbr_00")
    off "I enter the room and close the door behind me."
    off "The lights are down."
    off "[sf_name] sits on the chair by the window."
    off "Ok, [mc_name]."
    off "Now that you’re here, you’d better think carefully about what you want to achieve and how to behave to get it."
    scene ep4_sc15_mbr_01
    sf "I’m glad you came, [mc_name]."
    sf "I was afraid you'd changed your mind."
    off "This is it, [mc_name], if you want to get out of this, you have to say something, now!"
    sf "You are my first partner, and I may be a bit inexperienced, but I can promise you that you will like what’s about to come."
    off "Promises, again."
    off "When will I see that pussy?"
    scene ep4_sc15_mbr_02
    $ UnlockThat("ep4/ep4_sc15_mbr_02")
    sf "But I don’t want to go on with someone who lacks resolve."
    sf "[mc_name], before we go further, I want to renew our agreement."
    off "Her voice has a very strange tone."
    off "She moans softly."
    off "Is she...?"
    off "It’s pretty dark in here and I can’t see much."
    scene ep4_sc15_mbr_03
    sf "If you agree to continue, you understand that, unless you behave perfectly, there will be punishments as well as rewards."
    sf "And there will be pleasure, for both of us."
    off "She moans again."
    off "Her breathing is heavy."
    scene ep4_sc15_mbr_04
    $ UnlockThat("ep4/ep4_sc15_mbr_04")
    off "She’s masturbating."
    off "Right in front of me."
    off "Right now."
    off "Holy shit."
    sf "If you refuse, you can walk out of this room and we will go on as if nothing ever happened between the two of us."
    off "She’s trying to arouse you, [mc_name]."
    off "Well, it’s working."
    sf "I know you’re interested in one thing, and one thing only."
    sf "You want to fuck me."
    sf "And it’s there, almost in your grasp."
    sf "You just have to follow the path I draw for you."
    sf "Will you take it?"
    off "It’s almost there."
    off "If I play her game, I’ll fuck her soon."
    off "What do I say? Is it worth it?"

    menu:
        "I’m sorry [sf_name], I don’t want to continue. [red]\[Ends Relationship\]":
            scene ep4_sc15_mbr_05
            $ UnlockThat("ep4/ep4_sc15_mbr_05")
            $ ep4dompathended = True
            mc "When I first accepted I thought we were going for a classic boyfriend/girlfriend relationship, but..."
            mc "We’re very far from that."
            mc "That... game... It’s not for me."
            mc "I’m sorry."
            sf "It’s ok, [mc_name]."
            sf "I understand."
            sf "As I said, we’ll go on as if nothing ever happened."
            sf "You can go."
            sf "I have things to do on my own."
            sf "Good night [mc_name]."
            mc "Good night [sf_name]."
            scene ep4_sc15_c_02
            off "I leave the room quietly."
            off "Her voice sounded sad and disappointed."
            return
        "I want to continue, my lady. [sfDomPath]" if sf_dominance > 9:
            scene ep4_sc15_mbr_06
            $ UnlockThat("ep4/ep4_sc15_mbr_06")
            $ ProcessStat(5, "sf_dominance")
            $ DumpNotStack()
            sf "I’m glad to hear it."


    sf "What are you waiting for, [mc_name]?"
    sf "Lose your shorts."
    off "I comply immediately."
    sf "Touch yourself."
    scene ep4_sc15_mbr_07
    $ UnlockThat("ep4/ep4_sc15_mbr_07")
    off "She wants me to jerk off? No problem."
    off "My shaft is already hard."
    off "I start working on my dick slowly."
    scene ep4_sc15_mbr_08
    $ UnlockThat("ep4/ep4_sc15_mbr_08")
    off "She gets up from the chair and swiftly removes her panties."
    off "She walks around me, pantie-less."

    if ep4kfmeettold == True or ep4kflatetold == True:
        sf "Tell me, [mc_name]. What did you hope to achieve by lying to me?"
        off "Fuck."
        off "I guess I’m in for a punishment."
        sf "You met this girl behind my back, [mc_name]."
        off "That’s not very gentlemanly."
        off "Gentlemanly... Ok, maybe there’s still a way to talk through that."
        off "Use what you know about her."
        off "You know what she likes..."

        menu:
            "I’m sorry, my lady.":
                mc "That wasn't my intention."
                mc "I was curious and wanted to investigate the situation."
                mc "I was afraid you would uselessly worry, had you known what I was about to do."
            "I have no excuses. [sfDomPath]":

                $ ProcessStat(2, "sf_dominance")
                $ DumpNotStack()
                mc "I’m sure you know that it wasn't my intention but whatever my motivations, I’m ready to fully assume my responsibilities."
                mc "I’m sorry, my lady."

        sf "I see..."
        sf "Tell me, [mc_name], what did you think of her?"
        sf "Is she pretty?"
        off "She doesn’t like lies, [mc_name]..."
        off "Be careful."

        menu:
            "She is. [sfDomPath]":
                $ ProcessStat(2, "sf_dominance")
                $ DumpNotStack()
                mc "I won’t lie to you, my lady."
                mc "She is pretty."
                mc "She obviously can’t compare to you, but still."
            "She is not.":

                mc "And even if she was, nothing can compare to you."

        sf "Did you believe her, [mc_name]?"
        sf "Did you trust her?"

        menu:
            "Yes. I believe her. [sfDomPath]":
                $ ep4kfdombelieved = True
                mc "I think she really is ashamed of what she has done to you and [sis_name], along with other things."
                mc "She has a lot of regrets."
            "I don’t trust her.":

                $ ProcessStat(-2, "sf_dominance")
                $ DumpNotStack()
                mc "But it doesn’t matter."
                mc "She doesn’t matter to me."

        off "She sighs."
        sf "I don’t know what to do, [mc_name]."
        sf "You agree that you deserve a punishment, but I’m not sure I want to punish you."
        sf "You brought us some valuable information."
        scene ep4_sc15_mbr_09
        $ UnlockThat("ep4/ep4_sc15_mbr_09")
        off "She gently grabs my dick."
        off "Soft at first, her clutch gradually hardens."
        sf "You are lucky, [mc_name]."
        sf "I’m not in the mood for punishment."
        sf "Next time I won't be so magnanimous..."
        sf "Get on the bed."
    else:
        sf "You know what I expect from you, [mc_name]?"
        sf "Greatness."
        sf "You’re not planning to disappoint me, are you?"
        mc "No my lady."
        mc "I only aim to please you."
        scene ep4_sc15_mbr_09
        $ UnlockThat("ep4/ep4_sc15_mbr_09")
        off "She grabs my dick."
        off "Gently at first, her clutch gradually hardens."
        off "Weirdly, it’s not unpleasant."
        sf "I trust you, [mc_name]."
        sf "I know you won’t fail me."
        sf "Get on the bed."

    off "You won’t have to say that twice, my lady."
    scene ep4_sc15_mbr_10
    $ UnlockThat("ep4/ep4_sc15_mbr_10")
    off "I lay on the bed and she quickly gets on top of me."
    off "It’s happening."
    off "I’m going to get laid!"
    off "I can see her pussy."
    off "I’m going to fuck that pussy! Holy shit!"
    sf "It’s important for me to be fair."
    sf "Do you understand?"
    off "I nod."
    off "Whatever you want, baby!"
    sf "Good."
    scene ep4_sc15_mbr_11
    $ UnlockThat("ep4/ep4_sc15_mbr_11")
    off "She turns herself and promptly sit on my face."
    off "Holy mother of god."
    off "She moves a bit to find a suitable position."
    off "Her pussy comes right on my mouth."
    off "I’m a bit confused and surprised."
    off "She didn’t give me any clear instruction but the fact that she’s rubbing her vagina against my mouth probably means I have to use my tongue."
    off "I start licking right away."
    off "I’m a bit afraid of touching her in any other way but I finally grow the balls to grab her ass."
    off "God this is wonderful."
    scene ep4_sc15_mbr_12
    $ UnlockThat("ep4/ep4_sc15_mbr_12")
    off "She grabs my cock and starts stroking it."
    off "My hands clutch her ass."
    off "I knew it."
    off "I knew this agreement was worth it."
    off "I’m even more convinced when I start feeling her tongue playing with my glans."
    scene ep4_sc15_mbr_13
    $ UnlockThat("ep4/ep4_sc15_mbr_13")
    off "Oh my fucking God, she’s sucking on my cock!"
    off "She makes me shiver and for a second I stop licking her pussy."
    off "She uses her mouth as much as her hands."
    off "My whole shaft is stimulated."
    off "I’m not gonna last long."
    off "I play with her clitoris for a time."
    off "My tongue is exploring every part of her pussy but I have a very hard time concentrating on what I’m doing while trying not to ejaculate."
    off "Oh shit!"
    off "I’m losing the fight!"
    off "Oohhhhhhhh!"
    off "Aaah! "
    scene ep4_sc15_mbr_14
    $ UnlockThat("ep4/ep4_sc15_mbr_14")
    off "I unload in her mouth."
    off "Holy shit."
    off "She sucks all my strength along with my cum."
    off "That was incredible."
    off "I’m not sure I serviced her very well though."
    scene ep4_sc15_mbr_15
    $ UnlockThat("ep4/ep4_sc15_mbr_15")
    off "She turns herself and grabs my head gently."
    off "Wanna kiss?"
    off "Sure."
    scene ep4_sc15_mbr_16
    $ UnlockThat("ep4/ep4_sc15_mbr_16")
    off "What the...?"
    off "That’s my cum!"
    off "She filled my mouth with my own cum!"
    scene ep4_sc15_mbr_17
    $ UnlockThat("ep4/ep4_sc15_mbr_17")
    sf "And you’d better swallow, asshole."
    sf "Maybe you thought it would be fun to feed me your semen?"
    sf "Enjoy it yourself."
    off "Fuck. There’s so much..."
    off "I struggle a few seconds and finally manage to swallow everything."
    off "I swallowed semen."
    if ep3ballscrushed == False:
        off "For the second time. Shit."

    scene ep4_sc15_mbr_18
    $ UnlockThat("ep4/ep4_sc15_mbr_18")
    off "She gets up from the bed and stares at me."
    sf "You didn’t make me come."
    sf "I’m seriously disappointed."
    mc "I’m sorry. I was... a bit overwhelmed..."
    sf "You have no excuses."
    scene ep4_sc15_mbr_19
    off "She switches the light on and puts her panties back on."
    mc "I can still..."
    sf "No, you can’t."
    off "The mood seems to have gone to shit."
    off "You’d better stop arguing, [mc_name]."
    off "She sighs."
    sf "Do you want to have sex with me, [mc_name]?"
    off "Holy shit."
    off "Is that going to happen, now?"
    mc "Yes, my lady."
    sf "Do you think you deserve it?"
    mc "I’ll do whatever my lady wants me to do to prove myself worthy."
    sf "Really? I wonder."
    scene ep4_sc15_mbr_20
    $ UnlockThat("ep4/ep4_sc15_mbr_20")
    off "She looks at my dick."
    off "I’m slowly going soft."
    sf "I have a rule."
    sf "If you want to insert something inside me, you have to take as much inside you first."
    off "What?"
    sf "I don’t doubt you can take some."
    sf "But you’re... well endowed."
    sf "Can you take as much?"
    off "What is she talking about?"
    off "Take as much inside me?"
    mc "I’m sorry my lady, I don’t understand."
    sf "I’m not a savage."
    sf "I understand you can’t take it whole for your first time."
    scene ep4_sc15_mbr_21
    off "She disappears in the bathroom and comes back a few seconds later."
    scene ep4_sc15_mbr_22
    $ UnlockThat("ep4/ep4_sc15_mbr_22")
    sf "We’ll take it slow."
    sf "One step at a time."
    off "WHAT THE FUCK?"
    sf "I can see you’re struggling to understand."
    sf "Let me be more explicit."
    sf "You want to fuck me."
    sf "I’m ok with it, at the condition that I fuck you first."
    sf "We’ll take it slow."
    off "She wants to fuck my ass."
    off "With that thing"
    off "My cock goes flaccid in a second."
    off "I wasn’t drunk but I’m kind of sobering up instantly."
    off "That’s probably the adrenalin rushing through my brain."
    $ ep4mcassfucked = True

    menu:
        "No fucking way.":
            $ ep4reluctantsodom = True
            scene ep4_sc15_mbr_23
            $ UnlockThat("ep4/ep4_sc15_mbr_23")
            mc "I’m sorry my lady, I don’t want to disappoint you but, I’m not sure I want to take anything... Inside me..."
            sf "Oh? You’re not sure?"
            sf "So, you’re expecting me to accept your dick inside me while you don’t accept anything inside you?"
            mc "Well... Women are women, and men are men..."
            mc "It’s natural order..."
            mc "Girls are supposed to take it, boys are not..."
            sf "That’s bullshit."
            sf "Do you want to have sex with me?"
            mc "Of course, but..."
            sf "There is no but."
            sf "I’m going to put this thing in your ass, now."
            sf "Take the position."
            mc "My lady, I can’t..."
            sf "Do I look like I care?"
            sf "Take the position."
            mc "My lady..."
            sf "I said, take the position!"
            off "Fuck, it better worth it!"
            off "If anyone finds out about this I’m finished."
            off "It doesn’t look too big, though."
            off "At least I’m being fucked by a girl."
            scene ep4_sc15_mbr_24
            $ UnlockThat("ep4/ep4_sc15_mbr_24")
            off "I go on all fours and show her my anus."
            sf "Good."
            off "I can feel her hand on my ass."
            off "She spits in my butthole, probably to lubricate it."
            sf "You’d better relax if you want to enjoy it."
            off "Like I could relax in this situation."
            off "What the fuck am I doing here?"
            off "God! Help me!"
            scene ep4_sc15_mbr_25
            off "I can feel the cold kiss of her sex toy."
            off "It presses lightly against my anus before progressively entering me."
            scene ep4_sc15_mbr_26
            mc "Holy shit!"
            off "It feels way bigger than it looked."
            sf "I told you to relax, [mc_name]."
            sf "You can take it."
            sf "It’s not so big."
            scene ep4_sc15_mbr_27
            $ UnlockThat("ep4/ep4_sc15_mbr_27")
            off "I swear, bitch, I’m going to fuck you like a goddamn beast."
            off "I’ll ravage that little pussy of yours."
            off "The toy progress further."
            off "It’s not fully inside that I already want to puke."
            off "I want to shit myself."
            sf "How do you like it so far, [mc_name]?"
            sf "Feeling good?"
            mc "Not so much."
            scene ep4_sc15_mbr_29
            sf "You’ll come to enjoy it."
            off "She plays with the toy, pushing it and rotating it."
            off "I feel like my ass is about to give up."
            off "She’s going to tear me apart."
            scene ep4_sc15_mbr_28
            sf "I told you you could take it."
            mc "Is it done? Can you take it out now?"
            scene ep4_sc15_mbr_27
            sf "Take it out? [mc_name], we've barely begun."
            scene ep4_sc15_mbr_26
            off "I can feel the plug going in and out, slowly."
            scene ep4_sc15_mbr_27
            off "She’s fucking my ass."
            scene ep4_sc15_mbr_28
            off "She’s really fucking my ass."
            scene ep4_sc15_mbr_27
            off "She moves it faster and harder."
            scene ep4_sc15_mbr_26
            off "It’s painful, but in the middle of it, I began to feel something else."
            scene ep4_sc15_mbr_27
            off "Is that pleasure?"
            scene ep4_sc15_mbr_28
            off "Am I gonna come from my ass?"
            scene ep4_sc15_mbr_27
            off "Holy shit, that’s not possible."
            scene ep4_sc15_mbr_28
            off "There’s no way!"
            scene ep4_sc15_mbr_27
            off "Why am I rock hard right now?"
            scene ep4_sc15_mbr_26
            off "What the fuck is going on?"
            scene ep4_sc15_mbr_27
            off "I’m about to come!"
            scene ep4_sc15_mbr_28
            off "This is so humiliating!"
            scene ep4_sc15_mbr_30
            $ UnlockThat("ep4/ep4_sc15_mbr_30")
            off "And she suddenly stops."
            off "I wonder what’s going on."
            off "I’m equally happy that she stopped fucking me and unsatisfied that she didn’t finish me."
            sf "So, darling... How do you feel?"
            sf "Was it enjoyable?"
            mc "I’m not..."
            sf "Don’t bother to lie."
            sf "Your dick is about to explode, you’re breathing like a horny beast."
            sf "A few more seconds and you would have unloaded a second time."
            sf "I almost made you come from your ass."
            sf "How do you feel about it?"
            sf "Be honest."
            mc "Conflicted."
            sf "As expected."
            sf "And how do you feel about the fact that I haven’t finished you?"
            mc "Frustrated."
            off "This is so humiliating."
            sf "Good."
            sf "Then, maybe next time you will put some more heart into licking my pussy."
            mc "I will my lady."
            sf "Good."
            scene ep4_sc15_mbr_31
            $ UnlockThat("ep4/ep4_sc15_mbr_31")
            off "She pulls the toy out of my ass and heads to the bathroom."
            sf "I hope you won’t be there when I return from the bathroom."
            sf "I need to sleep."
            off "She leaves the room abruptly."
            off "I get up from the bed and put my shorts back on."
            off "My butt hurts."
            scene ep4_sc15_c_02
            off "I don’t know what to think about all that."
            off "I’ve licked her pussy, she sucked my dick."
            off "I came."
            off "She fucked my ass and almost made me come but ultimately denied me too."
            off "The worse part about that is that I somehow felt good from being sodomized."
            off "This is so disturbing."

        "Fuck it. Perhaps I’ll enjoy it. [sfDomPath]" if sf_dominance > 14:
            $ ep4willingsodom = True
            $ ProcessStat(5, "sf_dominance")
            $ DumpNotStack()
            off "No one will know it anyway."
            off "Let’s do that."
            scene ep4_sc15_mbr_32
            $ UnlockThat("ep4/ep4_sc15_mbr_32")
            off "I raise and spread my legs to give her easy access to my anus."
            sf "[mc_name]. I’m very pleased with your reaction."
            sf "You will enjoy this."
            sf "I swear."
            off "She touches me very gently."
            off "It’s obvious that I have apprehensions about that and she knows it."
            scene ep4_sc15_mbr_33
            off "She caresses my butthole with the toy before spitting on it to lubricate it."
            sf "Try to relax."
            off "Easier said than done."
            off "I can feel the pressure she’s applying to my asshole."
            off "Lightly at first then more firmly."
            off "I do my best to keep calm and relax as she advised me too."
            off "Oh my God, I can feel it."
            off "It’s penetrating me."
            scene ep4_sc15_mbr_34
            $ UnlockThat("ep4/ep4_sc15_mbr_34")
            off "It’s inside."
            off "At least part of it."
            off "Holy shit, it’s huge!"
            off "It’s bigger than I thought."
            sf "You’re doing great, [mc_name]."
            sf "How do you like it so far?"
            sf "We’re almost halfway in."
            mc "It doesn’t feel so bad, but I won’t say I really enjoy it."
            off "She laughs lightly."
            sf "You will soon. Trust me."
            off "She pushes her toy further."
            scene ep4_sc15_mbr_35
            off "It’s filling me up."
            off "Holy fuck, I can barely stand it."
            off "The pain is almost unbearable."
            off "How can anyone take something bigger than that up his ass?"
            sf "Here we are."
            sf "You took it so easily."
            off "Fuck, that didn’t look so easy from my point of view."
            sf "The fun can now truly begin."
            scene ep4_sc15_mbr_34
            off "She starts moving the toy back and forth."
            scene ep4_sc15_mbr_33
            off "Slowly, gently."
            scene ep4_sc15_mbr_34
            off "Just a bit at first, then with full long strokes."
            scene ep4_sc15_mbr_35
            mc "Oh my god!"
            scene ep4_sc15_mbr_34
            off "The pain is mostly gone."
            scene ep4_sc15_mbr_33
            off "I actually feel pleasure."
            scene ep4_sc15_mbr_34
            off "Fuck."
            scene ep4_sc15_mbr_35
            off "Can I really enjoy being sodomized?"
            scene ep4_sc15_mbr_34
            off "I’m not sure I want to enjoy that."
            scene ep4_sc15_mbr_35
            off "My cock is rock hard."
            scene ep4_sc15_mbr_36
            $ UnlockThat("ep4/ep4_sc15_mbr_36")
            off "She grabs it and starts working it."
            scene ep4_sc15_mbr_37
            $ UnlockThat("ep4/ep4_sc15_mbr_37")
            off "She’s fucking my ass with one hand and gives me a handjob with the other, in perfect sync."
            scene ep4_sc15_mbr_36
            off "She moves progressively faster, harder."
            scene ep4_sc15_mbr_37
            off "I moan."
            scene ep4_sc15_mbr_38
            $ UnlockThat("ep4/ep4_sc15_mbr_38")
            off "My ejaculation is like an explosion."
            off "My cock twitches in her hand."
            off "She laughs again."
            sf "I told you you would like it."
            off "She continue fucking me and working my shaft slowly."
            sf "Tell me, darling. How does it feel?"
            sf "Obviously, you enjoyed it."
            off "There’s no point in denying it."
            mc "I’m surprised myself but... it was enjoyable."
            mc "However, the handjob probably played a big role."
            sf "We’ll have to investigate further to be sure about that."
            scene ep4_sc15_mbr_39
            $ UnlockThat("ep4/ep4_sc15_mbr_39")
            off "She slowly pulls the plug from my ass and stands up."
            sf "Look."
            sf "It’s not even half as big as your penis."
            mc "It sure felt bigger when it was inside me."
            sf "I told you we would go slow, but you took it so easily tonight that we may try the complete thing next time."
            mc "The complete thing? What do you mean?"
            sf "Well, I've told you."
            sf "Whatever you want to put inside me, I’ll put something as big inside you first."
            off "She wants to fuck my ass with something as big as my dick."
            off "Holy fucking shit."
            mc "I’m not sure I can take..."
            sf "Don’t worry, Darling."
            sf "There is no shame in failing if you give it your best."
            sf "We’ll try."
            sf "If you can’t, we’ll just go back to a more manageable size."
            sf "But you know, the sooner you take it...."
            mc "O..ok..."
            scene ep4_sc15_mbr_31
            $ UnlockThat("ep4/ep4_sc15_mbr_31")
            off "She heads to the bathroom."
            sf "I have things to do on my own now."
            sf "I hope you won’t be there when I return from the bathroom."
            sf "Goodnight darling."
            off "She leaves the room abruptly."
            off "I get up from the bed and put my shorts back on."
            off "My butt hurts."
            scene ep4_sc15_c_02
            off "I don’t know what to think about all that."
            off "I’ve licked her pussy, she sucked my dick."
            off "I came."
            off "She fucked my ass and masturbated me at the same time."
            off "I came again."
            off "Holy shit."
            off "I enjoyed being sodomized."
            off "I liked it."
            off "This is so disturbing."
    $ renpy.end_replay()
    return


label ep4sc15:
    scene black with dissolve
    with Pause(2)
    show text "Later that night."
    with Pause(2)
    scene ep4_sc13_mcr_01 with fade
    off "I wait for [sf_name] to start snoring, just to be sure she’s asleep."
    off "Or at least I should."
    off "It’s already been an hour and she still doesn’t make a noise."
    off "Maybe she doesn’t snore every night."
    off "I should take the risk."
    off "I’m sure it’s safe."
    scene ep4_sc15_mcr_00
    off "Yeah, but what if it isn’t?"
    off "Will I risk [sis_name] and I getting caught?"
    off "I should wait some more."
    off "Come on, she won’t snore."
    off "She’s already asleep."
    off "How long am I going to wait for something that will not come?"
    off "Let’s go, [mc_name]."
    scene ep4_sc16_c_00
    off "The house is completely silent."
    off "I waited too long."
    off "[sis_name] is probably sleeping."
    off "Maybe I should let her rest?"
    scene ep4_sc16_c_01
    off "I softly knock on the door."
    sis "Yes?"
    off "The voice is muffled but the reply is instantaneous."
    off "She was waiting."
    mc "It’s me."
    sis "Come in."
    off "I immediately comply."

    scene ep4_sc16_sr_00
    $ UnlockThat("ep4/ep4_sc16_sr_00")

    if sf_love_path == True:
        off "She lays on her bed."
        off "Her back turned to me."
        off "I suddenly feel uncomfortable."
        off "The silence is long and awkward."
        sis "Did you fuck her?"
        off "Her words are brutal and cold."
        off "It’s not anger, but she’s clearly not happy."
        mc "No. I didn’t. I told you I wouldn’t."
        sf "But she wanted to."
        scene ep4_sc16_sr_01
        mc "No. I mean, yes, but she changed her mind."

        if ep4sflovetalked == True:
            scene ep4_sc16_sr_02
            mc "We just talked."
            sis "You just talked?"
            mc "Yes."
            sis "And I’m supposed to believe you?"
            mc "Come on [sis_name]."
            mc "Listen, we didn’t do anything."
            mc "When I came in, she was terrified to have sex with me."
            mc "I told her it wasn’t important, that I was more than happy to just share a moment with her, talking and knowing each other better."
            mc "We sat on the bed kissed and cuddled while chatting."
            off "She sighs."
            $ ProcessStat(5, "sis_affection")
            $ DumpNotStack()
            sis "Dumbass. It may be even worse."
            mc "What? Why? What are you talking about?"
            sis "You really know nothing about girls."
            mc "Hey, if you want me to understand anything, you’ll have to stop talking in riddles."
            sis "If you don’t want someone to love you, stop being lovable."
            mc "You would have preferred me to be a dork or something like that?"
            sis "Things would have been easier."
            off "She sounds sad."
            sis "Are you going to join me or will you stand there all night long?"
            scene ep4_sc16_sr_05
            $ UnlockThat("ep4/ep4_sc16_sr_05")
            off "I slowly get on the bed and throw an arm around her."
            mc "Hey. It’s ok. Everything will be ok."
            sis "No, it won’t."
            sis "And you know it."
            sis "I shouldn’t have done that."
            sis "Whatever I do, I’ll lose something, if not everything."
            sis "I’ll lose you, or I’ll lose her, maybe both. Maybe worse."
            sis "I’ve spent my time trying to decide which will be right, or the least painful."
            sis "And it’s obvious."
            mc "I’m sure there’s a way."
            sis "I’ve found one."
            scene ep4_sc16_sr_06
            $ UnlockThat("ep4/ep4_sc16_sr_06")
            off "The kiss is gentle but sorrowful."
            off "Something is happening."
            off "We keep on kissing for a long time before she gets on top of me."
            scene ep4_sc16_sr_07
            $ UnlockThat("ep4/ep4_sc16_sr_07")
            off "The mood is very strange."
            sis "Starting tomorrow morning, we'll go on as if nothing happened."
            mc "What are you talking about?"
            off "I know exactly what she’s talking about."
            off "I ask anyway."
            off "My heart is tightening."
            off "She hasn't yet uttered the words that the pain is already there."
            sis "We shouldn’t have done that in the first place."
            sis "I shouldn’t have done that."
            sis "It’s my fault."
            sis "You’ll be happy with her."
            off "I don’t want to hear that."
            mc "Don’t say that, please."
            scene ep4_sc16_sr_08
            sis "Come on [mc_name]."
            sis "It’s the only way."
            sis "You know it."
            mc "No! It’s not!"
            mc "There’s plenty of possibilities."
            sis "Possibilities that will hurt her."
            sis "That, I can’t stand."
            mc "So what?"
            mc "You think I can just go back to her and pretend nothing happened?"
            mc "You want me to act as if I love her?"
            mc "You think it won’t hurt her?"
            mc "You think it won’t hurt me?"
            scene ep4_sc16_sr_09
            $ UnlockThat("ep4/ep4_sc16_sr_09")
            sis "You won’t have to act, [mc_name]."
            sis "You know it."
            sis "I saw you."
            sis "You will be happy."
            sis "You already love her."
            mc "No, I don’t!"
            sis "You do."
            sis "And it’s ok."
            sis "I don’t blame you for that."
            sis "I know what she can do."
            sis "She did it to me too I guess."
            off "I want to scream, but I can’t."
            mc "What are you even talking about?"
            mc "I don’t understand!"
            scene ep4_sc16_sr_10
            $ UnlockThat("ep4/ep4_sc16_sr_10")
            off "She takes her top off."
            off "That surprises me."
            off "I wonder what kind of joke is this."
            off "I was about to cry and I’m now drowning into confusion."
            mc "What are you doing?"
            sis "This is our last night. We can do it."
            off "She cannot be serious."
            mc "Do what?"
            scene ep4_sc16_sr_11
            $ UnlockThat("ep4/ep4_sc16_sr_11")
            sis "Have sex."
            off "This is ridiculous."
            mc "Are you serious right now?"
            sis "You don’t want to?"
            sis "I thought this could be our goodbye."
            off "I don’t know if I’m about to burst in anger or let go in the sadness of the moment."
            off "Anger finally sounds like a good answer to the situation."
            mc "What kind of asshole do you think I am?"
            off "She seems surprised."
            scene ep4_sc16_sr_12
            $ UnlockThat("ep4/ep4_sc16_sr_12")
            off "She looks away and covers herself in shame."
            mc "I want you, I want all of you."
            mc "Of course, I want to have sex with you."
            mc "But as a goodbye?"
            mc "No thank you."
            mc "There’s no point if there’s no tomorrow for us."
            mc "It’s not how it works."
            mc "Look at you."
            mc "You don’t even want this."
            mc "Why are you doing it?"
            sis "I’m sorry, I thought... You may want it."
            mc "I want it, but not like that."
            scene ep4_sc16_sr_13
            $ UnlockThat("ep4/ep4_sc16_sr_13")
            off "She crashes on my chest crying."
            sis "I’m so sorry."
            mc "It’s okay."
            scene ep4_sc16_sr_14
            $ UnlockThat("ep4/ep4_sc16_sr_14")
            off "I wrap my arms around her and hold her tight, as to hold her back from something that would tear her away from me."
            off "We stay like that for a while."
            off "I search for something to say, something that would change her mind but I can’t think of anything."
            off "Sadness is exhausting."
            off "I can feel its weight upon us."
            off "It is said that some can let themselves die from sorrow."
            off "Right now, I have no doubt about it."
            off "[sis_name] took her decision alone."
            off "The idea of [sf_name] suffering from her actions was too much for her to take."
            off "Did she even think about my own pain?"
            off "Did she weight it up?"
            off "Does that mean she loves [sf_name] more than she loves me?"
            off "Or does she really think that both [sf_name] and I can be happy with this solution?"
            off "She’s right about something, however."
            off "Someone has to suffer."
            off "Obviously, she thinks it’s her burden."

            menu:
                "If you hadn't come to me last night...":
                    $ ProcessStat(1, "sis_affection")
                    $ DumpNotStack()
                    mc "... I would have come to you myself. It’s not your fault."
                    sis "I’m the one who made the move."
                "I don’t accept it. [blue]\[Harem Path?\]":

                    $ ProcessStat(1, "sis_affection")
                    $ DumpNotStack()
                    $ ep4nightchoosenone = True
                    sis "It’s not like you have a choice."
                    mc "I have. I’ll be with you, or I’ll be with no one."
                    sis "That would be silly."
                    mc "Everyone would be equally hurt."
                    mc "It sounds pretty right to me."
                    sis "Your argument is stupid."

            mc "You don’t have to be the one to suffer."
            mc "Do you know that?"
            sis "Of course I am."
            sis "I’m stealing my best friend’s boyfriend."
            sis "I deserve it."
            sis "But it’s irrelevant."
            sis "I didn’t take this decision because I wanted to atone for some sins."
            sis "I took it because I don’t want her to suffer."
            sis "You can understand that."
            mc "I can yes."
            mc "That doesn’t make it easier to accept."
            mc "And just to be clear, I don’t think it’ll work."
            mc "Even if we do our best to pretend, a lie is still a lie."
            mc "One day or another, she will find out."
            sis "Maybe. We’ll see."
            sis "You’ll spend tomorrow night with her and you won’t even think about me after that."
            sis "I promise."

            mc "I don’t want to let you go."
            sis "I don't want it either."
            sis "I have to do it anyway."

            off "The night goes on and we simply stay like that."
            off "Sometimes she cries, sometimes I do."
            off "Often both."
            off "I can feel her tears dripping on my chest while I try to shed mine in silence."
            off "For a few seconds, I can’t help but think that all of this is so ridiculous it can’t be true."
            off "It sounds like one of those desperate romance stories from a girl's novel."
            off "It’s so painful."
            off "I should have listened to Steve."
            off "Less feelings, less thinking, more YOLO."
            off "Things would be so much easier without love and other complications."

            return
        else:

            if ep4sfpussylicked == True:
                scene ep4_sc16_sr_03
                mc "I... gave her cunnilingus."
                sis "You licked her pussy?"
                mc "That’s what giving cunnilingus means..."
                sis "And you think that it doesn’t qualify as having sex?"
                mc "Hey, you think I had a choice?"
                mc "I had to do something."
                mc "I couldn’t just leave while she was expecting something to happen."
                mc "God, I don’t even understand how we came to that."
                mc "She stripped, I stripped, she lied on the bed..."
                mc "I had to do something."
                sis "Yeah, I’m sure it was a torture for you."
                mc "Come on, [sis_name]."
                mc "You have to trust me or we’ll go nowhere like this."
                off "She stays silent for a few seconds."
                sis "I’m jealous, ok?"
                mc "That I can understand."
                mc "I’m sorry."

            if ep4sfbuttholelicked == True:
                scene ep4_sc16_sr_04
                $ UnlockThat("ep4/ep4_sc16_sr_04")
                mc "I ... licked her... Butt hole."
                sis "You licked what?"
                sis "Who the hell does that?"
                mc "I don’t know, it seemed like a good idea at the moment..."
                sis "Are you some kind of anal pervert or something?"
                mc "No! I’m not!"
                mc "I don’t know why I did that, I just did."
                mc "I didn’t particularly like it."
                sis "... And.. What about her?"
                sis "Did she like it?"
                mc "I’m not sure..."
                mc "I mean, she enjoyed it a bit but..."
                mc "Well, I had a finger in her pussy too..."
                mc "So I’m not sure it really was the butthole licking that made her feel good."
                sis "Oh... You also inserted a finger in her vagina."
                sis "That’s great."
                sis "Anything else?"
                sis "Like your dick?"
                mc "[sis_name]. I didn’t fuck her."
                mc "Neither of us wanted to have sex."
                mc "I swear."
                sis "... I believe you... Your butt licking kink is so lame that it’s probably true."
                mc "I don’t have any butt licking kink."
                sis "Does that mean you wouldn’t lick mine?"
                mc "Not without kissing you first."
                sis "Oh, no, you won’t."
                sis "Not with that butt licking mouth of yours."
                sis "You go wash it first."
                mc "What? Are you serious?"
                sis "I’m not going to kiss a mouth that sucked on an asshole."
                off "Ok, [mc_name]. Let’s be a bit understanding, go wash that mouth."
                off "Five minutes of mouth washing in the bathroom later, I’m waiting beside her bed, again."
    else:
        label galleryScene9:
        mc "Hey."
        sis "What took you so long?"
        if ep4mcassfucked == True:
            off "I’ve spent some time being sodomized by your best friend, Princess."
            off "But I can’t tell you that."
        mc "I waited for [sf_name] to start snoring... but..."
        sis "She doesn’t snore every night, dumbass."
        sis "You could have waited all night long."
        sis "I was almost asleep."
        mc "Next time I’ll come right away."
        sis "We’ve already lost half the night."
        mc "I hope there’s still time for a kiss at least."


    off "She slowly raises and sits on the edge of her bed."
    sis "Turn on the lights, please."
    off "I comply."
    scene ep4_sc16_sr_15
    $ UnlockThat("ep4/ep4_sc16_sr_15")
    off "Her voice carries a very strange tone."
    sis "Can you do something for me?"
    mc "Sure. Name it."
    scene ep4_sc16_sr_16
    off "She looks away from me."
    sis "I would like to... see your thing..."
    off "My thing?"
    off "She looks so embarrassed."
    off "She’s definitely talking about my penis."
    scene ep4_sc16_sr_17
    mc "You want to see my thing?"
    sis "If you don’t mind..."
    off "She’s so cute when she’s embarrassed like that."
    mc "Ok, but... what thing are we talking about?"
    sis "You know... your thing..."
    mc "You’ll have to be more specific, I have a lot of things..."
    sis "Come on, you know what I mean."
    mc "I have sincerely no idea..."
    scene ep4_sc16_sr_18
    $ UnlockThat("ep4/ep4_sc16_sr_18")
    sis "Your dick, ok?"
    sis "I want to see your dick."
    sis "Are you trying to embarrass me on purpose?"
    mc "You’re too cute."
    mc "I can’t refuse you anything."
    scene ep4_sc16_sr_19
    $ UnlockThat("ep4/ep4_sc16_sr_19")
    off "I get rid of my shorts and stand right in front of her."
    off "I would have thought that this situation would have been more embarrassing but I strangely feel very comfortable."
    off "My cock is feeling great too and slowly going from soft to medium-hard on its own."
    off "The attention [sis_name] is giving it is very motivating."
    off "Maybe I’m a bit of an exhibitionist."
    scene ep4_sc16_sr_20
    sis "It’s... And... It can grow bigger."
    mc "With a bit of help, yes."
    sis "Can you..."

    if sf_dom_path == True:
        off "This situation feels a bit like deja vu."

    off "I take a step closer to her."
    mc "You can touch it if you want."
    mc "It’s yours."
    off "She looks at me with apprehension before going back to my dick."
    scene ep4_sc16_sr_21
    $ UnlockThat("ep4/ep4_sc16_sr_21")
    off "She starts caressing it with one finger, then her whole hand."
    off "She finally grabs it and clumsily gives it a couple strokes."
    off "I’m now fully hard."
    off "Her breathing is getting faster, just like mine."
    off "She’s aroused but there’s also something else."
    off "She seems worried, maybe even afraid."
    mc "Is everything ok?"
    sis "What? Yeah, sorry."
    sis "Everything’s fine... It’s just..."
    scene ep4_sc16_sr_22
    $ UnlockThat("ep4/ep4_sc16_sr_22")
    off "She lets go of my dick and looks away from it."
    sis "Listen. I... We... You know... I mean... "
    mc "Hey, Princess, calm down."
    mc "There’s nothing embarrassing, nothing to be ashamed of."
    mc "You can speak without fear of being judged. Ok?"
    scene ep4_sc16_sr_23
    sis "Ok... Then... If we are a couple... at some point you may want to have sex, I mean, we may want to have sex..."
    off "Oh yes, Princess, I may want to have sex."
    sis "And... Believe me, I thought about it a lot... I want it to happen..."
    off "Good to know!"
    sis "But now that I see it..."
    sis "I’m sorry [mc_name]..."
    sis "This... There’s no way I'll let this enter my pussy."
    mc "What?"
    sis "I’m sorry."
    sis "It would destroy me."
    sis "It’s too big!"
    off "She freaks out."
    scene ep4_sc16_sr_24
    $ UnlockThat("ep4/ep4_sc16_sr_24")
    mc "Ok. Calm down."
    sis "I’m sorry, I can’t!"
    sis "I’m very tight, this would hurt so much!"
    mc "Princess, please, It’s ok, calm down."
    mc "Everything will be ok."
    mc "Listen to me."
    mc "We will have sex. One day or another."
    mc "When we’re will be both ready for it."
    mc "And it will be great."
    scene ep4_sc16_sr_25
    mc "I won’t destroy you, my penis won’t be too big for your vagina and everything will be perfect."
    mc "I know it for sure because, first of all, I’m not a horny jerk who will just jump on you and fuck you like a beast. Ok?"
    mc "We will do it nicely, gently, slowly."
    mc "You’ll get used to it."
    mc "Secondly, the human body is amazing."
    mc "You will stretch. Trust me."
    scene ep4_sc16_sr_26
    sis "What? You want to stretch me?"
    off "Ok, maybe that wasn’t the most perfect phrasing I could have come up with."
    mc "No, Princess. I don’t want to stretch you."
    mc "The tighter the better."
    mc "But the vagina is .. elastic, the human body is made like that."
    mc "Look at my dick again. Look at it."
    mc "You’re freaking out for nothing."
    mc "It’s not even that big."
    scene ep4_sc16_sr_24
    sis "Are you kidding me?"
    sis "It’s as big as my forearm!"
    mc "No, it’s not."
    mc "I’m probably average."
    mc "Maybe a bit above if I want to flatter myself, but I can promise you it’s nothing you can’t handle."
    mc "You’re supposed to give birth with this vagina."
    mc "If a whole baby can pass through it, my dick can surely visit it as well without destroying you."
    off "The baby argument seems to work."
    scene ep4_sc16_sr_25
    sis "That’s... not wrong..."
    mc "How tight are you?"
    sis "What?"
    mc "You said you were very tight. How tight?"
    sis "Tight enough..."
    mc "Can I see?"
    scene ep4_sc16_sr_26
    off "She looks at me with suspicion then seems to remember that we’re actually a couple, even if a deviant one."
    sis "I guess it’s ok."
    scene ep4_sc16_sr_27
    $ UnlockThat("ep4/ep4_sc16_sr_27")
    off "She removes her panties and lays down on the bed."

    off "Holy shit, that pussy looks perfect."

    if sf_dom_path == True or ep4sflovelicked == True:
        off "The situation is completely fucked up but I got to see two pussy tonight."
        off "How many guys are that lucky?"


    off "This is [sis_name]’s pussy."

    off "I feel very strange about it."
    off "I shouldn’t be looking at it like that, and yet I feel attracted to it."
    off "That sensation is so strong that I’m almost shaking."

    if sf_dom_path == True or ep4sflovelicked == True:
        off "[sf_name]’s body is great, maybe even greater than [sis_name]’s but she didn’t have that effect on me."
        off "It was .. Different."

    scene ep4_sc16_sr_28
    $ UnlockThat("ep4/ep4_sc16_sr_28")
    off "I get on my knees and take a closer look at it."
    menu:
        "Princess... [sisLovePath]":
            mc "You are absolutely perfect."
            sis "What are you talking about?"
            mc "Your pussy is beautiful."
            sis "That kind of compliment sounds so weird... maybe you should keep those for yourself."
            $ ProcessStat(2, "sis_affection")
            $ DumpNotStack()
        "Holy mother of god. [sisSubPath]":

            mc "This is some prime pussy."
            sis "Prime pussy?"
            sis "What the hell are you talking about?"
            sis "Are you an expert?"
            mc "As far as an 18 old guy with an Internet connection can be, yes."
            sis "Oh, God, I don’t want any more details about your porn addiction."
            $ ProcessStat(1, "sis_affection")
            $ ProcessStat(1, "sis_submission")
            $ DumpNotStack()

    off "I gently caress her thighs while looking at her."
    scene ep4_sc16_sr_29
    $ UnlockThat("ep4/ep4_sc16_sr_29")
    sis "Ok, Are you done with it? This is so weird..."
    mc "Not quite."
    mc "I can’t see how tight you are like that."
    mc "I’ll have to at least to open it."
    mc "Maybe even slide a finger in it."
    sis "What? Are you serious?"
    mc "Do you see any other way?"
    off "She sighs vigorously."
    sis "This is so humiliating."
    mc "Why? As I said there is nothing to be ashamed of."
    sis "You will pay for this."
    mc "Of course I will."
    scene ep4_sc16_sr_30
    $ UnlockThat("ep4/ep4_sc16_sr_30")
    off "Slowly, I slide a finger inside her."
    off "She gasps."
    mc "Princess, you are indeed very, very tight."
    mc "You should relax and try to enjoy this."
    mc "You know I don’t want to force anything on you, don't you?"
    mc "If you want me to stop..."
    off "Another sigh."
    sis "It’s ok. You can... go on..."
    off "My finger slides a bit further."
    off "She’s ridiculously tight."
    off "It’s probably the stress of the situation."
    off "I should help her a bit."
    scene ep4_sc16_sr_31
    $ UnlockThat("ep4/ep4_sc16_sr_31")
    off "She doesn’t say a word but immediately grabs my hair when my tongue find her clitoris."
    off "It’s pretty clear for both of us that this isn’t an examination anymore."
    off "I slowly explore her with my index for a few seconds."
    off "She manages to relax a bit but she was clearly not joking saying she was very tight."
    off "She moans. "
    off "My middle finger joins the first one."
    off "I lick her more vigorously."
    off "I’m basically sucking her clitoris like my life depends on it."
    off "She’s wet enough so my fingers can go in and out of her with ease."
    off "God, she’s so tight."
    off "I can’t help but imagine my dick inside her."
    off "She groans continuously."
    scene ep4_sc16_sr_32
    $ UnlockThat("ep4/ep4_sc16_sr_32")
    off "She arches and lets go of my head to silence herself."
    off "I interpret it as a good sign."
    off "I have no idea what I’m doing but it seems to work nicely on her."
    off "She tastes so good, it’s incredible."
    off "It’s salty but sweet at the same time."
    off "Her legs suddenly start shaking while she lets out a long muffled scream."
    off "Did I manage to make her come?"
    off "I keep playing with her pussy until she stops trembling."
    scene ep4_sc16_sr_33
    $ UnlockThat("ep4/ep4_sc16_sr_33")
    off "She seems completely exhausted when I join her on the bed."
    off "We slowly move to a more comfortable position."

    menu:
        "Princess, your pussy is my new favorite meal. [sisLovePath]":
            $ ProcessStat(2, "sis_affection")
            $ DumpNotStack()
            off "She lets out an exhausted laugh."
            sis "You’re so bad at complimenting."
        "Did I make you come, Princess? [sisSubPath]":

            $ ProcessStat(1, "sis_affection")
            $ ProcessStat(1, "sis_submission")
            $ DumpNotStack()
            sis "You really are a moron."
            sis "I never asked for that in the first place!"
            mc "But you enjoyed it nonetheless."

    sis "I can’t believe you made me come so easily."
    sis "That’s so humiliating."
    mc "Humiliating?"
    mc "What’s your deal with shame and such?"
    mc "You’re perfect, you have nothing to be ashamed of, and just now, there was nothing humiliating, I just tried to make you feel good."
    mc "I don’t think there’s anything wrong in that."

    sis "Except for the fact that you're like a brother to me."

    mc "Well apart from that."
    mc "Maybe... I’m not even sure about that."
    mc "And you're right. You’re very, very tight."
    mc "But it’ll be ok. You don’t have to worry."
    sis "Easy for you to say, you’re not the one who’ll have to take it in."
    if ep4mcassfucked == True:
        off "Actually.. I may have to take it as well..."
    scene ep4_sc16_sr_33_plus
    $ UnlockThat("ep4/ep4_sc16_sr_33_plus")
    off "I slowly caress her belly and let my hand gently crawl to her pussy again."
    sis "Aren’t you done playing with it?"
    mc "Do you want me to stop?"
    sis "Well... It’s not... unpleasant... But in the meantime, it feels very weird..."
    mc "I know."
    mc "Very, very weird, like..."
    mc "You feel a bit nauseous, but there’s this thrill that continuously sends shivers down your spine, and those shivers come with some kind of pleasure that pushes you further."
    sis "That’s... exactly that."
    mc "I chose to ignore the nausea and follow the shivers."
    sis "You wouldn’t be here if I wasn’t following the shivers too."
    mc "I know."
    off "We stay silent for a few seconds, my fingers still playing with her."
    scene ep4_sc16_sr_34
    sis "I've never sucked a cock."
    off "She sounds very serious."

    menu:
        "I know. [sisLovePath]":
            sis "All these guys kept coming up to me, asking for it like it was nothing."
            sis "I refused every time."
            sis "Why didn’t they stop harassing me with that?"
            mc "I can only imagine what happened."
            mc "Every one of these morons came back to his friends after asking you."
            mc "And... Well, getting rejected by the girl who sucks everyone's dick could have been seen as a humiliation so..."
            mc "They probably started claiming that you gave them what they asked for."
            mc "I’ve met a couple of these guys."
            mc "I feel bad I didn’t punch their face."
            $ ProcessStat(2, "sis_affection")
            $ DumpNotStack()
        "There’s nothing wrong with sucking dicks.":


            $ ep4dickjoke = True
            mc "I mean, a reasonable number of dicks. Like, one."
            sis "Did you really just make this joke right now?"
            mc "What’s wrong with my joke?"
            sis "The timing. The mood. The moment."
            sis "Everything is wrong with your joke."
            mc "Ok... I’m sorry, I was just trying to lighten the mood."
            sis "You ruined the mood."
            off "Ok, maybe I could have chosen my words better..."



    scene ep4_sc16_sr_35
    $ UnlockThat("ep4/ep4_sc16_sr_35")
    sis "Do you expect me to suck on yours?"

    menu:
        "I sure hope so, but..." if ep4dickjoke == True:
            $ ProcessStat(3, "sis_affection")
            $ DumpNotStack()
            mc "You’ll only do what you want to do and it’ll be perfect that way."
            mc "There’s plenty of things we can do aside from that..."
        "I don’t expect anything. [sisLovePath]":

            $ ProcessStat(2, "sis_affection")
            $ DumpNotStack()
            mc "I hope you don’t think I just serviced you in hope you will return the favor."
            mc "I did it because I wanted to please you."
            mc "I didn’t expect anything in return."

    sis "I’m not a slut."
    mc "I know."
    sis "You’re the first guy I kissed."
    mc "I know."
    scene ep4_sc16_sr_36
    $ UnlockThat("ep4/ep4_sc16_sr_36")
    off "She slowly extends her arms towards my cock and caress it gently."

    mc "You don’t have to do that if you don’t want to."
    sis "I know."
    off "I’m back to rock hard in no time."
    off "She kneels beside me."
    sis "I never did that before."
    sis "Tell me if I... Hurt you."
    mc "Sure."
    scene ep4_sc16_sr_37
    $ UnlockThat("ep4/ep4_sc16_sr_37")
    off "She strokes my shaft and plays with my balls for some time."
    off "Her gaze going from my tool to my eyes."
    off "I can see she’s as eager to please me than I am to please her."
    scene ep4_sc16_sr_38
    $ UnlockThat("ep4/ep4_sc16_sr_38")
    off "She shyly licks my glans."
    off "I stacked up so much anticipation about this that the shivers it gives me are almost enough to make me come."
    off "I manage to contain myself but can’t help but vocalize it."
    mc "Holy shit, Princess."
    off "She alternates licking and stroking for a bit."
    off "My breathing gets loud and heavy."
    scene ep4_sc16_sr_39
    $ UnlockThat("ep4/ep4_sc16_sr_39")
    off "I’m already on the verge of coming when she finally takes it in her mouth."
    off "She doesn’t take more than a few centimeters."
    off "It’s warm and moist."
    off "She sucks on my glans while stroking the base of my cock."
    off "I can feel her tongue swirling around my penis."
    mc "Holy fuck!"
    off "I can’t resist any longer."
    mc "I’m going to come, Princess!"
    scene ep4_sc16_sr_40
    $ UnlockThat("ep4/ep4_sc16_sr_40")
    off "I barely finish my sentence that I unload everything I have."
    scene ep4_sc16_sr_41
    $ UnlockThat("ep4/ep4_sc16_sr_41")
    off "She seems surprised as she raises and rushes through the door."
    off "She covers her mouth with her hand, as if she was about to puke."
    off "I can hear her going to the bathroom."
    off "A faucet opens."
    off "Water flows through the pipes."
    scene ep4_sc16_sr_42
    off "I think about joining her when she comes back."
    off "She doesn’t seem upset."
    mc "Hey... Are you alright? I’m sorry, I..."
    sis "I couldn’t swallow it."
    sis "I thought I could take it but at the last minute, I just couldn’t swallow."
    off "Dear God."
    mc "You didn’t have to swallow it..."
    sis "I was just afraid to stain the sheets."
    mc "Seriously?"
    scene ep4_sc16_sr_43
    $ UnlockThat("ep4/ep4_sc16_sr_43")
    off "She pushes me on the bed."
    sis "I like these sheets, ok?"
    scene ep4_sc16_sr_44
    $ UnlockThat("ep4/ep4_sc16_sr_44")
    off "She switches the light off and joins me."
    sis "How was it?"
    mc "You want a performance report or something?"
    sis "I just want to know if it was nice, dumbass."
    mc "I’m sure you noticed that you made me come."
    mc "It was nice."
    mc "It was actually very nice."
    mc "And also kind of humiliating."
    mc "I usually last a lot longer..."
    sis "Usually? How many blowjobs did you have until now?"

    if ep4mcassfucked == True:
        off "Ok, maybe I shouldn’t talk about my sixty-nine experience with Crazy [sf_name]."

    mc "That was... my first time."
    mc "But you know... When I’m jerking off... I usually last longer."
    sis "I usually last longer too."
    mc "Maybe we’re... very compatible or something like that."
    sis "Maybe."
    mc "We’ll have to investigate that."
    off "She laughs."
    off "We spend some time softly talking about stupid things, kissing and cuddling into sleep."
    off "She sounds happy."
    off "At this moment I feel like we’re just a normal couple who just had a great time."
    off "Life isn’t so bad..."
    off "When you forget about the difficulties."
    $ renpy.end_replay()
    return


label ep4sc16:
    scene black with fade
    with Pause(2)
    show text "Later."
    with Pause(2)
    off "The house has been completely silent for some time now."
    off "[sf_name] doesn’t snore tonight, but I don’t care."
    off "I can’t wait anymore."
    scene ep4_sc17_lr_00 with fade
    $ UnlockThat("ep4/ep4_sc17_lr_00")
    off "I send [sis_name] a message as I walk into the living room."
    mc "I’m waiting for you in the living room."
    scene ep4_sc17_lr_01
    off "I wait for her five long minutes."
    off "Maybe she didn’t get the message."
    off "Maybe she’s asleep."
    off "Maybe she doesn’t want to come."
    off "Maybe I went too far today."
    off "I was convinced she wanted to play some more."
    off "Was I wrong?"

    if ep4subbadfail == True:
        scene black with dissolve
        with Pause(2)
        show text "Half an hour later."
        with Pause(2)
        scene ep4_sc17_lr_51
        $ UnlockThat("ep4/ep4_sc17_lr_51")
        off "She won’t come."
        off "Of course, she won’t come."
        off "I’ve been an ass."
        off "I had all the cards in my hand and I fucked it up."
        off "Shit."
        off "I’ve probably gone too far, or too fast."
        off "Or both."
        off "I could have pumped that pussy if I had been a little more patient."
        off "What a moron…"
        $ renpy.end_replay()
        return



    off "I’m about to send her another message when I hear a very faint noise coming from the hallway."
    off "My heartbeat intensifies."
    off "She’s here."
    off "Ok, [mc_name], remember. You’re the one in charge but don’t be an asshole."
    off "She wants to submit, that doesn’t mean you can do or say whatever you want.. Yet."
    off "Keep cool."
    off "I’m sure she hides behind the wall."
    off "She hesitates."
    off "Say something or she’ll go back to her room."

    menu:
        "You should come in. [sisSubPath]":
            $ ProcessStat(2, "sis_submission")
            $ DumpNotStack()
            mc "I can lick your pussy in the hallway but the sofa will be far more comfortable."
            mc "I’m not going to rape you, Princess."
            mc "You can rest easy."

        "I’m waiting for you, Princess. [sisLoveSubPath]" if sis_sub_love_path == True:
            $ ProcessStat(2, "sis_submission")
            $ ProcessStat(2, "sis_affection")
            $ DumpNotStack()
            mc "Take the time you need."
            mc "I understand your hesitations."
            mc "This is important."
            mc "This is the last time I’ll give you that choice."
            mc "Come in because you want it."
            mc "Come in because you want to belong to me."
            mc "Because you want to be mine."
            mc "I’ll be gentle."
            mc "I will protect you, with all I have."
            mc "You can trust me."

    scene ep4_sc17_lr_02
    $ UnlockThat("ep4/ep4_sc17_lr_02")
    off "She slowly emerges from the hallway."
    off "It's still fragile, but she still took a decision."
    off "She wants it."
    off "Maybe even more than I do myself."
    sis "Hey."
    mc "Hey, Princess."
    mc "Did I wake you up?"
    mc "I assumed that you would wait for my call, but perhaps were you sleeping?"
    sis "I… wasn’t sleeping but I wasn’t waiting for anything either…."
    off "I stand up and walk to her."
    scene ep4_sc17_lr_03
    mc "You’re here nonetheless."
    sis "I thought you may have something important to tell me…"
    mc "I want to lick your pussy."
    mc "Isn’t that important enough?"
    scene ep4_sc17_lr_04
    $ UnlockThat("ep4/ep4_sc17_lr_04")
    sis "Can’t you stop talking about that so casually?"
    mc "Does that bother you?"
    sis "You mention it just to embarrass me."
    mc "I licked your pussy."
    if ep3sisdoubleorgasm == True:
        mc "You sucked my dick."
    mc "We both enjoyed it."
    mc "I’m not embarrassed about it, why are you?"
    scene ep4_sc17_lr_05
    $ UnlockThat("ep4/ep4_sc17_lr_05")

    sis "Because you're like a brother to me!"

    sis "We shouldn’t do that."
    sis "Doesn't that bother you?"
    sis "This is so weird."
    mc "Actually, I think it’s even more exciting because we’re siblings."
    mc "And besides, this is the 21st century."
    mc "Everyone does that."
    mc "It’s trending."
    scene ep4_sc17_lr_04
    sis "No, it’s not."
    sis "I don’t know where you’ve found this kind of information but no one is doing this."
    sis "This is still taboo."
    mc "The taboo makes it more interesting."
    mc "Don’t you feel it? You want it."
    mc "Why? Because it felt good? Because you did it with me? Because it’s forbidden?"
    mc "It’s all of that."
    mc "You know it."
    mc "We won’t be able to feel something as intense with someone else."
    scene ep4_sc17_lr_05
    off "She stays silent for a few seconds before talking with a frail and sad voice."
    sis "You just want to fuck me, don’t you?"

    menu:
        "I want to fuck you. [sisSubPath]":
            $ ProcessStat(3, "sis_submission")
            $ DumpNotStack()
            mc "And again. And again. And again. And again."
            mc "You should have sensed it already."
            mc "That thing we have…"
            mc "It’s like a drug."
            mc "We’re hooked."
            mc "We’ll keep coming back to it until the day we’ll die."
            mc "Even if it’s purely sexual."
            mc "We’re in it for life."
            mc "If you thought I would let you go away after a fling, I’m sorry to disappoint you."
            scene ep4_sc17_lr_04
            sis "Is that supposed to seduce me?"
            sis "Do you think I only live for your cock or something?"
            mc "I’m just being honest, Princess."

            if sf_love_path == True:
                sis "What about [sf_name]?"
                mc "I’m not sure myself."
                mc "It’s very strange."
                mc "I like her a lot."
                mc "I might even say that I’m falling for her."
                mc "However I don’t feel like what I just told you is false, or wrong."
                mc "I have something for both of you."
                mc "Something different. But something real."
                sis "You’ll have sex with her too. Why would you want me…"
                mc "Because you are different."
                mc "You feel different."
                mc "There’s a thrill between you and me that we won’t find with anyone else."
                mc "And I feel like I’m inexorably drawn to you."
                mc "Like I don’t have a choice."
                mc "That’s the effect you have on me, Princess."

        "You can’t be more wrong. [sisLoveSubPath]" if sis_sub_love_path == True:
            $ ProcessStat(3, "sis_submission")
            $ ProcessStat(3, "sis_affection")
            $ DumpNotStack()
            mc "I will fuck you, but I won’t stop there."
            scene ep4_sc17_lr_04
            mc "I’ll take you whole."
            mc "I’ll take everything you have and give you everything I have in return."
            mc "You will be mine. I will be yours."
            mc "I will be there for you."
            mc "I will keep you safe."
            mc "I’ll die for you."
            mc "I’ll take care of you. Forever."
            scene ep4_sc17_lr_05
            sis "I … don’t really understand if you’re talking about loving or possessing me."
            mc "Do you think there’s a difference?"

            if sf_love_path == True:
                sis "What about [sf_name]?"
                mc "I’m not sure myself."
                mc "It’s very strange."
                mc "I like her a lot."
                mc "I might even say that I’m falling for her."
                mc "However I don’t feel like what I just told you is false, or wrong."
                mc "I have something for both of you."
                mc "Something different. But something real."
                scene ep4_sc17_lr_04
                sis "You love both of us, differently?"
                mc "I do."
                mc "Is it wrong?"
                mc "Do you want me to make a choice?"
                sis "You would chose her..."

                menu:
                    "Yes, I would.":
                        mc "And it would pain me."
                        mc "But she would be a much more reasonable choice."
                        sis "Of course, she is."
                        mc "That doesn’t mean I would forget you."
                        mc "Even if I have to choose her, I’ll be there for you."
                        mc "Whatever happens, I’ll take care of you."
                    "I would chose you. [sisLovePath] [sisSubPath]":

                        $ ep4subchoice = True
                        $ ProcessStat(2, "sis_submission")
                        $ ProcessStat(2, "sis_affection")
                        $ DumpNotStack()
                        mc "Without hesitation."
                        sis "You’re lying, obviously."
                        mc "No, I’m not."
                        mc "I'll go tell [sf_name] that it’s over, right this instant."
                        mc "If that’s what it costs to gain your trust, it’s a price I’ll pay gladly."
                        scene ep4_sc17_lr_05
                        sis "Wait! I... I don’t… I don’t know what I want, ok?"
                        sis "I’m not sure… It may not bother me… that much."
                        mc "Are you sure?"
                        sis "No! I’m not!"

    scene ep4_sc17_lr_05
    sis "All of this is so crazy…"
    sis "I feel like none this is real and I’m gonna wake up any moment."
    sis "I don’t even believe I’m considering giving in to what you’re proposing."
    sis "How is that even possible?"
    sis "Why did I obey your message?"
    sis "I’m going crazy!"
    mc "No, you’re not."
    scene ep4_sc17_lr_06
    sis "I’ve let you finger me!"
    sis "I’ve let you lick my pussy!"
    if ep3sisdoubleorgasm == True:
        sis "I sucked your dick for god's sake!"
    sis "I’m a slut!"
    mc "You’re not a slut."
    mc "Would you have let anyone else do these things to you?"
    sis "I… don’t think so…"
    mc "You’re just a unique girl, who has special needs."
    mc "It’s ok. And I’m here to fulfil these needs."
    mc "I’m here for you now."
    mc "Look at me."
    scene ep4_sc17_lr_07
    $ UnlockThat("ep4/ep4_sc17_lr_07")
    off "I gently caress her face."
    off "Her skin is soft as silk."
    off "Her lips are an invitation."
    off "I want to kiss them before filling up that mouth with my cock."
    off "I was awaiting this moment and surely build some expectations, but still… she has an immediate effect on me."
    off "She makes me horny as fuck."
    off "I barely touched her face and my dick is hardening like crazy."
    off "Controlling myself is harder every day."
    off "She’d better get ready to fuck soon."
    off "Keep cool, [mc_name]."

    menu:
        "Princess… [sisSubPath]":
            $ ProcessStat(2, "sis_submission")
            $ DumpNotStack()
            mc "You’re making me hard."
            mc "Again."
            mc "You’re doing it on purpose, aren't you?"
        "You are magical. [sisLovePath]":


            $ ProcessStat(1, "sis_submission")
            $ ProcessStat(2, "sis_affection")
            $ DumpNotStack()
            mc "You’re doing something to me."
            mc "You’re unlike any other girl."
            mc "You arouse me to the point that I lose my mind."
            mc "I can’t think about anything else but you."
            mc "You’re doing it on purpose, aren't you?"

    sis "I’m not doing anything…"
    mc "Maybe it’s your perfume."
    sis "I’m not wearing any…"
    scene ep4_sc17_lr_08
    $ UnlockThat("ep4/ep4_sc17_lr_08")
    mc "I like your scent. It’s intoxicating."
    off "She shivers as I’m breathing in her neck."
    mc "I’m curious."
    mc "Does your entire body smell that way?"
    sis "I don’t know…"
    mc "We should make sure."
    mc "Remove your clothes."
    off "She seems to be about to say something but finally stays silent."
    scene ep4_sc17_lr_09
    $ UnlockThat("ep4/ep4_sc17_lr_09")
    off "She obeys my wish without complaining."
    off "I take a couple steps back to fully enjoy the view."
    off "She tries to hide her breasts and her pussy with little success."
    mc "Remove your hands and turn around, slowly."
    mc "I want to see you."
    scene ep4_sc17_lr_10
    $ UnlockThat("ep4/ep4_sc17_lr_10")
    off "She’s a bit reluctant but still complies."
    off "She’s amazing."
    off "I’ve already seen most of her one way or another, but I actually never really fully witnessed the magnificence of her body."
    off "I can’t help but thinking that she’s perfect."

    scene ep4_sc17_lr_13
    $ UnlockThat("ep4/ep4_sc17_lr_13")
    off "Her ass is not as large nor as round as [sf_name]’s, but it’s still perfect to me."

    scene ep4_sc17_lr_11
    $ UnlockThat("ep4/ep4_sc17_lr_11")
    off "Her breasts actually look a bit bigger than [sf_name]’s but their shape is very different."
    off "They’re clearly perfect."

    scene ep4_sc17_lr_12
    $ UnlockThat("ep4/ep4_sc17_lr_12")
    off "Her belly: perfect."
    off "Her legs: perfect."
    off "She is perfect."
    off "I’m obviously too horny to be objective."


    scene ep4_sc17_lr_14
    $ UnlockThat("ep4/ep4_sc17_lr_14")
    mc "How do you feel, exposing yourself to me?"
    sis "It’s humiliating."
    mc "Are you ashamed?"
    off "She nods."

    menu:
        "You like it, don’t you? [sisSubPath]":
            $ ProcessStat(2, "sis_submission")
            $ DumpNotStack()
            scene ep4_sc17_lr_15
            $ UnlockThat("ep4/ep4_sc17_lr_15")
            mc "Being ashamed."
            mc "You like it when I put you in that kind of position."
            mc "Look at you."
            mc "Your nipples are as hard as my dick."
            off "God, I’m going to suck on these nipples."
            off "Just wait a couple minutes, Princess."
        "You are the most beautiful thing I’ve ever seen. [sisLovePath]":


            $ ProcessStat(1, "sis_submission")
            $ ProcessStat(2, "sis_affection")
            $ DumpNotStack()
            scene ep4_sc17_lr_16
            $ UnlockThat("ep4/ep4_sc17_lr_16")
            mc "You are simply perfect, Princess."
            mc "Nobody can compare to you."
            mc "That’s a fact."
            mc "You’re gorgeous."
            mc "However, you can continue acting shy and shameful if you want."
            mc "That makes you even more enticing to me."


    scene ep4_sc17_lr_17
    $ UnlockThat("ep4/ep4_sc17_lr_17")
    off "I take my shorts off, just to be more comfortable."
    off "[sis_name] tenses a bit."
    mc "Look at it. This is your doing."
    off "She gazes over my cock before shyly looking away as she used to."
    mc "You want it, don’t you?"
    mc "You want to take it in your mouth and suck on it."
    mc "You want it inside you."
    mc "It’s more and more difficult for you to deny this."
    mc "You’ll ask for it soon."
    off "I take her hand and lead it to my dick."
    scene ep4_sc17_lr_18
    $ UnlockThat("ep4/ep4_sc17_lr_18")
    off "She grabs it without much hesitation and starts stroking it."
    scene ep4_sc17_lr_19
    $ UnlockThat("ep4/ep4_sc17_lr_19")
    off "I caress her back, all along her spine and finally clutch her asscheek."
    off "She’s firm and yet soft."
    off "God, this is so satisfying."
    off "I should have done it sooner."
    off "My fingers slowly slide to meet her anus."
    off "She seems a bit surprised but doesn’t stop working on my shaft."
    off "I whisper in her ear."
    scene ep4_sc17_lr_20
    $ UnlockThat("ep4/ep4_sc17_lr_20")
    mc "How is it between your legs? Are you wet?"
    off "She nods."
    mc "Do you want me to lick your pussy?"
    off "She nods again, almost imperceptibly."
    mc "Princess, you’ll have to say it."
    mc "Tell me. What do you want?"
    off "She struggles to let it out but finally speaks the words."
    sis "I want you to lick my pussy."
    mc "How do you ask for something you want when you’re a polite little princess like you?"
    sis "Can you lick my pussy, please?"
    mc "Ooh, Yes, I can."
    scene ep4_sc17_lr_21
    $ UnlockThat("ep4/ep4_sc17_lr_21")
    off "I gently lead her to the nearest armchair and have her bend over it."
    off "I caress her back and feel her ass some more while enjoying the view."
    mc "Princess, You’re making me so horny… I’m having a very hard time controlling myself."
    mc "I hope you appreciate my efforts for what they're worth."
    mc "I'm trying very hard to be a gentleman."
    off "She doesn’t reply."
    off "Her breathing speaks for her."
    off "She’s as excited as I am."
    off "My fingers gently reach her pussy."
    off "I spend some time playing with it, enjoying [sis_name]’s reaction when I softly touch her lips."
    scene ep4_sc17_lr_22
    $ UnlockThat("ep4/ep4_sc17_lr_22")
    off "She moans when I insert my medium inside her."
    mc "You’re indeed, very wet."
    mc "You longed for this, didn’t you?"
    off "No answer. She lowers her head."
    mc "I want to hear you, Princess."

    off "She almost screams it."

    if sis_sub_love_path == True:
        sis "I did!"
        off "My finger goes in and out of her."
        off "She has trouble keeping her voice in check."
        off "It’s dangerous."
        off "[sf_name] may hear us."
        off "I like it."
        mc "Since when?"
        off "She moans loudly."
        sis "Last night! Right after I left you."
        mc "Oh. Did you want some more?"
        mc "You should have asked for it."
    else:
        sis "I didn’t! I didn’t!"
        off "My finger goes in and out of her. She has trouble keeping her voice in check."
        off "It’s dangerous. [sf_name] may hear us. I like it."
        mc "You are a very bad liar, Princess."
        off "She moans loudly."

    off "She’s incredibly tight."
    off "I can’t help but find this very promising."
    mc "Spread your legs more."
    off "She complies immediately."
    scene ep4_sc17_lr_23
    $ UnlockThat("ep4/ep4_sc17_lr_23")
    off "I kneel between her legs and start working on her with both my fingers and my tongue."
    off "She continuously groans and starts shaking a few minutes later."
    off "Making her come is easy."
    off "I know I’m not some kind of god of the cunnilingus or anything like that."
    if ep4sfpussylicked == True or ep4mcassfucked == True:
        off "I failed to make [sf_name] come a little sooner after all."
    scene ep4_sc17_lr_24
    off "It’s more like [sis_name] and I have an insane level of compatibility."
    off "I have more or less no idea what I’m doing but I can make her orgasm without any difficulty and she can make me unload just as fast."
    off "Maybe it’s a combination of things."
    off "Physical and psychological."
    scene ep4_sc17_lr_25
    $ UnlockThat("ep4/ep4_sc17_lr_25")
    off "Her legs cease to support her and she falls to the ground."
    off "I work my shaft while looking at her."
    mc "What are you doing?"
    mc "I haven’t finished yet."
    sis "I can’t… my legs…"
    off "I help her stand up."
    scene ep4_sc17_lr_26
    $ UnlockThat("ep4/ep4_sc17_lr_26")
    off "She tries to bend over the back of the armchair again but falls on it."
    off "Her feet don’t even touch the ground anymore."
    off "I go back between her legs and resume my licking."
    off "She’s not wet. She’s completely drenched."
    off "I can basically drink her."
    off "I like it."
    off "She’s moaning again, but this time, her voice is muffled the cushion of the armchair."
    off "I grab her ass with both my hands and eat her like a mad man."
    off "A few minutes later, her legs start shaking again."
    off "She completely loses control and lets out a groan that would have surely woke up [sf_name] if it hadn’t been muffled."
    scene ep4_sc17_lr_27
    off "I stand up and take a couple minutes to look at her, stuck in this absurd and humiliating position."
    off "I enjoy the show."
    off "Her body is still trembling."
    scene ep4_sc17_lr_28
    $ UnlockThat("ep4/ep4_sc17_lr_28")
    off "Slowly, I take her in my arms and lift her from the armchair."
    off "She doesn’t weigh much. She looks completely exhausted."
    scene ep4_sc17_lr_29
    $ UnlockThat("ep4/ep4_sc17_lr_29")
    off "I install us on the sofa and make her lay on my lap."
    off "She still searches for her breath."
    off "One of my hand runs over her belly as the other one plays with her hair."
    mc "Did you enjoy it, Princess?"
    sis "Yeah…"
    off "Her voice is nothing but a murmur."
    mc "It’s fortunate, because I enjoy licking you."
    mc "I plan to do it again. Often."
    sis "I like it…"

    menu:
        "Give her the choice. [sisLoveSubPath]" if sis_sub_love_path == True and sis_affection > 34:
            $ ProcessStat(5, "sis_submission")
            $ ProcessStat(5, "sis_affection")
            $ DumpNotStack()
            scene ep4_sc17_lr_30
            $ UnlockThat("ep4/ep4_sc17_lr_30")
            off "I bend over her to the point that our lips almost touch."
            off "Her breathing intensifies."
            mc "I want an answer, Princess, I want it now."
            mc "If you agree to be mine, I will have you how I want, whenever I want, wherever I want."
            mc "I promise I’ll be gentle and patient."
            mc "You can put on a show and pretend in front of everyone, but ultimately, you will do as I say."
            mc "You will obey me."
            mc "And you will like it."
            off "She stays silent for a while before falling into some kind of panic mode."
            scene ep4_sc17_lr_31
            sis "This is crazy."
            sis "I don’t understand!"
            sis "Why am I ok with that?"
            sis "Why do I let you do these things to me?"
            sis "I know this isn’t normal, I know this is wrong!"
            sis "But I want to say yes."
            sis "Why do I want to say yes?"
            sis "I’m terrified!"
            off "She’s about to cry."
            off "I gently stroke her head."
            mc "Shhhhh. It’s ok, Princess."
            mc "I’ve already told you."
            mc "You don’t have to be ashamed, or afraid or anything."
            scene ep4_sc17_lr_32
            mc "I’m here for you."
            mc "I’ll always be there for you."
            mc "You are unique and special."
            mc "I will take care of you."
            off "She calms down a bit."
            mc "You have to say it, Princess. Do you want it?"
            off "She struggles and seems to be about to break down again when she finally lets out the word."
            off "It’s an almost inaudible whisper, but she says it nonetheless."
            sis "Yes."
            mc "You will never regret this decision. I swear."
            scene ep4_sc17_lr_33
            $ UnlockThat("ep4/ep4_sc17_lr_33")
            off "I close the last few centimetres that separates us and kiss her."
            off "Her tongues immediately rush to meet mine."
            off "She longed for that."
            off "She shivers."
            off "I flatter myself and imagine she has an orgasm just kissing me."
            scene ep4_sc17_lr_34
            $ UnlockThat("ep4/ep4_sc17_lr_34")
            off "I gently fondle her breast as I realize that it’s done."
            off "She’s mine."
            off "She belongs to me."
            off "I promised to be gentle and patient but I can probably fuck her right this instant."
            off "That wouldn’t be very smart."
            off "Let us build some expectations for one more day at least."
            scene ep4_sc17_lr_35
            $ UnlockThat("ep4/ep4_sc17_lr_35")
            off "I break the kiss. She looks at me with an indefinable expression."
            sis "I can’t believe I said yes."
            mc "You are mine now."
        "Don’t give her the choice. [sisSubPath]":



            $ ProcessStat(7, "sis_submission")
            $ DumpNotStack()
            scene ep4_sc17_lr_36
            $ UnlockThat("ep4/ep4_sc17_lr_36")
            off "I softly grab one of her breasts and fondle it gently."
            mc "You are mine now."
            off "She seems a bit surprised."
            sis "Wait, I…"
            mc "You agreed to that when you stripped."
            sis "I didn’t..."
            mc "I’ll be gentle, and patient, as I promised, but you are mine."
            mc "There is nothing to discuss."
            mc "You are my property."
            mc "I gave you a choice, and you agreed."
            off "She looks away and stops arguing."
            mc "Don’t worry princess, you won’t regret it."

    mc "And by the way, Princess, your breasts are fantastic."
    sis ".. Thank you…"
    mc "You’re welcome."
    scene ep4_sc17_lr_37
    $ UnlockThat("ep4/ep4_sc17_lr_37")
    off "My hand slowly migrates to her pussy and she opens her legs."
    off "She’s still wet."
    off "I immediately finger her."
    off "She moans in surprise."
    off "I work her a few seconds before going for something more interesting."
    mc "Let’s try something else, Princess."
    off "I help her raise and show her the sofa."
    mc "Kneel here. And bend over."
    scene ep4_sc17_lr_38
    $ UnlockThat("ep4/ep4_sc17_lr_38")
    off "She complies and takes the position I expected."
    off "I slowly work my shaft looking at her body."
    mc "You have the finest ass I’ve ever seen."
    scene ep4_sc17_lr_39
    $ UnlockThat("ep4/ep4_sc17_lr_39")
    off "I get behind her and bring my cock to her pussy."
    off "She gasps and tenses immediately."
    off "She probably thinks I’m going to fuck her."
    off "She doesn’t complain."
    off "I use my glans to caress her lips and clitoris."
    scene ep4_sc17_lr_40
    $ UnlockThat("ep4/ep4_sc17_lr_40")
    off "My dick finds her way between her thighs."
    off "I grab her hips and start pumping on her as if I was fucking her."
    off "My whole length gently rubs against her pussy."
    off "Her crotch is wet and burning hot."
    off "I’m sliding in easily."
    off "Her surprise dissipate into pleasure after a couple thrust."
    off "She closes her legs even tighter and starts moaning."
    scene ep4_sc17_lr_41
    $ UnlockThat("ep4/ep4_sc17_lr_41")
    off "I progressively hump her faster."
    off "I do my best to massage her clitoris with my entire shaft."
    off "Sometimes, my glans bumps against her pussy and startles her."
    off "I have to be careful."
    off "I don’t want to accidentally penetrate her."
    mc "Do you like that Princess?"
    sis "Yes!"
    off "Her reply was immediate."
    mc "Does it feel good?"
    sis "Yes!"
    off "She’s completely letting go of her inhibitions. I like it."

    if sis_sub_love_path == False:
        off "I pull out and make her kneel before me."
        scene ep4_sc17_lr_47
        $ UnlockThat("ep4/ep4_sc17_lr_47")
        off "I grab her head and insert my dick in her mouth."
        off "She immediately starts sucking on it."
        off "It doesn’t take more than a minute for me to come."
        scene ep4_sc17_lr_48
        $ UnlockThat("ep4/ep4_sc17_lr_48")
        off "I get my dick out and spread my load on her face."
        scene ep4_sc17_lr_48_true
        $ UnlockThat("ep4/ep4_sc17_lr_48_true")
        off "She takes it without flinching."
        off "I cover her in semen, roaring far too loudly as I feel my cum rushing through my shaft."
        off "She looks surprised."
        mc "I hope you liked it as much as I did, Princess."
        mc "It was fantastic."
        mc "And this was nothing compared to what tomorrow will be."
        mc "I can’t wait. Can you?"
        scene ep4_sc17_lr_49
        $ UnlockThat("ep4/ep4_sc17_lr_49")
        off "She doesn't respond and looks away."
        off "She seems to be back to her shy and ashamed self."
        off "I made amazing progress today."
        off "I’ll fuck her tomorrow."
        off "I have no doubt about that."
        off "She’ll be ready."
        off "She’ll ask for it."
        mc "I think it’s time to get some sleep."
        scene ep4_sc17_lr_50
        $ UnlockThat("ep4/ep4_sc17_lr_50")
        mc "Goodnight Princess."
        off "She stays on the floor as I pick up my shorts and leave the room."
        off "She doesn’t move an inch."
    else:
        scene ep4_sc17_lr_42
        $ UnlockThat("ep4/ep4_sc17_lr_42")
        off "I pull out and make her lay on her back."
        off "I grab her legs tight and thrust like a mad man."
        off "I don’t last more than a couple minutes more."
        off "The spectacle of her jiggling breasts is mesmerizing."
        scene ep4_sc17_lr_43
        $ UnlockThat("ep4/ep4_sc17_lr_43")
        off "She looks at me while I unload on her tummy."
        off "I cover her in semen, roaring far too loudly as I feel my cum rushing through my shaft."
        scene ep4_sc17_lr_44
        $ UnlockThat("ep4/ep4_sc17_lr_44")
        off "I slowly let go of her legs as she looks and carefully touches the seed I just poured on her belly."
        mc "I hope you liked it as much as I did, Princess."
        mc "It was fantastic."
        mc "And this was nothing compared to what tomorrow will be."
        mc "I can’t wait. Can you?"
        off "She doesn't respond and looks away."
        off "She seems to be back to her shy and ashamed self."
        off "I made amazing progress today."
        off "I’ll fuck her tomorrow."
        off "I have no doubt about that."
        off "She’ll be ready."
        off "She’ll ask for it."
        off "I take her hand and help her to get up."
        mc "You may want to clean yourself before getting some sleep."
        mc "I’ll take care of the mess here."
        scene ep4_sc17_lr_45
        $ UnlockThat("ep4/ep4_sc17_lr_45")
        off "I kiss the back of her hand."
        off "She doesn’t know how to respond."
        off "I guess we’ll both need to adapt to our new relationship."
        mc "Goodnight, Princess."
        sis "… Goodnight…"
        scene ep4_sc17_lr_46
        $ UnlockThat("ep4/ep4_sc17_lr_46")
        off "She slowly heads out and seems to hesitate."
        off "She stops a second at the entrance and turns to me as if she was about to say something."
        off "We look at each other for a moment in silence and she finally picks up her clothes and leaves the room."
        off "I’ve put semen on the sofa as well as on the carpet."
        off "I hope it won’t get stained."
    $ renpy.end_replay()
    return


label ep4sc17:

    scene black with fade
    with Pause(2)
    show text "Later that night."
    with Pause(2)
    off "I can’t stop thinking about what happened and what I’ve done today."

    scene ep4_sc13_mcr_00 with fade
    if ep4sobcome == True:
        off "I can't believe he got the balls to come here and try to take her."

    if ep4handshaked == True:
        off "Why the fuck did I side with those assholes?"
        off "If anyone ever learns about this, I’m dead."
        off "I can’t even remember what I was thinking I would gain doing that."
        off "Do I really want to fuck [sis_name]?"
        off "Do I want it enough that I’m ready to give her to a rapist to have a chance to put my dick inside her?"
        off "Come on [mc_name]."
        off "You’re not giving anyone a chance."
        off "She wants it."
        off "She wants that big fat dick."
        off "And we don’t have any proof that this dude is actually a rapist."
        off "It may very well be a misunderstanding."
        off "Yeah sure…"
        off "And you’re suddenly ok with him fucking [sis_name]?"
        off "Not really but… But if I can fuck her…"
        off "[mc_name], It’s obvious that the guy is going to rip her pussy apart."
        off "I’m sure his dick is humongous."
        off "Douche-bags always have the biggest cocks."
        off "He’s going to hurt her."
        off "[sf_name]’s right."
        off "Now that you've acknowledged it, here are the questions you need to answer:"

        off "Do you want to fuck [sis_name]?"

        off "Do you want to fuck her at any cost?"
        off "Are you ready to serve her to a monster to fuck her?"


        menu:
            "I would like to fuck her… [gr]\[HateRegret\]":
                $ ep4hateregrets = True
                off "I can’t deny it…"
                off "But not at any cost…"
                off "I fucked up big time."
                off "I can’t even back down now."
                off "If I tell them that I’m not interested anymore, they could blackmail me."
                off "If they tell anyone about our arrangement, I’m going to jail."
                off "Calm down, [mc_name]."
                off "[sf_name] threw him out today, maybe they won’t even try something else."
                off "If we’re lucky we won’t hear about them ever again and no one will ever know how much of an asshole I am."
                off "Yeah... I don’t believe it for a single minute."
            "That bitch doesn’t give a shit about me. [gr]\[HateMotivation\]":

                $ ep4hatemotivation = True
                off "I don’t see why I should care about what happens to her."
                off "I tried to help her, she didn’t give a fuck."
                off "If she doesn’t respect me, I don’t see why I should respect her."
                off "If I have a chance to fuck her before that bastard stretches her pussy, I’ll take it."
                off "It'll teach her a lesson."
                off "Of course, I would prefer to keep her for myself as a fuck toy, but you can’t always get what you want."
                off "As Steve said: YOLO."

    if ep4sobbetrayed == True:
        off "Why the fuck did I side with those assholes?"
        off "If anyone ever learns about this, I’m dead."
        off "I can’t even remember what I was thinking I would gain doing that."
        off "Did I really hope to get information or did I just want to... fuck [sis_name]…?"
        off "I’m fucking crazy."
        off "Luckily for me, I came to my senses before doing something really stupid."
        off "These motherfuckers are probably even more enraged with us after that."
        off "I’d better be careful."


    if ep4decisivefail == True:
        off "I gave my all in that speech."
        off "It’s a shame it didn’t work out."
        off "She may have hesitated at some point but in the end, I couldn’t convince her."
        off "Maybe my words weren’t good enough."
        off "Was I too harsh?"
        off "Maybe it’s just too late, maybe our relationship is already damaged beyond repair."
        off "We were lucky [sf_name] could get her to listen."
        off "If she hadn’t been there, [sis_name] would probably be somewhere else with her pussy torn asunder by this scumbag and his brother."
        off "I can’t even begin to imagine the repercussions."

    if ep4decisivesuccess == True:
        off "[sis_name]’s tears were... Unexpected."
        off "I never thought that my words could have such an impact on her."
        off "I guess there’s hope for our brother/sister relationship."
        off "However, I have no idea how to behave from here."
        off "She probably doesn’t know either."
        off "Honestly, I’m surprised myself with what I told her."
        off "I came as far as telling her I love her!"
        off "And I didn’t have to force myself."
        off "It came out spontaneously."
        off "I have no idea where this is headed."
        off "I hope she doesn’t expect me to be some kind of perfect brother from now on because I don’t think I’ll fit nicely into the role."

    scene ep4_sc13_mcr_01

    if ep4handshaked == True or ep4decisivefail == True:
        off "I’m almost asleep when some noise coming from the hallway gets my attention."
        off "Some muffled footsteps."
        off "Someone is knocking on [sf_name]’s door?"
        off "Obviously, it’s [sis_name]."
        off "I can’t understand what she says."
        off "What the fuck are they doing in the middle of the night?"
        scene ep4_sc15_mcr_00
        off "I try to ignore what’s happening but the curiosity ends up getting the best of me."
        off "I get up and carefully head to the hallway and [sf_name]’s bedroom."
        scene ep4_sc18_c_00
        $ UnlockThat("ep4/ep4_sc18_c_00")
        off "I stick my ear to the door."
        off "Nothing. It’s perfectly silent."
        off "I head to [sis_name]’s bedroom."
        scene ep4_sc18_c_01
        off "Nothing either."
        off "I have to be sure."
        off "I take a deep breath and slowly turn the doorknob."
        off "Adrenaline is rushing to my brain as I look into the room."
        scene ep4_sc18_sr_00
        off "[sis_name] is not there."
        off "I quickly check the rest of the house but she’s nowhere to be seen."
        off "All rooms are empty and perfectly silent."
        off "She must be in [sf_name]’s bedroom."
        off "Maybe she decided to have a friendly talk and sleep with her tonight?"
        off "I should have heard them speaking though."
        scene ep4_sc18_c_00
        off "Back to [sf_name]’s door, I stick my ear to the wood once more."
        off "Wait … Is that…?"
        off "Is someone moaning?"
        off "It’s really hard to tell."
        off "Do I hear muffled groans coming from the inside or am I imagining it?"
        scene ep4_sc18_c_02
        $ UnlockThat("ep4/ep4_sc18_c_02")
        off "Holy shit!"
        off "Are they actually lesbians?"
        off "Calm down, perv, you’re imagination is running wild."
        off "Fuck!"
        off "There’s definitely someone moaning in that room!"
        off "Something is going on!"
        off "They’re lesbians!"
        off "That would explain why they’re so close, and why [sf_name]’s speech had so much impact on [sis_name]!"
        off "Maybe they’re going at it every night and I didn’t even suspect it!"
        scene ep4_sc18_c_03
        $ UnlockThat("ep4/ep4_sc18_c_03")

        if ep4handshaked == True:
            off "That slut!"
            off "If someone is stealing [sis_name] from me, it’s [sf_name] rather than the other asshole."
            off "I should have known it!"
            off "I can’t believe I saw nothing."
            off "It so obvious…"
            off "They take showers together for God’s sake!"
            off "Fuck! How could I be so blind?"
            $ ep4hatelesbiansbad = True
        if ep4decisivefail == True:
            off "Holy shit!"
            off "I wonder who’s eating who."
            off "They’re probably eating each-other in sixty-nine."
            off "That’s so hot!"
            off "I’m hard just thinking about it."

            off "[sis_name] is fucking her best friend in my parents' bedroom!"

            $ ep4hatelesbiansgood = True

        off "I need to jerk off."

    if ep4decisivesuccess == True:
        off "I’m almost asleep when my phone lightly buzzes."
        scene ep4_sc18_mcr_00
        $ UnlockThat("ep4/ep4_sc18_mcr_00")
        $ ep4nighttalk = True
        off "It’s a text message."
        off "From [sis_name]."
        sis "I was hungry. I made a sandwich. There’s too much. Want some?"
        off "What the fuck? Is that a joke?"
        mc "No thank you. I’m trying to sleep."
        sis "Come on, [mc_name]."
        off "Is she trying to annoy me?"
        mc "It’s 2 AM. And I’m not hungry."
        sis "Please."
        mc "Can’t you just put it in the fridge?"
        sis "Can’t you read between the lines for once? I can’t sleep, and I want to talk with you."
        off "Goddamn crazy. What the hell is this all about?"
        mc "It better be worth it."
        off "I get up and heads towards the kitchen."
        scene ep4_sc19_k_00
        $ UnlockThat("ep4/ep4_sc19_k_00")
        off "She sits at the counter with a barely touched sandwich."
        mc "Ok, girl. What’s gotten into you?"
        sis "Hey."
        off "She looks… sorry."
        off "I’ve set foot in the kitchen angry, but that anger now subsides."

        menu:
            "Ok. Let’s see that sandwich. [sisLovePath]":
                mc "I may be hungrier than I thought."
                off "I notice a faint smile briefly showing on her face as I sit next to her."
                $ ProcessStat(2, "sis_affection")
                $ DumpNotStack()
            "That sandwich better be good… [sisSubPath]":

                mc "Or I swear, I’ll spank your ass into hell."
                off "She tenses a bit as I sit next to her."
                $ ProcessStat(1, "sis_affection")
                $ ProcessStat(1, "sis_submission")
                $ DumpNotStack()

        scene ep4_sc19_k_01
        $ UnlockThat("ep4/ep4_sc19_k_01")
        sis "I… I’m sorry, I didn’t know how to get you to come here."
        mc "You just had to ask."
        off "She pushes the sandwich to my side."
        scene ep4_sc19_k_02
        $ UnlockThat("ep4/ep4_sc19_k_02")
        off "Honestly, it doesn’t look that good."
        sis "I wanted to talk."
        mc "Again, you just had to ask. No need to make a sandwich for me."
        sis "I hope I didn’t wake you up."
        mc "You didn’t. I couldn’t sleep either."
        off "There’s no way I'm eating that thing."
        off "I’m not hungry and it’s not even appetizing."
        mc "So.. You wanted to talk about…?"
        scene ep4_sc19_k_03
        sis "Us."
        mc "Us?"
        scene ep4_sc19_k_04
        $ UnlockThat("ep4/ep4_sc19_k_04")
        off "She looks embarrassed."
        sis "The things you said… when Luke was here…"
        mc "Yeah?"
        sis "You said that you cared. About me."
        mc "And?"
        sis "Is that true?"
        off "She wants confirmation."
        mc "You want me to say it again?"
        sis "… I want to know if you’re sincere."
        scene ep4_sc19_k_05
        $ UnlockThat("ep4/ep4_sc19_k_05")
        mc "Princess…"
        mc "I’ll say it again."

        mc "You’re like a sister to me."

        mc "And I love you."
        mc "I care about you."


        mc "Even if I’m often a moron, even if you’re sometimes a bitch, even if we hate each other, I care about you."
        mc "Now that doesn’t mean I’ll be a perfect loving friend or anything like that."


        mc "I’m still a perv and a moron, I will probably still annoy you, jerk off in your panties or I don’t know what else."
        mc "But that doesn’t mean that I don’t care about you."
        mc "To be honest, I thought about it a lot today."
        mc "And I came to realize that if I was so angry at you over the last three years, it’s because I love you."
        mc "I know it doesn’t make sense. But it’s how it is."
        mc "I’m sorry I didn’t believe you."
        mc "That’s a fact. I failed you. We failed you."
        scene ep4_sc19_k_06
        mc "But you have your share of responsibility."
        mc "You should have fought more."
        mc "I know it doesn’t sound fair, and it’s easy for me to say as I wasn’t in your position."
        mc "But it’s true."
        mc "Somehow, you also let us down by letting us believe these bullshit."
        mc "But it’s not too late."
        scene ep4_sc19_k_07
        mc "We can start anew."
        mc "But we’ll have to trust and accept each other."
        mc "Do you think we can do that?"
        mc "That’s what you really want to talk about, isn’t it?"
        mc "You want to know if we can still be brothers and sisters, if we can salvage our relationship."
        mc "Am I wrong?"
        mc "Well, you can answer that question yourself."
        mc "Do you want it?"
        off "Where have I found so many things to say?"
        off "I feel like I literally stunned her under an uninterrupted flow of words."
        off "She avoids my gaze and shyly replies."
        sis "I want it."
        mc "Ok then."
        off "I stand up and take her hand."

        mc "Can I finally have a hug?"

        scene ep4_sc19_k_08
        $ UnlockThat("ep4/ep4_sc19_k_08")
        off "She gets up and bursts out crying as I take her into my arms."
        off "She feels warm but fragile as she huddles onto me."
        sis "You’re a moron."
        mc "And a perv, I’ll probably grope your ass before we separate."
        off "Laughing mixes to the sobbing."
        sis "I think I wouldn’t even get mad."
        mc "Don’t tempt me."
        sis "Ok then, if you grope me, I’ll kill you."
        mc "Now, that’s way better."
        off "We keep silent for a few seconds."
        mc "I missed you."
        off "I don’t know where it’s coming from. I say it anyway."
        scene ep4_sc19_k_08_bis
        $ UnlockThat("ep4/ep4_sc19_k_08_bis")
        off "She burst out in tears again."
        sis "I missed you too."
        off "I gently pat her head as we go back to silence. We stay like that for several minutes until [sis_name] stops crying."
        mc "So… about that guy…"
        sis "I don’t know what I was thinking."
        sis "You and [sf_name], you’re obviously right."
        sis "I feel so dumb about that."
        sis "I’ve let him kiss me and touch me."
        sis "I disgust myself."
        mc "Easy, Princess. It’s ok."
        mc "It’s over now."
        sis "Yeah… I’ll text him to let him know I don’t want to see him ever again."
        mc "If he ever tries anything, you let me know, ok?"
        sis "Ok."

        off "Suddenly it doesn’t seem so hard or so bad to be a decent friend."

        mc "However, about groping that ass…"
        scene ep4_sc19_k_09
        $ UnlockThat("ep4/ep4_sc19_k_09")
        off "She laughs again and kisses me on the cheek as she breaks our embrace."
        sis "Maybe next time, perv."
        off "She looks completely exhausted."
        mc "Yeah, I think you’d better get to your bed."
        mc "You look tired as fuck."
        sis "I am. Good night, [mc_name]."
        mc "Good night, Princess."
        off "She leaves the room."
        scene ep4_sc19_k_10
        $ UnlockThat("ep4/ep4_sc19_k_10")
        off "It’s very strange."
        off "I think I’m happy."
        off "Now that I feel it, I realize that it has been a long time."
        off "In fact, it has been so long that I almost forgot what it’s like, to be happy."
        off "I’d better not talk about that with Steve, or he will mock me until the end of times."
        off "God, what did she put in that thing?"
    return


label ep4neutralend:

    scene black with fade
    with Pause(2)
    show text "Later that night."
    with Pause(2)
    off "I can’t stop thinking about the events of the day."

    scene ep4_sc13_mcr_01 with fade

    off "I don't know why but I have a feeling that our psycho brothers problem is only going to get worse."
    off "Let's get real: there's nothing I can do."
    off "We should have gone to the police as soon as it started."
    off "It's probably too late now."
    if ep4kfmeetingok == True:
        off "And Kelly..."
        off "I still have very mixed feelings about her."
        off "Her story was sad and sounded very convincing, but I still don't know if I believe her."
        off "The only thing I can be sure of is that I'm a moron with a weakness for cute girls."
        off "She may very well know that and use it against us."
        off "Or... she may be sincere."
        off "Yeah... sure."
        off "Get real, [mc_name]."
        off "A girl that cute? Having a crush on you?"
    off "Fuck."
    off "I hope tomorrow will be simpler."




label ep4end:

    scene black with dissolve
    with Pause(2)
    show text "End of Day 4" with dissolve
    with Pause(2)
    scene endscreen with dissolve

    menu:
        "This is the end of Day 4. You may want to save here."
        "Exit to main menu.":
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
