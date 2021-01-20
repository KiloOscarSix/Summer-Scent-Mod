

label day1start:


    scene black with dissolve
    with Pause(2)
    show text "Day 1 - Saturday" with dissolve
    with Pause(2)
    show text "The afternoon" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(2)
    show ep1px0001


    off "This is me. Relaxing by the pool."
    off "I just graduated and summer is starting nicely."
    off "My parents are gone for a week."
    off "Some symposium thing for my dad, my mom tagging along."

    python:
        mc_name = renpy.input("What is your name?")
        mc_name = mc_name.strip()

        if not mc_name :
            mc_name = "Jack"

    off "My name is [mc_name]."
    off "And this week could be great if someone wasn't bothering me."

    python:
        sis_name = renpy.input("What is her name?")
        sis_name = sis_name.strip()

        if not sis_name :
            sis_name = "Eve"

    hide ep1px0001
    show ep1px0002:
        subpixel True
        yalign 1.0
        linear 5.0 yalign 0.0

    with Pause(2)
    off "This is [sis_name]."


    off "She's my childhood friend."
    off "My dad was a close friend of her father."
    off "We are the same age and we grew up together, playing together, going to the same schools and the same classes."
    off "Her parents died in a car accident when we were nine years old."
    off "Without any family left, she was alone. So we took her in."
    off "She's part of the family now. She's like a sister to me."





    off "According to most of the people out there, I'm an asshole."
    off "But really, I'm the good guy here."
    off "On the other hand, [sis_name] is the real bitch."
    off "She was a nice girl until she entered high school."
    off "Then, out of nowhere, she transformed into some kind of drunken slut."
    off "The school headmaster even called my parents three or four times to complain about her behavior."
    off "She denied it at first and then just didn't give a fuck."
    off "Sucking dicks in the restroom, fucking random people, drinking, cheating, fighting and all that kind of thing."
    off "Last month she damaged mom's car while coming back drunk from a party."
    off "She's that kind of girl and she doesn't give a shit about what people say."
    off "And to make things even better, she hates me."
    off "She sees me as some kind of moron who doesn't understand shit."
    off "She has no consideration for me whatsoever."
    off "It's hard not to give her back all these nice feelings."
    off "When we were younger, our relationship was very different."
    off "We were close, like partners in crime."
    off "Doing everything together, sharing every moment."
    off "And then we grew up. And she became a bitch who's only motive in life is to ruin every day of my existence."

    hide ep1px0002
    show ep1px0003

    sis "Hey."
    mc "Hey Princess."
    off "My dad took the habit of calling her Princess when she was still a cute little girl."
    off "I somehow copied him and it stayed to this day, even if she doesn't really behave anything like a princess."

    hide ep1px0003
    show ep1px0004





    sis "I invited a friend to spend the week with us. She should be here in half an hour or so."
    python:
        sf_name = renpy.input("What is the name of her friend?")
        sf_name = sf_name.strip()

        if not sf_name :
            sf_name = "Cassie"

    call walkthroughVars

    mc "Let me guess... [sf_name]?"
    mc "The whole week?"
    sis "Do you have a problem with that?"
    mc "None. I'm sure she'll lighten the mood."
    off "[sf_name] is [sis_name]'s best and probably only friend. We have known her for years."
    off "There's a lot of rumours going around about [sf_name]."
    off "Most of them telling that she's as slutty as [sis_name]."
    off "However, I'm sure it's all bullshit."
    off "You just have to look at her to understand she's not that kind of girl."
    off "She is much more refined and agreeable than [sis_name]. She is mischievous and playful."
    off "I feel like she likes to play with people and I'm sure she knows how to manipulate her surroundings to get what she wants but she's clearly a nice girl."
    sis "I need you to go buy something to drink."
    off "I'm laughing."
    mc "Sure, I'll do your errands for you. Obviously I'll pay for everything. Anything else Princess? Please, ask."
    sis "Can't you stop being an asshole for once? I'm asking you to do me a favour."
    sis "You could be nice and help me. You could like that."
    mc "Yeah. And what about you being nice to me?"
    mc "And why do you need alcohol in the first place? Can't you drink water, juice or soda?"
    mc "I'm pretty sure [sf_name] can live without booze in the afternoon."
    mc "What about you? Are you an alcoholic or what?"

    hide ep1px0004
    show ep1px0005

    sis "You know what? Fuck you. We'll manage something. I don't need you. Neither your help nor your money."
    mc "Sure. May I help you remember the rules? Dad's reserve is off limits to you."
    mc "As is Mom's car. And you have to study for the catch-up session in September."
    off "I graduated. She failed."
    off "Our summers are going to be very different."
    sis "You missed your chance [mc_name], once again."
    mc "Sure. That's my thing. You remember? I'm a loser."
    mc "And that swimsuit doesn't suit your ass."

    hide ep1px0005
    show ep1px0006

    off "It's always the same story. She asks for help, I comply, and afterward she's still a bitch to me."
    off "I have some money, because I worked my ass off in a garage every weekend this year."
    off "In the meantime she was spending her time doing whatever she wanted."
    off "She deserves this..."

    hide ep1px0006
    show ep1px0007

    off "Fuck."
    off "If I help her, I get nothing but disdain."
    off "If I refuse, I feel like I'm the asshole she thinks I am."
    off "Either way, I'll be angry with her and with myself."
    off "I had enough of this shit. She needs a good spanking."

    menu:
        "Anyway..."
        "Help her. [gr][modSisHelped]":

            off "Why am I doing this to myself?"
            jump ep1help
        "She can go fuck herself. [red][modSisHelped]":
            off "I'm pretty sure she'll enjoy it."
            jump ep1nohelp

label ep1help:
    scene ep1px0008

    python:
        ep1sishelped = True

    off "I quickly get dressed and head to the garage. My mother's car is parked there."
    off "[sis_name] is forbidden to drive it for the whole summer, but I can use it freely."

    hide ep1px0008
    show ep1px0009



    off "There's a small convenience store nearby. It'll have everything I need."
    off "We live on the outskirts of the city, on the heights, but we are not so far from the commercial areas."
    off "It's only a five minute ride."
    off "The heat wave that paralyzes the country has almost completely emptied the streets."
    off "Thank God this car has efficient air conditioning."

    hide ep1px0009
    show ep1px0010

    off "The store is small but it packs all the essentials."
    off "She didn't tell me what kind of beverage she wanted."
    off "I should give her a quick call."
    off "..."
    off "Fuck. I forgot my smartphone."
    off "I'll have to choose by myself."
    menu:
        "Alright. What do I buy?"
        "Beer [sisLovePath]":

            show beer
            "Beer. Beer is always the right choice."
            python:
                ep1beer=True
            hide beer
        "Vodka":
            show vodka
            "That does look pretty brutal. Things could get interesting."
            python:
                ep1vodka=True
            hide vodka
        "Wine [sfLovePath]":
            show wine
            "Wine is a bit too elegant for my Princess but [sf_name] would appreciate it."
            python:
                ep1wine=True
            hide wine

    off "Ok. That should do the trick."
    off "I have a bad feeling about this, but she asked for it."

    hide ep1px0010
    show ep1px0011


    off "On my way back home, I notice a familiar figure on the sidewalk along the road."
    off "That's some seriously hot ass right there. I like that skirt."
    off "I have fantasized enough about this body to recognize it at first glance."
    off "That's [sf_name]."
    off "She's probably walking to the bus stop."
    $ modSFRide = "[{}Ride]".format(sf_name)
    menu:
        "Should I give her a ride?"
        "Let's be a gentleman. [gr][modSFRide]":
            hide ep1px0011
            show ep1px0012
            python:
                ep1sfride=True
            mc "Hello my lady. Can I be of assistance?"
            mc "May I drive you to your destination?"
            jump ep1sfrided
        "I'm sure she enjoys walking. [red][modSFRide]":

            python:
                ep1sfwalk=True
            off "She could not have such a fine ass without some regular exercise."
            hide ep1px0011
            show black

            jump ep1sfwalked

label ep1sfrided:

    sf "[mc_name]! Hi! That's so kind of you."
    $ ProcessStat(1, "sf_affection")
    $ DumpNotStack()
    scene ep1px0013
    mc "I saw you on the sidewalk and I knew you were coming to our house."
    mc "I could not do otherwise."
    sf "No, really, if you had not stopped, I think I'll be dead from the heat."
    sf "The sun is too hot for my taste."
    sf "I'll be sure to thank you properly but in the meantime..."

    sf "Thank you sir."
    mc "You are very welcome."



    scene ep1px0014
    off "I park the car in the garage and head to the house with [sf_name] by my side."
    sf "You are so lucky to have a pool."
    sf "I am very grateful to you for letting me enjoy it."
    mc "You can come whenever you want."
    mc "I'm sure [sis_name] already told you that."
    sf "She did. But I like it better when you are the one to say it."
    mc "Well then, you can enjoy the pool as much as you want and if it's too hot, the house is air-conditioned and you're at home."
    sf "You should not tempt me dear, or I may very well spend the whole summer in here."
    mc "As I said, you are welcome to stay as long as you want."
    sf "Thank you. I'll keep that in mind."


    off "She smiles, she laughs."

    hide ep1px0014
    show ep1px0015
    off "We find [sis_name] in the living room. She's taking a quick nap on the sofa."
    sf "Should we wake her up?"
    mc "This is her superpower. She can sleep anywhere, anytime."
    sf "Doesn't she looks like Sleeping Beauty to you? You should try to kiss her and see what happens."
    mc "I can feel her murderous intent towards me from here."
    sf "Come on [mc_name]. You know she's not really like that. It's just a facade."
    mc "I have yet to unveil that caring face of her you are talking about."
    sf "I wonder. Should I help you love each other? You seem to need assistance."
    mc "There's nothing to help. She hates me. That's all."
    sf "Obviously, you don't know what you're talking about."

    off "She smiles and bends over to kiss [sis_name] on the cheek."
    off "[sis_name] slowly opens her eyes and stretches with a smile before getting up to greet [sf_name]."

    hide ep1px0015
    show ep1px0016


    sf "Hi [sis_name]. [mc_name] was kind enough to save me from the harshness of the sun on his way back home."

    sis "He did well."
    mc "It was my pleasure. I also did a little hop by the convenience store."
    mc "I am sure you will use this with moderation."

    off "[sis_name] looks into the paper bag."


    if ep1beer == True:
        sis "Nice! That's my favourite beer brand. How did you know?"
        mc "I didn't. It's just my favourite one too."

        $ ProcessStat(1, "sis_affection")
        $ DumpNotStack()
    elif ep1vodka == True:
        sis "Vodka? Really? For an afternoon drink by the pool?"
        mc "Sorry, that may not be a good idea. I didn't know what to take ..."
        sis "It's ok, we have some juice. I'll do some cocktails."
    elif ep1wine == True:
        sis "Wine? Really? For an afternoon drink by the pool?"
        sf "Well it may be a little too soon for it but I like wine, we can save it for later. I'm sure it will do nicely."

        $ ProcessStat(1, "sf_affection")
        $ DumpNotStack()
    sf "Can I use your bathroom to get changed in something more appropriate to the pool?"
    mc "Sure, you don't have to ask. I'm sure you know the way."
    sf "Thank you sir. You are most kind."

    off "[sf_name] leaves the living-room with a smile on her face."
    hide ep1px0016
    show ep1px0017
    off "[sis_name]'s expression suddenly hardens "
    sis "Are you flirting with my friend?"
    mc "No more than usual."
    sis "If you dare try anything..."
    mc "Do you remember I just bought you enough alcohol to get miserably drunk in front of your friend?"
    sis "I was about to thank you for that."
    mc "No, you were about to threaten me for something I had no intention of doing."

    hide ep1px0017
    show ep1px0019
    mc "You missed your chance. Once again."
    mc "Have fun enjoying the pool, Princess."
    jump ep1livingafternoon

label ep1sfwalked:

    scene ep1px0018


    off "I park the car in the garage and head to the house."

    hide ep1px0018
    show ep1px0015


    off "I find [sis_name] in the living room. She's taking a quick nap on the sofa."

    hide ep1px0015
    show ep1px0020

    off "I'm coming closer in order to wake her up."

    menu:
        "..."
        "She does not seem so mean when she sleeps.":
            off "She almost looks innocent."
            off "I wonder why we can't stand each other anymore. I miss the time when we were best friends."
            off "She's pretty when she's not screaming at me."
        "This bitch sleeps well.":

            off "Her lips are very tempting but she has probably already sucked countless cocks."
            off "Her pussy has probably seen so much action."
            off "What a slut."

    off "She's waking up."
    off "I quickly move away to a safe distance."

    hide ep1px0020
    show ep1px0017

    sis "Hey..."
    mc "Hey..."
    sis "So you ..."
    mc "I did a little hop by the convenience store."
    mc "I am sure you will use this with moderation."

    if ep1beer == True:
        sis "Nice! That's my favourite beer brand. How did you know?"
        mc "I didn't. It's just my favourite one too."

        $ ProcessStat(1, "sis_affection")
        $ DumpNotStack()
    elif ep1vodka == True:
        sis "Vodka? Really? For an afternoon drink by the pool?"
        mc "Sorry, that may not be a good idea. I didn't know what to take ..."
        sis "It's ok, we have some juice. I'll do some cocktails."
    elif ep1wine == True:
        sis "Wine? Really? For an afternoon drink by the pool?"
        mc "Sorry, that may not be a good idea. I didn't know what to take ..."
        sis "Maybe with some ice in it? [sf_name] like wine anyway so... we'll see ..."

    mc "Then, I'll let you enjoy the pool with your friend."
    hide ep1px0017
    show ep1px0019
    sis "Hey, [mc_name]... Thank you."
    mc "You're welcome."
    jump ep1livingafternoon

label ep1nohelp:

    off "She ruined the mood of my afternoon."
    off "She has a talent for that."
    off "And that's just the beginning. She's going to piss me off all week."
    off "I'm sure she's already preparing her next bullshit."
    scene ep1px0021

    off "Of course, I find her rummaging in the parents' bottles."
    mc "You cannot be serious."
    sis "Fuck you."
    mc "Do you imagine that they won't notice that you drank their booze?"
    sis "That's ok. I'll replace the empty bottles before they come back."
    hide ep1px0021
    show ep1px0022
    sis "They will not notice... unless you betray me."
    menu:
        "I won't betray you. But I won't cover for you either.":
            sis "Yeah, yeah...as if I was counting on you to cover for me."
            off "I'll enjoy seeing you grounded until the end of time when mom and dad come back."
            $ ep1vodka = True
        "Maybe I will. If you piss me off. [sisSubPath]":


            sis "Are you threatening me?"
            mc "Do I need to threaten you? Will you behave nicely?"
            sis "Behave? Who do you think you are?"
            mc "The one you are pissing off, obviously."

            $ ProcessStat(1, "sis_submission")
            $ DumpNotStack()
            $ ep1vodka = True
        "Come on, Princess. I won't betray you. [sisLovePath]":

            mc "They will discover it without my help."
            mc "If you intend to replace the bottles, do not empty the expensive bottles."
            mc "You will never find anything to replace this 18 year old scotch nor this French liquor."
            mc "Vodka will be easy to put back, and it's cheap."
            sis "... Thank you for the advice."
            mc "You are welcome."
            $ ep1boozeadvice=True

            $ ProcessStat(1, "sis_affection")
            $ DumpNotStack()
            $ ep1vodka = True

    hide ep1px0022
    show ep1px0023
    mc "Well, anyway..."
    mc "Your choice, your responsibility."
    mc "Enjoy your afternoon."



label ep1livingafternoon:

    scene black with dissolve
    with Pause(2)
    show text "Later this afternoon." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(2)

    off "I spend time in the living room."
    off "The comfort of the sofa and a good TV series under the refreshing air conditioning leaves me relaxed and in a better mood."
    show ep1px0024

    off "I ended up watching a TV show with the main character banging his own aunt without knowing they were relatives."
    off "Let's be honest. If I had an aunt as young and sexy as this one, willing to be fucked, I would probably have banged her even if I had known."
    off "Incest is pretty trendy since this TV show started..."


    off "I'm about to go to my room when [sf_name] enters the room."
    hide ep1px0024
    show ep1px0025

    off "Holy shit, that girl..."
    off "As she approaches, I notice she does not wear any makeup."
    off "She looks fresh, innocent and pure. Her face is almost childish, as if she had just come out of her childhood."
    off "The contrast with her voluptuous body is simply striking. I could easily fall for her. Every one falls for her."
    off "It's like she's not letting you have any other choice. You just have to fall for her."
    off "You will love her and despair."
    off "Because even if she enjoys to be loved, she has no interest in loving you."
    hide ep1px0025
    show ep1px0061
    off "She constantly flirts in that innocent manner of hers."
    off "She maintains doubt and hope, but rejects all the guys who dare to ask her out."
    off "She is like a goddess of whom one can only dream."
    off "Of course, not everyone accepts rejection with a smile."
    off "The most resentful call her the queen of sluts."
    off "Some have started rumours about her. But nothing can stain her."
    off "She drives me crazy."
    off "Look at those lips."
    off "Is she talking to me?"
    off "Shit. She's talking to me. How long have I been spacing out?"

    if ep1sfride==True:
        sf "... I just wanted to thank you again for saving me the bus ride and the walk."
        mc "You don't have to. It was my pleasure."
        sf "It was nice of you anyway."
        sf "[sis_name] keeps telling me you are a jerk but I suspect she just wants to keep you for herself."
        mc "She and I are not in the best terms."
        sf "Yet, you helped her."
        mc "Yeah ... I must be a fool..."
        off "She laughs."
    else:


        sf "... so I just wanted to say Hello."
        mc "Hello then. I hope you are doing fine."
        sf "I'm doing my best to survive the heat. I hope you do not mind my presence here."
        mc "Not at all."
        mc "You can enjoy the pool as much as you want and if it's too hot, the house is air-conditioned and you're at home."
        sf "You should not tempt me dear, or I may very well spend the whole week in here."
        mc "As I said, you are welcome to stay as long as you want."
        sf "Thank you. I'll keep that in mind."


    sf "By the way, what do you think of my new swimsuit?"

    hide ep1px0061
    show ep1px0026:
        subpixel True
        yalign 1.0
        linear 5.0 yalign 0.0

    sf "I bought it specially for this week."
    sf "What do you think?"

    menu:
        "..."
        "I like the skulls, that's... cute... I guess.":
            sf "Really? I like them too. It's pretty far from my usual style but I like it."
            mc "Honestly, on anyone else, that would be ridiculous. But with you, it looks great."
            sf "I'm glad you like it."

            $ ProcessStat(1, "sf_affection")
            $ DumpNotStack()
        "It suits you.":

            mc "But I'm pretty sure that anything would look good on you."
            sf "What do you mean?"
            mc "Your figure is flawless. Every one would be looking at you, not at your swimsuit."
            sf "Well, that sounds a bit over exaggerated but I'll take the compliment none the less."
            sf "You know [mc_name], girls like compliments, and they like being admired."
            sf "But mindless worshiping is simply boring."
            mc "I do not worship. I was merely asserting a fact."
            sf "A pleasant one."

            $ ProcessStat(1, "sf_affection")
            $ DumpNotStack()

    sf "Anyway, your kindness deserves a reward."

    hide ep1px0026
    show ep1px0028
    off "The kiss lasts a few seconds."
    off "I can smell the subtle and sweet perfume of her skin."
    off "My cock hardens instantly."
    hide ep1px0028
    show ep1px0027
    sf "I'm going back to the pool. See you later!"
    mc "Yeah... See you later..."
    off "She gave me an erection with a simple kiss on the cheek."
    off "I am a total moron."
    off "This girl is toying with me like I'm nothing..."

    scene black with dissolve

    jump ep1aftmcroomphone

label ep1aftmcroomphone:
    scene black with dissolve
    with Pause(2)
    show text "Later in my room..."
    with Pause(2)
    hide text
    off "I'm thinking about taking a nap when my smartphone rings."
    show ep1px0029 with dissolve
    off "It's Steve. That dude is probably my best and only friend."
    off "He's currently away on a vacation on some paradise beach with his parents."
    mc "Hey Steve."
    mf "Hey Dude!"
    hide ep1px0029
    show ep1px0031
    mc "What's up by the ocean?"
    mf "Dude, this is crazy."
    mf "You should see it. Asses and tits everywhere. Girls here barely wear anything."
    mc "It's called swimsuits I guess."
    mf "Yeah, but some are so tiny that their very existence is barely enough to deserve a name."
    mc "Sounds like you're enjoying yourself there."
    mf "You have no idea. I have been here for three days and I already got to third base with a nice girl I encountered on the beach."
    mf "And tonight's gonna be even hotter. We're going to take a midnight swim."

    menu:
        "..."
        "I guess we're not talking about love here... [gr]\[Romantic\]":
            mf "Love?"
            mc "Yeah, never mind."
            mf "You are a romantic. Girls are not into that kind of thing anymore."
            $ ep1romantic = True
        "You do know that your right hand is not a real girl, do you?":
            mf "Believe me or not, tonight I'm gonna shag some nice pussy."
            mc "That lady sure is lucky."
            mf "Indeed."

    mf "Anyway, how are you holding up back there?"
    hide ep1px0031
    show ep1px0030
    mf "Are your parents already gone for their symposium thing?"
    mc "Yup. They departed this morning."
    mf "That's a shame. If I wasn't away, we could have set up some crazy party by your pool."
    mc "I'm not sure I would have agreed with that kind of project."
    mf "That's because you are a shy one."
    mc "If you say so."
    mf "So what? You just stay alone and do nothing? What's [sis_name] doing?"
    mc "Right now, she's laying by the pool with her friend. She invited [sf_name] for the week."
    mf "What?! [sf_name] is at your place right now?"
    mc "Yup. I'm looking at them right now."
    hide ep1px0030
    show ep1px0032

    mf "Dude I envy you. You are going to spend the whole week with [sis_name] and [sf_name]."

    mf "Your summer could turn out more interesting than mine."
    mc "What are you talking about?"
    mf "Are you telling me that you're going to let this week pass without trying anything?"
    mc "What do you want me to do?"
    hide ep1px0032
    show ep1px0033
    mf "Come on, stop playing dumb. Do I have to draw you a picture?"
    mf "Take your chance with one or the other, or both! At least try something! It's a matter of honour."

    mc "Are you insane? [sis_name] is like a sister to me and [sf_name] ... well, it's [sf_name]. If I try anything, she will reject me for sure."
    mc "There's nothing to try, aside from drowning myself in shame, disgust and humiliation."
    mf "You are the one who's insane. Who cares about that kind of thing nowadays?"
    mf "[sis_name] is so hot that I would sell my soul for a round with her."

    mc "Hey. Did I mention she's like a sister to me?"
    mf "Yeah. And it only makes it hotter."
    menu:
        "Hotter?"
        "You are disgusting. [gr]\[Disgusted\]":
            $ ep1disgusted = True


            mf "You two are not that close. Nothing is really stopping you."
            mc "She will kill me then tell my parents who will also kill me."
            mc "And still. Even thinking about it is weird."
            mf "Weird good or weird bad?"
            mf "My money's on weird good."
            mc "Just weird."


            mf "She's smoking hot, don't even try to deny it."
            mf "And that kind of relationship is trendy right now. No fear."
        "You would fuck your own sister?":

            mf "Why not? If she's hot and willing ..."
            mc "I don't know man... It's gross."
            mf "It's two people having sex. There's nothing gross about that."
            mf "You'd neither be marrying nor having babies, unless you're stupid. It's just sex."

    mc "Yeah I get the idea. She's hot, nothing else matters."
    mf "My point exactly."
    hide ep1px0033
    show ep1px0034
    mf "And for [sf_name], the two of you probably won't go to the same college next year, so if there is humiliation, it will not survive the summer."
    mf "You don't have any valid reason not to try anything."
    mc "You are crazy."
    mf "Dude, it's your duty as a man. I'm counting on you."
    mf "Be proud, be strong and show those sweet pussies who's the boss of that house."
    hide ep1px0034
    show ep1px0031
    mc "Do we live in the same world? I often feel that we do not live by the same rules and the same consequences."
    mf "We are young, in the middle of a hormonal storm going on 24 / 7."
    mf "Fuck every one, fuck every where, fuck as much as you can and enjoy every moment of it."
    mf "Rules and consequences are for later when you'll get old."
    mc "Dude, 6 months ago you were still a virgin and now you're talking like some batshit crazy philosopher after some weird sexual epiphany."
    mc "Are you high or something?"
    mf "You only live once. You should YOLO everything."
    mc "... okay ... I'll make sure to think about it."
    mf "Good. I have to go. I'll call you in a couple days. You better have made some progress."
    mc "YOLO."
    mf "YOLO."

    off "That crazy bastard..."

    scene black with dissolve
    with Pause(2)
    show text "30 minutes later ..."
    with Pause(2)
    hide text

    off "The dull sound of a shock attracts me into the hallway."
    label galleryScene1:
    scene ep1px0035 with dissolve
    off "There is no one here but the bathroom door is half open."
    off "I can hear the flowing water."
    off "Can someone have slipped in the shower?"
    menu:
        "Should I take a look?"
        "Yes. For safety reasons, of course... [sfLovePath]":
            $ ep1sisspied = True
            off "Someone may be injured."
            off "I'm just going to peek to assess the situation."
            off "No reason to look more than necessary, right?"
            hide ep1px0035
            show ep1px0036
            off "Holy shit."
            off "That's not quite what I hoped for but ..."
            hide ep1px0036
            show ep1px0049

            $ UnlockThat("ep1/ep1px0049")
            off "It's strange."
            off "I see her every day in a swimsuit that does not cover much of her skin, but ... I never realized that she was so ..."
            off "Damn."
            off "Steve is right."

            off "She is hot. [sis_name] is hot."
            off "This ass is pretty much perfect. And those legs ..."
            off "What am I doing here?"
            off "I'm going crazy."
            hide ep1px0049
            $ renpy.end_replay()
            show ep1px0036
            off "What kind of pervert am I?"


            off "I should get out of here before I get caught peeping on [sis_name]."

            sf "Hey [mc_name], are you enjoying the view?"
            hide ep1px0036
            show ep1px0037
            off "She says that with a playful smile on her lips."
            off "What do I say?"
            off "Come on [mc_name], find something smart."

            menu:
                "I heard a noise and...":
                    mc "... well..."
                "It's not what you think...":
                    mc "The door was open..."

            sf "And you decided to go see if the naked girl in the shower needed your help."
            sf "Is that it?"
            mc "Well.. Yes ... Somehow..."
            sf "She's beautiful, isn't she?"

            menu:
                "She's not.":
                    off "[sf_name] lightly frowns."
                    sf "I don't know if you are a liar or a moron. Either Way you need to open your eyes."
                "I'll have to admit that she is. [sfLovePath]":
                    $ ep1brhonest = True
                    $ ProcessStat(1, "sf_affection")
                    $ DumpNotStack()
                    sf "Do you find her prettier than me?"
                    menu:
                        "I can smell the trap. Time for a diplomatic answer."
                        "Well .. none of you is prettier. [sfLovePath]":
                            mc "Each of you are beautiful in your own ways."
                            sf "That sounds like a good answer."
                            off "Thank God."

                            $ ProcessStat(1, "sf_affection")
                            $ DumpNotStack()
                        "I think you still have the upper hand...":
                            sf "Really? Do you want to look at her some more?"
                            sf "She's obviously prettier. I'm jealous of her."
                            mc "I don't think so..."
                            sf "And I think you are a liar. But it's alright. We all are."


            sf "You look kind of embarrassed. It's ok. It's no big deal."

            sf "You just got caught peeping on your naked friend showering."

            sf "Does she turn you on?"

            menu:
                "No.":
                    mc "She's like a sister to me. How could she turn me on?"
                "No!":

                    mc "She's like a sister to me! Are you crazy?!"
                "She's like a sister to me. [sfLovePath]":


                    $ ProcessStat(1, "sf_affection")
                    $ DumpNotStack()
                    sf "Is that disappointment that I hear in your voice? I'll take that as a yes."

            sf "Look at her. Don't you want to join her?"
            menu:
                "Trap number 2 incoming"
                "No! Why would I ...":
                    sf "No? Then you're missing out on something."
                "No, thank you.":
                    sf "No? Then you're missing out on something."
                "It's tempting but I'll have to decline. [sfLovePath]":

                    $ ProcessStat(1, "sf_affection")
                    $ DumpNotStack()
                    sf "Too bad. It could have been interesting ..."

            hide ep1px0037
            show ep1px0038
            sf "I'm joining her myself."
            sf "See you later [mc_name]."
            off "Yeah... later..."
            hide ep1px0038
            show ep1px0039
            off "What has just happened?"
            off "I got caught watching [sis_name] showering."
            off "I have been a complete fool from start to finish."
            off "I was totally ridiculous."
            off "But wait ... [sf_name] didn't look angry ... She seemed to ... find that situation... funny..."
            off "And ... she joined her? In the shower?"
            off "What is happening here?"
            off "Is it normal for girls to shower together?"
            off "Or do these two have this kind of relationship?"
            off "I'm having a boner, again."
            off "I'd better stop fantasizing like that."
            off "I'll hide my shame in my room."
        "No. It would be totally inappropriate.":

            off "Whoever is in this bathroom right now surely value her privacy."
            off "I'd better go mind my own business."

    scene black with dissolve
    with Pause(2)

    off "An hour later, I can hear the car going out of the garage."
    off "[sis_name] is not allowed to take the car but she obviously does not care."
    off "At first I am angry at her carelessness, then I indulge in indifference, telling myself that watching over her is not my responsibility."
    off "It's her life."

    scene black with dissolve
    with Pause(2)
    show text "3 am that night."
    with Pause(2)
    hide text

    show ep1px0046 with dissolve
    off "Something wakes me up in the middle of the night."
    off "I quickly understand that the girls are back."
    off "I can hear [sf_name]'s voice and a loud thump then nothing."
    off "Something is wrong."
    off "I get up and make my way to the entrance."
    hide ep1px0046
    show ep1px0040
    off "Looks like someone is dead drunk."
    off "How surprising."
    off "[sf_name] looks pretty worried."
    mc "Hey [sf_name]."
    off "She turns to me, her expression conveying a mixture of distress and relief."
    hide ep1px0040
    show ep1px0041
    sf "Hey [mc_name]. I'm sorry we woke you up."
    mc "Don't be. I wasn't sleeping."
    off "I'm obviously lying and she can see it."
    mc "What happened? Has she drunk herself to the point she can't even walk anymore?"
    sf "I'm sorry, I don't know what happened."
    sf "She usually manages her drink far better than that."
    sf "I don't think she even drank that much, but she collapsed anyway."
    sf "The bouncer helped me put her in the car and I drove back here."
    mc "You don't have to be sorry for her drinking. She makes her own choices."
    sf "This is the first time I've seen her like this. I am a bit worried."
    mc "Well, this is the first time I've seen her like this too."
    mc "But I have heard enough about her excessive drinking from her arguments with mom and dad to not be surprised now."
    mc "At least you were there to bring her back. Thank you."
    mc "Anyway, let's put her to bed."
    mc "I'll carry her to her room."
    sf "Thank you. I don't know what I would have done without you."
    sf "I'll open the doors for you."
    hide ep1px0041
    show ep1px0042
    off "I take [sis_name] in my arms and lift her off the ground."
    off "She sleeps so deeply that she doesn't even flinch when I lift her up."
    off "I was preparing to break my back under her weight but she is strangely light."
    if ep1sfwalk==True:
        off "Just like when she was sleeping in the living room this afternoon."
    off "She looks fragile and helpless."
    off "I was angry seeing her lying on the floor."
    off "But now that she's in my arms, being so vulnerable, I'm just worried about her."
    hide ep1px0042
    show ep1px0043
    off "She does not really reek of alcohol."
    off "Her hair exhales an apricot scent, probably her shampoo."
    hide ep1px0043
    show ep1px0044
    off "It's overwhelming, but behind that, I can still guess a sweet blend of vanilla and sunscreen."
    off "She smells like summer."
    off "Her skin is soft and warm."
    off "And honestly, up close, her cleavage is pretty nice."
    off "[sf_name] opens the door of the room and I gently put [sis_name] on her bed."
    hide ep1px0044
    show ep1px0045
    sf "Thank you [mc_name]. I can take it from here."
    sf "I'm going to undress her and put on something more comfortable on her, then I'll go get some sleep."
    sf "I hope she'll be better tomorrow."
    mc "Don't worry too much. It may be a bit extreme but I'm pretty sure this is not her first rodeo."
    mc "She's tough. She will manage."
    sf "Well, from my point of view, she's not managing much right now."
    mc "Indeed. The hangover will probably be a hard one."
    mc "So... If you don't need me anymore, I'm off to bed. Good night [sf_name]."
    sf "Good night [mc_name]."
    hide ep1px0045
    show ep1px0046
    off "Back in my room I can hear [sf_name] struggling to change [sis_name]'s clothes."
    off "She battles for at least ten minutes before calm returns."
    off "I can then hear her going to the bathroom."
    off "I'm suddenly wondering where will she sleep?"
    menu:
        "..."
        "I should go help her find a bed. [sfLovePath]":

            $ ProcessStat(2, "sf_affection")
            $ DumpNotStack()
            off "I get up quickly and meet her in the hallway."
            hide ep1px0046
            show ep1px0047
            mc "Hey [sf_name]."
            sf "Yes?"
            mc "I was thinking... You were supposed to sleep with [sis_name] but in her condition ..."
            sf "Yeah, it may not be safe ..."
            sf "I'll sleep on the sofa, in the living-room."
            mc "I can't let you do that. You can sleep in my parents' room."
            sf "I'm sorry, I don't feel comfortable with that idea..."
            mc "Then you can sleep in my bed."
            sf "In your bed?"
            mc "Yes. You take my room and I'll sleep in the living room."
            sf "You really don't have to do that."
            mc "It's okay. I won't be able to sleep knowing you have to endure the sofa. I prefer it this way."
            sf "Thank you [mc_name]."
            mc "You're welcome. Have a good night."
            off "I go to the living room and lie down on the couch."
            $ ep1mcsofasleep = True
            hide ep1px0047
            show ep1px0048
        "I'm sure she can manage. She's a big girl.":


            off "I'm sure she will find the sofa."

    off "I close my eyes and sleep is not long to come."
    label galleryScene2:
    scene black with dissolve
    with Pause(2)
    show text "Later that night."
    with Pause(2)
    hide text
    show ep1px0050 with dissolve
    off "I'm not sure I really slept but a noise wakes me up."
    off "I feel like there is someone in my room."
    off "What time is it?"
    off "I'd better go back to sleep, I have to get up early tomorrow morning."
    off "Wait. To get up early, for what?"
    off "Something seems to emerge from the shadows surrounding my bed."
    off "And I'm not even worried."
    hide ep1px0050
    show ep1px0051
    $ UnlockThat("ep1/ep1px0051")
    off "[sf_name] slowly approaches my bed. Naked."
    sf "Hello [mc_name]."
    mc "... Hello..."
    sf "I'm feeling lonely. Won't you keep me company?"
    mc "Well ..."
    sf "I saw you looking at me. Did you like it? I did."
    mc "... Ok..."
    sf "I'm a bit cold here. Can you warm me up?"
    mc "... Sure..."
    hide ep1px0051
    show ep1px0052
    $ UnlockThat("ep1/ep1px0052")
    sf "You seem a bit sad."
    sf "I'm going to cheer you up. Don't worry."
    sf "I know how to do that."
    sf "I thought about that all day long."
    sf "I touched myself whenever I could, thinking of your big fat cock."
    hide ep1px0052
    show ep1px0053
    $ UnlockThat("ep1/ep1px0053")
    off "She pushes me to lie on my bed."
    mc "That's.. nice..."
    sf "You are a bit shy. I like that."
    sf "I'm going to take good care of you."
    off "She gently licks and massages my dick."
    off "A couple seconds later, my shaft is hard as a rock."
    hide ep1px0053
    show ep1px0054
    $ UnlockThat("ep1/ep1px0054")
    sf "Nice and hard."
    sf "What do you want me to do with it?"
    sf "I would gladly suck on it but I can see in your eyes that you want something else."
    sf "You want my pussy don't you?"
    sf "Well ..."
    sis "Or maybe you want mine?"
    hide ep1px0054
    show ep1px0055
    $ UnlockThat("ep1/ep1px0055")
    off "Since when did [sis_name] get here?"
    off "She's there, naked, looking at her best friend licking my dick."
    off "And she just asked me to fuck her pussy?"
    off "I'm dreaming. This is definitely a dream."
    off "Can I fuck [sis_name] in my dream?"
    off "Is it still wrong?"
    off "That doesn't count, right? It's just a dream..."
    off "No one will know..."
    hide ep1px0055
    show ep1px0056
    $ UnlockThat("ep1/ep1px0056")
    off "They both lie at my side."
    off "[sis_name] grabs my dick still full of [sf_name]'s saliva and slowly masturbates me."
    sf "That's a good question. By the way, who do you prefer?"
    sf "[sis_name]? Or me? Who do you desire the most?"
    sis "You know he wants me."
    sis "He'll deny it but he always wanted me."
    sis "When he was younger, he used to touch himself under the shower, thinking of me."
    sis "Even if it disgusts him, he cannot stop thinking about my pussy."
    off "Shit. What do I do? What do I say?"
    off "It's a dream right? Just a nice dream ..."

    menu:
        "..."
        "I prefer [sf_name]...":
            jump ep1dreammenusf
        "I prefer [sis_name]...":
            jump ep1dreammenusis
        "Can't I have both?":
            sf "Do you really think you can handle the both of us?"
            sis "You only have one dick, so you have to choose who you want to do first."
            menu:
                "Then I'll do [sf_name] first...":
                    label ep1dreammenusf:
                    sf "I am the lucky one, Am I not?"
                    sis "I'm a little disappointed. I thought our little pervert here would choose me instead."
                    sf "You will not regret it. I know you've been coveting me for years."
                    hide ep1px0056
                    show ep1px0058
                    $ UnlockThat("ep1/ep1px0058")
                    off "[sf_name] turns around and gets in position for some reverse cowgirl action."
                    sis "Let me help."
                    off "[sis_name] softly spreads [sf_name]'s buttocks so that my cock can easily rub against her pussy."
                    sf "Please, give it to me. I can't wait anymore!"
                    off "I have not yet penetrated her and I already feel like being on the verge of ejaculation."
                    off "Shit, I'm about to come."
                    off "SHIT SHIT SHIT"
                "Then I'll do [sis_name] first...":
                    label ep1dreammenusis:
                    sis "I told you..."
                    sf "I am so jealous. Please save some energy for when my turn will come."
                    sis "I'm dripping wet. You'd better make me come or I'll make your life miserable."
                    hide ep1px0056
                    show ep1px0057
                    $ UnlockThat("ep1/ep1px0057")
                    off "[sis_name] turns around and gets in position for some reverse cowgirl action."
                    sf "Let me help."
                    off "[sf_name] softly spreads [sis_name]'s buttocks so that my cock can easily rub against her pussy."
                    sis "Please, give it to me. I can't wait anymore!"
                    off "I have not yet penetrated her and I already feel like being on the verge of ejaculation."
                    off "Shit, I'm about to come."
                    off "SHIT SHIT SHIT"

    $ renpy.end_replay()
    if ep1mcsofasleep == True:
        scene black with dissolve
        with Pause(2)
        show ep1px0060 with dissolve
    else:
        scene black with dissolve
        with Pause(2)
        show ep1px0059 with dissolve

    off "Shit... That dream..."
    off "What a shame."
    off "I couldn't go all the way."
    off "And I stained my underpants."
    off "Great way to start the day..."



    jump day2start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
