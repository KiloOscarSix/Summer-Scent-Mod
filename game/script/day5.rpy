

label day5start:
    scene black with dissolve
    with Pause(2)
    show text "Day 5 - Wednesday" with dissolve
    with Pause(2)
    show text "The morning" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(2)


    if sis_sub_path == True and sis_sub_love_path == False:
        $ sis_hard_sub_path = True

    if ep4dompathended == True:
        $ sf_dom_path = False

    if sis_love_path == True:
        jump ep5sc1
    else:
        jump ep5sc5


label ep5sc1:
    if ep4sflovetalked == True:
        scene ep5_sc1_sr_00 with dissolve
    else:
        scene ep5_sc1_sr_14 with dissolve
    off "I have no idea what time it is."
    off "I don't really care."
    off "Holding her in my arms is comfortable."
    off "She's warm and her skin is soft."
    off "She still smells like vanilla."
    off "I like that."
    off "I slowly caress her while emerging from my slumber."


    if sf_love_path == True and ep4sflovetalked == True:
        off "It's so strange."
        off "A few days ago we hated each other or at least acted like we did."
        off "Then we became... lovers..."
        off "It lasted only two nights and a day, and we had to hide it."
        off "It felt like heaven."
        off "Like finally being just at the right place for the first time in my life."
        off "With the right person."
        off "And I'm about to lose all that."
        off "It's painful."
        scene ep5_sc1_sr_01
        off "It's her decision and I know it's the right thing to do."
        off "But I don't want to do the right thing."
        off "I know it's selfish."
        off "I don't care."
        off "But I love [sf_name] too."
        off "I can't deny it."
        off "If I'm being honest, I don't want to choose because I don't want to hurt either of them but also because I simply can't choose."
        off "I'm the worst."
        off "I've told [sis_name] that it won't work, that I can't force myself to love [sf_name], but it's completely false."
        off "I want to protect and love her just as much as I want [sis_name]."
        off "Maybe I have a thing for strange crazy damaged girls."
        scene ep5_sc1_sr_02
        sis "Hey."
        off "She barely wakes up. Her voice is still heavy with sleep."
        mc "Hey, Princess."
        off "I can't see her face but I can guess her smile fading as she remembers that these are our last moments together."
        mc "Morning has come, and I still love you."
        sis "Don't do that, please, it'll only make things more difficult..."
        off "I know. But I still want you to know it."
        off "Fuck, am I going to cry again?"
        sis "Thank you."
        mc "What for?"
        scene ep5_sc1_sr_03
        sis "For saying no... You know... Last night... You could have...."

        menu:
            "Yeah, about that... [sisLovePath]":
                $ ep5aboutthat = True
                mc "Is that offer still open?"
                off "She laughs."
                off "A sad laugh that hides her desire to cry."
                sis "You missed your chance, moron."
                mc "Too bad."
                mc "I'm sure it would have been great..."
                mc "I can't believe I didn't even grab your breasts."
                mc "They look incredible."
                $ ProcessStat(1, "sis_affection")
                $ DumpNotStack()
                off "She slowly gets on top of me, like last night."
                scene ep5_sc1_sr_06
                off "She looks sad and tired but tries to smile."
                sis "Incredible?"
                off "I can't help but heavily stare at her chest."
                scene ep5_sc1_sr_07
                off "She's beautiful."
                off "She grabs my hands and holds them on her breasts."
                scene ep5_sc1_sr_08
                off "I gasp in surprise."
                off "Holy shit."
                sis "It's my goodbye present."
                off "I briefly hesitate to knead her like crazy but I'm clearly not in the mood."
                off "They feel perfect in the hand."
                mc "A... A kiss... would have sufficed."
                sis "You can have that too."
                off "She leans onto me and our lips join."
            "I still can't believe you offered yourself like that.":

                sis "I don't know... It seemed like a good idea..."
                mc "Would you really have made love with me if I had accepted ?"
                off "She keeps silent for a few seconds."
                sis "I think so..."
                sis "I'd thought about it all day long yesterday..."
                sis "I wasn't really ready but I would have done it..."
                mc "You are crazy."
                sis "It was my goodbye present."
                mc "You read too many of those erotic romance novels."
                scene ep5_sc1_sr_05
                off "She laughs."
                off "A sad laugh that hides her desire to cry."
                sis "You may be right."
                off "My hand crawls across her naked skin."
                off "She shivers."
                mc "Can I have a kiss?"
                sis "You can have that."
                off "She slowly gets on top of me and our lips join."

        scene ep5_sc1_sr_09
        off "It's the longest kiss we've shared."
        off "Soft, and sad."
        off "We know it's the last one."
        off "Neither of us want it to ever stop."
        off "Eyes closed, my hands are running on her naked skin as our tongues wrestle each other."
        off "I don't want that moment to end."
        off "I can hear the muffled noise of the door slowly opening."
        off "[sis_name] hears it too."
        off "She instantly raises her head."
        off "My hands are still on her."
        scene ep5_sc1_sr_10
        with Pause(1)
    else:


        off "I like being the big spoon."
        off "My morning wood has found its way between her legs."
        off "It's completely accidental but it feels nice."
        scene ep5_sc1_sr_15
        off "My shaft rubs against her ass all the way to her pussy."
        off "I'm not even completely awake and I'm already horny."
        off "What kind of perv am I?"
        off "Well, I don't really give a damn right now."
        off "This feels too good."
        off "I feel comfortable."
        off "This is just right."
        sis "Hey."
        off "She barely wakes up."
        off "Her voice is still heavy with sleep."
        mc "Hey, Princess."
        sis "Are you trying to... penetrate me?"
        mc "I'm just rubbing it."
        mc "I thought you would enjoy a gentle wake up."
        mc "Do you want me to stop?"
        sis "No..."
        off "She hesitates."
        off "She seems a bit embarrassed."
        off "Not by what I'm doing, however."
        off "She just hesitates to acknowledge that she enjoys it."
        sis "... I like it."
        off "There you go, Princess."
        mc "I figured as much."
        mc "Your pussy is getting... wetter."
        off "It feels unreal."
        scene ep5_sc1_sr_16
        off "Still half asleep, breathing heavily, she moves her pelvis and traps my dick between her legs."
        off "I gently fuck her thighs."
        off "Slowly, my glans rubs against her pussy."
        off "Maybe I'm imagining it but I can feel her lips opening to grasp my shaft as it slides against her."
        off "If I move a bit I could penetrate her."
        off "Maybe I should do it."
        off "She wants it."
        off "It's obvious."
        off "If I do it as gently as possible, it should be ok."
        off "She suddenly moves and turns before getting on top of me."
        scene ep5_sc1_sr_17
        off "She squeezes my dick between her pussy and my belly and starts grinding on it."
        sis "I'm sorry, I can't let you do that."
        sis "I'm not ready yet."
        mc "I wasn't about to do anything..."
        sis "Don't worry, perv, I don't mind you trying, as long as I can say no."
        mc "I would never force you..."
        sis "I know."
        off "Her hands on my chest, she intensifies her grinding."
        off "She softly moans."
        off "She enjoys it as much as I do."
        off "I suddenly come to realize that shared pleasure is even more... Pleasurable."
        off "It's stupid, but I like the idea."
        off "She alternates long slides to enjoy most of my shaft and short ones to concentrate on my glans."
        off "I don't know where she learned to do that but hell, it feels good."

        if sf_love_path == True:
            mc "Holy shit, Princess! "
            scene ep5_sc1_sr_18
            off "I'm about to ejaculate when I hear the muffled noise of the door slowly opening."

    if sf_love_path == True:

        if ep4sflovetalked == True:
            scene ep5_sc1_sr_11 with dissolve
        else:
            scene ep5_sc1_sr_19 with dissolve

        off "[sf_name] is there, looking at us."
        off "She's in shock."
        off "The three of us stay like that for a second full of silence and pain that last an eternity."
        off "I should do or say something but I have no idea what."
        off "That it's not what it seems?"
        off "It's exactly what it seems."

        if ep4sflovetalked == True:
            scene ep5_sc1_sr_12
        else:
            scene ep5_sc1_sr_20

        off "[sis_name] screams as [sf_name] rushes through the door."
        sis "No! Wait! Please! Wait!"

        if ep4sflovetalked == True:
            scene ep5_sc1_sr_13
        else:
            scene ep5_sc1_sr_13_alt

        off "She stands up and runs after her friend."
        off "Her voice is distorted by pain, fear, and sadness."
        off "This is what she wanted to avoid, and it's happening, right now."
        off "I follow [sis_name] into the hallway."
        if ep4sflovetalked == True:
            scene ep5_sc1_c_00
        else:
            scene ep5_sc1_c_00_alt
        off "She knocks on the door of the master bedroom, begging [sf_name] to talk to her."
        off "She bursts into tears between apologies."
        off "I don't know what to do."
        off "Everything is happening because of me."
        off "I'm guilty."
        off "From the very start, I knew it wouldn't end well but I continued to mess up the situation."
        off "I destroyed their friendship."
        off "It is all they have and I destroyed it."
        off "Well played, [mc_name]."
        off "[sis_name] looks terrified."
        if ep4sflovetalked == True:
            scene ep5_sc1_c_01
        else:
            scene ep5_sc1_c_01_alt
        off "She's going through so much pain that it seems like she's overreacting."
        off "However, it's pretty easy to understand what she's going through."
        off "She's about to lose her only friend."
        off "[sf_name] is the only person who was there for her for the last three years."
        off "She has actually been much more than a friend."
        off "A sister, or even a mother maybe."
        mc "Princess..."
        sis "Please! I'm sorry! Please! [sf_name]!"
        if ep4sflovetalked == True:
            scene ep5_sc1_c_02
        else:
            scene ep5_sc1_c_02_alt
        off "She lets herself fall on the ground, sliding against the door."
        mc "I'm sorry."
        mc "Everything is my fault."
        mc "I'll explain it to her."
        mc "It's gonna be alright."
        sis "Don't be ridiculous."
        sis "Nothing will be alright!"
        mc "Princess..."
        sis "Leave us alone please."
        mc "I want to talk to her too..."
        sis "Please! Can't you understand ?"
        off "I can."
        off "I just don't want to."
        off "You're suffering."
        off "I don't want to let you face it without me."
        mc "Ok... If it's what you want, I'll leave you alone."
        mc "But just so you know... I'm here for you."
        mc "You don't have to be alone."
        sis "Please..."
        mc "I'm going. But if you need anything, you call me, ok ?"
        off "I look at her, half-naked, sitting on the parquet."
        off "I'm sure it won't help if [sf_name] sees her like that."

        if ep4sflovetalked == True:

            scene ep5_sc1_c_03
            off "I go to her room and bring back her shirt."
        else:


            scene ep5_sc1_c_03_alt
            off "I go to her room and bring back her panties."


        mc "Here. You'd better get dressed."
        mc "I don't think you want her to see you like that."
        off "She sadly nods but doesn't make the slightest move to get dressed."
        off "I don't think she really cares about anything I say."
        off "I don't even know if she really listens or understands what I'm saying."
        off "Maybe I should help her to dress?"
        off "I'm not sure she would enjoy that kind of promiscuity right now."
        off "She just needs time."
        off "[sf_name] is probably just as shocked on the other side of this door."
        off "[sis_name] doesn't move an inch as I enter my own room and get dressed."
        off "She keeps asking [sf_name] to open the door, to talk to her."
        off "Crying her apologies over and over again while the door stays closed and the room silent."
        off "I don't want to leave her like that but she doesn't want me around."
        off "I don't really have a choice."
        jump ep5sc2
    else:


        off "I'm about to ejaculate when [sis_name] suddenly stops moving."
        sis "Wait."
        sis "What time is it ?"
        off "What? Is she serious?"
        off "She sounds worried."
        mc "I don't know..."
        off "She grabs her phone."
        scene ep5_sc1_sr_21
        sis "Just give me a second, I need to..."
        off "Girl, you can't leave me hanging there like that..."
        sis "Shit!"
        scene ep5_sc1_sr_22
        sis "I forgot to set an alarm!"
        sis "[sf_name]'s probably awake, you have to move!"
        sis "Now!"
        mc "Shit."
        scene ep5_sc1_sr_23
        off "I quickly get up from the bed, put my shorts back on and head for the door when three barely audible little knocks break my momentum."
        off "I instinctively jump into the closet and hide, holding my breath."
        scene black
        off "Lights are out, I'm surrounded by darkness, not moving an inch."
        off "The adrenaline floods my brain."
        off "Holy fucking shit."
        off "She's going to find out."
        off "There's no way she doesn't find out."




        if sf_dom_path == True:
            off "I'm done."
            off "She'll find me in this closet and she'll destroy me."
            off "If she tells [sis_name] about our little games, everything is over."
            off "Fuck!"
            off "This girl is crazy!"
            off "She'll find out and ravage our life with it!"
        else:
            off "We're done."
            off "Calm down, [mc_name]."
            off "[sf_name] only wants [sis_name]'s happiness."
            off "She'll understand."
            off "She probably won't condone it but she'll understand."
            off "She won't say a word to anyone."
            off "It'll be ok."
            off "She's a nice person, she won't even judge us."
            off "So calm the fuck down, [mc_name]."

        sf "Hey."
        sis "Hey."
        off "A second of uneasy silence."
        off "She knows."
        off "I'm sure she knows."
        sf "Am I... disturbing you?"
        off "You bet you are..."
        sis "Not at all."
        sis "Why do you ask?"
        off "[sis_name]'s voice is riddled with fear."
        sf "I don't know... You're not wearing any panties... and you seem... pretty excited if I may say."
        sis "I don't know what you're talking about."
        sf "... you're so wet that I can see it from here..."
        off "Holy shit."
        sis "Ok, I was playing with myself so what?"
        off "Good thinking, Princess."
        off "You're free to masturbate whenever you want..."
        sf "Nothing."
        sf "Do you want me to let you finish?"
        sf "Or maybe... you need a hand?"
        off "What. The. Fuck?"
        sis "It's.... I... No... I'm good, thank you..."
        off "..."
        off "[sf_name] just proposed her help to masturbate and [sis_name] seemed more embarrassed than surprised."
        off "It's a little bit disturbing."
        off "Perhaps I'm imagining it."
        sf "Ok then... I'm ready to go..."
        sis "I'm sorry, I overslept..."
        sis "Give me a minute and I'll be right out."
        sf "Sure, I'll wait downstairs."
        sis "No need, I've told you that I just need to dress, just give me a minute."
        sf "Ok. So... you know, I was thinking about that dress you showed me yesterday."
        sis "Yeah? The purple one?"
        sf "You like purple."
        sis "Yes, I do. What about the dress?"
        sf "Well, it would be perfect with these shoes I've found on the web this morning, I have to show you...."
        off "Girls talk."
        off "[sis_name] quickly gets dressed and they leave the room talking about shoes."
        off "I wait a full minute before getting out of the closet and carefully head for my room."
        off "I can't believe [sf_name] didn't find out."
        off "Or maybe she found out but was tactful enough not to say a word about it."
        off "We'll have to be more cautious."
        off "You're not just fooling around, [mc_name]."
        off "You're having a relationship with [sis_name]."
        off "If anyone knows about that, you're both finished."
        jump ep5sc5


label ep5sc2:
    scene black with dissolve
    with Pause(2)
    scene ep5_sc2_k_01 with dissolve
    off "I mechanically head to the kitchen while my thoughts are still focused on what is happening upstairs."
    off "There's nothing I can do."
    off "I'm not going to break the door open and force her to listen to us."
    off "And [sis_name] doesn't want me around right now."
    off "Maybe she thinks that her chances of talking to [sf_name] are better if I'm not around."
    off "That would make sense."
    off "How could we have been so careless?"
    off "Sleeping together was nice but stupid."
    off "How could we assume that we wouldn't get caught?"
    off "If [sf_name] hadn't found us today, Mom or Dad would have uncovered us sooner or later."

    if ep4sflovetalked == True:
        off "It's so ironic."
        off "That was supposed to be our last kiss."
        off "Fate is a bitch."
    scene ep5_sc2_k_02
    off "There's no way [sf_name] forgives us."
    off "If we're lucky she'll keep it a secret."
    off "Friendship however is probably out of question."
    off "I don't know what [sis_name] will become if [sf_name] doesn't forgive her."
    off "She'll collapse."
    off "I'm sure of it."
    off "What am I doing here?"
    off "I'm not hungry or thirsty."
    off "Should I cook something for [sis_name]?"
    off "Probably not, she won't have any appetite, just like me."
    off "And she has other things on her mind right now."
    off "Goddammit, I feel so useless."
    off "Guilty and useless."
    scene ep5_sc2_k_03
    off "And I'm also a coward, as I somehow let [sis_name] face [sf_name] alone while I'm at fault."
    off "If there's anything I can do or say to save their relationship, I should do it."
    off "But what?"
    off "What would I say if I could talk to her?"
    off "Well, I could take the blame."
    off "It's me."
    off "[sis_name] didn't do anything."
    off "Can I say that I forced her?"
    off "I'm pretty sure that the show we put on this morning didn't look like I was the one controlling the situation."
    scene ep5_sc2_lr_01
    if ep3sfshoptalk == True:
        off "But [sf_name] warned me about [sis_name]'s confused feelings."
        off "I can tell her I abused it deliberately."
        off "[sis_name]'s a victim."
        off "Yeah, that could work."
        off "That would make me a total asshole... And it's not so far from the truth."
        off "She warned me."
        off "I knew [sis_name] was confused."
        off "I didn't reject her."
        off "I encouraged her."
        off "Somehow, yes... I abused her vulnerability."
        off "The fact that I love her doesn't make it any less horrible."

    off "I can beg."
    off "For her forgiveness."
    off "Not for me of course, but for [sis_name], that may work."
    off "If she loves her as much as I think, it may work."
    off "On the other hand, if I'm the problem and the culprit, she may very well refuse to hear a single word from me."
    off "Furthermore, anything I could say would sound meaningless if [sis_name] and I keep our relationship going afterward."
    off "It would be like there are no consequences to our actions."

    if ep4sflovetalked == True:
        off "I've thought about it as a provocation to [sis_name] about her decision of parting ways with me but..."
        off "... Choosing neither [sis_name] nor [sf_name] may be the only way to salvage something from this mess."
    scene ep5_sc2_lr_02
    off "So... that's it."
    off "If I have any occasion to talk to her, I'll beg her to forgive [sis_name]."
    off "I'll tell her that I'm an abusive asshole."
    off "I'll swear to keep my distance with both of them..."
    off "That sounds so weird."
    off "Even I wouldn't agree or even imagine forgiving."
    off "She'll think I'm just a liar."
    off "I betrayed her after all."
    off "I promised her I wouldn't play her and..."
    off "I'm an imbecile."
    scene ep5_sc2_lr_03
    off "The weathercast is announcing scorching heat until the end of the week."
    off "There should be a storm this weekend."
    off "I don't really care."
    off "I don't even know why I'm watching this."
    off "What time is it?"
    off "I should go see if [sis_name] needs anything."
    off "I feel like it's been hours since I've got downstairs."
    off "Shit, it's been only thirty minutes."
    off "This day is going to be very long."

    scene black with dissolve
    with Pause(2)
    show text "Thirty minutes later."
    with Pause(2)

    scene ep5_sc2_lr_04 with dissolve
    off "Still no signs of movement upstairs."
    off "I should go check on [sis_name]."
    off "I gave her some space but enough is enough."
    off "If [sf_name] hasn't opened her door yet, [sis_name] is probably still there, laying on the floor."
    off "I'm about to leave the living room when my phone's ringtone fills up the air."
    scene ep5_sc2_lr_05
    off "It's Mom."
    off "She's going to ask if everything's alright."
    off "What am I going to tell her?"
    off "Ok, calm down [mc_name]."
    off "You can manage."
    scene ep5_sc2_lr_06
    mc "Hi, Mom."
    mom "Hello, [mc_name]. I hope I'm not waking you up."
    off "If only..."
    mc "No, you didn't wake me up."
    mc "I'm actually in the living room, watching TV."
    mom "I tried to call on [sis_name]'s phone but she didn't pick up."
    mom "Is everything alright?"
    off "Here we go."
    off "Obviously, I can't let you know what's happening here."
    off "First lie."
    mc "She's in the shower right now."
    mc "That's probably why."
    mc "Everything is going fine here."
    mom "Really?"
    mom "Are you telling me that [sis_name] and yourself suddenly became responsible adults and stopped fighting for any reason?"
    off "We could put it like that..."
    mc "Come on Mom, we're not fighting that much."
    mc "We're actually getting along fairly well at the moment."
    scene ep5_sc2_lr_07
    if ep4sflovetalked == False:
        off "We're getting along so well that I almost slide my dick into her this morning."
        off "And she was happy with it."

    mom "That's a welcome development."
    mom "Maybe entrusting the house to the both of you was a good idea after all."
    mom "Your father keeps saying that you're probably about to kill each other before setting fire to the house."
    off "A welcome development."
    off "That's a good joke."
    mc "... I'm... glad to know that you trust us so much..."
    mom "What do you do with your days?"
    mom "Did [sis_name] start studying ?"
    off "Shit."
    off "A few days ago I would have gladly sold her but now... The second lie then."
    mc "She opened her books yes... [sf_name] is helping her."
    mc "And we're not doing anything extravagant I guess..."
    mc "You know... Chatting by the pool, watching movies at night..."
    mom "[sf_name]'s a really nice girl."
    mom "I hope you know how to behave and don't bother her too much."
    off "I didn't bother her."
    off "I betrayed her."
    off "I'm a fucking asshole."
    off "Third lie."
    mc "Mom, I'm a gentleman."
    mom "Absolutely."
    mom "A young eighteen-year-old gentleman, overflowing with hormones and fantasy."
    mom "I know how boys are, Honey."
    mom "And I was eighteen years old once too."
    off "She's mocking me."
    off "I don't like it, I'm not in the mood for that."
    scene ep5_sc2_lr_08
    mc "Mom, please."
    mom "Anyway, the airline has postponed our return flight."
    mom "As there may be a storm on Saturday, we won't be there until Sunday morning at best."
    mom "Will it be alright?"
    mc "Mom. We're adults. We'll manage, don't worry."
    mom "I'm sure you will."
    mom "Just stay at home and everything will be alright."
    mom "I don't want you to be outside, wandering the streets with that kind of weather."
    mc "Don't worry. We're not going out anyway."
    off "Not with the two psycho brothers lurking outside."
    mom "You don't, but [sis_name] may want to..."
    off "Of course."
    off "I'm just waiting for you to come back from your trip but we really need to talk about that."
    mc "She knows she's grounded at home."
    mc "She's not going out."
    mom "I never thought she would obey that."
    mom "Wait... Are you... covering for her?"
    off "Shit. Am I so bad at lying?"
    mc "What? No! You know I wouldn't."
    mom "I would normally know, yes, but something feels a bit weird."
    mom "We're leaving the town for a week and you two suddenly start getting along well..."
    mom "And you're even telling me that [sis_name] stays home and studies?"
    mom "It sounds too good to be true."
    mom "Are you hiding something from me, [mc_name]?"
    scene ep5_sc2_lr_09
    off "She sees right through my lies."
    off "She knows things aren't going so well."
    off "I knew it."
    off "I can't lie to her."
    off "Maybe I should tell her the truth?"
    off "Not everything of course... But the psycho brothers thing..."
    off "Calm down, [mc_name]."
    off "If you tell her anything now, with what's going on with [sf_name] and [sis_name], you will only worsen the situation."
    off "Mom isn't some kind of lie detector."
    off "She has a feeling, feelings can be wrong."
    off "Just tell her everything is alright and it's gonna be fine."
    mc "No Mom, I'm not hiding anything. We're fine."
    off "There's a few seconds of silence."
    off "Just enough to signify that she's now sure there's something wrong."
    mom "Listen, [mc_name], it may sound weird but... If you're covering for her, I'm proud of you."
    mom "It's new, but it's what a brother should do, and I like that."
    mom "However, if it's anything serious, you know you can and should tell me."
    mom "I trust you and [sis_name]."
    mom "You can call me anytime."
    off "Ok, what does that mean?"
    off "She knows but she trusts us to handle the situation?"
    off "Something like that?"
    mc "I know mom."
    mom "We love you, [mc_name]. Will you kiss [sis_name] for us ?"
    mc "Of course Mom."
    mom "I'll call you back soon."
    mc "Goodbye, mom."
    off "She hangs up."
    scene ep5_sc2_lr_10
    off "That conversation was disturbing."
    off "Lying to Mom aside, the fact that she trusts us while we're actually swimming in deep shit is very unpleasant."
    off "I can only disappoint her and I know it."
    off "I feel ashamed."
    off "I'd better go see [sis_name] and let her know."
    off "I'm not sure she'll give a fuck but at least she'll know."

    scene black with dissolve
    with Pause(2)
    off "I climb the stairs and join [sis_name] in the hallway."
    scene ep5_sc2_c_01 with dissolve
    off "She has barely moved."
    off "At least, she's fully clothed now."
    off "She doesn't react to my presence."
    off "She looks like she's in shock."
    off "I shouldn't have left her alone."
    off "What a moron."
    off "I tell her I want to protect her, to be there for her and I leave her alone when she needs me the most."
    off "She may have asked for it, but I could have refused."
    off "I sit next to her."
    off "I want to hug and comfort her but I'm not sure she would really enjoy my physical contact now, as I'm a huge part of the problem she has to deal with."
    scene ep5_sc2_c_02
    off "I clumsily grab her hand."
    off "No reaction."
    off "Immobile, her gaze empty and fixed, she seems absent and exhausted by the emotions that overwhelm her."
    off "She probably ran out of tears."
    mc "Hey, Princess."
    off "I gently caress the back of her hand."
    sis "She didn't open."
    off "She speaks without looking at me."
    mc "I know."
    sis "She didn't say a word."
    mc "It's ok, we just have to be patient."
    mc "She needs time."
    mc "She will talk to you soon."
    off "She doesn't reply."
    mc "You're not hungry? Or thirsty?"
    mc "I can bring you something..."
    off "She nods negatively."
    scene ep5_sc2_c_03
    mc "Ok... I couldn't eat anything either..."
    mc "Mom called me."
    mc "She tried to call you but you didn't pick up."
    mc "I've told her you were in the shower."
    mc "She knows something is wrong."
    mc "I've told her everything was alright but I'm afraid she has seen through my lies."
    mc "And... Well, strangely enough... She trusts us..."
    sis "She trusts you."
    mc "No, she trusts us."
    mc "She trusts us to handle any situation but if it's something serious, we should tell her immediately."
    mc "That's more or less what she said."
    sis "And it's something serious."
    scene ep5_sc2_c_04
    mc "You know it is."
    sis "Then tell her."
    sis "I don't care anymore."
    off "She wouldn't care about anything."
    off "[sf_name] is the only thing that matters right now."
    mc "If you say so. We'll call her together later."
    sis "Ok."
    scene ep5_sc2_c_05
    off "I'm not even sure she realizes what we're talking about."
    off "Her voice is barely more than a whisper."
    mc "Princess, you seem like you're about to collapse."
    mc "You should get some rest."
    mc "I'll stay there in your stead and I'll come to get you if [sf_name] opens her door. Ok ?"
    sis "No."
    mc "Come on."
    mc "Do you want me to carry you to your room ?"
    sis "No. I want to stay here."
    mc "Princess, you're frightening me."
    sis "I'll stay here."
    mc "You're as stubborn as ever."
    mc "I'll stay with you then."
    sis "[mc_name], I told you I want you to leave us alone."
    mc "And I don't want to."
    mc "I can't leave you knowing that you're in pain."
    sis "I... I don't want her to see us together."
    mc "I understand."
    mc "But I won't leave you alone."
    mc "I'm staying here."
    mc "We won't kiss, we won't cuddle or anything like this."
    sis "[mc_name]. Please."
    scene ep5_sc2_c_06
    mc "I can't stand seeing you like this."
    mc "You can't ask me to watch you endure this alone."
    mc "Don't even think about it."
    mc "I'm done closing my eyes on your suffering."
    mc "At least I can be there as your brother."
    mc "I agree it's conflictual, but my place is right there. Don't deny me this."
    scene ep5_sc2_c_07
    sis "I just don't want her to think that we're doing things right in front of her door..."
    mc "We're not doing anything."
    mc "We're just waiting for her."
    mc "I'll keep my distance, but I'll stay here and I'll wait along with you."
    mc "It's not negotiable."
    mc "Also, I'm guilty and responsible."
    mc "Not being there would be like refusing to assume what I've done."
    mc "I don't see myself as a coward."
    off "She doesn't even look at me."
    sis "Ok..."
    off "Her voice sounds defeated."
    off "It was easier than I thought."
    off "I should have done it sooner."

    scene black with dissolve
    with Pause (2)
    scene ep5_sc2_c_08 with dissolve

    off "We've been waiting together for I don't know how long."
    off "I don't even try to keep track of time."
    off "We don't talk, we barely move."
    off "We're not touching each other, but I feel like deeply, we are together in this."
    off "I hope [sis_name] feels like that too."
    scene ep5_sc2_c_09
    off "The door suddenly opens."
    off "The room is dark."
    off "[sf_name] probably kept the blinds shut."
    scene ep5_sc2_c_10
    off "She emerges from the gloom and [sis_name] and I look up to her."
    off "She's angry and sad."
    off "It's obvious that she's going through just as much pain as [sis_name]."
    off "She's hurt."
    off "I search for something to say but my mind is as empty as my resolve."
    off "I'm afraid to face her."
    off "I don't know what to say anymore."
    off "Come on [mc_name]."
    off "Think."
    off "Find something."
    off "No one moves an inch."
    off "[sis_name] and I wait."
    off "[sf_name] looks at us for a few seconds before talking."
    scene ep5_sc2_c_11
    sf "[sis_name]. Come in, please."
    off "[sis_name] slowly rises up."
    off "She has been sitting on her legs for hours."
    off "She has trouble standing up."
    off "I briefly think about helping her but she wouldn't like me to be that considerate in front of [sf_name]."
    scene ep5_sc2_c_12
    off "She enters the master bedroom and [sf_name] closes the door behind her, without a look for me."
    off "It hurts."
    jump ep5sc3


label ep5sc3:
    scene black with dissolve
    with Pause(2)
    scene ep5_sc3_c_01
    off "I don't know why I stayed there, sitting on the floor."
    off "I've essentially taken [sis_name]'s place in waiting for the girls to come out."
    off "I could have waited in my room but it felt more fitting to just stay here."
    off "I know it's stupid."
    off "What am I waiting for?"
    off "For [sis_name] to come out?"
    off "For me to have a chance to explain myself?"
    off "What is there to explain again?"
    off "Earlier this morning I'd prepared a speech but it now seems ridiculous."
    off "It's been almost two hours since [sis_name] entered that room."
    off "There hasn't been any yelling."
    off "I don't think they've been fighting either."
    off "Everything is quiet."
    off "It's so strange and sad."
    off "I think about lying on the ground in the foetal position."
    off "That would be a way to say that I'm sorry."
    scene ep5_sc3_c_02
    off "Come on, [mc_name]."
    off "Let's keep some dignity."
    off "You're a man, not a worm."
    off "Sitting on the floor is humiliating enough."
    off "Humiliating?"
    off "I don't give a fuck about humiliation right now."
    off "Honestly, if it can bring me her forgiveness, I'm ready to do anything, as long as it doesn't hurt [sis_name]."
    off "I'll kiss her feet."
    off "I'll crawl before her."
    off "If she wants to walk on me, I'm okay with it."
    off "I deserve it, and if it can bring some peace, it's a very small price to pay."
    off "But I'm sure it won't come to this."
    off "[sf_name] is a good girl."
    off "We'll talk like adults and I'll apologize."
    off "Of course, nothing will be like before but I'm sure we can save her friendship with [sis_name]."
    off "[mc_name]. You are a moron."
    off "Everything has gone to shit already."
    off "It's beyond repair."
    scene ep5_sc3_c_03
    off "Persuading her to keep your relationship with [sis_name] a secret would already be an achievement."
    off "Focus on that."
    off "If she refuses, your life will become miserable."
    off "You can already think about running away from this town, from this country and even from this life."
    off "Would [sis_name] agree to that?"
    off "We could start over somewhere no one knows us and live like a married couple..."
    off "It could be great..."
    off "I don't know how [sis_name] would stand her separation from [sf_name], however."
    off "She's somehow dependent on her."
    off "She doesn't imagine living without her."
    off "Her reaction this morning wasn't very promising."
    off "She'll get used to it."
    off "It's not like she has a choice."
    off "If [sf_name] wants to end their friendship, there's nothing she can do."
    off "The door slowly opens."
    scene ep5_sc3_c_04
    off "[sis_name] exits the room as I stand up."
    off "She looks away and immediately turns her back to me."
    off "She avoids me."
    sis "She wants to talk to you."
    off "Ok. It's my turn."
    off "I can feel my guts liquefying."
    off "She's waiting for me."
    mc "What did she say?"
    off "[sis_name] doesn't reply."
    sf "Come in [mc_name]."
    off "Her voice is cold as ice."
    scene ep5_sc3_mbr_01
    off "I step into the room and close the door behind me."
    off "The blinds are lowered, there's not much light entering."
    off "It takes my eyes a few seconds to accommodate to the semi-darkness."
    off "She stands on the other side of the bed."
    off "She doesn't say a word."
    off "She doesn't even face me."
    off "Should I talk?"
    off "I feel like I shouldn't."
    mc "[sf_name], I..."
    scene ep5_sc3_mbr_02
    sf "I asked you if you intended to play me."
    mc "... I'm..."
    sf "You told me you weren't that kind of guy."
    sf "Do you remember?"
    mc "I do."
    sf "You lied to me."
    sf "You cheated on me."
    sf "You betrayed me."
    mc "I'm sorry, I didn't intend to hurt you."
    sf "Really? So tell me, [mc_name], what did you intend to do?"
    sf "And don't bother lying."
    sf "[sis_name] already told me everything."
    off "Her voice is steady and clear."
    off "Unwavering, precise."
    off "Full of authority and confidence."
    off "She's like a solid, unshakeable rock that I made the mistake of irritating."
    off "She decides. She judges. She calls the shots."
    off "She makes me feel like I'm nothing."
    scene ep5_sc3_mbr_03

    if ep4sflovetalked == True:
        off "But I know better."
        off "I know this is nothing but a facade."
        off "She showed me the real [sf_name] last night."
        off "Insecure, fragile, isolated, and lonely."
        off "This is a mask she puts on to face the world."
        off "The discussion I had with her last night makes it obvious."
    else:
        off "She wasn't that confident last night while I was licking her pussy."
        off "That was really dumb."
        off "I shouldn't have done that."
        off "She's probably even angrier at me because we fooled around together last night."

    sf "So? I'm listening. Don't you have anything to say ?"

    menu:
        "If [sis_name] has already told you everything...":
            mc "... What more can I say?"
            sf "I don't know."
            sf "You don't want to try explaining yourself?"
            mc "It doesn't matter."
            mc "You've already judged us."
            mc "And even if I tried to explain, you wouldn't understand."
            sf "Understand? What is there to understand?"
            sf "You betrayed me!"
            sf "Look at it however you want, you betrayed me!"
            off "Her reply surprises me a bit."
            mc "No, I mean... Yes, I betrayed you, but... you wouldn't understand... [sis_name] and I..."
            sf "Oh. I wouldn't understand that you fuck [sis_name]?"
            sf "That's what you mean?"
            mc "We didn't fuck!"
            scene ep5_sc3_mbr_06
            sf "Not yet..."
            sf "I don't care that she's your father's ward."
            sf "I won't judge you for that. It's your problem, and yours alone."
            sf "But she's also my best and only friend."
            sf "You cheated on me with my best and only friend."
            sf "Had you wanted to hurt me you couldn't have chosen a better partner."
            off "She doesn't care that [sis_name] is my father's ward?"
            mc "Does that mean that... You would agree to keep it a secret?"
            off "She looks at me with disgust."
            sf "Because you thought that I would go around telling people about you and her?"
            sf "Who do you think I am?"
            sf "Unlike you, I am trustworthy, and I would never do anything that could hurt her."
            sf "If you think otherwise, you clearly didn't deserve my affection."
            scene ep5_sc3_mbr_07
            mc "Indeed. Listen, [sf_name]."
            mc "I'm sorry."
            mc "That's just how it is."
            mc "I know that I fucked up."
            mc "I know that there's nothing I can do or say that will make you feel better and I'm genuinely sorry that I hurt you."
            mc "We can't repair the relationship the three of us had."
            mc "There's just nothing we can do about it."
            mc "It's lost."
            mc "We didn't have a choice."
            mc "It's fate."
            mc "I wanted to tell you earlier, but I couldn't."
            mc "I'm not sure it would have eased things out, though."
            mc "You may not believe it but I honestly love you."
            mc "I love you both, just in a different way."
            mc "I discovered it too late and had to make a choice."
            mc "I'm sorry it turned out that way."
            mc "I apologize."
            sf "Fate."
            sf "How convenient."
            sf "You're not even responsible."
            scene ep5_sc3_mbr_10
            sf "Get out."
            mc "[sf_name]..."
            sf "GET OUT."
            off "The discussion is over."
            off "I'm not sure she liked my explanation."
            off "Our secret is safe, however, and she didn't sound like she will hold a grudge against [sis_name] for too long."
            off "So... I guess that's for the better."
            sf "I don't want to see you ever again."
            sf "You are an asshole and an imbecile."
            sf "But just to be clear."
            sf "If you ever hurt [sis_name] in any way, you'll regret it."
            sf "Do you understand?"
            mc "I do."
            off "As I thought. Her friendship with [sis_name] is somehow safe."
        "Everything is my fault.":

            mc "[sis_name] didn't do anything."
            mc "I forced her."
            sf "Are you telling me that you're raping her?"
            sf "It didn't look like that."
            mc "No... I mean, I seduced her. And..."
            sf "I understand, you are irresistible, she can't refuse you."
            off "She's mocking me."
            off "Come on [mc_name], this isn't the time to look like an idiot."

            scene ep5_sc3_mbr_06

            if ep3sfshoptalk == True:
                mc "That's not what I mean, and you know it."
                mc "You've told me that she was confused about me."
                mc "I just... took advantage of it."


            sf "So you are a scumbag who tricks his mentally unstable and insecure friend into having sex with him?"
            mc "I... that's... One way of seeing it."
            sf "Is there another way of seeing it?"
            mc "I love her."
            sf "You love her, so you coerce her into having a relationship with you."
            sf "That makes sense."
            sf "It's still rape."
            sf "Why shouldn't I report you to the police?"
            off "The way she talks to me makes it pretty obvious that she's not buying my crap."
            off "She plays along just for the sake of having me look like an idiot."
            off "I can't say I don't deserve it."
            off "I don't know what I expected."
            off "[sis_name] has already told her everything."
            off "My ridiculous tale didn't stand a chance."
            scene ep5_sc3_mbr_07
            mc "Alright, [sf_name]."
            mc "I'm sorry."
            mc "What do you want to hear?"
            mc "We fucked up. We're sorry."
            mc "Will you believe me if I tell you that we didn't intend to hurt you?"
            mc "We wanted to tell you but were afraid of the consequences."
            mc "I don't know how to explain it."
            mc "There's something irresistible that drags me to her."
            mc "I just don't have a choice."
            mc "I'm sorry."
            mc "It's just... Fate."
            sf "Fate."
            sf "How convenient."
            sf "You're not even responsible."
            scene ep5_sc3_mbr_10
            sf "Get out."
            mc "[sf_name]..."
            sf "GET OUT."
            off "The discussion is over."
            off "I'm not sure she liked my explanation."
            sf "I don't want to see you ever again."
            sf "You are an asshole and an imbecile."
            sf "But just to be clear."
            sf "If you ever hurt [sis_name] in any way, you'll regret it."
            sf "Do you understand?"
            mc "I do."
            off "At least she still cares about [sis_name]."

        "I'll tell you everything. [sfSisPath]" if ep3sfshoptalk == True:
            mc "But I'm not sure it'll make a difference."
            sf "I don't think that you have anything left to lose."
            off "I take a deep breath."
            off "This isn't the speech I thought I'll give her."
            off "I have no idea where I'm going with that."
            mc "So..."
            mc "I'm sure you remember our discussion at the lingerie shop."
            mc "About [sis_name] being confused."
            scene ep5_sc3_mbr_04
            sf "Of course I do."
            mc "The truth is... I was already confused myself."
            mc "I don't know where it comes from, but just like her, I was already seeing her as... Both a friend and a girl I was... Already falling for..."
            mc "I wanted to protect her, I wanted to take her in my arms, I wanted to take care of her."
            mc "Maybe it was guilt that triggered it, I don't know, but it was already there."
            off "[sf_name] looks at me in silence."
            off "I briefly try to make eye contact but I immediately regret it."
            off "Her anger shames me."
            off "I've hurt her so much..."
            mc "But she's my father's ward, and at that point, I thought that it was impossible, that it was wrong, that I was a fool."
            mc "So I choose to be reasonable and not to pursue her."
            mc "That night in the living room, I didn't lie to you."
            mc "I didn't intend to cheat on you or anything like that."
            mc "I wanted to be with you because I liked you."
            mc "It's true."
            mc "When you left the room, you were my girlfriend and you were the only one."
            mc "And then... [sis_name] came to my room."
            mc "We talked."
            mc "She seemed vulnerable and confused."
            mc "And I don't know... It happened."
            mc "Suddenly, I was still a fool but things were possible and I didn't give a damn about what was right or wrong."
            mc "I was in love with her."
            mc "To be honest, I didn't even think about you at this time."
            mc "[sis_name] completely wiped my mind blank."
            mc "There was her, me, and nothing else."
            mc "I'm sorry if that sounds harsh."
            mc "It's just so you understand that there hasn't been a moment when I thought that it was ok to cheat on you."
            mc "So... We talked, kissed, cuddled, and slept to the morning."
            mc "It was only then that I realized what I had done."
            mc "Believe it or not but I was mortified."
            mc "[sis_name] and I talked about it."
            mc "We wanted to tell you but... We were afraid of your reaction."
            mc "Afraid that you would judge us, afraid that [sis_name] would lose your friendship."
            mc "She was... She is completely terrified of losing your friendship."
            mc "We didn't know how to tell you and surely didn't want to hurt you."
            mc "We didn't want to cheat on you."
            mc "We didn't laugh behind your back."
            mc "Being together was painful because we knew it would hurt you."
            mc "So we've spent the whole day searching for a perfect way to tell you."
            mc "You can guess we didn't find it."
            mc "Ironically enough, that night... [sis_name] decided that there was no way for us to be together without hurting you."
            mc "So we just slept together one more time and we were saying goodbye when you surprised us."
            mc "We were supposed to go back to being just like brother and sister and me to be your boyfriend."
            scene ep5_sc3_mbr_05
            sf "Because you wouldn't have any problems to act as if nothing happened?"
            sf "You would have lied to me?"
            mc "It's... not that simple... I..."
            sf "You what ?"
            mc "On Monday night I told you that I liked you."
            mc "And it was true. I liked you."
            mc "Tuesday morning, after my first night with [sis_name], I had no doubt that I was in love with her."
            mc "A strong and true love."
            mc "I had to be with her, and I had to break up with you."
            mc "It was... Clear and simple."
            mc "But then... You smiled."
            mc "You showed me a different [sf_name]."
            mc "It was obvious that you were willing to give me everything you had to offer."
            mc "You were offering me your unconditional love and it... melted my heart."
            mc "I know it stupid but you made me fall in love with you."
            mc "I didn't want to acknowledge it until later tonight but I love you."
            mc "I didn't tell [sis_name]."
            mc "But she was aware of it."
            mc "She knew that I wouldn't have to force myself to love you... because I was already in love."
            scene ep5_sc3_mbr_06
            sf "So what? You love both of us?"
            mc "I know. You don't have to believe me."
            mc "It's just how it is."
            mc "I feel like... You are like the two faces of a coin."
            mc "I love you both."
            mc "Differently, but both."
            mc "I don't know how it is possible, it just is."
            sf "Oh. Poor [mc_name]."
            sf "So you're having a dilemma, Aren't you?"
            sf "What are you going to do now?"
            sf "Are you going to choose?"
            sf "Or maybe do you think this will end in a nice little harem, with both of us girls lusting for a threesome?"
            mc "What? No! Of course not!"
            mc "I never intended to pursue both of you."
            mc "It just happened..."
            sf "So you're a victim of the circumstances."
            sf "That's so sad."
            sf "However, I asked you a question."
            sf "I would appreciate an answer."
            sf "If I asked you to make a choice, who would you choose?"
            scene ep5_sc3_mbr_07
            off "What?"
            off "She's offering me a choice?"
            off "What does that mean?"
            off "What will happen then?"
            off "If I chose her, will she be my girlfriend like nothing happened?"
            off "If I choose [sis_name]..."
            off "Stop dreaming [mc_name]."
            off "There is no way [sf_name]'s still interested in you."
            off "You betrayed her."
            off "Everything is over."
            off "You can't guess what she has in mind."
            off "Don't expect any kind of happy end."

            menu:
                "I would choose you.":
                    mc "I have no doubt about that."
                    mc "It's the only reasonable choice."
                    off "Her expression changes a bit."
                    off "Is that disgust?"
                    off "She turns away from me."
                    sf "You are a liar."
                    sf "And a coward."
                    sf "I don't understand how I could have been attracted to you."
                    sf "I'd given you my heart, I've let you touch me!"
                    sf "You're like every other guy out there."
                    sf "You didn't care about me, not even for a second."
                    sf "I should have known."
                    sf "How could I be so stupid?"
                    sf "You just wanted to put your dick inside something."
                    sf "That being me or [sis_name]."
                    sf "You disgust me."
                    scene ep5_sc3_mbr_10
                    sf "Get out."
                    off "Her voice progressively fills up with a mix of sadness and anger as she says that."
                    mc "[sf_name], I..."
                    sf "I don't care."
                    sf "Get out!"
                    off "She's still yelling at me as I walk out."
                    sf "I don't want to see you ever again."
                    sf "You are an asshole and an imbecile."
                    sf "But just to be clear."
                    sf "If you ever hurt [sis_name] in any way, you'll regret it."
                    sf "Do you understand?"
                    off "Yes, I do."
                    off "At least you still care about her a bit."
                "I would choose [sis_name].":

                    mc "I'm sorry [sf_name]."
                    mc "It's... Even if I love you both..."
                    mc "I don't know how to put it, I'm sorry."
                    mc "I can't explain it."
                    sf "You love her more than you love me."
                    mc "No, I don't think it's like that."
                    mc "Just as she will choose you over me, I will choose her over you."
                    mc "I don't know how to explain it."
                    mc "These are different feelings."
                    sf "Love is love."
                    mc "Yes but... You can love for different reasons."
                    mc "I love you both because you are different."
                    mc "I don't know why I would choose her over you, but I'm sure I would."
                    off "She keeps silent for a few seconds before turning away from me."
                    scene ep5_sc3_mbr_05
                    sf "At least you're being honest this time."
                    sf "Thank you for your answer, [mc_name]."
                    sf "You can get out."
                    off "Her voice sounds sad."
                    off "I feel like I should say something more but I don't know what."
                    off "I leave the room quietly."

                "I would choose no-one. [sfSisPath]" if ep4nightchoosenone == True or ep4choosenone == True: # Possible 3some
                    mc "I thought about it a lot since Monday morning."
                    mc "If I'm with [sis_name], we're hurting you."
                    mc "If I'm with you, we're hurting [sis_name]."
                    mc "I don't want to hurt either of you."
                    mc "The only way it doesn't end badly is to not choose anyone."
                    scene ep5_sc3_mbr_07
                    sf "That doesn't make any sense."
                    sf "You don't want to hurt either of us but you would most probably end hurting both of us."
                    mc "I know. But that way you can still support each other."
                    mc "And I'm certain that [sis_name] needs you more than she needs me and you're no different."
                    mc "You need her more than you need me."
                    mc "Your relationship with her is beyond friendship."
                    mc "And it's the most precious thing you have."
                    mc "I understood that too late."
                    mc "The link between the two of you is almost vital."
                    mc "I'm sorry I endangered it."
                    mc "I apologize for that."
                    mc "I shouldn't have meddled with either you or her."
                    mc "We should have stayed friends and no more."
                    mc "If there's anything we can salvage from this mess, it has to be your relationship with her."
                    scene ep5_sc3_mbr_08
                    sf "Because you think it's still salvageable?"
                    sf "You betrayed me."
                    sf "Both of you."
                    sf "How can we save anything from that?"

                    menu:
                        "Apologize. [sfSisPath]":
                            $ ep5sfapologized = True
                            mc "We are sorry."
                            mc "I don't know how to put it differently."
                            mc "We messed up."
                            mc "We know that."
                            mc "But we didn't do it to hurt you."
                            mc "Actually, we messed up so much because we feared we'd hurt you."
                            mc "I know it sounds stupid, but that's how it is."
                            mc "I also know that what I ask from you is unthinkable but I'm doing it anyway."
                            mc "Forgive us."
                            mc "Please. Give us one more chance."
                            mc "We'll go back to being friends."
                            mc "Of course, it'll be awkward at first but we can try."
                            mc "We can act as if nothing happened."
                            mc "We'll just be friends and everything will be fine."
                            mc "What do you think [sf_name]?"
                            mc "I know I don't deserve it."
                            mc "But if we want to get out of this without every one of us getting hurt beyond repair... It's the only way."
                            scene ep5_sc3_mbr_09
                            sf "Did you seriously think I would consider that?"
                            mc "I had to try."
                            mc "You're angry right now."
                            mc "Rightfully angry."
                            mc "But I know that you don't want to hurt [sis_name]."
                            mc "And you know that she needs you, more than anything else."
                            off "She stays silents for a few seconds before turning away from me."
                            scene ep5_sc3_mbr_05
                            sf "Thank you for your answer, [mc_name]."
                            sf "You can get out."
                            off "Her voice sounds sad."
                            off "I feel like I should say something more but I don't know what."
                            off "I leave the room quietly."
                        "Beg her to forgive [sis_name].":


                            mc "[sf_name]... Let me take the blame."
                            mc "Without you, without her."
                            mc "It sounds equitable."
                            mc "I can take it."
                            mc "But [sis_name]... If she loses you... She just won't stand it."
                            mc "I know it. And you know it too."
                            mc "We messed up."
                            mc "We're sorry."
                            mc "I know it's not enough."
                            mc "So I'm begging you."
                            mc "Blame it on me, punish me as much as you want but forgive [sis_name]."
                            mc "She needs you."
                            mc "I promise you I'll never be more than a friend to her and I won't annoy you ever again."
                            mc "I can get on my knees if you want me to."
                            mc "Please, [sf_name]."
                            scene ep5_sc3_mbr_09
                            sf "What are you doing?"
                            off "She looks sad, angered, annoyed."
                            off "Maybe I'm going too far?"
                            off "I'm not sure I care anymore."
                            off "I've already lost everything."
                            mc "I'll do whatever you want me to, please. Forgive her."
                            scene ep5_sc3_mbr_05
                            off "She turns away from me."
                            sf "Morron. You don't know what you're doing."
                            off "She sounds irritated."
                            off "I feel hopeless and miserable."
                            off "I've played all my cards."
                            off "There's nothing else I can say."
                            off "She sighs."
                            sf "You can get out, [mc_name]."
                            off "Her voice sounds sad."
                            off "I feel like I should say something more but I don't know what."
                            off "I leave the room quietly."

    scene ep5_sc3_c_05
    off "Just as before, [sis_name] is there, seated on the ground."
    off "She stands up and looks at me."
    off "She doesn't have to say the words, I can read the question on her expression."
    mc "I don't know."
    mc "It's... You know her better than I do."
    mc "You know she's unreadable."
    mc "I've said a lot of things... I don't know if it had any effect on her."
    mc "I think she despises me."
    mc "She won't hold a grudge against you for long though..."
    off "[sf_name]'s voice interrupts me."
    sf "[sis_name], come back in, please."
    off "She rushes in and closes the door behind her."
    scene ep5_sc3_c_06
    off "I'm left alone with a strange and bitter aftertaste."
    off "Everything is falling apart and there's nothing I can do."

    jump ep5sc4


label ep5sc4:
    scene black with dissolve
    with Pause(2)
    scene ep5_sc4_mcr_01 with dissolve
    off "They've been talking behind this door for hours now."
    off "Well, they probably have a lot to talk about but still."
    off "I'm worried."
    off "My conversation with [sf_name] gave me the impression that she won't remove [sis_name] from her life."
    off "She'll do it for [sis_name] as well as for herself."
    off "At least, that's what I think."
    off "How could we fuck up so much?"
    off "We were careless."
    off "I'm so sorry it turned out like that, [sf_name]."
    off "I feel so bad."
    off "What are they doing?"
    off "No noise filters through that door."
    off "They're not fighting, they're not yelling at each other."
    off "That means that this is not a dispute but a quiet conversation."
    off "[sf_name] is going to leave."
    off "I can feel it."
    scene ep5_sc4_mcr_02
    off "There's no way she stays with us after what we've done."
    off "She'll forgive [sis_name] but it'll take some time."
    off "And she won't want to see my face ever again."
    off "She's going to leave."
    off "What are we going to do?"
    off "I'm not even sure I still have a relationship with [sis_name]."
    off "God damn."
    off "Right from the start, we knew it would end badly."
    off "Why did we do it anyway?"
    off "We? There's no we, [mc_name]."
    off "Face it."
    off "You're the one who's responsible."
    off "Sure [sis_name] approached you but you could have rejected her anytime."
    off "You were [sf_name]'s boyfriend."
    off "I'm despicable."
    off "I'm pitiful."
    off "She trusted me."
    off "Fuck, I was even her first boyfriend, and I betrayed her immediately."

    if ep5sfapologized == True and sis_affection > 70 and sf_affection > 70:
        off "I can hear [sf_name]'s door opening."
        scene ep5_sc4_mcr_03
        off "I slowly raise up as the faint voice of [sis_name] comes to me."
        sis "[mc_name]?"
        mc "I'm here."
        sis "Can you come in, please?"
        mc "I'm coming."
        off "Does she want to talk to me again?"
        off "I thought she would never want to see me again."
        off "I join them in the master bedroom and [sis_name] closes the door behind me before moving to [sf_name]'s side."
        scene ep5_sc4_mbr_01
        off "The mood seems lighter."
        off "The blinds have been opened."
        off "[sf_name] has changed clothes."
        off "She's wearing the comfy outfit she wears at home."
        off "That's strange."
        off "If she was leaving wouldn't she wear something else?"
        off "She doesn't seem angry anymore."
        off "She looks... embarrassed?"
        off "What's going on?"
        off "Did [sis_name] manage to convince her to stay?"
        scene ep5_sc4_mbr_02
        sf "[mc_name], [sis_name] and I talked a lot about what happened."
        sf "We talked about her feelings, about mine, about yours."
        sf "About the circumstances. About... Everything that has come to our mind..."
        scene ep5_sc4_mbr_03
        off "The girls gaze at each other."
        off "[sis_name] then looks away and concentrate on her feet."
        off "I don't understand what's happening but something is going on."
        scene ep5_sc4_mbr_04
        sf "[mc_name], can I ask you a few questions ?"
        mc "Sure..."
        sf "Will you be completely honest?"
        sf "This is very important. For all of us."
        mc "I will. But will you believe me?"
        mc "After all that, you could rightfully doubt me."
        sf "I could, but I will not, at least for the next few minutes."
        mc "You can ask anything you want, and I won't lie."
        off "She nods."
        scene ep5_sc4_mbr_05
        sf "So... How do you feel about [sis_name]?"
        off "How do I feel?"
        off "Does she really want to hear that?"
        off "Is this a trap or something like that?"
        off "I promised to be completely honest."
        off "Let's keep that promise."
        mc "Are you sure you want to hear that?"
        scene ep5_sc4_mbr_06
        sf "I am yes."
        off "So be it."
        mc "I love her."
        sf "Like a sister?"
        mc "And more than that."
        mc "She is like my sister and she's also more than that."
        mc "I don't think that you can describe my love for her with a \"like a sister\" or \"like a women\" statement."
        sf "So you love her."
        sf "And you desire her?"
        scene ep5_sc4_mbr_06
        mc "... I do, yes."
        sf "But she's like a sister to you."
        sf "Doesn't that disturb you?"
        mc "I thought a lot about it... and... It was disturbing, at first."
        mc "But it's not anymore."
        mc "Now, I just feel more and more attracted to her."
        sf "So you're not after her just for sex?"
        mc "No! I'm not!"
        scene ep5_sc4_mbr_07
        mc "I believe sex will come as it happens between two persons who love each other, but it's not my goal."
        sf "A few days ago you hated her."
        sf "And now you love her."
        sf "Isn't that transformation a bit sudden?"
        mc "I never hated her... I would say I was angry but I never hated her."
        mc "And yes, it's sudden. I don't know how to explain it."
        mc "Discovering how wrong I was about her changed a lot of things."
        sf "So you love her. Completely. True love."
        scene ep5_sc4_mbr_08
        mc "Yes."
        sf "Would you give anything, do anything for her ?"
        mc "I think so."
        sf "Would you agree to live a miserable life, without her, if it guaranteed that she would live happily?"
        off "I don't like this question, but the answer is obvious."
        scene ep5_sc4_mbr_09
        mc "I would. Yes."
        off "They stay silent for a moment."
        off "I think [sis_name] is smiling but I wouldn't bet on it."
        off "Her head is still down and it's difficult to see her expression."
        scene ep5_sc4_mbr_10
        sf "And what about me?"
        mc "About you?"
        sf "You understood me, [mc_name]."
        sf "How do you feel about me?"
        off "She wants me to say it in front of [sis_name]."
        off "I don't feel comfortable doing that, but I promised."
        mc "I ... love you."
        scene ep5_sc4_mbr_11
        sf "As I understood it, you really fell in love with me yesterday?"
        mc "Yes."
        off "My head is getting heavier."
        off "I progressively lower it."
        sf "What made you fall for me ?"
        scene ep5_sc4_mbr_12
        mc "I've told you already."
        sf "Please, I want to hear it again."
        mc "Your smile."
        mc "Your trust, the warmth of your feeling."
        mc "You were a different person."
        mc "You showed me the true [sf_name] I guess."
        scene ep5_sc4_mbr_13
        sf "Are you sure you don't just want to have sex with me?"
        sf "You can be honest, I won't be mad. [sis_name] won't be either."
        mc "I am sure. I love you."
        mc "I'm not just lusting after your body."
        sf "How can you be sure it's love ?"
        scene ep5_sc4_mbr_14
        off "How can I be sure?"
        off "This isn't an easy question."
        mc "Because I feel about you... the same way I feel about [sis_name]."
        mc "I don't know how to explain it, it's different, but it's the same."
        mc "Like the two faces of the same coin."
        mc "I know it's stupid."
        mc "But it's just how it is."
        scene ep5_sc4_mbr_15
        sf "You love me the same way you love her."
        sf "However, you chose her. Why ?"
        mc "It's not that simple."
        mc "I... I've chosen her before really acknowledging my love for you."
        mc "Maybe that things would have been different if she had come to me a day later."
        mc "I don't know..."
        off "[sf_name] looks away."
        off "I have a really hard time reading the mood of the room."
        off "I've never been good at that kind of exercise, but it's especially difficult right here and now."
        scene ep5_sc4_mbr_16
        sis "I told you."
        off "[sis_name]'s voice surprises me."
        off "Obviously, she's talking to [sf_name]."
        off "She told her? Told her what?"
        off "[sf_name] doesn't reply."
        off "She seems to be lost in her thoughts."
        off "I don't understand what's going on."
        scene ep5_sc4_mbr_17
        sf "You were right, [mc_name]."
        mc "About what?"
        sf "There's only one way this ends well."
        sf "But it's not your solution."
        off "What is she talking about?"
        scene ep5_sc4_mbr_18
        sf "If you go with [sis_name], I'll be hurt, I'll be jealous, I'll resent you and her."
        sf "If you go with me, she'll be the one to be hurt."
        sf "I think that going with neither of us would hurt everyone and it will surely destroy the friendship and the bond between us."
        off "She looks embarrassed as fuck."
        scene ep5_sc4_mbr_19
        sf "You love both of us and both of us love you."
        sf "And I think that... because [sis_name] and I also... kind of... love each other, we can try to... find another solution."
        off "You love each other?"
        off "Another solution?"
        off "What is she talking about?"
        off "I try to look at [sis_name] but she does everything she can to avoid my eyes."
        off "They're both embarrassed as fuck."
        scene ep5_sc4_mbr_20
        mc "I'm sorry [sf_name], I don't want to risk misunderstanding."
        mc "I'm afraid you'll have to be more explicit."
        mc "What are we talking about?"
        off "She's now in shy mode."
        off "A bit like last night when she welcomed me in her room."
        scene ep5_sc4_mbr_21
        sf "Well... [sis_name] and I talked about it... We... would be ok with it."
        sf "Because it's us."
        sf "I mean, it wouldn't work with anyone else, but if it's with [sis_name]... It can work for me... And... You're ok too, [sis_name], aren't you?"
        sis "Yes... If it's with you, it could work..."
        off "Her voice is barely audible."
        off "My heart is racing in my chest."
        mc "Ok... but what would work?"
        scene ep5_sc4_mbr_22
        sf "We thought we could try to... form a relationship... were the three of us could... participate equally."
        off "The three of us? What the...?"
        off "Wait... Am I understanding this correctly?"
        off "I must be dreaming."
        off "Or maybe it's a trap but there's no way this is real."
        scene ep5_sc4_mbr_23
        mc "Excuse me, I... You mean like... You would both be my girlfriends?"
        sf "I guess you could put it like that."
        off "She talks to me but they prefer to look at each other rather than gazing at me."
        off "They talked about this and decided it together."
        off "That's the result of the hours they just spent enclosed in this room."
        off "Are they smiling right now?"
        scene ep5_sc4_mbr_24
        mc "I ... I don't understand... Aren't you mad at me? At us? Is sharing me ok for you ?"
        sf "Well, you betrayed me, that is undeniable."
        sf "And there will be retribution."
        sf "But... I love you. And I have more to lose in hating you."
        sf "And sharing... With [sis_name]... As I just said, it's ok."
        sf "She's the only one I would be able to share you with."
        scene ep5_sc4_mbr_25
        off "[sis_name] seems to be completely ok with that."
        off "She looks actually quite happy about it."
        mc "Is this some kind of trap or something?"
        mc "What do you expect me to say?"
        mc "I've told you I love you both and you're somehow offering me every man's dream."
        mc "What am I supposed to answer ?"
        sis "It's not a trap, [mc_name], we're not trying to trick you or anything... it's just..."
        sf "We thought it could be a way to make everyone happy."
        sf "We thought we could try it."
        sf "And you could just say yes."
        sis "You don't want it?"
        sis "We thought you would like the idea..."
        off "What the fuck are you waiting for [mc_name]?"
        off "Say it! Yell it! Scream it! You want it!"
        off "You dreamed about it! Literally! Say it!"
        scene ep5_sc4_mbr_27
        mc "YES!"
        off "I utter the words far more loudly than I wanted."
        off "I feel ridiculous."
        mc "I mean... yes, of course..."
        off "The silence that ensues is of the awkward type."
        off "What now?"
        off "I have the feeling that my life just got infinitely more complicated."
        off "The air around me feels so dense that it's difficult to breathe."
        off "The tension is palpable."
        off "And it suddenly vanishes."
        off "They're both genuinely smiling."
        scene ep5_sc4_mbr_28
        sf "Great! I'm glad we could resolve our issue!"
        scene ep5_sc4_mbr_29
        off "She closes the distance between us and plants a small kiss on my lips."
        off "I don't even have the time to respond to her kiss that she's already gone, heading towards the door."
        off "The change of tone is simply shocking."
        off "[sf_name] is now so light and carefree that it completely wipes the mood and sets it to happiness."
        sf "Guys, I'm hungry. My stomach is growling."
        scene ep5_sc4_mbr_30
        off "[sis_name] is about to follow her when she stops and comes back to kiss me, just like [sf_name] did."
        off "She smiles."
        off "I wonder if I ever saw her smile like that."
        scene ep5_sc4_mbr_31
        off "I stand completely baffled while the girls leave the bedroom talking about that missed breakfast and how next time they should try to resolve their differences faster."
        sf "Is it too late for eggs and bacon?"
        sis "It's never too late for bacon. Ok? Never."
        off "What the fuck is happening?"
        $ dual_love_path = True
        jump ep5sc13
    else:


        off "I can hear [sf_name]'s door opening."
        scene ep5_sc4_mcr_03
        off "I slowly raise up as the faint voice of [sis_name] comes to me."
        sis "You don't have to go, [sf_name]."
        sf "Of course I have to go."
        sf "I'm not going to stay here watching the two of you."
        sis "We won't do anything, I promise."
        sis "I've told you, it's over."
        sf "It doesn't matter. I have to go."
        scene ep5_sc4_c_01
        off "I join them in the hallway."
        off "I know that there's nothing I can do or say."
        off "I can only contemplate the consequences of my actions."
        off "I feel ashamed."
        scene ep5_sc4_ent_01
        off "I follow them at the entrance."
        off "[sis_name] keeps begging [sf_name] to stay, then to call her when she'll be back home."
        off "She says goodbye to [sis_name] but doesn't even look at me."
        off "[sf_name] is gone."
        off "[sis_name] and I are alone."
        jump ep5sc7


label ep5sc5:


    if sis_love_path == True:
        scene ep5_sc5_mcr_03 with dissolve
        off "Back in my room, I leave the adrenaline rush behind me."
        off "That could have been bad."
        off "We've been careless."
        off "We can't allow ourselves to get caught, even by [sf_name]."
        off "That was intense, though."
        off "And kind of exciting if I'm being honest..."
        off "Yeah, well... I'm not sure that a little thrill is worth the consequences of getting caught."
        off "I can't even imagine what would happen if [sf_name] caught us like that."
    else:
        scene ep5_sc5_mcr_01 with dissolve
        off "I wake up to the sound of the girls leaving the house."
        off "I can hear their laughs fading in the distance as I emerge."
        off "Once again I have the impression that I barely got any rest last night."
        off "I do my best not to let my brain immediately replay yesterday's event, but it's kind of a lost cause."

    if sf_love_path == True:
        if ep4sflovetalked == True:
            off "I can't stop thinking about [sf_name]'s story."
            off "No wonder she's a special kind of a girl with such a weird background."
            off "Having a strange English Chinese dominatrix nanny who teaches you her twisted view on life while doing s/m stuff with your father right in front of you..."
            off "That must have some impact on your personality..."
            off "Her sudden disappearance is worthy of some mystery novel, though."
            off "That reminds me that I have actually no idea what [sf_name]'s father does."
            off "What's his job?"
            off "I only know it forces them to move every three or four years."
        else:
            if ep4sfbuttholelicked == True:
                off "That was weird."
                off "Why did I choose to lick [sf_name]'s asshole?"
                off "Next time, I'll definitely go for something more conventional."
                off "That was so awkward that I'm not even sure she got some real pleasure out of it."
            else:
                off "That was disappointing."
                off "I clearly failed to give [sf_name] any real pleasure."
                if sis_sub_path == True:
                    off "I didn't have any problem making [sis_name] come, but I couldn't do the same with [sf_name]."

                off "She was clearly stressed as fuck, and that didn't help, but still."
                off "Maybe I'm just not great at it."
                off "After all, I've never touched a girl in any way before this week..."
                off "I need to learn how to pleasure a girl."

        scene ep5_sc5_mcr_02
        off "The whole event was very strange."
        off "She was so afraid..."
        off "Did she really think that I would be... upset about her change of heart to the point that I could rape her or something?"
        off "She can't have that kind of opinion of me, or else she wouldn't even consider me as her boyfriend, that's unimaginable."
        off "And uncomfortable."
        off "I'll have to talk about it seriously with her."
        off "I can't let her be scared of me."
        off "That's not how this kind of relationship should work."
        off "She has to know that I'll never hurt her or anything like that."


    if sf_dom_path == True:
        off "My relationship with [sf_name] is obviously a really weird one."


        if sis_love_path == True:
            off "I have no idea how she would have reacted if she had caught us in the act this morning, but I'm sure I wouldn't have liked it."
        if sis_sub_path == True or sis_sub_path == True:
            off "Come on [mc_name]."
            off "What are you doing?"
            off "You know you shouldn't have agreed to play with her in the first place."
            off "You're in some serious mess."
            off "If [sf_name] learns about what I'm doing with [sis_name], I'm fucked."
            off "If [sis_name] learns about what I'm doing with [sf_name]."
            off "I'm fucked too."


        off "I don't even know why I haven't told her that I wasn't interested anymore."
        off "She gave me the perfect opportunity herself yesterday."
        off "Why didn't I seize it?"
        scene ep5_sc5_mcr_02
        menu:
            "Am I enjoying what she does to me? [sfDomPath]":
                $ ep5domenjoy = True
                off "Taking that thing in my ass was certainly painful, but let's be honest..."
                off "She made sure I got some pleasure from it..."
                off "And not only from her hand on my dick..."
                off "I don't enjoy suffering... at least I don't think I do..."
                off "But maybe I like her being... assertive..."
            "I have the feeling that there's more to it than it seems...":

                $ ep5domwhy = True
                off "I believe she said that it was a first for her too... and I didn't have the impression that she took much pleasure from it herself."
                off "However, she seems to be... resolute and determined to follow that path."
                off "I wonder why she's acting like that."
                off "Maybe I should talk with her about it."

            "She just wants to hurt me." if ep4willingsodom == False:
                $ ep5domno = True
                off "She's obviously crazy."
                off "If I let her do her thing she's going to rip my ass apart."
                off "And nothing tells me that she'll let me fuck her after that."
                off "She only wants to hurt me."
                off "She's crazy."
                off "I need to put an end to this."

    if sis_sub_path == True:
        scene ep5_sc5_br_01
        off "[sis_name]... She said yes."
        off "I still can't believe it."
        if sis_sub_love_path == True:
            off "It's very strange."
            off "I feel like I'm completely in charge of her now."
            off "She's my responsibility."
            off "It's actually pretty far from what I expected."
            off "What did you expect, [mc_name]?"
            off "A quick shag on the sofa from time to time?"
            off "Mindless and meaningless sex?"
            off "Instead of that, you are now emotionally involved with her."
            off "And I mean deeply involved."
            off "I feel like I only live for her now... and I'm happy with it."
            off "Fuck... It kind of gave some meaning to my life."
            off "Big words, [mc_name], you don't know what you're talking about."
            off "Is this what love feels like?"
            off "Am I in love with her?"
            off "Does she feel the same?"
            off "She sure liked me enough to submit to me completely."
            off "I'm pretty sure I could have fucked her last night."
            off "She was ok with it."
            off "Holy shit."
            off "It's going to happen."
            off "Soon."
        else:

            off "Her expression, when I sprayed my load on her face, was priceless."
            off "God, the things I want to do to her..."
            off "She makes me crazy."
            off "I should probably punish her for that."
            off "Oh yeah, I'm going to teach you a few things, Princess."
            off "Like respect."
            off "And discipline."
            off "You're mine now."
            off "My dick is getting hard just thinking about it."
            off "I'll have to do something about it."
        scene ep5_sc5_mcr_04
        off "I don't know where we're going but one thing is certain: it must stay secret."
        off "No one must know."
        off "I can't imagine Dad and mom's reaction if they learn about the kind of relationship I now have with [sis_name]."

    if ep4sobcome == True:
        off "The psycho twins must be so pissed off."

        scene ep5_sc5_mcr_02

        if ep4decisivetry == True:
            if ep4decisivefail == True:
                off "[sf_name] completely humiliated Luke."
                off "It's the first time I see her so... dominant."
                off "I couldn't convince [sis_name] to be reasonable after all."
                off "But at least I tried."
                if ep4sobbetrayed == True:
                    off "I betrayed the psycho twins in the process and ruined my chances of going undercover to... To do what?"
                    off "That was a really dumb idea."
                off "They have one more reason to hate us now."
                if ep4sobbetrayed == True:
                    off "And me personally."
                off "We should be careful."

            if ep4decisivesuccess == True:
                off "But [sis_name] listened to me."
                off "As unbelievable as it is."
                off "She listened."
                off "The things I've said may have felt dumb but they were true, and I think that touched her."

            scene ep5_sc5_br_01

            if ep4nighttalk == True:
                off "That moment I shared with her last night... That was special."
                off "However... I have no idea how to behave now."
                off "How were we doing things three years ago?"
                off "I remember we talked and hung out a lot together."
                off "She was kind of a tomboy back then."
                off "Things have changed."
                off "I don't think she'll come over to my room and play videogames with me, or anything like that."
                off "We both have changed and we'll need to adapt."
                off "We'll find out."
                off "I guess we're both willing to put some effort into it, so it's fine."
                off "We'll make it work again."

            scene ep5_sc5_mcr_04

            if ep4decisivesuccess == True:
                off "However, we should be even more careful than we were. The psycho twins may want to react to this humiliation."
        else:


            if ep4hateregrets == True:
                off "I completely fucked up yesterday."
                off "I need to do something, I need to stop swimming in shit."
                off "Let's be honest."
                off "Contacting the psycho twins was already a bad idea."
                off "What was I thinking?"
                off "That I would go undercover and bring them down like that?"
                off "And trying to play along with them was even dumber."
                off "I've completely lost the last remnants of respect the girls could have for me."
                off "The irony is that it wasn't even ill-intended, right?"
                off "If I called the psycho twins first, it was to find a way to push them away from [sis_name]."
                off "The bullshit about fucking her only came after that."
                off "God, I can't believe I seriously thought about it. "
                off "Maybe I can come clean about it."
                scene ep5_sc5_br_01
                off "If I tell the girls everything... Maybe they can understand."
                off "No, they won't."
                off "You'll just look like a moron once more."
                off "I was dumb anyway."
                off "I can't deny it."
                off "But I'd rather be dumb than a complete asshole."
                off "They won't even listen to you."
                off "They hate you now."
                off "I have no doubt that [sf_name] hates me."
                off "But I'm not so sure about [sis_name]."
                off "She may hear me."
                scene ep5_sc5_mcr_04
                off "Yeah, well, don't get your hopes too high, [mc_name]."
                off "You fucked up."
                off "They'll make you pay for that."

            if ep4hatemotivation == True:
                off "I can't believe I didn't understand it sooner."
                off "That whore..."
                off "Everything happens because of her."
                off "Everything has gone wrong since [sis_name] met her three years ago."
                off "She turned [sis_name] into that bratty bitch and isolated her from our family."
                off "She made her a lesbian."
                off "She corrupted [sis_name] and I've let her get away with it."
                off "Fuck it."
                off "I have to do something."
                off "She made me look like a fool in the eyes of [sis_name]."
                off "That slut has to pay."
                off "I don't know how but I swear, she will pay..."
                off "I bet that the psycho twins can help me with that."
                scene ep5_sc5_br_01
                off "Maybe I can deal with them."
                off "Trading [sis_name]'s safety for [sf_name]'s ass or something like that."
                off "Yeah, that sounds nice."
                off "That cunt deserves that."
                off "Maybe I'll fuck her myself before the twins double team her."
                off "I'll train her pussy myself..."
                off "Ok. Calm yourself, [mc_name]."
                off "This is going too far."
                scene ep5_sc5_mcr_04
                off "You are talking about raping her, or worse."
                off "This is no joke."
                off "This is a fucking crime."
                off "You will go to jail."
                off "You're not that kind of guy [mc_name]."
                off "You're not a fucking monster."
                off "It's her fault."
                off "She's turning me into this."
                off "Or maybe you're just overreacting."
                off "[sf_name] didn't do anything that deserves that kind of reaction."
                off "She just protected [sis_name] against the psychos and against you."
                off "Get real."

        if ep4lukephonedsuccess == True:
            jump ep5sc6

    if ep4sobcome == False and sis_sub_path == False and sis_love_path == False and sf_love_path == False and sf_dom_path == False:

        off "However, this is a new day and the past..."
        off "Well, it's in the past I guess..."
        off "Let's focus on what's to come."
        scene ep5_sc5_mcr_02

        if ep4gonetokf == True:
            off "Like Kelly."
            off "Kelly?"
            off "It's weird."
            off "I think about her a lot since I've met her."
            off "I can't help but feel sorry for her."
            off "It's stupid."
            off "The girl is like a professional liar."
            off "I can't trust her."
            off "I can't believe a single word that comes out of her pretty mouth."
            off "Pretty mouth, huh?"
            off "Yeah ok, she's pretty."
            off "You mean she's freaking cute."
            off "No one can hear the voice in your head, [mc_name]."
            off "There's no need to lie to yourself."
            off "The girl is cute as fuck."
            off "Ok. I can't deny it."
            off "How come I didn't notice her in High school?"
            off "There was something like a thousand students in our school, but still."
            off "Her attitude probably was very different back then, if she was a different person like she says... maybe you just don't recognize her."
            scene ep5_sc5_br_01
            off "That would make sense."
            off "We didn't share any class so that wouldn't be so farfetched."
            off "And she has some kind of a crush on you."
            off "Ok, that part is surprising."
            off "I'm not aware of any girl who's ever had a crush on me."
            off "So... to think that this kind of girl could be interested in me... That's a huge red flag."
            off "She's obviously lying."
            off "She's trying to manipulate you."
            off "Or... she really is not your regular high school cheerleader queen anymore."
            off "Maybe she's being honest."
            off "Her description of why and how seemed sensible."
            off "Again, a professional liar."
            off "I can't trust her."
            off "She warned you about the psycho brothers... why would she do that if she was trying to manipulate you?"
            off "Maybe it's just a diversion."
            off "Maybe she wants us to trust her before she betrays us."
            off "Or maybe she's being sincere and really wants to help."
            off "Things aren't getting any easier, are they?"
            off "I wonder what Steve would say about that."
            off "Probably something like YOLO this and YOLO that."
            off "She's cute."
            off "Maybe I should see her again, if I can talk with her a bit more, maybe I can see if she's really sincere or if she's just playing us."
            off "Should I call her?"
            off "I should call her."
            off "What will I tell her?"
            off "Maybe I'll start with \"Hello\" and \"How are you\"."
            off "Perhaps an \"I'm glad to hear your voice\"?"
            off "No, that's too much."
            off "That would be openly flirting with her."
            off "Do I want to flirt with her?"
            off "I don't know... I liked her voice, though..."
            off "Ok, That's enough [mc_name], stop thinking about her."
            off "I can see where this is going and it won't end well for you."
            scene ep5_sc5_mcr_04
            off "Kelly is probably the only girl on this planet you have to stay away from at any cost."
            off "If [sf_name] and [sis_name] know you're thinking about kelly in that way... They would kill you right on the spot."
            off "She's kind of their arch enemy."
            off "Even if she apologized to them in a spectacular fashion..."
            off "That's kind of unfair."
            off "And sad."
            off "But I don't think there's anything I can do about that."

    jump ep5sc8


label ep5sc6:
    scene black with dissolve
    with Pause(2)
    show text "One hour later."
    with Pause(2)

    if ep4sobbetrayed == True:
        scene ep5_sc6_lr_01_smile
        off "I don't really know why I'm watching TV right now."
        off "there's nothing interesting on."
        off "I'm just waiting for the girls to come back."
        off "I'm hungry."
        off "I think it's [sf_name]'s turn to handle breakfast today."
    else:
        if ep4hateregrets == True:
            scene ep5_sc6_lr_01_depressed
        else:
            scene ep5_sc6_lr_01_anger

        off "Television is usually a good choice when you need to brainwash yourself and momentarily forget about whatever problem you may have."
        off "This time, however, my problems are a bit too reluctant to fade away."
        off "I can't stop thinking about this mess."

        if ep4hateregrets == True:
            off "On one hand, I think I should apologize and explain everything."
            off "I can't be forgiven if I don't apologize and accept my stupidity."
            off "But on the other hand, I can't stop thinking that it's useless."
            off "That was one mistake too many."
            off "There's no chance they will forgive me."
            off "They won't even believe me, so..."
            off "Why should I humiliate myself by uselessly apologizing?"
            off "What is done is done."

        if ep4hatemotivation == True:
            off "[sf_name] humiliated me."
            off "Who does she think she is?"
            off "That bitch won't see it coming."
            off "She thinks I'm a useless moron or something like that."
            off "I'll show her."
            off "She probably thinks she's way out of my league."
            off "We'll see who has the last laugh."

    off "My phone rings."

    if ep4sobbetrayed == True:
        scene ep5_sc6_lr_02_serious
    if ep4hateregrets == True:
        scene ep5_sc6_lr_02_fear
    if ep4hatemotivation == True:
        scene ep5_sc6_lr_02_anger

    off "I grab it with moderate enthusiasm."
    off "I recognize this number."
    off "I used it yesterday."
    off "It's Luke."

    if ep4sobbetrayed == True or ep4hateregrets == True:
        off "Crap."
        off "Of course."
        off "I knew they would call me."
        off "Well... Let's get this over with."
    else:
        off "Just what I needed."
        off "With a bit of luck, these two morons will prove helpful."


    if ep4sobbetrayed == True:
        scene ep5_sc6_lr_03_serious
        mc "Hello?"
        lk "[mc_name], we are very disappointed with your behaviour yesterday."

        off "This is it."
        off "He's going with a cool voice but this won't be a pleasant conversation."
        off "He's going to threaten me, threaten us."
        off "He wants to instill fear."
        off "Maybe he hopes to get something from me if he manages to frighten me enough."
        off "Keep cool [mc_name]."
        off "How do we play this one?"

        menu:
            mod "No known conequences yet."
            "Keep it civil. [gr]\[KeepCivil\]":
                $ ep5keepcivil = True
                mc "Well, I changed my mind."
                lk "I could see that."
                lk "It's a shame, [mc_name]."
                lk "You probably didn't think of the consequences."
                scene ep5_sc6_lr_04_serious
                mc "I'll stop you right there, Luke."
                mc "You're going to threaten me, I'm going to tell you I don't care, and so on, and so forth."
                mc "Let's keep it short."
                mc "You have a choice here: you can let go of whatever you're after and leave peacefully."
                mc "You don't go after us, we forget about all of that, we don't see each other ever again and we're all happy."
                mc "Or you can pursue your attempt at whatever you're trying to achieve."
                mc "We will most likely end up clashing and I can assure you I am more than ready to protect [sis_name] and [sf_name]."
                mc "It won't end well, for you, for your brother, for me, most probably for all of us."
                mc "I'm not threatening you, it's just how it is."
                off "The line goes silent for a second before he hangs up without replying."
                scene ep5_sc6_lr_05_serious
                off "I tried my best to reason with him but it was pretty obvious that it was a lost cause."
            "I'm done with playing nice. [gr]\[ScumbagCrackWhores\]":

                $ ep5scumbagcrackwhores = True
                mc "Story of my life."
                mc "What do you want?"
                lk "You won't get away with this. We don't like to be played. You will regret this. You will all regret this. We're taking it personally."
                mc "Oh, I see. Should I tremble in fear?"
                lk "You won't be so cocky when we come for you."
                scene ep5_sc6_lr_04_hate
                mc "I don't have all day, you cocksucking moron."
                mc "If you're done threatening me like the little bitch you are, maybe I can show you how it's done, when it's done right."
                mc "If you ever come to my house again, you won't fucking get out of here alive."
                mc "That is a promise."
                mc "I don't care what it'll take but I'll fucking kill you."
                mc "If I ever hear about you or your brother bothering one of my friends again, I will track you down and I will break your fucking spine, you god damn sack of shit."
                mc "I'll make you swallow your balls."
                mc "Do you hear me or are you too busy sucking your brother's tiny baby penis?"
                mc "Don't bother replying, I don't want to hear your voices again."
                mc "Enjoy fucking yourselves, you scumbag crack whores."
                off "I hang out and let out a smile."
                scene ep5_sc6_lr_05_laugh
                off "Scumbag crack whores."
                off "That was a nice one."
                off "I don't know how I've came up with this but it's freaking good."
                off "I'll have to share this with Steve."
                off "It's hilarious."
                off "I guess I'm laughing to relieve the tension."
                off "My little speech was pretty intense."
                off "It was probably useless, though."

        scene ep5_sc6_lr_05_serious
        off "They will come back."
        off "There's no doubt about it."
        off "I'd better get ready."
        off "The guys are twice my size and there's two of them."
        off "I'll have to hit hard and hit first or they'll kill me..."
        off "And then do whatever they want to the girls..."

    if ep4sobbetrayed == False:
        if ep4hateregrets == True:
            scene ep5_sc6_lr_03_fear
            mc "Hello?"
            lk "Hello, [mc_name]. How are you ?"
            mc "I'm fine, thank you..."
            lk "Yesterday didn't turn out as we expected."
            lk "[sf_name] sure doesn't want to cooperate."
            lk "However, we want you to know that we're happy with your performance."
            lk "You quickly understood what you had to do."
            lk "We are satisfied."
            lk "We're counting on you from now on."
            off "They don't have a choice."
            off "With [sf_name]'s intervention, yesterday, Luke has surely lost all contact with [sis_name]."
            off "This only leaves them with two options: me or brute force."
            off "Crap, what do I say?"
            off "I don't want to have anything to do with them anymore."
            off "Going undercover was and still is a dumb idea, it'll get me killed."
            off "But hell... this is a golden opportunity... So..."
            off "What do I say?"
            off "Can I even step back now?"
            off "They won't take no for an answer."
            off "Maybe I shouldn't have taken that call..."
            off "He's waiting for an answer, [mc_name]!"
            off "Come on, say something!"
            scene ep5_sc6_lr_04_fear
            mc "Yeah, [sf_name]... sure is a bitch."
            lk "We thought about a solution that may please you."
            lk "We want to discuss it with you."
            lk "We think it would be best if we meet somewhere."
            lk "Are you free at noon ?"
            off "Like I have a choice."
            mc "Sure..."
            lk "I'll send you the address."
            lk "We're looking forward to this meeting, [mc_name]."
            mc "Likewise..."
            off "He hangs up."
            scene ep5_sc6_lr_05_fear
            off "What a fucking moron I am."
            off "What the fuck am I going to do, besides dying?"
            off "Calm down, [mc_name]."
            off "You heard him."
            off "He's going to tell you what they want to do then you can probably go to the police and set up a trap or something."
            off "As you said, it's a golden opportunity."
            off "Yeah, a golden opportunity TO GET KILLED."
            off "Everything will be fine, you just go there, you listen, then you go straight to the police and it'll be alright."
            off "Fuck, I truly am a moron."
        else:

            scene ep5_sc6_lr_03_anger
            mc "Hello ?"
            lk "Hello, [mc_name]. How are you ?"
            mc "Feeling like shit."
            mc "This bitch deserves a lesson."
            mc "Tell me we'll make her pay."
            scene ep5_sc6_lr_04_anger
            lk "I'm glad to see that we're on the same page."
            lk "What do you think about meeting us today at noon so we can talk about it."
            mc "Sounds wonderful. Where?"
            lk "I'll send you the address."
            lk "We're looking forward to this meeting, [mc_name]."
            mc "Likewise."
            off "He hangs up."
            scene ep5_sc6_lr_05_anger
            off "Those two fuckers are crazy."
            off "I'm pretty sure they already have a plan to bring [sf_name] to her knees."
            off "No doubt she will know her place after that."

    jump ep5sc8


label ep5sc7:

    scene black with dissolve
    with Pause(2)
    scene ep5_sc7_lr_01

    off "[sf_name] has been gone for a couple hours now."
    off "[sis_name] has retreated to her room."
    off "She doesn't want to talk to me."
    off "I can't blame her."
    off "I guess it will get better in a few days but for now, the feeling of loss and guilt is overwhelming."
    off "The doorbell rings its tone."
    off "I can hear [sis_name] literally bursting out of her room and running down the stairs."
    off "She hopes that [sf_name] could have changed her mind and came back."
    off "I hope so too of course."
    off "But the chances are low."
    scene ep5_sc7_ent_01
    off "Kelly?"
    off "What is she doing here?"
    kf "Hello, [mc_name]."
    mc "Hello, Kelly."

    if ep4morningkftold == False and ep4kflatetold == False:
        off "I just remembered that we're not supposed to know each other."
        off "But I don't think I care anymore."
        off "Enough lies."
        off "[sis_name] doesn't even seem to realize that Kelly and I have already met."
        off "She has other things on her mind."

    sis "So, are you going to tell us what you're doing here or what ?"
    off "[sis_name]'s voice sounds broken and harsh."
    off "Just as her facial expression."
    off "Kelly doesn't fail to notice it."
    scene ep5_sc7_ent_02
    kf "I'm sorry, I hope I'm not bothering you at a bad time, I..."
    sis "You are."
    sis "Get to the point."
    sis "What do you want?"
    off "Kelly clearly doesn't deserve to be treated this way, but I can easily understand [sis_name]'s lack of civility and patience."
    scene ep5_sc7_ent_03
    mc "[sis_name], please, we can at least be polite."
    mc "What can we do for you, Kelly?"
    kf "It's... I... I have something important to tell you and... It's about Luke and Ray, and... Isn't [sf_name] here?"
    kf "It does concern her so..."
    mc "She's not here at the moment..."
    kf "Oh..."
    off "She seems concerned."
    scene ep5_sc7_ent_04
    kf "Could you give her a call?"
    kf "We need to warn her..."
    sis "To warn her?"
    sis "What are you talking about?"
    kf "It's... Luke and Ray, [sis_name]..."
    kf "They're not really interested in you..."
    kf "They're after [sf_name]..."




    scene black with dissolve
    with Pause(2)
    show text "4 years later."
    with Pause(2)
    show text "Another country."
    with Pause(2)

    scene ep5_sc7_road_01
    off "The road is in pretty bad shape and the night is dark."
    off "Clouds are covering the stars."
    off "She has been driving for more than an hour now."
    off "I wanted to come alone but she insisted she came along."
    off "She took care of everything."
    off "I still remember how we felt."
    off "Just as we thought it couldn't get worse."
    scene ep5_sc7_lr_02
    off "[sis_name] jumped on her phone and tried to call [sf_name]."
    off "We all did."
    off "We called her mobile, we called her home."
    off "She didn't respond."
    off "We called the police."
    off "And they didn't give a shit."
    off "We called her father and he took the matter in his own hands."
    scene ep5_sc7_po_01
    off "Curiously, the cops weren't so prompt to discard his request as they were to ignore ours."
    off "Turns out, when you have money and social weight, authorities are more inclined to listen and help you."
    off "We also called mom."
    off "I remember she couldn't find a flight to come back immediately."
    off "So she rented a car and drove 8 hours in a row so she could be with us before sunrise."
    scene ep5_sc7_lr_03
    off "[sis_name] didn't even try to protest when she took her in her arms."
    off "She just let go and cried."

    off "A couple of hours after Kelly arrived, a panicked Steve called me."
    off "There was something on our school social network."
    off "A video I should see before it gets moderated."
    scene ep5_sc7_lr_04
    off "An unconscious [sf_name], being double teamed by two guys wearing masks."
    off "It was an hour-long drug rape on a bare mattress, thrown directly on the ground of some unoccupied warehouse."
    off "They took turns on her before using her both at the same time."
    off "I screamed and cried in rage and horror as I watched them doing their thing."
    off "I couldn't detach my eyes from the screen."
    off "It only took a few minutes for the video to spread everywhere on the web."
    off "Every porntube, every p2p forum, everywhere."
    off "They tried to have it removed but it proved futile."
    off "Even today you can find it in a matter of seconds."
    off " \"Cassandra Carter enjoys two big cocks.\""
    off "They made sure it would be published with her real name."
    off "They wanted to destroy her."
    off "They succeeded."
    off "The police took almost 48 hours to find her."
    scene ep5_sc7_warehouse_01
    off "The psycho brothers had abandoned her right where they raped her."
    off "An abandoned building in a creepy industrial zone."
    off "She was still on the mattress."
    off "She was alive."
    off "Raped, beaten, injured, but alive."
    off "Her aggressors where nowhere to be seen."
    off "Later I came to learn that they assaulted her almost immediately after she left our house."
    off "[sf_name] is a tough girl and she was more than able to defend herself, but there's nothing you can do when your aggressor tases you in the back before injecting you with some anesthetic."
    off "They transported her to that warehouse and raped her far longer than the video let you think."
    off "Eventually, the anesthetic faded away and she woke up."
    off "Still half asleep, she managed to break Luke or Ray's leg before being tased again and beaten to a pulp by these cowards."
    off "They broke her some ribs, an arm, and heavily damaged her face."
    off "They abandoned her and escaped."
    off "The police couldn't catch them but retraced their path to the nearest border."
    off "They had prepared their escape."
    scene ep5_sc7_ho_01
    off "[sf_name] was hospitalized at Harper's Hope Hospital, where my father works."
    off "We tried to visit her but she refused to let us see her."
    off "She made it clear that she didn't want to see us ever again."
    off "They moved out."
    off "Changed numbers."
    off "Disappeared."
    scene ep5_sc7_sr_01
    off "[sis_name] couldn't take it."
    off "I tried my best to support her but she rejected me, refusing to even see me."
    off "She had a breakdown."
    off "She stayed in her room at all times, crying until exhaustion only to fall into a sleep filled with nightmares from which she would wake up screaming."
    off "It lasted for 6 months."
    scene ep5_sc7_sr_02
    off "Then one morning, [sis_name] stopped crying."
    off "She stopped everything."
    scene ep5_sc7_sr_03
    off "Mom found her sitting on the floor of her room."
    off "Unresponsive."
    off "Her body was still there but her mind was gone."
    off "We don't know if the pain has consumed everything of her or if she's still there, locked in a corner of herself."
    off "We don't know if she can come back from that."
    off "Mom sleeps with her, clothes her, feeds her, takes care of her needs."
    off "She has quit her job to take care of her full time."
    off "She refused to have her placed in an institution and abandoned her own life in order to keep [sis_name] at home."
    off "Her state has been unchanged since then."
    scene ep5_sc7_road_02
    off "I guess that leads us to me."
    off "I failed in college."
    off "I didn't even manage to pass the first exams."
    off "I was focused on something else."
    off "Steve's father had spent some time in the military."
    off "He wasn't a big fish or anything, but after 6 months of efforts, he managed to put me in touch with a guy, who knew a guy, who knew a guy, who happened to knew a ghost."
    off "Dead several years ago, the man was still walking on his two feet and was making a living of the skills he acquired during his years in black ops or whatever it is."
    scene ep5_sc7_road_03
    off "His rates where outrageous but I didn't expect anything less."
    off "I gave him everything I had and worked my ass off for the last three years to keep him working on the task I contracted him for."
    off "He gave me a discount."
    scene ep5_sc7_road_04
    mc "It's here."
    mc "You can go and park inside."
    off "We haven't said a word since we left the hotel."
    off "I barely gave her the directions to follow according to the map."
    off "She knows as well as I do that this is the end."
    off "When I first met her, she was that cute and shy girl who was seeking redemption."
    off "I tried to push her away but she kind of clung to me."
    off "She is nothing but patience and kindness to me."
    off "I used her to ease the pain."
    off "She loves me and I'm using her."
    off "Just how much suffering can she stand for my sake?"
    off "I've become a monster."
    off "I know that."
    off "I don't care anymore."
    off "I stopped caring a long time ago."
    scene ep5_sc7_blacksite_01
    kf "Wait! I'm coming with you."
    mc "No, you're not."
    scene ep5_sc7_blacksite_02
    kf "It's not negotiable."
    mc "You're right."
    mc "You're not coming, and it's not negotiable."
    mc "Go back to the hotel."
    mc "Mr. Castle will give me a ride back later."
    scene ep5_sc7_blacksite_03
    off "She burst out crying."
    kf "No, he won't!"
    kf "I know he won't!"
    mc "Kelly, please..."
    kf "I know what you're going to do."
    kf "And they deserve it."
    scene ep5_sc7_blacksite_04
    kf "But you don't."
    kf "Do you hear me?"
    kf "You don't!"
    mc "Kelly, you can't come with me."
    kf "Then I'll wait here for you."
    kf "Promise me you will come back, [mc_name]. Please!"
    kf "Tell me you'll come back to me."
    kf "Please, promise me."
    off "It's harder than I thought it would be."
    mc "I've stopped making promises."
    kf "I know you don't love me and I don't care."
    kf "You have to come back to me."
    kf "No matter what."
    scene ep5_sc7_blacksite_05
    kf "I will take care of you."
    kf "Promise me, you will come back."
    mc "I promise."
    mc "I'll come back to you."
    off "She sighs. She trusts me. She slowly releases me, letting me go."
    kf "I'll wait for you here."
    off "I'm sorry, Kelly."
    scene ep5_sc7_blacksite_06
    off "Mr. Castle emerges from the shadows as I walk away from the car."
    mc "Mr. Castle."
    fc "Kid."
    mc "I received your message."
    scene ep5_sc7_blacksite_07
    off "He gives a quick look at Kelly and her car."
    fc "She'll be safe here."
    fc "Don't worry."
    fc "The package is downstairs."
    mc "Thank you."
    off "Strangely, I appreciate his concerns for her safety."
    off "I feel like I'm already gone, out of this world."
    scene ep5_sc7_blacksite_08
    off "It's not really me anymore, walking in this dirty corridor."
    off "I'm just looking at the scene as it unfolds before my eyes."
    fc "They were living on the coast."
    fc "They changed their names but weren't really hiding."
    fc "They even set up a little business."
    fc "They sell local girls to foreigners for \"special occasions\"."
    fc "Just as you asked, we tased them before putting them to sleep."
    fc "They woke up only a couple hours ago."
    mc "Thank you, Mr. Castle."
    scene ep5_sc7_blacksite_09
    off "Mr. Black stands up from his chair as we enter the room."
    off "He doesn't say a word and just gives me a tap on the shoulder before leaving."
    off "The place reeks of urine and shit."
    scene ep5_sc7_blacksite_10
    off "The two men lying on the ground shat themselves in fear."
    fc "Take your time, Kid. Make sure we got the right guys."
    off "I don't need time."
    off "They are the right guys."
    off "I know it."
    off "Mr. Castle and Mr. Black took care not to brutalize them."
    off "I can't see a mark on them."
    off "They're crying in fear and terror, their hands and feet tied on their back."
    off "I can hear them sobbing through their gags."
    mc "It's them. No doubt about it."
    fc "Good."
    scene ep5_sc7_blacksite_11
    off "Mr. Castle reaches to his back and draws a gun."
    fc "Are you sure you want to do this, Kid?"
    fc "You know... This is not a joke, there is no coming back from this."
    fc "They may deserve to die but if you kill them, they will take a part of you away with them."
    fc "Me... It's another story."
    fc "I can do it for you."
    off "I don't really listen to his words."
    off "The only thing that matters to me right now is the two guys who are looking at me in terror and the gun that Mr. Castle is handing to me."
    off "Everything else is blurred."
    scene ep5_sc7_blacksite_12
    off "I can hear the voice of Mr. Castle fading away."
    off "I feel the weight of the gun in my hand."
    off "It's surprisingly light."
    off "Luke... I don't even know if it's Luke or Ray..."
    off "He looks at me with protruding terrorized eyes as I point the weapon to his head."
    off "He tries to scream and beg."
    off "I can't hear him, but I'm sure he does."
    off "I feel like I should say something."
    off "I'm not sure what."
    mc "Do you remember me?"
    off "Speaking is difficult."
    off "My whole face feels weird."
    off "I don't even hear my own voice."
    scene ep5_sc7_blacksite_13
    mc "Do you remember her?"
    off "Am I even saying something?"
    off "He knows who I am anyway."
    off "I can see it on his face."
    off "I can't stop thinking about what they did to her."
    off "Finally, they're going to pay."
    off "I owe it to [sf_name] and [sis_name]."
    off "I can feel the trigger under my finger."
    off "Everything will be over after I press it."
    off "It won't repair anything though, I know that."
    off "Nothing will get better."
    off "[sis_name] won't come back from her oblivion and we'll never see [sf_name] again."
    scene ep5_sc7_blacksite_14
    off "We all died 4 years ago."
    off "Nothing can bring you back from that."
    off "They took everything from us."
    off "It's time I take something from them."
    off "I slowly pull the trigger."
    off "Click."
    off "What happened?"
    off "He's still looking at me."
    off "Did I miss him?"
    off "I press the trigger again."
    off "Click."
    off "Click."
    off "Click."
    off "I feel like I'm brutally being dragged back to reality."
    off "I feel nauseous."
    off "I'm crying and screaming."
    off "I've probably been the whole time."
    off "I'm panting miserably."
    off "My whole face hurts."
    off "Vertigo makes me wobble."
    scene ep5_sc7_blacksite_15
    off "The voice of Mr. Castle reaches me as he slowly puts his hands on my shoulder and on the gun."
    fc "It's ok, Kid."
    fc "You did it."
    fc "It's over."
    fc "It's ok."
    off "It doesn't feel ok."
    off "Luke is still alive."
    off "The gun didn't fire."
    scene ep5_sc7_blacksite_16
    off "Mr. Castle comes back to me, handing me a cellphone."
    fc "Someone wants to talk to you, Kid."
    off "What the fuck is happening?"
    mc "Hello?"
    cf "Hello, [mc_name]."
    off "I know this voice."
    cf "This is [sf_name]'s father."
    mc "Mr. Carter?"
    scene ep5_sc7_blacksite_17
    off "My jaws hurt."
    off "Speaking isn't easy."
    off "I'm completely lost."
    cf "Yes, [mc_name]. I want to thank you for what you did."
    mc "What? I don't understand."
    cf "You gave it your all."
    cf "You sacrificed everything you could for this moment to happen."
    cf "I thank you for that."
    cf "However, I can't allow you to kill them."
    cf "Mr. Castle and I are going to have a long and painful discussion with these two \"gentlemen\" before they meet their demise."
    scene ep5_sc7_blacksite_18
    mc "I can..."
    cf "[mc_name]. I don't doubt you can, I just don't want you to go further down that path."
    cf "You have done enough."
    cf "Mr. Castle will handle this."
    cf "You can go back and live again."
    cf "Goodbye, [mc_name]."
    scene ep5_sc7_blacksite_19
    off "Mr. Castles takes the phone back from my hand and gently pushes me out of the room."
    fc "Go back upstairs, Kid."
    fc "I'll join you in a moment."
    off "He closes the door."
    scene ep5_sc7_blacksite_20
    off "I'm so confused."
    off "All of this happened so suddenly..."
    off "What am I going to do?"
    off "I feel empty and lost."
    off "I have nothing left."
    off "Killing them has been my only goal and motivation for the last 4 years."
    off "I don't really feel frustrated."
    off "I pulled the trigger on Luke."
    off "The gun wasn't loaded, but I'm sure Luke could see himself dying."
    off "I kind of killed him and I know that Mr. Castle will take care of them for good."
    off "But what now?"
    off "I never imagined coming back from this."
    off "I always thought I would put a bullet in each of them before putting one in my own head."
    off "It seemed fitting."
    off "I've never thought of what I would do after that."
    off "I'm going to fulfill my promise of returning to Kelly after all."
    off "The poor girl."
    off "She must be terrified up there."
    off "I shouldn't make her wait."
    scene ep5_sc7_blacksite_21
    off "I've barely set foot in the room that she runs to me and starts crying again."
    off "Happier tears, I hope."
    kf "I thought I lost you."
    mc "I promised you."
    kf "You're so bad at lying."
    mc "I'm sorry."
    mc "I made you worry."
    kf "It's okay..."
    scene ep5_sc7_blacksite_22
    off "Mr. Castle joins us a few minutes later."
    fc "How are you feeling, Kid?"
    mc "I guess I'm alright, Mr. Castle."
    mc "Would you care to explain what happened ?"
    fc "I guess you deserve it."
    scene ep5_sc7_blacksite_23
    fc "Doesn't he, Miss Kowalsky ?"
    off "Kelly?"
    off "What does she have to do with this?"
    off "She hides behind my shoulder."
    kf "Do we have to do that?"
    fc "I'm afraid we do."
    fc "You see, Kid when you contacted me three years ago, you didn't have nearly enough money to even cover the expenses."
    fc "I told you I would think about it but I actually had no intention of calling you back."
    fc "But Miss Kowalsky gave us a call to support your project."
    off "Kelly?"
    off "How did she...?"
    scene ep5_sc7_blacksite_25
    fc "She didn't have any more money than you did."
    fc "But she found us a client who could afford our services and shared your interest in those two fine gentlemen."
    fc "She put a condition on it, however."
    fc "That we wouldn't let you kill them."
    fc "We had to take care of them in your stead."
    fc "Our new paying customer was ok with that."
    mc "What? Wait I ... that customer is..."
    fc "Mr. Carter. Yes."
    mc "I don't understand..."
    mc "If you're working for him, what am I doing here?"
    scene ep5_sc7_blacksite_26
    fc "Mr. Carter thought it could give you some closure."
    fc "He also needed you to confirm their identity."
    fc "He didn't want to take any risks."
    mc "That... Makes sense... I guess. So... what now?"
    fc "Just as Mr. Carter said, Kid."
    fc "You leave this god forsaken place and you resume your life."
    mc "But what about..."
    fc "Mr. Black and I will take care of everything."
    fc "They'll never get out of here."
    mc "I'm sorry, I... I need to hear you say it."
    fc "Ok Kid, listen."
    scene ep5_sc7_blacksite_27
    fc "For the next 24 hours, I will make them regret being born."
    fc "And once I'm done with them I'll put a bullet in their brains."
    fc "That's what Mr. Carter is paying for."
    fc "They're dead."
    fc "Don't doubt it."
    off "I feel like a weight lifted from my shoulders."
    off "I let out a sigh."
    mc "Thank you, Mr. Castle."
    fc "I'm just doing my job, Kid."
    fc "Oh, one last thing."
    fc "You just received an email with the coordinates of a bank account."
    fc "You gave us almost $90 000 over the last 3 years while Mr. Carter was our real client."
    fc "You can have it back."
    scene ep5_sc7_blacksite_28
    mc "What? You're refunding me?"
    fc "Miss Kowalsky asked us to make you pay, to keep you motivated."
    fc "She was afraid you could do something stupid if you didn't have that goal."
    fc "Now that it's done, you may need that money to start anew."
    fc "Good luck, Kid."
    mc "I don't know what to say..."
    kf "Thank you, Mr. Castle."
    off "Kelly's voice takes me by surprise."
    mc "Yeah, It's... Thank you, Mr. Castle."
    fc "You're welcome."
    fc "Now if you'll excuse me, I have some unfinished business waiting for my attention downstairs."
    off "A handshake later we're left alone."
    scene ep5_sc7_road_05
    off "The road that takes us back to the hotel seems weirdly different."
    off "The night itself seems brighter."
    off "I stay silent."
    off "I have a lot of questions for her but finally, none of them is really important."
    scene ep5_sc7_motel_01
    off "Back at the hotel, I notice things that didn't matter before."
    off "The room is ridiculously small, simple, and without any comfort."
    off "She doesn't seem to mind."
    scene ep5_sc7_motel_02
    off "This girl really took care of me."
    off "She even fuelled my obsession with vengeance so that I have a reason to keep on living."
    off "She did all that for me."
    off "She loves me."
    off "I don't really understand how it's possible."
    off "I feel like I don't deserve it."
    off "I don't deserve her."
    scene ep5_sc7_motel_03
    off "Somehow... I'm lucky."
    off "It's very strange."
    off "I feel like my heart is beating again."
    scene ep5_sc7_motel_04
    kf "Are you ... smiling?"
    mc "What?"
    kf "You're smiling."
    kf "I haven't seen you smile since... forever."
    kf "Are you alright ?"
    mc "Yeah. It's..."
    mc "I'm actually feeling... Different..."
    kf "How so?"
    mc "Better."
    kf "Really?"
    scene ep5_sc7_motel_05
    off "Her smile is so sweet."
    off "How haven't I noticed it before?"
    mc "Yeah. Thanks to you."
    off "What now?"
    off "Do I have a reason to keep on living now?"
    scene ep5_sc7_motel_06
    mc "I'm sorry, for everything you went through because of me."
    mc "I didn't treat you well."
    mc "You deserve better."
    kf "It's okay."
    kf "You haven't been that awful."
    mc "I have been... But I'll be better if you give me the chance..."
    kf "Like I'm going to dump you now."
    kf "I told you, I'll take care of you."
    kf "You won't get rid of me so easily."
    scene ep5_sc7_motel_07
    off "She's so kind."
    off "I've been in a relationship with her for three years and a half now and it's like I'm looking at her for the first time."
    off "Maybe I have a reason to keep on living."
    mc "I think we should go to see my parents next weekend."
    kf "What?"
    scene ep5_sc7_motel_08
    off "She seems genuinely surprised."
    off "I haven't seen my parents in years."
    off "They're not even aware of her existence."
    mc "I think it's time they meet my girlfriend."
    scene ep5_sc7_motel_09
    off "I barely have the time to see her smile before she hides her face in my chest and starts crying."
    off "Happy tears."


    scene black with dissolve
    with Pause(2)
    show text "You have reached one of the possible ends of Summer Scent."
    with Pause(2)
    menu:
        "Exit to main menu.":
            return

    return


label ep5sc8:
    scene black with dissolve
    with Pause(2)

    if ep4hatemotivation == True:
        scene ep5_sc8_k_01 with dissolve


        $ evil_asshole_path = True

        off "The bitch cooks."
        off "It smells damn good."
        off "There's no way she cooked any of that for me."
        off "I won't give her the satisfaction of lusting after her bacon."
        off "She's probably waiting for me to show up so she can tell me to go fuck myself."
        off "In my own house."
        off "I won't let her humiliate me again."
        off "Let's retreat for now."
        off "I'll eat later."


        scene black with dissolve
        with Pause(2)
        show text "A few minutes later."
        with Pause(2)

        scene ep5_sc8_mcr_01 with dissolve
        off "I still have a couple of hours to kill before I meet those two morons."
        off "I'll leave early and stop on the way for some food."
        off "That'll be better than her stupid breakfast."
        scene ep5_sc8_mcr_02
        sis "[mc_name]?"
        mc "What? Can't you knock, for god sake?"
        sis "Okay... I can see you're in a good mood, as always."
        sis "Sorry to bother you..."
        sis "Breakfast is ready."
        mc "So what ?"
        sis "What do you mean, so what?"
        sis "So come and eat it."
        scene ep5_sc8_mcr_03
        off "Fuck."
        off "Did that bitch cook me breakfast?"
        off "That slut."
        off "She did it on purpose."
        off "She knew I wouldn't show for breakfast but she still cooked it so I would look bad for refusing it."
        off "If I join them I owe her, if I don't, I'm an asshole."
        off "She'll win either way."
        mc "I'm not hungry."
        sis "Really? You're always hungry..."
        mc "And today, I'm not, ok?"
        mc "Leave me alone."
        off "She seems to hesitate and stares at me for a few seconds before heading out."
        sis "Ok, it's your call..."
        mc "Yeah, my call."
        scene ep5_sc8_mcr_04
        off "That bitch got me."
        off "But I'll settle the score, I swear."

        jump ep5sc11


    elif ep4hateregrets == True:
        scene ep5_sc8_k_02 with dissolve
        off "[sf_name] is busy cooking when I enter the room."
        off "[sis_name] is nowhere to be seen."
        off "The greasy fragrance of bacon gently greats me."
        off "I can feel it coming."
        off "She hates me."
        mc "Hello, [sf_name]."
        off "She doesn't reply."
        off "She doesn't even move."
        off "She ignores me completely."
        off "What did you expect [mc_name]?"
        off "She won't buy my undercover bullshit tale."
        off "It's not a tale."
        off "It's hardly believable but it's not a tale."
        off "I'm so fucking dumb, I ruined everything."
        off "Yeah but she knows you're stupid."
        off "She may believe that you're actually dumb enough to have pulled off that bullshit with good intentions."
        off "Not a chance."
        off "What do you have to lose?"
        off "She already hates you."
        scene ep5_sc8_k_23
        mc "[sf_name]... I'm sorry about yesterday."
        mc "It was stupid."
        off "Still no reaction."
        off "This is going to be difficult."
        mc "[sf_name], please."
        mc "Can we talk?"
        sf "I don't want to talk to you."
        sf "You are disgusting and evil."
        off "Anger. No mistake there."
        off "I can't say I'm surprised."
        mc "I called them yesterday."
        mc "I know it was stupid."
        mc "I thought that maybe I could threaten them, scare them... so they would leave us alone..."
        mc "But... it didn't work out very well... things got out of hand."
        mc "So ... I tried something else... I know it's crazy... I got carried away..."
        mc "I told them that I would help them."
        mc "I thought that maybe I could... I don't know... go undercover..."
        mc "Take them from the inside..."
        off "She suddenly turns and comes closer to me."
        scene ep5_sc8_k_24
        sf "Are you kidding me?"
        sf "What are you talking about?"
        sf "You think this is some kind of tv show?"
        sf "Undercover?"
        sf "How could they even believe you if you threatened them first?"
        mc "I... told them that... I wanted to fuck her too."
        off "I can read the disgust on her face."
        scene ep5_sc8_k_25
        sf "What?"
        sf "Are you insane?"
        sf "Did you plan to rape her with them?"
        sf "Is that what I should understand?"
        mc "No!"
        mc "Absolutely not!"
        mc "I mean, yes, but no!"
        mc "Listen I .... Ok..."
        mc "I thought about it a couple times ok?"
        mc "Having sex with [sis_name] I mean, she's sexy, she's cute, she's hot."
        mc "I thought about it, every man would, but it doesn't go farther than that!"
        mc "I told them that because I wanted in, not to rape her, but to put an end to their scheme!"
        off "She looks at me completely baffled."
        scene ep5_sc8_k_26
        sf "Either this is the dumbest lie ever or you are the biggest idiot I ever encountered."
        sf "Who do you think you are?"
        sf "What did you hope to achieve by doing that?"
        sf "Are you the hero of an action movie or something like that?"
        sf "What do you think would have happened after you had delivered her to them?"
        sf "I can't believe it."
        sf "This is so stupid that it must be true."
        sf "You are an imbecile."
        sf "Oh my god."
        sf "Why do you have to be so stupid?"
        mc "Hey... I thought I was..."
        scene ep5_sc8_k_27
        sf "No, [mc_name]."
        sf "You didn't think at all."
        sf "Don't you understand that your idea was so dumb that it would have got us raped, and maybe killed?"
        sf "You included?"
        mc "We didn't go to the police so I thought that I had to do something..."
        sf "You cannot be serious."
        sf "You had to do something, I can't disagree with that."
        sf "But not put us all in danger!"
        sf "What do you think you could have done?"
        mc "I..."
        off "Of course, she's right."
        off "I know she's right."
        off "I'm so ashamed."
        mc "Ok, maybe I didn't think this through perfectly but..."
        sf "There's no but [mc_name], they would have killed us."
        off "She's right. I can't deny it."
        mc "I'm sorry."
        sf "Of course you are!"
        off "She sighs."
        scene ep5_sc8_k_28
        sf "[mc_name], I don't want to humiliate you or anything like that."
        sf "I'm sorry if my words are rude."
        sf "But you've really fucked up."
        sf "I'm sure you understand now."
        sf "But... if you have any more brilliant ideas about this situation, please, talk to me beforehand."
        sf "We need to agree on a way forward. Ok ?"
        off "It feels like I'm being scolded by Mom."
        off "It's weird."
        mc "Ok..."
        sf "Great."
        sf "Now... you don't have anything else to tell me about, do you ?"
        mc "Actually.... They called me this morning."
        mc "They... Want to meet."
        sf "Tell me that you didn't agree to meet them, [mc_name]..."
        mc "Well..."
        sf "You have to be kidding me..."
        mc "I didn't know how to answer."
        scene ep5_sc8_k_29
        off "She takes a step toward me and puts her hands on my chest."
        off "I suddenly feel like she actually cares about me."
        off "She seems really concerned."
        sf "Look at me, [mc_name]."
        sf "You are not going."
        sf "Do you understand me?"
        mc "Yeah, I ...."
        sf "You're so bad at lying that they will know that you're playing them."
        sf "They will kill you."
        mc "I know, I know."
        mc "I won't go."
        sf "I'm not joking."
        mc "I won't go."
        off "She stares at me in silence for a moment."
        $ ProcessStat(5, "sf_affection")
        $ DumpNotStack()
        sf "Good."
        sf "Why don't you sit down [mc_name], the breakfast is ready."


    elif ep4decisivetry == True:
        scene ep5_sc8_k_02 with dissolve
        off "[sf_name] is busy cooking when I enter the room."
        off "[sis_name] is nowhere to be seen."
        off "The greasy fragrance of bacon gently greats me."
        scene ep5_sc8_k_03
        off "She turns to me with a smile on her face."
        sf "Hello, [mc_name]."
        sf "I hope you slept well."
        sf "Are you hungry?"
        mc "I guess I am..."
        off "The table is already set."
        off "I would usually take my place and wait for my plate but..."
        off "I don't think it would be very polite..."
        sf "It's almost ready."
        sf "Can you serve the coffee?"
        sf "I'll bring you your plate in a moment."
        mc "Sure... Thank you, [sf_name]."
        sf "You're welcome, [mc_name]."
        scene ep5_sc8_k_17
        off "The coffee is hot and steaming."
        off "I just have to pour it."

        if ep4decisivefail == True:
            sf "So [mc_name]... What are you going to do now?"
            mc "Now? What do you mean?"
            sf "Well... You failed to convince her to stay yesterday, but I believe you learned a bit about yourself and the relationship you share with her."
            sf "The question is: will you go back to be the lowest of the assholes to her or will you try... to be a decent friend ?"
            off "Her question is pretty brutal."
            off "[sf_name] is a very straight forward girl."
            scene ep5_sc8_k_18
            mc "I... don't know... She didn't listen to me so..."
            sf "You didn't convince her but she listened."
            sf "You can build on it."
            mc "Really? I..."
            sf "Really."
            mc "Well... I'm okay with making an effort."
            mc "But she'll have to make some too."
            scene ep5_sc8_k_19
            sf "Come on, [mc_name]."
            sf "Let's cut the bullshit for a moment."
            sf "You know that she's already making an effort."
            sf "I think that you can be a nice guy, you just have that strange and absurd pride that makes you think that being kind to [sis_name] is like letting her mop the floor with your dignity."
            sf "And it's not like that, really."
            sf "She could use a friend who cares about her."
            sf "And caring about her won't make you less of a man, or whatever..."
            mc "But I do care about her."
            mc "She wouldn't anger me that much if I didn't give a shit about her."
            sf "Well, maybe if you tried showing her a bit more of your interest for her well being, maybe she'll try not to anger you so much."
            scene ep5_sc8_k_20
            mc "I... I guess I can try that."
            off "She smiles."
            sf "I think I've already told you, [mc_name], you're not a bad guy."
            sf "You may be a moron, but you're not a bad guy."
            sf "And you know... Even morons can be lovable."
            off "Is that supposed to be some kind of compliment?"
            mc "Ok..."

        if ep4decisivesuccess == True:
            sf "[sis_name] told me about your little meeting in the kitchen last night."
            off "She really tells her everything."
            scene ep5_sc8_k_18
            mc "I can't say I'm surprised."
            sf "I'm kind of proud of you [mc_name]."
            sf "In the end, you stood up for her."
            sf "And it looks like you've finally decided to step up as her friend."
            mc "Well, I gave my best at being an asshole but I guess I wasn't one hundred percent cut out for the job."
            mc "I thought that a change of career would be nice."
            sf "It can be nice indeed."
            scene ep5_sc8_k_19
            mc "And that doesn't mean I won't speak my mind when she pulls some bullshit move..."
            sf "She told me about it."
            sf "And that you may try to grope her ass from time to time."
            off "She laughs."
            off "I laugh too."
            mc "I'm glad I've been clear on that matter."
            sf "Thank you, [mc_name]."
            mc "What for?"
            sf "Well, it looks to me that you have chosen to be a decent human being and that you're actually motivated to take care of her."
            sf "And I thank you for that."
            scene ep5_sc8_k_20
            mc "Ok... You know... the way you talk about her is very strange sometimes."
            sf "Strange?"
            mc "I don't know..."
            mc "Like if you were more than friends."
            mc "Just now, you sounded like a mother... Or a lover."
            mc "Is there anything I should know?"
            scene ep5_sc8_k_21
            sf "Oh, no, [mc_name], we're not... I mean... [sis_name] and I... We're probably more than friends, yes, I can't deny that."
            sf "We share more with each other and care more for each other than friends would do."
            sf "But our relationship... I can't define it like that..."
            sf "We're not lovers."
            sf "But we're simply..."
            sf "She's everything I have."
            sf "And I believe I'm everything she has."
            sf "It's just what the last three years have made of us."
            mc "Honestly, I feel like I can't really understand it... but I think I'm jealous."
            sf "Jealous of me?"
            mc "Perhaps jealous of both."
            mc "I'm not sure yet."
            off "She looks at me in silence for a few seconds."
            sf "That's actually a very kind thing to say."
            sf "And I have the feeling that you're being honest."
            mc "I don't know what's gotten into me, sorry."
            mc "I won't do it again."
            scene ep5_sc8_k_22
            sf "Depending on how you rebuild your relationship with [sis_name], I may end up being jealous myself."
            mc "Of me?"
            sf "Maybe both."
            sf "I'm not sure either."
    else:


        scene ep5_sc8_k_02 with dissolve
        off "[sf_name] is busy cooking when I enter the room."
        off "[sis_name] is nowhere to be seen."
        off "The greasy fragrance of bacon gently greets me."
        mc "Hello, [sf_name]."
        scene ep5_sc8_k_03
        off "She turns to me with a smile on her face."
        sf "Hello, [mc_name]."
        sf "I hope you slept well."
        sf "Are you hungry?"


        if sis_love_path == True:
            off "I'm still not sure that she didn't notice my presence in [sis_name]'s room this morning."
            off "She may be toying with me."
            off "Actually, I wouldn't be surprised..."
            off "I have no idea how she would react."
            off "God, how more complicated can my life get?"

        mc "I'm always hungry for your breakfast."
        sf "Your compliments have improved. I have to congratulate you on that."
        mc "Thank you. I'm working hard on it."


        if sf_love_path == True:
            sf "I guess you deserve a reward for your efforts."
            scene ep5_sc8_k_04
            off "She slowly clings onto me."
            off "Her smile completely melts my heart."
            scene ep5_sc8_k_05
            off "I grab her body as her lips find mine."
            off "Our embraces get more intimate each time."
            off "Maybe I should refrain myself a bit."
            off "She doesn't seem to mind but I'm a bit afraid of ruining something by overdoing it."
            off "Ok, I'll refrain myself next time."
            off "Yeah, next time."
            scene ep5_sc8_k_06

            if ep4sflovelicked == True:
                sf "I wanted to apologize for last night."
                sf "I was very stressed and..."
                sf "I know that it probably ruined that moment for both of us..."
                scene ep5_sc8_k_07
                mc "You don't have to apologize."
                mc "I was stressed as hell too."
                mc "Next time maybe we should just trust each other and communicate a bit more."
                mc "I'm sure that everything will be alright."
                off "She lightly kisses me again before returning to the bacon."
                scene ep5_sc8_k_11
                sf "Thank you, [mc_name]."
                sf "I was afraid that you wouldn't understand and... well... Thank you."
                mc "You don't need to thank me."
                mc "It's just normal behaviour."
                mc "To be honest, I'm still wondering how you could think that I would rape you or anything like that..."
                sf "Oh my god, no!"
                sf "I never thought you would do that..."
                sf "That you could get upset, or even angry, yes."
                sf "But that you could do such a thing didn't even cross my mind."
                mc "Well, that's a relief."


            if ep4sflovetalked == True:
                sf "I wanted to thank you again for being so understanding last night."
                mc "You don't need to thank me, [sf_name]."
                sf "You know [mc_name], you make me feel... comfortable."
                sf "And safe."
                sf "The things I told you last night..."
                sf "I've never told anybody about that before."
                sf "Except for [sis_name], of course."
                scene ep5_sc8_k_07
                sf "I mean, I never imagined I would tell anybody about it to anyone but her."
                sf "I honestly don't understand how I've could come to trust you so much, and so fast, but..."
                sf "I don't know... I think... I've been told to be cautious..."
                sf "And I've always thought that I would follow what I've been taught... but..."
                sf "I'm doing it all wrong [mc_name], I feel like I can't control myself around you."
                scene ep5_sc8_k_08
                sf "I'm sorry... I think I love you, [mc_name]... "
                off "She blushes and looks away."
                off "Did she just say love?"
                off "Holy shit."
                off "Are things getting that serious?"
                off "Come on, moron, you wanted this."
                off "You love her too, don't you?"
                off "I guess I do..."
                off "Should I reply? What do I say?"

                menu:
                    "I love you too, [sf_name]. [sfLovePath]":
                        $ ep5sftruelove = True
                        $ ProcessStat(10, "sf_affection")
                        $ DumpNotStack()
                        scene ep5_sc8_k_09
                        off "That smile again."
                        off "The way she looks at me... It makes me feel good."
                        scene ep5_sc8_k_10
                        off "The feeling of that kiss is completely different."
                        off "I can't put this into words."
                        off "Something is happening."
                        off "Our tongues mingle with each other and exchange more than saliva."
                        off "I guess this is some kind of decisive moment."
                        off "The kiss lasts until she suddenly parts from me and rushes to the bacon."
                        scene ep5_sc8_k_11
                        sf "I've almost burned it!"
                        off "She lets out a light and happy laugh."
                        sf "[sis_name] won't forgive us if her bacon isn't edible."
                        mc "I guess it's my fault."
                        mc "I'll stop distracting you."
                    "I'll be there for you anytime.":

                        $ ProcessStat(-5, "sf_affection")
                        $ DumpNotStack()
                        off "I can feel her disappointment."
                        off "She looks at me for a couple of seconds before she turns away from me and goes back to the bacon."
                        scene ep5_sc8_k_11
                        off "These weren't the words she wanted to hear."
                        off "I feel bad."
                        off "Why did I say that?"

        if sf_dom_path == True:
            off "As always, I have no idea how to behave as she approaches me."
            scene ep5_sc8_k_12
            off "She sucks on her fingers and gazes over me with a very suggestive look."
            off "Fuck, she's hot."
            off "I'm still confused as hell about her putting her toy in my ass but damn, I know why I've accepted it in the first place."
            scene ep5_sc8_k_13
            off "She puts her fingers in my mouth and grips my face while her other hand grabs my crotch."
            off "She presses my balls and squeezes my dick."
            scene ep5_sc8_k_14
            off "I was expecting something like that but it's so sudden and forward that I'm still surprised."
            off "There is nothing sweet or gentle in that."
            off "It's brutal and a bit painful."
            off "I can't help but suck on her fingers."
            off "My dick gets hard."
            off "Am I enjoying this?"
            off "This is so confusing."
            scene ep5_sc8_k_15
            sf "I can see you're enjoying this, you horny dog."
            sf "More than I do myself."
            sf "Remember it."
            sf "When you behave, you're rewarded."
            scene ep5_sc8_k_16
            off "She brutally parts from me and goes back to the bacon."
            off "That was so strange."
            off "It felt different than yesterday."
            off "We probably took a step forward when she sodomized me..."
            off "I don't know if I like it or not..."

        sf "It's almost ready. You can sit. I'll bring you your plate."
        off "I take my place and wait patiently."

    scene black with dissolve
    off "A couple minutes later, breakfast is served."
    off "It smells delicious."
    scene ep5_sc8_k_30
    sis "Hey, guys."
    mc "Hey, [sis_name]."
    sf "Breakfast is served."
    sis "I can smell it."
    sis "I'm drooling."
    sis "Sorry to be late."
    sis "I was on the phone with your Mom."
    mc "Oh? How are they doing?"
    scene ep5_sc8_k_31
    sis "Their flight back is on hold and may be cancelled."
    mc "What? Why?"
    sis "Apparently there's a storm incoming or something like that."
    sis "They may delay their return a few days."
    mc "So... they won't be here on Saturday..."
    sis "Maybe on Sunday, they're not sure."
    sis "She told us to stay safe."
    scene ep5_sc8_k_32
    sf "It'll be okay."
    sf "It's just wind and rain."
    mc "I've seen the weathercast talking about that storm."
    mc "It'll be big but as long as we don't wander outside while it's upon us, we'll be ok."
    scene ep5_sc8_k_33
    sis "I'm not worried at all."
    sf "Are you sure?"
    sf "You don't look like it."
    mc "She's a bit afraid of storms."
    sis "No, I'm not!"
    sis "I've never been afraid of storms ok? Never."
    sis "It's just that... I don't like thunder."
    sf "I'm sure it's gonna be alright."
    sis "Of course."
    sis "As I said, I'm not worried at all."
    off "As breakfast goes by, my mind wanders away while they're blabbering."

    if ep4hateregrets == True:
        jump ep5sc9

    scene ep5_sc8_k_34

    if sis_love_path == True or sis_sub_path == True:
        off "That means at least one more night without the parents around here..."
        off "I should start thinking about how we'll deal with their return."
        off "Fooling around with [sis_name] while [sf_name] is sleeping is one thing..."
        off "Doing the same thing with Dad and Mom here is something else entirely..."
        off "Fucking [sis_name] in my bedroom while Mom is sleeping just across the hallway..."

        menu:
            "I'm getting hard just thinking about it. [gr]\[RiskyKink\]":
                $ ep5riskykink = True
                off "I know that's sick but..."
                off "The risk of being caught... makes it even more exciting..."
                off "To be honest I think I could even... understand Steve and his girl..."
                off "Doing it in risky places, or even showing ourselves..."
                off "Fuck, no, that's sick."
                off "Come on, just a second [mc_name]."
                off "Could you record yourself, fucking [sis_name], and send it to Steve?"
                off "No way... I mean... If she was asking for it perhaps, it would be hot... but otherwise..."
                off "No, that's stupid."
                off "What the hell am I fantasizing about?"
            "There's no way we take any risk...[gr]\[SafeKink\]":

                $ ep5safekink = True
                off "There's a sofa in the laundry room."
                off "Maybe we could discreetly do something with it..."
                off "I mean, the room is pretty clean, we could probably use it straight away..."
                off "It would be safer than meeting in our rooms..."
                off "Even now, It's probably a miracle that [sf_name] hasn't hear us..."
                off "We should consider it seriously..."
                off "Maybe I should invite [sis_name] to join me there tonight..."

        if ep5sftruelove == True:
            off "How come I..."
            off "I've just told [sf_name] that I love her and I'm focusing on finding a better solution to fuck [sis_name]."
            off "What is wrong with me?"
            off "Am I a creep or are all guys like me?"
            off "The worse thing about it is that I truly love her."
            off "I have actually no doubt about it..."
            off "That's [sis_name]..."
            off "She makes me crazy."
            off "She leaves me no choice."
            off "Every time I think of her, I lose track of everything else."

    elif ep4decisivetry == True:
        off "I can do it."
        off "I can be a decent friend."
        off "Let's be honest, I already feel better just taking this decision."
        off "We can talk to each other without drama."
        off "We can trust each other and forgive each others mistakes."
        off "And we can care for each other."
        off "That actually feels good."
        off "It was stupid of me."
        off "Letting go of the anger was the right decision to take."
        off "I should have done it sooner."

    scene ep5_sc8_k_35
    sis "[mc_name]? Are you listening ?"
    mc "What? Sorry, I was lost in my thoughts..."

    if ep4decisivetry == True:
        scene ep5_sc8_k_36
        sis "Why are you smiling?"
        mc "I'm smiling?"
        sf "You are."
        mc "I don't know..."
        sis "I bet you're thinking of something perverted again."
        mc "Why would you even think that?"
        sis "I don't know... Do 18-year-old guys even think about anything else but sex?"
        mc "Yes! Yes, we do very much!"
        sis "Hmm... ok... If you say so..."
        sf "Anyway... "

    scene ep5_sc8_k_37
    sf "[sis_name] and I were talking about maybe... Going out tonight."
    off "Are they kidding me?"
    mc "For all we know, those two guys may still be waiting for you outside..."
    sis "That's what we were talking about..."
    sis "We were supposed to have fun together this week and... because of this, we're not doing anything..."
    sis "We would be careful and also..."
    sis "Maybe you could come with us..."

    if ep4decisivetry == True:
        off "This is unexpected."
        off "She seems to have completely changed her view on the psycho twins."
        off "Which is very welcome."
        off "And they're willing to kind of rely on me?"
        off "I'm not gonna lie... It's flattering."
        off "And pleasing."
        off "I like it."
        off "I guess that [sf_name] finally convinced her..."
        off "That makes me wonder even more."
        off "If she has this kind of persuasive power over her, why didn't she use it sooner?"
        off "I'm not going to complain, though"

    scene ep5_sc8_k_38
    sf "And we're not going to stroll about the streets at night."
    sf "We're just thinking about going to a club, have a drink, dance a bit..."
    sis "They wouldn't do anything in public, would they?"
    sis "If you think we shouldn't... we won't do it... but..."
    off "What?"
    off "The decision is mine to take and they won't complain if I refuse?"
    off "It's hard to believe..."
    off "They really seem to need that breather, though..."
    mc "I'm already regretting it but... ok..."
    scene ep5_sc8_k_39
    off "[sf_name] candidly smiles while [sis_name] literally bursts with enthusiasm."
    off "It's suddenly obvious."
    off "[sis_name] is happy because she knows she'll get out of here and have some fun."
    scene ep5_sc8_k_40
    off "[sf_name], however, doesn't really care about going out."
    off "She only wanted to see [sis_name] happy."

    jump ep5sc10


label ep5sc9:
    scene black with dissolve
    with Pause(2)
    show text "An hour later."
    with Pause(2)


    $ moronic_hero_path = True

    scene ep5_sc9_mcr_01 with dissolve

    off "I can't stop thinking about it."
    off "[sf_name] may be right."
    off "They will see through it and they will kill me."
    off "Come on [mc_name]."
    off "They're rapists, not murderers."
    off "They are motherfucking psychos, that's what they are."
    off "If they learn that I'm setting them up they won't let me get away with it."
    off "The meeting is in a coffee shop downtown, there will be plenty of people in the streets, witnesses everywhere."
    off "If they figure anything they'll probably threaten you before fleeing, nothing more."
    off "They won't murder you in public."
    off "It's simple."
    off "You go there, you make them talk, you record them, then you go directly to the police and it's done."
    off "All your problems will be over."
    off "Think about it, [mc_name]."
    off "You've been an asshole."
    off "You've made mistake upon mistake."
    off "But you heard [sf_name]."
    scene ep5_sc9_mcr_02
    off "Despite you being the biggest idiot known to man, she's ready to forgive you."
    off "And I guess [sis_name] would too."
    off "But you need to show them that you deserve a second chance and that you're not just a moron."
    off "Prove to them that you're a man."
    off "I just go there."
    off "I make them talk."
    off "I record them."
    off "Then I go directly to the police."
    off "I can do that."
    off "It's my ticket for... Not being seen as an asshole anymore."
    off "It's my redemption."
    off "I can do it."
    off "Wait."
    off "What do I tell them?"
    off "Easy."
    off "You want to fuck the girls."
    off "You want to fuck every girl."
    off "Both."
    off "You just want to fuck them first."
    scene ep5_sc9_mcr_03
    off "[sf_name] is a bitch."
    off "She has to learn respect."
    off "Yeah, that will please them."
    off "She's the one who fucked their plans for good, yesterday."
    off "They'll want her to pay."
    off "Be angry with her."
    off "You're a guy, you deserve respect."
    off "That bitch must learn."
    off "Something like that."
    off "Ok ... I can do that."
    off "Ok. I need to go."
    off "I'll take the car."
    off "Do I say something to the girls?"
    off "No."
    off "If you say anything, [sf_name] will understand and she will forbid you to go."
    off "They're in [sis_name]'s bedroom, just don't make too much noise in the hallway and you'll be good."
    off "Maybe I should write something."
    off "Just in case I don't come back..."
    off "Like a suicide letter?"
    scene ep5_sc9_mcr_04
    off "Come on [mc_name], you will come back."
    off "They won't kill you."
    off "They won't even notice a thing."
    off "These guys may be psychos, but they're also morons."
    off "It's safe."
    off "Mostly."
    off "This is crazy."
    off "No."
    off "This is manning the fuck up."
    off "You're taking things in your own hands now."
    off "You're reliable."
    off "You protect [sis_name] and her lover, friend, or whatever she is."
    off "You're her friend for God's sake."
    off "Are you going to let these two motherfuckers ruin their life?"
    off "Ruin your life?"
    off "Do you want this redemption or what?"
    off "You know the police won't do a thing if you don't give them a good reason to."
    off "You have to do this if you want to protect your girls."
    off "You don't have a choice."
    off "I don't have a choice...."
    scene ep5_sc9_mcr_05
    off "Fuck it. I'm doing this."
    off "Let's go."

    jump ep5sc11


label ep5sc10:
    scene black with dissolve
    with Pause(2)
    show text "An hour later."
    with Pause(2)

    scene ep5_sc10_mcr_01 with dissolve
    off "The girls have withdrawn themselves into [sis_name]'s bedroom."
    off "I don't know what they had been doing in there but there were screams and waves of laughter for a while until it calmed down."
    off "In the meantime, I waste my time watching trailers and music videos on the web."
    scene ep5_sc10_mcr_02
    off "Holy shit!"
    off "Blackpink just released a new music video!"
    off "I have to see that immediately."
    off "Let's just put my headphones on."
    off "K-pop is my dirty little secret."
    off "I don't know how the girls would react to that... I mean..."
    off "It's not a very... manly music style... and they would probably end up mocking me and calling me a pervert."
    off "It's not like I'm listening to that just for the pretty girls who sing it..."
    off "Ok, that may be a perverted thing, I can't deny that..."
    scene ep5_sc10_mcr_03
    off "Here we go."
    off "Nice dresses..."
    off "I don't like this song much but..."
    off "Oh, Lisa..."
    off "I'm in love with your... dancing skills..."
    off "Those legs..."
    off "And that smile..."
    off "You're damn pretty, girl."
    scene ep5_sc10_mcr_04
    sf "Is this K-pop ?"
    mc "Holy fucking shit!"
    scene ep5_sc10_mcr_05
    off "I almost screamed that."
    off "I didn't hear her coming in."
    off "I close my laptop as if I was watching something shameful and remove my headphones."
    scene ep5_sc10_mcr_06
    mc "Holy crap, [sf_name], you almost gave me a heart attack!"
    sf "Sorry, [mc_name]."
    sf "I didn't want to startle you so much."
    mc "It's ok, you just... Took me off guard..."
    sf "Am I bothering you?"


    if sf_dom_path == True:
        mc "No! No of course not!"
        sf "Good."
        sf "[sis_name] is having... an intimate moment with her diary."
        sf "I thought we could use this time to talk a bit."
        mc "Ok... sure... What do you want to talk about?"
        off "She goes around me and removes a blanket and cushion before she sits on the other side of the sofa."
        scene ep5_sc10_mcr_07
        sf "You see, [mc_name], I think that our relationship can't work properly without absolute trust between you and me."
        off "Why do I have the feeling that this won't be a pleasant conversation?"
        off "She's going to punish me for something."
        off "I can sense it coming."
        sf "Move that laptop away, [mc_name]."
        sf "I'm going to put my legs there."
        off "I comply and she immediately claims my lap as hers."
        scene ep5_sc10_mcr_08
        off "One of her feet gently rubs against my cock."
        off "She knows what she's doing."
        off "She looks at me in silence for a few seconds."
        sf "My legs are a bit heavy."
        sf "I guess you know what to do."
        off "No."
        off "I have no idea what to do."
        off "I can only make a supposition."
        off "I'm going to massage her legs to the best of my limited abilities..."
        off "... But I'm pretty sure that at some point she will find some pretext to crush my crotch and fuck my ass with a cucumber or something like that."

        if ep4willingsodom == True:
            off "I'm not sure I really mind, though."
            off "As disturbing and confusing as it is..."
            off "I may even find some pleasure in that..."

        off "And her legs..."
        off "Fuck, I would lick these legs."
        label galleryScene10:
        scene ep5_sc10_mcr_09
        off "I slowly let my left-hand slide on her thigh and my right one on her calve."
        off "It's more of a caress than a massage."
        off "My dick hardens under her feet."
        scene ep5_sc10_mcr_10




        if sis_sub_path == False and sis_love_path == False:



            sf "I'm a bit worried that you may not trust me."
            sf "I feel like you're afraid of me."
            sf "When we are alone, together..."
            sf "Do you fear me, [mc_name]?"
            off "I think I kind of do... But I can't tell you that, can I?"
            mc "I do not fear you. But sometimes your reactions... surprise me."
            sf "That I can understand."
            sf "I want you to know that whatever I do, [mc_name], I do it to please you."


            if ep4willingsodom == True:
                off "Well, that was kind of pleasant but..."
                off "I'm still not sure that I liked it..."
            else:

                off "Sure."
                off "Getting my ass raped was a real pleasure."
                off "Girl, I promise you, when I'll finally get inside you, I'll fucking destroy your pussy."

            sf "Do you believe me, [mc_name]?"
            mc "Of course. I trust you."
            sf "Good."
            off "She takes back her legs."
            sf "Remove your clothes."
            off "Here we go."
            scene ep5_sc10_mcr_38
            off "A couple of days ago I would have gladly get naked, foolishly hoping to get sucked dry or something like that."
            off "Today I obey without discussion but I'm full of apprehension."
            off "She makes me sit back on the sofa and comes closer to me."
            off "She takes hold on my boner with her left hand."
            scene ep5_sc10_mcr_39
            off "I was already half-erect but all she needed was a light touch to make me rock hard."
            off "Her other hand grabs my head and pushes it against hers."
            off "She slowly starts working on my shaft."
            off "She's surprisingly gentle."
            off "I can feel her breathing on my neck and her breasts pressing against my arm."
            off "This isn't like anything we had done the previous time."
            off "She's really taking care of me."
            off "This isn't a punishment."
            off "It's something else and I like it."
            off "She whispers."
            scene ep5_sc10_mcr_41
            sf "Do you enjoy this, [mc_name]?"
            mc "I do, yes."
            off "I'm panting."
            off "I don't think she could be in any doubt how much I really enjoy this."
            sf "I enjoy it too, [mc_name]."
            sf "If you like it, I like it too."
            off "Oh god."
            off "I'm not gonna last long."
            sf "I want you to think about last night."
            sf "I want you to remember when I inserted that toy into you."
            scene ep5_sc10_mcr_40
            off "Oh, crap."
            sf "Tell me, how did it feel at first?"
            sf "Did it hurt?"

            menu:
                "Yes! It did hurt a lot!":
                    $ ep5hurtalot = True

                "It did hurt a bit, yes... [sfDomPath]" if ep4willingsodom == True:
                    $ ep5hurtabit = True;
                    $ ProcessStat(1, "sf_dominance")
                    $ DumpNotStack()

            scene ep5_sc10_mcr_41
            sf "I'm sorry to hear that, [mc_name]."
            sf "I never wanted to hurt you."
            sf "When I was slowly going in and out of you, I felt like you were having some pleasure."
            sf "But maybe I was wrong."
            sf "Like you, I don't have any experience."
            sf "I'm trying things."
            scene ep5_sc10_mcr_43
            off "Holy shit."
            off "That can't be her first handjob."
            off "My dick is throbbing in her hand."
            sf "Don't you want to try those things with me, [mc_name]?"
            off "Her voice."
            off "It's not the usual strong and unwavering command."
            off "It's more like a sensible and fragile pleading."
            off "I don't know what the fuck is happening... but I can't deny that I like it."

            menu:

                "How can I refuse ? [sfDomPath]" if ep5hurtabit == True:
                    $ ProcessStat(2, "sf_dominance")
                    $ DumpNotStack()
                    $ ep5cantrefuse = True
                    sf "I promise you, [mc_name], I will try my best to give you as much pleasure as you can take."
                "I don't know...":

                    sf "I promise you, [mc_name]. It'll be worth it."

            scene ep5_sc10_mcr_44
            off "She's breathing heavily."
            off "This is actually the first time that I've seen her genuinely horny."
            off "My cock drools so much precum that I'm completely drenched."
            off "Her hand slides on my shaft like it belongs to her."
            off "She probably thinks it does."
            off "I'm losing my mind."
            scene ep5_sc10_mcr_42
            sf "So... [mc_name]... be honest."
            sf "Did you like it, last night?"
            sf "When I was inside you?"
            sf "You can tell me."
            sf "Nobody else will know."

            if ep4willingsodom == True:
                off "Oh, god, I don't even know!"
                off "I don't even fucking know if I liked it or not!"
                off "I'm still dealing with the shame of having taken it in the ass."
                off "It felt good, but did I like it?"


            menu:
                "Yes. I liked it. [sfDomPath]" if ep5cantrefuse == True:
                    $ ep5totaldom = True
                    scene ep5_sc10_mcr_45
                    off "Did I really say that?"
                    off "Holy shit."
                    sf "Oh [mc_name], that makes me so happy."
                    off "Her grasp on my dick gets firmer."
                    off "She wants to make me come."
                    sf "Tonight it will be bigger."
                    sf "Do you think you will enjoy it even more?"
                    off "Bigger... shit."
                    off "I don't know if I can take it..."
                    mc "I don't know..."
                    scene ep5_sc10_mcr_41
                    sf "But you will take it, won't you?"
                    sf "You will take it all."
                    mc "Yes..."
                    scene ep5_sc10_mcr_42
                    off "I can't believe I'm saying this."
                    off "It's like her pumping on my dick is squeezing answers out of me."
                    off "Answers I didn't even know I had in me."
                    sf "Do you think I will like it too, [mc_name]?"
                    sf "When you will penetrate me?"
                    sf "Do you think that I will enjoy feeling you inside me?"
                    sf "I hope you will be gentle."
                    sf "My pussy is burning, right now..."
                    sf "I can't wait."
                    sf "Will you be gentle [mc_name]?"
                    mc "YES! I'll be GENTLEEEEEE!"
                    scene ep5_sc10_mcr_46
                    off "I ejaculate as I try to answer her question without yelling."
                    off "It feels like she extracted some truth from me alongside my cum."
                    off "The pleasure leaves me completely devoid of any strength."
                    off "I can't move a finger."
                    sf "You seemed to enjoy that, [mc_name]."
                    sf "That makes me happy."
                    off "She quickly parts from me and heads to the door."
                    scene ep5_sc10_mcr_47
                    sf "I'm counting on you, [mc_name]."
                    sf "Tonight will be spectacular."
                    off "Spectacular."
                    off "Holy shit."
                    scene ep5_sc10_mcr_48
                    off "That girl can do whatever she wants with me."
                    off "I can't refuse her anything."
                    off "How has it come to that?"

                "No. I'm sorry. I didn't like it." if ep5cantrefuse == False:
                    $ ep5sorrydom = True
                    sf "I'm so sorry, [mc_name]."
                    scene ep5_sc10_mcr_42
                    sf "Does that mean you want us to stop?"
                    mc "I don't know I..."
                    sf "It's too late for uncertainty, [mc_name]."
                    sf "I gave you several opportunities to walk away from this."
                    sf "It's too late now."
                    sf "You belong to me."
                    off "What?"
                    sf "I can do whatever I want with you."
                    sf "And I will."
                    mc "[sf_name], I..."
                    sf "Shhhhh."
                    off "I'm not a thing."
                    off "I'm a human being!"
                    sf "Tonight will be different."
                    sf "You will like it."
                    off "She suddenly parts from me."
                    scene ep5_sc10_mcr_47
                    sf "I'll go back to [sis_name] now."
                    sf "You can finish yourself."
                    off "She's back to her assertive attitude."
                    off "I'm confused as fuck."
                    off "I try to find something to say."
                    off "I know I should protest, but I look at her leaving the room without saying a word."
                    scene ep5_sc10_mcr_49
                    off "What just happened?"
                    off "I belong to her?"
                    off "Do I want to finish myself?"
                    off "What will happen tonight?"
                    off "I feel like I've been played with once again."
            $ renpy.end_replay()
        else:




            sf "Great."
            sf "Of course, I understand that there are some things that you may want to keep for yourself."
            sf "Be it because you're afraid of my reaction, or because you are ashamed."
            sf "Maybe you're even afraid of hurting me and you want to avoid that."
            sf "That would be very considerate and kind of you."
            sf "However, what is really hurting me is the fact that you're keeping it from me."
            scene ep5_sc10_mcr_11
            sf "You don't trust me enough to tell me the truth."
            sf "If we have a problem, we cannot resolve it if you keep it to yourself."
            sf "Do you understand?"
            off "That sounds very patronizing."
            off "I'm not sure I care."
            off "Her skin is soft."
            off "She feels fresh under my touch."
            mc "Yes, I understand."
            sf "Good."
            sf "Do you trust me, [mc_name]?"
            mc "I do."
            sf "Will you tell me the truth then?"
            mc "I will..."
            scene ep5_sc10_mcr_12
            sf "Be careful [mc_name]."
            sf "You know that I don't like lies and liars."
            sf "You'd better think carefully."
            off "Her tone turns as cold as ice."
            off "This is a warning."
            off "And a very serious one."
            off "Behave or be punished."
            off "Obviously, she already knows something... and if I don't confess the right thing..."
            off "My blood runs cold."
            off "This is about [sis_name]."
            off "She knows."
            off "I'm fucked."
            off "Tremendously fucked."
            off "She's going to destroy me."
            off "She's going to destroy us."
            off "If she tells anyone about us, it will completely ruin our lives."
            off "Fuck."
            off "What are my options here?"
            off "Can I lie?"
            off "Do I pretend I don't know what she's talking about?"
            off "That would be foolish."
            off "Obviously, she knows."

            if sis_love_path == True:
                off "Maybe she heard me in [sis_name]'s bedroom this morning."
                off "Discretion isn't my forte."
                off "She probably noticed me."
            if sis_sub_path == True:
                off "Maybe she saw us."
                off "Or heard us."
                off "We got pretty vocal last night."
                off "Shit, I was careless."
                off "I should have known it would end this way."


            if sis_love_path == True or sis_sub_love_path == True:
                off "I don't have a choice."
                off "I have to confess."
                off "Is there a chance that she will understand?"
                off "If there's something I can be sure about [sf_name] is that she deeply cares about [sis_name]..."
                mc "I'm... having a thing with... [sis_name]."
                off "She seems totally unphased."
                off "As I thought."
                off "She knows."
                sf "A thing."
                sf "That's how you call it."
                sf "Alright, [mc_name]."
                sf "Tell me more about this thing you're having with [sis_name]."
                sf "Do you fuck her?"
                off "She seems calm and composed."
                off "She doesn't even seem bothered."
                off "It's like she just inquires about an insignificant matter."
                mc "No! We haven't.."
                sf "You haven't done it... yet."
                off "I may as well be completely honest about it."
                off "Do I have anything to lose at this point?"
                off "Fucked for fucked..."
                mc "I love her."
                mc "And she loves me."
                scene ep5_sc10_mcr_13
                sf "Ah. Love."
                sf "That's so sweet."
                sf "Should I be jealous?"
                off "I have no idea what to say."
                off "This situation is so messed up."
                off "Does [sf_name] love me?"
                off "At least a bit?"
                off "Does she even want to be loved?"
                off "I thought she wasn't interested in that kind of relationship but... maybe I'm wrong?"
                off "Our partnership is so special that I never saw it as a real romantic relationship."
                off "But maybe she sees it differently."
                mc "I don't know..."
                mc "You're the only one who can answer that question."
                off "Her attitude suddenly changes."
                off "In an instant, she grabs my hand and locks me with her legs."
                scene ep5_sc10_mcr_14
                off "She puts a foot on my neck and applies some pressure."
                off "I'm completely at her mercy."
                off "She's not the same person anymore."
                off "She's incredibly strong and determined."
                off "I feel like she could kill me in a heartbeat."
                off "I'm not even sure she would really mind it."
                sf "Listen to me carefully, [mc_name]."
                scene ep5_sc10_mcr_15
                off "Her voice is cold, calm, precise."
                off "She's confident, determined, resolute."
                sf "Are you abusing her?"
                sf "I want you to think about it very carefully."
                sf "Are you sure she's completely consenting to that thing with you?"
                sf "If not, I'm willing to give you one chance to walk away from this."
                sf "But if you lie to me and hurt her or take advantage of her in any way, I will hurt you so much that you will regret being born."
                sf "Do you understand?"
                scene ep5_sc10_mcr_16
                off "Her foot impedes me."
                off "I can barely nod a yes."
                sf "Are you abusing her?"
                mc "No. I'm not doing anything like that."
                mc "I love her, and she loves me."
                mc "She wants it as much as I do."
                scene ep5_sc10_mcr_17
                off "She looks at me for a few seconds, weighing my words."
                off "Her foot still on my throat, she tries to decide if I can be trusted."
                off "When she finally releases me, my neck and my arms hurt like hell."
                scene ep5_sc10_mcr_18
                sf "I'll believe you for now, but remember my warning, [mc_name]."
                sf "If you hurt her, I won't let you get away with it."
                sf "I hope I made myself clear."
                sf "If you force yourself on her, in any way."
                sf "I will break your neck."
                mc "Fine by me..."
                mc "I don't intend on hurting her, ever..."
                off "This girl is crazy."
                off "She was ready to cripple me, or worse."
                off "A new silence."
                off "I don't know what she's waiting for."
                off "It's awkward."
                off "She stares at me the whole time before looking away as she talks again."
                off "Her anger seems to have completely vanished."
                scene ep5_sc10_mcr_19
                sf "She's your father's ward."
                sf "You don't have a problem with that?"
                off "That's very strange."
                off "What just happened was definitely motivated by her concern for [sis_name]'s well being."
                off "But her mood changed in an instant."
                off "Her tone... her tone isn't judgmental at all."
                off "This question is motivated by some kind of... jealousy?"
                off "Just a minute ago, she was ready to kill me, and now..."
                off "It's like she shows me a more sensible and fragile face of her personality."
                off "I'm completely lost."
                scene ep5_sc10_mcr_20
                mc "It was... weird at first but... I don't know how to explain it."
                mc "I don't have a problem with it, because... it's also because she's like a sister to me."
                mc "We're like... Attracted to each other."
                mc "I know it doesn't make sense..."
                off "She looks... Sad?"
                off "I can't be sure."
                off "[sf_name] is unreadable."
                off "I have no idea what she really thinks."
                off "[sis_name]'s voice sounds through the door."
                off "She yells in the hallway."
                sis "[sf_name]?"
                scene ep5_sc10_mcr_21
                off "She stands up and heads for the door."
                sf "You were better with your hands last time you massaged my feet."
                sf "Work on that."
                off "I barely have the time to realize that she has already left my room."
                off "It's so weird."
                off "I don't know what to think about what happened."
                scene ep5_sc10_mcr_22
                off "Obviously, there will be consequences."
                off "I don't think she'll go telling anyone."
                off "I'm not even sure she'll talk about it with [sis_name]."
                off "There's something going on."
                off "Something I can't put my finger on."
                off "The only thing I'm sure is that she'll rip my ass open tonight if I let her do me..."

            if sis_sub_path == True and sis_sub_love_path == False:

                off "Crap."
                off "What do I do?"
                off "Will she understand?"
                off "I'm merely playing with [sis_name] the same way [sf_name] is playing with me."
                off "That at least I'm sure she will understand."
                off "However... I'm not sure that it will please her..."
                off "If there's something I can be sure about [sf_name] is that she deeply cares about [sis_name]."
                off "Calm down, [mc_name]."
                off "You don't know what she's talking about."
                off "Perhaps all of this is just one of her games."
                off "She doesn't know anything."
                off "She just wants to mess with you."
                off "This is just a test to trick you into saying something."
                off "Keep cool [mc_name]."
                off "You just don't know what she's talking about."
                scene ep5_sc10_mcr_23
                mc "I don't know what you're talking about..."
                mc "Have I done something that displeased you?"
                sf "Yes, you have."
                sf "If that is the way you want to play it, [mc_name]..."
                sf "I'm very disappointed in you."
                sf "There will be consequences."
                off "Here we go with the threats."
                mc "I'm sorry my lady, I don't understand."
                mc "I can't make amends if I don't know how I failed."
                scene ep5_sc10_mcr_24
                sf "You know exactly what you have done, [mc_name]."
                sf "It's too late now, you have chosen to lie."
                sf "I'll have to take action."
                sf "We'll see about that tonight."
                sf "Our meeting will be intense, I can tell you that."
                off "Intense."
                off "Great."
                off "She pushes me away and stands up."
                scene ep5_sc10_mcr_25
                sf "Do you have any idea what you're doing?"
                sf "This is nothing like the time you massaged my feet."
                sf "Yet another disappointment."
                mc "I... I'm sorry."
                mc "I'm doing my best."
                sf "And obviously this isn't enough."
                sf "You'll have to do better than that if you want to please me."
                sf "Or maybe you don't want to please me anymore?"
                mc "I apologize."
                mc "I'll do better next time."
                sf "Yes, you will."
                off "[sis_name]'s voice sounds through the door."
                off "She yells in the hallway."
                sis "[sf_name]?"
                off "She heads for the door."
                scene ep5_sc10_mcr_21
                sf "We'll pursue this discussion later, [mc_name]."
                sf "You should reflect on your actions."
                scene ep5_sc10_mcr_22
                off "That was so strange."
                off "Why does it always have to be so weird with her?"
                off "And I have no idea if she's really aware of something or if she was just toying with me."
                off "The only thing I'm sure is that she'll rip my ass open tonight if I let her do me..."
    else:

        mc "Bothering me? No!"
        mc "Of course not, [sf_name]."
        mc "You never bother me."
        sf "Great... Can I join you?"
        sf "[sis_name] wanted some privacy so she could write something down in her diary."
        sf "I thought we could just... Hang out a bit..."

        if ep5sftruelove == True:
            sf "You know... Like... Lovers do..."
            off "Lovers."
            off "That sounds nice."

        mc "I like this idea."
        mc "Do you want to do something in particular?"


        if sf_love_path == True:
            sf "I'll just sit there with you if you don't mind..."
            sf "I just want to spend some time with you..."
            sf "But I don't want to interrupt anything..."
        else:

            sf "I don't know."
            sf "I thought we could chat."
            sf "About anything..."
            sf "But I don't want to interrupt anything..."

        mc "No [sf_name], you're not interrupting anything."
        mc "Come here."
        off "I quickly remove blanket and cushion so she can sit comfortably."
        scene ep5_sc10_mcr_26
        off "She smiles and happily joins me on the sofa, sitting very close to me."
        sf "So... you like K-Pop ?"
        mc "Well... from time to time..."
        sf "Will you show me that music video ?"
        mc "... Sure..."
        off "This is a bit humiliating."
        off "What will she think of me after that?"
        scene ep5_sc10_mcr_27
        sf "These girls are pretty."
        off "Well, I can't deny that..."
        mc "You think so ?"
        sf "They have some serious dancing moves."
        sf "You don't see that kind of performance in our Pop music."
        mc "That's... true I guess."
        sf "I like the beat too."
        sf "It really makes you want to move your body."
        off "I can't believe it."
        off "She's not making fun of me, she's genuinely interested."
        sf "This girl here, have you seen her legs?"
        scene ep5_sc10_mcr_28
        sf "Oh my god, these legs."
        sf "I would kill to have these legs."
        mc "Are you serious?"
        mc "You have nothing to envy them."
        mc "Your legs are perfect."
        off "She lets out a little laugh."
        sf "That's very kind of you, [mc_name]."
        sf "But I know the truth."
        mc "The truth? What truth?"
        sf "I'm fat."
        sf "I know it."
        sf "I accepted it."
        mc "What?"
        mc "What are you talking about?"
        scene ep5_sc10_mcr_29
        sf "Didn't we already have a similar discussion?"
        sf "I know I'll never be as fit as these girls."
        sf "I've struggled with that a lot, in the past, but it's no big deal anymore."
        sf "I've come to peace with it."
        sf "I manage to keep my ass in check and it's good enough."
        mc "You have to be kidding me."
        mc "I can't let you say that."
        mc "It's simply not true."
        mc "Your ass his perfect, [sf_name]."
        mc "And so are your legs."
        mc "And so is the whole you, ok?"
        mc "Why do you think that every guy is looking at you when you set foot outside?"
        sf "They're ogling [sis_name], not me."
        sf "And if they still happen to look at me..."
        sf "It's probably because all men are perverted dorks who drool over any feminine body."
        mc "What? No !"
        mc "I mean ... Ok, maybe we all are perverted dorks, I can't honestly disagree with that."
        mc "But I can assure you that they're looking at you because you're beautiful."
        mc "Only a fool would think that you're fat or anything like that."
        off "She smiles."
        scene ep5_sc10_mcr_30
        sf "You don't have to lie, [mc_name]."
        sf "I told you I came to peace with it."
        mc "I'm not lying, [sf_name]."
        mc "Ok, listen."
        mc "This is going to sound weird but..."
        mc "I absolutely love your ass."
        mc "I love your legs too."
        mc "I also love your breasts."
        mc "I love everything about you."
        mc "You are perfect, ok ?"
        off "That's embarrassing."
        off "That sounded way better in my head."
        off "She's going to think that I'm a pervert."
        off "She has a weird smirk."
        sf "Ok... this is a very weird confession, but somehow very... empowering."
        sf "Thank you, [mc_name]."
        mc "Anytime..."

        if ep5sftruelove == False:
            scene ep5_sc10_mcr_31
            off "She kisses me on the cheek before getting away from me."
            $ ProcessStat(5, "sf_affection")
            $ DumpNotStack()
            sf "I'll go back to [sis_name] now."
            sf "I want to avoid the natural awkward silence that comes after such a confession."
            sf "Also, I have to tell her that you love my ass."
            sf "I'm sure she'll be pleased."
            off "She sounds mischievous and joyful."
            off "And I'm sure she'll go straight to [sis_name] and tell her what happened."
            scene ep5_sc10_mcr_32
            mc "Ok..."
            sf "See you later [mc_name]."
            mc "See you later [sf_name]..."
            off "She laughs while exiting my room."
            off "A pure, crystalline laugh."
            off "She sounds happy."
        else:


            scene ep5_sc10_mcr_31
            off "She kisses me on the cheek before slowly whispering into my ear."
            sf "You should put the laptop away."
            off "No need to tell me that twice."
            off "I discard my laptop a bit too roughly for my comfort but I don’t really care."
            off "[sf_name] immediately sits on my lap and kisses me."
            scene ep5_sc10_mcr_33
            off "She grabs my head while her tongue meets mine."
            off "I can feel her breasts pressing against my chest."
            off "My hands initially find her hips as I still try not to frighten her by groping her too much..."
            off "But to hell with caring."
            off "Her ass is there."
            off "My right-hand grabs it."
            scene ep5_sc10_mcr_34
            off "I want her."
            off "She knows it as well and doesn’t seem to mind."
            off "Maybe I should go further?"
            off "I’m about to grab one of her breasts when our lips part ways."
            scene ep5_sc10_mcr_35
            sf "[mc_name], I don’t want to... Pressure you or anything like that..."
            sf "This morning when I confessed..."
            sf "I hope you didn’t feel compelled to reply..."
            sf "I mean... I’m probably going a little too fast."
            sf "We should slow down."
            off "Why does it hurt a bit when she says that?"
            off "Does she have some second thoughts?"
            off "Maybe I wasn’t clear this morning?"
            mc "I love you."
            mc "I don’t have to think about it."
            mc "I didn’t feel compelled in any way."
            mc "We can still slow down if you want to..."
            mc "I don’t want to pressure you into something you’re not ready for either."
            scene ep5_sc10_mcr_36
            off "She smiles."
            off "She’s literally sparkling with happiness."
            sf "I like the pace we’re going at."
            off "I have a feeling that things are about to get intense when [sis_name]’s voice sounds through the door."
            off "She yells in the hallway."
            sis "[sf_name]?"
            off "[sf_name] lightly kisses me before she gets away from me and stands up."
            scene ep5_sc10_mcr_37
            sf "I should go."
            sf "We’ll pursue this conversation later if you don’t mind."
            mc "I’m looking forward to it."
            sf "I bet you are."
            off "She laughs while exiting the room."
            off "A pure, crystalline laugh."
            off "She looks happy."
            off "And her happiness is so true and bright that it lights up life itself around her."
            off "There's no mistake."
            off "I love her."

    jump ep5sc14


label ep5sc11:
    scene black with dissolve
    with Pause(2)

    if moronic_hero_path == True:
        scene ep5_sc11_cof_01
    else:
        scene ep5_sc11_cof_01_anger

    if ep3breakfastfailed == False:
        off "Meeting them here is very ironic."

    off "The psycho twins are already here."
    scene ep5_sc11_cof_02
    off "And aside from them and the barista, the Coffee Shop is completely empty."
    off "Great."

    if moronic_hero_path == True:
        off "It's okay, [mc_name]."
        off "You've already gone through all this multiple times on your way here."
        off "Your phone is recording."
        off "You meet them, you act like you're angry at [sf_name], like you want to give her a lesson."
        off "They tell you their plan, you ask them why they're doing it but don't push it too far."
        off "Once you're done, you keep cool, you leave and head directly to the police."
        off "That will work just fine."
        off "Don't worry."
        scene ep5_sc11_cof_03
        lk "Hello, [mc_name]."
        mc "Guys."
        lk "I'm glad you came. Ray was sure you wouldn't."
        ry "I thought you would chicken out."
        mc "Why are you even here then?"
        off "Because they don't have a choice, [mc_name]."
        off "You're their only chance to get to the girls."
        lk "To meet a new friend, of course."
        lk "Sit with us, [mc_name]."
        lk "I think we have several things to discuss."
        off "Don't sweat it, get into your role."
        off "You're an asshole who wants to rape his childhood friend and her lover."
        off "As disgusting as that sounds, you can do it."
        mc "So, what do you have in mind ?"
        lk "Straight to the point, I see..."
        off "You're going too fast, [mc_name]."
        off "Be careful."
        mc "We don't have much time."
        mc "If the girls found out I'm gone with the car, they may get curious."
        lk "And we don't want that."
        lk "You're right."
        lk "Tell me, [mc_name], how motivated are you ?"
        scene ep5_sc11_cof_04
        off "Motivated?"
        off "Are they already beginning to doubt me?"
        off "Don't panic, [mc_name]."
        off "You need to make an impression."
        off "Show them you have a pair."
        off "You make one big statement to assert dominance and it'll be fine."
        off "You can do this."
        off "Let's start by banging our fists on the table..."
        mc "Motivated? What is this?"
        mc "A god damn job interview or what?"
        off "Ok, you're too loud, [mc_name]."
        off "Tone down."
        scene ep5_sc11_cof_05
        mc "You told me to come here to listen to this bullshit?"
        mc "What the fuck do you expect me to tell you?"
        mc "I want to fuck [sis_name], ok?"
        mc "I want to fuck them both."
        mc "And I want to teach [sf_name] a lesson."
        mc "That lesbian cunt stole my friend from me and made a fool out of me."
        mc "She has to pay."
        mc "If it's not enough for you, then why the fuck did you make me come here?"
        off "Will they buy it?"
        off "I hope I didn't go too far..."
        off "They actually look surprised... and a bit afraid..."
        lk "Ok, [mc_name]. You need to calm down."
        lk "We don't want to draw any unwanted attention."
        lk "That was just small talk."
        lk "We're not doubting your motivations."
        scene ep5_sc11_cof_06
        off "Small talk, for sure."
        off "He was trying to get the upper hand and he failed."
        off "Goddamnit, [mc_name]."
        off "That was some genius acting."
        off "Keep it up."
        off "You're the boss now."
        off "Show them."
        mc "Yeah, you better not doubt me."
        mc "As far as I can see, I'm the only one here who has come clean about what and why."
        mc "If anyone, I'm the one who should doubt you."
        mc "How do I know you're not going to chicken out of this if it gets ugly?"
        lk "Ugly?"
        lk "We sure hope it won't get ugly."
        off "They look at each other."
        scene ep5_sc11_cof_07
        off "Luke is searching for some kind of approval."
        lk "It's a long story, [mc_name]. Are you sure you want to hear it?"
        off "Is he going to tell me why they're doing this?"
        off "Crap, it's been far easier than I thought it would be."
        off "I'm truly good at this."
        off "Maybe I should make a living out of it?"
        off "Holy shit, Steve won't believe me when I tell him."
        mc "How can I trust you without hearing it ?"
        off "He suddenly looks humbler."
        scene ep5_sc11_cof_08
        lk "I guess you're right."
        lk "So ... I should start by telling you that we don't care about [sis_name]."
        lk "We want her friend."
        lk "She was just a means to an end."
        off "Ok. Don't show them you're surprised."
        mc "You're after [sf_name]."
        mc "Ok. Why ?"
        off "It's ok, you have the tone right."
        off "Confident, authoritative..."
        off "Just don't push it too far."
        lk "Her father ruined our lives so we decide to ruin his."
        scene ep5_sc11_cof_09
        lk "We've been told that his daughter was the only thing that had any value in his eyes so..."
        lk "Here we are."
        mc "That's a bit short."
        mc "What did he do to you?"
        ry "He killed our parents, ok?"
        scene ep5_sc11_cof_10
        ry "Is that enough for you ?"
        off "What the hell is this about?"
        off "I thought that [sf_name]'s father was some kind of businessman or something like that..."
        lk "Ray, please, let me do the talking."
        lk "You've probably already heard of Knave Structured."
        lk "It's a big countrywide company who has its roots in this city."
        mc "Sure. What about it?"
        lk "Three years ago, our father was an employee of this company."
        lk "He had been for twenty years."
        lk "At that time, the company had some problems."
        lk "Serious losses, money problems, angry shareholders."
        lk "I don't know the details but you get the idea."
        lk "To solve these problems, they hired a man."
        scene ep5_sc11_cof_11
        lk "Mr. Carter."
        off "[sf_name]'s father..."
        off "So it's a work-related problem?"
        lk "The first thing he did was to lay off half of the workforce of the company."
        lk "But not only that."
        lk "He also managed to rob them of all their redundancy pay."
        lk "He sent them packing with the bare minimum."
        lk "Our father was amongst them."
        off "[sf_name]'s dad fired their father."
        off "I guess that can be a source of tension but to that extent?"
        lk "After that... He never managed to find an equivalent position."
        scene ep5_sc11_cof_12
        lk "He's had a series of menial, degrading, low-paying jobs."
        lk "When our mother got sick a year later, he didn't have the means to get her a decent medical care."
        lk "Her agony lasted several weeks."
        lk "It was painful."
        off "Ah, crap. That's some depressing shit..."
        lk "Our father didn't survive our mom very long."
        lk "He committed suicide 6 months later."
        lk "Ray found him in his garage."
        off "And here we are."
        off "Both parents are dead and as they can't cope with the loss, they need someone to blame."
        off "[sf_name]'s father is the ideal culprit."
        mc "I'm sorry for your loss."
        lk "Thank you, [mc_name]."
        mc "But... How does raping [sf_name] avenge your parents?"
        scene ep5_sc11_cof_13
        mc "You said that her father ruined your life, I can see how, but how does raping [sf_name] ruin his ?"
        off "They exchange another glance."
        lk "We intended to go a little further than that."
        off "Holy fucking shit."
        off "You were wrong, [mc_name]."
        off "They are murderers."
        mc "You want to kill her?"
        lk "Oh no! We're not murderers."
        lk "We want to... record a little souvenir of what will happen between her and us."
        lk "Once it's done, we'll make sure that it gets published worldwide."
        lk "The internet is inevitable now."
        lk "Having that kind of video surfacing every time someone does some research on you..."
        lk "We have no doubt that it will ruin her life, and her father's."
        off "No, they're not murderers."
        off "What kind of vengeance is that?"
        off "No doubt they are evil but it's also clear that they have completely lost touch with reality."
        off "They are crazy as fuck."
        off "You'd better get out of here as fast as possible, [mc_name]..."
        mc "You want to film yourselves while you rape her?"
        off "This is completely dumb."
        off "How can they hope to escape justice after that?"
        lk "Yes. We weren't supposed to do that."
        scene ep5_sc11_cof_14
        lk "At first, we thought that we could just seduce her and get her into our bed legitimately..."
        lk "But she has proven difficult to deal with."
        off "Did he really say \"our bed\"?"
        off "Ok, don't think about it, [mc_name]."
        off "You don't want to know."
        lk "So we don't really have a choice."
        mc "But that will be the end of you."
        mc "The police will come right at you after that."
        lk "We're prepared."
        lk "We'll leave the country once we're done with her."
        off "These morons are telling me everything."
        off "They trust me."
        off "I can't believe it."
        off "Let's try to hear their plan."
        mc "Okay... What do you have in mind?"
    else:
        off "I can't wait to make her pay."
        off "What better way to do it than to use these two crazy fuckers?"
        off "I should be careful, though."
        off "They're also morons."
        off "Their plan could be dumb as shit."
        off "Their attempts haven't been very successful until now."
        off "Finger crossed I'm not wasting my time with these bastards."
        scene ep5_sc11_cof_03
        lk "Hello, [mc_name]."
        mc "Guys."
        lk "I'm glad you came."
        lk "Ray was sure you wouldn't."
        ry "I thought you would chicken out."
        mc "And I didn't."
        scene ep5_sc11_cof_04
        mc "Can we cut the bullshit and get straight to the point?"
        mc "You've told me you had something in mind to deal with [sf_name]."
        mc "I'm listening."
        off "I don't like their ridiculous smile and I'm not here to befriend them."
        lk "Aren't you a bit impatient..."
        off "Asshole."
        mc "You saw how this bitch talked to us yesterday."
        mc "And she did another round on me after you left."
        mc "This whore is the reason why my family has gone to shit for the past three years."
        mc "She corrupted my friend."
        mc "She took her from us."
        scene ep5_sc11_cof_13
        mc "Everything is her fault."
        mc "So yes, I'm impatient."
        mc "Either you have something good to suggest or I do something on my own, but she's going to pay."
        lk "I told you. He's motivated."
        ry "At least he looks like he is."
        lk "That girl's family is rotten to the core."
        lk "They're egoist and evil bastards."
        lk "They ruin lives and get away with it."
        lk "We're like-minded, [mc_name]."
        scene ep5_sc11_cof_14_anger
        lk "Someone has to teach them a lesson."
        mc "I know nothing about her family, and I don't care."
        mc "What do you have in mind ?"
        off "They look at each other, probably trying to decide if they can trust me."
        off "They don't have a choice."


    lk "It's a very simple plan."
    lk "You put them to sleep and you let us in."
    lk "We do our thing and we leave before morning."
    mc "How do I put them to sleep?"
    off "He shows me a small bottle, half-filled with pills."
    scene ep5_sc11_cof_15
    off "They want me to dose the girls."
    off "I can't say I'm surprised."
    lk "You give them one of those, mixed with alcohol, and they'll hit their bed for hours."
    mc "Just like you drugged [sis_name] last Saturday night."
    ry "One pill in a beer, or a glass of wine, is enough."

    if moronic_hero_path == True:
        off "You just need them to give you these pills now."
        off "Keep cool [mc_name], you're almost there."
        off "Don't be too hasty."
        off "They trust you."
        off "Stay in character."


    mc "Yeah, well, there may be a small problem."
    mc "[sf_name] hates me."
    mc "I don't see how I can get her to drink that."
    mc "She won't want to interact with me at all."
    lk "That could be problematic."
    scene ep5_sc11_cof_16
    lk "You don't have to do it tonight."
    lk "Try to make peace with them so that they trust you enough so you can pour them a drink tomorrow."

    if moronic_hero_path == True:
        mc "I can try that."
        mc "I can't promise anything, though."
        mc "[sf_name] isn't really forgiving."
        lk "We know."
        lk "We're counting on you, [mc_name]."
        off "Don't accept too easily or it could be suspicious."
        off "Negotiate a bit before sealing the deal."
        mc "Also, you're not interested in [sis_name]."
        lk "No. We are not."
        mc "So you won't touch her."
        lk "We won't touch her."
        mc "Good. Also, I can't let you \"do your thing\" in my house."
        mc "You'll have to do it elsewhere."
        lk "Of course. We won't."
        scene ep5_sc11_cof_17
        lk "We'll take her to some other place."
        off "Don't go too far, [mc_name]."
        off "It's time to put an end to this."
        mc "Ok then."
        mc "Anything else I need to know?"
        off "Come on, moron, give me the pills and let me go now."
        lk "I knew we could count on you, [mc_name]."
        lk "First time I saw you I knew you were a nice guy."
        off "Your definition of a nice guy is so distorted that I'm not sure I'd like to fit in."
        mc "Yeah, likewise."
        lk "Contact me if there's any problem."
        lk "We need to be reactive if anything comes up."
        mc "Sure."
        off "I grab the bottle and stash it in my pocket as I stand up."
        scene ep5_sc11_cof_18
        ry "Remember, just one pill, in a bottle of beer, or a glass of wine, and that's enough."
        mc "I'll remember. No worries."
        lk "Goodbye, [mc_name]."
        lk "We'll see you tomorrow night."
        lk "We'll be waiting for your call."
        off "I leave the table and head to the door."
        scene ep5_sc11_cof_19
        off "My chest is about to explode."
        off "I feel nauseous."
        off "But it's done."
        off "I have everything I need."
        off "I can't believe it turned out so well."
        off "I just need to get to the police station, give them the pills and let them hear that conversation."
        off "And just like that, everything will be over."
        off "Girls, you better be ready, you'll soon have a hero to praise."
        jump ep5sc12
    else:
        mc "Are you asking me to apologize to that bitch ?"
        scene ep5_sc11_cof_20
        lk "You may have to."
        lk "[mc_name], if you really want your vengeance..."
        mc "How many times do I have to be humiliated by this bitch?"
        lk "I know. That's not easy to swallow."
        lk "But it'll be worth it."
        lk "Trust me."
        mc "You'd better be right."
        mc "So... I put them to sleep, I give you a call and you come in."
        mc "As simple as that."
        lk "No need to complicate things."
        scene ep5_sc11_cof_21
        lk "We come in, we get our fun and we leave before the morning."
        mc "About that fun... I want to make sure that you won't touch [sis_name]."
        lk "You've already made it clear that you wanted to fuck her first."
        mc "And that rule has changed."
        mc "I'll fuck her first and you won't fuck her at all."
        mc "She's mine. And mine only."
        off "That doesn't seem to bother them."
        off "Either they don't intend to respect any deal we may conclude or they have something else in mind."
        lk "We're cool with that."
        scene ep5_sc11_cof_14
        lk "Truth be told, we're not really interested in your friend."
        lk "From the beginning, we've only been interested in [sf_name]."
        lk "She was just a means to an end."
        off "Not interested in [sis_name]?"
        off "How could that be?"
        off "Unless this isn't about sex at all..."
        off "[sf_name] was their target, right from the start."
        off "What kind of grudge do they hold against her?"
        off "I don't really care, though."
        off "[sis_name] is mine, that's all that matters."
        mc "So I have [sis_name], you have [sf_name], and that's all?"
        lk "Actually you can have [sf_name] as well."
        scene ep5_sc11_cof_21
        lk "As long as we have our round with her before morning, we're fine."
        scene ep5_sc11_cof_22
        lk "You can fuck her all you want."
        lk "We'll give you enough drugs to keep them both sedated for days if you want."
        lk "Ray can show you how to handle that."
        lk "You will have all the fun you want and they won't even remember it."
        lk "When they wake up, just tell them they drank themselves into oblivion the night before and it will be good."
        lk "They'll feel like they've drunk their life away anyway."
        lk "What you do to them after we're gone is none of our concern."
        off "I could fuck them for days..."
        off "Shit..."
        off "[mc_name], are you really going to do that?"
        off "They won't remember a thing..."
        off "Is that really wrong if they don't even know it?"
        off "They won't even feel it."
        off "Of course, it's fucking wrong."
        off "It's fucking rape!"
        mc "Wait... If [sf_name] doesn't remember a thing, how is that vengeance?"
        mc "It won't make her less cocky after that."
        lk "She'll never know for sure, but she will feel different for the rest of her life."
        scene ep5_sc11_cof_16
        lk "There's no doubt about that."
        mc "That sounds so simple..."
        mc "You're telling me that I can put them to sleep tomorrow, fuck them for let say three days and then let them wake up as if nothing happened ?"
        lk "You could."
        lk "However, the longer the sleep the harder the hangover."
        lk "You shouldn't go past two days."
        ry "Also, more than two days would be dangerous."
        scene ep5_sc11_cof_23
        ry "They could die of dehydration."
        off "This guy knows."
        off "It's not their first time doing this kind of thing."
        mc "If I let them wake up on Saturday morning ?"
        ry "They'll have one hell of a hangover but aside from that they'll be perfectly fine."
        lk "You tell them that they drank like crazy and they won't even notice that their pussy hurt like hell nor that Friday has disappeared."
        off "I'm going to fuck them until my dick drops to the floor."
        mc "Ok. I'm in."
        off "I've said it. It's done. I'm teaming up with them."
        lk "I knew we could count on you, [mc_name]."
        lk "First time I saw you I knew you were a nice guy."
        off "A nice guy who's about to drug rape his childhood friend and her lesbian lover."
        off "These bitches deserve it."
        off "And if they don't remember it, it's like it didn't happen."
        off "I'm fine with it."
        mc "Yeah, likewise."
        lk "Contact me if there's any problem."
        lk "We need to be reactive if anything comes up."
        mc "Sure."
        scene ep5_sc11_cof_18
        ry "Remember, just one pill, in a bottle of beer, or a glass of wine, and that's enough."
        mc "I'll remember. No worries."
        lk "Goodbye, [mc_name]."
        lk "We'll see you tomorrow night."
        lk "We'll be waiting for your call."
        scene ep5_sc11_cof_24
        off "I'm going to fuck the girls."
        off "I'm going to fuck them until my dick falls off."
        off "Fuck I can't wait..."
        jump ep5sc14


label ep5sc12:
    scene black with dissolve
    with Pause(2)
    show text "Later - The police station."
    scene ep5_sc12_po_01 with dissolve
    off "I've waited almost an hour before an officer could hear me out."
    off "I can't help but think that I'm wasting my time."
    off "I explained to him everything twice and he still doesn't seem concerned at all."
    off "I brought him the recording and the pills, and he gazed at me with suspicion."
    off "The officer looked more bored than interested in my story."
    off "I already have the feeling that everything I did was completely useless..."
    ms "Alright Mr. Archer, we'll take it from here."
    off "At last..."
    mc "Thank you, sir..."
    mc "But... Are you going to arrest them?"
    mc "What do I do if they try to contact me ?"
    ms "This is now an ongoing investigation and I can't tell you anything about it."
    ms "I'll ask for patrols to scout your neighbourhood regularly."
    ms "If they ever try to contact you, do not respond."
    ms "Call the police if you notice anything related."
    ms "I'll also ask that you and your friends don't leave town."
    ms "Don't do anything unusual and everything will be alright."
    off "The patrols?"
    off "He must be joking."
    off "I came here asking for help and all they'll give us is a patrol strolling on our street two times a day or something?"
    off "How will that keep us safe from the psycho twins?"
    off "And he asks us not to leave town?"
    off "Are we the criminals or the victims?"
    off "What the fuck is going on?"
    scene ep5_sc12_po_02
    mc "Wait, you won't provide us with some protection?"
    mc "If you don't arrest them immediately, they will come for us!"
    mc "You heard them."
    mc "They're crazy!"
    mc "Are you going to search for them at least?"
    ms "As I said, Mr Archer."
    ms "I'll ask for patrols to scout your neighbourhood regularly, and if you notice anything suspicious, you can call the emergency telephone number."
    off "This can't be real."
    off "This is ridiculous."
    off "What do I have to say to have them do something?"
    scene ep5_sc12_po_03
    mc "Are you kidding me?"
    mc "They will kill us before you even reach our door!"
    ms "You can rest assured that we will come as fast as possible."
    ms "You are safe, Mr Archer."
    ms "Just stay home and call us if you notice anything's wrong."
    off "He pushes me outside of his office."
    off "This must be a joke."
    scene ep5_sc12_poc_01
    off "They don't give a shit about us."
    off "They won't do a thing."
    off "[sis_name] was right."
    off "We're alone."
    off "The psycho twins will know I've betrayed them."
    off "They will come."
    off "I have to warn the girls."
    jump ep5sc15


label ep5sc13:
    scene black with dissolve
    with Pause(2)
    scene ep5_sc13_k_01 with dissolve

    off "This is so weird."
    off "I've been here for a couple of minutes now, looking at them getting the breakfast ready while we're already in the middle of the afternoon."
    off "They talk about a movie they want to see, with a popular actor."
    off "They act like everything is normal, like nothing has just happened."
    off "They look happy."
    off "It makes me seriously question reality."
    off "Maybe it's a dream."
    off "Yeah, it's probably a dream."
    off "There's no way something like that happens to a moron like me."
    off "And if it had an infinitesimal chance to happen, it wouldn't be like that."
    off "That was so sudden..."
    scene ep5_sc13_k_02
    off "But what if it's real?"
    off "I'm now in a three-way relationship, with [sf_name] AND [sis_name]..."
    off "A throuple?"
    off "I think I have already heard that word."
    off "I can't even fathom the implications of it."
    off "What am I supposed to do now?"
    off "How am I supposed to behave?"
    off "I can't believe they're acting so normally."
    scene ep5_sc13_k_03
    off "I'm completely lost while they seem to already have accepted it without any problems."
    sf "[mc_name]?"
    sis "What are you waiting for?"
    mc "I...Sorry... I was daydreaming..."
    scene ep5_sc13_k_04
    off "I move to my seat as an awkward silence surround us."
    off "They've stopped discussing I don't know what."
    off "We look at each other with embarrassment."
    off "Did I manage to break their mood?"
    off "Ok, [mc_name]. Grow up a bit."
    off "Take the lead for once, and ask the questions."
    off "I know it's easier thought than done but someone has to do it."
    mc "Ok, I ... I think that we still need to talk about it..."
    scene ep5_sc13_k_05
    sis "I thought you were ok with it..."
    mc "I am!"
    mc "I am completely ok with it."
    mc "It's weird. It's strange."
    mc "But I'm completely ok with it, I don't think that there's any guy on this planet who wouldn't be ok with it."
    mc "I'm just... I don't know how to behave from now on..."
    scene ep5_sc13_k_06
    mc "How do we even do that?"
    mc "Are there rules to follow?"
    mc "I feel like we just avoided a disaster and the last thing I want is to hurt either of you by... doing or misunderstanding something..."
    sf "I thought it would ... come naturally... that everything would find its place..."
    scene ep5_sc13_k_07
    sf "Do you think we need rules?"
    off "She sounds so innocent and sincere..."
    off "She never had a single doubt that this could work."
    off "From the instant she imagined it, she was ready to give it her all."
    off "I feel so ashamed to have even thought that it could be a dream, a trap or anything else but an honest and pure idea born out of love."
    off "I feel unworthy."
    mc "I don't know... I mean..."
    mc "I feel like we need to discuss a couple of things, even if they are obvious."
    mc "Like... how do we behave in public?"
    off "[sf_name] looks at [sis_name], searching for her approval as she speaks."
    sf "I guess I'll be your official girlfriend..."
    sf "If it's ok with you, [sis_name]..."
    off "She nods."
    sis "It's not like I can be his girlfriend anyway..."
    scene ep5_sc13_k_08
    sis "At least one of us can make it obvious that he is ours."
    off "I'm theirs."
    off "That sounds so possessive."
    off "Again, I feel like I'm an object."
    off "But I'm also kind of... Proud and happy to hear that."
    off "She seems to have completely integrated the throuple thing, and the way she talks about it..."
    off "It's more like they are a couple, and they share me."
    off "That makes me think that..."
    off "Should I ask?"
    off "Of course, you should, [mc_name]."
    off "You want to know."

    mc "You said that you... Kind of love each other too..."
    mc "Is there something I should know ?"

    scene ep5_sc13_k_09
    off "[sis_name] hides her face behind her hand while [sf_name] intensely fixes her plate and blushes."
    sf "We should tell him."
    sis "What?! No!"
    sis "And I don't know what you're talking about!"
    off "Ok, there's definitely something I should know."
    sf "You know that this relationship can't work if we keep it a secret from him."
    sis "It's not a secret..."
    sis "Just something nobody has to know..."
    sf "He should know."
    scene ep5_sc13_k_10
    sis "You should never have said that in the first place."
    off "[sis_name] sounds annoyed, and kind of sad."
    off "She's giving in."
    sf "First I'll say that... It's not what you think."
    sf "We're not lesbians or anything like that. Are we?"
    sis "Of course we're not!"
    scene ep5_sc13_k_11
    sis "Oh gosh, I can't believe we have to tell him that."
    off "She hides her face in... Shame? Embarrassment?"
    off "It's actually cute."
    off "I like that."
    sf "I would say that we're like... soul sisters or something like that?"
    scene ep5_sc13_k_12
    sf "I'm not sure there's a word to describe what we are."
    sf "So we're not lovers like you may think we are, and in the meantime, I think we are much more than that."
    off "There's nothing embarrassing in that..."
    off "There must be something else..."
    scene ep5_sc13_k_13
    sf "However we... did things."
    off "Holy shit, it's coming."
    sis "We kissed! Ok? We kissed!"
    scene ep5_sc13_k_14
    sis "You don't have to tell him everything!"
    scene ep5_sc13_k_15
    sis "Oh my god, this is so embarrassing."
    sf "We were curious."
    sf "I mean... at some point, it became obvious that neither of us would meet anyone interesting during our high school years and..."
    scene ep5_sc13_k_16
    sf "We wanted to know how it felt... so we tried it."
    off "They kissed."
    off "No big deal..."
    mc "So you kissed..."
    sf "Yes... among other things..."
    sis "He doesn't have to know that."
    off "Oh but I want to know!"
    off "Just thinking about it makes me horny."
    off "Why am I a living cliché?"
    sf "We... I don't know how to describe it..."
    sis "Touched! We touched each other, ok?"
    scene ep5_sc13_k_17
    sis "Nothing more!"
    sf "Yes, we ... explored and touched each other, with our fingers, and tongues and..."
    scene ep5_sc13_k_18
    sf "We gave each other some pleasure..."
    off "My imagination is running wild."
    off "That's so freaking hot."
    sis "Oh my god."
    sis "Why do you have to tell him that?"
    sis "This is so embarrassing..."
    mc "When did you..."
    sf "I think we started... Last summer..."
    scene ep5_sc13_k_19
    off "Started... That means this isn't a one-time thing..."
    off "And it's probably still going on..."
    mc "So you're like... Sex friends, or friends with benefits I guess ?"
    sf "We could probably say that..."
    mc "And you're still ... ?"
    sf "Oh no! No, of course not!"
    sf "It's... since... I mean... we didn't do anything since ... last week..."
    scene ep5_sc13_k_20
    sis "I want to die."
    off "[sis_name] sounds and looks like she's drowning in shame."
    mc "You don't have to be embarrassed..."
    mc "There's nothing wrong or shameful in that..."
    sis "Yeah. Sure. Do you have sex with Steve ?"
    mc "What? No! Of course not!"
    mc "What does that have to do with..."
    mc "I don't have that kind of relationship with Steve..."
    sis "Yeah, that's what I thought."
    scene ep5_sc13_k_21
    sis "Shut up then."
    mc "No seriously!"
    mc "I'm sorry you take it like that but... I honestly think that you don't have a reason to be ashamed of it."
    mc "The way [sf_name] talks about it is actually... Beautiful."
    sis "Beautiful?"
    sis "Are you kidding me?"
    mc "No... I'm kind of... Admirative."
    off "She looks at me suspiciously for a few seconds."
    sis "Are you having a boner right now?"
    scene ep5_sc13_k_22
    mc "No ! I'm not!..."
    off "I'm totally having a boner right now. "
    mc "Ok, Princess."
    mc "I may have a boner, but it's a completely natural reaction given the current circumstances."
    mc "There's nothing I can do about it and it doesn't belittle what I'm about to say..."
    mc "I'm not judging you in any way, and I'm actually happy that the two of you share a bond deep enough to allow you to fulfil your curiosity and explore things together."
    mc "As I understand it, it made you happy, and that's all that matters."
    sis "I'm not ashamed, ok?"
    scene ep5_sc13_k_23
    sis "It's just that I would prefer to keep it private..."
    sis "Even if [sf_name] is right."
    sis "I know that she's right..."
    sis "And telling you was... Ok..."
    sis "Stop looking at me like that."
    sis "Just to be clear, [sf_name] and I won't suddenly get rolling on the table half-naked, kissing and licking each other just for your enjoyment ok ?"
    off "Holy mother of god."
    off "Stop putting these images in my brain, please."
    mc "I never thought that you would!"
    sis "Great."
    off "[sf_name] laughs."
    off "She's mixing embarrassment and amusement."
    sf "You're so cute."
    scene ep5_sc13_k_24
    sf "Seeing you like that... It all makes sense now..."
    sis "What are you talking about?"
    sf "You know... The two of you..."
    sf "Twins bickering over trivial things... like an old couple... "
    sis "We're not... We're... I mean... I guess..."
    off "[sis_name] fights to find some riposte but she just ends up pouting, admitting defeat."
    scene ep5_sc13_k_25
    off "I suddenly understand something."
    mc "We don't have to hide anymore..."
    sis "What?"
    mc "Sorry, it... It just hit me."
    mc "I'm slowly catching up with reality here."
    scene ep5_sc13_k_26
    mc "I just realized that."
    mc "We don't have to hide from [sf_name] anymore..."
    off "[sf_name] gently smiles."
    off "[sis_name] sports her most ironic smirk."
    sis "I guess you're right."
    sis "But I hope you'll let us finish that breakfast before you jump me on this table."
    sf "I don't mind."
    sis "But I do! I do very much!"
    sf "You're as bad a liar as [mc_name]."
    off "[sf_name]'s laughs again."
    off "I still don't get how both of them can accept and integrate our new situation so easily."
    off "They joke about it while I still strive to accept it."
    off "It probably has to do with their unique bond..."
    off "Maybe I should try a couple of jokes too."

    scene ep5_sc13_k_27

    menu:
        mod "No Conequences Yet."
        "What if I take you on this table right now, [sf_name]? \[SfJoke\]":
            $ ep5sfjoke = True
            mc "Would you mind?"
            off "Ok, that's a fail, that didn't sound like a joke at all."
            off "[mc_name], you are a moron."
            off "What kind of joke is that?"
            off "How about subtility?"
            scene ep5_sc13_k_28
            off "What is she going to think of you now?"
            off "You sounded like a total pervert."
            off "You are an imbecile."
            off "Look at her she's terrified, and I bet [sis_name] is going to beat the crap out of me..."
            scene ep5_sc13_k_29
            sf "I wouldn't mind..."
            $ ProcessStat(2, "sf_affection")
            $ DumpNotStack()
            off "HOLY MOTHER OF GOD."
            off "Did I hear that right?"
            off "It was barely more than a whisper."
            off "She sounded shy and embarrassed as hell."
            off "What do I say?"
            off "What do I do?"
            off "Find something, [mc_name], something sweet, and smart, avoid the awkward silence!"
            off "Crap. Should I make a move?"
            off "Of course not, it's clearly too soon, idiot."
            off "But what if it isn't?"
            off "Is she waiting for me to..?"
            scene ep5_sc13_k_30
            sis "Ok, I'm gonna take my plate elsewhere and let you do your thing."
            sis "You have obviously something to take care of..."
            off "Oh thank you, [sis_name]."
            off "Your mocking will lighten up the mood."
            sis "Just let me tell you, young lady, I never thought you would be so naughty."
            sf "You can talk."
            sf "You would enjoy the table too!"
            sis "Please don't give him any more ideas, or we may have to pay the price afterwards."
        "I wouldn't mind either...":




            $ ep5sisjoke = True
            off "She barely flinches."
            sis "I can't say I'm surprised."
            sis "I was joking ok?"
            scene ep5_sc13_k_31
            sis "You're not going to take me on this table right now."
            sis "So you can calm down, Perv."
            $ ProcessStat(2, "sis_affection")
            $ DumpNotStack()
            off "Ok, maybe that wasn't the best joke ever."
            off "But that was very tempting."
            off "[sf_name] bursts out laughing, though."
            sf "You should see your face, right now."
            sis "What? What is it with my face?"
            scene ep5_sc13_k_24
            sf "Dear, it's so obvious that you're okay with it."
            sis "No, No, No. I'm not... not like that at least..."
            sis "Not at first... I mean..."
            sis "Oh, will you shut up ?"

    off "And here they go again."
    off "Joking and laughing about it while I'm left hanging."
    off "I can't help but wonder if they're not... Playing me."
    off "Of course, they're not."
    off "They're just happy to share something."
    off "I envy them."
    off "I should just stop thinking about it and just live it."
    off "YOLO."
    off "All of that leads me to my next question."
    off "The very embarrassing one."
    off "I'm not gonna lie, it's like the first thing that came to my mind when they proposed this solution..."
    off "It's ok, [mc_name]."
    off "Asking is natural and you can't let that kind of things unsaid."
    scene ep5_sc13_k_32
    mc "So... what about... intimate moments?"
    off "They suddenly stop laughing and turn to me."
    off "The mood changed completely."
    sf "You mean when we... do things... ?"
    mc "Yes... will we... take turns?"
    off "This is so embarrassing."
    off "Did I really say that?"
    off "It sounds so insensitive."
    mc "I mean it doesn't feel... Natural, as you said..."
    sf "It could feel a bit weird, indeed..."
    scene ep5_sc13_k_33
    sis "Are you proposing that the three of us... do it together?"
    sis "Right from the start?"
    sis "I didn't even have my first time..."
    off "Did I really propose having threesomes?"
    mc "Wait, I didn't..."
    scene ep5_sc13_k_34
    sf "I didn't have it either..."
    sis "I know!"
    sis "It would be so weird..."
    sf "But in the meantime..."
    sf "I can't help but think that it would be... Reassuring to have you there when... You know..."
    scene ep5_sc13_k_35
    sis "I know... I feel the same..."
    mc "Girls, I don't want to..."
    sf "I think I would be ok with it."
    sf "If it's with you. Even for the first time..."
    sis "I'm okay with it too..."
    mc "Please, girls! Wait! I never wanted to propose that! I was just asking how we would do... The normal thing..."
    scene ep5_sc13_k_36
    sf "No, no, you're right, [mc_name]."
    sf "There can't be a normal thing."
    sf "The three of us have to... do it together."
    off "Oh my god."
    off "We're going to have threesomes."
    sf "That doesn't mean we can't have some intimate couple moments."
    sf "But the three of us doing it together... yes, the more I think of it, the more it seems obvious..."
    off "Am I hyperventilating?"
    off "I'm hyperventilating."
    off "I'm going to pass out."
    off "I need to calm down."
    off "Concentrate on breathing, [mc_name]."
    off "Slowly."
    scene ep5_sc13_k_37
    sis "So... I was thinking..."
    sis "Do you want to do it first?"
    sf "I don't know... Do you want me to?"
    sis "I'm... a little afraid of ... his size..."
    sf "He's pretty big."
    off "I'm passing out."
    off "I can sense reality fading away."
    off "Am I having an erection right now?"
    off "My dick feels funny."
    off "It tingles."
    sis "Maybe you could do it and tell me how it felt before I..."
    scene ep5_sc13_k_38
    sf "I... I guess I could do that..."
    sis "I'll be there ... to support you I guess..."
    off "I'm going to do it."
    off "With both [sf_name] and [sis_name]."
    off "At the same time."
    off "Everything is blurry."
    off "My whole face feels numb."
    sf "You know that I'm not on the pill..."
    sf "I never thought I would... "
    sis "I am."
    sis "And I never thought I would either..."
    scene ep5_sc13_k_39
    sis "You need a consultation to get a prescription."
    sf "I doubt I can get one this afternoon..."
    sf "We'll have to be careful."
    sis "You mean like... Pulling out?"
    sis "Maybe [mc_name] has some condoms?"
    sis "It would be safer."
    off "No, I don't have any..."
    sis "[mc_name]?"
    sf "[mc_name]!"
    sis "Oh my god!"
    scene black with dissolve
    with Pause(2)
    scene ep5_sc13_k_40 with dissolve
    sf "Take it easy, [mc_name]."
    off "Am I lying on the floor?"
    off "What happened?"
    sf "You fainted."
    sis "I'm calling an ambulance."
    off "[sis_name]'s voice is filled with panic."
    off "[sf_name] gently caresses my face with the back of her fingers..."
    off "An ambulance?"
    mc "What? There's no need for an ambulance..."
    sis "[sf_name] just told you, you fainted!"
    mc "I'm ok now. I'm ok."
    sis "No, you're not."
    off "I try to stand up but [sf_name] keeps me grounded."
    off "Her knees are very comfortable."
    sf "Don't move, [mc_name]."
    sf "Are you sure you're not hurt anywhere?"
    sf "You've hit the floor pretty hard when you fell from your chair."
    mc "I'm okay."
    mc "I was just... A bit overwhelmed by... the situation."
    mc "I'm not hurt, my only bruises are on my self-esteem right now."
    off "This is so humiliating."
    sis "Overwhelmed? Are you kidding me?"
    mc "I'm alright, ok? You don't need to worry. I'm fine."
    off "She doesn't seem satisfied."
    off "I slowly stand up."
    scene ep5_sc13_k_41
    off "The girls cling to me as if they feared I faint again."
    mc "How long did I stay out?"
    sf "No more than a minute."
    sis "Enough to have us worrying to death, you moron!"
    mc "I'm sorry about that."
    sf "You're sure that you're alright?"
    mc "Yes. I am."
    sis "You don't want to lay down a moment or something ?"
    mc "No, I'm ok."
    mc "Stop worrying, please."
    mc "It was just a one-time thing ok?"
    mc "I think that I hyperventilated a bit and I guess I couldn't take it... But I'm alright now."
    mc "Let's go back to breakfast."
    off "The girls look at me suspiciously as we take our places back around the table and resume the cleaning of our plates."
    off "The breakfast is cold."
    off "We've barely touched it."
    off "The conversation has changed to some more casual subjects."
    off "I can't stop harping on about what was just said."
    off "We're going to do it."
    off "The three of us."
    off "[sis_name] is on the pill, [sf_name] is not."
    off "It's going to happen."
    off "Holy shit."
    off "No pressure, [mc_name]."
    off "You can do it."

    jump ep5sc14


label ep5sc14:

    scene black with dissolve
    with Pause(2)

    if evil_asshole_path == True:
        scene ep5_sc14_mcr_01 with dissolve
        off "I've thought that meeting with the psycho twins and planning something would bring me some peace of mind."
        off "I was wrong."
        off "I can't stop thinking about what I'll do to the girls."
        off "I need to calm down."
        off "If I keep thinking about it, I'm going to go crazy and commit a mistake I can't afford to make."
        off "I'm going to fuck them."
        off "That's for sure. But for now, I need to keep calm."
        off "Stay cool [mc_name]."
        off "You need to play the nice guy."
        off "Get them to trust you enough so that they won't refuse drinking with you tomorrow night."
        off "Fuck, I have no idea how I should do that."
        off "We have nothing in common. Nothing I can talk about with them."
        off "I should have eaten breakfast with them this morning..."
        scene ep5_sc14_pool_01
        off "Look at them, [mc_name]."
        off "They'll be yours soon."
        off "You will destroy that pussy."
        off "And that ass too...... Am I really?"
        off "Am I really going to do that?"
        off "Ok, they treated me like shit, ok they deserve a spanking..."
        off "But ... drugging them and raping them for days..."
        off "That's something else entirely..."
        off "If you do that, you're going to jail, [mc_name]."
        off "You can't possibly be serious."
        scene ep5_sc14_pool_02
        off "You just have pushed the fantasy a bit too far, you can still back down and return to your usual moron self."
        off "You'll find another way to make [sf_name] pay."
        off "Something safer, that doesn't mean committing some inhuman crime."
        off "But they said that they won't even remember a thing."
        off "They'll feel that something as changed, that something is wrong, but nothing more."
        off "If they don't remember it, it's like nothing happened."
        scene ep5_sc14_pool_03
        off "I'll just have a good time."
        off "And everything will go back to the usual mess."
        off "No one will ever know. It's safe."
        off "It's fucking rape!"
        off "Yeah, yeah... And she's fucking [sis_name]."
        off "And so what?"
        off "It's their life!"
        off "They do what they want with it!"
        off "That slut took her from us."
        off "No, she didn't!"
        off "She didn't take anything!"
        off "You rejected [sis_name]!"
        scene ep5_sc14_pool_04
        off "Bullshit."
        off "Everything started with her."
        off "Without [sf_name], everything would have been very different."
        off "It's her fault."
        off "She deserves this."
        off "You'd better think this through very carefully, [mc_name]."
        off "There is no coming back from this."

        if ep2sisabused == True:
            off "I've already put my dick in her mouth and nobody got hurt."
            off "Why would it be any different?"
            off "It's considerably worse, dumbass."
            off "No doubt about it."

        scene ep5_sc14_mcr_02
        off "Do you really want to become a monster?"
        off "It'll be a one-time thing."
        off "And they won't remember anything."
        off "No one will know."
        off "No need to overreact."
        off "I'm sure it happens every day and no one makes a fuss about it."
        off "It's ok..."
        jump ep5sc18
    else:
        scene ep5_sc14_pool_05
        off "The sun hits hard."
        off "The air itself burns."
        off "I've barely set foot outside that I already miss the cold kiss of the AC."

        if dual_love_path == True:

            off "Everything feels strange since we decide to... since they decided that we should..."
            off "Be a throuple."
            off "I'm pretty happy with it, of course, who wouldn't be?"
            off "It's just that it feels like I've barely been consulted."
            off "And it's so sudden, that's it feels unreal."
            off "Let's be honest."
            off "I'm nothing more than a regular guy and I score high enough on the nerd scale to get out of high school with my virginity unscathed."
            off "And tonight I'm going to have a threesome with [sis_name] and [sf_name]."
            off "That is nuts."
            off "At some point, I'll probably wake up and cry in despair when I'll realize that everything was just a dream."
            off "Once again, I can't help but hear Steve's voice screaming into my hear: YOLO."
            off "How can this moron be so right?"

        off "Both girls turn to me as I walk by the pool."

        if dual_love_path == True:
            scene ep5_sc14_pool_06_dual
        elif sf_love_path == True:
            scene ep5_sc14_pool_06_cassie
        elif sis_love_path == True:
            scene ep5_sc14_pool_06_eve
        else:
            scene ep5_sc14_pool_06

        if sf_love_path == True:

            off "I love [sf_name]'s smile."
            off "Each time I see it, I melt a little more."
            off "And at the same time, I feel a bit ashamed."
            off "I feel unworthy of that pure and innocent love."

            if sis_sub_path == True:
                off "And I have a good reason for that."
                off "The things I do with [sis_name] behind her back..."

            if dual_love_path == True:
                off "And I have a good reason for that."
                off "The things I did with [sis_name] behind her back...."
                off "Of course, it's now resolved but..."
                off "I can't help but still feel guilty..."

            if sis_sub_path == True:
                off "How did it come to this?"
                off "My life has become so crazy since last weekend..."
                off "[sf_name] is my girlfriend..."
                off "And [sis_name] is my..."
                off "I don't know what she is.... But she is."
                off "How long can I can keep it like that?"
                off "I have no desire to make a choice but let's get real for a moment..."
                off "I will have to."
                off "I only wish that there could be another way."
                off "Come on [mc_name]."
                off "You've already been unbelievably lucky."
                off "There can't be any other way."

            if dual_love_path == True:
                off "And then..."
                off "There's [sis_name]'s smile."
                off "It's beautiful, but there's also something weird about it."
                off "At first, I couldn't quite put my finger on what was bothering me but I understand now."
                off "I haven't seen it in years."
                off "I haven't seen [sis_name] smile for the last three years."
                off "Why do I realize that only now?"
                off "Another reason to feel guilty and ashamed."

        scene ep5_sc14_pool_07
        mc "Hey, girls. Slowly cooking ?"
        sis "I'm almost well done."
        sf "It's too hot for me."
        sf "I was about to head back inside."
        sis "The weathercast wasn't kidding with that heatwave thing."
        mc "And it's supposed to last until Saturday."
        mc "It can even get worse before that."
        sf "God bless the AC."


        if dual_love_path == True:

            scene ep5_sc14_pool_08
            off "[sf_name] grabs my arm and puts her hand on my chest."
            off "Her touch is soft and gentle."
            off "I like it."
            off "Her large shades forbid me to read her expression, but I can guess she still worries about me."
            off "[sis_name], on the other hand, seems ready to mock me."
            sf "What about you?"
            sf "Are you feeling better ?"
            mc "I'm alright!"
            mc "I told you it was nothing."
            mc "I just got... A little too excited by... The conversation..."
            sis "Excited, huh ?"
            scene ep5_sc14_pool_09
            mc "Hey, it's humiliating ok?"
            mc "You can't talk about these things so casually in front of me and expect no reaction."
            sis "You're the one who came up with the subject so..."
            mc "I know... but I wasn't expecting that the both of you would be so... Straightforward about it..."
            sis "He's saying that he can't handle us."
            mc "I never said that."
            mc "I can totally handle the both of you, ok?"
            sis "Yeah. Sure."
            mc "I guess I'll show you tonight."
            off "That sounded a bit more aggressive than I wanted."
            sis "... We'll see about that..."
            off "[sis_name] seems embarrassed and looks away."
            scene ep5_sc14_pool_10
            off "[sf_name] laughs."
            sf "I think that we all have some tensions to relieve."
            sf "We may have been very straightforward, talking about these things earlier, that doesn't mean that we're not nervous or stressed about it."
            sf "I guess that none of us knows how to behave, right?"
            sf "And it's perfectly normal, isn't it?"
            sf "None of us has ever been a couple before and we're now in a more complex relationship."
            sf "Maybe we should just try to relax."
            off "Easier said than done."
            scene ep5_sc14_pool_11
            off "She slowly clings into me and goes for my lips."
            off "This is our first true kiss since the throuple thing was decided."
            off "I can feel my guts liquefying."
            off "I'm afraid that everything will fall apart as soon as we have any \"serious\" contact."
            off "How will [sis_name] react?"
            off "I can feel her tensing up a bit."
            off "Is it anger? Embarrassment? Jealousy?"
            scene ep5_sc14_pool_12
            off "[sf_name]'s lips are as sweet as ever."
            off "Her tongue shyly invades my mouth."
            off "I welcome her."
            off "I slowly let go of my apprehensions and finally enjoy the moment."
            off "Her body presses against mine."
            off "I want to grope her a bit more but I manage to restrain myself."
            off "I barely allow myself to put my hands on her but her contact feels... Fulfilling."
            scene ep5_sc14_pool_13
            sf "I have no idea what I'm doing."
            sf "Please, bear with me."
            mc "Whatever you want..."
            off "I answered that instinctively and have no idea where that comes from."
            off "But yes, indeed, I'll do anything she wants."
            off "She parts from me and she gently pushes me towards [sis_name]."
            off "We're looking at each other awkwardly as [sf_name], leans on my back and whispers."
            scene ep5_sc14_pool_14
            sf "Grab her."
            sf "Hold her tight."
            off "My saliva is suddenly hard to swallow."
            sf "If the three of us are to be together, we have to let go of things like shame, and fear."
            sf "No one will be hurt."
            scene ep5_sc14_pool_15
            off "My lips meet with [sis_name]'s."
            off "I can feel her twitch under my touch."
            off "Kissing in front of [sf_name] embarrasses her as much as me."
            off "[sf_name] knows it of course."
            off "She pushes us together so we can overcome the fear to hurt her or something like that."
            off "And it's working I guess."
            off "I'm giving it my all."
            scene ep5_sc14_pool_16
            off "[sis_name] seems a bit reluctant at first but quickly joins me in some kind of moist and warm oblivion."
            off "I can feel [sf_name] still leaning against my back and I suddenly understand something important."
            off "This isn't just a kiss."
            off "[sis_name] and [sf_name] know that too."
            off "This is the moment we truly give ourselves to each other, the moment that throuple thing gets real."
            off "I still don't fully understand how we could come to form that bond, but I like it."
            scene ep5_sc14_pool_17
            sf "That wasn't that hard, was it?"
            off "They both softly cry."
            off "I have a hunch that these are tears of joy rather than sadness."
            off "I don't really understand why they cry."
            off "I could argue that women are mysterious creatures impervious to reason but it's probably just a thing between them."
            scene ep5_sc14_pool_18
            off "I don't even feel left aside when they hug."
            off "I feel relieved."
            sis "Thank you."
            sf "I've done nothing."
            sf "I don't know why you're thanking me."
            sis "I don't know either."
            off "They're weird."
            off "And cute."
            off "And I love them."
            off "It's so obvious."
            off "I'm about to join their embrace when a faint noise gets my attention."
            scene ep5_sc14_pool_19
            off "It's the doorbell."
            off "We can barely hear it from here."
            mc "I think there's someone at the door."
            mc "I'll see to it."
            jump ep5sc15

        if sf_love_path == True:
            sf "We've been out for barely half an hour and I can already feel my skin burning."
            scene ep5_sc14_pool_20
            off "She grabs my arm and lightly kisses my lips."
            sf "I'm sorry to abandon you but I'm going back inside."
            sf "I can't stand it any more."
            mc "Ok... I guess I'll join you in a few minutes."
            sf "You don't have to."
            sf "I'll take some time to call my dad."
            sf "He needs to hear from me every day."
            scene ep5_sc14_pool_21
            off "She quickly dries herself with a towel before heading back inside."
            off "She playfully waves a goodbye as she leaves the place."
        else:
            sf "We've been out for barely half an hour and I can already feel my skin burning."
            scene ep5_sc14_pool_22
            sf "I'm sorry to abandon you but I'm going back inside."
            sf "I can't stand it any more."
            sis "I'm coming with you."
            sf "You don't have to."
            sf "I'll take some time to call my dad."
            sf "You know he needs to hear from me every day."
            scene ep5_sc14_pool_23
            off "She quickly dries herself with a towel before heading back inside."

        if sf_dom_path == True and ( sis_sub_path == True or sis_love_path == True ):
            off "After what happened in my room earlier, she leaves me alone with [sis_name]..."
            off "It's obviously a trap."
            off "If I try anything she'll probably jump out of the house to surprise us or something like that..."

            if sis_hard_sub_path == True:
                off "That girl is crazy."
                off "I have no idea how she would react if she happened to know what's going on between [sis_name] and me."
                off "She would probably kill me."
                off "After all, I'm kind of cheating on her..."
                off "Yeah, I should keep a low profile for now."
                scene ep5_sc14_pool_24
                off "What's with that weird look, Princess?"
                off "You expect me to do something, don't you?"
                off "You want me to..."
                off "Don't worry."
                off "We'll catch up later."
                off "I can feel it."
                off "Tonight is our big night, isn't it?"
                off "You're ready for me."
                off "I'm going to fill your pussy up."
                off "You'll like it."
                sis "What?"
                mc "What what ?"
                sis "Why are you looking at me like that ?"
                mc "Can't I look at you, Princess?"
                scene ep5_sc14_pool_25
                sis "I don't know... You're making a weird face..."
                mc "You should see yours."
                mc "It looks like your expecting me to do something."
                sis "I'm not expecting anything."
                mc "I can control myself."
                mc "I'm not going to jump on you as soon as we have a minute alone."
                sis "No, I didn't mean that... I know..."
                off "I slowly get away from her without saying a word."
                off "I can feel her gaze over me."
                off "She's disappointed."
                off "She hoped for more."
                off "Good."
                scene ep5_sc14_pool_26
                off "We avoid looking at each other for the few more minutes we spend simmering in the pool."
                off "The silence is uncomfortable."
                off "[sf_name]'s steps and voice manage to break the mood a moment later."
                sf "[sis_name]? [mc_name]? I think you should come in."
                sf "We... have a visitor."
                jump ep5sc15

            if sis_sub_love_path == True or sis_love_path == True:
                off "Why would she do that, however?"
                off "I mean, I kind of confessed that I have an affair with my father's ward."
                off "That's already enough to fuck up our lives."
                off "Now, the question is... should I tell [sis_name] what happened?"
                off "That would mean confessing that I did... These things with [sf_name]..."
                off "I'm not sure that I want [sis_name] to know that I've let [sf_name] fuck my ass..."
                off "Definitely not."
                off "I don't know what she would think of me after that..."
                off "Look at her."
                off "We have a few minutes alone."
                off "How can I miss this occasion?"
                off "Just a hug."
                off "Maybe a kiss..."

        if sis_sub_path == True:
            scene ep5_sc14_pool_27
            off "[sis_name] and I look at each other. She knows I’m coming for her. We have a few minutes alone. I'm going to put them to good use."

        if sis_sub_love_path == True:

            if sf_love_path == True and sis_sub_path == True:
                off "There's something new, though."
                off "I look at [sis_name] with desire but also a bit of apprehension."
                off "I feel kind of bad for [sf_name]."
                off "I'm cheating on her."
                off "It’s weird."
                off "I have some honest feelings towards [sf_name] but I just can’t resist the urge to fool with [sis_name]."
                off "Maybe I’m sick or something."
                off "Maybe I’m just an asshole."
                off "I don’t want to choose."
                off "I may have to, but I certainly don’t want to."

            mc "So... How is my Princess doing today?"
            sis "I... I'm doing fine..."
            off "She tenses up."
            off "She thinks I'm going to try something naughty again."
            mc "Great."
            scene ep5_sc14_pool_28
            off "I wrap my arms around her and hold her close to me."
            off "She doesn't resist but I can sense her surprise."
            off "She has no idea how to react."
            sis "[sf_name] could..."
            mc "Yes, she could."
            mc "And I don't care."
            mc "I can hug my friend, can't I?"
            sis "I ... I guess so..."
            mc "Good."
            mc "I want you to relax."
            mc "Close your eyes."
            mc "Breathe."
            mc "You're safe."
            off "She hesitates to give in but finally follows my commands."
            mc "It's okay to be surprised."
            mc "It's not something we've done for a while."
            mc "I haven't been there for you, but that has changed."
            mc "As long as I'm here, nothing bad can happen to you any more."
            off "She gradually lets herself go."
            scene ep5_sc14_pool_29
            off "She leans on me and huddles in my arms."
            mc "You are mine now."
            mc "I'll take care of you."
            off "She sighs as she completely surrenders herself."
            off "I can feel the stress leaving her body."
            mc "We're together."
            mc "We'll always be."
            off "I gently caress her head and play with her hair."
            off "I can feel her breath on my shoulder."
            mc "It feels nice, doesn't it ?"
            sis "Yeah..."
            mc "You like it."
            sis "I do..."
            scene ep5_sc14_pool_30
            mc "I can feel your heart beating in your chest."
            mc "Can you feel mine ?"
            sis "Yeah..."
            off "I give her a little minute of silence to appreciate the moment."
            off "She doesn't move an inch."
            mc "We should hug more often."
            mc "Make it a ritual."
            mc "What do you think?"
            sis "I guess we could..."
            off "I'm about to make a move toward her lips when the faint noise of the doorbell interrupts me."
            off "[sf_name] will probably take care of it but still..."
            scene ep5_sc14_pool_31
            off "[sis_name] and I slowly part ways and I can't help but think that she looks a bit disappointed."
            off "Maybe she wanted more."
            off "That moment was short but great, though."
            off "I wanted her to feel safe and making it so was very satisfying."
            off "She seems to have completely integrated that she's now mine and that she can trust me."

            off "[sf_name]'s steps and voice achieves breaking the mood a minute later."
            sf "[sis_name]? [mc_name]? I think you should come in."
            sf "We... have a visitor."
            jump ep5sc15

        if sis_hard_sub_path == True:

            off "She tenses as I slowly walk towards her."
            off "She takes a step back and I end up cornering her against the edge of the pool."
            scene ep5_sc14_pool_32
            sis "[sf_name]... Could come back anytime..."
            off "She could yes."
            off "I'll have to make it quick."
            mc "So what?"
            sis "You shouldn't..."
            off "She looks so shy and embarrassed."
            off "So vulnerable... I like that."
            off "It makes me feel powerful."
            off "In control."
            mc "I shouldn't what?"
            off "I gently caress her face as she struggles to utter her reply."
            sis "You know..."
            mc "No, I don't know."
            mc "Would you please explain it to me ?"
            sis "... You shouldn't do things to me."
            mc "Oh. Things... Like what I did to you last night?"
            off "I let my hands wander on her."
            scene ep5_sc14_pool_33
            off "She trembles when I gently caress her breast."
            off "Her hands ridiculously hang in the air."
            off "She doesn't know what to do with them."
            mc "You enjoyed it."
            off "She keeps silent and breathes heavily."
            mc "You're a very naughty girl."
            mc "Do you know that?"
            mc "But it's ok."
            mc "It's perfectly normal."
            mc "Everyone would have enjoyed that."
            mc "I enjoyed that."
            scene ep5_sc14_pool_34
            off "My fingers are running on her hips."
            off "I know that I'll soon grab on these as I'll pump my dick into her as hard as I can."
            off "I enjoy the expectation for now."
            off "I can feel that it makes her go crazy too."
            off "She wants it but is still too ashamed to acknowledge it."
            off "I enjoy seeing her struggle with her feelings."
            off "I bet she can't stop thinking about it."
            off "I whisper in her ear."
            mc "And you want more."
            off "I go for her pussy."
            scene ep5_sc14_pool_35
            mc "I want more too."
            off "She gasps and twitches as I touch her down there."
            off "I like her reaction."
            off "I massage her through her bikini."
            off "Her hands clutch on my shoulders."
            off "She doesn't even try to escape my touch."
            off "She tries to endure it."
            mc "I hardly can wait for tonight."
            mc "What do you want me to do to you?"
            mc "Tell me, Princess..."
            sis "I don't want anything..."
            scene ep5_sc14_pool_36
            off "My hand invades her panties."
            off "I gently visit her slit before going in."
            off "She arches as my finger slowly enters her."
            mc "Are you saying that anything I'll do will be fine ?"
            sis "No! I... Maybe you can... Lick me..."
            mc "I will if you deserve it..."
            mc "Have you been a good girl ?"
            scene ep5_sc14_pool_37
            off "She closes her mouth with her hands but can't suppress a long and high-pitched moan."
            mc "What can you do to deserve it ?"
            sis "I... can ... take you in my mouth..."
            mc "That's very naughty, Princess."
            mc "I'm looking forward to that."
            off "I think about giving her my dick right now when the faint noise of the doorbell ruins my hopes."
            scene ep5_sc14_pool_38
            off "[sis_name] slips under my arms and escapes from me."
            off "She looks ashamed as fuck and quickly gets out of the pool."
            off "She's running away from me in shame."
            off "I'll fuck her tonight."
            off "I know it."
            off "I'm nervous as hell."
            off "I can't wait."
            off "[sf_name]'s footsteps and voice break the mood a minute later."
            sf "[sis_name]? [mc_name]? I think you should come in."
            sf "We... have a visitor."
            jump ep5sc15

        if sis_love_path == True:

            scene ep5_sc14_pool_39
            off "[sis_name] looks at me with suspicion."
            sis "What's with that smile?"
            mc "What smile?"
            sis "The one on your face."
            mc "What about it?"
            off "I take a step toward her."
            off "She immediately stops me."
            scene ep5_sc14_pool_40
            sis "Don't come closer."
            mc "Why ?"
            sis "I know what you're about to do."
            sis "Don't."
            mc "You've got me curious."
            mc "What am I about to do?"
            sis "Are you playing dumb?"
            sis "You know exactly what I'm talking about."
            mc "I'm not playing dumb."
            mc "I'm trying to flirt."
            mc "I'm no expert, though."
            mc "Am I failing at it?"
            off "She looks away."
            scene ep5_sc14_pool_41
            sis "I'm no expert either."
            off "I move one step closer."
            sis "[sf_name] almost caught us this morning."
            sis "We should be careful."
            mc "Does she suspect anything?"
            sis "I don't think so... "
            mc "Then we're good, aren't we?"
            scene ep5_sc14_pool_42
            sis "How can we be good?"
            sis "She almost caught us going at it!"
            mc "Oh, were we going at it?"
            sis "You know what I mean."
            sis "Can you please stop that?"
            sis "And I've told you not to come any closer."
            mc "I want to kiss you."
            sis "And it's not going to happen."
            mc "Alright."
            off "I'm not going to force her."
            off "I move on her side and lean on the side of the pool."
            scene ep5_sc14_pool_43
            mc "That's too bad."
            mc "I like your lips."
            mc "They're soft and sweet."
            sis "Will you shut up?"
            mc "And so warm."
            mc "When I kiss you I feel like you share that warmth with me."
            mc "It starts with the lips and it invades my chest and lights something in my heart."
            sis "Yeah sure."
            sis "I don't know where you've read that but that's not the best line you could have come up with."
            mc "I can feel it right now."
            mc "Or rather the memory of it."
            mc "It's sweet and bitter at the same time."
            mc "It makes me want to cry but its also comforting."
            scene ep5_sc14_pool_44
            sis "You're making it weird."
            mc "I've never felt anything like that, but now that I've tasted it, I can't live without it."
            sis "You have to stop with the big words."
            sis "If anything, you're ridiculous."
            mc "You may be right... But I don't care."
            mc "That sensation I get when I'm with you, I just want for it to last forever."
            sis "If you think that this kind of speech will get you into my pants, you're making a huge mistake."
            mc "It was worth a try though."
            mc "What did I get wrong ?"
            sis "You do remember that I'm your father's ward, right?"
            mc "I do."
            mc "One more reason to care for you."
            off "I expect a sarcastic reply but she keeps silent for a few seconds."
            off "She seems embarrassed."
            scene ep5_sc14_pool_45
            sis "There's something I want to do..."
            mc "I'm game."
            mc "What is it?"
            sis "If you mock me, I kill you."
            mc "I won't."
            off "She seems to hesitate and finally gets closer to me."
            scene ep5_sc14_pool_46
            off "She grabs my hand, sinks it into the water and looks away."
            off "It takes me almost a minute to understand that this is what she wanted... for us to hold hands."
            off "Weirdly, I feel as ashamed as happy."
            off "What a moron."
            off "I should have done it sooner."
            off "Her hand feels small and fragile."
            off "Holding it makes me want to smile."
            off "Memories suddenly crush me under their weight."
            off "Memories of happier times."
            off "Before all of the bullshit."
            off "I remember that I often held her hand at that time."
            off "And I think I liked it."
            off "How could I forget that?"
            off "Something so simple and yet so important?"
            off "Holding her hand, hugging her... loving her?"
            scene ep5_sc14_pool_47
            sis "So..."
            off "The sound of her voice wrenches me from my thoughts."
            off "Shy and embarrassed."
            mc "Yeah..."
            sis "If we... Keep going like this..."
            off "I don't like that \"if\"."
            mc "We keep going."
            off "She strengthens her grip on my hand."
            sis "How... What will we do... I mean... Our parents will be back soon..."
            mc "I know."
            off "I can't say I haven't thought about that."
            mc "Hiding from them won't be so different than hiding from [sf_name]."
            sis "And she caught us this morning."
            mc "Almost. She almost caught us."
            sis "Your mom would have..."
            mc "I know."
            off "You were pantiless and dripping on the floor."
            off "No doubt that Mom would have been... Intrigued, to say the least..."
            scene ep5_sc14_pool_48
            mc "It's not like we have a choice."
            mc "I don't want to let go of you."
            mc "You can forget this idea."
            mc "We'll hide for the time being."
            mc "In a few months, we'll be in college."
            mc "Things will be different."
            sis "We'll still have to hide from [sf_name]."
            mc "I guess so..."



            if sf_dom_path == True:
                off "I'm actually not so sure about that."
                off "She already knows about us so..."
                off "I'm more worried about you finding out about her and myself than the other way around..."
            else:
                off "[sf_name] will find out one way or another."
                off "It's inevitable."

            scene ep5_sc14_pool_49
            sis "... Maybe we could tell her..."

            if sf_dom_path == True:
                off "Here we go."
                off "Crap."
                off "I would have preferred to have some more time to prepare for this..."
                mc "Have you said anything to her yet ?"
                sis "No, of course not!"
            else:

                mc "I guess that's for you to decide."
                off "[sf_name] would never do anything that would hurt [sis_name]."
                off "Never."
                off "She would rather die."
                off "I'm sure of that."
                off "She'll keep our secret."
                off "But will she approve of our relationship?"
                mc "She's your friend."
                mc "I know you will make the right decision."



            sis "I never doubted we could trust her... it's just that... you know..."
            sis "We're not supposed to..."
            mc "You're ashamed."
            sis "No! I mean, I'm not ashamed of you! It's..."
            mc "It's okay."
            mc "It's not easy to overcome that."
            mc "You're afraid of what she would think of you."
            mc "I understand."
            mc "Take your time."
            scene ep5_sc14_pool_50



            if sf_dom_path == True:
                off "So that I can try to clarify the situation with [sf_name] beforehand..."
                off "At least, I want to know what she's going to do about it."
                off "She didn't seem angered by my relationship with [sis_name], but rather afraid that I could hurt her."
                off "I can't believe she won't do anything, but who knows?"
                off "I'll have to speak to her, as soon as possible."
                off "Anyway, [mc_name], you've clearly gone too far."
                off "I get that you're intrigued by [sf_name]'s behaviour, but you love [sis_name]."
                off "You have no doubt about it."
                off "So why push the bullshit that far?"
            else:
                off "I don't know what she could do but if she can help in anyway..."
                off "Accepting our relationship would already be great."
                off "We wouldn't have to hide in front of her anymore."
                off "That would be nice."
                off "Also, I have a feeling that [sis_name] desperately needs to talk about it with [sf_name]."
                off "She misses her friend."

            off "We stay like that for a moment."
            off "Holding hands without saying a word."
            off "It's peaceful."
            off "That makes me thinks that maybe we're missing something by going too fast."
            off "The faint noise of the doorbell gets me out of my thoughts."
            off "[sf_name] will probably take care of it but still."
            scene ep5_sc14_pool_51
            off "[sis_name] quickly releases my hand and steps further away from me."
            off "[sf_name]'s footsteps and voice breaks the mood a minute later."
            sf "[sis_name]? [mc_name]? I think you should come in."
            sf "We... have a visitor."
            jump ep5sc15
        else:

            scene ep5_sc14_pool_52
            off "The silence that takes place between [sis_name] and I is a bit awkward."
            off "We still have to adjust to our freshly renewed relationship as brother and sister."

            if ep4nighttalk == True:
                off "After all, we were like mortal enemies yesterday."
            else:
                off "After all, we were like mortal enemies a few days ago."

            off "I have no idea how to behave."
            off "I can't help but think that all this was one hell of a fucked up misunderstanding."
            off "All that time we have lost..."
            off "All the pain she went through..."
            off "That's crazy."
            scene ep5_sc14_pool_53
            mc "I have no idea how to behave."
            sis "What?"
            mc "I mean, with you."
            off "I don't really know what to expect from this conversation, but being honest seems like a good start for whatever could come after."
            scene ep5_sc14_pool_54
            sis "Me neither. It feels... weird... [sf_name] has been gone for a few minutes now and we haven't tried to kill each other yet..."
            mc "We just have to find something to talk about instead."
            sis "Yeah..."
            mc "Like what ?"
            sis "I don't know... We don't like the same things..."
            mc "Right... Maybe we should try to return to the basics."
            sis "The basics ?"
            mc "The basics. Like... I don't know... What do you like? What do you want to do later? What are your dreams? "
            scene ep5_sc14_pool_55
            off "She looks at me suspiciously."
            sis "Are you going to make fun of me ?"
            mc "No, of course not. I can start if you want me to..."
            sis "Oh, I want you to, please. I'm eager to hear what you have to say about yourself."
            mc "How about I tell you one thing and you tell me one ?"
            sis "Deal."
            mc "Ok, then... Let's see... "

            off "We probably already know what we're about to say but..."
            off "I guess we're not trying to learn anything."

            label ep5sc14neutraltalk:
                menu:
                    "[gr]I like cars and mechanics." if ep5discussionlevel == 1:
                        $ ep5discussionlevel += 1
                        mc "There's something simple and beautiful about the combustion engine..."
                        mc "I feel like I understand it."
                        sis "You're saying that you like explosions ?"
                        mc "More like the conversion of thermal energy into mechanical power."
                        scene ep5_sc14_pool_54
                        sis "I'm afraid that's a bit too nerdy for me."
                        sis "I like to run."
                        sis "One stride at a time I feel like it empties my mind."
                        sis "It's stupid but..."
                        sis "Sometimes when I run, I feel like I'm joining with the wind and it takes me away from my problems... it's almost like I was flying..."
                        scene ep5_sc14_pool_56
                        sis "It's stupid."

                        menu:
                            "No, it's not. [sisLovePath]":
                                $ ep5neutralrunning = True
                                $ ProcessStat(2, "sis_affection")
                                $ DumpNotStack()
                                mc "Not at all. I think I can understand that feeling."
                                off "And it really seems to have some special meaning for her."
                                off "I never imagined that running was that important to her."
                                off "Maybe I should try running myself."
                                $ ProcessStat(2, "sis_affection")
                                $ DumpNotStack()
                            "As long as the wind doesn't take you away from us... [sisSubPath]":

                                $ ep5neutralcare = True
                                $ ProcessStat(2, "sis_submission")
                                $ DumpNotStack()
                                off "She looks at me a bit surprised."
                                sis "Yeah... I guess I'll be careful..."
                                off "Why did I say that? I thought it would be sweet but she didn't seem to appreciate it."

                    "I like Don Giovanni's pizzas." if ep5discussionlevel == 1:
                        $ ep5discussionlevel += 1
                        $ ep5neutralpizza = True
                        mc "He always put a lot of cheese on it."
                        scene ep5_sc14_pool_54
                        sis "I like cheese a lot."
                        sis "The cheesier the better."
                        mc "These pizzas are great."
                        sis "The one with bacon on it is my favourite."
                        mc "I'm hungry now."
                        sis "I am too."
                        $ ProcessStat(1, "sis_affection")
                        $ DumpNotStack()
                        off "She lightly laughs."
                        off "We like the same pizzas."
                        off "It's nothing."
                        off "And we're already aware of that, but simply saying that we are actually agreeing with each other feels strangely nice."
                        off "That's stupid."
                        off "I'm probably making this up."
                        off "When did I become so sensitive?"


                    "[gr]I like video games." if ep5discussionlevel == 2:
                        $ ep5discussionlevel += 1
                        mc "FPS, RPG, I can play almost anything."
                        mc "I don't really like PvP games as I'm very bad at those, I can't stand to lose."
                        scene ep5_sc14_pool_57
                        sis "I didn't understood a thing."
                        sis "What are FPS, RPG and the other things ?"
                        mc "They are different kinds of game."
                        mc "Games where you shoot at things, role-playing games..."
                        mc "PvP games are games where you compete against other people."
                        scene ep5_sc14_pool_59
                        sis "Ok. I guess I wouldn't like that kind of game either..."
                        sis "I mean, I don't like to compete."
                        sis "I don't play video games, though..."
                        sis "I like the books."
                        sis "And stories..."
                        scene ep5_sc14_pool_54

                        menu:
                            "There are some good stories in games too. [sisSubPath]":

                                $ ep5neutralvn = True
                                mc "I bet you would enjoy some."
                                mc "Some RPG, or maybe some visual novels..."
                                sis "Visual novels?"
                                off "Moron, why did you mention those?"
                                off "How are you going to explain that to her?"
                                mc "Yeah, it's... well... it's... like a novel, with pictures and choices you can make that will change the story..."
                                mc "It's... They're often... You know... Porn games..."
                                mc "But the stories can still be good..."
                                scene ep5_sc14_pool_58
                                sis "Porn?"
                                sis "You want me to play porn games?"
                                mc "I don't know..."
                                mc "I never played any of those obviously..."
                                sis "Yeah obviously..."
                                off "She looks amused."
                                sis "Maybe if you have any good ones you can recommend to me..."
                                $ ProcessStat(3, "sis_submission")
                                $ ProcessStat(2, "sis_affection")
                                $ DumpNotStack()
                                mc "Well, I... I can look for some I guess..."
                                off "Am I really going to select some porn games for her to play?"
                                off "Great."
                            "I know that you're reading a lot... [sisLovePath]":

                                $ ep5neutralthomas = True
                                mc "... But I have no idea what kind of books you like."
                                mc "What genre ?"
                                sis "I don't know... I mean, I like novels. The genre isn't important as long as the story is good."
                                mc "Ok, but you must have a favourite book, don't you?"
                                off "She seems embarrassed."
                                scene ep5_sc14_pool_59
                                sis "Yeah... It's... It's not a novel... It's a collection of poems by Dylan Thomas."
                                off "I have no idea who Dylan Thomas is."
                                off "I feel a bit dumb and uncultured."
                                mc "I've never heard of him."
                                mc "Maybe you could lend it to me? I'm curious."
                                scene ep5_sc14_pool_57
                                off "She looks at me with surprise and suspicion."
                                sis "You would read it?"
                                mc "Of course."
                                mc "Or at least I'll try."
                                mc "I told you, I'm curious."
                                off "Her expression changes to a faint smile."
                                $ ProcessStat(3, "sis_affection")
                                $ ProcessStat(2, "sis_submission")
                                $ DumpNotStack()
                                sis "Ok then... I'm curious to know what you will think of it..."
                                off "I just hope I'll be able to read it... I don't think I've ever really read poetry..."






                    "I listen to almost any kind of music." if ep5discussionlevel == 2:
                        $ ep5discussionlevel += 1
                        $ ep5neutralmusic = True
                        mc "However... This is a secret, you absolutely can't tell anyone, ok ?"
                        mc "I have a sweet spot for K-pop music videos."
                        mc "The music is nice and well... I like... Many things in it."
                        scene ep5_sc14_pool_55
                        sis "K-pop? Really?"
                        $ ProcessStat(3, "sis_affection")
                        $ DumpNotStack()
                        mc "Yeah, yeah... Less mocking, more answering, please."
                        sis "You're right, sorry..."
                        sis "I'm very eclectic too..."
                        sis "But I think I like old-school rock the most."
                        mc "How old are we talking about?"
                        scene ep5_sc14_pool_54
                        sis "My favourite song is probably California Dreamin'."
                        sis "I know, that's a bit of a cliché but... I just like it."
                        sis "It was released in the '60s..."
                        off "It's beyond old..."
                        off "Our grandparents were barely born..."
                        mc "I'm not even sure I ever heard that song."
                        sis "I'm sure you have."
                        sis "It's very well known."


                    "When I'm done with college..." if ep5discussionlevel == 3:
                        $ ep5discussionlevel += 1
                        $ ep5neutralwriting = True
                        mc "I'll try to find a job as a mechanical engineer or something like that."
                        mc "But I'm pretty sure I would be ok to work as a mechanic."
                        scene ep5_sc14_pool_58
                        sis "You love mechanics so I guess it's not surprising."
                        mc "I guess so... What about you?"
                        scene ep5_sc14_pool_59
                        sis "I ... Don't know... I mean..."
                        sis "If I get into college, I'll probably go for English Literature."
                        sis "Maybe... Some creative writing if I can..."
                        off "Creative writing?"
                        off "Like in writing stories?"
                        off "I had no idea she was interested in that..."
                        sis "I have no idea what I'll do after that..."
                        sis "Maybe I'll try to... Write a book..."
                        scene ep5_sc14_pool_56
                        sis "That's stupid."
                        mc "No, no, it's not stupid."
                        mc "It really is not."


            if ep5discussionlevel < 4:
                scene ep5_sc14_pool_54
                off "What else can I tell her?"
                jump ep5sc14neutraltalk


            scene ep5_sc14_pool_54
            off "She hides it well, but she actually has very low self-esteem."
            off "All those times she was yelling at me and calling me a moron, I thought that she was arrogant and pretentious."
            off "But she looks very different now."
            off "I've been an imbecile."
            off "All this time we have lost..."
            scene ep5_sc14_pool_57
            mc "I want to read that book."
            sis "Which one ?"
            mc "The one you'll write."
            mc "I'm sure it'll be great."
            $ ProcessStat(5, "sis_affection")
            $ DumpNotStack()
            scene ep5_sc14_pool_60
            off "Her face seems to brutally convulse for a second before she bursts out crying."
            scene ep5_sc14_pool_61
            off "She turns her back to me and hides."
            off "Her tears surprise me."
            mc "Hey. I'm sorry. Did I say something wrong ?"
            sis "No. No... I'm okay... I just have something in my eye."
            mc "Yeah, sure, lamest excuse ever... You're crying."
            sis "No, I'm not. I just have something in my eye, okay?"
            off "I'm thinking about trying to hug her to comfort her when [sf_name]'s footsteps and voice startle me."
            off "[sis_name] quickly washes off her face with the pool water and immediately gets out of the pool."
            sf "[sis_name]? [mc_name]? I think you should come in."
            sf "We... have a visitor."
            jump ep5sc15



label ep5sc15:



    if (ep4kfmeetingok == True and ep4kflatetold == False) or  ( ep4kfmeetingok == False and ep4morningkftold == False ):
        $ ep5kfgirlsunknown = True

    if ep2cameraset == True or ( ep2sissleepingmovie == True and ep3handshaked == True ):
        $ ep5kfnew = True


    scene black with dissolve
    with Pause(2)



    if moronic_hero_path == True:
        off "I've barely set foot in the house that I can hear [sis_name] yelling at me."
        sis "[mc_name] ?"
        off "Shit. I can feel it."
        off "I'm in for a rough ride."
        off "[sf_name] probably understood where I was going and told [sis_name] everything."
        off "They're going to kill me."
        off "Well, I probably kind of deserve it as that bullshit felt useless in the end."
        off "I'm not sure that the police will really do anything to help us."
        scene ep5_sc15_lr_23 with dissolve
        mc "Hey girls."
        off "[sis_name] looks angry."
        off "[sf_name] is more composed."
        off "As usual."
        off "They both stand up."
        off "[sis_name] storms up to me."
        sis "Where the fuck were you?"
        mc "I ..."
        sis "Oh don't even try to lie to me, you moron."
        sis "[sf_name] already told me everything."
        mc "Ok..."
        off "Why do you ask then?"
        scene ep5_sc15_lr_24
        off "She suddenly gets closer."
        sis "How can you be so dumb ?"
        scene ep5_sc15_lr_25
        off "I don't even see it coming."
        off "She hits me so hard that I feel like my cheek has just exploded."
        off "My whole face suddenly burns."
        off "I can feel the pain quickly progressing through my entire skull."
        mc "What the...?"
        scene ep5_sc15_lr_26
        off "She hugs me and starts crying. "
        sis "How the fuck can you be so dumb?"
        sis "Do you have any idea how much you scared me?"
        off "She sobs and trembles uncontrollably."
        off "What do I do now?"
        off "I have no idea what to do with my hands."
        off "Should I return the hug?"
        off "Is she going to hit me again if I touch her?"
        scene ep5_sc15_lr_27
        mc "Are you ok, Princess?"
        sis "They could have killed you!"
        sis "Moron!"
        off "I haven't held her like this for years."
        off "It feels... strangely good."
        mc "But they didn't so..."
        sis "So nothing!"
        sis "You're an imbecile."
        off "My jaws hurt."
        off "She put everything she had in that slap."
        off "I'm lucky she didn't break my face."
        mc "Yeah... It wasn't very smart... I just wanted to..."
        sis "I know. You didn't need to do that!"
        off "I feel like I'm going to cry too..."
        mc "Well, I fucked up... and that seemed like a good way to fix things..."
        sis "No, it wasn't."
        $ ProcessStat(10, "sis_affection")
        $ DumpNotStack()
        off "[sf_name] slowly approaches us."
        scene ep5_sc15_lr_28
        sf "You are a moron, [mc_name]."
        sf "You know that?"
        sf "You are lucky you got out of that alive."
        mc "I didn't think I had a choice... I thought it was the only way..."
        sf "The only way to do what?"
        mc "As I said... To fix... The things I fucked up..."
        sf "Like your relationship with [sis_name]?"
        mc "Yeah..."
        sf "Did you try to apologize?"
        sf "To say you were sorry like you mean it, for once?"
        mc "I thought... That I was... Way past that point..."
        sf "You were not."
        sf "Moron."
        $ ProcessStat(5, "sf_affection")
        $ DumpNotStack()
        off "[sis_name] tightens her grip on me."
        off "She has stopped trembling but still sobs."
        off "[sf_name] silently exits the room and leaves us alone."
        scene ep5_sc15_lr_29
        mc "I'm sorry."
        sis "Dumbass."
        off "It's strange how that word can suddenly sound affectionate."

        jump ep5sc18


    if dual_love_path == True:

        off "I swiftly make my way to the entrance, wondering who may wait at the door."
        off "We're not expecting anyone."
        off "Steve is still away and [sf_name] is here with us."
        off "I don't see anyone who could drop by unexpectedly."
        scene ep5_sc15_ent_01 with dissolve
        mc "Kelly?"
        kf "Hello, [mc_name]."
        mc "Hello, yes, of course... Sorry, I'm a bit surprised..."
        kf "I'm the one who should apologize."
        kf "I should have called before dropping by... I'm sorry..."


        if ep4kfcompassion == True:
            mc "How are you?"
            mc "Is everything alright ?"
            kf "I'm not sure..."
            off "Well, that's an intriguing response."
            mc "You're not sure?"
            off "She looks embarrassed?"
            off "Perhaps even a bit afraid?"
            off "Did something happen to her?"
        else:
            off "What does she want?"


        if ep4kfmeetingok == True:

            off "I've never thought I would see her again after yesterday..."
            off "Or at least not so soon..."

        elif ep4kfmeetingok == False:
            off "I thought I was pretty clear when I rejected her..."


        if ep5kfgirlsunknown == True:
            off "Fuck."
            off "I should have told the girls about her."
            off "If they see her, it's gonna be a shit show."
            off "The situation is already complicated enough..."

        scene ep5_sc15_ent_02
        kf "I'm really, really sorry, I hope I'm not bothering..."
        mc "You're not bothering me, Kelly."
        mc "But I'm wondering why you're here..."
        kf "I've come to talk."
        kf "I have several things to tell [sf_name], and [sis_name]... and you."

        if ep5kfgirlsunknown == True:
            off "Fuck me."
            off "She wants to talk to the girls."
            off "Can I refuse?"
            off "It wouldn't do any good."
            off "She'll just give them a phone call and they will know everything."

        mc "You have something to tell us?"
        mc "Ok... I guess it's important, or you wouldn't have come here ?"
        kf "Yes... It's... It's about Luke and Ray."
        kf "I came to warn you... and also ... I think you deserve some explanation."

        if ep4kfcompassion == True:
            off "That sounds very serious."
            off "Something definitely happened."

        if ep5kfgirlsunknown == True:
            off "FUCK ME."
            off "I have even less of a choice."
            off "Can I ask her to act as if we don't know each other?"
            off "That sounds like a terrible idea."
            off "I guess I'll just grit my teeth and bear it."


        if ep4kfmeetingok == False:
            mc "Ok... That sounds very serious..."


        scene ep5_sc15_ent_03

        mc "Let me show you to the living room."
        mc "I'll then call [sis_name] and [sf_name] to join us."
        kf "Thank you, [mc_name]."

        scene black with dissolve
        with Pause(2)
        show text "A minute later."
        with Pause(2)

        scene ep5_sc15_lr_01 with dissolve

        sis "Kelly?"
        sis "What are you doing here?"
        kf "Hello, [sis_name], [sf_name]."
        sf "Hello, Kelly."
        sis "Yeah, Hello..."
        sis "What are you doing here?"
        sf "[sis_name], please."
        sf "There's no need to be rude."
        sf "Let's sit."
    else:


        off "We quickly dry ourselves and head into the house."
        scene ep5_sc15_lr_01 with dissolve
        off "Our guest wait for us in the living room."


        if ep5kfnew == True:
            off "Who's that?"
            off "Holy crap, she's cute."
        else:




            if ep5kfgirlsunknown == True:
                off "Holy shit."
                off "Just as things were going nicely..."
                off "Brace yourself for a new shitstorm, [mc_name]."
                off "Goddammit, I should have told the girls about her."

            off "What is she doing here?"

            if ep4kfmeetingok == True:
                off "I've never thought I would see her again after yesterday..."
                off "Or at least not so soon..."
            else:
                off "I thought I was pretty clear when I rejected her..."


            if ep4kfcompassion == True:
                off "She seems embarrassed."
                off "Perhaps even a bit afraid..."
                off "Did something happen to her?"


        sis "Kelly?"
        sis "What are you doing here?"
        kf "Hello, [sis_name]... Hello, [mc_name]."



        if ep5kfnew == True:
            off "She knows my name?"
            mc "Hi... do we know each other ?"
            kf "No, but I know who you are."
            kf "You're [sis_name]'s friend."
            sf "[mc_name], this is Kelly."
            off "That name sounds familiar."
            mc "Nice to meet you, Kelly."
            kf "Nice to meet you too, [mc_name]."
            sis "Yeah, ok. Hello Kelly."
            sis "What are you doing here?"
            sf "[sis_name], please. There's no need to be rude."
            sf "Let's sit."
        else:

            mc "Hello, Kelly."

            if ep5kfgirlsunknown == True:
                off "I can feel [sis_name] and [sf_name]'s suspicious gaze on me."
                off "It's done."
                off "They have already understood."

            sis "Ok... Hello Kelly."
            sis "What are you doing here?"
            sf "[sis_name], please. There's no need to be rude."
            sf "Let's sit."

    scene ep5_sc15_lr_02


    kf "I'm very sorry to intrude..."
    sf "Kelly, please, stop apologizing."
    sf "You're not bothering us."
    sf "You came here to tell us something."
    sf "We're listening."
    off "[sis_name] is clearly on a defensive stance, but [sf_name] is acting on a more civilized fashion, with a polite smile and a welcoming tone."
    off "Kelly doesn't dare to look at them eye to eye."
    off "She clearly isn't comfortable."
    scene ep5_sc15_lr_03
    kf "First, I want to thank you again, for coming to my party, last Monday..."
    kf "I already told you that but I was very happy that you came."
    kf "I have to apologize for the behaviour of my other guests that night."
    kf "It didn't go... as well as I hoped..."

    if ep5kfnew == True:
        off "I get it now, she's THAT girl."

    sf "It's okay."
    sf "We were curious but didn't expect much."
    sf "Hence we were... A bit surprised by your behaviour, but not disappointed with theirs."
    kf "I'm so sorry..."
    sis "Will you stop with the sorry thing already?"
    sis "You're saying it so much that it's getting tiresome."
    sis "We won't believe you more if you keep saying it."
    sis "If anything, you're going to anger me!"
    off "That's quite harshly said."
    off "But I kind of understand."
    sf "As [sis_name] just said, you've already apologized enough."
    kf "I'm sorry, I can't help myself..."
    scene ep5_sc15_lr_04
    off "She realizes what she has just said and looks even more embarrassed."
    off "It's almost comical."
    off "It takes her a few seconds to regain some composure, but it's enough to relax the atmosphere a little."
    off "[sis_name] sighs loudly."
    sis "So... you had something to tell us?"
    kf "Yes... I have many things to tell you."
    kf "I don't really know where to start..."
    kf "I was at home, earlier this afternoon when Luke and Ray dropped by."
    kf "They barely said hello before asking me to set up another party so that they could approach you again, [sf_name]."
    scene ep5_sc15_lr_05
    sf "Me ?"
    kf "Yes... they were behaving very... weirdly."
    kf "At first, I thought that they could be on drugs or something."
    kf "They were frantic."
    kf "They told me that I was their last chance, that they needed my help."
    kf "Of course, I refused."
    kf "You and [sis_name] made it very clear that you weren't interested in them."
    kf "And they were acting so strange..."
    kf "It became obvious that you were right about them, and that I was wrong."

    off "Shit."
    off "Does that mean that the psycho twins are on the move?"
    scene ep5_sc15_lr_06
    kf "I've known them for a long time."
    kf "Since we were children."
    kf "I always thought that their father was a friend and a subordinate of my father... but I'm not so sure anymore..."
    kf "They were invited to every barbecue, birthday, things like that."
    kf "They were nice guys."
    kf "Sometimes their jokes were a little off... but they never were... like that."
    kf "When they showed up at my door today... they had nothing to do with the Luke and Ray I knew."

    off "I guess you didn't expect them to become some sick rapist assholes."
    scene ep5_sc15_lr_07
    kf "I told them to calm down and to leave you alone."
    kf "And they became more... aggressive."
    kf "Then yelled at me."
    kf "They asked why I was trying to protect you."
    kf "They said that I should be on their side after what you and your father have done to them, and to my own family."
    kf "That's when I understood what all this is about."

    off "[sf_name] frowns."
    off "She's about to say something but Kelly doesn't let her."
    scene ep5_sc15_lr_08
    kf "I know you haven't done anything."
    kf "Neither has your father."
    kf "I told them that."
    kf "I told them that they were mistaken."
    kf "Luke was so angry."
    kf "He started to insult and threaten me, saying that I was a slut and that maybe... they should... fuck me instead."

    off "Holy shit."
    off "Did they threaten to rape her?"

    kf "At some point, Luke raised his hand and I think he was about to hit me."
    kf "Ray stopped him and dragged him away."
    kf "After that, I came here as fast as I could."
    kf "To warn you... they are... Dangerous."

    off "It's a miracle she got out of there alive..."
    off "Ray may still have a bit of brain, but Luke seems to have completely lost it."
    scene ep5_sc15_lr_09
    sis "So they were after [sf_name] all this time?"
    kf "I think so."
    mc "You were together at the club."
    mc "Both your drinks were probably loaded, but as [sf_name] refused to drink..."
    mc "After that, I guess that they tried to use the little contact they had with you, to get to [sf_name]."
    sis "They used me..."
    sf "No, they didn't."
    sf "They tried."
    sf "But they failed, ok?"

    sis "I'm so sorry, [sf_name]."
    sis "I got you into trouble..."
    sf "No, you didn't."
    sf "You haven't done anything."
    sf "Why would you apologize for something they have done?"

    scene ep5_sc15_lr_10
    mc "Ok... so... What is this all about?"
    mc "I mean... Why do they want to hurt [sf_name] so bad?"
    mc "I guess there's a reason, right?"
    mc "Probably a bad one, of course..."

    off "Kelly takes a deep breath."
    off "She looks at her feet."
    kf "It would be because of my dad."
    off "Her voice is barely more than a whisper."
    sis "What have you done?"
    sf "[sis_name], please..."
    off "[sf_name] doesn't smile anymore but she remains calm and composed."
    off "She dominates the discussion with some kind of gentle benevolence."
    scene ep5_sc15_lr_11
    sf "It's about something my father supposedly did. Isn't it?"
    off "Kelly shyly nods."
    sf "My dad... is a fixer."
    sf "When a company is in trouble, they hire him to control and correct the problem."
    sf "Three years ago, he was hired by Knave Structured."
    sf "It's a big company who has its roots in this city."
    sf "I guess your father and their fathers were employed in that company too. Am I right?"
    off "A second nod."
    sf "My father is hired by companies who may have very diverse difficulties."
    sf "Sometimes these difficulties are economic."
    sf "Which means that he is hired at a time where others are losing their jobs."
    off "Third nod."
    scene ep5_sc15_lr_12
    sf "But firing people isn't part of my dad's work."
    kf "Things... are a little more... Complicated..."

    kf "My father... was the head of a department of Knave Structured that got completely laid off when your own father got hired."
    kf "Luke's father was working under him."
    kf "When the news got out that they were going to lose their jobs, my father stepped in and proposed to negotiate with the higher-ups."
    kf "But... It didn't turn out well."
    scene ep5_sc15_lr_13
    kf "The entire department was fired with minimal compensation."
    kf "My father came back from the negotiation, explaining that he couldn't do anything, that he was forced to sign the deal."
    kf "Your father was newly hired, and... my dad put the blame on him."
    sis "But your dad didn't do anything, right, [sf_name] ?"
    sf "As I said, my father doesn't fire people."
    sf "He doesn't negotiate that kind of thing either."
    scene ep5_sc15_lr_14
    sf "His work is about communication, advice and counselling, relations with investors and banks, he finds money to fund things."
    sf "If anything, he hires people, he doesn't fire them."
    kf "My father lied."
    off "She briefly looks at me, totally distraught."
    kf "He... conned his entire department."
    kf "He negotiated a deal for himself."
    kf "He was given a lot of money, in exchange for minimum compensation for the rest of his staff."
    kf "He basically robbed them and blamed everything on your dad, [sf_name]."
    off "I can feel her pain."
    off "She's ashamed of her father's sins."
    scene ep5_sc15_lr_15
    kf "I... I have... Confused memories of him talking with mom."
    kf "I knew we had money... but I believed him."
    kf "I understood what he did last year..."
    kf "After being let go from Knave Structured, he quickly found an equivalent job at another company..."
    kf "And last year... one day... he just didn't come back from work."
    scene ep5_sc15_lr_16
    kf "The cops came in his stead."
    kf "They searched our house."
    kf "My father had stolen millions from his company and had fled with his secretary."
    kf "A lot of things became... Obvious... that day."
    off "So... her father is a conman who has abandoned Kelly and her mother."
    off "How nice..."
    sf "But Luke and Ray still think that my dad cheated their father of his remuneration."
    kf "Yes. They chose to... ignore the truth."
    kf "I told them that your father didn't do anything but..."
    kf "They didn't want to listen."
    kf "It's... They have... I know that their father had trouble finding a new job..."
    scene ep5_sc15_lr_17
    kf "And their mother... She died from cancer sometime last year."
    kf "They never made any direct accusation, but..."
    kf "I heard them a couple times, saying that maybe, with more money, they could have saved her..."
    kf "After that, their father sank into depression and..."
    kf "He committed suicide 6 months ago."

    off "I'm not going to pity them but..."
    off "I have to admit that it's one hell of a shitty life."

    kf "Maybe that made them snap."
    kf "I don't know..."
    scene ep5_sc15_lr_18
    mc "Maybe they hold your father responsible for their parents' death."
    mc "Maybe they want to get some kind of revenge on him by hurting you, [sf_name]."
    kf "That's the only explanation I can think of."
    kf "They're not the guys I knew any more."
    kf "They've clearly became... insane."
    kf "They frightened me."
    kf "This afternoon, it was obvious that they were ready for the worst..."
    kf "I think they're going to try something."
    kf "I'm afraid that... They're going to get violent."
    sis "So... they are crazy and violent, and they want to hurt [sf_name]."
    kf "I think they're crazy enough to hurt anyone who stands in their way."
    sis "Great."

    off "The silence settles in for several seconds."
    off "Everyone is probably searching for something to say, or to do."
    scene ep5_sc15_lr_19
    sf "Do you think they'll try to assault my father ?"
    kf "I don't know... They seemed obsessed with you."
    kf "Also... You're probably an easier target than your father."

    mc "We should go to the police."
    mc "Immediately."
    mc "Could you come with us, Kelly?"
    mc "If you could repeat everything you just said to an officer..."
    kf "Yes, yes of course."
    scene ep5_sc15_lr_20
    sis "Wait, guys, could we talk for a second? In private ?"
    mc "In private?"
    off "What is there to discuss?"
    scene ep5_sc15_lr_21
    sis "Yes, please."
    sf "Excuse us, Kelly."
    kf "Oh sure."
    off "[sis_name] and [sf_name] head to the kitchen."
    off "I don't really see the point of it but I follow them."
    off "I guess we're going to discuss if we should believe her or not."
    off "The answer should be more than obvious."

    scene black with dissolve
    with Pause(2)
    scene ep5_sc15_k_01 with dissolve
    sis "So... what do you think?"
    mc "What do you mean?"
    mc "Kelly has been pretty clear."
    mc "We should go to the police."
    sis "Yeah, sure."
    scene ep5_sc15_k_02
    sis "Do we even believe her to begin with?"
    mc "Why would she even lie about it?"
    sis "I don't know..."
    sis "She lied about so many things..."
    mc "She has apologized and I thought that you were considering accepting her apologies."
    sis "And I'm considering it."
    scene ep5_sc15_k_03
    sis "But I can still be careful, can't I?"
    mc "Sure, of course you can."
    mc "It's just that I don't see why she would warn us if she was on the psycho twins' side or anything like that."
    sis "Yeah, but we know nothing about her motives..."
    mc "To protect you, and [sf_name]!"
    mc "She's trying to make amends!"
    sis "Yeah, I feel like you're falling a bit too easily for her cute little face."
    mc "What?"
    scene ep5_sc15_k_04
    sis "I've seen how you look at her."
    mc "I can't believe it."
    mc "Are you jealous?"
    sis "Me? Jealous? Of Her? Please!"
    mc "It sure looks like it!"
    sis "In your dreams maybe."

    if ep5kfnew == False  and ep5kfgirlsunknown == True:

        sis "And what was that?"
        sis "You already know each other?"
        sis "Do you have anything to tell us, [mc_name]?"
        off "Shit."
        off "Here we go again."

        menu:
            "No. [gr]\[FurtherLie\]":
                $ ep5furtherlie = True
                mc "I mean... we probably bumped into each other at school..."
                mc "I know her face and her name, nothing more."
                sis "Yeah sure."
                sis "And I'm supposed to believe you?"
            "Ok.":
                mc "You're right."
                mc "I know her."
                mc "But we should talk about that later."
                mc "We have a more urgent matter to attend to right now."
                mc "Don't you think?"
                sis "How convenient for you."

    scene ep5_sc15_k_05
    mc "Please..."
    menu:
        "I think she's being honest. \[KfTrust\]":
            $ ep5kftrust = True
            mc "She's trying very hard to get some forgiveness from both of you."
            mc "She really feels bad for what she has done."
            mc "I'm not saying that you should forgive her, but today, she's not here to trick you."
            mc "She's trying to save you."
            mc "I think she's sincere."
            mc "She's trying to redeem herself."
        "You have some good reasons to hate her.":

            mc "But she came to warn us."
            mc "If there's even the slightest chance that she's telling the truth, we have to go to the police."
            mc "Because if we ignore her warning, we would be just sitting here waiting for the psycho twins to come in and rape the both of you before killing us all."
            mc "That would be stupid."
            mc "We've already had hints that they're crazy and do not have the best of intentions towards us."

    scene ep5_sc15_k_06
    sf "Enough, please."


    if dual_love_path == True:
        sf "You both know that I absolutely love to see you flirt like that..."
    else:

        sf "You both know that I absolutely love to see you bicker like that..."

    sf "... But I think that [mc_name] is right."
    sf "We should trust her."
    sf "I don't see how her warning us could hurt us."
    sis "And what if she's trying to hurt them?"
    sis "Maybe all this is just a lie and she wants to use us against those two guys ?"
    mc "Come on."
    mc "She's a girl who lied about you, ok, but she's not some kind of evil genius."
    mc "And besides, even without her warning, we already know that these two guys are up to no good."
    sis "Are we sure about that?"
    sf "Yes. We are sure."
    off "[sis_name] looks at [sf_name] for a few seconds before lowering her eyes."
    sis "So... what do we do ?"
    sf "We go to the police."
    off "We should have gone Sunday morning."
    off "We're probably lucky that nothing awful has happened since then."
    sis "Are you... Going to call your father?"
    sf "I should... He has to know."
    sf "I'll call him once we're done with the police."
    sis "He'll probably ask you to go home immediately."
    sf "He will. But he trusts me."
    sf "If I tell him that I'm safe here."
    sf "He'll let me stay."
    sf "However, I should really go back home."
    sf "At least you would be safe."
    mc "That's a very bad excuse and we're not even sure about that."
    mc "Don't even think about it."




    if sf_love_path == True:
        off "She sighs and suddenly looks smaller."
        sf "I'm sorry."
        sf "I'm the one who got you into trouble..."
        sis "What are you talking about?"
        sf "I've put [sis_name] in danger."
        mc "No, you didn't."
        mc "It's just as you said before."
        mc "Do not apologize for what they have done."
        mc "They are the crazy ones."

    if dual_love_path == False and sf_love_path == True:
        scene ep5_sc15_k_07
        off "I grab her and pull her to me. I hug her as she buries her face in my shoulder."
        mc "It's ok. It's over now."
        mc "We're going to the police and everything will be alright after that."
        mc "They'll arrest them and we won't have to worry any more."
        if sis_sub_path == True:

            scene ep5_sc15_k_08
            off "I extend my arm to grab [sis_name] and draw her to us."
            off "She joins us without protesting."
        mc "We're going to be alright."
        mc "I promise."
    elif dual_love_path == True:

        scene ep5_sc15_k_08
        off "I manage to grab both [sf_name] and [sis_name] and draw them to me."
        mc "It's ok. It's over now."
        mc "We're going to the police and everything will be alright after that."
        mc "They'll arrest them and we won't have to worry any more."
        mc "We're going to be alright."
        mc "I promise."
    else:

        mc "It's ok. It's over now."
        mc "We're going to the police and everything will be alright after that."
        mc "They'll arrest them and we won't have to worry any more."
        mc "We're going to be alright."
        mc "I promise."

    scene black with dissolve
    with Pause(2)
    show text "A few minutes later."
    with Pause(2)
    scene ep5_sc15_lr_30 with dissolve
    off "Kelly stands up from the sofa as we enter the room."
    mc "Kelly, we're going to the police."
    mc "Can you come with us ?"
    kf "Yes. I'll tell them everything."
    mc "Thank you."
    mc "We will get changed quickly and I'll get the car ready."

    jump ep5sc16


label ep5sc16:
    scene black with dissolve
    with Pause(2)
    show text "Later - The police station."
    with Pause(2)
    scene ep5_sc16_po_01 with dissolve

    off "We had to wait almost an hour before an officer took the time to listen to us."
    off "We explained the situation a couple of times already."
    off "The officer doesn't seem overly concerned."
    off "He keeps asking questions and taking notes but he doesn't look very convinced."
    off "I have a feeling he doubts us."
    scene ep5_sc16_po_02
    ms "So, let me get the situation straight once more."
    ms "You think that these two guys want to assault you, probably rape you, and maybe even kill you."
    ms "You think that they have already tried to drug you when you encountered them in a club, last Saturday."
    ms "You have reasons to think that they followed you home and spied on you."
    ms "Is that right?"
    sf "Yes, sir."
    off "He turns to Kelly."
    scene ep5_sc16_po_03
    ms "On the other hand, they reached out to you to get in touch with them."
    ms "They looked very disturbed and, as you refused to help them, they got angry."
    ms "They insulted you and threatened to rape you."
    ms "One of them raised his hand on you but was stopped by his brother who dragged him out of your house."
    ms "Am I correct ?"
    kf "Yes, sir."
    ms "You think they want revenge on Mr Carter through his daughter."
    ms "You think that they hold him responsible for the death of their parents."
    kf "Yes."
    off "The officer keeps silent for a few seconds, looking at his notes."
    scene ep5_sc16_po_04
    ms "Why didn't you go to the police on Sunday morning, if you thought that they may have drugged you?"
    off "The question surprises [sis_name]."
    sis "I... We... we thought that... We didn't have any proof..."
    sis "We thought it was... Useless."
    off "No doubt we should have come sooner."
    ms "What makes you think that you had been drugged?"
    sis "I..."
    scene ep5_sc16_po_05
    sf "She was in a comatose state."
    sf "I had to carry her to the car, with the help of a bouncer."
    ms "How many drinks did you have at that club ?"
    sis "I don't know for sure... A couple ?"
    sf "She drank two cocktails."
    ms "Miss Carter, please, let her answer."
    mc "How do you want her to answer that?"
    mc "She was drugged!"
    mc "She doesn't remember the end of the night!"
    off "Is he dense? Or what?"
    off "The officer sighs before going back to Kelly."
    scene ep5_sc16_po_06
    ms "Miss Kowalsky, were you alone when they came to your house earlier today?"
    kf "Yes... I... My mom is hospitalized..."
    kf "I'm currently living alone..."
    ms "What makes you think that your friends want to sexually assault Miss Carter?"
    kf "They were very explicit... I mean... Their threats..."
    kf "They threatened to rape me instead of [sf_name]."
    kf "That was very clear..."
    ms "And you think that they would have done it?"
    ms "What makes you think that it wasn't just a figure of speech?"
    off "That officer is a complete moron."
    off "His questions are insulting."
    scene ep5_sc16_po_07
    kf "I've already told you... They weren't kidding."
    kf "I was afraid and I genuinely felt threatened..."
    kf "I honestly think that they were serious..."
    kf "I don't know what more you need..."
    kf "Luke was about to hit me."
    kf "Without Ray, maybe I wouldn't even be here now."
    ms "Did you fear for your safety, and your life?"
    kf "Yes, I did."
    off "I can't take any more of this shit."
    scene ep5_sc16_po_08
    mc "Come on, officer."
    mc "It's the third time she's told you that."
    mc "You cannot be serious."
    mc "How many times do we have to repeat ourselves?"
    mc "They're dangerous!"
    mc "They want to rape, and maybe even kill [sf_name], and probably anything that would stand in their way!"
    mc "Kelly truly feared for her life!"
    mc "Is that so hard to understand?"
    mc "What more do you need?"
    off "I didn't intend to, but I end up yelling at him."
    off "I'm out of patience and self-control."
    ms "Mr Archer, please, calm down."
    ms "I need precise and consistent answers."
    mc "Yeah, sure! You're interrogating us like we are the culprits!"
    mc "We are the victims for god sake!"
    sf "[mc_name], please. Calm down."
    sf "This officer is only doing his job."
    off "I don't know how she does that but [sf_name] manages to stay perfectly calm."
    mc "Sorry. I just... I just feel like you're not taking us seriously."
    ms "I assure you that I take this matter very seriously."
    ms "I'm just following basic procedure."
    scene ep5_sc16_po_09
    off "He stands up."
    ms "Alright, I think I have enough information for now."
    ms "We're going to investigate."
    off "Investigate?"
    mc "Wait... investigate?"
    mc "Aren't you going to arrest them immediately?"
    ms "We're going to investigate and we'll take the appropriate actions."
    scene ep5_sc16_po_10
    mc "You cannot be serious!"
    mc "Didn't you understand anything we've said?"
    mc "They're going to try something!"
    mc "You have to protect us!"
    ms "I'll ask for patrols to scout your neighbourhood regularly."
    ms "Call the emergency telephone number if you notice anything suspicious."
    ms "I'll also ask that you and your friends don't leave the town."
    ms "Don't do anything unusual and everything will be alright."
    off "The patrols?"
    off "He must be joking."
    off "We came here asking for help and all they'll give us is a patrol cruising our street two times a day or something?"
    off "How will that keep us safe from the psycho twins?"
    off "What the fuck is going on?"
    off "This can't be real!"
    off "This is ridiculous!"
    off "What do we have to say to have them do something?"
    scene ep5_sc16_po_11
    mc "Are you kidding me?"
    mc "If they come after us, they will kill us before you even reach our door!"
    ms "You can rest assured that we will come as fast as possible."
    ms "You are safe, Mr Archer."
    ms "Just stay home and call us if you notice anything's wrong."
    scene ep5_sc16_po_12
    ms "Thank you."
    ms "Have a nice day."
    off "He ushers us out of his office and closes the door behind us."
    scene ep5_sc16_poc_01
    mc "What the hell just happened?"
    mc "Did he really throw us out ?"
    sf "I think he did, yes."
    sis "He didn't give a fuck about us."
    sis "We just lost two hours of our lives."
    sf "Don't judge him too hastily."
    sf "He may have thrown us out of his office, that doesn't mean that he won't take care of the problem."
    kf "He said that they will investigate right?"
    kf "That means that they're going to search for them?"
    mc "I don't know. I hope so."
    mc "In the meantime, I guess we can't expect much more than a couple of patrols a day."
    mc "I hope it'll be enough to drive them off."
    scene ep5_sc16_poc_02
    sis "I told you."
    sis "Coming here was useless."
    mc "No, it wasn't."
    mc "They're aware of the problem, they'll do something."
    sis "Yeah, when it'll be too late probably."
    sis "You said it yourself."
    sis "If they come after us, they will have enough time to kill us all before the police even reach our door."
    mc "Oh, come on."
    mc "You know that it was a ridiculous exaggeration."
    mc "They won't break our door so easily, ok ?"
    sis "Yeah... we'll see about that..."
    off "Kelly keeps silent and stays a few steps away from us."
    mc "Are you okay, Kelly ?"
    scene ep5_sc16_poc_03
    kf "Oh, yes... I'm just... I can't help but feel a bit guilty."
    sis "You bet you are."
    sf "[sis_name]. Please."
    kf "No, no, she's right."
    kf "There's no point in denying it..."
    scene ep5_sc16_poc_04
    sf "You certainly did a number on us, but you're not responsible for this."
    kf "They were... my friends... and my father..."
    sf "They were."
    sf "And that does not mean that you are responsible for their actions."
    kf "Maybe..."
    kf "Thank you, [sf_name]."
    kf "I think I should go back home."
    kf "I hope that you will all be fine."
    scene ep5_sc16_poc_05
    sf "Kelly, wait."
    sf "Luke was ready to assault you for refusing to help them."
    sf "What do you think will happen if he knows that you came to warn us and then to the police with us?"
    off "I suddenly understand."
    kf "I don't know..."
    off "If the psycho twins know about that, chances are that they will seek vengeance on Kelly too."
    off "These guys are insane."
    off "I have no doubt that they would kill her."
    scene ep5_sc16_poc_06
    sf "If they're so disturbed and obsessed... I wouldn't be surprised if they were stalking us right now."
    sf "They could even be waiting for us outside of the police station..."
    off "I wouldn't be surprised either. "
    scene ep5_sc16_poc_07
    off "Kelly looks more resigned than afraid."
    off "She's risking her life."
    off "Did she even think about it before coming with us?"
    scene ep5_sc16_poc_08
    off "[sf_name] exchanges a lengthy look with [sis_name] before she turns to me."
    off "She silently asks us to invite Kelly to stay with us."
    off "It's obvious."
    scene ep5_sc16_poc_09
    sis "Oh, come on! You can't be serious!"
    sf "Do you see any other solution?"
    mc "[sf_name] is right... She's home alone."
    mc "We can't let her go like that."
    sis "She'll be fine!"
    sf "I won't take any risk with her life."
    sis "I can't believe we're doing this."
    scene ep5_sc16_poc_10
    kf "Are you talking about me?"
    kf "I don't understand..."
    mc "You can't go back home, Kelly."
    kf "Excuse me?"
    sf "It'll be safer if you stayed with us at least for a few days."
    kf "I'm sure I'll be ok. You don't have to worry..."
    sf "How can we not worry?"
    mc "Again, [sf_name] is right. Luke and Ray probably already know that you came to us."
    mc "We can't let you go like that."
    mc "It wouldn't be right."
    kf "No, no, I don't want to impose myself..."
    mc "We're inviting you to stay with us."
    mc "You can't refuse."
    kf "I don't think that everyone is ok with that..."
    sf "[sis_name]?"
    sis "What?"
    sf "Please."
    sis "Oh, for god's sake!"
    kf "You don't have too. I'll be fine, really..."
    off "[sis_name] sighs loudly before turning to Kelly."
    scene ep5_sc16_poc_11
    sis "No, you won't."
    sis "You'll stay with us."
    kf "Really... you don't have to.."
    sis "What? You're going to refuse now?"
    sis "It's not like you really have a choice."
    off "Kelly stares at her feet in embarrassment."
    kf "Ok then... Thank you."
    sis "Great. It's settled then."
    sis "We'll hop by your place to get what you need on our way back home."



label ep5sc17:
    scene black with dissolve
    with Pause(2)
    show text "Kelly's house"
    with Pause(2)
    scene ep5_sc17_kh_01 with dissolve

    off "The villa Kelly lives in is pretty fancy."
    off "It's one of these architect designed houses made of concrete and glass."
    off "It feels very cold and impersonal."

    sis "I still can't believe we're doing this."
    sf "We don't have a choice, [sis_name]."
    mc "She risked her life to come and warn you and [sf_name]..."
    sis "If all that is true..."
    mc "Oh come on..."
    sis "I'm not saying that everything is false, just that maybe all this is part of some plan..."
    sis "Maybe that's what she wanted from the start..."
    sf "I'm not sure that anyone would be dumb enough to come with us to the police and lie in the face of an officer..."
    mc "Given your common history, I think it's perfectly natural and sane to be a little suspicious."
    mc "But [sf_name] is right."
    sis "Yeah, yeah... I get it..."
    sis "Maybe she's not completely dishonest."

    if dual_love_path == True:
        scene ep5_sc17_kh_02
        sis "But you understand what having her at home, with us, means, right?"
        sis "For the three of us... We'll have to hide our feelings."
        sis "We can't even have the rest of this week for ourselves."
        off "Her attitude changes completely."
        off "She seems depressed and sad."
        mc "Yeah... I know..."
        sf "We all knew that this wouldn't be... simple, didn't we?"
        sf "But I promise you that we'll have time for that later."
        sf "The summer is young."

        if ep4studytrustreward == True:

            scene ep5_sc17_kh_03
            sf "We've already talked about going on a trip together to celebrate your future success at the catch-up session..."
            sf "We just have another reason to sail away for a week or two."
            mc "That would be great."
            sis "Yeah..."
            mc "Where would you want to go?"
            sis "I don't know."
            sis "It's your idea, remember?"
            sis "You talked about going to a place where I would have to speak Spanish."
            mc "Yeah, sure, but do we want some beach?"
            mc "Someplace tropical maybe?"
            sf "Tropical?"
            scene ep5_sc17_kh_04
            mc "How about Brazil?"
            sis "They don't speak Spanish in Brazil."
            mc "Really?"
            mc "It sure sounds like Spanish to me..."
            sis "It's Portuguese, [mc_name]..."
            scene ep5_sc17_kh_05
            mc "Ok, I get it, you don't like Brazil."
            mc "We'll find someplace else."
            off "[sis_name] lets out a consternated sigh and [sf_name] lightly laughs."
            sis "I don't care where we go... as long as we go together."
            sis "It'll be fine."
            scene ep5_sc17_kh_06
            sf "It'll be great."
            sf "You know what we need?"
            sf "Some new swimsuits."
            sf "And hats."
            sf "Hats would be terrific."
            sf "I've seen some very larges ones, as big as an umbrella..."
            off "I let the girls ramble about this year's hat fashion."
            off "The idea of a trip with both of them is very seductive."
            off "I imagine a bungalow by the sea, the three of us lazing on a bed, naked."
            off "Our bodies, crushed by the humidity of the tropics, rubbing against each other."
            off "We would drink cocktails and make love all day long."
            off "Oh my God."
            off "I'm getting hard on my fantasies again."
            off "Calm down, [mc_name]."
            off "Don't get carried away."
            off "Keep your imagination in check."

    scene ep5_sc17_kh_07
    off "[sis_name] yawns as she stretches."
    sis "What the hell is she doing now ?"
    sf "She's barely been gone for 10 minutes."
    sf "Give her some time."
    sis "Yeah, and in the meantime, we're here burning under the scorching sun."
    sis "She could at least have let us in."
    sf "We're in the shade..."
    scene ep5_sc17_kh_08
    off "Holy shit... I never imagined that stretching could be so... interesting..."
    off "Focus, [mc_name]. Focus!"
    sf "And she probably didn't think it would take her so much time."
    sis "Come on, you don't need half an hour to pack a couple of panties and t-shirts."
    sf "I'm sure she has a hard time deciding what to take."
    sf "You know... If she wants to... get his attention..."
    sis "Oooh. Of course."
    sis "She won't miss that opportunity."
    mc "His attention?"
    scene ep5_sc17_kh_09
    sis "Like you haven't noticed anything."
    mc "What are you talking about?"
    sf "It's obvious."
    sf "The way she looks at you...."
    mc "How does she look at me?"
    sf "She's begging for your attention."
    sis "Oh, I have a feeling that she's begging for way more than his attention."
    mc "You're exaggerating."


    if ep5kfnew == False:
        off "Kelly has been pretty clear about having a crush on me but I didn't really think seriously about it."

    if ep5kfgirlsunknown == False:
        sis "I didn't want to believe it but... she genuinely seems to be interested in you."
        mc "What's so hard to believe? I mean ..."
        sis "Yeah sure... Don't waste your saliva, playboy."
    if sf_love_path == True or ( sf_dom_path == True and (sis_sub_path == True or sis_love_path == True )):

        sf "You seem to have a lot of success with the girls, lately."
    if sf_love_path == True:

        mc "And I'm as surprised as satisfied..."
    elif ( sf_dom_path == True and (sis_sub_path == True or sis_love_path == True )):

        mc "If you say so..."

    if sis_love_path == True or sf_love_path == True:

        sis "I swear, [mc_name] if you touch her, I will kill you."
        off "Is that her idea of trust?"
        mc "What? Why would I touch her?"
    else:


        sf "You seem to be interested too."
        mc "Interested? Me? Why would I be ?"

    if full_neutral_path == True:

        off "I'm pathetic. Who am I trying to fool?"

    scene ep5_sc17_kh_10
    sf "Well, you can't deny that she's very pretty."
    sis "And her body... Have you seen her ass ?"
    sf "Oh yes, I have."
    sf "It's very hard not to look at it..."
    mc "You're telling me that you checked her out?"
    sf "Because you haven't ?"
    off "Obviously, this is a trap."
    off "They're toying with me."
    mc "I'm trying to be a gentleman."
    sf "And I appreciate that."
    sf "But you've clearly been missing out on."
    mc "Ok, that conversation has gone way over the boundaries of weirdness."

    if sf_love_path == True:
        mc "She's very pretty, and her ass may, or may not be fantastic, but you have nothing to worry about."
        scene ep5_sc17_kh_11
        sf "I'm not worried at all."

        if dual_love_path == True:
            sf "Are you [sis_name] ?"
            scene ep5_sc17_kh_12
            sis "Not in the slightest."

        mc "Everything is fine then..."
        sf "Everything is fine."
        off "[sf_name] smiles while [sis_name] looks at me with death threats in her eyes."
        scene ep5_sc17_kh_13
        off "Just as I'm thinking that they will really kill me if I ever misstep, they burst out laughing."
        sis "You should see your face!"
        off "What the hell?"
        sf "You know, you're cute when you're afraid."
        mc "I wasn't afraid!"
        off "I almost pissed my pants. Yeah."
        mc "I knew you were kidding, right from the start."
        off "They keep on laughing as I try not to show my shame."




    if dual_love_path == False and sf_love_path == False:
        mc "She's very pretty, and her ass may, or may not be fantastic, but I'm not interested."
        mc "Not every man thinks with their genitals."
        scene ep5_sc17_kh_13
        off "[sis_name] and [sf_name] look at each other and burst out laughing."
        mc "What?"
        mc "What did I say ?"
        off "They're laughing so hard that they're apparently unable to answer me."
        off "I feel mocked."
        off "I'm ashamed and a bit angry."

    scene ep5_sc17_kh_14
    mc "Ok, yeah... That's really funny..."
    mc "Instead of laughing like maniacs, why don't one of you two go and see what's going on?"
    mc "Maybe she needs help?"
    sf "Not a chance."
    sf "You see, I've been properly educated, and there's no way I set foot in a house where I haven't been invited."
    mc "Ok... [sis_name] ?"
    sis "You heard the lady, [mc_name]."
    sis "It wouldn't be proper."
    off "I'm about to explain that we could just knock on the door to get Kelly's attention when I suddenly think of something else."
    mc "Girls... What if they were already here waiting for her?"
    mc "What if they were inside ?"
    scene ep5_sc17_kh_15
    off "The discussion isn't that fun anymore."
    sf "You think they could be?"
    mc "I don't know... They're crazy."
    mc "I'm just thinking that maybe we shouldn't have let her go alone..."
    sf "How much time has she been gone ?"
    sis "I don't know... fifteen minutes maybe?"
    mc "It's a bit long, right ?"

    menu:
        "Can you give her a call ?":
            $ ep5kfcalled = True
            mc "Just ask her if everything is alright?"
            sf "I guess I can."
            scene ep5_sc17_kh_16
            off "[sf_name] takes out her phone and quickly makes the call."
            sf "I think she's already on the phone."
            sis "Who is she talking to?"
            sf "How would I know?"
            sis "Perhaps she's calling her mother?"
            mc "She would have a few things to say..."
            sf "At least to let her know what she won't be home for a few days."
            mc "You're probably right."
            scene ep5_sc17_kh_17
            sis "Yeah, whatever. If she could hurry a bit..."
        "[gr]I'm going in.":

            $ ep5gonein = True
            scene ep5_sc17_kh_18
            sis "What? Wait!"
            mc "You go back in the car and close the doors."
            sis "Are you crazy?"
            sis "What if they're inside?"
            mc "If I'm not back in five minutes, you get away from here and you call the police."
            sis "Are you fucking insane?"
            sis "You're not going to risk your life for her, are you?"


            menu:
                "She's risking hers for the both of you. [sfLovePath]":
                    $ ep5risklife = True
                    mc "That's the least I can do."
                    sis "What are you even talking about?!"
                    sf "[mc_name]..."
                    mc "It'll be ok."
                    mc "I'm sure we're just worrying about nothing."
                    mc "I'll just go and let her know we're still waiting."
                    mc "Now get back in the car."
                    $ ProcessStat(2, "sis_affection")
                    $ ProcessStat(2, "sf_affection")
                    $ ProcessStat(2, "sf_dominance")
                    $ DumpNotStack()
                "Do you have a better idea? [sisSubPath]":

                    $ ep5betteridea = True
                    mc "I don't think so."
                    mc "I know what I'm doing."
                    mc "Trust me."
                    mc "Go back in the car."
                    mc "Now!"
                    off "I almost yell that last word."
                    off "They briefly look at each other before silently obeying."
                    $ ProcessStat(2, "sis_submission")
                    $ ProcessStat(2, "sf_dominance")
                    $ DumpNotStack()

            scene ep5_sc17_kh_19
            off "What the fuck am I doing?"
            off "What will I do if the psycho twins are in this place?"
            off "I'd better be discreet."
            off "If I can be stealthy, maybe I can take one down before the other one react..."
            off "Listen to yourself, [mc_name]."
            off "You're ridiculous."
            off "What are you? A superhero? Moron."
            off "Besides, you're just getting a bit paranoid."
            off "Kelly is probably fine and chances are you're just going to rudely intrude her house and scare her for nothing."
            off "Yeah well... I'll hope I'll just have to apologize for my rudeness."
            off "I open the door without knocking."
            scene ep5_sc17_kh_20
            off "I've barely set foot inside, when I can hear Kelly's muffled voice coming from further away in the house."
            off "She's talking to someone."
            off "I take a few steps in."
            scene ep5_sc17_kh_21
            off "I know that minimalism is a thing but this is very empty."
            off "I feel like there's something missing in this room."
            off "There isn't a single piece of furniture in here."
            off "This is very weird."
            off "Kelly's voice becomes clearer."
            off "I can't hear the person on the other end of the conversation."
            off "She's probably on the phone."
            kf "I know... I'm sorry for the delay..."
            kf "I'll have the money shortly..."
            kf "Yes... No, it won't be a problem..."
            kf "I assure you, I'll pay next month..."
            kf "I'll do whatever it takes."
            kf "Just a few more weeks, please..."
            kf "Thank you."
            kf "Thank you for your patience."
            kf "Yes. Have a nice day."
            off "What was that about?"
            off "Money problems?"
            off "And what's that noise now?"
            scene ep5_sc17_kh_22
            off "Is she crying?"
            off "She's coming this way."
            off "Crap. What do I do? What do I say?"
            off "She notices me and immediately turns away to hide her face."
            off "She wipes away her tears."
            off "I slowly take a few steps towards her."
            mc "Hey, Kelly... I'm sorry to intrude but..."

            scene ep5_sc17_kh_23

            menu:
                "We were a bit worried. [kellyPath]" if ep5risklife == True:
                    $ ep5kfworried = True
                    scene ep5_sc17_kh_25
                    off "She swallows her last sobs and looks at me as if nothing happened."
                    off "She's quite talented to hide the pain."
                    kf "Worried?"
                    $ ProcessStat(5, "kf_affection")
                    $ DumpNotStack()
                    mc "Yeah... It's probably ridiculous but..."
                    mc "Well, we came to think that maybe Luke and Ray could have been waiting for you inside..."
                    kf "And you came in to rescue me?"
                    mc "I guess so... I mean... I'm sorry, I know it was stupid..."
                    kf "Thank you, [mc_name]... It's... very sweet of you."
                    off "She's damn cute."
                    off "But her smile is so sad."
                    mc "If you say so..."
                    mc "Anyone would have done the same..."
                    kf "I don't think so."
                "I thought that maybe you would need some help...":


                    scene ep5_sc17_kh_25
                    off "She swallows her last sobs and looks at me as if nothing happened."
                    off "She's quite talented to hide the pain."
                    kf "Thank you, [mc_name]."
                    kf "I'm just taking this small bag."
                    kf "It should be enough."
                    scene ep5_sc17_kh_24
                    off "Her definition of small... is surprising..."
                    mc "You're packing pretty lightly."
                    kf "It's just for a few days, right?"
                    mc "Let's hope so."

            scene ep5_sc17_kh_26

            menu:
                "I'm sorry, I can't act as if I've seen nothing... [kellyPath]" if ep5kfworried == True:
                    mc "You were crying."
                    mc "Is everything alright, Kelly?"
                    $ ProcessStat(2, "kf_affection")
                    $ DumpNotStack()
                    scene ep5_sc17_kh_27
                    kf "Oh, don't worry."
                    kf "It's just... It's unrelated to our current situation."
                    menu:
                        "Unrelated? [kellyPath]":
                            $ ep5kffriend = True
                            mc "Does that mean that I shouldn't care?"
                            off "She looks at me for a few seconds before she shyly asks."
                            kf "Why would you care?"
                            mc "I don't know... I don't like when my friends cry."
                            off "Her eyes open wide in surprise."
                            scene ep5_sc17_kh_28
                            kf "Your friends?"
                            off "Ok, maybe I'm going a bit fast here."
                            off "My words have gone far beyond my thoughts but I can't tell her that, right?"
                            off "Fuck. I have a feeling that [sis_name] would kill me if she ever learns about this."
                            mc "Yeah... You came to see us, to warn and help us..."
                            mc "And doing so you've put yourself in a difficult position..."
                            mc "Maybe I'm going a bit fast but... In my book, that puts you among the good guys."
                            $ ProcessStat(5, "kf_affection")
                            $ DumpNotStack()
                            off "Her expression adds incredulity to surprise."
                            kf "I'm not sure that [sis_name] and [sf_name] would agree with you."
                            mc "You may be surprised."
                            mc "They can forgive."
                            mc "Even [sis_name]."
                            mc "It'll just take some time."
                            off "That bitter smile says it all."
                            off "A bit of hope lightens her sad loneliness."
                            off "To think that I've could do that with these few words... that makes me feels good."
                            scene ep5_sc17_kh_29
                            kf "Thank you, [mc_name]. You're a nice guy."
                            off "Her voice trembles and for a second I wonder if she's going to crumble in tears or something, but nothing happens."
                        "Ok...":

                            mc "I'm sorry, I never meant to intrude in your personal matters."
                            scene ep5_sc17_kh_30
                            kf "It's ok."
                            kf "I'll manage."
                            kf "Thank you for your concern."
                            mc "I guess you're welcome."

                            if sf_dom_path == False:
                                off "She's just like [sf_name] and [sis_name]."
                                off "Tough outside, frail inside."
                            else:
                                off "Obviously, she isn't as tough as she wants me to believe."

                            off "I don't know what I expected."
                            off "I'm basically a stranger, she wasn't going to trust me with her problems just like that."
                "So...":

                    scene ep5_sc17_kh_31
                    mc "Are we ready?"
                    kf "Yes. I think I've taken everything I need."
                    kf "I just need a couple more minutes to check on the house and I'm good to go."

            mc "Ok then... I'll wait for you outside. Take your time."

            scene ep5_sc17_kh_32
            off "Back outside, the girls get out of the car as soon as they see me."
            sis "What is she doing ?"
            mc "She's fine."
            mc "She's checking the house and she'll be ready."
            mc "Just give her a minute."
            off "I hesitate to tell the girls what happened."
            off "After all, Kelly's life and problems are none of our business."
            off "If I want their trust, however... I should tell them."
            scene ep5_sc17_kh_33
            mc "She was on the phone when I went in..."
            mc "I think she has some money problems."
            scene ep5_sc17_kh_34
            sf "Her father probably didn't leave them much when he abandoned them."
            mc "And her mother has been sick for a long time now."
            mc "Several months at least..."
            sf "I wonder what disease she suffers from."
            sis "Well... month-long... With heavy hospitalization..."
            sis "Maybe it's cancer. I mean, that's an obvious possibility."
            sf "For you maybe, your father is an oncologist."
            mc "You think that Kelly's mom could be one of Dad's patients?"
            scene ep5_sc17_kh_35
            sis "I don't know..."
            sis "I'm not sure I want to talk about that with her..."
            off "A heavy silence sets in."
            off "We just seem to understand that Kelly is losing her mother."
            off "It tastes like shame, pain and sadness."
            off "Even [sis_name] can't help but empathize."


    scene black with dissolve
    with Pause(2)
    show text "A few minutes later."
    with Pause(2)
    scene ep5_sc17_kh_36 with dissolve
    kf "I'm sorry, I made you wait."
    sf "It's ok, Kelly."
    kf "I received a call I had to answer and..."
    kf "It took more time than I expected."
    sis "It's fine."
    sis "You weren't that long."

    if ep5gonein == True:
        sis "I hope you've packed enough panties because I'm not lending you any of mine."
        kf "I... Should have enough... Thank you."
        off "[sf_name] bursts out laughing as I engage the car on the road home."
        off "Kelly seems as embarrassed as ever."
    else:
        sis "Yeah, we've berely been waiting for an hour."
        sis "No big deal."
        mc "[sis_name]..."
        sf "Don't pay attention to her, Kelly, she's just a bit grumpy today."
        mc "She's grumpy every day."
        sis "Probably because of you."
        mc "Obviously, making you grumpy is my prerogative."
        off "[sf_name] laughs as I engage the car on the road home."
        off "Kelly shyly joins in."


label ep5sc18:
    scene black with dissolve
    with Pause(2)
    show text "The evening"
    with Pause(2)


    if evil_asshole_path == True:
        scene ep5_sc18_k_01 with dissolve
        off "I've been brainstorming for hours."
        off "I have no idea what to do."
        off "How can I gain their trust in so little time?"
        off "We didn't even eat together this evening."
        off "They ordered a pizza and left half of it for me on the kitchen table."
        off "I don't know how to feel about that."
        off "The girls are in the living room, watching some tv show."
        off "I can hear them laughing from here."
        scene ep5_sc18_k_02
        off "Come on, [mc_name]."
        off "Think harder."
        off "What can I do?"
        off "If I want to dose them tomorrow, I need them to trust me enough to drink whatever I offer them, right?"
        off "[sis_name] didn't look angry with me."
        off "The real problem is [sf_name]."
        off "She clearly wants me dead right now and I don't see how I can improve my relationship with her."
        off "I can't just go in there and apologize, can I?"
        scene ep5_sc18_k_03
        off "What would I even say?"
        off "That I'm sorry?"
        off "Sorry for what?"
        off "I just tried to be friendly to [sis_name]'s boyfriend."
        off "Fuck. I don't see any way out of this."
        off "I can't tell her that I suddenly decided to be nice and friendly with these two morons."
        off "A few hours earlier I was calling them rapists, psychos and such."
        off "I can't play innocent."
        scene ep5_sc18_lr_01
        off "[sf_name] will see right through my lies and that will only anger her further."
        off "I can't just act as if nothing happened and hope she will cooldown by tomorrow."
        off "I have to find something."
        off "Look at them."
        off "They seem to enjoy themselves, having a drink and relaxing on the sofa..."
        off "If I could just..."
        off "Wait... That drink..."
        scene ep5_sc18_lr_02
        off "I don't actually need to serve it."
        off "I just need to put the pill in it."
        off "They can serve it themselves..."
        off "Ok... But how can I do that?"
        off "Maybe I can make a diversion?"
        off "If I wait for them to enjoy their evening, just like today..."
        off "Once they have settled in the living room with their drink, I..."
        off "Do something that will make them leave the room for a minute, just enough time for me to put the pill into their glasses."
        off "Sounds great... but I have absolutely no idea what kind of diversion I could use..."
        off "Maybe I can do something else."
        scene ep5_sc18_mcr_01
        off "What if I dose their bottle before they drink from it?"
        off "I mean, there's only a couple of beers and that half bottle of wine left..."
        off "If they don't finish it tonight, of course..."
        off "If I get rid of the beers, they'll have only the wine to drink."
        off "I can easily put a pill in it before they pour it..."
        off "That sounds way easier than the diversion thing..."
        off "That could work."
        off "Yeah... that will work... these bitches won't see it coming."
        off "Fuck yeah!"
        off "And I won't even have to apologize or anything."
        off "I'm a fucking genius."
        off "I'll wait for them to go to sleep and I'll go check on the bottles."
        scene ep5_sc18_mcr_02
        off "The ring tone of my phone startles me."
        off "Who the fuck calls me at this hour?"
        off "That's Steve's number."
        scene ep5_sc18_mcr_03
        mc "Hey, Steve."
        uk "Hello, [mc_name]."
        off "This isn't Steve."
        off "Unless he has suddenly turned into a girl."
        uk "How are you tonight?"
        off "Is this Steve's girlfriend?"
        mc "I'm doing fine."
        uk "Great. Do you remember me?"
        off "She whispers."
        off "There's some noise on the background."
        mc "Yeah, of course.... You're..."
        ja "Jane."
        mc "How are you doing, Jane? Having some fun?"
        ja "Oh yes. Tons of fun. Haaan!"
        off "Was that a moan?"
        ja "I wanted to talk to you and your girls...."
        mc "My girls?"
        ja "[sis_name]? And [sf_name]?"
        scene ep5_sc18_mcr_04
        mc "I'm afraid I'm alone right now...."
        off "What does she want to tell them?"
        off "That girl is crazy."
        ja "Oh, that's too bad... I'm sure they would have enjoyed this..."
        ja "As much as you will."
        off "I can't really imagine them enjoying anything with me right now..."
        mc "Yeah... As you say..."
        ja "It'll be you alone then."
        ja "Are you ready?"
        off "Her words are intertwined with soft moans."
        off "Are they... fucking ?"
        scene ep5_sc18_mcr_05
        mc "Ready... for... ?"
        ja "Steve's just taken his fingers out of my pussy."
        off "Holy shit."
        ja "I can feel his dick pushing on my... Haaan!"
        off "HOLY FUCKING SHIT."
        mf "Not so loud honey! He's going to hear us."
        off "Steve's voice, in the background."
        off "They're hiding from someone and fucking at the same time?"
        off "I understand that the girl's into risky action... This is probably something like that."
        ja "Slowly! Yes!"
        off "Damn, Steve, you bastard."
        scene ep5_sc18_mcr_06
        off "You're having the time of your life right now."
        ja "I can feel him penetrating me."
        ja "Centimetre by centimetre, slowly."
        off "I don't know what game she wants to play with me but I like it already."
        ja "It's so good! I like it."
        ja "Half of it is inside!"
        ja "There's so much!"
        off "That's so fucking hot."
        off "My mouth has gone completely dry."
        ja "He's taking it out a bit."
        ja "He's teasing me."
        ja "Haaaan!"
        scene ep5_sc18_mcr_07
        off "I got rid of my shorts and grabbed my dick without even thinking about it."
        off "That's sick."
        off "I'm going to fap to Steve's girlfriend explaining how she's having sex with him."
        ja "He's back inside!"
        ja "Deeper! Do it!"
        ja "Fuck me, baby!"
        ja "Fuck my pussy!"
        off "Her moans intensify."
        mf "You're too loud!"
        scene ep5_sc18_mcr_08
        ja "I know! It's so good!"
        ja "We're doing it.... Right under my dad's window..."
        off "They're completely crazy."
        off "Steve, you're going to die tonight."
        ja "Faster! Faster!"
        off "Her voice and moans suddenly sound muffled."
        off "I can hear some noise in the background..."
        off "Is that... The pounding?"
        ja "I'm so wet! I've wanted to do this for so long!"
        ja "Harder! Harder!"
        ja "Haaaaaaaaaan yes... that's it...."
        off "I'm working my shaft ruthlessly."
        ja "He's taking me doggystyle."
        ja "He's going so deep! Haan !"
        off "The moans get out of hand."
        off "Maybe now discretion isn't her priority."
        ja "I can feel him stretching my insides."
        ja "Haaan!"
        ja "Every time he hits me down inside, it sends shivers down my spine."
        scene ep5_sc18_mcr_09
        off "This is crazy."
        off "Steve is actually fucking this girl like a beast."
        off "STEVE."
        off "How is that even possible?"
        ja "My legs are shaking."
        ja "Oh, my Gooooood!"
        mf "Quiet down! You're going to wake him up!"
        ja "He's plowing me so hard... He could break my ass at any moment."
        ja "I love it!"
        off "She doesn't even try to keep it down."
        off "She basically screams on the phone."
        ja "Haaaaaaann, yeeeeeeeeeeeees"
        scene ep5_sc18_mcr_10
        uk "WHAT THE FUCK ARE YOU DOING UNDER MY WINDOW ?"
        mf "Fuck!"
        off "Holy shit."
        off "That loud and unknown voice, Steve's reaction..."
        off "They've been caught in the act."
        off "I can hear them running."
        off "Someone is yelling things I don't understand in the background."
        mf "Left! Turn left !"
        off "More running."
        off "More screaming."
        mf "Here! Under the stairs! hide !"
        off "I hear them try to catch their breath for a couple of minutes."
        off "Jane starts laughing."
        mf "Holy fuck! He almost caught us!"
        ja "Yes, he did!"
        scene ep5_sc18_mcr_11
        off "She sounds happy."
        off "This girl is insane."
        mf "Holy fucking shit! He saw us... you think he recognized you ?"
        ja "Not a chance."
        ja "He was probably half drunk."
        off "Did they forget about me?"
        ja "Oh my god. You're still hard..."
        off "How is that even possible?"
        off "When did Steve become a freaking sex machine?"
        ja "Let me help you with that."
        mf "Oooh, that's very nice of you...."
        off "I can't believe it."
        mf "[mc_name], you still there?"
        scene ep5_sc18_mcr_12
        mc "Yeah..."
        mf "I hope you enjoyed the show..."
        mc "I did... you guys are crazy.... Is she ... sucking your dick right now ?"
        mf "Yes, she is... I'm almost there baby... "
        mc "This is fucking nuts. Are you really the Steve I know ?"
        mf "Who eeeellllsse? Ohh, shiiiit."
        off "His groan sounds barely human."
        off "I imagine him letting go a gallon of semen like in these crazy hentai mangas he keeps reading."
        ja "[mc_name]?"
        mc "Yes."
        ja "Did you jerk off to us ?"
        scene ep5_sc18_mcr_13
        mc "I have to confess that I did..."
        off "I couldn't finish though... That conclusion was a bit abrupt."
        ja "It's a shame you're not here with us..."
        ja "I could have taken care of you myself."
        off "What the fuck?"
        off "Did I understand that correctly?"
        scene ep5_sc18_mcr_14
        mc "What ?"
        off "I can hear Steve laughing in the background."
        mf "You're going to make him crazy, baby."
        ja "But that would be fun, right?"
        ja "You could take me both at the same time..."
        off "Is she being serious?"
        scene ep5_sc18_mcr_15
        mc "I guess so..."
        off "And Steve is okay with that?"
        ja "What do you say, [mc_name], would you like that ?"
        off "Holy fuck, of course..."
        off "Wait this is a joke right?"
        off "Steve wouldn't make a fool out of me... But her, maybe..."
        mc "I don't know... It's tempting but..."
        ja "I understand, you would prefer to fuck [sis_name], right ?"
        off "How the hell?"
        scene ep5_sc18_mcr_16
        mc "What? No! She's..."
        ja "Maybe [sf_name] then?"
        ja "I wish you good luck, [mc_name]."
        ja "Be nice and you'll get them eventually."
        ja "I'm rooting for you."
        off "Her voice gets distant."
        off "She keeps talking as she puts the phone away."
        ja "Now... I hope you don't think we're done for tonight..."
        off "I can hear Steve laughing right before the communication cuts."
        scene ep5_sc18_mcr_17
        off "What the fuck just happened?"
        off "I have so many questions."
        off "This is so frustrating."
        off "My dick has gone soft, I've lost the motivation to finish myself."
        off "I'm so confused."
        off "I just listened to Steve literally fucking his girlfriend in front of her father..."
        off "And what the fuck was that at the end?"
        off "She could have taken care of me herself?"
        off "Taking her both at the same time?"
        off "Was that a joke or a proposition?"
        off "And what the fuck did Steve tell her about [sis_name] and me?"
        scene ep5_sc18_mcr_18
        off "Fuck my life."
        off "Steve is having all the fun while I'm stuck here."
        off "I'm jealous."
        off "Even if I mess with [sis_name] and [sf_name] tomorrow night, it's not the same as fucking that crazy girl by the beach..."
        off "I should have gone with him..."

        jump ep5NightDispatch

    elif moronic_hero_path == True:
        scene ep5_sc18_lr_03 with dissolve
        sf "So... They want to rape me... Not [sis_name] ?"
        mc "I think that you were the real target at the club, last Saturday..."
        mc "[sis_name] was a collateral victim."
        mc "After that, they tried to use her to reach you..."
        sf "But why? Why me? What have I done to them?"
        mc "It's an act of vengeance."
        mc "They want to hurt your father through hurting you."
        sf "My father? I doubt that Dad has anything to do with them."
        mc "Does he work for Knave Structured?"
        scene ep5_sc18_lr_04
        sf "He does, for the moment, yes..."
        mc "Their story was a bit confused but..."
        mc "They claim that your dad fired their own father three years ago or something like that."
        mc "They also say that he robbed him of some money..."
        sf "That's ridiculous. Dad doesn't fire people. And he doesn't rob money."
        mc "I'm just telling you what they said."
        mc "I don't think that's the truth but that's probably what they believe."
        sf "And that's all?"
        sf "That's enough for them to assault us?"
        mc "No... There's more... It goes a tad deeper than that."
        mc "The firing thing led to money problems, and their mother got sick..."
        mc "And died..."
        mc "They seemed to think that they could have saved her if they had more money..."
        mc "And then..."
        mc "Their father committed suicide..."
        mc "They're blaming your dad for all of that."
        mc "I know it doesn't make any sense."
        mc "They are insane."
        mc "That made me think of that tv show about profilers when they explain that a dramatic event can lead to some kind of psychotic break."
        mc "I think it's something like that."
        scene ep5_sc18_lr_05
        sis "What? You're a psychiatrist now?"
        mc "You're right, I have no idea what I'm talking about."
        mc "I'm just making suppositions based on their story and some tv shows pseudo-knowledge..."
        mc "But there's something I'm sure: they are crazy, no doubt about that, and trying to understand them is useless."
        mc "It's just like their plan."
        mc "I mean, it's ridiculous."
        mc "They want to rape you, record it then put it on the internet."
        mc "By doing so they expect to traumatize you and your father for life."
        mc "They are insane."
        sis "You have to call your father, [sf_name]. He should know."
        sf "I'll call him in a moment..."
        sf "So they gave you pills, to put us to sleep?"
        mc "Yeah... I was supposed to make you drink some alcohol mixed with that drug."
        mc "That would have put you to sleep."
        mc "Just like it did with you on Saturday night, [sis_name]."
        mc "After that, I would have given them a call and let them in..."
        scene ep5_sc18_lr_06
        sis "That's sick. I feel like throwing up."
        off "A heavy silence settles in."
        off "[sf_name] seems more worried than afraid."
        off "That girl has nerves of steel."
        scene ep5_sc18_lr_07
        sf "I'll be back shortly."
        off "[sf_name] exits the room."
        off "She's probably going to have that phone call to her father."
        scene ep5_sc18_lr_08
        off "[sis_name] and I awkwardly look at each other for a moment."
        sis "So... You traded [sf_name] for me?"
        mc "What ?"
        sis "You were supposed to rape me too, right ?"
        off "Great. The subject I wanted to avoid..."
        mc "No... I mean, that's what I told them..."
        mc "I needed to give them a reason to trust me ..."
        sis "I wonder how that idea manage to come to your mind..."
        mc "It was ... obvious..."
        scene ep5_sc18_lr_09
        sis "Oh really?"
        mc "At the time I was sure they were after you..."
        mc "So I told them that I wanted to... fuck you too..."
        sis "And that worked. You must have been very convincing."
        mc "I guess I was... They must have thought that I was as sick as them..."
        sis "Yeah... Sure... because you're definitely not a real perv."
        mc "If you say so..."
        scene ep5_sc18_lr_10
        sis "[sf_name] told me you have the hots for me."
        mc "What?!"
        sis "You told her so this morning."
        mc "No, I didn't! And I don't!"
        mc "I told her that you're cute. Nothing more."
        sis "And that you fantasize about me."
        mc "I said that I've thought about it a couple times, that's all ok ?"


        if ep2pantietaken == True:
            sis "That sure explains a lot of things..."
            mc "No it doesn't."

        sis "Yeah... Whatever..."
        scene ep5_sc18_lr_11
        off "She changes position and looks away."
        off "She continues with a much softer tone."
        sis "Thank you..."
        sis "That was stupid but very brave..."
        off "That's... unexpected."
        mc "You don't have to thank me..."
        off "But I enjoy it very much..."
        sis "If you do something as stupid as that again, I'll kill you myself."
        mc "Ok..."
        scene ep5_sc18_lr_12
        off "She lights up the tv and searches for something to watch."
        off "The discussion seems to be over."
        off "[sf_name] comes back a few minutes later and sits by [sis_name] without saying a word."
        scene ep5_sc18_lr_13
        off "We watch the end of a superhero movie."
        off "Nothing really exciting."
        off "I think about going back to my room to play some games when my phone suddenly rings."
        scene ep5_sc18_lr_14
        off "That's Steve's number."
        off "I take the call as I rise from my chair."
        mc "Hey, Steve."
        uk "Hello, [mc_name]..."
        off "This isn't Steve. It's a girls voice."
        off "The surprise stops me in my track."
        scene ep5_sc18_lr_15
        uk "How are you tonight?"
        off "Who is this?"
        off "Is this Steve's girlfriend?"
        mc "I'm doing fine."
        uk "Great. Do you remember me?"
        off "She whispers."
        off "With the tv on, I have trouble hearing her clearly."
        off "I can feel the suspicious gazes of [sf_name] and [sis_name] weighing on my shoulders."
        mc "Yeah, of course.... You're..."
        ja "Jane."
        mc "How are you doing, Jane? Having some fun?"
        ja "Oh yes. Tons of fun."
        ja "I wanted to talk to you and your girls...."
        mc "You want to talk with my girls?"
        off "The tv immediately goes off."
        off "I have a feeling that this is going to cost me dearly."
        scene ep5_sc18_lr_16
        sis "Your girls?"
        sf "You should come back here, [mc_name]."
        off "Crap."
        off "I should have left the room before talking."
        off "They won't let me leave now."
        ja "[sis_name]? And [sf_name]?"
        mc "Yeah... what is this about?"
        ja "You will like it, [mc_name]."
        ja "And they will too, I promise."
        off "I can't help but being sceptical."
        off "Somehow I'm pretty sure that things are about to go weird as fuck."
        off "But I guess I can't help it."
        mc "Ok... let me just..."
        off "Oh, fuck this."
        off "Steve is right."
        off "Stop worrying, [mc_name]."
        off "Just YOLO, for once."
        off "What kind of shit can happen?"
        off "Steve's nonsense can't be worse than the shit you pulled yourself these last few days."
        off "Let's hear it."
        scene ep5_sc18_lr_17
        mc "I put you on speaker, Jane."
        mc "Everyone can hear us know."
        mc "So... [sis_name], [sf_name], this is Jane..."
        mc "She's Steve's girlfriend..."
        off "They give me one last suspicious look before quickly gathering around my phone."
        off "They ogle it with unrivalled curiosity."
        scene ep5_sc18_lr_18
        sf "Hi, Jane..."
        sis "Hi..."
        ja "Hello, girls."
        ja "Are you ready? Haaan!"
        scene ep5_sc18_lr_19
        off "That was a moan. No doubt about that."
        mc "Ready... for... ?"
        ja "Steve's just taken his fingers out of my pussy."
        off "Holy shit."
        ja "I can feel his dick pushing on my... Haaan!"
        off "HOLY FUCKING SHIT."
        scene ep5_sc18_lr_20
        off "[sis_name] and [sf_name] look at each other with surprise."
        mf "Not so loud honey!"
        mf "He's going to hear us."
        off "Steve's voice, in the background."
        off "They're hiding from someone and fucking at the same time?"
        off "I understand that the girl's into risky action... This is probably something like that."
        ja "Slowly! Yes!"
        off "Damn, Steve, you bastard."
        off "You're having the time of your life right now."
        ja "I can feel him penetrating me."
        ja "Centimetre by centimetre, slowly."
        sis "Oh my God."
        ja "As you say. Ooooh my God!"
        off "I don't know if I should laugh or cry."
        off "I'm here, with [sis_name] and [sf_name], listening to Steve fucking a crazy girl."
        off "The girls seem... actually curious about what's happening."
        off "Everything is normal."
        ja "It's so good! I like it."
        ja "Half of it is inside! There's so much!"
        off "[sf_name] bends toward the phone and shyly asks."
        sf "Isn't that... painful?"
        ja "Painful? Oh god no! Haaan!"
        ja "This is delicious!"
        off "This is so weird."
        off "I have a hard-on."
        off "And in the meantime, I'm embarrassed as fuck."
        ja "He's taking it out a bit."
        ja "He likes to tease me with his cock."
        ja "He knows I want it all inside me and he takes his time filling me up to the brim."
        ja "HAAAAN!"
        scene ep5_sc18_lr_21
        off "The girls seem genuinely interested in what's happening."
        off "This audio show is obviously more interesting to them than the boring movie we just watched."
        ja "He's back inside! Deeper! Do it!"
        ja "Fuck me, baby! Fuck my pussy!"
        off "Her moans intensify."
        mf "You're too loud!"
        ja "I know! It's so good!"
        ja "We're doing it... Right under my dad's window..."
        sis "Her dad?"
        off "They're completely crazy."
        off "Steve, you're going to die tonight."
        sf "Are you doing that... Next to your dad?"
        ja "Yes! It's so... exciting!"
        ja "Haaaan! Faster! Faster !"
        off "Her voice and moans suddenly sound muffled."
        off "I can hear some noise in the background..."
        off "Is that... The pounding?"
        ja "I'm so wet! I've wanted to do this for so long!"
        ja "Harder! Harder! Haaaaaaaaaan yes... That's it...!"
        scene ep5_sc18_lr_22
        sf "What if he catches you?"
        ja "Haaaan... I hope he will !"
        off "She's insane."
        off "They both are."
        ja "He's taking me doggystyle."
        ja "He's going so deep! Haan !"
        off "The moans get out of hand."
        off "Discretion isn't her priority anymore."
        ja "I can feel him stretching my insides."
        ja "Haaan! Every time he hits me down inside, it sends shivers down my spine."
        off "Come on, how long is this going to last?"
        off "This is crazy."
        off "Steve is actually fucking this girl like a beast."
        off "STEVE."
        off "How is that even possible?"
        scene ep5_sc18_lr_23
        ja "My legs are shaking."
        ja "Oh, my Gooooood!"
        mf "Quiet down! You're going to wake him up!"
        ja "He's plowing me so hard... He could break my ass at any moment."
        ja "I love it!"
        off "She doesn't even try to keep it down."
        off "She basically screams on the phone."
        ja "Haaaaaaann, yeeeeeeeeeeeees!"
        scene ep5_sc18_lr_24
        uk "WHAT THE FUCK ARE YOU DOING UNDER MY WINDOW ?"
        mf "Fuck!"
        off "Holy shit."
        off "That yell startles all of us."
        off "That loud and unknown voice, Steve's reaction..."
        off "They've been caught in the act."
        off "I can hear them running."
        off "Someone is yelling things I don't understand in the background."
        mf "Left! Turn left !"
        off "More running."
        off "More screaming."
        mf "Here! Under the stairs! Hide !"
        off "We hear them try to catch their breath for a couple of minutes."
        off "Jane starts laughing."
        mf "Holy fuck! He almost caught us!"
        ja "Yes, he did!"
        off "She sounds happy."
        off "This girl really something else."
        mf "Holy fucking shit! He saw us... you think he recognized you ?"
        ja "Not a chance."
        ja "He was probably half drunk."
        off "Did they forget about us?"
        ja "Oh my God. You're still hard..."
        scene ep5_sc18_lr_25
        off "Just like in a goddamn porn movie."
        off "Come on... How is that even possible?"
        off "When did Steve become a freaking sex machine?"
        ja "Let me help you with that."
        mf "Oooh, that's very nice of you..."
        off "I can't believe it."
        scene ep5_sc18_lr_26
        off "Ensue a few minutes of uncomfortably close suction and licking noises intertwined with moans and crowned by a barely human groan."
        off "I imagine him letting go a gallon of semen like in these crazy hentai mangas he keeps reading."
        mf "Oh, shit, I'm done."
        off "She laughs."
        ja "Girls? Are you still there?"
        off "Jane's voice surprises us."
        sis "Oh, yes... yes, we're still there."
        ja "Great. I think it's time you take that phone to a more private place."
        ja "The three of us should talk."
        off "Wait, what?"
        scene ep5_sc18_lr_27
        sis "Ok... Just... Give us a minute..."
        off "They stand up and [sis_name] grabs my phone from the table."
        mc "Wait... Are you serious?"
        sis "What? We'll give you your phone back later don't worry."
        mc "No, no... I mean... What are you going to talk about?"
        sis "Obviously it's none of your business."
        mc "But... "
        off "I don't see anything to reply to that."
        off "But come on!"
        off "What the fuck is going on?"
        sis "Hang on a second, Jane."
        sis "Let's go to my room, [sf_name]. "
        scene ep5_sc18_lr_28
        off "I'm left alone in the living room."
        off "I can hear them climbing the stairs in a hurry."
        off "They are clearly eager to have that conversation between girls..."
        off "I don't know what to expect from that discussion between Jane and the girls."
        off "Nothing good, for sure."
        off "I have a feeling that I'm about to set foot in some kind of silly nightmare."
        off "I want to turn off all lights and scream in the dark."

        jump ep5NightDispatch
    else:


        off "We bought a pizza and a bottle of wine on our way back from Kelly's place."
        scene ep5_sc18_la_01 with dissolve
        off "[sf_name] called her father while [sis_name] took upon herself to install Kelly in the laundry room."
        off "The old sofa that sits in that room can be arranged in a pretty large and comfortable bed."
        off "I guess it'll be good enough for a few days stay."
        off "We talked about our meeting with Officer Smith and kept an eye open for the promised patrols."
        off "Surprisingly enough, we saw a couple of police cars cruising by our door in the next few hours."
        off "I'm not sure it'll be enough to deter the psycho twins..."
        off "...But it was reassuring to see that the police were actually doing something."
        scene ep5_sc18_lr_29
        off "We have since moved on to some more insignificant topics."
        off "Kelly just sits there silently waiting."
        off "I can see that she wants to take part in the discussion but doesn't dare to say a word."
        off "She's still dealing with her guilt and shame."
        off "I can't say I'm surprised."

        if ep4kfmeetingok == True:

            off "She said something about it when we met at the coffee shop the other day."

        off "She lusts for their friendship."
        off "She dreams about it."
        scene ep5_sc18_lr_30
        off "They're probably the only people who could legitimately hate her the most in this city, and Kelly longs to receive their forgiveness and their friendship."
        off "It's sad."
        off "Should I help her?"
        off "I've been telling the girls that we should trust her about the psycho twins and things like that, but asking them to forgive Kelly is something else entirely."
        off "I have no right to do that."
        scene ep5_sc18_lr_31
        off "They seemed ok to talk with her when they got back from her party, Monday night..."
        off "But exchanging a few polite words and friendship are clearly on a whole different levels."
        off "I should do something."
        off "Without talking about forgiveness, if they don't get along, the situation is going to get very, very awkward."
        off "How can I approach that, however?"
        off "If they could talk together, maybe..."
        off "Maybe I can propose a game."
        scene ep5_sc18_lr_32
        off "Like the one, we played on Sunday night."
        off "Yeah, that could do the trick."
        off "If I can get them to know each other better maybe it can ease things for everyone."
        off "Let's do that."

        off "I seize the first occasion to interrupt their discussion without being rude."
        scene ep5_sc18_lr_33
        mc "So... girls... I was thinking..."
        mc "How about we play that game again?"
        sis "That game?"
        mc "The drinking game we played on Sunday night..."
        off "[sis_name] looks at me suspiciously."
        off "I have a feeling that this conversation isn't going to be an easy one."
        scene ep5_sc18_lr_34
        sis "Are you trying to get us drunk?"
        mc "I just thought it could be fun..."
        sis "I'm not in the mood."
        sf "Me neither."
        sis "And I don't think we should drink too much."
        sf "We don't know what could happen..."
        off "Ok, they're right, maybe it's not a good time for a drinking game..."
        off "I should have thought about that."
        mc "I never..."
        sis "Yeah, you never."
        sis "I know what you're trying to do."
        sf "It's pretty obvious..."
        scene ep5_sc18_lr_35
        mc "Really ?"
        sis "You want us to get along."
        off "Well, that's a surprise."
        off "I expected them to go with the \"perv trying to get us drunk\" thing."
        off "They saw right through me."
        mc "I just think it would be better for everyone if we could make it... less awkward."
        sis "Yeah, sure."
        sis "You think I didn't see how you look at her?"
        sis "How you gazed over her all evening long ?"
        off "Kelly seems surprised and embarrassed."
        off "She lowers her head and looks at her hands clenched on her knees."
        mc "What?"
        scene ep5_sc18_lr_36
        sf "Subtility and discretion really aren't your forte."
        sis "You know exactly what I'm talking about."
        kf "I'm sorry, I don't want to cause any problem..."
        mc "You're not causing any, Kelly."
        mc "They're just making fun of me."
        mc "Alright."
        mc "I think that we should know her better, ok, but I didn't do the things you say."
        mc "We're going to spend a few days together so... maybe we should talk things out, once and for all."
        scene ep5_sc18_lr_37
        sf "You are right, [mc_name]."
        sf "But this conversation may not be pleasant."
        sf "For her, as much as for us."
        sf "Maybe even for you."
        sf "And the outcome may not be as positive as you hope."
        off "She turns to Kelly, who furiously refuses to make eye contact."
        off "I wonder what she is thinking about."
        off "Maybe I was wrong."
        off "Maybe she doesn't want to talk about anything at all."
        sf "Are you ok with that Kelly?"
        sf "Do you want THAT conversation to happen now?"
        kf "I... Don't think that things could get any worse."
        kf "I have nothing to lose, right?"
        sis "I can still throw you out."

        menu:
            "She's joking. [sisLovePath] [sfLovePath]":
                $ ep5sweetest = True
                scene ep5_sc18_lr_38
                mc "She won't throw you out, Kelly."
                mc "I promise."
                mc "She likes to play the tough and bitchy one but she's not like that at all."
                mc "She's the sweetest of us all."
                $ ProcessStat(2, "sis_affection")
                $ ProcessStat(2, "sf_affection")
                $ DumpNotStack()
                mc "You have nothing to fear."
                scene ep5_sc18_lr_39
                sis "Did you just call me the sweetest of us all?"
                sis "I'm not sweet at all, ok?"
                sis "Don't believe him."
                sf "He's kind of right."
                sis "Absolutely not."
                sis "I'll throw her out without even blinking."
                scene ep5_sc18_lr_40
                sf "Are you going to sulk now?"
                sf "I like it when you do that face..."
                mc "I have to agree that's she's damn cute when she pouts."
                sis "I swear, you'll pay for that, both of you."
                off "She turns away and tries very hard not to sulk."
                off "She fails."
            "Like I'm going to let you do that. [kellyPath] [sisSubPath] [sfDomPath]":

                $ ep5wontletyou = True
                mc "You won't throw her out."
                sis "Are you going to force her on me or something?"
                mc "No, I won't force anything on you."
                mc "But I won't let you throw her out."
                mc "And that's final."
                $ ProcessStat(2, "sis_submission")
                $ ProcessStat(2, "sf_dominance")
                $ ProcessStat(3, "kf_affection")
                $ DumpNotStack()
                scene ep5_sc18_lr_41
                off "[sis_name] briefly seems about to explode but she simply turns away and goes straight into sulking mode."
                sis "Yeah, whatever... We can't even joke anymore..."

        off "[sf_name] gently smiles."
        scene ep5_sc18_lr_43
        sf "No one will throw you out, Kelly."
        sf "But you may not be able to leave this house as you might wish either."
        sf "Remember that being alone, outside, may not be safe for you."
        off "Kelly seems a bit lost and surprised."
        off "She takes a few seconds to assimilate what we just said."
        kf "This has to happen. We..."
        kf "I should have done it sooner."
        kf "Apologizing is something but... It's not enough..."
        kf "I don't know where to start..."
        sis "You could tell us why you ruined our life, to begin with..."
        off "That's really not the kind of friendly discussion I had in mind..."
        off "And [sis_name] is definitely not helping with her aggressive tone."
        scene ep5_sc18_lr_44
        kf "I remember being jealous of [sf_name]."
        kf "The first time I saw her... it was obvious that she was... that she is... Way above my league."
        kf "I was the wealthy pretty girl, but when [sf_name] came into the picture it was clear that she was better than me in every way."
        scene ep5_sc18_lr_45
        kf "Her family had more money than mine, and yet she wasn't obnoxious about it..."
        kf "She was prettier than me and clearly more elegant but still modest and tempered."
        kf "Seeing her put me back in my place."
        kf "I felt like she was a lady fraying with the commons, while I was a peasant trying to pass for what I wasn't."
        kf "I didn't like it."


        if ep4sflovetalked == True:
            off "That's actually a good description of [sf_name]."
            off "I have a feeling that Miss Mei's tutoring is no stranger to that impression she leaves on people."

        scene ep5_sc18_lr_46
        kf "So... You know what I did."
        kf "I can't believe that I could do that because of jealousy alone."
        kf "But that's how I remember it."
        kf "I'm ashamed of myself."
        kf "I am sorry."

        off "So, in the end, it's just a question of competition between girls."
        off "That's actually pretty scary."
        scene ep5_sc18_lr_47
        sis "And what about me?"
        sis "You weren't jealous about me, right?"
        kf "It's... When I tried to discredit [sf_name]... I wasn't very successful."
        kf "People peddled my lies but... [sf_name] was... She has that kind of aura and my lies just couldn't stain her."
        kf "I managed to isolate her a bit but I couldn't get people to really believe that she was... what I wanted them to believe she was."
        kf "And the worse thing is that she didn't even seem to care about what people were saying around her."
        scene ep5_sc18_lr_46
        kf "It was a defeat."
        kf "A defeat she inflicted upon me without even trying to defend herself."
        kf "It was infuriating. One more humiliation."
        kf "That's when you came into the picture."
        kf "You just decided to become her friend."
        kf "I remember... the first time I saw you together..."
        kf "I asked someone what was your name and I told them something like..."
        kf "\"Isn't she the one who was sucking dicks in the restroom? What? You don't know? Yeah, a 3rd year told me he saw her sucking a few guys...\"."
        kf "It didn't take more than that..."
        kf "Two days later the whole school knew about it... even the headmaster."
        off "Was it so easy?"
        off "That's crazy."
        off "And I believed it too..."
        off "What a moron I've been..."
        scene ep5_sc18_lr_48
        off "She hides her face in her hands and starts sobbing."
        kf "The thing is... It made me notice something."
        kf "My lies couldn't really get to [sf_name], but you were a much easier target."
        kf "And... [sf_name] seemed to care about you."
        kf "A lot."
        kf "So if I couldn't hurt [sf_name] directly, I could hurt her through you."
        sis "I guess I'm always collateral."
        off "She sounds sad. I understand her."

        if sis_love_path == True or sis_sub_love_path == True:
            off "If I could I would close the gap between us and take her into my arms."
            off "I'm not sure she would enjoy it, however."

        kf "I am so sorry."
        sis "Yeah, sure..."
        scene ep5_sc18_lr_49
        off "Kelly wipes away her tears before continuing."
        kf "The first year... I spread a lot of rumours about you two."
        kf "A couple per month I think."
        kf "But as soon as the second year started... I didn't have to do anything anymore..."
        kf "The school itself was coming up with new rumours regularly."
        kf "I don't want to give the impression that I'm trying to minimise my responsibility."
        kf "But... I think that I haven't told any lies about you since the middle of that second year."

        sis "Great. That makes you only half a cunt."
        off "That's harsh."
        off "But I can't blame her."
        off "She has the right to be angry."
        scene ep5_sc18_lr_50
        off "I'm about to say something but [sf_name]'s eyes stop me."
        off "Kelly is right about her."
        off "She has this thing: she's always above everyone else."
        off "She obviously has already let go of any resentment against Kelly."
        off "Despite all her efforts, she couldn't blemish her."
        off "She holds no grudge against her."
        off "What's going on now, is for [sis_name] and Kelly only."
        off "They both need it."
        off "We shouldn't intervene."
        off "I'm a bit concerned, but I know it's true."
        kf "You're right. I deserve that. And more."
        sis "What? Are you going to let me insult you like that?"
        kf "I'm not going to defend myself."
        kf "I am guilty."
        kf "I have no excuses."
        scene ep5_sc18_lr_51
        sis "That's not even funny."
        sis "I want to punch you in the face, and I don't even know why anymore."
        sis "I wanted to kick your ass for all the lies you were spreading but you look so miserable right now that I'm sure it wouldn't even make me feel better."
        sis "If anything, it would make me the bad girl."
        off "I don't feel any real anger in [sis_name]'s voice."
        off "She seems more annoyed by Kelly constant apologizing than by her past lies."
        sis "Why do you even apologize?"
        sis "Do you think it's going to change anything?"
        sis "You keep telling us what you're not the same bitch anymore."
        sis "Why should we believe you ?"
        off "The same bitch."
        off "Her choice of words sounds deliberately provocative."
        kf "I ..."
        off "Kelly looks at me as if she was looking for help."
        off "She seems embarrassed as usual, but also a bit afraid."

        if ep4kfmeetingok == True:
            off "Come on, Kelly."
            off "Tell them everything you told me yesterday."
            off "You know you have to."

        scene ep5_sc18_lr_45
        kf "I had... a few problems... that helped me realize... that I wasn't a good person."
        sis "What? That's all?"
        sis "You think you can escape this discussion without telling us?"
        sis "You'd better be more specific than that."
        kf "I don't think it's important..."
        sis "I don't care."
        sis "I want the details."
        sis "All of them."
        sis "Now."

        kf "I don't want you to pity me."
        sis "Trust me, I won't."
        sis "Spit it out."
        scene ep5_sc18_lr_46
        off "Kelly takes a deep breath."
        kf "It began last year."
        kf "I've already told you that... my father conned his company and stole their money before he ran away with his secretary."
        kf "My mom... She was already... fragile."
        kf "Her illness got worse."
        off "What an asshole."
        off "He abandoned them, knowing that his wife was seriously sick."
        off "That guy has no heart."
        kf "Our situation got... difficult."
        kf "I skipped a few classes and started to have difficulties at school."
        kf "I asked for help. But no one was there to help me."
        kf "The ones I considered my friends... They didn't really care about me."
        kf "Progressively I came to realize that I didn't have any real friends."
        kf "All these people around me weren't interested in me as a person but in what I was."
        kf "They were just waiting for their chance to take my place, or something like that."
        scene ep5_sc18_lr_45
        kf "I can't blame them."
        kf "I guess that was the life I chose for myself."
        kf "But that was very painful because..."
        kf "In the meantime... you and [sf_name]... I watched you from a distance..."
        kf "And your friendship... it looked real."
        kf "I was envious of the two of you..."
        kf "I thought that maybe... We could..."
        kf "Of course, I knew it was impossible."
        kf "It was a punishment and I deserved it."

        if ep4kfmeetingok == False:
            off "It's called Karma I guess."
            off "Life can be funny sometimes."

        kf "I began to question all my relationships."
        kf "My friends, my boyfriend... everything was fake."
        kf "They were just trying to take advantage of me, as I was probably trying to take advantage of them."
        kf "As I said, I can't blame them."
        scene ep5_sc18_lr_46
        off "She's incredibly lucid on her past self."
        off "It's a bit humbling."
        off "Maybe I should question myself too."
        off "There's a lot of things I could blame myself for."

        kf "My mother's health got even worse."
        kf "I told her that I would take care of her but she asked to be hospitalized."
        kf "So I took her there."
        kf "At that time, I had already started crumbling."
        kf "Seeing my mom being taken care of... That was my breaking point."
        kf "I guess I was lucky."
        kf "Someone noticed me at the hospital."
        kf "She got me to talk and sent me... to a psychiatrist."
        kf "I have been in therapy since then."

        off "Lucky?"
        off "What does she mean?"
        off "Why do I have the impression that there's something terribly dark behind that?"
        scene ep5_sc18_lr_53
        kf "I... know what I've done."
        kf "I regret it and I'm ashamed of myself."
        kf "I know I have been a cunt, as you say."
        kf "There is little I can do beside apologizing and trying to be a better human being."
        kf "I really feel like I am a different person."
        kf "But I would understand that you don't believe me."
        kf "Even if I keep apologizing to you, I know I don't deserve your forgiveness..."
        scene ep5_sc18_lr_52
        sis "Wait. Let me sum up this."
        sis "You've been a bad girl and now that your life has gone to shit, you feel bad for what you've done."
        sis "Now that you know that all your previous friends are cunts, you've apologized to us because you want to befriend us?"
        sis "Is that how it is ?"

        off "That's a bit far-fetched, but exceptionally on point."

        kf "No! No! I... I apologized because I know that I've hurt you."
        kf "Your friendship... I can't even dream about it."
        kf "I know I don't deserve it."

        sis "Yeah. You know what you deserve?"
        sis "A good punch in the pussy!"

        off "That last word is magical."
        off "I can hardly prevent myself from laughing."

        off "My phone ring tone startles everyone."
        off "[sis_name] turns to me in what seems to be a burst of anger."
        scene ep5_sc18_lr_54
        sis "Who the fuck is calling you right now?"
        sis "Can't you see I have something important going on here?"
        sis "You're ruining it."
        off "Her reaction surprises me."
        off "I try to babble an apology as I get my phone out of my pocket to look at it."
        mc "I'm sorry... It's... It's Steve..."
        sis "Oh yeah? Give it to me."
        mc "What ?"
        sis "Give me your phone."
        off "Oh, Steve, I'm so sorry for what's about to happen..."
        scene ep5_sc18_lr_55
        sis "What the hell, Steve?"
        sis "Do you have any idea what time it is?"
        sis "I hope you have a good reason to..."
        off "She doesn't finish her sentence. Her attitude changes."
        sis "Oh... Yeah. Hello..."
        sis "No, I'm [sis_name]... Yeah..."
        off "What is going on?"
        sis "Yeah, she's here..."
        sis "Sure... No, we're doing good... Ok..."
        sis "You want me to put the speaker on?"
        sis "Ok, hold on a few seconds."
        off "She puts the phone on the table."
        sis "You're on speaker now."
        sis "Everyone can hear you."
        scene ep5_sc18_lr_56
        uk "Thank you, [sis_name], you're an angel."
        uk "Hello everyone."
        off "A girls voice."
        ja "This is Jane."
        ja "I'm Steve's girlfriend."
        sf "Hello, Jane..."
        mc "Hi..."

        ja "I want to share something with you."
        ja "Something I like a lot."
        off "I have such a bad feeling about this..."
        ja "Are you ready? Haaan!"
        off "That was a moan. No doubt about that."
        mc "Ready... for... ?"
        ja "Steve's just taken his fingers out of my pussy."
        off "Holy shit."
        ja "I can feel his dick pushing on my... Haaan!"
        off "HOLY FUCKING SHIT."
        scene ep5_sc18_lr_57
        off "[sis_name] and [sf_name] look at each other with surprise and embarrassment."
        off "Kelly seems almost afraid."
        off "The poor girl must wonder what kind of perverted household she has fallen into."
        mf "Not so loud honey!"
        mf "He's going to hear us."
        off "Steve's voice, in the background."
        off "They're hiding from someone and fucking at the same time?"
        off "I understand that the girl's into risky action... This is probably something like that."
        ja "Slowly! Yes!"
        off "Damn, Steve, you bastard."
        off "You're having the time of your life right now."
        ja "I can feel him penetrating me."
        ja "Centimetre by centimetre, slowly."
        sf "Oh my god."
        ja "As you say. Ooooh my God!"
        off "I don't know if I should laugh or cry."
        off "I'm here, with [sis_name], [sf_name] and Kelly, listening to Steve fucking his crazy girlfriend."
        off "The girls seem... actually curious about what's happening."
        off "Everything is normal."
        ja "It's so good! I like it."
        ja "Half of it is inside! There's so much!"
        off "[sf_name] bends toward the phone and shyly asks."
        sf "Isn't that... painful?"
        ja "Painful? Oh God no! Haaan!"
        ja "This is delicious!"

        off "This is so weird."
        off "I have a hard-on."
        off "And in the meantime, I'm embarrassed as fuck."
        ja "He's taking it out a bit."
        ja "He likes to tease me with his cock."
        ja "He knows I want it all inside me and he takes his time filling me up to the brim."
        ja "HAAAAN!"
        scene ep5_sc18_lr_58
        off "The girls seem genuinely interested in what's happening."
        off "Strangely, I'm kind of grateful."
        off "This audio porn is a much-appreciated mood changer after the discussion [sis_name] and Kelly just shared."
        ja "He's back inside!"
        ja "Deeper! Do it!"
        ja "Fuck me, baby! Fuck my pussy!"
        off "Her moans intensify."
        mf "You're too loud!"
        ja "I know! It's so good!"
        ja "We're doing it.... Right under my dad's window..."
        kf "What? Did she say..."
        sis "Her dad?"
        off "They're completely insane."
        off "Steve, you're going to die tonight."
        sf "Are you doing that... Next to your dad?"
        ja "Yes! It's so... exciting!"
        ja "Haaaan! Faster! Faster !"
        off "Her voice and moans suddenly sound muffled."
        off "I can hear some noise in the background..."
        off "Is that... The pounding?"
        ja "I'm so wet! I've wanted to do this for so long!"
        ja "Harder! Harder! Haaaaaaaaaan yes... That's it...."
        scene ep5_sc18_lr_59
        sf "What if he catches you?"
        ja "Haaaan... I hope he will !"
        off "She's insane. They both are."
        ja "He's taking me doggystyle."
        ja "He's going so deep! Haan !"
        off "The moans get out of hand."
        off "Discretion isn't her priority anymore."
        ja "I can feel him stretching my insides."
        ja "Haaan! Every time he hits me down inside, it sends shivers down my spine."
        off "Come on, how long is this going to last?"
        off "This is crazy."
        off "Steve is actually fucking this girl like a beast."
        off "STEVE."
        off "How is that even possible?"
        scene ep5_sc18_lr_60
        ja "My legs are shaking. Oh, my Gooooood!"
        mf "Quiet down! You're going to wake him up!"
        ja "He's plowing me so hard... He could break my ass at any moment."
        ja "I love it!"
        off "She doesn't even try to keep it down."
        off "She basically screams on the phone."
        ja "Haaaaaaann, yeeeeeeeeeeeees"
        scene ep5_sc18_lr_61
        uk "WHAT THE FUCK ARE YOU DOING UNDER MY WINDOW ?"
        mf "Fuck!"
        off "Holy shit."
        off "That yell startles all of us."
        off "That loud and unknown voice, Steve's reaction..."
        off "They've been caught in the act."
        off "I can hear them running."
        off "Someone is yelling things I don't understand in the background."
        mf "Left! Turn left !"
        off "More running."
        off "More screaming."
        mf "Here! Under the stairs! Hide !"
        off "We hear them try to catch their breath for a couple of minutes."
        off "Jane starts laughing."
        mf "Holy fuck! He almost caught us!"
        ja "Yes, he did!"
        off "She sounds happy."
        off "This girl really something else."
        mf "Holy fucking shit! He saw us... you think he recognized you ?"
        ja "Not a chance."
        ja "He was probably half drunk."
        off "Did they forget about us?"
        ja "Oh my god. You're still hard..."
        scene ep5_sc18_lr_62
        off "Just like in a goddamn porn movie."
        off "Come on..."
        off "How is that even possible?"
        off "When did Steve become a freaking sex machine?"
        ja "Let me help you with that."
        mf "Oooh, that's very nice of you..."
        off "I can't believe it."
        scene ep5_sc18_lr_63
        off "Ensue a few minutes of uncomfortably close suction and licking noises intertwined with moans and crowned by a barely human groan."
        off "I imagine Steve letting go a gallon of semen like in these crazy hentai mangas he keeps reading."


        mf "Oh, shit, I'm done."
        off "She laughs."
        ja "Girls? Are you still there?"

        off "We need a couple of seconds to understand we got Jane's attention back."
        sis "Oh, yes... yes, we're still here."
        ja "Great. I think it's time you take that phone to a more private place."
        ja "The three of us should talk."
        off "Wait, what?"
        scene ep5_sc18_lr_64
        sis "Ok... Just... Give us a minute..."
        off "They stand up and [sis_name] grabs my phone from the table."
        mc "Wait... Are you serious?"
        sis "What? We'll give you your phone back later don't worry."
        mc "No, no... I mean... What are you going to talk about ?"
        sis "Obviously it's none of your business."
        off "I don't see anything to reply to that."
        off "What the fuck is going on?"
        sis "Hang on a second, Jane."
        off "She turns to Kelly."
        scene ep5_sc18_lr_65
        sis "Are you coming or what ?"
        kf "Me ?"
        sis "Yeah, you."
        sis "Who else is a girl here ?"
        kf "I don't know..."
        sis "Like you have a choice."
        off "She goes back to my phone as Kelly stands up."
        sis "It'll be the four of us, Jane."
        sis "We... Have a friend with us for a few days."
        ja "Even better."
        off "Did she say friend?"
        off "That's an interesting turn of events..."
        off "Kelly noticed it as well."
        off "She seems about to cry as she basically runs towards [sis_name]."
        scene ep5_sc18_lr_28
        off "I'm left alone in the living room."
        off "I can hear them climbing the stairs in a hurry."
        off "They are clearly eager to have that conversation between girls..."
        off "This is one hell of a crazy evening."
        off "I don't know what to expect from that discussion between Jane and the girls."
        off "Nothing good, for sure."
        off "I have a feeling that I'm about to set foot in some kind of silly nightmare."
        off "I want to turn off all lights and scream in the dark."


label ep5sc19:
    scene black with dissolve
    with Pause(2)
    show text "Two hours later"
    with Pause(2)
    scene ep5_sc19_pool_01 with dissolve

    off "The night is burning hot."
    off "I should have stayed inside to enjoy the fresh bite of the AC..."
    off "... But I was feeling a bit oppressed by the weirdness of the situation."
    off "The girls abandoning me to have a discussion with Jane left me very confused."
    off "I shouldn't have let them go like that."
    off "I have no idea what they're talking about but I'm sure that nothing good will come out of it."
    off "Jane is crazy."
    off "No doubt about that."
    off "I don't know where Steve found her, and I'm kind of happy for him..."
    off "But I'm a bit worried about what she can tell the girls."
    off "Like... What if Steve has told her anything about me?"
    off "Will she tell them?"
    off "Jane seems obsessed with sex."
    off "They're probably going to talk about that."
    off "The girls looked very curious about it..."
    scene ep5_sc19_pool_02

    if dual_love_path == True:
        off "I guess they have doubts, and probably some questions..."
        off "We're... About to do it too so..."
        off "It sounds natural..."
        off "I can't believe it."
        off "I'm about to do it... With [sf_name], AND [sis_name]."
        off "How am I even going to do that?"
        off "I don't even know how to handle a girl, how am I going to handle two, at the same time?"
        off "How do they expect me to perform?"
        off "Perhaps they expect it to be perfect or something like that."
        off "Maybe they hope for a romantic mood."
        off "How do you do that when there are three people involved?"
        off "I'm going to fail."
        off "I know it."
        off "I'll be lucky if I manage to last more than a minute."
    else:
        off "[sf_name] especially..."
        if ep5sftruelove == True:
            off "Things got pretty serious between us."
            off "This afternoon in my room... that was intense."
            off "If [sis_name] hadn't called for her... perhaps we would have gone further."
            off "Maybe tonight..."
            off "Love..."
            off "We were simply flirting a couple days ago and now we're talking love..."
            off "And I like it."
            off "I feel ridiculous, but I like it."
            off "I don't care."
            off "I love the girl."
            if sis_sub_path == True:
                off "And that only makes things more complicated."
                off "How can I conciliate that with the things I do with [sis_name]?"
                if sis_sub_love_path == True:
                    off "There is absolutely no way I let go of her."
                    off "She's mine, I'm hers."
                    off "If I ever have to choose, I'll have to let go of [sf_name]."
                    off "And it will definitely break my heart."
                    off "But is there any solution?"
                    off "If I keep going like this, sooner or later, [sf_name] will find out."
                    off "She wouldn't understand."
                    off "It would be the end of us."
        if ep4sflovetalked == True and ep5sftruelove == False:
            off "Her, confessing like that..."
            off "That was a bit embarrassing..."
            off "I felt bad for not reciprocating but..."
            off "I can't help but think that this is going a bit too fast with our emotions."
            off "I don't know what to do."
            off "Her words sounded like an engagement..."
            off "I like her a lot, but I don't know if I want it to go that far."
            off "We're 18 years old."
            off "We're too young for that."
            if sis_sub_path == True:
                off "Maybe I should put an end to it."
                off "I have [sis_name] to focus on..."
        if sf_love_path == True and ep4sflovetalked == False:
            off "That's promising... She's interested."
            off "Perhaps we're going to speed up our game tonight..."

        if sf_dom_path == True:

            off "I wonder if that means something."
            off "Am I getting close to some... Change of dynamic?"
            off "I don't know what to do with that."
            off "That moment on the sofa, this afternoon... that was very strange."
            if sis_love_path == True or sis_sub_love_path == True:
                off "She could have killed me."
                off "And in the end, she seemed more sad than angry."
                off "I guess we'll need to have a more serious discussion about it tonight..."
                off "If she calls me..."
            if sis_hard_sub_path == True:
                off "She's crazy."
                off "I should stay the fuck away from her."
                off "I still don't know if she was playing some mind games with me or if she really knows what I'm doing with [sis_name] at night."
                off "But damn... If she's interested in taking a dick in the pussy, I'm still game."
            if sis_love_path == False and sis_sub_path == False:
                off "And so freaking hot."
                if ep5totaldom == True:
                    off "She handled me like..."
                    off "Her touch was..."
                    off "She emptied me like I was nothing."
                    off "That was incredible and so different from what she usually does..."
                else:
                    off "She didn't finish me but hell... that was still something."
                    off "I feel like that was a promise."
                    off "Maybe I won't have to take it in the ass as much as I feared."

    off "It's been what?"
    off "2 hours since they locked themselves in [sis_name]'s bedroom?"
    off "What are they even doing in there?"
    off "I'm not going to wait all night until they come out of their room."
    scene ep5_sc19_pool_03
    off "I'm yawning so bad that I could dislocate my jaw"
    off "Either they don't give a damn about me or they're laughing at me right now."
    off "Oh, come on, [mc_name]."
    off "Don't be like that."
    off "You feel abandoned and you're turning bitter."
    off "You should give them a little space."
    off "I'm sure that the conversation with Jane didn't even last that long."
    off "They took Kelly with them."
    off "And [sis_name] used the word friend."
    off "That means that... they probably have a lot of things to talk about."
    off "In the end, things turned out quite better than I expected."
    off "It's kind of weird."
    off "I can't help but feel bad."
    off "The lucidity Kelly seems to have with her past mistakes..."
    off "And how the girls forgave her..."
    off "That makes me think that they're all far better human beings than I am."
    off "I feel like crap."
    if sis_sub_path == True or sis_love_path == True:

        off "I'm even taking advantage of the situation."
        off "I can't deny it."
        off "I'm the worst."

    scene ep5_sc19_pool_05
    kf "[mc_name]?"
    off "Kelly's voice."
    scene ep5_sc19_pool_06
    mc "Hey, Kelly. Is everything ok? Do you need anything?"
    kf "I'm alright. Thank you."
    off "She shows me my phone."
    kf "I am supposed to give this back to you."
    mc "Thank you, Kelly..."
    off "She hesitates a few seconds."
    kf "Can I... join you?"
    kf "I don't want to disturb you..."
    mc "Sure. You're not disturbing me."
    scene ep5_sc19_pool_07
    off "She carefully sits next to me and dips her feet into the pool."
    kf "The water is so warm..."
    scene ep5_sc19_pool_08
    mc "Yes, it's not really refreshing..."
    off "She shyly plays with the water."
    off "If she wanted to tell me something she seems too embarrassed to utter a word."
    mc "So... What did you talk about with Jane?"
    kf "Oh... I'm sorry... I've promised not to tell you a word about it..."
    mc "Are you serious?"
    mc "Who decided that?"
    kf "A bit of everyone..."
    mc "What? Come on..."
    mc "It was some naughty stuff right?"
    kf "I'm sorry, I can't tell you anything..."
    mc "But why?"
    mc "I don't understand..."
    mc "Why keep that a secret from me?"
    kf "You should ask [sis_name] and [sf_name] about that."
    kf "Sorry."
    scene ep5_sc19_pool_09
    mc "You're kidding me right?"
    off "Obviously not."
    kf "I'm sorry, [mc_name], I promised..."
    mc "It's ok. I understand."
    mc "Forget about it."

    off "The silence that takes place between us isn't that uncomfortable."
    off "Kelly has some kind of humble and peaceful presence."
    off "I feel like she's bathing me in a warm aura of kindness."
    off "That's dramatically different from the cold hearted lying bitch she was a couple of years earlier."
    off "This is so strange."

    if ep4kfmeetingcanceledasshole == True:
        mc "Kelly, about yesterday..."
        mc "I'm sorry about the things I said to you on the phone."
        mc "It was very lame of me."
        kf "Oh, don't worry about it."
        kf "I understand."
        kf "You were rightfully angry."
        kf "I shouldn't have contacted you like that... That was... underhanded."
        kf "You had every reason to think that I was scheming something."
        scene ep5_sc19_pool_10
        mc "That doesn't justify my words."
        mc "I'm sorry."
        mc "Even anger doesn't give a free pass for that kind of aggression."
        kf "It's ok, [mc_name]."
        kf "Besides, you've already apologized for that."
        mc "Yes, but as you said, apologizing face to face feels... better."
        kf "Let's act as if nothing happened, please."
        mc "Alright."

    kf "I want to thank you, [mc_name]."
    kf "You have been very kind to me."
    kf "It's been a while since someone even seemed to care about me."
    off "I've barely treated her like a human being."
    off "What kind of world is she living in?"
    mc "I don't know what you're talking about, Kelly."
    mc "I didn't do anything."
    kf "You did a lot."

    if ep4kfmeetingok == True:

        scene ep5_sc19_pool_11
        kf "You listened to me."
        kf "That's was important to me."
        kf "I don't know if you believed me, but you were kind enough not to laugh at me."
        mc "Laughing at you?"
        mc "Has someone already mocked you for this?"
        off "She doesn't reply but her sad expression says it all."
        off "What kind of heartless bastard can be so cruel?"


    kf "You invited me to stay here."
    kf "You didn't have to do that but..."
    scene ep5_sc19_pool_12
    mc "Of course I had to do that!"
    mc "I couldn't do otherwise."
    mc "Should I have let you go back to Ray and Luke?"
    mc "They would have killed you, or worse."
    mc "And I'm not alone, [sis_name] and [sf_name] thought the same."
    mc "I know that [sis_name] doesn't seem like it but she was more than ok too."
    mc "She acts like she's always angry, but it's not really her."
    off "Who am i to talk about her like that?"
    off "I'm not even sure I know her myself anymore."
    scene ep5_sc19_pool_13
    kf "I kind of see it now."
    kf "And that's thanks to you too."
    kf "You helped me talking with her tonight."
    mc "No, I didn't do anything."
    mc "I didn't even think that you would have that kind of discussion, I only tried to push for a friendly exchange."
    mc "But I guess you and her... Needed that."
    mc "How was she?"
    mc "I mean, after you left for her room, tonight."
    mc "She called you a friend right?"
    mc "Did she treat you like one after that?"
    scene ep5_sc19_pool_14
    off "She seems to take a deep breath but suddenly starts sobbing."
    off "Tears flood her eyes and run down her cheeks."
    off "For god's sake, [sis_name]."
    off "What did you do to her?"
    mc "Are you alright Kelly?"
    mc "What happened?"
    mc "Did I say something?"
    off "She tries to wipe away her tears without much success."
    scene ep5_sc19_pool_15
    kf "I'm alright! I'm alright."
    kf "Everything is fine."
    kf "[sis_name]... After everything I've done to her..."
    kf "She treated me like we've been friends forever."
    kf "Once we got to her room, she didn't say a word about it, but it was like she completely forgave me."
    kf "And [sf_name] wasn't any different."
    kf "All the things I did to them..."
    kf "And they can forgive me..."
    kf "I'm happy, and in the meantime, that makes me feel even worse..."
    kf "They should hate me."
    kf "I don't deserve their kindness."
    scene ep5_sc19_pool_16
    mc "I know exactly how that feels."
    mc "You and I, Kelly, we have so much in common."
    mc "We have both wronged them for years and... in the end... they offer us a second chance."
    mc "They should hate us, but they don't."
    mc "That makes our guilt heavier."
    mc "They're so much better human beings than us that it makes us hate ourselves more."
    mc "We feel like we don't deserve that second chance."
    scene ep5_sc19_pool_17
    kf "I'm sorry [mc_name], it's my lies that made you..."
    mc "No Kelly."
    mc "I can't let you say that."
    mc "You lied, that's true, but I chose to believe it."
    mc "The more I think about it, the less I understand how I could do that, but I choose to believe it."
    mc "And you have nothing to do with that."
    mc "It's my mistake, not yours."
    off "She looks at me for a second before focusing on the pool."
    off "I can tell that she would gladly take my guilt and make it her own."
    off "This girl is so convinced that she deserves suffering that she searches for it."
    mc "So... I get it that she was nice to you."
    kf "Yes. Very nice."
    mc "Good..."
    scene ep5_sc19_pool_07
    off "Silence floods the place again."
    off "We spend probably a full minute looking at the pool without saying a word."

    if sf_love_path == True:

        scene ep5_sc19_pool_18
        kf "So... [sf_name] and you..."
        mc "She's my girlfriend, yes..."
        if dual_love_path == True:

            off "My official one at least."
        kf "She's very fond of you..."
        mc "I'm fond of her too I guess..."
        mc "Did she tell you about us?"
        kf "It was obvious by the way she talked about you..."
        mc "You talked about me ?"
        scene ep5_sc19_pool_19
        kf "No! We talked about a lot of things!"
        kf "And, you were mentioned a couple of times... So..."
        kf "I asked [sf_name] about it and she confirmed it."
        mc "Ok... Does that bother you?"
        kf "Oh no! I'm glad for you!"
        kf "It feels nice to see some... Genuine happiness..."
        off "She doesn't look so happy, though."


    scene ep5_sc19_pool_20
    mc "Kelly... The way you talk about... almost anything..."
    mc "I have the impression that you're going through some very dark times right now."
    mc "I don't want to be intrusive or anything but... you know..."
    mc "If you need friends..."
    mc "We probably still need some time to adapt to the situation but..."
    mc "We are here."
    mc "You don't have to be alone."
    scene ep5_sc19_pool_21
    off "She looks at me like she's about to cry again."
    off "She struggles to contains her tears."
    kf "I'm sorry, I might cry again..."
    mc "I don't see any reason to shed tears..."
    mc "But it's okay, you don't have to be sorry."
    mc "There's no shame in that."

    off "She rubs her eyes a few seconds and takes a deep breath."

    kf "Can I ask you a question ?"
    off "Her voice trembles."
    mc "Sure."
    scene ep5_sc19_pool_22
    off "She gets one of her feet out of the water."
    kf "Why do you all walk barefoot in this house?"
    off "I let out a little laugh."
    scene ep5_sc19_pool_23
    mc "It's a habit of my mom."
    mc "I guess we all copied it."
    mc "You can keep your shoes on, Kelly."
    mc "You don't have to walk barefoot if you don't like it."
    kf "Oh no! I'm just not used to it."
    kf "It's... oddly comfortable."
    kf "It'll probably sound stupid but... It makes me feel free."
    kf "I like it..."
    mc "All the better then... I like your feet by the way."
    mc "They're pretty."
    off "She laughs."
    scene ep5_sc19_pool_24
    kf "My feet? Really? Are you serious?"
    mc "Yes, I am."
    kf "Is that a fetish of yours?"
    mc "What? No!"
    mc "I just like your feet, I mean, they're cute, that's all!"
    off "She's smiling."
    off "A true and beautiful smile."
    scene ep5_sc19_pool_25
    kf "[sis_name] told me to be careful around you."
    kf "She said that you were a Perv."
    off "Why am I not even surprised?"
    mc "Ok. Listen, whatever she told you, it was a joke."

    if sf_love_path == True or sf_dom_path == True or sis_love_path == True or sis_sub_path == True:

        kf "You mean that you don't spy on them when they're in the shower?"
        mc "No! Of course not!"
        kf "[sis_name] also said that she caught you looking at my ass earlier today..."
        mc "What? They're the one who checked you out!"
        mc "They couldn't stop commenting on your... Assets..."
        kf "My assets?"
        mc "Yeah, if I were you, I would be careful around those two."
        scene ep5_sc19_pool_26
        kf "Oh, you think they might attempt to take my virtue?"
        mc "Who knows?"
        mc "They take showers together..."
        kf "Really? That sounds like fun."
        kf "Maybe I could join them?"
        mc "What?"
        off "She laughs."
        mc "Wait a second. You're joking, right?"
        scene ep5_sc19_pool_27
        kf "Who knows?"
        kf "[sis_name] told me that I had to annoy you a bit if I wanted in the team."
        kf "She gave me a couple of hints."
        kf "Am I doing it right?"
        mc "Oh great. I'm sure I'm going to enjoy that."
        mc "You're doing just fine, Kelly, don't worry."
        mc "I have no doubt you'll fit right in."
        scene ep5_sc19_pool_28
        off "She laughs and plants a little kiss on my cheek."
        kf "Thank you, [mc_name]."
        kf "You're a nice guy."
        mc "If you say so..."
        kf "I think I'll head to bed now."
        kf "Good night!"
        mc "Good night, Kelly."
        scene ep5_sc19_pool_29_alt
        off "I quietly watch her walk away from me."
        off "I'm a bit baffled by how easy this new complicity with the girls settled in but I'm sure that it's for the better."
        off "Kelly seemed happy."
        off "That's a nice development."
    else:


        scene ep5_sc19_pool_30
        kf "She also warned me that she would break my legs if I'd ever hurt you."
        off "I didn't expect that."
        off "I don't know what to reply."
        off "Does [sis_name] try to protect me?"
        mc "Why... Would you hurt me?"
        off "Her smile softens gradually."
        off "The silence gets a bit awkward."
        kf "I should go to bed."
        scene ep5_sc19_pool_31
        off "What did [sf_name] say about reading the mood?"
        off "Crap... Her lips are... Very tempting..."
        off "Would it be weird if I tried to kiss her?"
        mc "Yeah... it's getting late..."
        off "Does she want it?"
        off "She's supposed to have a crush on me, right?"
        off "Oh god, why isn't this easier?"

        menu:
            "Let her go.":
                $ ep5kfmissed = True
                scene ep5_sc19_pool_32
                off "Hold your horses, [mc_name]."
                off "It's... Too soon."
                off "And that would be weird."
                off "You should wait."
                off "Yeah. Let's wait."
                kf "Thank you for everything [mc_name]. You're a nice guy."
                scene ep5_sc19_pool_28
                off "She lightly kisses my cheek before she stands up."
                kf "Goodnight [mc_name]."
                mc "Goodnight, Kelly."
                scene ep5_sc19_pool_29_alt
                off "I silently watch her walk away from me like an idiot."
                off "Yeah, clearly, that was the right decision."
                off "Let's wait."
                off "Until I die a virgin."

            "Kiss her. [kellyPath]" if kf_affection > 14:
                $ ep5kfkissed == True
                scene ep5_sc19_pool_33
                off "I lean towards her and stick my lips to hers."
                off "I'm clumsy and far more brute than I hoped to be."
                off "I'm stealing this kiss."
                off "I'm a moron."
                off "I can feel her gasp in surprise but she doesn't escape my kiss."
                $ ProcessStat(3, "kf_affection")
                $ DumpNotStack()
                scene ep5_sc19_pool_34
                off "Her lips are warm and soft."
                off "There's a subtle scent of cinnamon floating around her."
                off "My guts are liquefying."
                off "We part ways too quickly."
                off "I'm out of breath."
                scene ep5_sc19_pool_35
                off "She looks at me with an indefinable expression."
                off "Did I fuck up something?"
                off "It was probably too soon."
                off "[mc_name], you're an idiot."
                mc "I'm sorry Kelly, I didn't want to offend you or anything..."
                kf "You didn't offend me, [mc_name]."

                if ep5kfnew == True:
                    kf "You know I have... A crush on you..."
                else:
                    kf "I... Have been interested in you for some time now..."


                kf "But I can't help but wonder why you did that..."

                menu:
                    "I like you... [kellyPath]":
                        $ ep5kfliked == True
                        mc "Do I need any other reason?"
                        scene ep5_sc19_pool_36
                        kf "You don't know me. How can you like me?"
                        mc "I know that I have a lot more to learn about you but..."

                        if ep5kfnew == True:

                            mc "The things you've already told me..."
                        else:

                            mc "The things you've told us..."

                        mc "And the way you said those things..."
                        mc "I guess that touched me."
                        mc "And as I said earlier... you and I have a lot in common..."
                        mc "Maybe I'm going a bit too fast... but... I care about you."
                        scene ep5_sc19_pool_37
                        kf "Are you pitying me?"
                        mc "No. I'm not."
                        mc "I just feel that we're alike."
                        mc "I want to know more about you."
                        off "She looks at me in silence for a moment."
                        off "She seems so vulnerable."
                        mc "Maybe it's a bit pretentious of me but..."
                        mc "Perhaps that we deserve each other."
                        $ ProcessStat(5, "kf_affection")
                        $ DumpNotStack()
                        mc "I'm sorry, I'm not making any sense."
                        scene ep5_sc19_pool_39
                        off "She kisses me."
                        off "Her lips intertwine with mine."
                        off "Our tongues, still shy, barely touch."
                        off "This kiss feels more real than the previous one."
                        off "My heart is pounding like crazy in my chest. "
                        off "And she backs away."
                        scene ep5_sc19_pool_40
                        off "She quickly stands up and takes a few steps away from me."
                        kf "I'm sorry, [mc_name]..."
                        kf "I... I'm not an easy package..."
                        kf "I have problems I can't impose on you..."
                        mc "What?"
                        kf "I'm sorry!"
                        mc "Kelly, wait, please!"
                        off "She runs away from me and disappears into the house before I even have the time to get on my feet."
                        scene ep5_sc19_pool_41
                        off "I'm confused."
                        off "Did I fuck up something?"
                        off "She kissed me too..."
                        off "I don't understand."
                        off "Why are girls so complicated?"
                    "Well, you're very cute...":



                        $ ep5kfcute == True
                        off "She seems disappointed."
                        off "What does she want to hear?"
                        mc "I mean, you're probably the cutest girl I've ever met."
                        mc "You're beautiful."
                        scene ep5_sc19_pool_38
                        off "She looks away in sadness."
                        kf "I guess I should thank you for the compliment."
                        off "I have no idea what to say."
                        off "I fucked up something, somewhere, but I don't know what."
                        off "Why are girls so complicated?"
                        kf "I'm sorry, I don't want to be that kind of girl anymore."
                        off "That kind of girl?"
                        off "What does she mean?"
                        scene ep5_sc19_pool_29
                        off "She stands up and walks away."
                        kf "Goodnight, [mc_name]."
                        off "I should say something but I don't really understand what's happening."
                        off "I just stay there watching her sailing away."
                        off "I'm an idiot."
                        mc "Goodnight, Kelly..."


label ep5NightDispatch:

    if evil_asshole_path == False:
        if sis_sub_path == False and sis_love_path == False:
            call ep5sc20_part1 from _call_ep5sc20_part1
        if sf_love_path == True and dual_love_path == False:
            call ep5sc21 from _call_ep5sc21
        if sf_dom_path == True and sis_hard_sub_path == False:
            call ep5sc22 from _call_ep5sc22

        if sis_love_path == True and dual_love_path == False:
            call EveEventIntro from _call_EveEventIntro

        if sis_sub_path == True:
            call EveEventIntro from _call_EveEventIntro_1

        if dual_love_path == True:
            call ep5sc25 from _call_ep5sc25

        if sf_love_path == False and sf_dom_path == False and sis_love_path == False and sf_affection > 4:
            call ep5sc20_part2 from _call_ep5sc20_part2

    jump day5end


label ep5sc20_part1:
    scene black with dissolve
    with Pause(2)

    if sf_love_path == True or sf_dom_path == True:
        scene ep5_sc20_c_01_alt with dissolve
    else:
        scene ep5_sc20_c_01 with dissolve

    $ ep5sisnighttalk = True
    off "I've checked every door and closed every shutter of the ground floor before going upstairs."
    off "Everything looks fine but I can't help being a bit nervous."
    off "I know there's no need to panic, though."
    off "They won't break into the house so easily."
    off "The doors are solid."

    if sf_love_path == False and sf_dom_path == False:
        off "No light, no noise."
        off "The girls are probably asleep."
        off "Steve and Jane's phone call was actually a welcome distraction albeit a very weird one."
        off "It has changed the mood for something better."

    if sf_dom_path == True or sf_love_path == True:
        off "There's a sliver light coming from under [sf_name]'s door."



    if ep5kfkissed == True:
        off "I don't know what to think about my conversation with Kelly."
        off "Did I miss something?"
        off "I thought she had a crush on me..."
        off "I'll guess I'll try to talk to her tomorrow."
        off "I'll ask her what I did wrong and apologize."
        off "Girls are so complicated..."
    if ep5kfmissed == True:
        off "I should have tried my luck with Kelly."
        off "What a goddamn moron."
        off "Maybe I'll grow a pair someday."
        off "Even Steve has a girlfriend."
        off "What am I doing with my life?"

    if moronic_hero_path == True:

        off "[sis_name] forgot to return my phone..."
        off "No big deal I guess."
        off "I'll have it back tomorrow."
        off "I can't think of anything else than our psycho twins problem."
        off "They will come."
        off "And I don't know if the cops patrolling outside will do anything to deter them."
        off "Probably tomorrow, when it'll be obvious that I'm not calling them."
        off "They will understand, and they will come."
        off "I need to be ready."
        off "I just need to keep them outside of the house until the cops arrive."
        off "It's feasible."
        off "Crazy but feasible."

    if sf_love_path == True or sf_dom_path == True:
        scene ep5_sc20_c_02_alt
    else:
        scene ep5_sc20_c_02

    off "Wait... I heard a noise."
    off "It seems to be coming from... my room?"
    uk "Oh! What are you doing stepbro? Oh my god !"
    off "Are you kidding me?"
    off "What the hell is going on here?"
    scene ep5_sc20_mcr_01
    mc "What the hell?"
    off "Is she watching a porn movie? In my room?"
    mc "What are you doing here?"
    scene ep5_sc20_mcr_02
    off "She barely gives me a look before focusing on the screen again."
    scene ep5_sc20_mcr_01
    off "The noise stops."
    sis "Waiting for you, obviously."
    off "I switch the lights on."
    mc "Wait, is that my laptop?"
    off "How the heck did she get my password?"
    scene ep5_sc20_mcr_03
    sis "It sure isn't mine."
    sis "Dude, your browser history is nasty."
    off "Shit. I'm dead. Again."
    sis "Incest porn really?"

    menu:
        mod "No Concequence yet."
        "I don't know what you're talking about. [gr]\[PornHack\]":
            $ ep5pornhack == True
            mc "I must have been hacked or something like that..."
            scene ep5_sc20_mcr_05
            off "She bursts out laughing."
            sis "You're killing me, Perv."
            sis "That's the best excuse I've ever heard!"
        "Hey, it's not like I have a choice, ok? [gr]\[PornChoice\]":

            $ ep5pornchoice == True
            mc "It's kind of trendy."
            mc "All the best actress are doing... that genre of movie... So..."
            sis "Yeah sure. And you watch it for the art."
            mc "Well..."
            scene ep5_sc20_mcr_05
            off "She bursts out laughing."
            sis "That excuse is so lame!"
            sis "I'll have to tell that one to [sf_name]!"


    off "At least she didn't get upset..."
    mc "Ok, ok, when you stop laughing like a maniac, maybe you could tell me what you're doing here?"
    mc "Looking into my stuff?"
    sis "I told you. I was waiting for you."
    sis "I wanted to talk."
    mc "Ok... about what?"
    off "She suddenly seems less confident."
    sis "... things..."
    off "It's a bit late for that but..."
    off "We didn't have much occasion to talk, just the two of us..."
    off "And we have a lot of time to catch up."
    mc "Ok... Let's talk, Princess."
    scene ep5_sc20_mcr_06
    off "I walk around the table and sit next to her. "
    off "Her attitude is much less aggressive."
    off "She grabs her legs and doesn't utter a word."
    off "Should I take the initiative?"
    mc "So... How are you doing, Princess?"
    off "She looks at me with a weird smirk on her face."
    sis "I'm doing fine."
    sis "Do I look like I'm not?"
    off "She tries to look tough but she kind of dropped the act the second I sat next to her."
    off "She's afraid."
    mc "You look terrified."
    sis "I don't know what you're talking about."


    menu:
        "You know what? [sisLovePath]":
            $ ep5pornhug = True
            mc "For my part, I think I could really use a hug..."
            $ ProcessStat(1, "sis_affection")
            $ DumpNotStack()
            off "She looks at me suspiciously."
            off "I expected her to throw a couple of \"Perv\" accusations at me but she throws herself instead."
            scene ep5_sc20_mcr_07
            off "She crashes on my chest and clutches on me as hard as she can."
            off "She bursts in tears immediately."
            off "It's a bit more extreme than what I was prepared for."
            off "I stand bewildered for a few seconds before I wrap my arms around her."
            scene ep5_sc20_mcr_08
            off "This feels strangely familiar."
            mc "It's ok, Princess."
            sis "I'm not crying!"
            mc "It's ok."
            off "I can feel her collapsing in my arms."
            off "She's been keeping her tough and aggressive face in front of everyone."
            off "I'm surprised that she choose to let go of herself with me rather than with [sf_name]."
            off "No, that actually makes sense."
            off "She stays strong for [sf_name]."
            off "I'm the only one she can turn to."
            off "Ironically, I realize only now that I'm just as afraid as she is."
            scene ep5_sc20_mcr_09
            sis "I should have listened."
            sis "We should have gone to the police on Sunday."
            sis "Now... Because of me..."
            mc "You can stop right there, Princess."
            mc "It is not your fault."
            mc "You did nothing wrong."
            sis "We should have called your mom..."
            mc "We'll call her tomorrow."
            mc "It's alright."
            mc "We'll talk to her together."
            off "It's weirdly satisfying to take on the role of the mature big brother and comfort her..."
            off "And at the same time, seeing her like this makes me sad."
            off "She softly sobs while I hold onto her."
            off "It lasts a couple of minutes before she parts from me, hiding her face while she wipes away her tears."
            scene ep5_sc20_mcr_10
            off "She goes back to the other side of the sofa and looks away from me."
        "If you say so...":


            $ ep5pornso = True
            scene ep5_sc20_mcr_10
            off "She looks away without saying a word."
            off "I guess I'll give her some time."
            off "We still have a long way to go until we truly repair our relationship."
            off "If it's even possible."

    off "She whispers."
    sis "You think that they will try something?"

    menu:
        mod "Unknown Conequence."
        "Yes. [gr]\[WtYes\]":
            $ ep5wtyes = True
            mc "But it'll be ok."
            mc "The cops are patrolling, and if they come here during the night, they won't be able to enter easily."
            mc "I'm sure they will make enough noise to wake us all up."
            mc "The cops will be here before they set foot in the house."
            mc "We can handle that together."
            sis "So, you think we'll be alright?"
        "No. [gr]\[WtNo\]":

            $ ep5wtno = True
            mc "They're crazy, but they're also cowards."
            mc "There's not a chance that they will try anything."
            mc "The cops are patrolling, and I'm here too."
            mc "They won't try anything and I'm sure that it's only a matter of time until the police catch them."
            sis "You're trying to reassure me, aren't you?"


    mc "We'll be fine, Princess."
    mc "I promise."
    off "She takes a deep breath and sighs."
    off "She focuses on her toes for a bit."
    off "I don't know if she's waiting for me to say something or if I should shut up."
    off "The silence isn't really weird nor awkward."
    off "It actually feels nice to share this moment with her."

    if sf_love_path == True:
        scene ep5_sc20_mcr_11

        sis "Are you serious about her?"
        off "Her question surprises me."
        off "It takes me a few seconds to understand that we have changed the topic."
        off "It's about [sf_name]."
        mc "I ... think so..."
        off "Her attitude changes."
        off "She takes a more protective tone."
        scene ep5_sc20_mcr_12
        sis "I'm not gonna threaten you again."
        sis "I just need you to know that if you're not serious about her, you should put an end to it."
        sis "Right now."

        menu:
            "I like her very much.":
                $ ep5ntsfliked = True
                mc "I'm not going to hurt her or anything..."
                off "She frowns."
                scene ep5_sc20_mcr_14
                sis "Like?"
                sis "Do you understand what I just said?"
                mc "What did I say?"
                sis "Liking her isn't nearly enough, [mc_name]."
                sis "She's already way past that point."

                if ep4sflovetalked == True:
                    sis "She loves you."
                else:
                    sis "She thinks she loves you."

                sis "It's not about sharing a moment anymore."
                sis "She talks about... A Life defining love."
                sis "Do you understand?"
                sis "LOVE. In capital letters."
                sis "She dreams about life, adventure, engagement, children."
                mc "Wow wow wow wow wow."
                mc "You're kidding."
                mc "You're trying to frighten me or something."
                mc "We've been a thing for barely 3 days..."


            "I love her. [sfLovePath]" if ep5sftruelove == True:
                $ ep5ntsfloved = True
                off "She frowns."
                scene ep5_sc20_mcr_14
                sis "Love?"
                sis "Are you sure about that?"
                sis "Aren't you a bit too quick in using that word?"
                off "I don't understand her reaction."
                off "Why does she get upset?"
                off "Maybe she thinks I'm lying?"
                mc "I know... It sounds ridiculous... but..."
                mc "I really think that I love her..."
                sis "And you moron, you've told her that."
                mc "Yeah... She confessed she loved me... so I replied..."
                sis "You have no idea what you have done."
                off "I'm totally puzzled. "
                mc "Well, maybe you can stop talking in riddles and explain it to me then..."


        off "She obviously has something important to say but she hesitates."
        scene ep5_sc20_mcr_15
        sis "You have to promise me that you won't tell this to anyone, not even to [sf_name]."
        mc "Sure. I won't tell anyone."
        sis "Swear it."
        mc "I swear. Don't worry. I know how to keep a secret."
        off "She probes my gaze in search for a reason to trust, or distrust me."
        sis "I'm trusting you with something very important here."
        sis "Please don't make me regret it."
        mc "I swear, [sis_name]. You won't regret it."
        scene ep5_sc20_mcr_16


        if ep4sflovetalked == True:
            sis "You already know about Miss Mei."
            sis "She told me about your conversation."
            mc "Yeah... That's quite an interesting character..."
            sis "You know what she taught [sf_name], about boys."
            sis "You know how she warned her."
            mc "Yeah..."
        else:

            sis "I can't tell you everything but... I'll summarize it like that..."
            sis "[sf_name] has been raised by someone who... warned her about guys."
            sis "For like 10 years, she's been taught that men are pigs and brutal abusers and..."
            sis "Things like that."
            sis "She's been told not to ever trust a guy."
            mc "Ok..."
            mc "That mysterious teacher sounds very angry against the whole male gender..."


        sis "Now... How do I say this..."
        sis "Shortly after we met, I... Introduced [sf_name] to ... Romance novels..."
        sis "And she has been obsessed with that kind of literature, since then."
        mc "Romance novels?"
        off "I don't really see where this is going..."
        sis "Yeah... you know..."
        mc "Are you talking about girls erotic literature?"
        sis "It's... well... You could say it like that..."
        sis "But the main component of these novels isn't just erotica."
        scene ep5_sc20_mcr_17
        sis "It's love."
        sis "A mutual love so strong that it makes you lose control, of everything..."
        mc "Yeah sure... But hold on a minute."
        mc "You were fifteen at the time... and you were reading erotic novels?"
        sis "Yeah, because you were a saint and didn't do anything like that too."
        sis "At least we weren't watching incest porn..."
        mc "Oh, come on, everyone watches incest porn nowadays... It's like the new vanilla..."
        sis "I'll trust your expertise, Perv."
        sis "Now, can we focus on the real subject, please?"
        mc "Yeah... sorry..."

        if ep4sflovetalked == True:
            mc "Ok... so... [sf_name] has some trouble trusting men because of Miss Mei teachings."
        else:
            mc "Ok... so... [sf_name] has some trouble trusting men because of her mysterious teacher."

        off "And in the meantime, she's obsessed with novels where the heroine lives a crazy love story..."

        sis "Yes."
        scene ep5_sc20_mcr_18
        mc "Are you saying that [sf_name] has some... internal conflict because of this?"
        sis "She doesn't know where to stand."
        sis "She dreams about that crazy idealized love she keeps reading about..."
        sis "... While every guy we have encountered the last three years was at least a douchebag if not a complete asshole."
        sis "She wants to believe that love is possible, and in the meantime, she's terrified that a man, could just use her and throw her away..."
        sis "Or worse."
        off "Worse?"
        sis "And then... You come in."
        sis "And for once... You're not a total imbecile..."

        if ep3handshaked == False:
            sis "You take that... heroic stance where you kind of protect us."

        scene ep5_sc20_mcr_19
        sis "And you're nice to her..."
        sis "And she starts thinking that maybe everything she was taught is a lie?"
        sis "Maybe you're like the guy in these novels?"
        sis "Maybe you're the love of her life."
        sis "Maybe you're going to ravish her and take care of her forever in some kind of unending life of pleasure and love..."
        off "Ok, that escalated quickly..."
        mc "Did she tell you that?"
        sis "Yes, she did."
        scene ep5_sc20_mcr_20

        if ep5sftruelove == True:
            sis "And then you told her that you love her."
            sis "That obliterated her last doubts."
            sis "Now the only thing she wants is to surrender herself to you, completely."
            sis "She wants to take... That leap of faith her novels are talking about..."
            sis "You understand what I mean, right?"

            menu:
                "Yes. I understand.":
                    off "I guess I should be happy... but instead, I feel kind of sad."
                    off "How can I meet her expectations?"
                    off "It's just impossible."
                "Not really...":

                    sis "Oh come on, you want me to spell it for you?"
                    sis "She's ready to have sex with you, moron!"
                    mc "Oh! Ok..."
                    off "I feel lame."
                    off "And unworthy."

        elif ep4sflovetalked == True and ep5sftruelove == False:
            sis "She confessed to you this morning, right ?"
            off "[sf_name] told her everything."
            mc "Yeah..."
            sis "And you didn't reciprocate."
            sis "She tried not to show it to you but it hurt her."
            sis "However... She quickly decided to... Give you another chance."
            sis "Do you understand, [mc_name]?"
            mc "I think I do, yes."
        else:

            sis "She still has some doubts, but she desperately wants to live that fairy tale."
            sis "She just waits for a sign from you."


        scene ep5_sc20_mcr_21
        sis "So I'm asking you again, [mc_name]."
        sis "Are you serious about her?"
        sis "Do you think you can give her what she wants?"

        menu:
            "I don't know. [sfLovePath]" if ep5ntsfloved == True:
                $ ep5ntsfgogogo = True
                scene ep5_sc20_mcr_21
                mc "Her expectations are... way too high, and I have obviously not a single chance of meeting them."
                mc "But... I'm willing to try."
                mc "I love her. I have no doubt about that."
                mc "You will probably think I'm crazy, or ridiculous, but... listening to you right now... I just love her more."
                mc "I'll have to tell her that I'm only a... regular human being, but I'll try to make her happy."
                mc "I'll do my best."
                mc "I know it's silly to talk like that."
                mc "We're barely 18 years old and... it's our first relationship, for both of us..."
                mc "But I'm ready to give her everything I have too."
                off "Her expression is weird."
                off "I don't know if it's sadness, jealousy or disappointment."
                off "Perhaps a mix of the three."
                scene ep5_sc20_mcr_23
                sis "Those are some big words."
                mc "You don't look satisfied."
                sis "She's dreaming."
                sis "And there's no way you can give her what she hopes for."
                sis "But she will settle for less as long as she feels loved."
            "As I said... I like her very much...":


                $ ep5ntsfnogo = True
                scene ep5_sc20_mcr_21
                mc "There's no way I meet her expectations."
                mc "To be honest... that sounds pretty crazy to me..."
                if ep5ntsfloved == True:
                    mc "I mean... Love is something that should come later... right?"
                    mc "Once we know each other better."
                    mc "Maybe that in a month I'll be madly in love with her, but for now..."
                mc "She's a very nice girl that I like and I truly care about her..."
                mc "But I don't know if I want it to get that serious..."



        scene ep5_sc20_mcr_24
        sis "Just... please..."
        sis "If you're looking for a quick fuck, or even a few weeks of fun..."
        sis "Don't."
        sis "I can understand that Steve's thing gave you ideas..."
        sis "But please, don't."
        sis "I beg you."
        sis "That would destroy her."

        if ep5sftruelove == True:
            mc "You don't need to beg me, [sis_name]."
            mc "I want to make her happy."
            mc "That's all I want."
        else:
            mc "You don't need to beg me, [sis_name]."
            mc "I don't want to hurt her in any way."
            mc "I'll talk with her."

        sis "I hope so..."
        sis "If you fuck this up I will kill you for real, [mc_name]."
        sis "You know that."
        off "This threat has never been so serious."
        off "But this time, she also sounds sad."
        mc "I know. Thank you for the warning."


        off "I can taste her bitterness."
        off "That conversation wasn't the most pleasant for her."

    if moronic_hero_path == False:
        scene ep5_sc20_mcr_25
        off "She sighs."
        sis "So... What do you think of Kelly?"

        off "The tone of the conversation has shifted towards something more relaxed."

        if sf_love_path == True:
            off "The change of subject, however, is a bit abrupt and leaves me speechless for a few seconds."

        mc "What do I think of her?"
        sis "Yeah... You do believe her right?"
        sis "I mean, when she says that she's not the same person any more..."
        mc "I didn't know the... Old Kelly, so I can't really judge on that."
        mc "But her story... And the way she tells it..."
        mc "I want to believe her..."
        scene ep5_sc20_mcr_26
        sis "I guess she was convincing..."
        off "Why does she look so sad?"
        off "Is it that Kelly's story moves her like that?"
        off "She sure didn't look that emotional when Kelly told us about it."
        mc "So you forgave her in the end?"
        sis "I hated her, you know... For years..."
        sis "But in the end, I felt like it was useless."
        sis "The thing I hated was already gone."
        sis "After we saw her on Monday night, [sf_name] told me that hate was useless, and that it could consume you."
        sis "That the best revenge we could get was to let go of the past."
        sis "And she's right."
        sis "So... Yeah, I forgave her."
        mc "I'm actually proud of you."
        sis "Oh please, don't make it weird..."
        scene ep5_sc20_mcr_26_prime

        if ep3sisluked == False:
            sis "You forgave her pretty quickly too..."
            sis "You weren't so forgiving when we got back from the party on Monday Night..."
            mc "It's easy to hate someone when you don't know her."
            mc "That was stupid of me."
            mc "I'm glad you didn't listen to me on that one."
            mc "And as you said yourself... If I deserve a second chance, maybe she does too."
            sis "I guess I can't be wrong every time..."



        mc "You even called her your friend."
        mc "I was quite surprised..."
        sis "That was... What she wanted... Right?"
        sis "I don't know if we're really friends."
        sis "She'll never be a friend like [sf_name] is."
        sis "But we can try."
        off "Kelly's story definitely got to her. [sis_name]'s heart is soft and sweet."


        if sf_love_path == False and sf_dom_path == False and sis_love_path == False and sis_sub_path == False:
            scene ep5_sc20_mcr_27
            sis "Are you going to make a move on her?"
            off "She doesn't sound pissed, nor even sarcastic."
            scene ep5_sc20_mcr_28

            if ep5kfkissed == True:
                scene ep5_sc20_mcr_29
                mc "I kissed her tonight."
                sis "I guess that answers my question."
                mc "It was really strange."
                mc "We kissed and then she basically ran away from me."
                sis "You're breath is that bad?"
                mc "I guess so."
                mc "She turned green and puked in the pool."
                mc "Pfff."
                mc "I don't know."
                mc "Perhaps I said something wrong."
                mc "I'll let the night pass on it and I'll try to talk to her tomorrow."
                sis "Maybe she just needs some time..."
                mc "Maybe."
            else:

                scene ep5_sc20_mcr_30
                mc "I don't know... I'm not gonna lie, she's... very, very cute."
                mc "And I feel like she's interested in me..."
                mc "But with this setting..."
                mc "I don't want her to feel she has to give in to me just to stay with us or anything like that."
                sis "The situation may not be the best for that kind of development."
                mc "Yeah... That's what I thought."

        scene ep5_sc20_mcr_26_prime
        mc "May I ask what you talked about with her?"
        mc "You've spent like two hours locked in your room..."
        sis "Girls talk. You know. Plenty of things."
        mc "You won't tell me?"
        sis "I won't tell you."
        mc "I figured as much."



    if moronic_hero_path == True:
        mc "I guess it's useless to ask about your conversation with Jane?"
    else:
        mc "I guess it's also useless to ask about your conversation with Jane?"

    scene ep5_sc20_mcr_31
    sis "My lips are sealed."
    mc "Oh come on!"
    mc "At least give me a hint!"
    mc "Did you talk about me?"
    mc "It was about sex right?"
    mc "Did she gave you a show or something?"
    sis "Yes."
    mc "Yes? What question does that answer?"
    off "She laughs."
    sis "I'll let you guess."
    mc "You're playing dirty."
    sis "I'm trying my best."
    sis "Listen, the only thing I can tell you is that Jane is a really interesting person."
    sis "She may be completely crazy, but she's kind and very friendly."
    sis "She's also completely hooked up on Steve."
    sis "As crazy as it sounds."
    sis "You should talk to him."
    sis "And I mean, a serious talk."
    mc "A serious talk?"
    scene ep5_sc20_mcr_32
    sis "Yeah... We're going to be an interesting bunch of crazy and broken people... And idiots."
    mc "What are you talking about?"
    mc "Oh please, can't you be more explicit?"
    sis "I promised not to say a word about it."
    mc "You can't tease me so much and give me nothing."
    mc "That's just... Psychological torture."
    sis "It's a thing us girls are very proficient at."
    off "She laughs again and rises from the sofa."
    scene ep5_sc20_mcr_33
    off "She waves goodbye as she heads for the door."
    sis "Good night, [mc_name]!"
    mc "Good night, Princess."
    sis "I liked talking with you."
    mc "I liked it too."
    off "She disappears in the hallway and closes the door behind her."

    if ep2cameraset == True:
        off "I suddenly think of the camera I've set in the bathroom."
        off "I need to get rid of that shit."
        off "If I want to be a decent brother or anything close to that, I need to stop that bullshit."

    return


label ep5sc20_part2:
    scene black with dissolve
    with Pause(2)
    show text "The middle of the night."
    with Pause(2)

    scene ep5_sc20_mcr_34 with dissolve

    sf "[mc_name]?"
    off "I wake up with a jolt."
    mc "What? What's going on?"
    off "A feminine silhouette leans towards me, her hand gently touches my leg."
    off "It's [sf_name]."
    sf "I'm sorry, [mc_name]... I didn't mean to... I mean... Of course, I meant to... but I'm sorry to wake you up."
    off "I have a hard time emerging from my slumber and that sentence confuses me."
    off "What is she talking about?"
    off "[sf_name] wouldn't wake me up like that without a reason."
    off "Something is going on."
    mc "What's going on, [sf_name]?"
    mc "Did something happen?"
    mc "Just give me a second..."
    scene ep5_sc20_mcr_35
    sf "No, no, sorry [mc_name]. It's..."
    off "I can hear the embarrassment in her voice."
    off "She sighs."
    sf "I can't sleep."
    off "I wait a few seconds for a follow up that never comes."
    mc "Ok... I'm sorry to hear that..."
    sf "Can we talk? Just a few minutes..."
    off "What kind of conversation could not possibly have waited until tomorrow morning?"
    mc "Oh... sure..."
    sf "Thank you."
    off "She stops me as I'm about to stand up."
    sf "Don't move [mc_name]. I'll just..."
    scene ep5_sc20_mcr_36
    off "She lies next to me."
    off "I have no idea what's going on."
    off "She's clearly not like her usual self."
    off "We lay there in silence for several seconds before she starts talking again."
    sf "I'm sorry, this is ridiculous, I shouldn't have woken you up like that..."
    mc "It's ok, [sf_name]. Just... Tell me what's bothering you."
    off "I still don't understand why she came to me."


    if ep3sfangrylove == True or ep4dompathended == True:
        if ep3sfangrylove == True:
            off "We kissed a couple of time..."
        if ep4dompathended == True:
            off "She... Made me do those things..."

        off "But ... That doesn't make us particularly close or anything..."
        off "Shouldn't she go to [sis_name] instead of me?"


    scene ep5_sc20_mcr_37
    sf "I'm not afraid."
    sf "It's just... I'm a bit stressed."
    off "So it's about fear."
    off "I guess she's just human after all."
    sf "It's... I've been thinking about all that, over and over again..."
    off "I'm pretty sure we all do."
    mc "Are you sure you want to be here, [sf_name]?"
    mc "You could have returned home."
    mc "I'm sure that your Dad would feel better..."
    scene ep5_sc20_mcr_38
    sf "I want to stay with [sis_name]."
    off "Ok... but you're in my bed right now, not hers..."
    sf "If I return home, will they leave you alone?"
    mc "There's no way to predict what they will do."
    mc "They're insane."
    mc "But I feel like they wouldn't."
    mc "They want to hurt you to get revenge on your father."
    mc "They'll probably want to hurt [sis_name] too, to get revenge on you, and me."

    if moronic_hero_path == False:
        mc "And they'll want to hurt Kelly, because she warned us."

    mc "I have little doubt that they would torture and kill us all if they could."

    sf "How can you say that and stay so calm?"
    mc "I'm just as terrified as you are [sf_name]."
    mc "It's normal."
    mc "But we're safe here."
    mc "They can't get in here and it's only a matter of time before the police get them."
    mc "We just have to wait."

    scene ep5_sc20_mcr_39
    sf "Do you think they will try something?"
    sf "They will come during the night, won't they?"
    mc "That seems like the logical thing to assume."
    mc "But I'm sure that the cop will get them before they do anything."
    mc "You know, the patrols..."
    sf "They pass once every hour."
    off "Ok... that's not much."
    mc "Yeah... But as I said... They can't get in here."
    mc "And you can't break a door without making a lot of noise."
    mc "If they try anything, we will know and we will call the cops."
    mc "It's as simple as that."
    off "She takes a deep breath."
    scene ep5_sc20_mcr_40
    sf "You know... I can defend myself..."
    sf "And I already have, but never against something so serious..."
    sf "I don't want... To be alone, [mc_name]..."
    off "Alone?"
    off "She turns to me."
    sf "Will you help me? When they'll come?"
    off "The question baffles me."
    off "Her voice trembles."
    off "She's about to cry."
    mc "Are you serious?"
    mc "Do you really think that I could just stand there and do nothing?"
    mc "Of course, I'll help you, [sf_name]."
    scene ep5_sc20_mcr_41
    off "She rolls over the bed and huddles against me."
    off "I instinctively wrap my arms around her."
    off "The sobs start almost immediately."


    if ep3sfangrylove == True or ep4dompathended == True:
        if ep4dompathended == True:
            sf "The things I did to you... I didn't want to..."
        if ep3sfangrylove == True:
            sf "I rejected you..."

        mc "It doesn't matter [sf_name]."
        mc "It's ok."


    scene ep5_sc20_mcr_42
    mc "Don't worry."
    mc "I won't let anything happen to you."
    mc "I promise."
    off "I hug her gently while she softly cries for a few more minutes."
    off "The tears stop as she falls asleep."

    return


label ep5sc21:
    scene black with dissolve
    with Pause(2)
    scene ep5_sc21_c_01 with dissolve


    off "Ok, [mc_name]. Breathe."
    off "This is the moment."
    off "It'll be alright."
    off "You can manage, right?"
    off "No pressure. Just relax."
    off "Don't be a dork, and everything will be just fine."
    off "Knock on that door now. Not too hard."
    off "Yeah, like that."
    sf "Come in."
    off "Her voice is barely audible."
    scene ep5_sc21_mbr_01
    mc "Hey."
    sf "Hey."
    off "I can't read her expression."
    off "I don't know it she's afraid or impatient, perhaps a bit of both."
    scene ep5_sc21_mbr_02
    off "The way she looks at me triggers me."
    off "My heart pulses so hard in my chest that I feel dizzy. "
    off "The mood is very different from yesterday."
    off "It feels more serious."
    off "The stakes are much higher."
    off "She waits for me to say something but I'm as petrified as her."
    scene ep5_sc21_mbr_03

    if ep5sftruelove == True:
        off "Both of us want to go further but neither of us knows how to initiate it."
        off "It became real and with that, the stress of the situation has made it difficult to overcome."


    if ep4sflovetalked == True and ep5sftruelove == False:
        off "We have to talk about her confession and my reaction."
        off "There's something awkward between us since then."
        if ep5sisnighttalk == True:
            off "And in any case, [sis_name] has been pretty clear."
            off "We need to have a conversation."

    if ep4sflovelicked == True:
        off "After last nights failure, I shouldn't have expected it to be less awkward."
        off "I have to get out of it one way or another."
        if ep5sisnighttalk == True:
            off "And in any case, [sis_name] has been pretty clear."
            off "We need to talk about what's going on between us."


    off "I take a couple of steps towards her while she stands up from the bed."
    scene ep5_sc21_mbr_04
    mc "I just wanted to see if you needed anything."
    mc "Like a kiss, or... a kiss maybe?"
    off "She laughs."
    sf "A kiss would be nice."
    scene ep5_sc21_mbr_05
    off "She passes her arms around my neck as I seize her waist."

    if ep5sftruelove == True:
        $ ep5sflovecomplete = True
        scene ep5_sc21_mbr_06
        off "Soft and gentle at first, the kiss becomes more intense after a few seconds."
        off "I welcome the warmth of her body and let my hands wander on her back."
        scene ep5_sc21_mbr_07
        off "I can feel her weight on my neck as if she was trying to climb on me."
        off "Going with the flow, I grab her ass and lift her from the floor."
        scene ep5_sc21_mbr_08
        off "I don't even think about it."
        off "She weighs close to nothing."
        off "She squeaks in surprise and wraps her legs around me."
        off "She laughs."
        off "I hold her as tight as I can."
        off "This isn't a kiss anymore."
        off "We're furiously devouring each-other's breath, our tongues continuously meeting in a sensual wrestle."
        off "The longer we keep it going, the less we're able to think clearly."
        off "Pure lust dominates us. "
        off "She clutches on my head, pulling my hair."
        off "I imprint the mark of my hands on her butt cheeks."
        scene ep5_sc21_mbr_09
        off "I don't know why I put her against the door."
        off "That makes her laughs again."
        off "She whispers."
        sf "The bed would be more comfortable."
        off "I can't disagree with that."
        off "I feel ridiculous."
        off "I move us to the bed and sit on it."
        scene ep5_sc21_mbr_10
        off "I let go of her ass and move on to her hips, then her waist."
        off "I grab the bottom of her tank top and lift it."
        off "I only realize what I've done once her shirt lies on the floor."
        off "Her exposed breasts take my breath away."
        off "She looks at me with a mix of surprise and arousal."
        scene ep5_sc21_mbr_11
        off "And maybe a bit of fear."
        off "Do I scare her?"
        off "I just stripped her naked after all..."
        mc "[sf_name]... If I'm going too far... Just tell me to stop and I will understand."
        mc "I love you."
        mc "The last thing I want is to hurt you or force you into doing anything you wouldn't be ready for."
        mc "I can wait."
        scene ep5_sc21_mbr_12
        off "The words aren't easy to speak."
        off "She slowly nods but doesn't utter a sound."
        off "I guess she's okay with it."
        off "I gaze over her breasts and try very hard not to just jump on them and knead them like a brute."
        off "I'm very proud of my self-control."
        scene ep5_sc21_mbr_13
        off "I touch her as gently as possible."
        off "Her skin is the softest thing that I've ever had under my fingers."
        off "Her bosom is heavy and full."
        off "I do my best to restrain myself but I can't help but press and massage it."
        off "I want to kiss these nipples."
        off "I want to suck on them."
        scene ep5_sc21_mbr_14
        off "I bend over and lick them."
        off "I intended to be as gentle and considerate as possible, but I'm actually sucking on it as if my life depends on it."
        scene ep5_sc21_mbr_15
        off "She moans loudly enough to bring me back to reality."
        off "My head is spinning."
        off "My breathing is loud and completely out of control."
        off "She grabs my shirt and clumsily snatches it from me."
        off "I lift her from the bed to relocate us further from the edge."
        scene ep5_sc21_mbr_16
        off "I install [sf_name] on her back and lean over her."
        off "She opens her legs to welcome me."
        off "I kiss her lips before going down on her."
        off "I want to lick her body."
        off "I imagine myself covering her with my saliva."
        off "To my utter disappointment, my tongue quickly runs dry."
        off "I stop at her breasts to play with them some more."
        off "I can't get enough of them."
        off "I can't get enough of her."
        off "I can feel her pussy below my chest."
        off "I know it's there."
        off "I know she's wet and burning hot."
        off "I feel like it's calling me."
        off "I stand between her legs and look at her eyes."
        scene ep5_sc21_mbr_17
        off "My hands slowly crawl on her belly, heading for her hips."
        off "She knows what I'm going to do."
        off "She gathers her thighs together."
        scene ep5_sc21_mbr_18
        off "Our eyes are locked on each other while I get rid of her underwear."
        off "I take my time removing her panties."
        scene ep5_sc21_mbr_19
        off "She hides her face with her arms and slowly opens her legs again."
        off "She's beautiful."
        off "I want to tell her that but I'm completely lost in the moment."
        off "No sound comes out of my throat."
        off "And her pussy is there yelling at me that she wants my attention."
        off "She looks so tiny."
        off "I find a very uncomfortable position to settle in."
        scene ep5_sc21_mbr_20
        off "The only thing important to me right now is to bring my tongue to her."
        off "I have no idea what I'm doing, but I'm running with it."
        off "She starts moaning as soon as I touch her."
        off "She smells and tastes wonderful."
        off "Salty, and sweet at the same time."
        scene ep5_sc21_mbr_21
        off "I have no doubt that I could eat her out for days."
        off "She's juicy."
        off "Her fluids quickly cover the lower parts of my face."
        off "From my nose to my chin."
        off "I grab her left breast and try to caress it gently."
        off "She immediately catches my hand and presses it against her as hard as she can."
        off "Confined in my pants, my dick is about to explode."
        off "I'm so hard that it hurts."
        off "I try to get rid of my remaining clothes without success."
        scene ep5_sc21_mbr_22
        off "She watches me as I stand back and lose my shorts."
        off "No."
        off "She doesn't look at me."
        off "She looks at my cock."
        off "The thing is literally on fire and covered in precum."
        off "I get closer and lean in for a kiss."
        scene ep5_sc21_mbr_23
        off "She greets me between her legs and surprises me when she grabs my penis."
        off "She strokes it."
        off "Gently."
        off "She ogles it with greed and desire."
        scene ep5_sc21_mbr_24
        off "She wants it as much as I do."
        off "I don't doubt it."
        off "I don't know why I ask, but I still do."
        mc "Are you sure ?"
        off "She nods."
        sf "Yes."
        scene ep5_sc21_mbr_25
        off "She slowly guides my glans between her lips."
        off "I barely touch her that her already loud breathing gets even more intense."
        off "We look at each other eyes for one last confirmation."
        scene ep5_sc21_mbr_26
        off "And I penetrate her."
        off "She arches and moans."
        off "She yells while gripping on my shoulders."
        sf "Haaaaaaaannnnn!"
        sf "Slower! Please! Please!"
        off "I slid inside her without feeling any resistance."
        off "Her reaction worries me."
        off "I feel like trash."
        mc "Do you want me to stop?"
        mc "I'm sorry [sf_name]."
        mc "I didn't want to hurt you."
        mc "I'm so sorry..."
        scene ep5_sc21_mbr_27
        sf "Oh no! No no no!"
        sf "Just, please... You're... big..."
        sf "Oh my god, you're so big..."
        sf "I never thought it would be..."
        sf "I...I have to get used to it..."
        off "I'm paralyzed."
        off "I'm halfway into her."
        off "I'm not moving an inch."
        off "I'm so excited that I feel dizzy."
        off "My whole body tingles, I'm not sure I'm even feeling anything."
        off "If anything, I'm going to pass out on top of her."
        off "She tries to kiss me but my lips are too far from her."
        off "She let outs a nervous laugh."
        sf "You're a bit tense. You should relax..."
        off "Her voice calms me down a bit."
        sf "It's just the first time."
        sf "I'm sure that we'll have several others after that..."
        scene ep5_sc21_mbr_28
        off "She draws me in and makes me lie on top of her."
        off "I'm a bit afraid to crush her under my weight but she doesn't seem to mind it."
        sf "I want to feel you against me."
        scene ep5_sc21_mbr_29
        off "I start to move my hips as slowly as I can while our lips join."
        off "She moans in my mouth and gasps in surprise."
        off "I try not to go further inside than I already have."
        off "She needs time."
        scene ep5_sc21_mbr_30
        off "I begin to get some real sensations."
        off "And it feels insanely good."
        off "I've beat my beat a fairly high number of times but it never felt that good."
        off "This is so different."
        off "It can't even compare."
        scene ep5_sc21_mbr_29
        off "She's warm and moist. Welcoming."
        off "And she's so tight."
        off "It feels like her insides are squeezing my dick, alternatively sucking me in and pushing me out."
        off "After a time, I allow myself to move faster."
        scene ep5_sc21_mbr_30
        off "She moans almost continuously when we're not kissing."
        off "I feel clumsy and ridiculous but actually don't give a damn."
        off "I feel like we're one."
        off "I like it."
        mc "Do you think I can... Go deeper ?"
        scene ep5_sc21_mbr_31
        off "She frowns in surprise and she raises her head to look at our joined crotches and let out a little panicked laugh."
        sf "Oh my God..."
        off "She looks as afraid as desirous."
        sf "Yes. Yes, but slowly, please."
        sf "Sloooowlyyyy! Mhmmm!"
        mc "Tell me if I go too far."
        off "I slide further in with ease."
        off "I try to progress as slowly as possible."
        sf "Haaaaaaaan! Haaaaan! Haaaaaaan!"
        off "She doesn't ask for me to slow down and even less to stop."
        off "So I keep going until I'm fully in."
        off "I fill her to the brim."
        scene ep5_sc21_mbr_32
        off "She clutches her legs around my hips and grips on my sides with her hands."
        sf "Slower! Please! Oh my god."
        sf "I never have been so... full..."
        sf "You're so deep..."
        off "She seems to feel more pain than pleasure."
        mc "Are you alright? We can stop ..."
        sf "Oh no please don't stop!"
        sf "Just, move slowly."
        sf "Yes, just like that! Oh my... Haaaaaan!"
        off "I try to go with her flow but actually simply move as slow as I can."
        off "I give her a few strokes like that."
        off "She moans louder when I go in, softer when I go out."
        off "I try to give her my full length every time."
        off "We've entered some kind of full body to body mode that feels just right."
        off "She presses me against her as hard as she can and I burrow my face in her shoulder."
        off "I barely manage to kiss her neck."
        off "I'm out of breath."
        off "She asks me to go faster after a couple of minutes."
        off "I'm about to come."
        off "I try to contain myself, and I feel lame as it seems way too early for me to unload."
        off "I think about slowing down a bit."
        off "Maybe I should pull out a moment, just to avoid letting it go too soon."
        off "But she asks me to go faster, deeper."
        off "Is she about to come too?"
        off "Perhaps I can push it further..."
        off "... Just a little bit deeper..."
        off "... A few more seconds."
        scene ep5_sc21_mbr_33
        mc "Haaaan! Haaan !"
        mc "HAAAAAAAN! HAAAAAAAARRRRRRWWWWNNNN!"
        off "I suddenly explode inside her."
        off "My whole body shakes as I unload."
        off "I can feel it, from my neck to my knees."
        off "I come inside her."
        off "I give her everything."
        off "I never felt anything like that."
        off "I literately liquefy myself on top of her."
        off "She holds on to me with both her legs and her arms."
        off "I'm balls deep inside her and I came so much that I can feel my dick bathing in my semen."
        off "It's kind of disgusting and I'm probably imagining that."
        off "But it also feels weirdly fulfilling."
        off "I like it."
        off "We stay like that for a moment as my dick is going limp inside her."
        scene ep5_sc21_mbr_34
        off "She gently smiles."
        off "We exchange a few kisses but the truth is we're both exhausted."
        off "It feels as good as humiliating."
        off "I'm not even close to having lasted long enough."
        off "I should apologize."
        off "But I don't even know where to start."
        off "How to formulate it?"
        scene ep5_sc21_mbr_35
        off "She whispers in my ear."
        sf "I felt you coming inside me."
        off "She sounds very embarrassed."
        sf "I liked it but..."
        sf "Perhaps this is a good time to tell you that I'm not on the pill..."
        off "Holy fucking shit."
        off "Could I fuck up more than that?"
        scene ep5_sc21_mbr_36
        mc "Oh, [sf_name], I'm so sorry!"
        mc "I didn't even think about it."
        mc "I'm so dumb!"
        mc "I'm a goddam moron..."
        off "She puts a finger on my lips and smiles."
        sf "It's ok, I'm pretty sure it's a safe day."
        sf "You don't have to worry, ok?"
        sf "And besides, I should have told you..."
        sf "To be honest, once we started..."
        sf "My mind has kind of gone blank and... I didn't even think about it."
        sf "Also... I think I'm kind of happy that it turned out that way..."
        sf "Don't get me wrong, doing it without any contraception is foolish but..."
        sf "I mean... without a condom..."
        sf "It felt... Fitting, for our first time."
        off "Fitting... Yeah, I kind of understand that."
        mc "I'm still sorry... I'll get some condoms for the next time."
        scene ep5_sc21_mbr_37
        sf "You won't need it."
        mc "I won't need it? But..."
        sf "I called my gynaecologist this afternoon."
        sf "I have an appointment tomorrow morning."
        sf "So... I should be on the pill starting tomorrow..."
        mc "Oh... Ok... That's... Good news."
        off "She looks ashamed."
        sf "[mc_name]... I think I need to go to the bathroom."
        sf "I feel like I'm dripping..."
        off "Oh my God."
        mc "Yeah, sure! Of course!"
        scene ep5_sc21_mbr_38
        off "I move away from her and she quickly heads to the bathroom, holding her pussy and the semen I filled her with."
        off "I can't believe it."
        off "We did it."
        off "I made love with [sf_name]."
        off "I'm not a virgin anymore!"
        off "Holy shit! I'll have to tell Steve!"
        off "He won't believe me!"
        off "And I came inside her."
        off "But fuck!"
        off "I didn't last more than what?"
        off "5 minutes perhaps? Maybe less?"
        off "I fucked up big time."

        if sis_sub_path == True:
            scene ep5_sc21_mbr_39
            off "Well, that's longer than what I lasted when [sis_name] touched me..."
            off "So I guess that's some kind of progress..."
            off "[sis_name]... Crap, what am I going to do?"
            off "I'll go see her later."
            off "I'm sure she heard us."
            off "[sf_name] and I haven't been very discreet."
            if sis_sub_love_path == True:
                off "We'll have to talk about it."
                off "That's not the kind of thing that can be left unspoken."
            off "Oh, come on [mc_name]."
            off "What the hell are you doing?"
            off "You just had sex with [sf_name] and you're thinking about [sis_name] already?"
            off "You're a total disgrace."

        scene ep5_sc21_mbr_40
        off "[sf_name] comes back from the bathroom with a smile on her face."
        off "She happily runs towards me on her tiptoes."
        off "That's one of the things that made me completely fall for her."
        off "That pure and innocent happiness."
        off "She's beautiful in and out."
        off "She laughs as she pushes me on the bed."
        scene ep5_sc21_mbr_41
        off "She wraps my arm around her."
        off "She captures my hand and playfully places it on her breast, pressing it against her."
        off "I feel like I'm in heaven."
        sf "Any regrets?"
        mc "Regrets? Why would I regret anything?"
        mc "I just made love with the person I love, who happens to be the most beautiful girl I've ever met."
        sf "Oh, I'm so sorry for you, Honey, you must not have met many of them then!"
        mc "I'll have you know that I've met plenty."
        mc "And none can compare to you."
        off "She giggles and huddles against me."
        scene ep5_sc21_mbr_42
        sf "You've already bedded me, Honey, you can relax on the seduction attempts."
        mc "I'm not even trying, Sunshine."
        sf "Sunshine?"
        mc "You don't like it?"
        mc "You called me Honey so I thought..."
        sf "You don't like Honey?"

        menu:
            "You can call me however you want.":
                $ ep5sfloveperv = True
                mc "Your sweet voice will make it sound great."
                off "She bursts out laughing."
                sf "Alright then, how about Perv?"
                mc "You know what?"
                mc "I like Honey."
                mc "Let's go with Honey."
            "It sounds a bit sweet for a guy.":

                $ ep5sflovecaptain = True
                mc "How about ... O captain, my captain ?"
                off "She bursts out laughing."
                sf "That's something [sis_name] could have come up with."
                mc "I don't know why, but I'm not really surprised."
                mc "You know what?"
                mc "I like Honey."
                mc "Let's go with Honey."

        scene ep5_sc21_mbr_42_alt
        sf "Sunshine is great too."
        sf "I like it."
        mc "That was an obvious choice."
        sf "Obvious?"
        mc "Just a moment ago, as you walked towards me..."
        mc "I thought that you are so beautiful and bright that your light drives out the darkness and the sadness of the world..."
        mc "Well, that's stupid."
        mc "I'm no poet."
        sf "I like it."
        sf "Sunshine will be perfect."
        off "She marks a pause before timidly resuming."
        scene ep5_sc21_mbr_43
        sf "[mc_name], will you stay with me tonight?"

        if sis_sub_path == True:

            off "Here comes the dilemma."
            off "To stay with her, or to go spend some time with [sis_name]..."
            off "Do I even have a choice?"
            mc "I want to... but you know..."
            mc "I'm afraid I'll have a hard time controlling myself if I stay with you..."
            mc "You're very... Tempting... And I don't want to hurt you..."
            sf "Hurt me?"
            mc "Yeah... You know... I've read that... The first time could be... Painful..."
            mc "Some girls can have a hard time... For several days after that..."
            sf "Oh Honey, that's very considerate but..."
            sf "It wasn't the first time I..."
            off "I wasn't her first?"
            off "Is that what she said?"
            sf "I mean, it was but..."
            scene ep5_sc21_mbr_44
            off "She suddenly raises and seems a bit afraid."
            sf "Honey, please, don't be upset."
            mc "Upset? Why would I be?"
            mc "I just don't understand..."
            sf "It was my first time with a boy but..."
            off "She looks at me ashamed and terrified."
            sf "I did it with [sis_name]."
            off "I hear her words but their significance takes a few seconds to hit me."
            mc "You're telling me that you had sex with [sis_name]?"
            off "She nods."
            off "She seems about to cry."
            off "Does she think that I'm going to hate her for that?"
            mc "Ok, hold on there..."
            mc "You know, the virgin thing, the first time... That wasn't important to me..."
            mc "It's... It's no big deal ok?"
            mc "That doesn't change anything."
            sf "Really?"
            mc "Really. It's ok."
            scene ep5_sc21_mbr_45
            off "I pull her to me and hold her tight."
            off "I kiss her forehead and can sense her relaxing against me."
            mc "I have questions, however..."
            sf "You can ask whatever you want."
            sf "I should have told you sooner anyway..."
            mc "So... You're lovers?"
            sf "No! No! It's not like that..."
            sf "It's... We just tried it..."
            sf "I mean... We tried kissing..."
            sf "Then we tried other things..."
            sf "And we just kept doing it when we were feeling... Alone..."
            mc "Ok, so... More like sex friends or something like that..."
            sf "I don't know how I should define it."
            sf "We're not lovers, but we're more than friends."
            mc "Sounds like an amazing friendship to me."
            sf "You don't think it's weird?"
            mc "Well... Friends usually don't bed each other..."
            mc "But I guess you two have a special relationship."
            mc "Actually, I think it's great."
            mc "And... So... Is this still going on ?"
            off "She whispers."
            sf "... I guess we'll stop."
            off "So it is still going on."
            off "That's... Interesting."





            menu:
                mod "Unknown Conequences."
                "Why? [gr]\[SFLoveWhy\]":
                    $ ep5sflovewhy = True
                    sf "Why what?"
                    mc "Why would you stop?"
                    scene ep5_sc21_mbr_46
                    off "She raises her head and looks at me completely baffled."
                    sf "You want me to cheat on you, with [sis_name]?"
                    mc "Oh... that's... It's weird, right?"
                    mc "I didn't even think of it as cheating."
                    mc "If we were talking about another guy I would get crazy mad in the second but [sis_name]..."
                    sf "You wouldn't have any problem with me having sex with her?"
                    mc "I don't think I would."
                    mc "I know it's weird. I think that the two of you have taken care of each other for some time now..."
                    mc "If I take you from her... who would take care of her?"
                    mc "Do you think she will find someone else?"
                    mc "I don't know why but... I have a feeling that it wouldn't end well for her."
                    off "She looks at me in silence for several seconds."
                    off "I'm sure she's considering it."
                    scene ep5_sc21_mbr_47
                    sf "Are you sure about this?"
                    mc "The more I think about it the more it seems weird and right at the same time."
                    mc "But, I'm not asking you to do that ok?"
                    mc "I'm just saying that if it's important for you, and for her... you shouldn't stop because of me."
                    mc "I just don't want to destroy what you both have."
                    mc "I want both of you to be happy."
                    off "She seems completely lost."
                    off "I feel bad."



                    off "I feel like trash for confusing her so much."
                    scene ep5_sc21_mbr_49
                    sf "I don't really know how to react to that."
                    sf "But... I guess some of your arguments sound right..."
                    sf "I'll need to think about it..."
                "And so... [gr]\[SFLoveSo\]":

                    $ ep5sfloveso = True
                    mc "Who's better at it, her or me?"
                    scene ep5_sc21_mbr_46_bis
                    off "She raises her head and looks at me, positively terrified."
                    sf "Oh please Honey, don't ask me that."
                    sf "Whatever you want, but not that..."
                    off "Holy fucking crap."
                    off "Her reaction says it all."
                    mc "Wait, does that mean that she is better than me ?"
                    sf "[mc_name], please..."
                    off "She seems about to burst in tears."
                    off "I tighten my arms around her."
                    mc "Hey, hey, hey. What are you so afraid of?"
                    mc "Do you think I'm going to get upset or anything?"
                    mc "It's a bit humiliating, but I have no reason to get angry."
                    mc "I just think that I should know these things if I want to get better at it."
                    mc "For you."
                    off "She looks at me for a few seconds."
                    off "The fear disappears and she seems tired and embarrassed."
                    scene ep5_sc21_mbr_48
                    sf "She has an obvious advantage over you. She's a girl..."
                    sf "So... She kind of knows how a vagina works..."
                    mc "Yeah, but she doesn't have a dick so..."
                    sf "We have toys..."
                    mc "Oh... Ok..."
                    sf "But none is... As big as you are..."
                    mc "But it hurt you..."
                    sf "A bit, but it'll be better next time."
                    sf "I just need to get used to it..."
                    sf "Also... the real thing feels... Better..."
                    mc "Ok... but... Was it pleasurable at least a little?"
                    mc "When I was inside you... I thought you enjoyed it..."
                    scene ep5_sc21_mbr_49
                    sf "I did enjoy it! A lot!"
                    sf "It's not because I didn't have any... you know... that I didn't get any pleasure."
                    off "Of course, she didn't have any."
                    off "I'm a total failure, that's it."
                    off "I feel so ridiculous."
                    off "My childhood friend fucks my girlfriend better than I do."
                    mc "Ok well... I'm sorry about that... but I promise you I'll improve."
                    mc "Perhaps you could guide me next time?"
                    mc "Give me a couple of hints?"
                    mc "And I'll also need a lot of practice."
                    mc "Yeah, definitely a lot of practice."
                    off "She laughs."
                    sf "Maybe I can help you with that."
                    mc "I sure hope you will."


            mc "Just keep in mind one more thing."
            sf "Which is?"
            mc "That you're my Sunshine."
            sf "I like the sound of that."
            scene ep5_sc21_mbr_50
            off "She chuckles lightly and kisses my chest."
        else:

            mc "Because you thought I would leave after that?"
            sf "I just wanted to make sure you know that I want you to stay with me."
            mc "There's no way I leave you alone."
            sf "I like the sound of that."
            scene ep5_sc21_mbr_50
            off "She chuckles lightly and kisses my chest."

        mc "You know what? I just realized that we did it on my parents' bed."
        sf "Oh... does that disturb you ?"
        mc "No, it's just that... I feel like they could come in any second now and scold me for that..."
        sf "I wonder what they would say if they found us like that..."
        mc "Well, first, they would probably ask us to get decent and then throw us out of their room."
        sf "Decency is so overrated."
        mc "I agree, let's live naked from now on."

        off "We keep on babbling for some time, cuddling and kissing."
        off "Her embrace is soft and comfortable."
        if sis_sub_path == True:
            off "She falls asleep pretty quickly and I enjoy the bit of time I spend looking at her sleeping in my arms."
        else:
            off "She falls asleep first and I enjoy the bit of time I spend looking at her sleeping in my arms."

        $ renpy.end_replay()
        return
    else:

        scene ep5_sc21_mbr_06
        off "Our lips met in a warm and moist embrace."
        off "The kiss is as delicious as ever but I can't fully focus on it."

        if (ep4sflovetalked == True and ep5sftruelove == False) or (ep5sisnighttalk == True):
            off "We have many things to discuss before we can go on."
            off "I feel like I'm going to hurt her and break her dreams or something like that."
            off "I'm not comfortable with that idea."
        else:
            off "I can feel the pressure rising."
            off "I have to make her come tonight."
            off "I can't disappoint her again."
            off "Come on, [mc_name]."
            off "It can't be so difficult to give her an orgasm."
            if sis_sub_path == True:
                off "You had no problem making [sis_name] shake like crazy."
                off "You should be able to do the same with her."

            off "I'm going to lick your pussy real good, [sf_name]."
            off "I swear."

        sf "Is everything ok, [mc_name]?"
        sf "You seem a bit tense..."
        scene ep5_sc21_mbr_05
        mc "Yeah, well... I guess we all are..."

        if (ep4sflovetalked == True and ep5sftruelove == False) or (ep5sisnighttalk == True):
            off "It's now or never, [mc_name]."
            off "If you have to say something, do it now."
            menu:
                "Say something.":
                    mc "[sf_name], I think we should talk..."
                    off "She looks at me, surprised."
                    scene ep5_sc21_mbr_52
                    off "I can see her expression changing towards fear and sadness."
                    sf "Is it... something I did?"
                    off "She thinks that I want to dump her."
                    off "[mc_name], you're a moron."
                    off "Learn to choose your words, dammit."
                    mc "Oh [sf_name], no!"
                    mc "Please, it's not what you think."
                    mc "I'm not breaking up with you."
                    off "I'm not breaking up but it may be even worse..."
                    mc "Please, just..."
                    mc "Listen to what I have to say before making any conclusions, ok ?"
                    sf "You don't want to break up with me?"
                    mc "No [sf_name], I don't want to break up with you."
                    off "She doesn't really seem reassured."
                    off "She is expecting the end of our relationship."
                    mc "Let's sit. Please."
                    scene ep5_sc21_mbr_53
                    off "We settle next to each other, on the edge of the bed."
                    off "I grab her hand and slowly caress her."
                    mc "This isn't easy to say but I don't think that it's necessarily bad."
                    mc "It's... How can I say it...?"

                    if ep4sflovetalked == True and ep5sftruelove == False:
                        mc "When you confessed to me this morning..."
                        mc "It surprised me, and I didn't respond."
                        mc "I wish I could tell you that I love you too, but I can't."
                        mc "I like you a lot and I really care about you, but I just don't know if I love you."
                        mc "You're very important to me and I felt that leaving you hanging like that wasn't right."
                        mc "I'm not saying that I don't love you, nor that I won't ever love you."
                        mc "I can't put a name of what I'm feeling."
                        mc "You're the first girl to makes me feel that way and I'm very confused."
                        mc "Maybe, in a week or a month from now, things will be different, but for now..."
                        mc "I felt that not telling you that was like abusing your feelings..."
                    else:
                        mc "I talked with [sis_name] tonight."
                        mc "She wanted to make sure that I was taking our relationship seriously enough."
                        mc "She's very worried because..."
                        mc "She thinks that you're way more engaged than I am and she's afraid you could get hurt."
                        mc "And... well, to be honest, I'm a bit concerned that I'll never really meet your expectations."
                        mc "[sis_name] told me that you were talking about love and making projects."
                        mc "Honestly, I like you and I care about you a lot, but love is such a big word..."
                        mc "Maybe, in a week or a month from now, I will think differently, but for now..."
                        mc "I felt that not telling you that would be like abusing your feelings..."

                    scene ep5_sc21_mbr_54
                    off "She frowns, sad and confused."

                    sf "I don't understand... Why are we even having this conversation?"
                    sf "I already know I'm getting a bit carried away."
                    sf "But I have the right to dream, haven't I?"
                    off "She sounds hurt."
                    mc "Of course..."
                    scene ep5_sc21_mbr_55
                    sf "What do you want me to do?"
                    sf "To expect less?"
                    sf "I don't expect anything!"
                    sf "I just wanted to be with you."
                    sf "Is that too much?"
                    mc "No, no, it's..."
                    sf "Why is that even bothering you?"
                    sf "Is that so important ?"
                    mc "Because I feel guilty."
                    mc "I thought that being honest was important and I didn't want you to do anything you may regret later."
                    off "I feel miserable."
                    scene ep5_sc21_mbr_56
                    off "She stands up and turns away from me."
                    off "She sighs."
                    sf "I'm very tired."
                    sf "I think I'll go to bed."
                    off "She's throwing me out."
                    off "The discussion is over."
                    off "She wants to be alone."
                    mc "[sf_name], I..."
                    sf "Please, [mc_name]. We'll talk tomorrow."
                    off "I'm a dumbass."
                    off "Why did I even talk about that?"
                    off "I only succeeded in hurting her. "
                    mc "Good night, [sf_name]."
                    sf "Good night, [mc_name]."
                    scene ep5_sc21_c_02
                    off "Why do I keep fucking up things?"
                    off "I had something nice with [sf_name] and I had to destroy it with that bullshit."
                    off "I definitely ruined everything."
                    off "I feel like shit."
                    off "Calm down, [mc_name]."
                    off "She just needs to think about it."
                    off "And so do you."
                    off "No doubt you chose your word poorly."
                    off "You basically told her that you don't love her."
                    off "Yet! I don't love her YET!"
                    off "Yeah well, that YET doesn't matter."
                    off "She was already aware that your relationship was... Asymmetrical."
                    off "And she surely didn't need to hear you say it."
                    off "You'd better apologize tomorrow, for being a heartless moron."
                    off "But what should I have done?"
                    off "Say nothing? Lie to her? "
                    off "Why is this so complicated?"
                    $ ep5sflovemistake = True

                    return
                "I can't. [sfLovePath]":

                    off "It would just hurt her."
                    off "And that's the last thing I want."


        scene ep5_sc21_mbr_57
        sf "I have an idea. You're going to like it."
        mc "I'm all ears..."
        $ ep5sflovebj = True


        if ep4sflovelicked == True:
            sf "Last night you did go down on me... and..."
            sf "I thought that I could return the favour..."
            mc "Are you serious? You want to..."
            off "She nods maliciously."
        else:
            sf "There's something I want to try..."
            sf "With your penis."
            off "That word makes my whole spine shivers."
            off "She wants my dick."
            off "Wait. Did I even hear that right?"
            mc "I... ok ... what do you have in mind?"
            sf "I don't know..."
            sf "I thought that maybe I could take it in my mouth..."
            off "Holy mother of god."
            off "She says that with a sweet and innocent tone."
            off "My heart is about to explode."



        off "Still in my pants, my tool is already hardening."
        mc "Well... it's... Yours to play with... I mean... If you want it..."
        sf "I want it."
        scene ep5_sc21_mbr_58
        off "She drags me to the bed."
        sf "Sit there and relax."
        mc "Ok..."
        off "I'm trembling in expectation."
        off "She unbuttons my shorts and lowers them with disconcerting ease."
        off "She playfully throws my clothes over her shoulders."
        off "She observes my cock for a few seconds."
        off "It grows under her gaze."
        off "It's like I could feel her caressing me with her eyes."
        off "It arouses me."
        off "She doesn't seem afraid or shy in any way."
        off "She looks curious and interested."
        sf "It's my first time doing something like this so..."
        sf "Please, tell me if I do anything wrong..."
        sf "I don't want to hurt you."
        if sis_sub_path == True:
            mc "I'm sure you'll do great..."
        else:
            mc "To be honest I don't have much experience either..."



        scene ep5_sc21_mbr_59
        off "She grabs my dick and slowly gives it a couple of strokes."
        off "It doesn't take more than that to make me fully hard."
        sf "You're... Big, right?"
        off "Is she talking about the size of my penis?"
        mc "I'm pretty sure I'm average..."
        sf "It really looks big to me... like porn big."
        mc "If you say so... I'll take that as a compliment."
        off "She handles me very gently."
        off "Her fingers softly grip on my shaft with just the right amount of pressure."
        sf "That's not necessarily a compliment."
        sf "Some girls may be afraid of taking something this big."
        mc "Really?"
        mc "I honestly thought that the bigger the better."
        sf "It's my first time seeing a real one so..."
        sf "I may not be the best person to talk about it."
        scene ep5_sc21_mbr_60
        off "She brings my glans to her nose and shyly smells it."
        mc "I guess I'm not in a better position."
        sf "I thought it would smell more than that."
        mc "I take showers you know?"
        sf "It doesn't smell more than a vagina."
        off "The comparison is surprising but... It kind of makes sense."
        mc "Ok..."
        scene ep5_sc21_mbr_61
        off "She gives it a little lick."
        off "She tastes it."
        off "I await her comment on that but she decides otherwise."
        off "She brings her tongue back in the game and looks me in the eyes while taking care of me."
        off "I briefly think of delivering some clever words of encouragement but I only manage to utter a pathetic groan."
        mc "Oh, shit! [sf_name].... That feels very good..."
        scene ep5_sc21_mbr_62
        off "She smiles and immediately takes the thing in her mouth."
        mc "Oh my god !"
        off "She sucks on my glans."
        off "I can feel her tongue rolling around it."
        off "She quickly tries to claim more of it but can't handle most of my shaft."
        off "She let it go a few seconds, to catch her breath."
        sf "I'm sorry, I can't go deeper than that..."
        mc "It's perfect [sf_name], don't worry."
        scene ep5_sc21_mbr_63
        off "She smiles and goes back at it."
        off "She grows more aggressive and energetic."
        off "Using both her hands and her mouth, she quickly brings me to the brink."
        mc "If you keep going like that... I'm going to come... very quickly..."
        off "She doesn't slow down a bit."
        mc "[sf_name]! Haaaan!"
        scene ep5_sc21_mbr_64
        off "I let it all go in her mouth."
        off "She doesn't even flinch."
        off "She swallows everything as it comes and not a single drop of semen slips through."
        mc "Haaan! Oh my Goood !"
        off "She keeps on sucking and stroking my shaft for a while after I unloaded."
        off "She makes sure that there's nothing left in my balls."
        scene ep5_sc21_mbr_65
        off "She finally lets go of my dick and smiles innocently."
        off "She looks as fresh as ever."
        sf "How was it?"
        sf "Did you like it?"
        mc "That was incredible... it was..."
        mc "I don't think there are any words to describe that."
        sf "Great!"
        scene ep5_sc21_mbr_66
        sf "Jane gave us a couple of bits of advice."
        sf "She said you would like that."
        off "Jane. Of course."
        off "I'm not really surprised."
        mc "I guess I'll have to thank her at some point."
        sf "She's an interesting girl."



        if sis_sub_path == True:
            mc "Really?"
            off "I'm curious to see what she taught [sis_name]..."
            sf "Yes. She may seem a bit crazy, but she seems very kind and friendly."
            mc "Ok... What did you talk about?"
            mc "Apart from... The art of..."
            sf "It's a secret!"
            mc "Oh come on!"
        else:


            mc "[sis_name] said something like that too."
            mc "I guess you'll refuse to tell me anything about your conversation?"
            sf "Girls' secret!"
            mc "Seriously, you girls are not fun."


        off "Her laugh is bright and playful."

        sf "I need to hit the bathroom."
        sf "So I guess this is goodnight."
        scene ep5_sc21_mbr_67
        off "She plants a little kiss on my cheek and parts away."
        mc "Ok..."
        off "I haven't even recovered from that blowjob that she's throwing me out."
        off "I'm a bit disappointed by this hasty conclusion."
        mc "Goodnight then..."
        off "She laughs again."
        off "I can't help but leer at her ass as she walks to the bathroom."
        off "It's magnificent."
        off "I can hear the shower running as I put my shorts back on."
        scene ep5_sc21_c_02
        off "I leave the room still wondering if I dreamt that or if it really happened."
        off "I don't know what the girls talked about in that room but that blowjob was a very nice consequence."
        off "I wonder how things would have turned out without Jane's phone call..."
        $ renpy.end_replay()

    return


label ep5sc22:
    scene black with dissolve
    with Pause(2)
    scene ep5_sc22_mcr_01 with dissolve

    off "I've been waiting for a text from [sf_name] for some time now, and it's not popping."
    off "What is going on?"
    off "Maybe she decided not to \"have fun\" tonight?"


    if (sis_sub_path == False and sis_love_path == False):
        $ solo_dom_path = True
        off "This afternoon, she was pretty clear about it, though."
        off "Could it be a test?"
        off "Maybe I was supposed to go meet her by myself?"
        off "How long have I waited?"
        off "Fuck me, if it's a test I've already failed it."
        off "Should I go see her?"
        off "She will rip my ass open."
        off "I can feel it."


        if (ep5totaldom == True):
            off "And I think I'm ok with it..."
            off "Let's be honest: I liked it."
            off "It's weird and humiliating, but I liked it."
            off "I liked the way she took control."
            off "I liked being played with."
            off "Fuck, what kind of pervert am I?"
            off "I want more."
            off "I can't deny it anymore."
        else:


            off "Yeah... But..."
            off "I'll soon be able to fuck her too."
            off "We have a contract."
            off "She rips my ass, I rip her ass."
            off "There's no way I stop now after all I've been through."
    else:

        off "Maybe she decided to let me off the hook... But after this afternoon... I have to talk to her."
        off "I can't let things be left unspoken."
        off "I have to know what she's going to do."
        off "Her reaction was very weird."
        off "She was very protective but... I think I felt sadness, and maybe even jealousy."
        off "Could it be that [sf_name] actually cares about me?"
        off "I'm perplexed."
        off "We need to talk about that."


    scene ep5_sc22_c_01
    off "There's no light under her door."
    off "There wasn't any yesterday either."
    off "Let's knock softly."

    sf "Come in."
    off "I take a deep breaths and enter the room."
    scene ep5_sc22_mbr_01
    off "It takes me a few seconds to see her, seated in that armchair in the corner."
    sf "Good evening, [mc_name]."
    mc "Good evening, [sf_name]..."
    off "She seems to appreciate this staging."
    off "It's just like yesterday."

    if solo_dom_path == True:
        sf "I'm horny, [mc_name]."
        sf "And you made me wait."
        sf "I don't like it when my boyfriend makes me wait."
        off "Horny?"
        off "Well, that's promising..."
        off "But I'd better find some clever excuses for my lateness."

        menu:
            "I apologize. [sfDomPath]" if ep5totaldom == True:
                $ ep5domapo = True
                scene ep5_sc22_mbr_02
                mc "I thought you would send me a message to request my presence."
                mc "So I waited for it."
                mc "Perhaps I missed it."
                mc "In all honesty, I was very eager to join you tonight."
                mc "But I was also afraid I would annoy you if I had come before being formally summoned."
                off "I barely believe it myself but... It's mostly true."
                $ ProcessStat(2, "sf_affection")
                $ ProcessStat(2, "sf_dominance")
                $ DumpNotStack()
                scene ep5_sc22_mbr_03
                sf "I'm sorry [mc_name]."
                sf "I should have messaged you."
                sf "We've lost some precious time but I hope you won't begrudge me that."
                off "She's apologizing to me?"
                off "Am I dreaming?"
                mc "You know I can't resent you in any way."
                mc "You're too dear to my heart."
                off "She chuckles."
                sf "Dear to your heart."
                sf "I like that."
                sf "Maybe you're dear to mine too."
                sf "Let's play to find out."

            "I didn't know you were waiting..." if ep5sorrydom == True:
                $ ep5domdeny = True
                scene ep5_sc22_mbr_02
                mc "If I had known otherwise I would have come sooner."
                off "The silence is too long for comfort."
                off "I can feel her gaze over me."
                off "She isn't pleased."
                scene ep5_sc22_mbr_04
                sf "Are you mocking me, [mc_name]?"
                sf "I think I made myself very clear this afternoon."
                sf "I'm disappointed."
                sf "After our last conversation, I thought that we had come to an understanding about our relationship."
                sf "But you still seem reluctant."
                off "Why?"
                off "Because I'm not particularly happy to get my ass violated again?"
                off "Because I don't like pain?"
                sf "Are you afraid of me, [mc_name]?"
                off "Afraid of your dildos, for sure."
                mc "I'm sorry, I may still have some reservations about... taking it in the ass again."
                sf "You don't have to worry about that."
                sf "I'll make sure you enjoy it."
                sf "I promise you will learn to like it."
                off "Yeah, sure."
                mc "If you say so..."
                off "She sighs."
            "I'm sorry.":

                scene ep5_sc22_mbr_02
                mc "I have no excuses."
                scene ep5_sc22_mbr_04
                sf "As you say. No excuses."
                sf "That calls for punishment."
                off "Shit."
                sf "Do you like being punished, [mc_name]?"
                sf "Maybe you like to suffer?"

                menu:
                    "A bit of pain can be nice. [gr]\[PainYes\]":
                        $ ep5painyes = True
                        mc "But I don't particularly enjoy suffering."
                        mc "And I don't enjoy being punished either."
                        off "She takes a few seconds to appreciate my reply."
                    "No. [gr]\[PainNo\]":
                        $ ep5painno = True
                        mc "I don't enjoy suffering nor being punished."
                        sf "Then why are you searching for it so actively?"
                        sf "Are you trying my patience, [mc_name]?"
                        mc "I'm sorry, I won't do it again."

                off "She sighs."

        sf "Look behind you, [mc_name]."
        sf "On the dressing table."
        sf "Do you see it?"
        off "I get closer to the piece of furniture and search for something unusual."
        scene ep5_sc22_mbr_05
        off "I see it immediately."
        off "The thing is hard to miss."
        off "Holy shit."
        off "She must have seen me shaking in fear because I can hear her giggling."
        sf "Take it in the light, [mc_name]."
        sf "I want you to look at it."
        sf "Appreciate its weight."
        scene ep5_sc22_mbr_06
        off "That thing is massive but lighter than I expected."
        off "It's made of some kind of rubber."
        off "It's neither really hard nor soft."
        off "I can feel some kind of veins on its surface."
        off "I guess it's supposed to mimic the real thing."
        sf "What do you think, [mc_name]?"
        mc "It's... big."
        sf "It's the biggest I own."
        sf "But it's not as impressive as your own instrument."
        off "It seems way bigger to me."
        off "Can I really take that thing in my ass?"
        sf "Bring it to me."
        off "Girls take it all the time."
        off "You can do it, [mc_name]."
        scene ep5_sc22_mbr_07
        sf "I like this one very much."
        sf "Let me show you why."
        sf "It's easy to understand."
        scene ep5_sc22_mbr_08
        sf "This side will go inside you."
        sf "It's probably not as soft as a real dick but It will work just fine."
        sf "This side will go inside me."
        sf "Once inserted in my vagina, I will wear it like a cock."
        sf "You can guess it, [mc_name]."
        sf "I'm going to pump inside you and we will both get some pleasure out of it."
        off "Holy shit."
        off "She's going to fuck me proper."
        off "Yesterday was just a joke."
        off "Cold sweat runs on my back."

        if ep5totaldom == True:
            off "The worst of it all is I still don't know if that's out of fear or expectation."


        sf "To correctly fit it in me, I need to be wet enough."

        if ep5totaldom == True and ep5domapo == True:


            sf "Will you help me, [mc_name]?"
            off "What? Did I hear that right?"
            mc "You want me to help you get wet?"
            off "My mouth has run dry at some point."
            off "Speaking is difficult."
            sf "Yes. Would you please remove my panties?"
            scene ep5_sc22_mbr_09
            off "She joins her thighs and raises her legs."
            off "She sounds embarrassed and shy."
            off "That's all it takes."
            off "I'm gone."
            off "She can do whatever she wants with me."
            off "I'm her thing."
            off "I kneel before her."
            sf "Thank you, [mc_name]."
            off "I try to be as gentle as possible."
            off "Her skin is so soft."
            off "I want to touch her more."
            scene ep5_sc22_mbr_10
            off "She puts her feet on my shoulders and slowly spreads her legs."
            sf "Look at me, [mc_name]."
            sf "Do you like what you see?"
            mc "Yes. I like it very much. You are... very... beautiful."
            sf "Thank you, [mc_name]."
            sf "I appreciate your kind words."
            sf "Do you think you could lick me down there?"
            off "Holy mother of god."
            mc "Yes. Yes, I can."
            sf "Then go on, [mc_name]. Please."
            scene ep5_sc22_mbr_11
            off "I bring my mouth to her."
            off "I completely botched it last night, I no longer have the right to make a mistake."
            off "I still have no idea what I'm doing."
            sf "You seem a bit tense, [mc_name]."
            sf "Don't worry. I'll guide you."
            off "Her tone is very gentle and caring."
            off "I almost want to cry."
            off "I don't know what's happening to me."
            sf "Huuum, there, yes, that's not bad."
            off "She grabs my head and forces it into her pussy."
            off "My tongue gently explores her vagina."
            off "This is so different than yesterday."
            sf "Yes, you're doing great."
            off "I suddenly realize that her words of encouragement are very valuable to me."
            off "They make me happy."
            off "And more than anything, I want to please her."
            sf "Haaann! Yes!"
            sf "Now, look, this little bump there."
            sf "Yes! Han! That's my clitoris."
            sf "I want you to take care of it."
            sf "Oh Yes! Just like that!"
            off "She's more than wet now."
            off "My mouth is drenched in her fluids."
            scene ep5_sc22_mbr_12
            sf "Look at me, [mc_name]. I want you to put a finger inside me."
            off "Holy fuck."
            sf "Only one for a starter."
            sf "Yes, like that."
            sf "Slowly, go in, and out. Yes!"
            sf "You're getting good at it."
            sf "Focus on the top."
            sf "Yes, yes! that's the spot! Haaan!"
            sf "I want a second finger, now! Now!"
            scene ep5_sc22_mbr_13
            sf "Yes! Haaaaan! Haaaaaaan! Haaaaaaaaaaaan!"
            off "She arches and lets out a very intense moan."
            off "Did I just give her an orgasm?"
            off "Holy crap."
            off "She gently pushes me away with her feet and gives me a very suggestive look."
            off "I must be dreaming."
            sf "Thank you, [mc_name]."
            sf "You've earned a nice reward."
            sf "I don't want to hurt you."
            sf "This is all about pleasure."
            sf "So I need this thing to be adequately lubricated."
            sf "Do you want to see what's the best way to do so?"
            off "I can't utter a word."
            off "My mouth and my entire throat have gone as dry as the desert."
            off "I frenetically nod a yes."
            off "I can guess her smiling in response."
            scene ep5_sc22_mbr_14
            off "She brings the toy to her pussy."
            off "She rubs it against her lips a couple of time before going for it."
            scene ep5_sc22_mbr_15
            off "Just the glans at first."
            off "She gently pushes it inside herself."
            off "Her loud breathing and her moans fill up the room."
            off "Then she goes deeper."
            scene ep5_sc22_mbr_16
            off "A few seconds later and she's playing with the full length of that thing."
            off "It seems so easy."
            sf "I want you to watch it very closely, [mc_name]."
            sf "Because tomorrow, it will be you, going inside of me like that."
            sf "I'm confident that you will do your best to please me."
            sf "You won't disappoint me, right?"
            sf "I'm sure you won't."
            scene ep5_sc22_mbr_17
            off "Her words reach me between her gasps of pleasure."
            off "I am mesmerized by her voice and the show she gives me."
            off "This thing slides gently inside her and makes her feel good."
            off "Will I be able to do the same? "
            sf "I think it's enough."
            off "She takes it out."
            sf "Lose your shorts, [mc_name]."
            sf "And get on the bed."
            sf "I want you on all fours."
            scene ep5_sc22_mbr_18
            off "I obey her command as she inserts the other side of the dildo in her vagina."
            scene ep5_sc22_mbr_19
            off "She really wears it like a cock."
            off "A cock I'm going to take in my ass."
            off "She climbs on the bed behind me."
            off "I can feel her hand on my buttocks."
            off "Her thumb gently probes my anus."
            off "I choose to let go of fear."
            off "Let's trust her."
            off "I ended up enjoying it last night."
            off "I'll probably enjoy it tonight too."
            scene ep5_sc22_mbr_20
            sf "You seem more relaxed than last time."
            sf "It's better this way."
            sf "You're going to enjoy this."
            off "I can feel the toy pressing against me."
            off "She gives a couple of very tender pushes and it pops in like it's nothing."
            off "It's way bigger than yesterday and yet it enters me with ease..."
            off "It takes my breath away."
            off "There is close to no pain."
            off "It just fills me up and stretches my insides."
            sf "Do you see?"
            sf "When it's properly lubricated, it's way more comfortable, isn't it ?"
            mc "Yes! Yes!"
            scene ep5_sc22_mbr_21
            off "She slowly slides in."
            off "That thing is so big... How deep can it go?"
            off "Holy shit."
            off "It's entirely different from yesterday."
            off "I sense more than just an object penetrating me."
            off "I can feel her intent, I can feel the care she puts in fucking me slowly so that it doesn't hurt me."
            off "I can feel her own pleasure."
            scene ep5_sc22_mbr_22
            mc "Haaaaan!"
            off "I'm moaning."
            off "I can't control it."
            off "I'm not her victim anymore."
            off "This feels like we're actually a couple."
            off "A weird one, but a real one."
            off "She called me her boyfriend, right?"
            scene ep5_sc22_mbr_23
            mc "Haaaaaaaaoooow!"
            off "She stumbles on my buttocks."
            scene ep5_sc22_mbr_24
            off "She can't go deeper."
            off "I took it all in."
            off "Oh my god, I took it all in."
            off "I can sense it pushing my guts inside me."
            off "It feels so weird... and good at the same time."
            off "But I don't give a damn anymore."
            off "Fuck the shame."
            sf "Do you like it, [mc_name] ?"
            mc "Yes! Fuck Yes!"
            sf "Oh! Do you think I can move a bit?"
            mc "Yes, please! You can move all you want!"
            scene ep5_sc22_mbr_25
            off "She tightens her grasp on my hips and starts pumping."
            off "She has barely shagged me for a few seconds that I feel a massive wave of pleasure surging from my bottom."
            off "It comes from the inside, between my crotch and my rectum."
            off "It's like an explosion running up through my spine."
            off "My dick tingles."
            mc "Haaaaaawwwwwwnn!"
            off "I almost came."
            mc "Holy mother of god!"
            sf "You seem to enjoy it very much, [mc_name]."
            sf "That makes me happy."
            off "Her breathing is as loud as mine."
            off "She softly groans with every move."
            off "She's not doing that to me."
            off "We're doing it together."
            off "I'm having sex with her."
            off "Just not the usual way..."
            off "The rhythm of her blows intensifies."
            off "She fucks me faster."
            scene ep5_sc22_mbr_26
            sf "A bit rougher maybe?"
            sf "Do you like that [mc_name]?"
            mc "I like it! Oh, shiiit!"
            off "It explodes again."
            off "And it's brutal."
            off "The same sensation runs through my spine, but it's stronger."
            off "My lower limbs start contracting uncontrollably."
            off "My whole body is soon shaking."
            scene ep5_sc22_mbr_27
            off "I can't keep my position anymore and I crash on the mattress."
            off "I came on the sheets and I lay on it."
            sf "Oh, dear, you really seem to have a good time."
            off "She leans on me and whispers."
            scene ep5_sc22_mbr_28
            sf "But I'm not done yet."
            off "She penetrates me and fills me up again."
            off "She fucks me silly."
            scene ep5_sc22_mbr_29
            off "Each time she pushes it in, I can feel the ripples of the impact going through my ass."
            off "I feel like coming again but my balls are already drained."
            off "It's like trying to ejaculate dust."
            off "She goes on for a couple more minutes before she crashes on my back moaning."
            scene ep5_sc22_mbr_28
            sf "Haaan, [mc_name]... That was great... Don't you think?"
            mc "Yes... yes it was great."
            off "She softly kisses my shoulders."
            sf "I'm so glad."
            sf "I feel like we finally understand each other."
            sf "Can you feel it, [mc_name]?"
            off "Can I feel it? What do I feel exactly?"

            menu:
                "I love you, [sf_name]. [sfLovePath]" if sf_affection > 34:
                    $ ep5domlove = True
                    off "Did I say that loud?"
                    off "Where the hell did that come from?"
                    off "I feel like I'm going to cry."
                    off "What the hell is going on with me?"
                    scene ep5_sc22_mbr_30
                    off "She tenses up and raises from my back."
                    sf "What did you just say?"
                    $ ProcessStat(3, "sf_affection")
                    $ ProcessStat(2, "sf_dominance")
                    $ DumpNotStack()
                    off "Am I sure of this?"
                    off "It feels so real..."
                    mc "I said I love you, [sf_name]."
                    off "She pulls out and stands up."
                    sf "Please [mc_name], don't mess around with those words."
                    off "She sounds very serious."
                    off "The mood has shifted in a second."
                    scene ep5_sc22_mbr_31
                    off "I look at her as she removes the toy from her pussy."
                    mc "I'm sorry... I'm not kidding... Did I say something wrong?"
                    off "She switches the lights on."
                    sf "Enough. I don't want to hear it."
                    sf "I'm going to the bathroom."
                    sf "I want you gone when I come back."
                    sf "Goodnight [mc_name]."
                    scene ep5_sc22_mbr_32
                    off "She heads for the door without waiting for a reply."
                    off "She seemed annoyed by my words."
                    off "I'm completely lost."
                    off "I thought the two of us had a moment just now... Was I wrong?"
                    off "Obviously, she didn't want to hear that."
                "I think I do... [sfDomPath]":





                    $ ep5domsurrender = True
                    sf "Everything goes better when you do as I say, right?"
                    $ ProcessStat(5, "sf_dominance")
                    $ DumpNotStack()
                    off "I can't deny that tonight was more interesting and satisfying than our previous... Sessions."
                    mc "Yeah..."
                    sf "I promise you, [mc_name]."
                    sf "If you behave well, you won't be disappointed."
                    off "She pulls out and stands up."
                    sf "We'll do that again soon, but first... We had a deal, [mc_name], and you fulfilled your part."
                    scene ep5_sc22_mbr_31
                    off "I look at her as she removes the toy from her pussy."
                    off "We both came on that thing."
                    sf "That means that tomorrow night will be special."
                    sf "I hope you will be ready."
                    mc "I will."
                    sf "I have greats expectations, [mc_name], this will be my first time."
                    sf "It'll have to be perfect."
                    off "Perfect? What does that even mean?"
                    mc "I'll do my best."
                    off "She switches the lights on."
                    sf "I'm sure you will."
                    sf "I'm going to the bathroom."
                    sf "I want you gone when I come back."
                    sf "Goodnight [mc_name]."
                    scene ep5_sc22_mbr_32
                    off "She heads for the door without waiting for a reply."
                    off "I can't help but look at her ass as she heads out of the room."
                    off "It is magnificent."



            scene ep5_sc22_c_02
            off "I can barely walk as I head to my room."
            off "I feel like she dislocated my ass."
            off "Fuck, that felt good."
            off "And I don't have any problems admitting it."
            off "I like it."
            off "I like having my ass fucked by [sf_name]."
            off "That's crazy."
            off "What am I going to do about that?"

            return
        else:


            off "She closes her thighs and removes her panties."
            scene ep5_sc22_mbr_33
            off "She spreads her legs and slowly touches herself."
            sf "I want you to kneel, just there."
            off "Kneel. Of course. No problem."
            off "Shit."
            off "Why isn't there more light in this room?"
            off "She doesn't take long to insert a couple of fingers in her pussy."
            off "Her breathing is getting loud."
            sf "Do you like what you see, [mc_name]?"
            off "My mouth has run dry."
            off "Speaking has become difficult."
            mc "Yes... I like it very much."
            sf "Would you want to touch me, [mc_name]?"
            sf "Would you want to make me wet?"
            off "Holy shit, yes I want it very much!"
            mc "Yes... please..."
            scene ep5_sc22_mbr_34
            sf "Oh, I'm so sorry. But you're clearly not ready yet."
            off "That bitch just wants to tease me to death."
            off "Her pussy is just there and I can't touch her."
            off "This is torture. She wants to torture me."
            off "Ok, I fucked up big time last night when we got that 69 moment, but come on!"
            off "Give me a second chance, dammit!"
            off "She works herself for a few minutes."
            off "She looks at me in the eyes while she tastes her own juices dripping from her fingers."
            off "She's beyond wet."
            sf "I think that's enough."
            off "She pushes me away and stands up."
            scene ep5_sc22_mbr_35
            off "She plugs the thing into her pussy."
            off "Holy mother of god."
            off "She really wears it like a cock."
            off "She's going to destroy my ass with that thing."
            sf "Now [mc_name], there is something you need to know."
            sf "We need some lubricant for it to be... Comfortable for you."
            sf "Do you have any?"
            sf "Without lubricant, it may hurt you a bit."
            off "What?"
            mc "Lubricant? I... don't have any..."
            sf "It's ok. Don't worry."
            sf "There is something you can do to lubricate it."
            sf "You're going to suck on it."
            sf "Open your mouth, [mc_name]."
            off "Is she serious? Of course, she's serious."
            off "She wants me to suck her rubber dick?"
            mc "What? There must be another way... I..."
            sf "I'm going to fuck your ass, [mc_name]."
            sf "You have a choice."
            sf "Do you want it to hurt? Or not ?"

            menu:
                "Resist":
                    $ ep5domresist = True
                    scene ep5_sc22_mbr_36
                    mc "No! Please no!"
                    mc "I'd rather die than suck a dick."
                    mc "Even a rubber one."
                    sf "You didn't have any problem with me sucking yours last night."
                    mc "I... I'm a guy..."
                    sf "So what?"
                    sf "Guys can't suck on a piece of rubber?"
                    sf "You're pathetic."
                    mc "I..."
                    sf "I don't care."
                    sf "You have chosen."
                    sf "Lose your shorts and get on the bed."
                    sf "I want you on all fours."
                    scene ep5_sc22_mbr_18
                    off "I obey mechanically."
                    off "There's no point in putting a fight now."
                    scene ep5_sc22_mbr_19
                    off "She's going to fuck my ass."
                    off "But I can promise you, sweetie, that you're going to pay for that."
                    off "I'm going to pound you so hard that no one will be able to find your pussy once I'll be done with you."
                    off "She climbs on the bed behind me."
                    off "I can feel her hand on my buttocks."
                    off "Her thumb probes my asshole."
                    scene ep5_sc22_mbr_20
                    sf "You need to relax, [mc_name]."
                    sf "If you don't, it will only hurt more."
                    off "Sure, I'm going to relax and enjoy getting my ass violated."
                    off "Fuck that."
                    mc "I'm doing my best!"
                    sf "It could have been much easier and pleasurable for you."
                    sf "You choose the hard way."
                    off "I didn't choose shit!"
                    off "I can feel the toy pressing against me."
                    off "She gives a couple of very soft pushes without much success."
                    off "She finally puts some strength into it."
                    off "She forces her way in."
                    scene ep5_sc22_mbr_21
                    mc "Fuuuuuuck!"
                    off "That thing is so fucking big."
                    off "And much harder than I thought."
                    off "It hurts."
                    off "It hurts a lot!"
                    mc "Shiit!"
                    sf "I warned you."
                    mc "Please! At least spit on it!"
                    sf "You choose not to use any lubricant, remember?"
                    off "She takes it out a bit and I hear her spit on her rubber shaft."
                    off "I'm grateful and ashamed."
                    off "That's a defeat."
                    mc "Thank you."
                    sf "You're welcome."
                    sf "I don't want to hurt you, [mc_name]."
                    sf "You choose this by yourself."
                    off "She pushes back in and goes deeper."
                    scene ep5_sc22_mbr_22
                    mc "Holy shit!"
                    off "I feel like my whole ass is going to explode as she slowly pumps her way inside me."
                    off "The pain is still there but it's bearable, thanks to the few drops of saliva she spat on her toy."
                    off "The toy goes deep enough to touch and move my guts around it."
                    scene ep5_sc22_mbr_25
                    off "I feel it in my belly."
                    off "Was it really that long?"
                    off "It makes me nauseous."
                    off "She tightens her grasp on my tighs and speeds up a bit."
                    off "She moans as she ruthlessly rams into me."
                    sf "Haaan!"
                    scene ep5_sc22_mbr_26
                    mc "Haaaaarwww!"
                    off "She fucks me for real."
                    off "Yesterday was just a joke."
                    off "It's so humiliating."
                    off "And the worse thing about it is that I get some pleasure from it, mixed with the pain."
                    off "It comes from the inside, between my crotch and my rectum."
                    off "It's like an explosion running through my spine."
                    off "My cock is hard as a rock and my balls are ready to discharge their contents."
                    off "She goes at full speed."
                    off "My asshole burns under her assault."
                    mc "Fuuuuck!"
                    off "My lower limbs start contracting uncontrollably."
                    off "My whole body is soon shaking."
                    scene ep5_sc22_mbr_27
                    off "I can't keep my position anymore and I crash on the mattress."
                    off "I came on the sheets and I lay on it."
                    off "I'm out of breath."
                    scene ep5_sc22_mbr_41
                    off "She pulls out and stands up."
                    sf "You came pretty fast for someone so reluctant."
                    sf "How do you feel, [mc_name]?"
                    sf "Did it hurt?"
                    off "Like shit, that's how I feel."
                    mc "A lot."
                    sf "I warned you, didn't I?"
                    off "And you could have spit on it a bit more, for god's sake!"
                    mc "You did."
                    off "She sighs."
                    scene ep5_sc22_mbr_31
                    off "I look at her as she removes the toy from her pussy."
                    sf "However, you took the whole thing."
                    sf "You did it, [mc_name]."
                    sf "I guess you fulfilled your part of the deal."
                    off "Oh yes, I did, bitch."
                    off "And I'm going to enjoy my price, believe me."
                    off "She switches the light on."
                    sf "We'll see how it goes tomorrow."
                    off "She doesn't sound so confident now."
                    sf "I'm going to the bathroom."
                    sf "I want you gone when I come back."
                    sf "Goodnight [mc_name]."
                    $ renpy.end_replay()
                    scene ep5_sc22_mbr_32
                    off "She heads for the door without waiting for a reply."
                    off "I can't wait."
                    off "I'm coming for your pussy, [sf_name] and you know it!"
                    scene ep5_sc22_c_02
                    off "I can barely walk as I head to my room."
                    off "I feel like she dislocated my ass."
                    off "Just wait for it, [sf_name]."
                    off "I'll fuck you so hard that you won't be able to move for days."

                    return
                "Submit [sfDomPath]":

                    $ ep5domsurrender = True
                    $ ProcessStat(2, "sf_dominance")
                    $ DumpNotStack()
                    off "I surrender."
                    off "I just don't want to suffer."
                    off "I can only trust her with it."
                    off "I open my mouth."
                    off "She smiles."
                    sf "You're a smart guy, [mc_name]."
                    sf "Here. Slowly."
                    scene ep5_sc22_mbr_37
                    off "She gives me the tip and I start sucking on it."
                    sf "Take your time."
                    sf "Tell me when you think you have enough."
                    off "I quickly understand that sucking isn't really efficient, I have to lick it and take it deeper."
                    off "If I want that thing to go inside me smoothly, I must have it as slippery as possible."
                    off "I don't know how much time I spend on it."
                    off "A few minutes, perhaps."
                    scene ep5_sc22_mbr_38
                    off "At some point I find the balls to grab her hips."
                    off "She giggles but doesn't protest."
                    off "She even starts caressing my head with both hands."
                    off "She's gentle."
                    off "I feel like she cares about me."
                    off "I like it."
                    off "I'm working that shaft like a passionate whore."
                    off "That dick doesn't taste much."
                    off "Feeling it in my mouth makes me want to puke at first but I quickly accommodate."
                    off "It's not so bad."
                    off "It's just a piece of rubber."
                    scene ep5_sc22_mbr_39
                    off "I can feel [sf_name]'s eyes ogling on me the whole time."
                    off "She smiles."
                    off "When I'm done with it, the rubber cock is soaked in saliva."
                    off "I can't do much more."
                    off "I hope it will be enough."
                    sf "It will be alright, [mc_name]."
                    sf "Trust me. I won't hurt you."
                    off "Her words are actually reassuring."
                    off "She sounds sincere and caring."
                    off "I want to believe her."
                    sf "Lose your shorts and get on the bed."
                    sf "I want you on all fours."
                    off "I guess this is the time."
                    scene ep5_sc22_mbr_18
                    off "I take a deep breath and assume the position."
                    off "She's going to fuck my ass."
                    scene ep5_sc22_mbr_19
                    off "But it's ok. I can take it."
                    off "And she said that she won't hurt me."
                    off "I can trust her, right?"
                    off "She climbs on the bed behind me."
                    off "I can feel her hand on my buttocks."
                    off "Her thumb probes my anus."
                    scene ep5_sc22_mbr_20
                    sf "You're very tense, [mc_name]. You need to relax."
                    sf "The more relaxed the less pain."
                    off "Easier said than done."
                    mc "I'm trying... Just... Just give me a minute please."
                    sf "Sure."
                    off "She sounds concerned."
                    sf "Do you trust me, [mc_name]?"
                    off "Can you trust the girl who's about to violate your ass?"
                    mc "I think I do..."
                    off "I can't really answer anything else, can I?"
                    sf "Good. Then listen."
                    sf "I'm going to penetrate you, but it's going to be alright."
                    sf "It will feel good."
                    sf "It won't hurt."
                    sf "Just the tip, at first."
                    sf "And I'll go slowly."
                    sf "You will tell me when I can go deeper and faster."
                    mc "Ok..."
                    sf "Just relax... You have the right to enjoy it."
                    sf "There's nothing wrong in that."
                    sf "And there's no one to see us."
                    sf "No one will judge you."
                    off "Deep breath."
                    off "She's right."
                    off "No one will ever know."


                    if ep4reluctantsodom == True:
                        off "I almost came from my ass last night."
                        off "So... I guess it can be enjoyable..."
                    else:
                        off "She made me come last night..."
                        off "If I'm being honest, most of it was from my ass..."
                        off "So... I guess it can be enjoyable..."

                    sf "Good. You're doing great. I'm going in, [mc_name]."
                    mc "Ok..."


                    off "I can feel the toy pressing against me."
                    off "She gives a couple of very soft pushes and it pops in like it's nothing."
                    off "It's way bigger than yesterday and yet it enters me so easily..."
                    off "I panic."
                    off "My asshole immediately tightens around the rubber cock."
                    off "It hurts."
                    sf "It's ok, [mc_name]. Don't fight it."
                    sf "Breath. Relax."
                    off "Her voice actually helps me."
                    off "The pain subsides."
                    sf "Yes, just like that. You're doing good, [mc_name]."
                    sf "It's way more comfortable when you accept it, isn't it?"
                    mc "Yes..."
                    sf "Great. I'm going a bit deeper, ok?"
                    mc "Ok..."
                    scene ep5_sc22_mbr_21
                    off "She slowly slides in."
                    off "That thing is so big... How deep can it go?"
                    off "Holy shit."
                    mc "Haaaaan!"
                    off "Did I moan?"
                    off "Fuck, I can't control it."
                    off "She's fucking my ass and I'm starting to feel good."
                    off "She starts pumping more seriously."
                    off "That thing is so big that I can feel it touching and moving my guts around it."
                    off "It makes me nauseous."
                    sf "You're really doing great."
                    sf "I'm going fully in."
                    scene ep5_sc22_mbr_22
                    mc "Okkaaaaaaay!"
                    off "She stumbles on my buttocks."
                    off "She can't go deeper."
                    off "I took it all in."
                    off "Oh my god, I took it all in."
                    off "It feels so weird... and good at the same time."
                    off "She's right."
                    off "She's completely right!"
                    off "Fuck the shame!"
                    off "I want her to fuck me more!"
                    scene ep5_sc22_mbr_24
                    mc "Haaaannn!"
                    off "She shags me slowly for a few seconds."
                    off "My moans make it obvious that I'm enjoying this."
                    sf "You seem to enjoy this, [mc_name]."
                    sf "Do you mind if I speed up a bit?"
                    off "Her breathing is loud."
                    off "She groans from time to time."
                    mc "Yes, please..."
                    scene ep5_sc22_mbr_25
                    off "She tightens her grasp on my hips and starts ramming into me faster."
                    off "I suddenly feel a massive wave of pleasure coming from my ass."
                    off "I barely manage to hold it."
                    off "It's brutal and ripples through my spine."
                    off "My dick is hard as a rock."
                    off "My balls are on fire."
                    mc "Haaaaaawwwwwwnn!"
                    off "I almost came."
                    mc "Holy mother of god!"
                    off "The rhythm of her blows intensifies."
                    off "She fucks me faster."
                    scene ep5_sc22_mbr_26
                    sf "A bit rougher maybe?"
                    sf "Do you like that [mc_name]?"
                    mc "I like it! Oh, shiiiiiiit!"
                    off "Here it comes again, and there's nothing I can do this time."
                    off "I unload everything I have."
                    off "I come so much that, for a moment, I wonder if I haven't pissed myself."
                    off "My lower limbs start contracting uncontrollably."
                    off "My whole body is soon shaking."
                    scene ep5_sc22_mbr_27
                    off "I can't keep my position anymore and I crash on the mattress."
                    off "I came on the sheets and I lay on it."
                    off "I'm out of breath."
                    scene ep5_sc22_mbr_40
                    off "She pulls out and stands up."
                    sf "How do you feel, [mc_name]?"
                    sf "Did it hurt?"
                    sf "You seem to have enjoyed it a lot, am I wrong?"
                    off "She fucked my brains out."
                    off "There are no other words."
                    mc "Yeah."
                    sf "Oh, Dear. You'll have to be more explicit."
                    mc "It didn't hurt much... And I enjoyed it."
                    $ ep5domsurrender = True
                    $ ProcessStat(2, "sf_dominance")
                    $ DumpNotStack()
                    sf "I'm glad to hear that."
                    sf "You see, that's what happens when you trust me."
                    sf "Do you want me to take care of you again soon?"
                    off "Holy shit, I want to cry."
                    mc "Yes... Please..."
                    off "I can't believe I'm saying this."
                    sf "You're making me very happy, [mc_name]."
                    sf "I want you to know that."
                    sf "I promise I'll take good care of you."
                    scene ep5_sc22_mbr_31
                    off "I look at her as she removes the toy from her pussy."
                    sf "You did it, [mc_name]."
                    sf "You fulfilled your part of the deal."
                    off "I'd almost forgotten about that."
                    off "It's ridiculous."
                    sf "We'll see tomorrow how we can conclude that."
                    off "She sounds bright and playful."
                    off "She's actually looking forward to it."
                    off "Holy shit!"
                    sf "I'm going to the bathroom."
                    sf "I want you gone when I come back."
                    sf "Goodnight [mc_name]."
                    scene ep5_sc22_mbr_32
                    off "She heads for the door without waiting for a reply. "
                    scene ep5_sc22_c_02
                    off "I can barely walk as I head to my room."
                    off "I feel like she dislocated my ass. "
                    off "I'm completely baffled."
                    off "She fucked my ass hard and I liked it."
                    off "I came from it."
                    off "Tomorrow night I will have sex with her and she seems more than ok with it."
                    off "Am I smiling?"
                    off "I am smiling."
                    off "I think I'm happy..."
                    off "Holy shit..."

                    return
    else:

        scene ep5_sc22_mbr_42 with dissolve
        sf "What do you want [mc_name]?"
        off "Her tone is cold and harsh."
        off "Maybe even angry."
        off "Perhaps I shouldn't have come."
        mc "I... thought you would want to see me..."
        sf "Why would I want to see you?"
        off "That's an excellent question."
        off "She knows that I'm doing stuff with [sis_name] while also... Playing with her."
        off "Why would you want to see an asshole like me?"
        mc "I thought that... maybe you would want to talk..."
        sf "About what? I wonder."
        sf "Perhaps about the fact that you have some... Unusual interactions with my best friend?"
        off "She sounds bitter and sad."
        mc "You don't want to talk about it ?"
        off "The silence gets heavy."
        off "I can't see her eyes but I can feel her gaze washing over me."
        off "She sighs."
        sf "You just want to know if I'll tell anyone."
        sf "I won't."
        sf "It would only hurt her."
        sf "She's precious to me."
        sf "I don't want to hurt her."
        off "Thank god."
        scene ep5_sc22_mbr_04
        sf "Now tell me I don't have to warn you again."
        sf "You are aware of what will happen if she ever complains about you, right?"
        sf "Can I trust you, [mc_name]?"
        mc "Yes... Of course..."
        sf "Of course? As if it was obvious."
        off "Fair point."
        sf "You lied and you cheated on me."
        sf "And lied and cheated on her."
        sf "Do you think I should give you my confidence just like that?"
        off "I lied and cheated?"
        off "I guess I did."
        off "But she sounds like she viewed us as a real couple."
        off "Was she my girlfriend?"
        off "I'm so confused."
        mc "I...I'm sorry..."
        sf "Oh, I bet you are..."
        off "Ok. I'm an asshole."
        off "There is no doubt about it."
        off "The guilt is there and it crushes me."
        off "And I'm ashamed."
        off "She lets me linger a bit in my malaise before resuming in a much softer, sadder tone."
        sf "She was happy today."
        sf "Despite everything that happened in the last few days."
        sf "She was genuinely happy."
        sf "I believe you when you say that you're not abusing her."
        mc "I would never do anything like that."
        off "The silence again."
        off "She looks away."
        scene ep5_sc22_mbr_43
        off "She rises from her chair and turns to the window."
        off "I'm not sure there's anything interesting outside."
        off "She's just tired of looking at me."
        sf "Get out, [mc_name]."
        sf "You have what you came for."
        sf "From now on we're just acquaintances."
        off "Ok... So... she won't say anything to anyone, she will let me continue my relationship with [sis_name] and... our thing is over."
        off "I guess everything went better than I expected."

        if sf_affection > 10:
            off "Then why am I not satisfied?"

        menu:
            "Get out.":
                $ ep5domgotout = True
                off "I guess I'm free to go then."
                off "I should leave before she changes her mind."
                mc "Goodnight [sf_name]."
                sf "Goodnight [mc_name]."
                off "She doesn't move."
                off "I have second thoughts as I head for the door."
                off "I'm about to abandon her to her sorrow."
                off "I don't feel good about that."
                mc "[sf_name]... I'm sorry for everything."
                off "I probably hoped that she would give me her forgiveness."
                off "Maybe talk a bit more and leave each other as friends... But none of that happens."
                off "She stays silent as I ridiculously wait for a reply that doesn't come."
                scene ep5_sc22_c_02
                off "I leave the room, feeling like the worst cunt ever."
                off "What a fucking mess."
                off "I'm gonna need a moment to process all that."

                return

            "Stay. [sfDomPath] [sfLovePath]" if sf_affection > 34 and sf_dominance > 24:
                $ ep5domstayed = True
                off "I should get out of here."
                off "Why am I not moving?"
                off "What am I doing?"
                off "At least say something, [mc_name]."
                off "You look like an idiot."
                off "Don't you think it's time to grow a pair?"
                scene ep5_sc22_mbr_44
                off "You've hurt her."
                off "You're not just going to leave, right?"
                off "Yeah, she fucked your ass, and you weren't completely ok with that."
                off "And she made you eat your own cum."
                off "But she's still... [sf_name]... and she's clearly not doing well."
                off "It must have been hard for her to act as if nothing had happened all day long."
                off "Can you try to be a decent human being, [mc_name]?"
                scene ep5_sc22_mbr_45
                off "She turns to me."
                sf "Why are you still here?"
                sf "What part of \"get out\" is too difficult for you to understand?"
                mc "I'm sorry [sf_name], but I don't want to leave you alone like that."
                sf "Excuse me?"
                mc "I never wanted to hurt you."
                sf "So you thought that two-timing us was ok and that everything would go smoothly ?"
                mc "No! No, it didn't happen like that."
                mc "I just got caught up in it."
                mc "I never planned that."
                mc "It was an accident..."
                sf "An accident? Are you mocking me?"
                mc "No, [sf_name]... I know it doesn't make much sense but..."
                sf "Alright, I'm listening."
                sf "How did you get trapped in this situation?"
                sf "I am very curious."
                off "Are you sure about this [mc_name]?"
                off "Aren't you just going to make things worse?"
                off "You never think before talking, do you?"
                scene ep5_sc22_mbr_46
                mc "Ok... I... I guess it started last Sunday."
                mc "We got a bit drunk that night and... after we all got to bed... at some point..."
                mc "You were snoring... And I needed to pee..."
                mc "[sis_name] and I got up and unexpectedly met in the living room."

                if sis_love_path == True:
                    mc "Nothing really happened."
                    mc "We just... Looked at each other."
                    mc "I don't know how to explain it."
                    mc "Something was different."
                    mc "Something happened between us at that moment."
                    mc "You will probably think that it's stupid."
                    sf "You're telling me that you suddenly fell in love with just a look?"
                    mc "Well, there was a hug... then that look... but yes..."
                    off "I wait a few seconds, expecting her to comment on how ridiculous this is but she doesn't say a word."


                if sis_sub_path == True:
                    mc "She was... watching a porn movie and touching herself."
                    mc "I don't know why I did that... I just joined her."
                    mc "I sat next to her, got my dick out and started jerking off."
                    sf "How elegant."
                    mc "I know it's crazy."
                    mc "We ended up touching each other."
                    sf "Touching each other?"
                    sf "I'm going to need more details, [mc_name]."
                    mc "She... Stroked my dick and I... Inserted a few fingers inside her..."
                    off "She sighs loudly."


                scene ep5_sc22_mbr_47
                mc "The day after that I was very confused."
                mc "I felt guilt but also... Excitement."
                mc "But... It's [sis_name] we're talking about."
                mc "And she's like a sister to me."
                mc "So I never really thought that it was a real possibility."
                off "My mouth gets dry."
                off "I'm not really comfortable talking about all this."
                off "Why am I even doing that?"
                mc "When you asked me to join you in that fitting room..."
                mc "I had no doubt that I was... fully available."
                mc "I thought that your offer was... Weirdly presented, but I accepted it."
                mc "I did so because I was interested in you."
                mc "You're beautiful and kind, and to be honest, I have dreamed of being with you..."
                mc "Just like every other guy in school I guess..."
                mc "I was sincere."
                mc "But... I don't know how to say that..."
                mc "Your approach of our relationship... was... unexpected."
                scene ep5_sc22_mbr_48
                sf "What are you talking about?"
                off "She stills sounds angry but there's something else."
                off "She's vexed."
                mc "Well... The whole thing was weird..."
                mc "It was our first moment as a couple..."
                mc "We could have kissed a bit, cuddle a lot, talk about stuff and it would have been perfect."
                mc "But instead of that, you stripped me naked and well... you know what happened."
                scene ep5_sc22_mbr_49

                if ep3ballscrushed == True:
                    mc "It was humiliating and painful."
                    mc "You crushed my balls..."
                    sf "You deserved that."
                    sf "You shook hands with Luke!"
                    off "I can't deny that."
                    off "But that handshake did not deserve such a punishment."
                    mc "Maybe, but that isn't the point."
                else:

                    mc "It was humiliating..."
                    sf "I made you come."
                    sf "Weren't you satisfied ?"
                    off "I can't deny that the footjob was nice but..."
                    mc "You made me eat my cum from your feet!."
                    sf "You didn't like it?"
                    off "She sounds... surprised."
                    off "Did she really think I would enjoy that?"
                    mc "No! No, I didn't!"



                mc "[sf_name]... That's... That's just not how you treat your significant other."
                mc "At least not in my book."
                mc "And... I thought that maybe I wasn't your boyfriend after all, that you were just toying with me."
                sf "I have never toyed with you!"
                off "She has obviously no doubt about that."
                off "That makes the situation even weirder."
                scene ep5_sc22_mbr_50
                mc "Well, sorry, but to me, it looked a lot like you did."
                mc "So when we parted ways after... our encounter in the living room, I was very confused."
                mc "You weren't my girlfriend, and we weren't a couple."
                mc "It was something else."
                mc "Something weird I wasn't sure I wanted in."
                mc "I didn't understand what you wanted from me."
                scene ep5_sc22_mbr_51
                off "She seems troubled."
                off "Maybe she's has some regrets about that event?"
                off "I take a deep breath."
                off "The story wasn't easy to tell until now, but she may find it really unpleasant with what's yet to come."

                if sis_love_path == True:
                    mc "That night, [sis_name] came to my room and we had a talk."
                    mc "She was as confused as I..."
                    mc "We kissed."
                    mc "We kind of decided that... We wanted to try to be... More for each other."


                if sis_sub_path == True:
                    mc "That night... I met [sis_name] in the kitchen."
                    mc "Again it was completely fortuitous."
                    mc "We talked... about the things we did the night before that."
                    mc "And... I realized that... I wanted to take care of her..."
                    mc "She seemed... happy about it and we did things..."
                    off "Maybe I can elude the actions a bit."
                    off "She asked for details but I'm not sure that they're necessary."
                    mc "But that's not important."
                    mc "What matters is that I offered her to be more than just her friend... And she accepted..."


                scene ep5_sc22_mbr_52
                sf "Are you telling me that this is... A misunderstanding?"
                off "That sounds ridiculous... But that's kind of what I'm trying to explain."
                mc "I wouldn't say it like that."
                mc "Obviously, I've handled the situation very poorly."
                mc "But... I didn't think that we were a couple."
                mc "I didn't even think that you may be... Serious about me... or us."
                mc "I looked for a way to tell you that I wasn't interested in that kind of game..."
                mc "But when the morning came and we talked in the living room..."
                mc "I was still confused and you were very... Persuasive."
                mc "I'm ashamed to say that but..."
                mc "I simply wasn't able to tell you because I didn't want to hurt you."
                mc "And also, because I was still interested in you."
                scene ep5_sc22_mbr_53
                sf "I made you horny."
                sf "That's what you're saying."
                sf "I made you horny and that prevented you from breaking up with me."
                sf "This is pathetic, [mc_name]."
                sf "Do you know that?"
                off "I did my best to sugar coat it but she saw right through me."
                off "It's embarrassing."
                mc "I can't deny it..."
                scene ep5_sc22_mbr_54
                sf "And that's the only reason why you joined me last night."
                sf "You thought that you had an option."
                sf "You thought that maybe you could have sex with me."
                sf "Am I right?"

                menu:
                    "It's true. [sfLovePath]":
                        $ ProcessStat(2, "sf_affection")
                        $ ProcessStat(1, "sf_dominance")
                        $ DumpNotStack()
                        mc "But wasn't it what you wanted?"
                        mc "I mean... You were pretty assertive that morning."
                        mc "You did everything you could to make sure I would join you in the evening."
                        mc "I just couldn't resist you and I'm not proud of it."
                    "No! [sfDomPath]":
                        $ ProcessStat(1, "sf_affection")
                        $ ProcessStat(2, "sf_dominance")
                        $ DumpNotStack()
                        mc "I mean... Yes, of course, the... Possibility of having sex with you was a strong incentive."
                        mc "But... I told you... I was confused."
                        mc "And intrigued by you."




                mc "I think I also hoped that things could become... normal between us."
                mc "It was foolish."
                mc "But even if your games aren't to my liking, you're still [sf_name]."
                mc "And I care about you."
                mc "When I heard you talking earlier, I realised that you cared about me too and that I just hadn't been able to see it."
                mc "To me, it feels like we both like each other but we don't express it in the same way."
                scene ep5_sc22_mbr_55
                sf "Are you saying that I'm at fault?"
                off "She remains calm but her words are filled with cold anger."
                off "Choose your words wisely, [mc_name]."
                mc "No! No, of course not."
                mc "It's just that... the way you express your feelings makes it harder for me to... understand them."
                sf "How should I have expressed myself?"
                sf "Tell me."
                sf "You think I don't know what you wanted to do to me?"
                off "The intensity of her voice rises."
                mc "What I wanted to do to you?"
                sf "Yeah, perhaps I should have let you fuck me and dump me once it was over?"
                mc "Why would I..."
                sf "I know that's what every guy wants."
                sf "Are you going to tell me that you're different?"
                off "Holy shit, what kind of dork does she think I am?"
                scene ep5_sc22_mbr_56
                mc "Ok hold on there."
                mc "I can't deny I'm interested in having sex with you."
                mc "Of course, I am. But come on..."
                mc "I'm not going to get rid of you once it's done!"
                mc "I've just told you that I would have been more than happy with a few kisses and cuddles for our first moment together."
                sf "And I'm supposed to believe you?"
                mc "[sf_name], I can't deny that some guys are total assholes that would do such things."
                mc "But not all of us are!"
                mc "Why would you believe that I could treat you like that?"
                mc "All the things you did to me, was that just because you were afraid of me?"
                mc "Why did you even approach me if you were so defiant?"
                scene ep5_sc22_mbr_57
                sf "Because I like you, moron!"
                sf "Is that so hard to understand?"
                off "What the hell is going on in her head?"
                off "She thinks that every guy is an asshole, but she likes me so she decided to do these things to me?"
                off "I begin to put things together."
                off "She likes me and is afraid of me at the same time?"
                off "She thinks I'm going to fuck her and get rid of her once I've used her?"
                off "This is crazy."
                mc "Are you... are you trying to... Domesticate me?"
                mc "To make sure I won't leave you?"
                scene ep5_sc22_mbr_58
                sf "What if I was? What is wrong with that?"
                off "Her defiance is heartbreaking."
                off "She's afraid of being abused and abandoned or something like that."
                off "What kind of scars does she hide?"
                off "I am at a loss of words."
                mc "[sf_name]... You don't need to do that."
                mc "I'm sorry... I'm no expert but... you simply can't force love."
                mc "It comes, and if we're lucky, it stays..."
                mc "If it fades away, we just don't have a choice but to cope with it."
                off "It didn't sound so bad for something that came out naturally from my mouth..."
                sf "I did what I had to do!"
                sf "Would you have loved me and stayed with me without that?"
                sf "You're leaving me for [sis_name]!"
                sf "I'm not going to believe your lies, [mc_name]."
                off "She wants to be loved."
                off "She's terrorized of being used and discarded."
                mc "Our story would have been very different, that's for sure."
                mc "I don't know what would have become of us."
                mc "And... It will sound selfish and you will probably think that I'm the king of assholes..."
                mc "But I don't want to leave you..."
                scene ep5_sc22_mbr_59
                off "Silence fills the room."
                off "She seems shocked."
                off "I don't really understand why I said that."
                off "I want to be with [sis_name]."
                off "But in the mean time... Now that I'm aware of her weakness and her suffering... I don't want to abandon her."
                off "I want to take care of her too."
                off "What a moron."
                off "I really have a thing for broken girls, don't I?"
                scene ep5_sc22_mbr_60
                sf "You don't want to leave me?"
                off "Her tone is much softer."
                mc "No! I've just realized that you care about me."
                mc "And I care about you..."
                mc "And everything that happened between us was... something I just couldn't get my grip on."
                mc "I feel like a moron because we should have had this discussion long ago."
                mc "I think I was afraid of you too."
                sf "I don't understand, [mc_name]."
                sf "What are you expecting from this conversation?"
                mc "I have no idea."
                mc "The only thing I'm sure of is that I don't want you to suffer in any way."
                mc "Yet, because I'm an idiot, I may not have the choice."
                scene ep5_sc22_mbr_61
                off "She looks at me for a moment before turning back to the window."
                off "The silence grows uncomfortable."
                off "I should say something."
                sf "What did you tell her?"
                off "Her question surprises me."
                mc "About what?"
                sf "Did you tell her that you love her?"
                mc "Yes."
                sf "What else?"
                mc "That I wanted to protect her... To be there for her... That I would never leave her alone."
                sf "Would you have said these things to me if I hadn't... treated you like I did?"
                mc "I'm sure I would have."
                mc "I could even tell you these words right now because I understand you a bit more."
                mc "Despite what you may think, I still care about you."
                off "The silence again."
                off "At least she doesn't seem angry anymore."
                sf "Lay on the bed."
                off "I thought we were done with that kind of game."
                off "I guess I was wrong."
                mc "What?"
                sf "I asked you to lay on the bed. Please. Just do it."
                scene ep5_sc22_mbr_62
                off "I obey."
                off "I'm not sure I mind."
                off "She turns to me and gazes over me for a moment."
                off "She slowly approaches the bed and crawls on it towards me."
                scene ep5_sc22_mbr_63
                off "She crashes on my chest."
                sf "Hold me."
                off "This is so weird."
                off "I never imagined I would share this kind of embrace with her."
                off "It's comfortable... but so sad."
                off "It tastes like a farewell."
                sf "So you didn't enjoy licking my foot? I thought that guys liked that."
                off "She definitely has something for pulling some inappropriate questions at the weirdest moment."
                off "And she asks that with a childish and innocent tone."
                off "Let's answer honestly."
                mc "Licking your foot was ok."
                mc "Not because it was a foot, but because it was yours."
                mc "Eating my cum, on the other hand, was definitely not ok."
                sf "What about the thing I did to your ass?"
                mc "Ok, just don't tell anyone about that... but I may have liked it."
                sf "You would have enjoyed going further."
                mc "I'm sure I would have."
                off "We stay like that, laying on the bed in silence."
                off "I don't know what to do."
                off "I don't really want to do anything."
                off "I feel like we could have been something else, and it all ended because we couldn't understand each other."
                off "I'm responsible for this."
                scene ep5_sc22_mbr_64
                off "She finally moves away from me and sits on the edge of the bed, turning her back to me."
                sf "Get out now."
                off "She sounds sad and resigned."
                off "I guess this is it."
                mc "[sf_name]..."
                sf "Get out. She's waiting for you."
                off "There's nothing I can reply to that."
                mc "Good night, [sf_name]."
                sf "Good night [mc_name]."
                scene ep5_sc22_c_02
                off "What a fucking mess."
                off "I can't say I'm feeling well."
                off "I don't know what happened to her to make her have these kinds of fears about boys and relationships..."
                off "What more could I have done to help her?"
                off "I'm gonna need a moment to process all that."


    return

label EveEventIntro:
    scene black with dissolve
    with Pause(2)


    if ep5sftruelove == True:
        if sis_sub_love_path == True:
            scene ep5_sc23_mbr_01 with dissolve
        else:
            scene ep5_sc23_mbr_02 with dissolve

        off "[sf_name] has been asleep for around half an hour now."
        off "I looked at her, peacefully sleeping for some time."
        off "She's beautiful."
        off "She was so happy that I stayed with her tonight..."

        if sis_sub_love_path == True:

            off "What the fuck is wrong with me?"
            off "This girl is wonderful."
            off "She loves me."
            off "She gave herself to me."
            off "She trusts me."
            off "And I'm about to go meet [sis_name]..."
            off "I don't understand myself."
            off "I love [sf_name] and I want to stay here with her, but in the meantime, I know that [sis_name] is alone, and waiting for me."
            off "I want to join her."
            off "We weren't very discreet."
            off "I'm sure that [sis_name] heard us."
            off "I can't leave her wondering all night long."
            off "I have to talk to her."
            off "I shouldn't have made love with [sf_name]."
            off "I wanted it, and it was fantastic, but it was a mistake."
            off "It can only lead to problems."
            off "I'm going to hurt her."
            off "I'm a fucking scumbag."

        if sis_hard_sub_path == True:

            off "I'm pretty sure she won't wake up if I leave her for an hour."
            off "Just enough time to find [sis_name] and play with her a bit."
            off "I'm sure that this is the night."
            off "She's ready."
            off "I'm gonna score two pussies tonight!"
            off "I can't believe it."
            off "I'll have to tell Steve about it."
            off "I can't keep that to myself."
            off "I'm sure he won't tell anyone."
    else:

        scene ep5_sc23_mcr_01 with dissolve
        if sf_love_path == True:

            if ep5sflovemistake == True:

                off "Now that I've ruined everything with [sf_name], I can go and enjoy [sis_name] light-heartedly."
                off "That conversation was painful but in the end, I think that it's for the better."
                if sis_sub_love_path == True:

                    off "Let's be honest."
                    off "Flirting with [sf_name] was a mistake."
                    off "I can't take care of [sis_name] and have a relationship with [sf_name] at the same time."
                    off "It's just impossible."
                if sis_hard_sub_path == True:

                    off "It's no big deal."
                    off "I don't need [sf_name]."
                    off "I have [sis_name] to take care of my needs."
                    off "I'm going to fuck her tonight."
                    off "I can't wait."
                    off "I can hear that pussy calling my name!"
            if ep5sflovebj == True:

                off "I'm not gonna lie, the blowjob that [sf_name] gave me was incredible."
                off "And it's something she learned from Jane."
                off "I wonder if [sis_name] got some special skills out of it too?"
                off "I like where this is going."

        if sf_dom_path == True:

            if sis_sub_love_path == True or sis_love_path == True:

                if ep5domgotout == True:

                    off "I'm not happy about how things ended with [sf_name] but it's over now."
                    off "It should never have been this way."
                    off "It's hard to believe but... After all the things she did to me... Learning about my affair with [sis_name] really took its toll on her."
                    off "It hurt her."
                    off "I guess that she cared about me more than I thought."
                    off "Maybe that I was more than a toy to her after all..."
                if ep5domstayed == True:

                    off "I can't stop thinking about it."
                    off "That hug with [sf_name]... what did that mean?"
                    off "I feel so bad about all of that..."
                    off "Despite what she did to me... I'm not just a toy to her."
                    off "I hate hurting her..."
                    off "It was clearly a farewell."
                    off "Our weird story is over I guess..."
                    off "Why do I feel so bad about it?"
                    off "No doubt I've been an asshole."
                    off "But there's something else."
                    off "Regrets?"

                off "I guess it's too late to think about that now."
                off "I should concentrate on [sis_name] now. She's waiting for me."

            if sis_hard_sub_path == True:

                off "I've waited for quite some time, in case [sf_name] finally requested my presence."
                off "It's getting late."
                off "I'm sure she's asleep by now."
                off "I've already wasted a good opportunity to have some fun this afternoon, I'm not gonna do that again."
                off "I'm going to take my chances."
                off "I'm sure that [sf_name] was bluffing."
                off "She knows nothing."
                off "Otherwise, she would have already intervened."

        if sf_love_path == False and sf_dom_path == False:

            if sis_sub_path == True:

                off "I'm going to have an intense conversation with [sis_name]."
                if sis_sub_love_path == True:

                    off "We have many things to talk about."
                    off "It's time to deepen our bond."
                    off "I have to make her understand how much I care about her."
                    off "Our moment this afternoon was a nice start."
                    off "Let's build on that."
                if sis_hard_sub_path == True:

                    off "I have a blowjob to collect, and that's just an appetizer."
                    off "I'm horny as fuck."
                    off "I need to release some pressure."
                    off "What's best for that than getting my balls emptied by my pretty little princess?"

            if sis_love_path == True:

                off "I can't stand being away from [sis_name] for too long."
                off "I waited long enough..."
                off "The more I think about it the less I care about being caught in the act by anyone."
                off "I need her."
                off "I don't give a damn about what others may think."
                off "Holding her hand, this afternoon... That's stupid... I just couldn't stop thinking about it."
                off "I hate myself for not doing it sooner."
                off "Simple things, that say that I love her."
                off "I just want to hold her in my arms and be with her."



    scene ep5_sc23_c_01

    off "Everyone should be fast asleep by now."
    off "I'm going to knock on her door."
    scene ep5_sc23_c_01
    off "No response."
    off "Maybe she's sleeping."
    off "I can't blame her."
    off "I wait a bit and open the door."
    scene ep5_sc23_sr_00
    off "There's no one here."
    off "Where did she go?"
    scene ep5_sc23_c_03
    off "Wait... Is that some noise coming from downstairs?"
    off "Voices? Music?"
    off "Someone is watching TV."
    off "It feels like a re-enactment of Sunday Night."
    off "I wouldn't mind that becoming a habit."
    label galleryScene11:
    scene ep5_sc23_lr_01
    if sis_sub_path == True:

        off "The film is quite different though."
        off "No more high-quality porn but some old black and white movie."
        off "She really likes that kind of stuff."
        call ep5sc23 from _call_ep5sc23
    if sis_love_path == True:

        off "Another black and white movie."
        off "She really likes that kind of stuff."
        call ep5sc24 from _call_ep5sc24



    return


label ep5sc23:
    scene ep5_sc23_lr_02
    off "She silently looks at me as I walk towards her."
    off "I like the expression on her face."
    off "She knows that something is about to happen."
    scene ep5_sc23_lr_03
    if sis_sub_love_path == True:
        mc "Hey, Princess. Having fun?"
        sis "Hey... I'm... watching a movie..."
        mc "I can see that."
        mc "Mind if I join you?"
        sis "Sure... But it's not your kind of movie..."
        mc "Black and white is growing on me."
        mc "I'll soon be a fan."
        sis "Ok, if you came here to mock my tastes..."

        menu:
            "I came here for you. [sisLoveSubPath]":
                $ ProcessStat(3, "sis_affection")
                $ ProcessStat(3, "sis_submission")
                $ DumpNotStack()
                $ ep5siscameforyou = True
                mc "And I don't have anything against black and white movies."
                mc "If you like this one, it's probably because it's good."
                mc "I'm not mocking you."
                off "Here it is."
                off "That embarrassed look."
                sis "Ok..."
            "You know what I came for. [sisSubPath]":

                $ ProcessStat(5, "sis_submission")
                $ DumpNotStack()
                $ ep5siscameknow = True
                off "She looks at me with that embarrassed and vulnerable expression on her face."
                off "I just can't resist it."

        scene ep5_sc23_lr_04
        off "I sit next to her and immediately grab her by her shoulder."
        off "I pull her to me."
        off "She protests but doesn't resist."
        sis "What are you doing?"
        mc "I want to hug you. Is that a problem ?"
        sis "Someone could see us..."
        mc "Who cares?"
        mc "Kelly and [sf_name] are sleeping."
        mc "And even if they are not, they're on the other side of the house with hallways and doors between us."
        mc "There's no way they can hear or see us."
        mc "Come on, remember this afternoon."
        mc "Just lean on me and relax."
        mc "You will like it."
        scene ep5_sc23_lr_05
        off "She obeys and progressively lets go of herself."
        mc "Are you comfortable?"
        sis "Yeah..."
        mc "Great... So what's the movie?"
        sis "Spellbound."
        mc "Sounds nice."
        off "I let her go back to the film."
        off "I gently hold her against me and caress her arm and shoulder."
        off "I can feel her relaxing on me a bit more with each minute."
        sis "You're not here for the movie."
        off "It sounds like an accusation."
        off "She sounds tired and resigned."
        off "Her breathing gets more intense."
        off "Did I turn her on in any way?"
        mc "I've already told you why I'm here."
        scene ep5_sc23_lr_06
        sis "What are you... Going to do to me?"
        mc "I think I'm going to lick your pussy."
        mc "You know I like how you taste."
        mc "After that, I'll probably play with your breasts for some time."
        mc "Then I guess I'll let you surprise me."
        mc "I'm sure you will find how to please me."
        mc "But first, I'm going to kiss you, and we're going to have a nice conversation."
        mc "Does that program suit you ?"
        off "She takes some time to utter the words."
        off "I can feel her struggle."
        off "There's still some inner conflict at work inside her."
        scene ep5_sc23_lr_07

        if sis_submission > 30:
            sis "Yes."
            off "That word feels good."
            off "She gives in."
            off "If I had any doubt that she wanted me to take control, here is my confirmation."
            off "She chooses to rely on me."
            mc "I'm here. Don't worry. You're safe."
            mc "I've told you that I will protect you."
            mc "I don't intend to go back on my words."
            mc "You can trust me."
            mc "I'll take care of everything."
            mc "Look at me, Princess."
            mc "You know that I won't allow anyone to hurt you, right?"
        else:

            sis "I don't know... It's... We shouldn't..."
            mc "Shhhh... Do you trust me, Princess?"
            off "She seems to hesitate."
            sis "Yeah..."
            mc "We don't care if we should or shouldn't."
            mc "We're together."
            mc "You're mine, I'm yours. Remember?"
            mc "That's the only thing that matters."

        scene ep5_sc23_lr_07_bis
        off "She silently looks at me a few seconds before she nods a shy yes."
        mc "Great. Now, about that kiss..."
        off "I slowly caress her chin and her cheeks."
        off "She stares at my lips as they are getting closer to her."
        off "I'm not going for an innocent peck."
        scene ep5_sc23_lr_08
        off "Our tongues meet before our lips."
        off "She seems hesitant at first, but after a few seconds, I can tell that she's been waiting for it as much as me."
        scene ep5_sc23_lr_09
        off "We suck on each other's lips and tongues for several minutes."
        off "Her breathing is loud."
        off "Her eyes are barely opened."
        off "She seems to be about to collapse in bliss."
        scene ep5_sc23_lr_10
        mc "I want you to remove your pyjamas."
        off "She's surprised."
        off "She probably thought that I would wait until after our conversation to strip her naked."
        off "She stands up and looks away in shame while losing her clothes."
        scene ep5_sc23_lr_11
        off "She tries to hide her intimacy with her arms and hands."
        off "She's cute."
        mc "Come here, Princess."
        off "I grab her and pull her towards me."
        off "I caress her thighs and her hips."
        mc "You're beautiful, Princess."
        mc "I don't think I've told you that often enough."
        scene ep5_sc23_lr_12
        off "I want to stick my face between her thighs but my position is awful and I fail miserably."
        off "I can barely touch her clitoris with the tip of my tongue."
        off "But I can smell her."
        off "And it makes me hard in the second."
        scene ep5_sc23_lr_13
        off "I kiss her pubis."
        off "I can feel the pubic hairs barely surfacing on her skin."
        off "She shaves."
        off "That looks perfect to me."
        mc "Princess, you make me crazy."
        mc "Do you know that?"
        sis "I'm... not doing anything..."
        off "I clutch her and drag her with me as I move to the corner of the sofa."
        mc "Sit on my lap. Here. Like that."
        scene ep5_sc23_lr_14
        off "I gently hold her against me."
        off "I let my hands wander over her hips and her belly."
        off "It's extremely difficult not to directly grab her breasts and knead the shit out of them."
        off "I still manage to control myself."
        off "I want her to understand that I'm not an animal."
        off "She can trust me and my self-control."
        mc "Are you comfortable?"
        off "She nods a shy yes."
        mc "Great. I want to hear your voice, Princess."
        mc "Tell me about your day."
        sis "My day? You were there the whole time..."
        mc "No that's not true."
        mc "We've been separated for some time."
        mc "I want to know everything."
        mc "What you did, how you felt... from last night to this moment."
        mc "Everything."
        off "Her skin is softer than silk."
        off "And it's hot."
        off "It's like her whole body is radiating heat."
        off "She progressively leans on me."
        sis "Ok..."
        scene ep5_sc23_lr_15
        mc "Let's start with last night."
        mc "Just after you left this room."
        mc "What did you do?"
        sis "I... Went to the bathroom... To clean my belly."
        mc "Because I came on it. Did that bother you?"
        sis "No..."
        off "I like the sound of that. "
        mc "Ok... what did you do after that?"
        sis "I went to bed. I slept."
        mc "Was it easy to fall asleep?"
        sis "No..."
        mc "Why?"
        sis "Because I kept thinking... about the things you did to me."
        scene ep5_sc23_lr_16
        off "My fingers lightly brush the bottom of her breasts."
        off "Her breathing intensifies a bit."
        scene ep5_sc23_lr_17
        mc "Did that trouble you?"
        off "She nods a yes."
        mc "I'm sorry Princess."
        mc "Didn't you like what we did?"
        off "She swallows with difficulty before taking a deep breath."
        sis "I liked it."
        off "It's barely a whisper."
        off "She seems to be about to break down in tears."
        off "She liked it, and that's the problem."
        mc "Shhhh... It's ok Princess."
        mc "You don't have to be afraid, or ashamed."
        mc "You liked it and it's alright."
        mc "There's nothing wrong with that."
        off "Let's be honest, there are many legitimate reasons for her to be uneasy with what we're doing."
        scene ep5_sc23_lr_18
        mc "I love you, Princess."
        mc "I don't like to see you cry."
        mc "It breaks my heart."
        mc "Everything will be alright."
        mc "I promise."
        mc "Do you trust me?"
        off "She nods."
        mc "Great."
        scene ep5_sc23_lr_19
        off "I start kissing her neck."
        off "I can feel her reacting to my breath on her skin."
        off "She likes it."
        mc "So you fell asleep."
        sis "Yeah... [sf_name] woke me up in the morning..."
        sis "We ran to the park."
        sis "We did some yoga..."
        mc "I didn't know you did yoga."
        sis "It's... A new thing."
        mc "And you like it?"
        sis "Yeah... I guess it's ok..."
        sis "[sf_name] did her Tai Chi thing and... We came back home."
        sis "We took a shower."

        if sf_love_path == True:

            sis "She told me about the things you did last night."
            mc "How did you feel about that?"
            sis "Sad."
            sis "And guilty."
            sis "I don't like lying to her."
            mc "I understand that."

        scene ep5_sc23_lr_20
        off "One little peck after another, she relaxes completely."
        off "Her voice sounds tired and distant."
        off "She keeps talking but she seems to be gone into a dream."

        sis "Then [sf_name] got busy cooking breakfast and I received a call from your mom."
        sis "She was worried we wouldn't get along."
        sis "I told her we were ok."
        sis "I think she believed me."
        sis "Then we talked about the storm and I joined you for breakfast."
        mc "We didn't go out tonight as we talked about this morning."
        sis "Yeah... it's no big deal... We'll go out another day I guess."
        mc "As soon as our problems are over."
        sis "Yeah... Then [sf_name] and I went to my room."
        scene ep5_sc23_lr_21
        off "I softly grab her left breast and fondle it."
        off "She lets out a faint moan and takes a deep breath before continuing."

        if sf_love_path == True:

            sis "She talked a lot about you..."
            if ep5sftruelove == True:

                sis "That you love each other..."
                sis "That she can't stop thinking about you..."
            else:

                sis "That she's falling for you but she still has some doubts..."
        else:
            sis "We talked about clothes and stuff..."
            sis "She's reading a new book..."

        sis "I wanted to... write things in my diary so she left me alone."
        mc "I remember you writing in your diary, a long time ago."
        mc "You're still doing that."
        sis "Yeah..."
        mc "What are you writing about ?"
        off "She looks away."
        sis "Everything..."
        mc "Are you writing about me?"
        sis "Maybe..."
        off "She seems a bit reluctant to talk about her diary...."
        off "It's her most private space..."
        off "I shouldn't annoy her with that."
        mc "Writing these things... It's very important for you, am I right?"
        off "She nods."
        mc "I'm sure you have a lot of things to consign."
        mc "After that, you moved to the pool, right?"
        sis "Yes, and you joined us shortly after."
        mc "And we hugged. It was nice isn't it?"
        scene ep5_sc23_lr_22
        off "I gently move her right arm and claim her breast for myself."
        off "I play with her nipple."
        off "Her breasts are unreal."
        off "Hard and soft at the same time."
        off "She moans."
        sis "Yeah... I liked it..."
        mc "What about Kelly?"
        mc "How did you feel when you saw her in the living room?"
        sis "I was surprised. And a bit upset."
        mc "I could see that."
        mc "But you changed your mind about her, didn't you?"
        mc "As the afternoon went by?"
        sis "It... It wasn't about what she told us... it was about her."
        sis "I didn't want to acknowledge it but I believed her right from the start."
        sis "What annoyed me was to see her so miserable."
        sis "I really wanted to hate her, you know... but seeing her like that... I just wanted to hug her and comfort her."
        sis "And that made me so angry with myself."
        sis "I think I've known for a long time already that... she isn't the evil mastermind I thought she was."
        sis "But it was easier to hate her than to hate the whole world."
        sis "Or myself."
        scene ep5_sc23_lr_23
        off "She trusts me enough to freely speak to me about her feelings."
        off "That's quite magical."
        off "Did she even talk about that to [sf_name]?"
        mc "So your anger tonight...?"
        sis "I just wanted her to stop apologizing."
        sis "She has already paid enough."
        mc "And so... You're friends now?"
        sis "I don't know... It seemed like the best thing to do."
        sis "She was longing for it... And it felt good to give her that."
        sis "Forgiving her, and trying to befriend her..."
        sis "It was like if three years of pain were lifted from my shoulders..."
        sis "Just like when I decided to forgive you."
        off "A couple of tears run down her eyes."
        off "She quickly dispatches them with the back of her fingers."
        off "She forgave me."
        off "I tighten my embrace on her."
        scene ep5_sc23_lr_24
        off "My fingers stroke her clitoris."
        off "Her breathing accelerates and becomes chaotic."
        mc "And what about Jane ?"
        sis "It's a weird one. And she's crazy."
        sis "She likes Steve, a lot."
        sis "I know it's strange to say that after... what happened tonight..."
        sis "But I feel that she's responsible and reliable."
        sis "And she already thinks of us as friends..."
        mc "So... that conversation the four of you had... was it nice?"
        scene ep5_sc23_lr_25
        off "I put a bit more strength in caressing her pussy."
        off "One of my fingers slides between her lips."
        off "She lets out a more intense groan but doesn't react more than that."
        off "She's completely relaxed and welcomes anything I could do to her."
        sis "I... I promised not to tell you..."
        mc "I know about that oath already."
        mc "I just want to know how it felt to you."
        mc "Was it really like... Four friends having fun together?"
        mc "Did you share a good laugh?"
        mc "Did it feel good ?"
        sis "Yeah... We all laughed..."
        sis "Kelly had a hard time to adjust at first... but she got up to speed in the end."
        sis "We all had fun."
        mc "That sounds great. I'm happy to know that you have friends and that you have fun with them, Princess."
        off "A faint but genuine smile stretches on her lips."
        off "It quickly disappears."
        scene ep5_sc23_lr_26
        off "I get my fingers back and suck on them for a couple of seconds."
        off "Her juices are delicious."
        off "She slowly emerges from her ecstasy."


        if sf_love_path == True and ep5sftruelove == True:

            scene ep5_sc23_lr_27
            sis "I heard you. With [sf_name]."
            off "Of course, you did."
            mc "I suspected as much."
            mc "I was about to tell you about it."
            sis "You... Did it with her..."
            mc "Yes. Does that bother you?"
            sis "I don't think so. Are you going to choose her?"

            menu:
                "No. [sisSubPath]":
                    $ ep5subchooseno = True
                    mc "No, Princess, I've already told you."
                    mc "I love you both, but if I have to choose, I'll choose you."
                    mc "We'll be together forever."
                    mc "I promised you."
                "I'll choose whoever I want.":

                    $ ep5subchoosewhoever = True
                    mc "But whatever happens, I won't abandon you."
                    mc "I'll take care of you, one way or another."
                    mc "You know that right?"
                "I won't choose. [blue]\[HaremPath?\]":

                    $ ep5subchooseboth = True
                    mc "I'll have you both."
                    mc "Is that a problem for you ?"
                    off "She takes some time to reply but I don't sense any hesitation."
                    off "She sounds resolved."
                    sis "No... but..."

            sis "She will find out... I don't want to hurt her."
            off "Her concern is not feigned."
            off "[sf_name] is the only thing that is important to her."
            scene ep5_sc23_lr_28
            mc "I don't want to hurt her either."
            mc "So... We'll have to do our best to keep our thing a secret."
            mc "We shouldn't take any risks..."
            mc "We're crazy to do things like that, here in the living room but I just couldn't resist you."
            mc "Next time we'll go somewhere with a locked door..."
            off "She shyly nods a yes."
            mc "There's something else."
            off "She looks at me without saying a word."
            off "I observe her expression with attention, I don't want to miss her reaction."
            mc "She told me about you two."
            off "She wonders what I'm talking about for a few seconds before realizing."
            off "Her expression gradually decomposes into shame and panic."
            sis "It's not what you think! We're not..."
            mc "Shhhh... I know... It's ok Princess."
            mc "She already told me."
            mc "You're just helping each other, right?"
            mc "Besides... There's nothing wrong with that."
            mc "You're both free to do whatever you want."
            mc "No one can judge you."
            off "She calms down."
            sis "Really?"
            mc "Yeah. Really."
            mc "I wanted you to know that I think it's great that the two of you are so close that you can take care of each other like that."
            mc "I'm happy for you."
            sis "Ok..."

        off "I'm hard as a rock."
        off "I'll need to do something about it soon."
        scene ep5_sc23_lr_29
        off "I tighten my hold on her and lick her ear."
        off "She shivers."
        mc "I'm proud of you, Princess."
        mc "You deserve a reward."
        mc "I'm about to lick your pussy."
        mc "But I wonder... Maybe there's something else you would like?"
        mc "Something else you would prefer?"
        mc "Maybe you want me inside you?"
        sis "Licking will do! Please! Please !"
        mc "Let's get to work then."
        off "I briefly think of laying her on the sofa but I change my mind."
        off "We stand up and I move the coffee table."
        off "I knock over the books and knick-knacks that clutter it up."
        off "I make her lay on it."
        off "My cock ridiculously distorts my shorts."
        off "It's time to remove my clothes."
        scene ep5_sc23_lr_30
        off "I proudly stand before her and show her the goods."
        off "She ogles my dick."
        off "I can't say if she's terrified or impatient."
        off "I get between her legs."
        off "[sis_name] tenses up."
        off "Her breathing intensifies."
        mc "You're so beautiful, Princess... It's impossible to resist you."
        off "I get on my knees and give her the tongue."
        scene ep5_sc23_lr_31
        off "She groans."
        off "I caress her ass and thighs."
        off "I can feel her shiver under my fingers."
        mc "Your pussy is delicious. You make me crazy."
        off "She doesn't bother replying."
        off "Her head hangs on the other side of the table."
        off "She tries to muffle her moans with both her hands."
        off "Making her come is easy."
        off "I don't know why but as soon as we touch each other there's some kind of weird alchemy that kicks in."
        off "I've barely given her a few laps that she's about to explode in my mouth."
        off "She drips on the table and the carpet."
        off "And it goes both ways."
        scene ep5_sc23_lr_32
        off "I haven't touched myself and I feel like I could unload any moments now."
        off "Her scent, her taste, her warmth, everything in her makes me go crazy."
        off "I never thought that I would enjoy eating a pussy so much."
        off "Is it because of the taboo?"
        off "Our circumstances add some spice, I have no doubt about it."
        off "Her legs start convulsing on my back."
        scene ep5_sc23_lr_33
        sis "Haaaaaaaaannnnn!"
        off "I keep licking for a minute while the shaking subsides."
        mc "How is it, Princess?"
        off "She looks exhausted."
        off "I get closer and slowly rub my shaft against her lips."
        scene ep5_sc23_lr_34
        off "She rises on her elbows."
        off "She's afraid."
        off "She probably thinks that I'm going to shove it inside her."
        off "I expect her to protest."
        off "She will probably offer to suck on my dick rather than letting me penetrate her."
        off "She doesn't utter a word."
        off "Wide opened, her eyes are locked on my cock."
        off "She breathes fast and loud."
        off "She thinks about it."
        off "She considers it very seriously."
        off "Time stands still."
        scene ep5_sc23_lr_35
        off "And she bursts into tears."
        sis "I'm a slut!"
        sis "Why am I such a slut?"
        sis "I don't understand!"
        sis "Why do I want it so much?"
        sis "I can't think of anything else."
        sis "As soon as we're in the same room ... I can feel your eyes on me."
        sis "I want you to do all these things to me..."
        sis "I can't deal with it anymore..."
        sis "Why? I'm not supposed to..."
        scene ep5_sc23_lr_36
        off "I bend over her and caress her cheeks."
        mc "Shhh..."
        sis "I can't stop thinking about it..."
        sis "I imagine it over and over..."
        sis "I dream about it!"
        mc "It's alright Princess."
        mc "You're not a slut."
        mc "You're my precious little princess."
        mc "You just want to be happy."
        mc "It's perfectly fine."
        mc "We both want it."
        sis "I want it so much!"
        sis "What is wrong with me?"
        mc "Nothing. There's nothing wrong with you."
        mc "You have the right to be happy."
        mc "Why would that make you a slut?"
        sis "I don't... The things I want you to do to me..."
        sis "It's so wrong!"
        sis "You could shove my head into the ground and fuck me in front of everyone... I would be ok with it!"
        sis "I'm going crazy!"
        sis "I don't know how to deal with that anymore!"
        scene ep5_sc23_lr_37
        mc "Shhh... It's okay, Princess."
        mc "You don't have to torture yourself like that."
        mc "We'll take care of that together."
        mc "I'm here for you."
        mc "I'll handle this."
        sis "I can't resist it anymore..."
        mc "Then embrace it."
        mc "You will feel better."
        mc "I promise."
        off "She hesitates."
        off "She probes my gaze in search of a reason to trust me or to reject me."
        off "We look at each other for a few seconds."
        off "And she nods."
        off "I wipe her tears and kiss her forehead."
        off "I make her move to a more comfortable position and put a cushion under her head."
        scene ep5_sc23_lr_38
        off "I join her on the table and look at her from between her legs."
        off "Why did I choose the table? That's so dumb..."
        mc "If you want me to stop, if it hurts, if you changed your mind, anything... just say it. Do you understand?"
        off "She nods again."
        off "This is it. We're doing it."
        scene ep5_sc23_lr_39
        off "She hides her face under her arms as I bring my glans between her pussy."
        off "I've barely touched her that my dick twitches in my hand."
        off "I won't last long."
        scene ep5_sc23_lr_40
        off "I push it in."
        off "Her whole body tenses up and she arches."
        off "Her mouth opens and she takes one last and brutal inspiration before she completely loses her breath."
        off "Holy shit. That's it. I entered her."
        off "I can't believe that she's letting me do this."
        off "I can't believe that she wants this."
        off "She doesn't make a single sound as I penetrate her further."
        off "Holding her hips, I go fully in with one long and slow swoop."
        off "Her insides grip me tightly."
        off "Even though I barely move, her muscles stroke me on their own."
        off "I could come just by being inside her."
        scene ep5_sc23_lr_41
        mc "Are you okay? Breathe, Princess. Breathe!"
        off "She finally lets out a moan before breathing again."
        off "I gently start pumping."
        off "My hands are locked on her hips and waist."
        off "I try to give her everything I have, nice and slow."
        off "I focus on not ruining everything by ejaculating too soon."
        scene ep5_sc23_lr_42
        mc "You're so tight."
        mc "Your pussy is just like you, Princess, It's perfect..."
        sis "Mhmm!"
        mc "It's like it has been made for me."
        mc "You have been made for me."
        mc "We've been made for each other."
        mc "Don't you think so ?"
        sis "Yeaaaah.."
        mc "Loving you is even better than I thought it would be."
        scene ep5_sc23_lr_43
        sis "Haaaaaan !"
        off "She breathes and groans in rhythm with my thrusts."
        off "With her face hidden, I briefly wonder if she groans in pain or pleasure."
        off "Maybe a bit of both."
        scene ep5_sc23_lr_44
        off "I'm not going to last more than a couple of minutes, I can feel it."
        off "She's way too stimulating."
        off "It's like if her insides were milking my dick."
        off "Shit, I'll have to work on my endurance."

        if sf_dom_path == True and ep5domstayed == True:

            scene ep5_sc23_lr_45
            off "And that's when I see her."
            off "[sf_name]."
            off "Looking at us from the entrance of the room."
            off "Cold sweat runs down my spine."
            off "I don't know what to do."
            off "I'm balls deep inside [sis_name] and for a second, my hips stop working."
            off "My brain goes blank."
            off "What to do? What to say?"
            off "She looks... Sad... and also envious... maybe even aroused."
            off "No, I'm probably imagining it."
            off "She lowers her head and leaves."
            scene ep5_sc23_lr_46
            off "I'm so confused."
            off "Was that even real?"
            off "[sis_name] moans bring me back to her."
            off "They are getting out of hands."
        else:

            off "Her moans are not helping."

        scene ep5_sc23_lr_47
        off "She covers her mouth to muffle her groans."
        off "The shaking starts with her legs but after a couple of seconds, her whole body trembles chaotically. Her orgasm hits her hard."
        sis "MMMMMMMMMhhhhhhhhmmmmmm!"
        off "I can feel her vagina contracting around my shaft."
        off "She's literally squeezing my dick inside her."
        off "Her pleasure is too much for me to handle."
        off "I intended to pull out but I just can't."
        scene ep5_sc23_lr_48
        mc "Holy shiiiiiiit! HAAAAAAAARRRRRRWWWWNNNN!"
        off "I try to give her a couple more shags but my hips start shaking too."
        off "The surge of pleasure strikes me so hard that I fall on top of her."
        off "I can feel the semen rushing through my dick."
        off "Shoved deep inside her, I fill her."
        off "The spasms of her vagina are sucking me dry."
        scene ep5_sc23_lr_49
        off "My balls give her everything I have in stock and then try to give her some more."
        off "I ejaculate so hard and so long that my testicles hurt."
        off "She still trembles and softly moans."
        off "Her pleasure ripples through me."
        off "I'm sure that it would be incredible if we were to go another round."
        off "It takes me a minute to realize what I've just done."
        off "I came inside [sis_name]."
        scene ep5_sc23_lr_50

        if sf_love_path == True and ep5sftruelove == True:

            off "I can't believe that I pulled the same bullshit twice in the same night."
            off "And this time it's my childhood friend."

        off "I'm so fucking dumb."
        off "What the hell is wrong with me?"
        off "Cold sweat runs down my spine."
        off "My dick goes limp faster than my dignity can cope with."
        mc "Tell me you're on the pill, Princess."
        mc "Please."
        off "She nods a yes."
        mc "Thank god."

        off "I pull out my flaccid penis from her vagina."
        off "She gasps in surprises."
        scene ep5_sc23_lr_51
        mc "I'm sorry Princess, I couldn't last longer."
        mc "But I promise I'll do better next time."
        off "She doesn't reply."
        off "Her eyes half-closed, and her breathing still messy, she seems to have reached her limits."
        off "I know that her orgasms leave her unable to move for a few minutes."
        scene ep5_sc23_lr_52
        off "I give her a little kiss before I lift her from the table."
        off "She huddles against my chest, frail and vulnerable."
        off "She relies on me entirely. "
        mc "Are you ok?"
        off "She nods with difficulty."
        off "I gently kiss her cheeks and forehead."
        mc "How was it?"
        off "She looks away."
        off "Her voice is barely more than a whisper."
        sis "It hurt a bit... but it was ok..."
        mc "Oh, Princess, you should have told me."
        mc "I would have stopped."
        mc "Or at least slowed down."
        sis "I'm fine..."
        scene ep5_sc23_lr_53
        off "I'm about to enter the hallway when it comes to my mind that I should have put my shorts back, and dressed [sis_name] up a bit more."
        off "But I don't care."
        off "We just had sex in the living room."
        off "I guess that walking naked across the house isn't such a big risk in comparison."
        mc "So you didn't enjoy it?"
        off "Her breathing speeds up a bit."
        off "She takes a few seconds to reply."
        sis "I enjoyed it. I liked it."
        off "She seems about to cry again."
        mc "Shhh, Princess, it's alright."
        mc "Why would you cry? It was beautiful."
        sis "Because it's wrong..."
        mc "Sometimes, fate plays little tricks on us."
        mc "We're made for each other."
        mc "When I was inside you, it was obvious."
        mc "I know you felt it too."
        mc "That's the only thing that matter."
        mc "We don't care about what others think of us."
        mc "We have each other, forever."
        $ renpy.end_replay()
        scene ep5_sc23_sr_01
        off "She doesn't reply but I know that my words satisfied her."
        off "Together, forever."
        off "I guess that's love."
        off "Weird and twisted, but love nonetheless."
        off "I want to do her more and more, but she needs to sleep."
        off "I have completely broken her. "
        off "I put her in her bed and kiss her goodnight."
        off "She kisses me back. "
        scene black with dissolve
        with Pause(1)
        scene ep5_sc23_lr_54 with dissolve
        off "I take care of our clothes in the living room and tidy up the place a bit."
        off "My semen has dripped from her pussy to the floor all the way from the living room to her bedroom."
        off "Cleaning up everything I slowly realize..."
        off "I had sex with [sis_name]... I had sex with my father's ward..."
        off "Shouldn't I feel bad about it?"
        off "Instead, I feel like it's the best and rightest thing I've done in my whole life."
        off "I don't regret it one second."
        off "I'm just thinking of doing it again and better."
        off "Something is wrong with me."
        off "Something is wrong with us."
        off "But I don't care."

        if sf_dom_path == True and ep5domstayed == True:
            scene ep5_sc23_mcr_02
            off "What about [sf_name]?"
            off "That was so weird."
            off "She didn't say a word."
            off "Was she even there?"
            off "Was she real?"
            off "Did I dream of her watching us?"
            off "Should I go see her?"
            off "No, that's probably not the time for that."
            off "I'd better wait till tomorrow to speak with her..."
            off "But what am I going to say?"

        if sf_love_path == True and ep5sftruelove == True:
            scene ep5_sc23_mbr_02
            off "[sf_name] hasn't moved a bit."
            off "I look at her sleeping."
            off "She looks like an angel."
            off "Why did I do that?"
            off "I'm a scumbag."
            off "I lay on the bed and wrap my arms around her."
            off "I can't keep that thing going on forever."
            off "I have to do something."
            off "I don't know what, but I have to do something."
    else:

        off "I don't waste any time talking."
        scene ep5_sc23_lr_56
        off "I immediately remove my shorts and stand proudly before her."
        off "Her expression is priceless."
        scene ep5_sc23_lr_55
        sis "What... ?"
        mc "Yeah, what are you waiting for?"
        off "She looks behind me."
        sis "Someone could..."
        mc "Kelly and [sf_name] are sleeping."
        mc "And even if they are not, they're on the other side of the house with hallways and doors between us."
        mc "There's no way they hear us."
        mc "Unless we start being very loud."
        mc "But maybe you want us to be loud."
        mc "Do you think I can make you moan loud enough to wake up [sf_name]?"
        mc "Perhaps you would enjoy some voyeurs while I lick your pussy?"
        mc "That's it."
        mc "Do you want Kelly to watch us while I fuck you?"
        sis "You're crazy!"
        mc "Then get to it quietly."
        off "She hesitates a few second."
        scene ep5_sc23_lr_57
        off "She looks away as she reaches out her hand and grabs my still flaccid cock."
        mc "You see? It's not that difficult."
        off "She strokes my dick for a few seconds until it gets decently hard."
        scene ep5_sc23_lr_58
        off "She takes the tip of my cock in her mouth."
        off "She doesn't seem to mind but doesn't look as though she's enjoying it either."
        mc "Come on Princess."
        mc "Put some spirit into it."
        mc "I know you can do better than that. "
        scene ep5_sc23_lr_59
        off "Her tongue swirls around my glans."
        off "She starts working on it more seriously."
        off "She takes it deeper, and the suction gets more intense."
        mc "That's it, Princess."
        mc "Just like that."
        mc "Oooh, yeah that's nice."
        scene ep5_sc23_lr_60
        off "She plays with my balls a bit."
        off "That's new."
        off "She takes some initiative to please me."
        off "I like that."
        scene ep5_sc23_lr_61
        off "Damn, she's actually good at it."
        off "I'm not going to last long."
        mc "You're doing great, Princess, but don't make me come."
        mc "I need that juice to fill up your pussy."
        off "She suddenly lets go of my cock."
        scene ep5_sc23_lr_62
        sis "Please no, I can't, [mc_name]."
        sis "Please... I'll suck you as much as you want but ... Not my pussy, please."
        sis "Anything but that."

        if sf_dom_path == False:

            off "She’s terrified."
            off "She's not faking that."
            mc "It's ok, Princess, I understand. I know you want it, deep down. But I can give you more time. You don't have to be scared of me."
            scene ep5_sc23_lr_63
            off "I slowly caress her cute little face."
            mc "I've told you that you can trust me, haven't I?"
            off "She nods."
            mc "Great. Remove your panties."
            off "She hesitates but complies."
            scene ep5_sc23_lr_64
            off "I grab her legs and make her lay on her back."
            mc "Do you know what we're doing here?"
            mc "I will never hurt you, Princess."
            mc "We're pretending that I force you to do things against your will."
            mc "So that you can indulge in those things with the excuse of having said no."
            off "She's still a bit stiff and worried."
            scene ep5_sc23_lr_65
            off "I continue talking as I push the coffee table aside and kneel between her thighs."
            mc "You want to do these things, but you can't admit it to yourself."
            mc "So I'm helping you."
            mc "That means that even if you say no, I may still try to push further."
            mc "Sometime you will like it, sometimes you won't."
            mc "That's why we need a safe word."
            sis "A safe word?"
            scene ep5_sc23_lr_66
            off "I bend over her pussy and smell her perfume."
            off "God, I like it."
            off "I know it's weird and probably disgusting, but I like it."
            mc "Yes, something you can say when you really want me to stop."
            mc "If you say no, I will push further."
            mc "If you say that word, I'll stop immediately."
            mc "No questions asked."
            mc "I don't want to take the risk of misunderstanding you and going too far."
            scene ep5_sc23_lr_67
            off "I brush her clitoris with the tip of my tongue."
            off "She moans lightly."

            sis "Ok...."
            off "Her body begins to relax."
            off "I should have thought of that safe word thing sooner."
            mc "What do you think of... Vegetables?"
            sis "What ?"
            mc "As a safe word. Would that work for you?"
            off "I suck on her clitoris."
            sis "Mhhhhm! Yeaaaah! It'll work ! Haaaaaan!"
            scene ep5_sc23_lr_68
            mc "Alright then."
            mc "Now, Princess, I want you to be absolutely honest for a few seconds."
            mc "Tell me. Do you want me to lick your pussy?"
            off "She doesn't look away, doesn't gasp in surprise."
            off "She just nods. Yes."
            mc "Then I'm listening. Ask for it."
            sis "Would you... lick my pussy, please?"
            scene ep5_sc23_lr_69
            off "There isn't a trace of hesitation in her voice."
            off "Some embarrassment and probably some shame, but she didn't lose a second thinking about it."
            off "She wants it and she requests it."
            off "Let's give her the satisfaction."
            off "Working her pussy is easy."
            scene ep5_sc23_lr_70
            off "I lick her a couple of minutes and she's already about to come."
            off "There's some kind of electricity between us that makes it simple."
            off "I take advantage of this."
            off "The more pleasure I give her, the more pleasure she'll want from me."
            off "She suddenly tenses up."
            scene ep5_sc23_lr_71
            off "She gags herself with both hands to muffle her moaning."
            off "The shaking starts a few seconds later."
            off "That's her thing."
            off "When she orgasms, she loses control of her legs and it leaves her exhausted."
            off "I like that."
            mc "Do you feel better Princess?"
            scene ep5_sc23_lr_72
            off "I slowly work my shaft as I talk."
            off "My glans is only a few centimetres from her pussy."
            off "It's so tempting..."
            mc "You look like you enjoyed that."
            mc "How was it?"
            off "She looks completely destroyed."
            off "She moans something."
            mc "I didn't understand."
            mc "Could you repeat that?"
            sis "It was great..."
            off "She sounds tired and ashamed."
            mc "And that was just my tongue."
            mc "Imagine what you will feel with my whole cock tearing you apart..."
            off "She's beautiful and vulnerable."
            off "Despite what we just did, she looks innocent."
            off "I want to defile her."
            mc "Grab your legs."
            mc "Show me your pussy."
            mc "I want to look at it while I jerk off."
            scene ep5_sc23_lr_73
            off "She moves her hips and lifts her thighs, offering me a perfect view of her intimate parts."
            off "I'm going to fuck this pussy soon."
            off "I just have to be a bit more patient."
            off "Tomorrow? Yeah, maybe."
            off "I feel like each day, each time I lick her pussy, each orgasm I give her, brings me closer to plunging my cock inside her."
            mc "Look at my cock, Princess."
            scene ep5_sc23_lr_74
            mc "Imagine it going inside you."
            mc "It's okay, I know you're still afraid of it."
            mc "But you will like it, I promise."
            mc "You will love having me inside you."
            off "I don't understand her."
            off "She refused me, but she ogles my dick with an evident desire."
            off "She's aroused."
            off "And it's not because of the pleasure I gave her a few minutes ago."
            off "Her mouth opened, she breathes loudly."
            off "I'm about to come."
            mc "Open your pussy for me, I want to see your insides."
            scene ep5_sc23_lr_75
            mc "Yeah, just like that."
            scene ep5_sc23_lr_76
            mc "It's perfect."
            mc "Oh, Princess, you're so beautiful... Haaaaaan!"
            off "I ejaculate."
            scene ep5_sc23_lr_77
            off "I aim for her vagina and I'm right on target."
            off "I let go of several long sperm lines."
            off "I put as much on her as inside her."
            scene ep5_sc23_lr_78
            off "I keep looking at the mess I just did long after I finished emptying my balls."
            off "I slowly realize what I've done."
            off "I came inside her."
            scene ep5_sc23_lr_79
            off "It's just at the entrance, though."
            off "It should be ok."
            off "I hope..."
            off "I'm going flaccid at light speed anyway."
            scene ep5_sc23_lr_80
            mc "Tell me you're on the pill."
            off "She doesn't reply."
            off "She keeps looking at her pussy covered in cum."
            off "She's visibly in shock."
            scene ep5_sc23_lr_81
            mc "Princess. Are you on the pill?"
            off "I finally get her attention."
            off "She nods."
            mc "Great."
            off "I put my shorts back on and head toward the exit."
            mc "Clean up and go get some sleep."
            mc "Tomorrow will be intense."
            scene ep5_sc23_lr_82
            off "She looks at me with confusion."
            off "She hasn't moved a bit nor said a word."
            off "She's still holding her pussy as I leave the room."
            off "She seems completely lost."
            off "I leave the room as fast as I can."
            off "I feel a bit bad about what I just did and I'm basically fleeing."
            off "I'm sure she'll be ok, though."
            off "It's just a few drops of semen."
            off "It may even convince her to accept some more... Decisive action."

            if sf_love_path == True and ep5sftruelove == True:
                scene ep5_sc23_mbr_02
                off "[sf_name] hasn't moved a bit."
                off "I look at her sleeping."
                off "She looks like an angel."
                off "I had some second thoughts before joining [sis_name], but now I don't even feel bad about it."
                off "I know I should."
                off "But I don't."
                off "I lay on the bed and wrap my arms around her."
                off "I'm sure I can keep things going like that."
                off "If I'm careful enough, I can fuck [sis_name] on the side without [sf_name] noticing anything."
                off "It'll be alright."

        if sf_dom_path == True:
            label galleryScene12:
            off "Did she just refuse me?"
            mc "Are you serious?"
            mc "How much longer will you make me wait, Princess ?"
            sis "I can't, I'm sorry... Please..."
            mc "Are you toying with me?"
            mc "You're teasing me and you think I'm gonna wait until Christmas or something?"
            scene ep5_sc23_lr_83
            off "She starts crying."
            off "She's scared of me."
            off "Maybe I'm going too far."
            sis "I... I'm sorry... I didn't tease you..."
            sis "[mc_name], please... I don't want to do that."
            mc "You're not making it easy for me, Princess."
            sis "We can't do that [mc_name].... Please..."
            mc "Yeah, enough."
            mc "I heard you."
            mc "Anything but that..."
            off "No pussy tonight I guess."
            mc "Show me your ass."
            scene ep5_sc23_lr_84
            off "She tries to wipe her tears and looks at me bewildered."
            mc "Show me your ass!"
            mc "Lose your panties and show me your ass!"
            off "She lowers her head and obeys reluctantly."
            off "She stands up and turns her back to me as she strips."
            off "I guide her back to the sofa and makes her kneel on it."
            mc "You truly have an amazing ass, Princess."
            scene ep5_sc23_lr_85
            off "I grope and spread her ass cheeks."
            off "Her pussy is just there, a few centimetres away from my cock."
            off "How would she react if I was to plunge inside her?"
            off "I'm sure she won't be so defiant once I'll be in her."
            off "Ok, calm down [mc_name]."
            off "She said no."
            off "If you stick it in, it's called rape."
            off "Shit, she makes me crazy."
            off "I have to control myself."
            sis "[mc_name] please...."
            mc "It's ok Princess."
            sis "Please, I can take you in my mouth..."
            sis "I'll swallow... But not that..."
            mc "Relax."
            mc "I'm not going to fuck your pussy."
            mc "Trust me."
            scene ep5_sc23_lr_86
            off "I slide my dick between her legs and start grinding on her like we did last night."
            off "I fuck her thighs for a few minutes."
            off "She lets out a few soft and embarrassed moans."
            off "But I'm not enjoying this as much as I should."
            off "I slowly understand that I won't get off from this."
            off "I need to fuck her."
            off "That's the only way."
            off "If I can't fuck her pussy... maybe I can fuck something else."
            scene ep5_sc23_lr_87
            off "I grab my cock and bring my glans to her butt hole."
            mc "I'm going to fuck your ass."
            off "Her reaction is instantaneous."
            sis "No! Please! Not that!"
            sis "Please! You're going to hurt me!"
            sis "Please! I don't want you inside me!"
            scene ep5_sc23_lr_88
            off "She twists to turn around and push me away."
            off "She's terrified."
            mc "You can't leave me like that Princess!"
            mc "It's either that or your pussy, you choose!"
            sis "No, please! No !"
            off "The lights suddenly switch on."
            scene ep5_sc23_lr_89
            sf "I believe she's being clear. Asshole."
            off "[sis_name] is already on her feet, fleeing from me."
            off "That voice...."
            off "Holy shit ..."
            off "She's going to murder me."
            mc "[sf_name]!"
            mc "I... It's not what it looks like..."
            mc "[sis_name], please, can you tell her..."
            scene ep5_sc23_lr_90
            off "She gets closer. [sis_name] hides behind her."
            sf "Tell me what, [mc_name]?"
            sf "That you were about to abuse her?"
            mc "No, no, it was... It was kind of a prank..."
            sf "A prank... Really..."
            scene ep5_sc23_lr_91
            off "I don't even see the slap coming."
            off "It's violent enough to send me sprawling on the sofa."
            off "I feel like my jaw has exploded."
            off "How come she has so much strength?"
            off "[sf_name] turns to [sis_name] and gives her a few instructions."
            sf "Go to my room and bring me the purple one."
            sf "It's in my bag, in the bathroom."
            scene ep5_sc23_lr_92
            off "[sis_name] runs out of the room."
            off "I stand up and try to plead my case."
            mc "[sf_name]... I swear, I never intended to go further... I wasn't..."
            sf "Shut up."
            sf "You don't have any right to talk."
            sf "We'll tell you when you can open your filthy mouth."
            sf "Do you understand?"
            off "Her voice is harsh and full of anger."
            off "Her authority is overwhelming."
            off "I feel like she could crush me just with her words."
            mc "Please, maybe I've gone too far but..."
            scene ep5_sc23_lr_93
            off "She takes a step towards me and the second slap hits even harder than the first one."
            off "I’m back on the sofa."
            sf "I don't like to repeat myself, [mc_name]."
            sf "Do you understand?"
            off "I can't help but nod a yes."
            off "My cheek burns."
            off "My whole face hurts like hell."
            scene ep5_sc23_lr_94
            off "[sis_name] comes back running."
            off "Oh my god."
            scene ep5_sc23_lr_95
            off "What is that?"
            sf "Thank you, sweetie."
            off "That thing is massive."
            sf "Kneel. There."
            off "[sf_name] shows me the place where I asked [sis_name] to settle just a moment ago."
            off "I feel like my life depends on what will happen in the next few minutes."
            scene ep5_sc23_lr_96
            off "I obey and hide my face in my arms in shame."
            off "I know what's coming for me."
            off "My heart beats so hard that I can almost hear it."
            off "She's going to annihilate my asshole."
            off "Do I deserve that?"
            off "Did I really fuck up that much?"
            off "My God, she wears that thing like a dick."
            off "She's going to destroy my ass."
            off "She goes behind my back."
            off "How the hell could this turn into such a shit show?"
            sf "You're the worst, [mc_name]."
            sf "Did you think it was ok to force her?"
            off "She's going to crush me."
            off "But the worst is that she's going to do that in front of [sis_name]."
            mc "[sis_name], please!"
            mc "You know I wouldn't have done it!"
            mc "I swear! I was just messing with you !"
            off "I'm the one begging now."
            off "I’m fucking pathetic."
            off "I should stand up and defend myself... but I won’t."
            off "Deep down, I know that I’ll just submit."
            off "Maybe I want it."
            off "[sis_name] looks at me without saying a word."
            off "Her face is still wearing that mask of fear and pain I inflicted on her."
            scene ep5_sc23_lr_97
            off "I'm still hopelessly pleading my case when the rubber shaft penetrates my anus."
            off "[sf_name] enters me in a single and powerful swing."
            off "The pain is overwhelming."
            off "I'm about to scream but [sf_name] advises me otherwise."
            sf "I wouldn't get too loud if I were you."
            sf "Unless you want Kelly to join the party."
            sf "Take it quietly."
            off "She was here right from the start."
            off "She saw everything."
            off "The previous night, she took care not to hurt me while she sodomized me."
            off "Tonight, her priority is obviously different."
            off "She tears me apart."
            off "Right from the start, she brutally rams into me at full speed."
            off "That thing is massive and hard."
            off "And it goes deep inside me."
            off "My whole ass is burning."
            scene ep5_sc23_lr_98
            sf "That's what you wanted to force her into."
            sf "How is it, [mc_name]?"
            sf "Do you like it?"
            sf "She trusted you, you disgusting piece of shit."
            off "She pumps into me hard."
            off "She doesn't intend to make it last."
            off "I can feel that thing brutalizing my guts."
            off "If she keeps going like that I'm going to puke."
            off "The worst part of it is that despite the pain, my dick is hard as a rock and my balls are on fire."
            off "I'm going to come soon."
            sf "Are you going to apologize?"
            sf "What are you waiting for ?"
            mc "Haaaaaaaaaaaaaaaaan! I'm sorry!"
            mc "Please.... I apologize!"
            mc "I won't... I'll never do it again !"
            scene ep5_sc23_lr_99
            off "My balls suddenly empty themselves on the sofa."
            off "I gasp in pain and pleasure."
            off "The orgasm is violent and disgracing."
            off "I tremble as I unload."
            off "This is so humiliating."
            off "[sf_name] quickly pulls out and grabs me by the hair."
            scene ep5_sc23_lr_100
            off "She throws me on the floor."
            sf "I'm not convinced."
            sf "Kiss her feet."
            sf "Swear you'll never touch her again."
            off "My lower half is still awkwardly shaking from that unwanted orgasm."
            off "Yet, I immediately crawl to [sis_name] and starts kissing her feet."
            mc "I'm sorry. I'll never touch you again!"
            mc "I swear!"
            mc "I'm so sorry, please, forgive me! Please!"
            off "She doesn't say a word and backs away."
            sf "If she ever complains about you, [mc_name], I swear, I will kill you."
            sf "Do you understand ?"
            mc "I swear! I'm sorry!"
            mc "Please, I would never have..."
            sf "Shut up."
            sf "And clean the room."
            sf "Asshole."
            scene ep5_sc23_lr_101
            off "[sf_name] gathers their panties and grabs [sis_name] by the waist as they head out the room."
            sf "I'm so sorry, love."
            sf "I should have understood sooner."
            sf "It's over now...."
            off "I'm left alone, kneeling on the floor."
            off "My ass hurts like hell, my face burns and I've lost all my dignity."
            off "I'm not even sure that I'll be able to walk back to my room."
            off "I can't say I didn't deserve that."
            off "I wouldn't have raped her."
            off "I swear I would have let her go..."
            off "But I did go too far..."
            off "[sf_name] fucked my ass, but I'm the one who fucked my life."

    return

label ep5sc24:
    scene ep5_sc24_lr_01
    off "She gives me a very swift look as I walk towards her."
    off "I like that faint smile on her lips."
    off "I sit next to her and she immediately closes the gap between us."
    scene ep5_sc24_lr_02
    off "She wraps herself with my arm and huddles against me."
    sis "You took your time."
    mc "I'm sorry, I didn't know that you were waiting for me here."
    mc "What are we watching?"
    sis "Spellbound."
    mc "Never heard of it."
    sis "I can't say I'm surprised."
    sis "It's an Alfred Hitchcock movie."
    mc "I know that name."
    mc "Sunday's movie was from him too right?"
    sis "Yeah... they're doing some kind of retrospective..."

    if ep4chosenmovie == "Casablanca":

        scene ep5_sc24_lr_03
        mc "Oh, I know her."
        mc "She was in Casablanca, right?"
        sis "Yeah... That's Ingrid Bergman."
        mc "She's beautiful."
        sis "Yeah..."
        mc "Not as beautiful as you of course."
        off "She giggles."
        sis "I think you're out of your mind."
        mc "It's your fault."
        mc "You're making me crazy."
        off "She laughs again."
        sis "Your pick up lines are lame."
        sis "You won't score with that level of game, my good sir."
        mc "I promise I'll work on it."

    scene ep5_sc24_lr_05
    off "The film isn't really to my liking, but I enjoy the moment."
    off "Sharing these things with her feels good and absolutely right."
    off "She quickly senses my lack of interest in the movie itself, though."
    sis "I've already seen this one."
    sis "We don't have to watch it if you don't want to..."
    mc "I'm totally fine with the movie."
    sis "If you say so..."
    off "I try very hard to focus on the screen, but her intervention wiped clean my desire to concentrate on anything else but her."
    mc "You know Princess, I'm very proud of you."
    sis "Proud?"
    scene ep5_sc24_lr_06
    off "She sounds surprised and turns to me."
    mc "Yes."
    mc "I'm impressed by how you dealt with Kelly."
    mc "You forgave her and even decided to treat her as a friend."
    mc "To be honest, I was sure that you would agree to have her here as a guest for a few days."
    mc "But you've gone way beyond my expectations."
    scene ep5_sc24_lr_07
    sis "Yeah well... I guess I ended up believing her..."
    sis "She's not the bitch she was three years ago..."
    sis "So there was nothing left to hate and no point in holding a grudge..."
    off "That sounds so... Mature..."
    off "I don't know if I would be able to let go of my hatred so easily."
    sis "Do you know what annoyed me the most?"
    sis "That was seeing her so miserable."
    sis "Seeing her like that... I wanted to hug her and comfort her."
    sis "I also wanted to slap her and tell her to pull herself together."
    sis "A bit of both... Anyway... That made me angry with myself."
    sis "I think I've known for a long time already that... she isn't the evil mastermind I thought she was."
    sis "But it was easier to hate her than to hate the whole world."
    sis "Or myself."
    scene ep5_sc24_lr_08
    sis "In the end, I just wanted her to stop apologizing."
    sis "She has already paid enough."
    off "I'm astonished and ashamed."
    off "In her shoes, I'm pretty sure that I would have hated Kelly until the end of times."
    mc "You called her a friend."
    mc "You know what it did to her, right ?"
    sis "Yeah... It seemed like the best thing to do."
    sis "She was longing for it..."
    sis "And it felt good to give her that."
    sis "Forgiving her, and trying to befriend her..."
    scene ep5_sc24_lr_09
    sis "It was like if three years of pain were lifted from my shoulders..."
    sis "Just like when you hugged me, Sunday morning..."
    mc "I should have done it sooner."
    sis "I don't know..."
    sis "Would we be here like this if these three years hadn't happened?"
    scene ep5_sc24_lr_10
    mc "That's some... Intense existential questioning..."
    mc "I guess there's no way to know that for sure."
    off "Yet, I have no doubt that these events changed the way we perceived each other."
    off "Would I have come to imagine [sis_name] in a sexual way if there weren't all these rumours about her?"
    off "Probably not."
    off "I mean... We played husband and wife when we were children..."
    off "And... ok, I thought about it before all that mess..."
    off "But I wasn't serious about it... was I?"
    sis "Yeah..."
    sis "But what about you?"
    sis "How do you feel about having Kelly here ?"
    scene ep5_sc24_lr_11
    off "I sense a subtle change in her tone."
    off "This is a trap."
    off "We were having a nice chat and suddenly, I'm a rabbit running for his life in front of a vicious hunter."
    mc "Well... it's not like we have a choice."
    mc "You know as well as I do that we couldn't let her go back to her home alone."
    mc "It just wouldn't have been right."
    sis "I know that."
    sis "But I felt like you enjoyed her presence here a bit too much."
    off "Holy shit."
    off "Is this jealousy?"
    mc "What are you talking about?"
    scene ep5_sc24_lr_12
    sis "You know exactly what I'm talking about."
    sis "She's very pretty, and she's had a crush on you for some time now..."
    sis "She told us about it..."
    sis "You may want to make a move on her..."
    mc "What? Are you serious?"
    mc "Why would I do that?"
    scene ep5_sc24_lr_13
    sis "As I said... She's cute..."
    mc "Come on, you know I'm not interested."
    mc "You're the only one I want."
    mc "And it has nothing to do with the cuteness."
    mc "It's because it's you."
    off "She gives me a very judgemental look."
    sis "You really have no idea how to talk to a girl."
    sis "You're incredibly bad at this."
    mc "What? Why?"
    sis "You've just told me that Kelly is cuter than me."
    sis "Whatever comes next is of little to no value."
    mc "What? I never said that!"
    sis "You never said anything to the contrary."
    mc "What kind of logic is that?"
    scene ep5_sc24_lr_14
    sis "One that you should understand if you ever want to bed a girl."
    mc "Alright. You're cuter, you're prettier than her."
    sis "That's better."
    mc "And your body is nicer."
    sis "My body?"
    mc "Yeah, your ass is fantastic, your breasts are magnificent, she can't even compare."
    sis "Ok, now you're overdoing it."
    sis "Why do you always have to make it weird..."
    mc "Also, you're the only one who gives me that thrill, when we touch."
    mc "I like how your skin always feels smooth and warm under my fingers."
    mc "Your taste and your perfume are sweet and intoxicating."
    mc "When I hold you in my arms, I am complete."
    scene ep5_sc24_lr_15
    mc "I can't talk about the way I feel when we kiss because there are simply no words to describe it."
    mc "But I have no doubt that it's something unique to us and I'm sure that nothing can come close to it."
    mc "Being with you makes me happy."
    mc "I don't care about anything else."
    mc "I can assure you that Kelly can't beat that."
    mc "No one can."
    scene ep5_sc24_lr_16
    off "She climbs onto me and throws her arms around my neck."
    scene ep5_sc24_lr_17
    sis "I think it's time you finally shut up and kiss me."
    off "That leaves me speechless."
    off "How come she's so bold and assertive?"
    off "Did something happen?"
    scene ep5_sc24_lr_18
    off "Our lips join."
    off "I grab her ass as she leans on me."
    off "She seems ok with it."
    off "I even think that she enjoys it."
    off "Our tongues haven't yet met but my cock is already stiffening."
    off "My shaft rubs against her pussy as it's becoming erect."
    off "Something has changed since last night."
    off "She's way more \"girlfriendly\" than yesterday."
    scene ep5_sc24_lr_19
    sis "A kiss and you're ready to go?"
    mc "I guess I'm easily triggered."
    sis "I can see that..."
    scene ep5_sc24_lr_20
    sis "Do you want me to take care of it?"
    off "What? Really?"
    off "I'm beyond surprised."
    mc "I... Guess that would be great..."
    mc "But you don't have to do it if you don't want to."
    sis "If I propose it, it's that I want it."
    sis "And besides... I feel like you and I have an unfinished business."
    mc "Oh..."
    mc "You want to pick up where we left it this morning?"
    sis "You don't want to?"
    mc "Oh, I want it very much!"
    off "She looks to the hallway for a few seconds."
    off "She evaluates the risks of doing it here, in the living room."
    off "We could get caught."
    off "Like this morning."
    off "She stands up and unexpectedly grabs my shorts and removes them."
    label galleryScene13:
    scene ep5_sc24_lr_21
    off "She then takes care of her own panties."
    off "I'm as hard as a rock."
    off "My head is spinning."
    off "I'm already breathing through my mouth."
    off "Her pussy is so beautiful."
    off "I don't know what has gotten into her to take such a proactive stance, but I like it."
    scene ep5_sc24_lr_22
    off "She gets back on top of me."
    off "She softly rubs her clitoris on my shaft."
    sis "Am I dreaming or is it even bigger than yesterday?"
    mc "You're dreaming."
    off "Holy shit, she teases me so hard."
    off "Does she even know how difficult it is for me to control myself?"
    off "We clumsily find a more or less comfortable position and she sits on my dick, squeezing it between my belly and her pussy."
    off "I can feel she's already wet."
    off "She's as horny as me."
    scene ep5_sc24_lr_23
    sis "Is that ok?"
    sis "You're comfortable?"
    mc "That's perfect. You ?"
    sis "That's great."
    off "She starts moving."
    off "She clutches on my shoulders and grinds against my dick."
    mc "Holy shit, that feels incredible..."
    off "Her pussy is literally wide open, massaging my shaft between her lips."
    off "We're both breathing like animals."
    off "She moves faster and moans."
    off "Her movements get quicker as she tries to cover the whole of my tool."
    off "I feel ballsy and grab her shirt."
    scene ep5_sc24_lr_24
    off "She lets me remove it and I throw it across the room."
    off "We look at each other and I'm about to go for her breasts when my glans suddenly feels funny."
    off "She lets out a little muffled scream and jumps on the side."
    scene ep5_sc24_lr_25
    sis "Oh my God! It came in a bit!"
    mc "Oh crap... Did it hurt?"
    mc "I'm so sorry, I didn't want to..."
    mc "Let me see..."
    sis "It's ok... It was just the tip of your dick..."
    sis "It's just... It surprised me, ok?"
    sis "I'm not hurt."
    mc "Are you sure?"
    mc "Maybe I should kiss it to make sure it heals."
    mc "What do you think?"
    scene ep5_sc24_lr_26
    off "She puts her foot on my face and pushes me away as I try to get my lips to her pussy."
    sis "Is this the moment you chose to make fun of me? Really?"
    mc "I'm sorry..."
    mc "I just wanted to give you a bit of attention..."
    mc "Perhaps I formulated it wrong."
    mc "We can stop there if you want."
    mc "I'll understand."
    off "She looks at me completely bewildered."
    sis "Are you serious?"
    mc "Well..."
    sis "Are you sure you want to have sex with me?"
    sis "Because you sure don't show a lot of interest in it."
    mc "What?"
    mc "Come on, Princess, I'm the guy who rubbed his dick against your sweet little pussy while you were still asleep..."
    mc "Of course, I'm interested in having sex with you."
    mc "I'm dying with impatience."
    mc "I'm just trying to be a good and understanding boyfriend here."
    mc "You told me that you didn't want to... do it yet..."
    mc "If you happened to change your mind, please let me know..."
    scene ep5_sc24_lr_27
    sis "You're a moron."
    sis "I'm afraid."
    sis "That doesn't mean that I don't want to do it."
    mc "Ok... but you..."
    sis "You don't have to be a genius to understand that."
    mc "What are you talking about?"
    mc "Are you saying that I'm supposed to force you?"
    sis "What?"
    sis "Who said anything about forcing anyone?"
    mc "I don't understand where we're going with this discussion..."
    mc "What am I supposed to do?"
    sis "I don't know... Comfort me?"
    sis "Make me less afraid?"
    mc "Didn't I already do that?"
    mc "Come on."
    mc "You know I will never hurt you."
    mc "What more can I say or do?"
    mc "If I'm failing at this, please, help me."
    mc "You know I'm no romance expert..."
    scene ep5_sc24_lr_28
    off "She stares at me for a few seconds before she rises and climbs back on me."
    sis "Yeah, obviously, you're not."
    off "Why are girls so complicated?"
    off "The moment you think you understand them, you fail the most."
    sis "I'm afraid. That doesn't mean I don't want it as much as you."
    off "You've already said that, Princess..."
    off "She grinds on my shaft again."
    scene ep5_sc24_lr_29
    off "Her magnificent breasts are gently jiggling a few centimetres away from my eyes."
    off "I want to suck on those nipples but I hesitate to grope her."
    off "I've just made a speech about trying to be a good boyfriend."
    off "I wonder if it's compatible with being a pervert."
    off "I understand that the mood has changed a bit before I can reach a conclusion on that question."
    off "[sis_name] focuses on my cock appearing and disappearing under her."
    mc "Princess?"
    sis "You don't move, ok ?"
    mc "What?"
    sis "Just let me do it."
    sis "Please."
    off "Do what?"
    scene ep5_sc24_lr_30
    off "She rises and grabs my dick."
    off "She brings my glans to her pussy."
    off "Holy shit."
    mc "Are you sure about this?"
    sis "Will you shut up with your carefulness?"
    sis "It's tiresome."
    off "She breaths loudly and caress her lips with the tip of my dick."
    off "She whispers in my ear."
    sis "Do you love me?"
    sis "Tell me you love me. Please..."
    off "Her voice suddenly seems about to break."
    mc "I love you, Princess."
    mc "I love you."
    mc "You don't have to force yourself."
    sis "Oh, shut up with that!"
    off "She takes a couple of profound breaths and seems to calm down a bit."
    scene ep5_sc24_lr_31
    off "And then she impales herself on me."
    off "Slowly."
    scene ep5_sc24_lr_32
    off "I can feel my glans pressing against her tiny hole and suddenly popping inside her."
    off "She lets out a long and muffled moan as the first centimetres slide inside her."
    off "It's so easy, it feels unreal."
    off "She's ridiculously tight but she's wet enough to smooth out any resistance."
    scene ep5_sc24_lr_33
    off "She marks a pause and starts pumping on my shaft, progressively going deeper and deeper."
    sis "You're so fucking big."
    sis "Why are you so big?"
    sis "Haaaan."
    mc "Well... I wonder why you're so tight also..."
    mc "That feels incredible..."
    mc "Ooh, Shit!"
    off "Her pussy is burning hot."
    off "I can feel her warmth wrapped around my cock."
    scene ep5_sc24_lr_34
    sis "Oh fuck... There's still so much..."
    mc "You don't have to take it all... If you can't..."
    sis "Are you saying I can't?"
    mc "I'm saying that you don't have to hurt yourself."
    sis "Haaaaaaaaaaaaaaan."
    sis "Aren't you a bit too full of yourself right now?"
    mc "You're the one yelling that I'm big!"
    off "I grope her ass as she engulfs my shaft whole."
    sis "Haaaaaaan!"
    sis "I'm not yelling at all!"
    scene ep5_sc24_lr_35
    sis "Ooh, my Gooood!"
    sis "It's all in!"
    sis "Mhhhmmm!"
    off "She starts laughing."
    off "A couple tears run down her cheeks."
    off "She falls on top of me and buries her face in my neck."
    off "Her breathing is brisk and jerky as if she had just run a hundred metres."
    sis "I feel like I won't be able to walk tomorrow."
    sis "You've dislocated my vagina."
    scene ep5_sc24_lr_36
    off "I enfold her in my arms and hold her tight."
    mc "Take it easy, if it hurts..."
    sis "It doesn't hurt much..."
    sis "I can feel you inside me..."
    sis "Up to my stomach..."
    sis "Fuck... You're really stretching me."
    mc "I'm not that big..."
    sis "Seriously... I can't move... Give me a minute."
    mc "You can have all the time you want."
    scene ep5_sc24_lr_37
    off "She doesn't take more than a minute of rest before she slowly starts moving again."
    sis "Oooh. Ooh. Ooooh, my Goood."
    off "My hands knead her ass and run on her hips."
    off "I try to caress as much of her body as I can, but it's extremely difficult to focus."
    off "I struggle not to simply let go and fade away in bliss."
    off "I feel like I could pass out anytime soon."
    off "That and ejaculating."
    off "I have to concentrate hard not to let it all go in a pathetic and premature ejaculation."
    off "She does all the work."
    off "Slowly pumping in and out on my shaft."
    off "She breathes and moans in rhythm with the movements of her hips."
    off "My eyes are locked on her breasts."
    scene ep5_sc24_lr_38
    sis "So... are you going to play with them at some point or what? Haaaan..."
    off "Her question surprises me."
    mc "What?"
    sis "My breasts."
    sis "Mhhhhm..."
    sis "I let you toss my shirt away."
    sis "Oooh, shiit..."
    sis "I expect to get something out of it."
    mc "I..."
    sis "You dummy."
    sis "You're thirty centimetres inside me."
    sis "Mmhhm!"
    sis "Don't tell me you're trying to be a good and understanding boyfriend."
    sis "Haaaannn!"
    off "She's so right."
    off "What the fuck am I waiting for?"
    scene ep5_sc24_lr_39
    off "I grab one of her breasts and kiss the other one."
    off "I hold her tight."
    off "Her body is twitching in my arms."
    off "I suck her nipples and she moans hard in response."
    off "I lick her until my mouth runs dry."
    off "Her boobs are soft and hard at the same time."
    off "They're full and firm."
    off "They're beautiful."
    off "They're perfect."
    off "Just like the rest of her body."
    off "Just like her."
    off "She pushes me back and starts pumping harder and faster."
    scene ep5_sc24_lr_40
    off "She buries my head between her breasts and manages to get some long and ample thrusts, using all my length."
    sis "Holy shiiiiiit. Haaaaaaaan!"
    sis "You're so fucking deep..."
    sis "MMHHHHM!"
    mc "I'm going to come soon, Princess!"
    sis "I'm on the pill! I'm on the pill!"
    off "She almost yelled that."
    off "She wants me to come inside her."
    off "She thrusts harder, and faster."
    off "I can't breathe anymore."
    scene ep5_sc24_lr_41
    off "I explode inside her as she stops pumping."
    off "She gives one final and brutal swoop on my shaft, taking it even deeper than before."
    off "She clutches onto me as she starts shaking uncontrollably."
    scene ep5_sc24_lr_42
    sis "Haaaaaaan, Haaaaaaaaaaaaan, Haaaaaaaaaaaan!"
    mc "Haaaaaaaaaaaaaaaaaaaaaaaaaaarrrrwwwwwwn!"
    off "I hold her as tight as I can while I empty my balls inside her."
    off "I can feel my cum rushing from my testicles, through my entire shaft."
    off "I can feel it blowing out of my glans."
    off "My whole genitals are on fire. "
    off "I can feel her vagina contracting around my shaft."
    off "She's squeezing me inside her with an insane strength."
    off "Both our orgasms seem to last longer than they should be."
    scene ep5_sc24_lr_43
    off "It takes us maybe a couple of minutes to emerge from the bliss."
    mc "Holy shit, Princess."
    mc "I think I won't be able to move for a while."
    off "She's still shivering from time to time."
    off "She's very sensitive."
    sis "You destroyed me... I can't move either."
    off "She sounds exhausted."
    mc "That was... I have no words for it."
    scene ep5_sc24_lr_43_alt
    sis "Maybe... We could just not speak... I just... Want to stay like this for a bit..."
    mc "Yeah... I'm ok with that..."
    mc "We'll stay like this as long as you want."
    mc "Enjoy the moment."
    off "My whole body is tingling."
    off "I'm still about to pass out."
    off "I need to calm down."
    off "We stay like that for several more minutes."
    off "I'm going limp inside her."
    off "She's so tight that her pussy is still sucking me inside her. "

    if sf_dom_path == True and ep5domstayed == True:

        scene ep5_sc24_lr_44
        off "That's when I see her."
        off "[sf_name]."
        off "Looking at us from the entrance of the room."
        off "Cold sweat runs down my spine."
        off "I don't know what to do."
        off "I'm balls deep inside [sis_name]."
        off "My brain goes blank."
        off "What to do? What to say?"
        off "She looks... Sad... and also envious... maybe even aroused."
        off "No, I'm probably imagining it."
        off "She lowers her head and leaves."
        scene ep5_sc24_lr_45
        off "I'm so confused."
        off "Was that even real?"

    off "[sis_name] hasn't moved or spoken for a while now."
    off "Her voice surprises me."
    scene ep5_sc24_lr_46
    sis "We're so deep in trouble..."
    off "She seems sad."
    mc "In trouble?"
    sis "We just fucked, [mc_name]."
    sis "We're not supposed to do that."
    off "Fucked."
    off "That word sounds so harsh and insensitive."
    off "I feel like it doesn't even remotely come close to describe what we just did."
    mc "No. We didn't fuck."
    mc "We made love."
    mc "That's entirely different."
    scene ep5_sc24_lr_47
    off "She suddenly sobs."
    mc "Hey, Princess."
    mc "Everything will be alright."
    mc "I promise."
    sis "No, it won't."
    off "She takes a deep breath and the sobbing stops as fast as they came."
    sis "But we'll deal with it, right?"
    mc "Yeah. We'll deal with it."
    sis "We're so deep in trouble..."
    mc "Yeah..."
    off "The silence that takes place between us is warm and comfortable."
    off "I want it to last."
    off "Yet, it's dangerous."
    off "I feel that we could fall asleep as we are."
    off "And we also have some other matters to take care of."
    scene ep5_sc24_lr_48
    mc "Speaking of trouble..."
    mc "I'm done going limp inside you."
    sis "I can feel it."
    mc "And... That means that everything I unloaded inside you..."
    mc "It's going to drip on the sofa..."
    sis "Shit."
    off "She sighs."
    sis "You filled me up..."
    sis "I'm going to drip all the way up to my room."
    sis "I should go to the bathroom and take care of it..."
    mc "Probably, yeah..."
    mc "I'll clean everything up."
    mc "Don't worry about it."
    mc "Can you walk?"
    mc "I can carry you."
    sis "I'll walk."
    sis "I should be ok now."
    mc "Go get some rest then, I'll join you once I'm done with the cleaning."
    off "She nods and gives me a quick kiss before she stands up."
    scene ep5_sc24_lr_49
    off "She holds her pussy and tries to prevent it leaking anymore while she picks up her clothes and heads out."
    off "I spend a few minutes cleaning the room, wiping my semen from the sofa, the carpet and the floor."
    off "God bless the washable cushion covers."
    $ renpy.end_replay()
    scene ep5_sc24_lr_50
    off "It should be ok."
    off "We did it."
    off "We made love."
    off "I know that I should feel guilty about it."
    off "I should feel weird, disgusted, something like that."
    off "But I just feel good."
    off "And it's not just because I've emptied my balls, no."
    off "There's something else, something more."
    off "[sis_name] and I are even closer now than before."

    if sf_dom_path == True and ep5domstayed == True:
        off "What about [sf_name]?"
        off "That was so weird."
        off "She didn't say a word."
        off "Was she even there?"
        off "Was she real?"
        off "Did I dream of her watching us?"
        off "Should I go see her?"
        off "No, this is probably not the time for that."
        off "I'd better wait till tomorrow to speak with her..."
        off "But what am I going to say?"

    scene ep5_sc24_sr_01
    off "[sis_name] is already asleep when I join her."
    off "I wanted to talk about a few things but I guess it'll have to wait until tomorrow."
    off "I don't know what got into her tonight."
    off "I sure didn't anticipate that we would have sex so soon in our relationship."
    off "I won't complain, though."
    off "It was fantastic."


    return

label ep5sc25:
    scene black with dissolve
    with Pause(2)
    scene ep5_sc25_c_01 with dissolve


    off "Ok."
    off "Breathe, [mc_name]. You're going to manage."
    off "This is so weird."
    off "That discussion in [sf_name]'s room was weird, the breakfast was weird, that moment in the pool was weird."
    off "I don't understand how we've come to this."
    off "Ok, we all love each other in some strange love triangle."
    off "And it sounds pretty logical to try to be happy together in a throuple rather than sinking into hatred and anger."
    off "But still..."
    off "The average human being doesn't react this way."
    off "It was... too easy... and unexpected."
    scene ep5_sc25_c_02
    off "It feels unreal."
    off "[sis_name] and [sf_name] are waiting for me behind that door."
    off "How am I going to handle that?"
    off "Calm down, [mc_name]."
    off "It'll be ok."
    off "They're probably as stressed out as you are."
    off "Nothing will happen tonight."
    off "You're going to enter that room."
    off "You'll have a nice chat with these two beautiful girls."
    scene ep5_sc25_c_03
    off "If you're lucky, you will get a few kisses, maybe you will even get to grope an ass."
    off "But it won't go further than that."
    off "The three of you have yet to grow accustomed to this throuple thing before anything happens."
    off "So... No need to panic."
    off "No pressure."
    off "I get closer to the door."
    scene ep5_sc25_c_04
    off "I raise my hand to knock on it when I notice the faint murmur of the girls' voices coming from the other side."
    off "I can't help but stop and listen."
    sf "It's huge."
    sf "About this long... and thick... like this."
    sis "Holy shit... I knew he was well-endowed but..."
    sis "He's bigger than the purple one then?"
    off "Are they talking about... my dick?"
    off "What the hell is the purple one?"
    scene ep5_sc25_c_05
    sf "Oh yes. He is much bigger."
    sis "Shit..."
    sf "It's ok. It may seem a lot, but we will do just fine."
    sf "He'll just have to be a bit careful for the first time and take it slow."
    sf "After a couple of times, I'm sure that we will be used to it."
    sf "He'll make you forget the purple one."
    sis "Oh my god..."
    sis "It took me more than a couple of times to get used to the purple one."
    sf "But after that, you couldn't even imagine not playing with it. Am I right?"
    sis "Hey, as far as I know, it's also your favourite toy!"
    sf "And I'm sure this is about to change."
    scene ep5_sc25_c_06
    off "[sis_name] sighs loudly."
    sis "So we're doing it."
    off "She doesn't sound too excited."
    sf "You don't want it?"
    sis "It's... I want it. I want it very much."
    sis "I mean... doing it together..."
    sis "It's weird."
    sis "I want it and in the meantime, I'm afraid of it."
    sis "And also... If I do it with him, right in front of you..."
    sis "You're sure you won't be upset?"
    sis "Or jealous?"
    off "That's exactly what I'm afraid of, Princess."
    sf "I can't be sure."
    sf "I think I will be."
    sf "But I also know that my turn will come."
    sf "Or maybe that I won't just watch."
    sf "Maybe I'll participate."
    sis "He only has one dick you know?"
    scene ep5_sc25_c_07
    off "[sf_name] laughs."
    sf "That is true."
    sf "But he also has a mouth, two hands... and you have some assets too..."
    off "Oooh..."
    sis "Now, that sounds naughty young lady..."
    sf "Would that annoy you?"
    off "[sis_name]'s hesitation is palpable."
    off "She takes a few seconds to reply."
    sis "No. I'll probably enjoy it."
    off "Holy mother of god..."
    sf "Do you think he'll enjoy it too ?"
    off "Oh yes, I will!"
    sis "Oh, I'm sure he will."
    sis "Guys love girl on girl action."
    sis "I don't understand why."
    sis "The instant we kiss he'll be ready to go."
    off "I'm ready to go just hearing this, Princess."
    off "And I'm not even ashamed to be a living cliché."
    sf "And what about you?"
    sf "If we do it tonight, right there, in front of you..."
    sf "Will you be upset? Or jealous? "
    scene ep5_sc25_c_08
    off "Another few seconds of silence."
    sis "Yeah. I will be."
    sis "But... It's so weird..."
    sis "When I think about him being inside you... I can feel him inside me too."
    sis "It's... I think I'll be jealous, and I'll like it at the same time."
    sis "That's so disturbing..."
    sf "I feel the same."
    sf "And it's not just about watching."
    sf "It's about knowing, and feeling that he is with one of us."
    off "I don't hear it, but I can sense [sis_name] nodding her approval."
    sf "And... will you participate ?"
    sis "Again... It's so weird... and I want it so much..."
    sis "I feel like I'm going crazy."
    sf "I don't think there's anything crazy in that."
    sf "As I said, I feel the same."
    sf "You have nothing to fear, nor to be ashamed of."
    sf "I'm here with you."
    off "Their relationship is definitely something special."
    off "Obviously, because of that, we're now in this situation."
    sis "So... you don't think that... We're disgusting?"
    sf "You're talking about you and [mc_name]."
    sis "Yeah..."
    scene ep5_sc25_c_09
    sf "No."
    sf "It's weird, and a bit surprising."
    sf "But I wouldn't call it disgusting."
    sf "I read that book a couple of weeks ago..."
    sf "It was a very cheap romance full of stereotypes."
    sf "Not a fascinating read."
    sf "But even the most generic and uninteresting of stories can hold some truth."
    sf "And well... You don't choose who you love."
    sf "And... If you don't go with it, you will regret it for the rest of your life."
    sf "So... Yeah, he is your childhood friend."
    sf "But if you're completely sure that you love him... Then either you run with it or you will regret it."
    sf "I'm not encouraging you."
    sf "I'm just saying that... Maybe we don't really have a choice."
    sf "But you have to be absolutely certain."
    sf "If you still need to think about it, he can wait."
    sf "He will understand."
    scene ep5_sc25_c_10
    off "Of course, I can wait."
    off "I never wanted to pressure her into anything..."
    sis "I don't have a single doubt about it."
    off "[sis_name]'s voice overflows with melancholy."
    sis "I think I've loved him for as long as I can remember."
    sis "I've never told him of course."
    sis "I wasn't supposed to fall for him in the first place."
    scene ep5_sc25_c_11
    off "I can hear her sobbing."
    off "She's crying."
    off "My heart tightens."
    off "She's held something for me for so long?"
    off "How could I not notice it?"
    sis "Then all that bullshit happened."
    sis "And he became a real asshole..."
    sis "I thought that I'd lost him forever..."
    sis "But I kept loving him."
    sis "Because I'm dumb as fuck."
    off "Oh, Princess, I'm the one to blame."
    off "I'm so sorry."
    sf "You're not dumb."
    scene ep5_sc25_c_12
    sf "You can't control your feelings."
    sis "And when he took me in his arms and apologized..."
    sis "I could feel something breaking inside me."
    sis "Those feelings came back."
    sis "Somehow stronger."
    sis "I just couldn't keep it inside me anymore."
    sis "I'm so sorry, [sf_name]."
    sis "I teased him."
    sis "I'm the one who went to his room at night."
    sis "I kissed him."
    sis "I knew what I was doing."
    sis "I just couldn't help myself."
    sf "It's ok, sweetie. I understand."
    sf "You didn't have a choice."
    sf "I wish you would have talked to me about that beforehand, but I understand."
    sf "That wasn't easy for you."
    sf "You don't choose who you love, and you thought it was your last and only chance..."
    sf "I understand."
    off "[sis_name] stops crying and takes a deep breath."
    sis "He always has been a bit like that."
    sis "You think he is an idiot and then at some point, he will do something so sweet and so nice that you fall for him more and more each time."
    sis "But the opposite is also true."
    sis "It's when you think he is like the charming prince, then he will pull the dumbest bullshit ever."
    off "I don't know if this is flattering or insulting."
    sf "I noticed that."
    sf "I fell for him too, remember?"
    off "[sis_name] chuckles."
    sis "I guess that's one more thing we have in common then."
    sf "Yes. One more thing we'll share."
    scene ep5_sc25_c_13
    sis "Speaking of him... What is he doing?"
    sis "He can't have anything more interesting to do..."
    off "Crap. I shouldn't have made them wait so long."
    sf "I think he is a bit... Stressed out by our situation."
    sf "You saw how he reacted during breakfast..."
    sis "Yeah... That moron scared the hell out of me."
    sis "We should have taken him to a doctor."
    sf "It's ok."
    sf "It's like he said, he was too... Excited and hyperventilated."
    sf "That made him pass out."
    sf "He was in total panic mode once we brought up the idea of... Doing it together..."
    sis "You think he is afraid?"
    sf "I don't know... But he may be feeling a bit of pressure..."
    off "Yeah... Just a bit..."
    sis "Yeah... Well, I'm going to see what he is doing."
    sis "We're not going to wait for him all night long..."
    off "Shit."
    scene ep5_sc25_c_14
    off "I immediately stand up and knock on the door."
    off "I can feel the mood shifting inside the bedroom."
    off "The girls have stopped talking and only the silence answers me."
    off "I wait a minute and think about knocking again when [sis_name]'s faint voice reaches to me."
    sis "Come in."
    off "I take a deep breath and comply."
    scene ep5_sc25_sr_01
    off "I don't know how long it really lasts, but we spend what seems to be an eternity looking at each other from across the room."
    off "No one utters a word."
    off "They don't seem so confident."
    off "Alright. Say something, [mc_name]."
    off "Something clever and charming."
    off "Something reassuring."
    off "Comfort them."
    off "Be a gentleman... That kind of thing..."
    off "Ok... but what?"
    off "Nothing comes to my mind."
    off "This is so awkward."
    off "All this feels so rushed and forced..."
    scene ep5_sc25_sr_02
    mc "So..."
    sis "Yeah..."
    off "..."
    off "This is pathetic."
    off "I am pathetic."
    off "No wonder I'm still a virgin."
    off "[sf_name] takes a deep breath and sighs."
    sf "I guess we're all a bit tense."
    sf "We should relax."
    sf "What will happen will happen."
    sf "No pressure, no expectations."
    scene ep5_sc25_sr_03
    sf "How about we just sit on that sofa and have a nice chat?"
    sf "I'm sure we have a few things to talk about."
    sis "Yeah! That... sounds great."
    off "A nice chat."
    off "I can do that."
    mc "With pleasure."
    off "They sit on either side of me."
    off "[sis_name] seems to hesitate, but [sf_name] gives her a little nod and they both close the distances that separate us."
    scene ep5_sc25_sr_04
    off "They wrap themselves in my arms and cuddle."
    off "It feels very weird."
    off "But also very nice."
    off "I still feel uneasy."
    off "Can I really touch them?"
    off "Come on, [mc_name], grow some balls, dammit!"
    off "They are your girlfriends."
    off "Aren't you supposed to... enjoy them?"
    sf "There's no need to worry, right?"
    sf "If anything happens in this room tonight, it can only be something nice."
    mc "Ok..."
    sis "We're not going to eat you..."
    off "Holy mother of god."
    off "But I want to be eaten..."
    off "Why is it so hard for me to cope with it?"
    sf "Are you alright, [mc_name]?"
    sf "You're not going to pass out again, aren't you?"
    sf "You look like you don't want to be here."
    mc "I'm alright."
    mc "And I want to be here very much."
    mc "I'm just a bit nervous."
    scene ep5_sc25_sr_05
    sf "Oh, it's not easy for us either."
    sf "But... We talked about it, and we know we want it."
    sf "And you want it too, right ?"
    mc "Oh, yes, no doubt about that."
    off "Who wouldn't?"
    sf "Today has been pretty eventful, too..."
    sf "It's normal to be a bit worried."
    sf "Stress is to be expected."
    mc "Yeah..."
    mc "Speaking of which, [sf_name]... How are you doing?"
    mc "I must say that I'm impressed by the ease with which you handle the... Revelation about the psycho twins true motive..."
    scene ep5_sc25_sr_06
    sf "Oh... I'm okay."
    sf "It's not the first time that there's that kind of rumour around my dad."
    sf "He is always that new guy who shows up when the company is in crisis so... people tend to have him bear responsibilities for things like that."
    sf "This time it's a little more extreme than usual but... we'll be alright."
    mc "So you're used to it?"
    sf "I wouldn't say that but... These are the kind of things that happen."
    sf "Once you know that, it's easier to manage."
    sf "The last time, I think I was twelve, someone threatened to harm us."
    sf "Dad hired a bodyguard to ensure my safety and that of Miss Mei."
    sf "But we didn't have any problem in the end."
    sf "The threats were just words with no real intentions to back them."
    off "Bodyguards."
    off "We're definitely not living in the same world."
    scene ep5_sc25_sr_07
    sis "But this time... It's different..."
    sis "They're crazy... and they already tried something..."
    sf "Yes... But we'll be fine, right?"
    sf "We've gone to the police, and we're doing everything we can to stay safe."
    mc "Of course."
    mc "I doubt they will even try to approach the house."
    mc "So as long as we're careful, we'll be perfectly fine."
    sf "Oh... By the way..."
    sf "Dad asked me to come back home."
    sf "But I told him that I was fine here and that... my boyfriend was here to protect me if needed."
    off "I guess things are getting serious."
    off "Her father knows I exist."
    off "I am officially her boyfriend now."
    mc "Sure... I'm here. Obviously."
    off "She looks at me with as much malice as embarrassment."
    off "I must have missed something."
    scene ep5_sc25_sr_08
    sf "He... wants to meet you."
    off "Holy shit."
    off "Am I going to get some kind of dad talk?"
    off "[sf_name]'s father doesn't really seem to be an easy-going guy."
    sis "He's going to murder you."
    mc "What?"
    off "[sis_name] plays with my hand has she joyfully drops her joke."
    off "She's enjoying this situation."
    sf "Of course not!"
    sis "And he will hide your body somewhere."
    sf "No, he won't!"
    sis "He has the money to get away with it, no problem."
    scene ep5_sc25_sr_09
    off "[sf_name] changes her posture and turns to [sis_name]."
    off "My hand falls on her back and fortunately grabs the first thing it finds."
    off "Her ass."
    off "She doesn't seem to mind."
    off "She gently caresses the back of my head while scolding [sis_name]."
    sf "You little scoundrel!"
    sf "Will you stop that?"
    sf "You're going to frighten him!"
    sf "He just wants to meet you, [mc_name]."
    sf "He won't murder you or anything, I promise."
    sf "My dad isn't like that."
    sf "You have nothing to fear."
    scene ep5_sc25_sr_10
    off "[sis_name] passes a thumb over her throat as her lips silently articulate the word murder."
    off "I know she's kidding, but I can't help but worry a bit."
    mc "Yeah... Well... Sure... Whenever you want..."
    sf "Maybe for a dinner... Next week?"
    off "So soon... Crap..."
    off "What about next year instead?"
    mc "Sure... As soon as we're done with the two crazies..."
    sf "And you will come too."
    scene ep5_sc25_sr_11
    sis "I wouldn't miss it."
    sis "I'm sure it will be hilarious."
    sis "I'm so eager to witness the moment when your father will understand that his cherished daughter is in a relationship with a mere mechanic nerd."
    off "No pressure at all."
    sf "Don't listen to her."
    sf "She's just messing with you."
    sf "Dad will like you."
    sf "I know that already."
    mc "Ok..."
    off "It's ok, [mc_name]."
    off "Don't panic."
    off "If you're serious about her, you will have to do it sooner or later."
    off "I would prefer later than sooner but... I'm sure it'll be alright."
    off "They're smiling."
    off "They're enjoying themselves, and the moment."
    off "Why do I keep worrying about all these things that don't really matter?"
    off "The only thing that's important is them, right?"
    off "Us."
    off "Yolo."
    off "I turn to [sis_name] and address her in a conspirational tone."
    scene ep5_sc25_sr_12
    mc "If anything happens to me, I'm counting on you to take care of my porn stash."
    off "She bursts out laughing."
    off "[sf_name] feigns outrage before joining in."
    sis "Fear not, Bro. I'll have your back."
    off "We laugh together for a minute."
    off "I seize that opportunity to change the subject of our conversation."
    mc "So... I didn't dream it, did I?"
    mc "You called Kelly your friend, right?"
    scene ep5_sc25_sr_13
    sis "I did yeah..."
    mc "You surprised me."
    mc "With your speech, I was sure that you would tolerate her here, but nothing more."
    mc "You even threatened her to punch her in the pussy."
    mc "That made me laugh as much as it frightened me."
    mc "For a moment I thought that you might assault her..."
    scene ep5_sc25_sr_14
    sis "I was... upset... By her attitude."
    sis "I mean... [sf_name] and I, we talked about it a lot."
    sis "And... Yeah, she isn't the evil bitch she was anymore."
    sis "If she was even an evil bitch at some point."
    sis "She was the source of the first rumours, she confessed it herself... but not everything that happened to us was her fault."
    sis "Not directly at least."
    sis "She had no control over it."
    sis "She couldn't have stopped it even if she wanted to."
    sis "That doesn't mean that she's innocent of everything..."
    sis "But yeah... She didn't harass us for the last three years..."
    sis "The school did..."
    sis "Well... you understand what I mean."
    mc "I think I do, yeah..."
    mc "But still, forgiving her... and befriending her? In one go ?"
    scene ep5_sc25_sr_15
    sis "Hating her was pointless."
    sis "And also... she's so miserable that holding a grudge against her would only make me feel bad."
    sis "That's what upset me."
    sis "She has to stop with her goddamn apologies."
    sis "That's enough."
    sis "I understand that she feels guilty and that she won't get rid of it easily, but her constant apologetic stance was making me crazy."
    sis "And for the friend thing..."
    sis "I don't know..."
    sis "It seemed like the right thing to do."
    sis "She has paid enough."
    sis "And it was... liberating."
    sis "For her and for us."
    off "That's very mature."
    off "I'm ashamed."
    off "I'm pretty sure that I wouldn't be able to let go of my anger so easily."
    mc "She was crying when you left the living room together."
    mc "I guess that had some impact on her."
    scene ep5_sc25_sr_16
    sf "Oh, she cried for several minutes."
    sf "[sis_name] had to threaten her again with that dreadful pussy punch for her to stop shedding those tears."
    sf "But we tried as hard as we could to implicate her in our discussion with Jane."
    sf "In the end, I think she felt better."
    mc "Well, she cried again when she brought me my cellphone back, by the pool."
    mc "She thinks that she doesn't deserve forgiveness."
    sis "I'll have to spank her some more tomorrow."
    off "I imagine the scene and I can't help but chuckle."
    mc "Can we watch?"
    sis "I'll sell some tickets."
    scene ep5_sc25_sr_17
    off "We spend a few seconds laughing, and I try my luck with something else."
    mc "So, about that conversation with Jane?"
    mc "How was it?"
    off "The mood shifts a bit as [sis_name] and [sf_name] look at each other."
    sis "That was... interesting."
    sis "And fun I guess?"
    sf "Oh, yes. It was fun."
    mc "Ok... but... What was it about?"
    sf "It's a secret."
    mc "Oh, come on..."
    sis "You've already asked Kelly, haven't you?"
    off "They won't tell me anything. Goddammit."
    mc "Yeah..."
    sis "And what did she tell you?"
    mc "Nothing."
    sf "Nice!"
    scene ep5_sc25_sr_18
    sis "Chicks before dicks."
    sis "I knew we could trust her on that."
    mc "What? Was that a test for her? Or something?"
    scene ep5_sc25_sr_19
    sis "Nah."
    sis "We just don't want you to know what we talked about."
    sis "Jane said it would be better to keep you wondering, and the three of us agreed."
    mc "The three of you. Great..."
    sis "Glad you like it."
    off "I'll question Steve about it tomorrow, but I have very little hope I'll ever know what they talked about."
    mc "I have the impression that your very select group of friends has grown from two to four members today."
    sf "I don't think we know Jane, and Kelly, well enough to be sure about that but... having that moment together sure was nice."
    sis "Jane is weird, but I like her."
    scene ep5_sc25_sr_20
    sf "I like her too."
    sf "She's very honest and straightforward."
    sf "And also very kind, and empathic."
    off "So she's not just a perverted weirdo?"
    sf "I have a feeling that things are going to get interesting."
    mc "What are you talking about?"
    sis "Steve is bringing her back with him. You didn't know?"
    mc "No... I... I didn't really talk with him today..."
    sis "Well... Turns out, they really are... fond of each other."
    sis "So she will come here for at least a week."
    off "Holy shit."
    mc "Ok..."
    sf "He will probably tell you about it the next time you have him on the phone."
    mc "Yeah... sure..."
    off "Steve is my best... and my only real friend."
    off "Why didn't he tell me about that?"
    scene ep5_sc25_sr_21
    sis "Hey. Don't fret about it."
    sis "They decided upon it today, so he didn't have any time to talk to you."
    off "Did she just read my mind or something?"
    mc "Sure. He'll tell me next time."
    mc "It's just... I didn't have the impression that their thing was so serious."
    mc "I guess I'll know more about it tomorrow."
    off "The discussion sinks into silence."
    off "Just when I'm sure we're done with it, [sis_name] brings it up again."
    scene ep5_sc25_sr_22
    sis "You know what's really weird?"
    sis "The first thing we saw of her was her pussy impaled on Steve's dick."
    sf "And that was quite a show."
    sis "I first thought that she was completely insane and... Not someone I would want to know more about."
    sis "But things are different now."
    sis "We're thinking of her as a potential friend..."
    sis "And that video..."
    sis "I don't know how... but now, I'm totally ok with it."
    sis "It's normal."
    sis "It's just Jane."
    sis "It's weird isn't it?"
    mc "What do you mean, totally ok with it?"
    scene ep5_sc25_sr_23
    sf "I feel the same."
    sf "The first time we saw that video, we were surprised, and a bit grossed out."
    sf "And our first reaction was \"How can someone can have sex with Steve, record it and send it to a complete stranger?\"."
    sf "But now, I'm pretty sure that we would just watch it... and... it would be just Steve and Jane doing their thing."
    sf "Like there is nothing strange about it, nothing weird, nothing gross."
    sf "It's just them."
    sf "We're ok with it, and we're even ready to talk and laugh about it with them."
    sf "I'm not sure I'm making much sense."
    sf "Sorry."
    scene ep5_sc25_sr_24
    sis "That's exactly what I meant."
    mc "I think I understand."
    mc "You can get used to their shenanigans fairly quickly, once you know them."
    sis "I'm glad they can have that much fun together."
    sis "They seem happy."
    mc "I can't talk for Jane, but Steve is having the time of his life."
    mc "I have no doubt about that."
    sf "She enjoys it too."
    off "The conversation goes back to silence once again."
    off "The girls exchange a rather long look."
    off "[sis_name] takes a deep breath and whispers."
    sis "So... you want to know what we talked about with Jane?"
    scene ep5_sc25_sr_25
    off "She's embarrassed and looks away as she speaks."
    off "Her change of tone is unexpected. Something is going on."
    mc "Yeah... sure..."
    sis "Then... you should lose your shorts."
    off "Holy fuck."
    off "I swallow with difficulties."
    off "I feel like the whole room is spinning around me."
    off "My heart accelerates."
    off "I can feel its beating in my temples."
    scene ep5_sc25_sr_26
    off "I turn to [sf_name]."
    off "She looks me in the eyes and I can read as much embarrassment as arousal in her expression."
    off "This is happening."
    off "This is it, [mc_name], this is your goddamn moment."
    off "Don't fuck it up."
    off "You've dreamt about it."
    off "You're the luckiest guy on Earth."
    off "Grow a pair and do something."
    off "Something other than passing out, moron."
    off "I stand up and undress."
    label galleryScene14:
    scene ep5_sc25_sr_27
    off "My semi boner dangles in front of them."
    sis "Holy shit."
    off "They both ogle it shyly before exchanging another look."
    off "I feel like they're having a whole and complex conversation through that single glance."
    scene ep5_sc25_sr_28
    off "[sis_name] pushes me back a bit and kneels before me."
    off "Our eyes meet."
    off "I want to say something."
    off "Like that she doesn't have to do that if she doesn't want to."
    off "But my mouth and throat are completely dry."
    off "My breathing is loud and heavy."
    off "I can't articulate a word."
    off "[sf_name]'s voice answers my silent worries."
    off "That girl reads me like an open book."
    sf "We want it."
    off "She said that without any hesitation."
    off "We. She talks for both of them."
    scene ep5_sc25_sr_29
    off "[sis_name] slowly lifts my cock and plants a little kiss on my glans."
    off "The contact of her lips makes me shiver."
    off "My dick reacts instantly and hardens."
    off "She strokes it gently."
    off "I'm fully erect in a few seconds tops."
    scene ep5_sc25_sr_30
    off "Her tongue on my glans feels heavenly."
    off "I shiver each time she licks my tool."
    off "She takes her time to taste my dick and cover the tip of it with her saliva."
    off "Is this what they talked about with Jane and Kelly?"
    off "Did they discuss blowjobs?"
    off "Holy shit!"
    scene ep5_sc25_sr_31
    off "She takes my cock in her mouth and starts sucking on it."
    off "She struggles a bit to keep her teeth away from my shaft but she's doing a great job."
    off "Her tongue swirls around my glans as she sucks harder and harder."
    off "Her head slowly pumps on my dick."
    off "We're just getting started and I already know that I'm not gonna last long."
    off "It would be pathetic to let it end so soon."
    off "Fuck. It feels so good..."
    scene ep5_sc25_sr_32
    off "[sf_name] watches us from the sofa."
    off "She seems to be enjoying the show very much."
    off "Focused on my dick and [sis_name]'s lips around it, she's touching herself through her underwear."
    scene ep5_sc25_sr_33
    off "We look at each other."
    off "I understand a bit more about what they were talking about earlier."
    off "Suddenly that makes everything better."
    off "The girl seems about to explode."
    off "Holy fuck, her eyes..."
    off "Do something, [mc_name]."
    off "Now."
    off "But what?"
    off "[sis_name] looks at me, my dick still in her mouth."
    off "She knows."
    off "She understands."
    scene ep5_sc25_sr_34
    off "She slowly lets go of my tool and nods."
    off "Oh, God."
    off "She gave me a blowjob and I'm going to switch to [sf_name] without even repaying her?"
    off "I'll have to go back to her later."
    off "I can't let this business be left unfinished."
    scene ep5_sc25_sr_35
    off "[sf_name] tenses up as I kneel between her legs."
    off "I gently lay my hands on her thighs and caress her legs while I go for her underwear."
    off "She moves her hips to help me to remove her clothes."
    off "We look at each other for a few seconds."
    off "I don't see any doubts or hesitation in her eyes."
    off "During breakfast, they talked about her being first."
    off "They weren't kidding."
    off "We're going to have sex tonight."
    off "Or rather, we're going to make love."
    off "She knows it."
    off "She wants it."
    off "I look at her pussy."
    off "My mouth was dry a minute ago, but I'm now drooling."
    off "She looks delicious."
    off "I place her legs on my shoulders and slowly gets closer to her clitoris."
    scene ep5_sc25_sr_36
    off "She moans and shivers as soon as my tongue touches her."
    off "[sis_name] watches us with attention."
    off "She doesn't want to miss seeing any of the action."
    off "I can feel her arousal."
    off "I suck on [sf_name]'s pussy and rummage it with my tongue."
    off "I try to kiss her lips down below as if it was her mouth."
    off "And I was right."
    scene ep5_sc25_sr_37
    off "She is delicious."
    off "She groans and arches as I softly work on her."
    off "I have no idea what I'm doing but as long as she seems to enjoy it, I guess it's fine."
    off "I stay focused on her vagina a few minutes."
    off "Maybe more. Maybe less."
    off "Tracking time is difficult."
    sis "[mc_name]. She's ready."
    scene ep5_sc25_sr_38
    off "I emerge from between [sf_name]'s thighs and take a few seconds to fully grasp the situation."
    off "[sf_name] nods."
    off "I stand up before them."
    off "My dick is still hard and proudly erect."

    off "I feel the urge to grab it and give it a few strokes."
    off "They watch me doing so as if they were mesmerized."


    scene ep5_sc25_sr_39

    sis "Holy shit..."
    off "I have no idea how I am supposed to take [sf_name] on that sofa and she seems to read my mind."
    off "She clumsily climbs from the sofa onto the bed."
    off "[sis_name] immediately accompanies her and sits by her side."
    off "I slowly follow them and crawl between [sf_name]'s legs."

    scene ep5_sc25_sr_40

    off "I'm going to do it."
    off "I'm going to have sex with [sf_name] while [sis_name] watches us."
    off "This is so weird."
    off "And so hot."
    off "Far from disturbing me, [sis_name]'s gaze arouses me."
    off "And their complicity..."
    off "It takes everything a step higher."
    sis "That thing is so big..."
    mc "If you want me to stop..."
    sf "Just go slow, please. I'll need to get used to it..."
    mc "As slow as you want."
    off "I lean over her and bring my glans to her pussy."
    off "I try to caress her."

    scene ep5_sc25_sr_41

    off "I planned to do that for a few seconds but her pussy is drenched and eager."
    off "It opens up outright and swallows the tip of my dick without me applying any pressure."
    sf "Haaan! Oh!... Ooh my God!"
    sis "It's going in! It's really going in!"
    sf "I know! Mmmmhhm! I can feel it!"
    sis "Oh my God!"
    off "I'm inside her."
    off "Holy shit!"
    off "I'm inside a girl."
    off "I'm inside [sf_name]."
    off "I'm having sex with her and [sis_name] is watching us."
    off "This is real!"
    off "Holy fucking shit!"

    scene ep5_sc25_sr_42


    off "I clutch on her hips."
    off "It feels warm and welcoming."
    off "I give her a few second before going deeper inside her."
    off "I progressively pump further, centimetre by centimetre."
    sf "Oooooh!"
    off "She wraps her legs around me."
    off "It makes it easier to go in and out of her."
    sis "Slow down a bit, [mc_name]. Please."
    off "[sis_name] giving me instruction doesn't even surprise me."
    off "I just accept it and go with the flow."


    scene ep5_sc25_sr_43

    mc "Sure."
    mc "I'm sorry, maybe I've got a bit carried away."
    sis "It's ok."
    sis "You're doing fine."
    sis "Just... a bit slower, please."
    off "I nod a yes and go back to [sf_name]."
    off "I pump as slow as I can and thrust in her with only half my shaft."
    sf "Mmmmmhm, you're so much bigger than our toys..."
    sis "Definitely bigger than the purple one."
    sf "Oh, yeeeeeeees!"
    off "I'm getting curious about these toys they're talking about."
    off "I'll take that as a compliment."
    sis "Wait."

    scene ep5_sc25_sr_44

    off "[sis_name] gets closer and lays a hand on [sf_name]."
    sis "There..."
    sis "Try to rub it on the top of her vagina."
    sis "Against my hand."
    off "I comply."
    sf "Haaaaaaaaaan!"
    off "[sf_name]'s reaction is brutal."
    off "I can feel her vagina contracting around my dick."
    off "She arches and holds her breath before moaning again."
    sf "Mmmmhm!"
    sis "Most of the girls love that."
    off "She says that in a shyer tone."
    mc "I'll try to remember that..."
    off "I slowly pump further inside her and [sf_name] seems to enjoy it greatly."

    scene ep5_sc25_sr_44_bis

    sis "I can feel him inside you..."
    sis "That's crazy..."
    sf "Oh, I can feel him too!"
    sf "Haaan!"
    sis "How is it?"
    sf "Greaaat! Mmhhm!"
    sf "Oh my God!"
    off "[sis_name] stands back a bit."
    off "[sf_name]s raises her head to look at my dick plunging inside her."
    sf "I want everything, please."
    sf "But slowly."
    off "And I comply."
    off "With a few gentle and progressive thrusts, I dive inside her."
    sf "Ooh, my Goood!"
    off "She gets rid of her tank top and I immediately grab one of her breasts."
    off "She drags me closer to her. "

    scene ep5_sc25_sr_45

    off "She makes me lay on her and she wraps herself around me."
    off "Our lips and tongues join in a permanent kiss."
    off "I give her a few second of rest before I start thrusting again with all the length I can give her."
    sf "Haaan!"
    off "[sis_name] wiggles on her side of the bed as she removes her underwear."
    off "She touches herself while she watches us."
    off "[sf_name] is very tight."
    off "I think about telling her this but it sounds so much like a porn cliché that I finally keep it to myself. "

    scene ep5_sc25_sr_46

    sis "Mmmmmmmhhhhm..."
    sis "You can go faster..."
    sis "She likes it slow, but hard."
    sis "Thrust in as hard as you can."
    sis "Haaan."
    sis "Like if you were trying to break her pussy with your hips..."
    sis "Mmmhhm..."
    sis "Then go real slow for a few runs..."
    sis "Then hard again..."
    sis "You keep at it until... Mmmhm."
    sis "Grab her."
    sis "Hold her tight."
    sis "Yeah... just like that."
    sf "Haaaaaan!"
    sf "Haaaaaaaaaaan!"
    sf "Mhhhmmm!"
    off "I can't even begin to understand what's going on with [sis_name] giving such detailed directives."
    off "But [sf_name] seems totally fine with it and so am I."
    off "I comply as best as I can."
    off "But it's far from easy."
    off "I'm about to reach my limit."
    off "I bury my head in her hair and put as much strength as I can into my hips."

    scene ep5_sc25_sr_47

    sis "She's close."
    sis "Faster!"
    sis "As fast and as hard as you can!"
    sis "Deeper !"
    sis "Mmmhhhhhm!"
    sf "Ooooooooooh!"
    off "Oh god, just a few more seconds!"
    off "Come on [mc_name]!"
    off "You can do it!"
    mc "I'm gonna come too!"
    sis "She's not on the pill, [mc_name]!"
    sf "It's ok, it's ok, it's ok!"
    sf "Don't pull out!"
    sf "Please!"
    sf "Don't pull out!"
    sf "Please! Please! Pleaaaaaaaaaaaaaaaaase!"

    scene ep5_sc25_sr_48


    mc "HAAAAAAAN, Haaaaaaaaaarwwwwwwwwwnnn!"
    off "I literately explode inside her."
    off "I can feel my jizz bursting out of my testicles and rushing through my shaft."
    off "I have to stop pumping inside her as a flash of pure pleasure completely shatters my spine and paralyses me."
    off "I've never felt anything like that."
    off "Jerking off can't even begin to compare."
    mc "Holy fuck!"
    mc "Holy fucking fuck!"
    off "Holy mother of god."
    off "That was intense."
    off "I came... But she didn't."
    off "I can feel her disappointment."
    mc "I'm so sorry, I couldn't..."
    sf "It's ok... Oh, God... It's ok..."
    off "I'm a fucking disgrace."
    off "I can't let her down like that..."
    mc "I can keep going..."
    sf "What?"
    sis "Really?"
    mc "At least I can try..."
    off "I grab [sf_name]'s legs and lift them."
    off "I lock them behind my elbows."
    off "She seems surprised at first but immediately goes back to moaning as I resume the pumping."

    scene ep5_sc25_sr_49

    off "She clutches on my buttcheeks with both hands."
    off "My pleasure turns to pain."
    off "My whole shaft burns."
    off "It is as if my dick was pierced by hundreds of thorns."
    off "But I don't care."
    off "I grit my teeth and carry on."
    off "I thrust as hard and as fast as I can."
    off "Pumping into her vagina full of my cum feels funny."
    sf "Ooooh! Yeeeeeeees!"
    off "I surprise myself."
    off "As [sis_name] asked, I fuck [sf_name] as if I wanted to break her."
    off "Hard and deep."
    off "And she seems to like that a lot."

    scene ep5_sc25_sr_49_bis

    off "Her breasts jiggle gently right under my chest."
    off "She's beautiful."
    off "Fuck, I love that."

    scene ep5_sc25_sr_49_bis_bis

    off "I love that girl."
    off "How the hell can I be so lucky?"
    off "I want to make her come so bad..."
    off "After a minute, she doesn't moan anymore."
    off "She yells."
    sf "Haaaaaaaaan! Haaaaaaaaaan!"
    sf "Ooohh! Mhhhhhhhhhhh !"
    sf "Ooh my Gooooooooood!"
    off "The pain subsides just as she squeezes my cock inside her."
    off "It's like if her pussy was trying to milk my dick."
    off "I have barely any strength left but I keep pumping as deep and hard as I can."

    scene ep5_sc25_sr_50

    off "She arches and gasps."
    off "I feel like I could ejaculate again."
    off "I just have to push a little further."
    off "Completely relaxed, [sf_name] lets herself go."
    off "She still moans softly with her every breath but doesn't move a bit."
    off "It's as if she's gone somewhere else while I finish job."
    off "I ruin her pussy twice in a row."
    off "She shivers from time to time."
    off "I last one more minute before I gift her with another load."
    off "My whole shaft is burning."
    off "I feel like my balls are being sucked dry."


    scene ep5_sc25_sr_51

    mc "Haaaaan! Holy shit!"
    off "Pleasure comes and goes faster than the first time, mixed with pain."
    mc "Haaan!"
    off "I clumsily pull out and fall on the bed."
    off "I'm completely exhausted."
    off "Out of breath, out of strength."
    off "Done."
    off "And my genitals are roasted."
    off "I came twice in a 10 minutes span."
    off "Maybe less."
    off "I ejaculated too soon, but I recharged pretty quickly."
    off "I don't know if I should be proud of it or sad."
    off "I need to work on my stamina."

    scene ep5_sc25_sr_52

    sis "Did you just came inside her, TWICE?"
    sis "I told you she's not on the pill!"
    sis "What is so hard to understand?"
    mc "But she said..."
    sf "It's ok..."
    sf "I'm sure it's a safe day..."
    off "[sf_name] sounds exhausted, about to sink into sleep."
    off "[sis_name] gets closer to her and tenderly caresses her belly."
    sis "Are you sure?"
    sf "I have an appointment tomorrow anyway..."
    sf "Don't worry about it..."
    sis "Ok..."
    sis "So... How was it?"
    sf "Big."
    off "They both laugh."
    sf "And deep..."
    sf "And it feels... way better than the purple one."
    sis "You came hard..."
    sf "I did, yes."
    sf "That was incredible."

    scene ep5_sc25_sr_53

    off "It seems that I didn't fail everything in the end."
    scene ep5_sc25_sr_53_bis
    off "Holy shit."
    scene ep5_sc25_sr_53_bis_bis
    off "I just had sex with [sf_name]."
    off "And I came inside her. TWICE."
    off "I'll have to tell Steve about that."
    off "There's no way I'm keeping that to myself."
    off "Let's rest a minute while they debrief."
    off "They keep talking about how my dick stretched her insides."
    off "It's as flattering as disturbing."

    scene ep5_sc25_sr_54

    sf "Oh, I'm sorry but... could you get me some tissues?"
    sf "I should go to the bathroom... But I don't think that I'll be able to move for a few more minutes..."
    sf "And it feels like I'm leaking... it's very embarrassing..."
    sis "Oh! Oh my god!"
    sis "Yes, of course!"
    sis "I'll find something."
    sis "I'll be right back."
    off "She jumps off the bed and rushes out of the room."

    scene ep5_sc25_sr_55

    off "We can hear her rummaging in the bathroom."
    off "I'm afloat, like in a dream."
    off "Everything is a bit blurry and soft."
    off "I really did a number on her."
    off "Shit, I fucked her senseless in the end."
    off "Did I overdo it?"
    off "She seemed to like it though..."
    off "I mean... She came, right?"
    off "That means she enjoyed it, right?"

    menu:
        "I'm sorry [sf_name]...":
            mc "I got carried away in the end..."
            mc "I didn't want to be so rough..."
            mc "But [sis_name] told me to go hard... so I thought..."
            sf "It's ok, [mc_name]."
            sf "Don't worry."
            sf "[sis_name] was right, but... having an orgasm isn't necessarily the definition of making love."
            sf "Next time, maybe we could... do it softer?"
            mc "That would be great, yes."
            off "You're such a moron, [mc_name]."
            sf "I love you, [mc_name]."
            off "Oh, shit."
            off "As soon as I hear her say those words I know I've fucked up."
            mc "I love you, [sf_name]."
            $ ProcessStat(1, "sf_affection")
            $ DumpNotStack()
            off "I mean these words but I should have told her that sooner."
            off "Way sooner."
            off "I'll have to make up for that."
        "I love you, [sf_name]. [sfLovePath]":

            $ ProcessStat(5, "sf_affection")
            $ DumpNotStack()
            $ ep5dlclove = True
            off "I mean these words. It's so obvious."
            off "Was that a sob I just heard? Is she crying? Maybe telling her that was a mistake after all."
            sf "I love you, [mc_name]."
            off "Or maybe not."
            mc "I'm sorry, I should have told you sooner."
            sf "It's ok. I had no doubt."
            mc "I'm sorry, I feel like I have been a bit too rough... I got carried away..."
            sf "It's ok. We'll do it softer next time."
            mc "That would be great, yes."

    off "[sis_name] storms back into the bedroom, victorious."

    scene ep5_sc25_sr_56

    sis "Look what I've found!"
    off "She jumps on the bed and gets to work."
    sis "Let me do it."
    sf "It's ok..."
    sis "Holy shit, he filled you up... there's so much..."
    sf "I'll go to the bathroom in a few minutes..."
    off "Their voices are getting distant."
    off "They're whispering."
    off "That bed feels nice and comfortable."
    off "I'm so tired."
    off "I need to rest a bit before I can take care of [sis_name]."
    scene black with dissolve
    off "Yeah..."
    off "I'm going to close my eyes just a minute."
    off "Yeah..."
    off "Feels good..."


    return



label day5end:

    scene black with dissolve
    with Pause(2)
    show text "End of Day 5" with dissolve
    with Pause(2)
    scene endscreen with dissolve

    menu:
        "This is the end of Day 5. You may want to save here."
        "Exit to main menu.":
            $ MainMenu(confirm=False)()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
