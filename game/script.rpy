
define k = Character("Keikumusume", color="#1adf0a")
define dk = Character("Detective Keikumusume", color="#1adf0a")
define p = Character("Policeman", color="#e60101")
define z = Character("Zan", color="#009702")
define sp= Character("PA speaker")
define h1 = Character("Miki", color="#6c00a2")
define who=Character("???")
define y=Character("Yui", color="#88b2e1")
define n = Character("Nana", color="#ecf300")
define h = Character("Hinata", color="#f50563")
define x = Character("Xenia", color="#05aef1")
define i = Character("Ichihime", color="#fc1b1b")
define everyone = Character("Everybody")
define m = Character("Sawako", color="#7400d5")
define b1 = Character("Igor Bogdanoff", color="#db1919")
define b2 = Character("Grichka Bogdanoff", color="#db1919")
define boss = Character("???", color="#db1919")
define w = Character("Akane", color="#f22199")

label start:

    scene bg parlor with fade
    play music "audio/detectivekeiku.mp3" fadeout 1.0 fadein 1.0
    show dhat
    dk "(Another case of mahjong cheating huh.)"
    dk "(These mahjongers, they’re just silver room rookies. I don’t know why the MCD even bothered to send me out here.)"
    dk "Officer. Tell me about the crime scene here."
    show dhat at left1
    show police at right1
    p "Yes, ma’am!"
    p "This group was playing a hanchan, and they found that there was an extra haku in their set."
    p "We’ve also found that the set is missing a two sou."
    dk "Have you checked to make sure that it’s a standard issue set for silver ranked games?"
    p "Yes of course."
    dk "Hmmmmm..."
    dk "Yeah these tiles are definitely from your standard silver set."
    dk "They’re made of the usual cheap wood, everything is painted on instead of engraved, and they’re all greasy as hell."
    dk "You’ve identified the set, right?"
    p "Yes. We’ve found that the extra haku has the same micro identification number on its back as the rest of the set."
    dk "So we can be sure that this haku is from the same set… yet there are five haku tiles."
    p "That is correct. But how can that be?"
    p "Is it possible that someone used their thumb to rub off the two souzu to turn it into a haku?"
    dk "I don’t think it’s possible for someone to do that with just their thumb. Not unless they were some sort of super human."
    dk "Show me the suspects."
    p "Yes ma’am!"
    scene bg jail  with fade
    show dhat at left1
    show police at right1
    dk "These are all four players from the hanchan, correct?"
    p "Yes, these are the four."
    hide dhat
    hide police
    show mai
    dk "(A holy girl, huh. Wouldn’t be the first time I caught a holy person committing mahjong crimes. She seems nervous. Something to hide perhaps?)"
    hide mai
    show bart
    dk "(This guy seems pretty plain. Not too many distinguishing features. But you know, criminals love to hide in plain sight.)"
    hide bart
    show zan
    dk "(This guy, he reeks. He’s got the stench of alcohol all over him.)"
    hide zan
    show osamu
    dk "(This guy has some nice clothes on him. What’s he doing playing with the poor silver players? Seems suspicious.)"
    hide osamu
    show dhat at left1
    show police at right1
    p "So who are you going to question first?"
    dk "Hmmmmmmm."
    dk "What’s the name of that guy with the sword?"
    p "Zan Tsukini."
    dk "It was him. He’s the one who did it."
    hide police
    show zan at right1
    z "Huh? You’re wrong! I’m just a simple travelling ronin. I don’t even care about my rank, I would never cheat."
    dk "No, it was definitely you."
    hide zan at right1
    show police at right1
    p "How did you work that out so fast?"
    dk "It’s simple. He has the stench of alcohol all over him."
    dk "Remember when I said that it would be impossible to rub off the sign for the two souzu with just a thumb?"
    dk "Well that’s true. But it definitely would have been possible if one were to do it with both their thumb and also some alcohol!"
    hide police at right1
    show zan at right1
    z "Eek!"
    dk "Officer, was there any alcohol found at the scene of the crime?"
    hide zan at right1
    show police at right1
    p "Ah, yes! There was an opened bottle of vodka that belonged to Zan here."
    dk "Well there you go, there’s the ‘weapon’ of this case."
    hide police at right1
    show zan at right1
    z "I admit it, I did it! I simply wanted to earn a little more money so that I could give the local children some candy, so I cheated."
    z "I’m not a pervert or anything like that, I simply wanted to see their smiling faces!"
    z "Please detective, don’t send me to the shadow realm!"
    dk "Hmmmmm."
    dk "Hmmmm."
    z "I beg of you!"
    hide zan at right1
    show police at right1
    p "Keikumusume, if this guy really has been cheating, he must be punished!"
    dk "(It’s just a game of mahjong, I don’t understand why everyone gets so invested in it.)"
    dk "Zan, uh, Zucchini? Was that the name?"
    dk "Whatever. Zan, I, mahjong detective Keikumusume, sentence you to, uhhh, twenty hours of community service."
    hide police at right1
    show zan at right1
    z "Thank you! Thank you! I owe you a life debt!"
    dk "(It’s just a gambling game, it’s not that big of a deal!)"
    dk "Well that wraps this case up."
    hide zan at right1
    show police at right1
    p "Excellent, I’ll send the paperwork around to you tomorrow."
    dk "(Aww, not the paperwork.)"
    dk "(I almost want to go back and shadowrealm that guy now, it always has way less paperwork.)"
    dk "(I have so much school work to do as well!)"
    p "Excellent work as always detective Keikumusume. Job well done!"
    dk "No need to thank me officer. Just doing my job."
    stop music
label op_credits:
    scene bg start  with fade
    ">The Winning Team presents…"
    "A >The Winning Team production."
label moping:
    scene bg keikunight  with fade
    play music "audio/doubt.mp3" fadeout 1.0 fadein 1.0
    show hat
    k "(Another pathetic case is over.)"
    k "(I’m glad that I’m not involved in any more petty murder cases and all, but damn, they sure are all so pointless.)"
    k "(Everyone praises me for solving them, but it seems like such a waste. What’s the good in being praised for work you don’t care about.)"
    k "(I would have been better off spending that time solving this pile of homework.)"
    k "(And besides, there’s only one crime I’m really interested in solving.)"
    k "(“Victim: Hercule Watson.”)"
    k "(“Cause of death: Unknown. Believed to be some form of flow manipulation.”)"
    k "(“A single piece of paper was left on Watson's body. It read ‘Stay away from the UGR, and the UGR will stay away from you.’”)"
    k "(“Final ruling from the Mahjong Crimes Division: Case unsolvable at present time.”)"
    k "(Is this crime really impossible to solve?)"
    k "(This case file, it really does seem to be useless.)"
    k "(An unsolvable mystery is just too cruel.)"
    k "(I'm sorry, uncle. I guess you were wrong about me, I really am a useless girl after all.) "
    k "(Even though my parents weren't here to take care of me, you were.) "
    k "(Even though you were so busy with detective work, you always spent time with me.)"
    k "(Even though I'm a girl with no talents, you still entrusted that case to me. That made me feel like I was the brightest person in the world.)"
    k "(Even when I didn't appreciate it, you always did your best for me when no one expected you to.)"
    k "(But even after you've done so much for me, I still can’t avenge you.)"
    k "(What happened on that day? What were you doing? Why can’t someone tell me?)"
    k "(I want to go to sleep. I have school tomorrow. But I can't stop thinking about this.)"
    k "(. . .)"
    k "(I remember you always tried to show me how to play mahjong.)"
    k "(Remember that joke you would always repeat?)"
    k "('Why Keikumusume, I do think that with our brains put together, we could clear out my boss's entire paycheck in just a hanchan or two!')"
    k "(I always found those jokes so corny. I'd laugh and tell you I was busy reading.) "
    k "(If I could wish for anything, right now, I'd just wish that we could play a game of mahjong together. Just one game like you wanted to.)"
label classroom:
    scene bg classroom with fade
    play music "audio/counselling.mp3" fadeout 1.0 fadein 1.0
    "*the next afternoon*"
    show hat
    k "(Another day at school is over, huh.)"
    play sound "audio/aba.mp3"
    k "(*abababa* *abababa*)"
    k "(Yet another call from the MCD. It’s probably another case request.)"
    k "(Muted.) "
    k "(Just because uncle left the title of mahjong detective to me, they think I'll take all these requests for them.)"
    k "(I just solved a case for them last night. Give me a break.)"
    k "(Although, it’s not like I have a particularly rosy high school life to enjoy.)"
    k "(The only thing I had to enjoy at school was the literature club, and that’s been disbanded since that guy transferred to a different school.)"
    k "(I guess that's what happens in a club with just two members.)"
    k "(Even then, it wasn't much of a club, looking back on it. I just read in silence while he used it as an excuse to play video games. I don't even remember his name.)"
    k "(Kyou... Kyouta... Kyaoutako Sugi? Was that it?)"
    sp "Keikumusume. You’re wanted in the counsellor’s office. Keikumusume, please come to the counsellor’s office before heading home."
    k "(Ugh, why do they have to announce it over the speaker system like that? It’s so embarrassing.)"
label counsellor:
    scene bg counsellor with fade
    show hag at lefthag
    h1 "Keikumusume, please take a seat."
    show hat at right1
    k "Sure."
    h1 "Me and some of the other staff members have been worried about you."
    h1 "We’ve noticed that your grades are slipping."
    h1 "Teachers have made comments to me that you seem moody or upset in class."
    h1 "Is everything alright?"
    k "(Of course things aren’t alright. But I’m not going to entrust my feelings to some counsellor hag that I don’t even know.)"
    k "Things are fine. I’m just tired is all. Nothing more to it than that."
    h1 "I see. Well, we’ve actually decided that it would be best for you to consider putting your work with the MCD on hold for a year."
    k "Eh?"
    h1 "We’re all worried about your mental health. Having a seventeen year old working in the Mahjong Crimes Division is, well, it’s legal but it’s also unprecedented."
    k ". . ."
    h1 "I understand that your work is important to you, but school is important too."
    h1 "You have the rest of your life to work, but you only have one year left in highschool."
    h1 "We’ve already made the arrangements with the higher-ups at the division for you to take a holiday."
    k "Sounds fine to me. It’ll give me more time to read."
    h1 "However, we’re also worried that you aren’t making any friends."
    h1 "It’s not good for your mental health to remain cooped up."
    k "(That’s none of your business, but okay.)"
    h1 "Furthermore, every student in school is mandated to join at least one club."
    h1 "We’ve given you a little bit of leeway since the literature club had to disband and you started your detective work, but that will have to stop now."
    h1 "Recently, the mahjong club has lost its fifth member. You should join them."
    k "Do I have to?"
    h1 "Pretty much. Is there any particular reason why you wouldn’t want to?"
    k "Well what if I said that I don’t know how to play mahjong?"
    h1 "Well I’d say that I don’t believe you. There’s no way a mahjong detective wouldn’t know how to play mahjong."
    h1 "Come on, tell me the truth. What you say here won’t leave this room."
    k "I don’t think I’m good at making friends, so I’d rather not."
    h1 "Really? You’re telling me that you can solve crimes but you can’t make any friends?"
    k "It’s true! Solving a crime is easy. You put on the badge and sunglasses and suddenly you’re a different person."
    k "But making friends is totally different."
    h1 "Well that’s a shame, but it’s already been decided. Just go in, be confident in yourself and you’ll be fine. I have the paperwork right here."
    h1 "In fact, I think they’re actually having a club meeting today, so you should go right now."
    k "Eh?! Right now?"
    h1 "Yes, right now. You can consider it an order from the principal if you like."
    h1 "Have fun."
    hide hag
    scene bg hallway with fade
    show hat
    stop music
    k "(Ahhhhhhhh! That dumb hag!)"
    k "(I guess I have no choice. It’s decided that I’m going to be joining the mahjong club.)"
    k "(I gotta do it so I’ll just do it. Just walk in and hand in that form.)"
    k "(Easy peasey.)"
    k "(Just walk in, hand in the form. Say you want to join.)"
    k "(Aaaaa, why's this so hard!)"
    k "(What if they get mad at me because I haven't memorised all of the scoring rules? I don't even know how to count fu. Aw gosh this could be so embarrassing.)"
    k "(But there’s no use thinking about that. If I can solve a murder case then I can join a mahjong club. I just need to take these first steps inside.)"
label mahjongclub:
    scene bg clubroom with fade
    play music "audio/sliceoflife.mp3" fadeout 1.0 fadein 1.0
    show hat at left1
    k "H-hello…"
    k "HELLO! I, WOULD LIKE TO JOIN THE MAHJONG CLUB. PLEASE. THANK YOU."
    k "(Aaaaa! I overcompensated! I should just go home and never come back!)"
    show yui at right1
    y ". . ."
    k "(Oh gosh she's staring at me. I've made such a scene.)"
    y "Sure, you can join. Do you have the form?"
    k "Aa--aaa yes! I do! The form, I have it right here."
    y " . . . Okay. Sit down, we're about to play a hanchan."
    hide yui
    show nana at right1
    n "Hehe, that's a big entrance you've made there."
    k "(Aaaaaa, she totally noticed it. She's definitely laughing at me!)"
    n "I'm Nana, but everyone else calls me... banana! Nice to meetcha."
    hide hat
    show yui at left1
    y "None of us call her banana."
    hide nana
    show hinata at righthinata
    h "Hello, my name’s Hinata. Welcome to the club."
    y "My name's Yui."
    hide yui
    show hat at left1
    k "Ah, I'm Keiku. Keikumusume! I'm very new to mahjong but I'd really like to play with you guys."
    h "That’s no problem. We all had to start somewhere."
    hide hinata
    show nana at right1
    n "Yep. Just take a seat and do your best."
    k "(I guess it’s fine then? There’s nothing to be worried about?)"
    hide nana
    show yui at right1
    y "I'm glad you came today."
    k "Eh? Really?"
    y "Yep. I don't like playing sanma at all."
    k "(Okay. This is just like the online games of mahjong I've played. There's no need to be nervous!)"
label game:
    scene bg double with fade
    play music "audio/fencingwithnana.mp3" fadeout 1.0 fadein 1.0
    k "What to do....."
    menu:
        "Riichi":
            k "D-daburi riichi!"
        "Riichi":
            k "D-daburi riichi!"
        "Riichi":
            k "D-daburi riichi!"
    scene bg clubroom with fade
    show nana at right1
    show yui at left1
    n "A double riichi on your very first turn? Looks like we have a prodigy in our club."
    y "Eurgh."
    hide nana
    show hat at right1
    k "(Hmmm, I think everyone's trying to fold?)"
    k "Ah, ron! Double riichi! Pinfu! That's ummm, 3900 points!"
    hide yui
    show hinata at lefthinata
    h "So be it then."
    hide hat
    show nana at right1
    n "Wait.. that's furiten!"
    h "Oh you’re right, that is furiten."
    hide nana
    show hat at right1
    k "Wait, if my double riichi was furiten, that means…"
    hide hinata
    show yui at left1
    y "Tenhou…"
    k "(Owwwwww. Like tiles down the drain.)"
    hide yui
    show nana at left1
    n "Wow. Yikes!"
    k "Ehehe, next hand."
#    {play tile shuffling sounds}
    k "(Hmmmm... I can riichi here for a tanki. But which wait should I pick?)"
#    {present the following options: south wind, north wind. If North is picked, play the following dialogue.}
    menu:
        "North":
            k "(I'll go with the tanki on the north wind!)"
            k "(...)"
            k "(...)"
            k "(Come on, come on...)"
            k "(Ah, I just drew the south wind!)"
            k "(Geez come on!)"
        "South":
            k "(I'll go with the tanki on the south wind!)"
            k "(...)"
            k "(...)"
            k "(Come on, come on...)"
            k "(Ah! I just drew the north wind!)"
            k "(Geez come on!)"

    n "Ron! That's mangan, 12000 points!"
#    {Cut music, play https://www.youtube.com/watch?v=szDKbPLq-to}
    play music "audio/sliceoflife.mp3" fadeout 1.0 fadein 1.0
    k "(Even though I came fourth, and even though I seriously embarrassed myself, that was pretty fun.)"
    hide nana
    show xenia at left1
    x "Oh? Who's this new girl?"
    n "Oh Xenia, you're back! Are you going to be able to make it to the tournament this weekend?"
    hide hat
    show nana at right1
    x "I just barely managed to convince my parents to let me go. So long as I'm back home by 7 it'll be fine."
    n "Great! Now this here is Keikumusume, she'll be our fifth player in the tournament."
    hide xenia
    show hat at left1
    k "Wait, I'm your what now?"
    n "Our fifth player. We're really lucky that you showed up when you did. This local tournament needs five people per team and we were one short until you came along."
    n "We actually had a club member leave quite recently."
    k "Well, I guess I could do it. Just don't expect too much from me."
    hide nana
    show yui at right1
    y "Yep. I don't expect too much from you."
    k "(Oof. Even though she's just repeating what I just said, that stings a little.)"
    y "..."
    hide hat
    show hinata at lefthinata
    h "Yui, that's a little..."
    hide hinata
    show xenia at left1
    x "Anyway, tell us about yourself, Keiku. Oh, can I call you that? Saying ‘Keikumusume’ every time is just a little long is all."
    hide yui
    show hat at right1
    k "Oh yeah, that's fine."
    k "Well, my hobbies include reading, writing, and I'm also technically a mahjong detective."
    hide xenia
    show hinata at lefthinata
    h "You work for the MCD? While in high school? That’s amazing."
    k "Thanks. I've only actually solved one case though."
    hide hinata
    show nana at left1
    n "Tell us about it! Is it really like how it is in all those television dramas about MCD officers? Do you have a catchphrase you shout when you send someone to the shadowrealm?"
    k "Honestly it was pretty similar to what you'd see in a detective manga, or even a video game. As for the catchphrase, I guess it was something like..."
#    {Play KAAAAN.wav}
    play sound "audio/kan.mp3"
    k "KAAAAAAAAN!"
#    {Play SORERONDE.wav}
    play sound "audio/ron.mp3"
    k "SORE RON DE!"
#    {Play YAKUMAN.wav}
    play sound "audio/yaku.mp3"
    k "YAKUMAN!"
    k "Aaaah, honestly I actually feel sort of embarrassed shouting that out loud."
    hide hat
    show yui at right1
    y "That sounded cool."
    n "Yeah that was super cool!"
    hide nana
    show xenia at left1
    x "Being a mahjong detective is a noble cause. There's nothing to be embarrassed about."
    hide yui
    show hat at right1
    k "Ehehehe."
    hide xenia
    k "(I think I should ask them about themselves too. If I want to join this club, I should get to know them a little better.)"
$ q1=False
$ q2=False
$ q3=False
$ q4=False
label first_choice:
    scene bg clubroom with fade
    menu:
        "Who should I talk to?"

        "Hinata":
            show hinata at lefthinata
            show hat at right1
            k "What about you, Hinata, do you have any hobbies?"
            h "Well, when I'm not playing mahjong, I enjoy gardening a lot."
            h "I have a big garden at home. The plants are like my babies."
            h "It's really satisfying watching them grow. It saves me a lot of money being able to use my own vegetables for cooking."
            h "My favourite plants to grow are different varieties of berries. They’re somewhat delicate and they’re a lot of hard work, but the payoff is wonderful."
            h "Right now I’m trying to grow some strawberries in the school’s garden."
            h "You really do need to be careful around berries though. Often people eat them before they’re ripe and get sick."
            h "A lot of people get sick foraging for wild berries and mushrooms."
            h "Every year people die after misidentifying wild berries and mushrooms."
            k "Um, I'll keep that in mind."
            h "You should come around to my garden sometime. I'll let you borrow some of my herbs."
            $ q1=True
            jump first_choice

        "Yui":
            show yui at left1
            show hat at right1
            k "So Yui, do you have any sort of hobbies?"
            y "Yes. I really like anime."
            k "Ah well, I'm a big light novel fan, and a lot of anime adapt those, so I guess that sort of makes me an anime fan too. What sort of anime do you like?"
            y "{size=-10}...Gundam{/size}"
            k "Huh? I couldn't hear you."
            y "I really like Gundam."
            k "Sorry, I still didn't quite catch that."
            y "Don't worry about it. It's nothing. I just like anime in general."
            k "(Hmmmm. I think she's hiding something. But I don't think she means anything bad by it.)"
            y "Well if you ever want to watch anime together I wouldn't mind."
            $ q2=True
            jump first_choice

        "Nana":
            show nana at left1
            show hat at right1
            k "So what are you into, Nana?"
            n "Oh, I'm into sports."
            k "Really? What kind of sports?"
            n "Oh, you know. This and that. Rugby, wrestling, football, the American kind of football, tennis, golf, curling, birdman rallying, etc."
            n "I think my favourite kind is skateboarding though."
            n "I get a lot of offers to join sports clubs but it'd be a conflict of interest with my student council duties. I'd feel like I'd have to allocate more budget to whichever club I'm in."
            n "That's actually why I joined the mahjong club. All you need is a mahjong set and a table and you're good to go."
            k "Wow, that's a lot of different sports."
            n "Right? But I think it's important to stay fit. You only get one body, so you need to take care of it."
            n "Let me know if you ever want to do some sports with me, kay?"
            $ q3=True
            jump first_choice

        "Xenia":
            show xenia at left1
            show hat at right1
            k "Do you have any hobbies, Xenia?"
            x "Not really. I don't actually have a lot of free time."
            k "Really? Why?"
            x "It's my family. They're ridiculously strict."
            x "For example, when I get home tonight I must study until 7, have a piano lesson at 8, practice latin until 9, and then I have to be asleep by 9:30."
            x "This club time is the only time I'm allowed to truly relax."
            k "That sounds really tough."
            x "Indeed. I suppose that's the drawback of living with parents that are as rich as mine."
            k "They’re rich?"
            x "Quite so. My father's expectations for me are simply too high. He's always like 'when I was your age, I was already pulling myself up by my bootstraps and blah blah blah.'"
            x "Actually, you should come over sometime. He loves flaunting his wealth, so he's always very hospitable to guests."
            x "It's also an easy way for me to escape all these annoying extracurricular lessons."
            k "Hmmm, I'll definitely consider it."
            k "(I am kind of curious what sort of rich people house she lives in.)"
            $ q4=True
            jump first_choice


        "That's all, I guess" if (q1&q2&q3&q4) == True :
            jump next

label next:
    scene bg clubroom with fade
    play sound "audio/bell.mp3"
    "*ding dong* *ding dong*"
    show hat at left1
    k "Ah, the bell's ringing."
    show nana at right1
    n "Time to go then."
    stop sound
    hide hat
    show hinata at lefthinata
    h "Yep, I'll see you all next meeting."
    hide nana
    show yui at right1
    y "Mhm."
    hide hinata
    show xenia at left1
    x "Ah, is it really that time already?"
    hide xenia
    show nana at left1
    n "Anyway, I look forward to seeing you at the next club meeting, Keiku."
    n "We really were in a jam before you suddenly showed up."
    n "I had no idea what to do about this weekend tournament, but then you just rushed in."
    y "You were quite the deus ex machina."
    hide nana
    show hat at left1
    k "Well, I'm glad to hear that, but my mahjong definitely isn't up to tournament level yet."
    hide yui
    show xenia at right1
    x "Oh don't worry dear, we'll whip you into shape in no time..."
    hide xenia
    show hinata at righthinata
    h "Oh, we should probably give Keiku our numbers, right?"
    h "That way we can keep her in the loop."
    k "O-oh, thank you!"
    k "(The phone numbers of four girls in one day...)"
    k "(If I was a guy I'd be over the moon right now.)"
    #{Change bg scene, Keikus room at night. Stop music, play cricket sounds https://www.youtube.com/watch?v=Olfg9KK_bmE}
    #    {add music here: some ambivalent contemplation music, like https://www.youtube.com/watch?v=-l1W6g7UYtY}
    scene bg keikunight with fade
    play music "audio/contemplation.mp3" fadeout 1.0 fadein 1.0
    show hat
    k "(They seemed like a strange bunch.)"
    k "(But I'm really happy that they accepted me so easily.)"
    k "(I wish I knew earlier that making friends would have been as easy as just walking into a club room.)"
    k "(I still feel sorta lonely. I still really miss Watson.)"
    k "(But maybe with these people, things won't be so bad.)"
    k "(. . .)"
    k "( z z z )"
    scene bg schoolfront with fade
    show hat
    play music "audio/counselling.mp3" fadeout 1.0 fadein 1.0
    k "(Another boring day at school has gone by.)"
    k "(I don't have any exams coming up.)"
    k "(I don't feel like actually doing any of this homework either.)"
    k "(. . .)"
    k "(Maybe what that counsellor hag said was right. Maybe I really should try making some friends.)"
    k "(I could try calling someone from the club and asking them to hang out.)"
    k "(But what if that's too imposing? I only just met them yesterday. I don't want to just barge in on them.)"
    k "(But then again, you don't make friends by not talking to anyone.)"
    k "(They all made offers too. So it should be fine, right?)"
    k "(Which one should I text though.)"
    k "(Somehow this feels like a big decision. It really shouldn't be. I'm just asking someone to hang out.)"
    k "(But for some reason it feels like this is going to be some sort of major turning point for me.)"
    menu:
        "Who should I ask?"

        "Yui":
            $ girl="Yui"
            jump yui_date1

        "Nana":
            $ girl="Nana"
            jump nana_date1

        "Xenia":
            $ girl="Xenia"
            jump xenia_date1

        "Hinata":
            $ girl="Hinata"
            jump hinata_date1

label post_date1:
    scene bg keiku with fade
    play sound "audio/kiki.mp3"
    "*Kikikanri!* *Kikikanri!*"
    show hat
    k "Ugh, be quiet you useless alarm..."
    k "*Yawwwwwn*"
    k "(It’s that time already huh?)"
    scene bg schoolfront with fade
    "...."
    scene bg classroom with fade
    play music "audio/clock.mp3" fadeout 1.0 fadein 1.0
#    {play clock ticking noise https://www.youtube.com/watch?v=8VUgLhAvN0U}
    k "(Class is going so slowly today. I want it to end already.)"
    k "(I feel something tingling in my stomach. It’s like there’s a ping-pong ball bouncing around my head.)"
    k "(Is this what it feels like to actually have something to be excited about?)"
    k "(I can’t believe I’m actually looking forward to the club meeting so much.)"
    k "(That counsellor was right. I’m going to have to eat my hat.)"
    k "(. . .)"
    k "(Come on you dumb clock, move faster!)"
    stop music
    "(Time passes)"
    play sound "audio/bell.mp3"
    "*Bing bong* *Bing bong*"
    k "(About time!)"
    stop sound
    scene bg clubroom with fade
    play music "audio/sliceoflife.mp3" fadeout 1.0 fadein 1.0
#    {Play https://www.youtube.com/watch?v=szDKbPLq-to}
    hide hat
    show nana at right1
    show hat at left1
    n "Ah, Keiku, you’re here."
    k "Hi, Nana. Where is everyone?"
    n "Ah, they’re running a little late. So right now it’s just me and Yui here."
    n "Actually, we were wondering if you could settle a debate for us."
    n "Which do you think is cooler. Shounen anime or mecha anime?"
    hide hat
    show yui at left1
    y "Mecha anime is definitely cooler."
    n "Nuh-uh, no way. That’s for nerds."
    menu:
        "Mecha":
            y "That’s right, mecha is definitely the best."
            n "What? No way."

        "Shounen":
            n "That’s right! Shounen is definitely the best genre."
            y "I disagree. Mecha is better, and I can objectively prove it."
            if girl=="Yui":
                y "Keikumusume, I thought you would understand at least."

    n "Shounen anime is all about self-improvement and making yourself stronger."
    n "In a mecha anime, only the robots can get stronger instead of your own body."
    n "So obviously the shounen anime will be more interesting."
    y "Ah, but you can get better at piloting though."
    y "You see, the original Mobile Suit Gundam is a perfect example of this, as shown by the growth of the protagonist Amuro Ray."
    y "At the start of the anime he’s really not very good at piloting the gundam. He’s carried solely by how strong the Gundam is, relative to Zeon mobile suits."
    y "However, as the series goes on, the mobile suits from Zeon get stronger and stronger, and Amuro has to get better as a pilot in order to keep up."
    y "By the end of the series Amuro’s position has reversed, and he is now piloting an inferior machine and only survives due to his improved piloting skills."
    y "I think the scene with Ramba Ral is a really good example of…"
    n "So, Keiku! What sort of anime do you like best?"
    y "Ah, I wasn’t finished talking…"
    hide yui
    show hat at left1
    k "I personally like detective anime the best."
    k "Although honestly I read a lot more light novels than I watch anime."
    n "Ah, personally I could never get into reading. Having something visual just feels a bit more, tactile, y’know?"
    hide nana
    show hinata at righthinata
    h "Hello everyone."
    hide hat
    show xenia at left1
    x "Good afternoon."
    hide hinata
    show nana at right1
    n "Ah, Hinata, Xenia. We need you to help us settle something. Which anime genre is best?"
    hide nana
    show hinata at righthinata
    h "I like shoujo and magical girl anime the best actually. Stuff like K-on is nice too."
    x "Yep, that does seem like the sort of anime Hinata would like. Probably a little too girlish for your tastes, Nana."
    hide hinata
    show nana at right1
    n "Yeah. Shoujo anime is a little too mushy for me. I have no interest in it."
    x "I don’t actually watch much anime. But for me, it’s gambling anime."
    x "In any case, let’s get down to business."
    n "Right. If we want to have a shot at this weekend's tournament, we’re going to need to train Keiku up."
    hide xenia
    show hat at left1
    k "Training? Like mahjong training?"
    k "Also, when and where is this tournament supposed to happen? Is there a prize?"
    n "Nope, no prize. It’s just for fun."
    n "Unless you can classify ‘reputation’ as a prize."
    n "I’ll text you the details later. Now onto training."
    hide nana
    show hinata at righthinata
    h "We’re just going to look at a series of mahjong problems to solve."

    #{change bgm to  https://www.youtube.com/watch?v=szDKbPLq-to}
    play music "audio/wwyd.mp3" fadeout 1.0 fadein 1.0
    h "Let’s start off with something simple. What would you discard in this situation?"
    hide hinata
    hide hat
    scene bg wwyd1 with fade
    $ renpy.pause (10.0)
    $ s1=False
    $ s2=False
    menu:
        "Red 5m":
            show nana at right1
            n "Keiku, are you nuts?"
            show yui at left1
            y "That’s a very unsafe discard."
            hide nana
            show hinata at righthinata
            h "Hey, she’s new, lay off a little."
            h "Although yes, that’s not what I would have chosen."

        "9s":
            show xenia at right1
            x "Yep, the nine souzu is what I would have picked too."
            show hinata at lefthinata
            h "Really? Why the nine souzu?"
            hide hinata
            show hat at left1
            k "There’s two of them. If you discard one of them and it passes, then that’s a free safe tile for the next turn."
            x "Precisely. It’s also a terminal tile, so it’s quite safe to begin with."
            hide hat
            show yui at left1
            y "While it is true that one passing would give a free safe tile, I think it’s more important to try avoiding the ippatsu."
            y "The fact of the matter is that there’s more potential patterns that involve waiting on the nine sou than the honour tile."
            x "Well, I suppose this is one of those things we’ll just have to agree to disagree on."
            y "Indeed. While I’d prefer to have an objective answer, that’s very difficult to find in mahjong."

        "Chun":
            show yui at left1
            y "I agree. The red dragon is definitely the safest discard."
            show xenia at right1
            x "Huh. I had a different answer."
            x "I would have actually discarded the nine souzu myself."
            x "If you discard one and it passes, then you get two free safe tiles."
            y "That’s true. However, I don’t think that outweighs the safety of the red dragon."
            y "The fact of the matter is that there are a lot less combinations of tiles that create tenpais waiting on honour tiles."
            hide xenia
            show nana at right1
            n "I think this is one of those cases where there isn’t exactly an objectively right answer."
            $ s1=True
    hide yui
    hide hinata
    hide hat
    hide nana
    hide xenia
    scene bg clubroom with fade
    show nana at right1
    n "Alright, next question, here we go."
    scene bg wwyd2 with fade
    hide nana
    $ renpy.pause (10.0)
    menu:
        "1p":
            show yui at right1
            y "Why did you pick that discard?"
            show hat at left1
            k "Well, just because it gives you the possibility of getting pinfu, and to avoid the one pin - two pin edge wait on the three pin."
            y "Hmmmmmm."
            y "I understand your reasoning, but I don’t think it’s optimal."
            y "Your chance of getting a non furiten tenpai for pinfu is pretty low here. You’d have to draw the six souzu."
            y "Furthermore, given that your opponent has called on triplets of the one souzu and the one manzu, there’s a high chance that they’re waiting on the one pin for chanta, junchan, sanshoku doukou or even something even scarier like chinroutou."
            k "Hmmmm. I guess you’re right then."
            y "It’s not like your answer didn’t have any merit behind it at all though."
            y "Getting a tenpai with two dora, riichi, and pinfu, could bring you very close to first place."
            y "With ura dora it could even reach haneman."
            hide hat
            show hinata at lefthinata
            h "Yes. Even though I agree with Yui’s answer, it’s not completely cut and dry."
            hide hinata
            hide yui

        "2p":
            show yui at right1
            y "I agree with your answer, Keikumusume. But why did you pick that answer?"
            y "Having the right answer is great, but your reasoning for it is important too."
            show hat at left1
            k "Well, it’s simple. I already have tenpai if I discard the two pin, and I have a safe tile too."
            k "Discarding the one pin wouldn’t give me a greater number of tiles to wait on."
            k "It’d also be slightly more dangerous, since the shimocha’s calls indicate a high probability of chanta, junchan, sanshoku doukou or even something even scarier like chinroutou."
            y "Yep. That’s the same reasoning I had."
            y "Some people might try to argue that you should discard the one pin since it can upgrade the hand with pinfu if you draw a six souzu."
            y "But I don’t think it’s worth the risk."
            $ s2=True
            hide hat
            hide yui

    scene bg clubroom with fade
    show nana
    n "Alright, let’s do one more and then play a game."
    hide nana
    scene bg wwyd3 with fade
    $ renpy.pause (10.0)
    show hat at left1
    k "Some information is missing. When did the player call this chi?"
    show xenia at right1
    x "I was just about to mention that, but I like your attention to details. As expected from a true mahjong detective. Chi was called shortly before the first riichi."
    hide hat
    hide xenia

    menu:
        "2s":
            show xenia at right1
            x "I see, so you’d discard the two souzu. Why is that?"
            show hat at left1
            k "Well, the way I see it, the two souzu is safe against the shimocha’s riichi, since the toimen was able to safely discard it."
            k "I guess technically the two souzu is pretty dangerous since the kamicha could still be waiting on it, but at least it guarantees I won’t get double ronned."
            x "Heh, that’s a valid reasoning. But this is actually something like a trick question."
            k "Huh? What do you mean?"
            x "This problem is from an actual tournament. The player discarded the two souzu and dealt into last place’s mangan."
            k "Ah, so was the correct answer to discard the red dragon instead then?"
            x "Nope. If they discarded the red dragon, they would have been ronned by second place’s mangan instead."
            k "So it’s basically a no win scenario? What good is a problem like this then?"
            hide xenia
            show hinata at righthinata
            h "Well, I think what’s important is that your answer has reasoning and justification behind it."
            h "Perhaps the two souzu would have passed nine times out of ten, and in this case it just didn’t."
            h "That’s just mahjong though. It’s kind of like life. You make the best decision you can and if it doesn’t work out, then that just can’t be helped."
            hide hinata
            hide hat
        "Chun":
            show hat at right1
            k "I think I’d discard the red dragon."
            show xenia at left1
            x "I see. Why is that?"
            k "Well, honour tiles are usually safe tiles, right?"
            k "The only way anyone could be waiting on them is with a pair or for a triplet, which is pretty unlikely."
            x "Heh. That is true, but this is actually a trick question."
            x "You see, this problem is actually taken directly from a famous tournament match."
            x "In that match, the red dragon would have actually dealt into second place’s mangan hand."
            k "Huh? So does that mean the correct answer was two souzu then? That seems like the most reasonable second option. It’s safe against second place since the toimen dropped it after they declared riichi."
            x "That’s true, but the two souzu isn’t a safe choice either. That would have dealt into fourth place’s mangan hand."
            k "So both reasonable options are wrong then? What’s the point of this problem?"
            hide xenia
            show hinata at lefthinata
            h "Well, I think what’s important is that your answer has reasoning and justification behind it."
            h "Perhaps the red dragon would have passed nine times out of ten, and in this case it just didn’t."
            h "That’s just mahjong though. It’s kind of like life. You make the best decision you can and if it doesn’t work out, then that just can’t be helped."
            hide hinata
            hide hat
    scene bg clubroom with fade
    show hinata
    h "Well, that’s that. Shall we play a few games now?"
    hide hinata
    scene bg black with fade
#    {Fade to black, play mahjong tiles sfx in the background}
    "....."
#    {bg change, school at sunset}
    scene bg schoolfront with fade
    show hat at left1
    k "(Aaah, those games were really fun.)"
    k "(Even though I didn’t win a single one of them.)"
    k "See you all on the weekend!"
    show nana at right1
    n "Yep. See you all then."
    hide hat
    show yui at left1
    y "Bye bye."
    hide nana
    show xenia at right1
    x "Have a good night, everybody."
    hide yui
    show hinata at lefthinata
    h "Best of luck, everyone."
    hide hinata
    #{Fade to black, bg change to Keikus room at night}
    scene bg keikunight with fade
    play music "audio/crickets.mp3" fadeout 1.0 fadein 1.0
    show hat
    k "(Club was a lot of fun today.)"
    k "(Even if half of it was just goofing off.)"
    k "(I’m sort of nervous about this tournament though. I really don’t want to embarrass myself.)"
    k "(Guess I’ll just have to do my best, and let the heavens take care of the rest.)"
    k "(. . .)"
    k "( z z z )"
    stop music
    if s1&s2:
        jump secret
    scene bg keiku with fade
    play sound "audio/kiki.mp3"
    "*kikikanri!* *kikikanri!*"
label pre_date2:
    show hat
    play music "audio/sliceoflife.mp3" fadeout 1.0 fadein 1.0
    k "Yawwwwwwn."
    k "Time for another school day."
    scene bg schoolfront with fade
    show hat
    k "Thank god it’s friday."
    scene bg classroom with fade
    show hat
    k "(Ahhhhhh, history class is so dull. I want the weekend to hurry up already.)"
    k "(Why do we have to learn about Australian history in a Japanese school?)"
    k "(Nothing happened there, it’s so boring and irrelevant.)"
    k "(I wonder what [girl] is doing this afternoon. Maybe they’d like to hang out.)"
    k "(I’ll send her a text.)"
    k "(. . .)"
    "*bzzt*"
    if girl=="Yui":
        jump yui_date2
    if girl=="Nana":
        jump nana_date2
    if girl=="Xenia":
        jump xenia_date2
    if girl=="Hinata":
        jump hinata_date2

label post_date2:
    scene bg keiku with fade
    stop music
    play sound "audio/kiki.mp3"
    "*Kiki kanri!* *Kiki kanri!*"
    "*yawwwwwwn*"
    #{Play https://www.youtube.com/watch?v=yN77vYbXLB4 }
    show hat
    play music "audio/meetupatthetournament.mp3" fadeout 1.0 fadein 1.0
    k "(Ah, that tournament is happening today.)"
    k "(Oh look, Nana texted me the time and place.)"
    k "(Better get going then. I don’t want to keep them all waiting.)"
    #{Fade to black, play train noises, bg change to front of some sort of rec center.}
    scene bg rec with fade
    show hat
    k "(This place isn’t particularly big. I guess they did just say this was a local tournament though.)"
    hide hat
    show nana at right1
    n "Yo, Keiku!"
    show xenia at left1
    x "Yoohoo."
    hide nana
    show yui at right1
    y "Hello."
    hide xenia
    show hat at left1
    k "(Ah, they’re all here already.)"
    k "Hey guys. Where are we meant to go?"
    hide yui
    show hinata at righthinata
    h "Just follow us."
    scene bg tourney with fade
    show hat at left1
    k "So how does this team format work anyway?"
    show hinata at righthinata
    h "Have you ever read that manga, Saki?"
    h "It’s like that. Each team starts out with 100,000 points and plays five hanchans with the players swapping out."
    k "Woah, will we be going to the nationals or something if we win this?"
    h "Nope. It’s purely for fun."
    hide hat
    show nana at left1
    n "Also for reputation. Can’t forget the reputation."
    hide hinata
    show yui at right1
    y "We already have a reputation."
    y "A reputation for losing."
    hide nana
    show xenia at left1
    x "It’s unfortunate, but true. Our team is cursed with terrible luck."
    hide yui
    show hat at right1
    k "Cursed? What do you mean?"
    x "We’ve played in four of these sorts of tournaments before and every time one of us dealt into a yakuman."
    x "In fact, our previous fifth club member actually left precisely because she was worried this tournament would be her turn."
    hide hat
    show yui at right1
    y "I keep telling you, we’re not cursed. It was unlikely for us to have dealt into a yakuman four tournaments in a row, but it’s not as if it’s impossible."
    y "It’s all just superstition in the end."
    hide xenia
    show nana at left1
    n "No way. You can’t go four tournaments in a row dealing into yakuman hands without some sort of supernatural involvement."
    y "In your case we don’t need to involve the supernatural to explain it. You dealt the chun after someone already ponned the haku and the hatsu."
    n "But I had such a nice iishanten! What were the odds, Yui? What were the odds!?"
    hide yui
    show hinata at righthinata
    h "Anyway, that’s how that is. I don’t believe in curses or anything like that, Keiku, but you might want to be a bit careful around potential yakuman hands."
    hide nana
    show hat at left1
    k "Right. I’m going to break that curse. There’s no way I’d deal into a yakuman!"
    k "Also, what order are we playing in?"
    hide hinata
    show yui at right1
    y "Would you mind playing last?"
    y "Please don’t take any offense to this, but you’re our newest member."
    y "So I think the best strategy would be for us to build you a big points lead, and then let you turtle and pass the last hanchan with quick and safe hands."
    k "No offense taken. I can definitely do that."
    hide yui
    show nana at right1
    n "Great. I’ll go first then. Xenia, you go second, Hinata, you go third, Yui, you go fourth."
    k "Also, does our team have a name?"
    hide hat
    show yui at left1
    y "Yep. We called ourselves ‘The Winning Team’."
    n "I came up with that one. I thought it would be funny if we actually won, and I thought it’d also be funny if we lost."
    hide nana
    show xenia at right1
    x "I think that name is what cursed us, to be honest."
    y "Even I can believe in a curse like that."
    hide yui
    show hinata at lefthinata
    h "God truly does have a sense of irony."
    hide xenia
    show nana at right1
    n "W-well, don’t blame me. You all agreed to the name!"
    n "Anyway, it’s going to be starting soon. Good luck, guys!"
    hide hinata
    show hat at left1
    k "Good luck, Nana."
    n "Ehe, just leave it to me."
    scene bg seats with fade
    play music "audio/tournament.mp3" fadeout 1.0 fadein 1.0
    #{Play https://files.catbox.moe/i91fhx.ogg }
    show hat
    k "(Oh wow, it’s starting, this is so exciting.)"
    k "(Even though there’s no incentive or prize, I really want us to win this!)"
    k "(Truly, we can become ‘The Winning Team’.)"
    hide hat
    show hat at left1
    show yui at right1
    y "Nana’s playing really riskily again."
    hide yui
    show xenia at right1
    x "Indeed. She loses big, but she also wins big."
    if girl=="Nana":
        k "(The way Nana plays is so bold. It’s really impressive. It’s like she doesn’t even care if someone else riichis, she just charges ahead with no fear.)"
        k "(Even the way she announces her tsumos and rons is cool. It’s as if looking stylish is part of her strategy.)"
    hide xenia
    show hinata at righthinata
    h "Wow, she’s getting us quite a lead. We might actually be able to make it this time."
    hide hat
    show yui at left1
    y "I wouldn’t have discarded that dora there."
    y "But risky plays of that sort is why Nana is fun to watch."
    hide hinata
    show xenia at right1
    x "Wouldn’t have her play any other way."
    hide xenia
    hide yui
    "(Time passes.)"
    n "Ron! That’s game. GG!"
    show nana at right1
    n "Well guys, how’d you like that?"
    show xenia at left1
    x "Splendid and bold play, like usual."
    hide xenia
    show hinata at lefthinata
    h "I felt like I was going to faint at some of those dora discards."
    n "Hehe, I was really worried about a few of my oikake riichis."
    n "I didn’t want to get scolded by anyone for taking useless risks again. But they mostly paid off."
    n "You’re up now, Xenia, good luck."
    hide nana
    show xenia at right1
    x "Thanks. I’ll be back with some extra points."
    h "I’m really looking forward to seeing what sort of monster dora hand Xenia is able to unleash here."
    hide xenia
    show yui at right1
    y "That’s just another superstition. There’s no reason to believe Xenia is anymore likely to draw doras than the rest of us."
    h "Come on, Yui. We all know she’s more likely to draw doras than the rest of us. Her hands are rich in doras."
    y "I won’t believe it until I see the stats."
    y "Although I will admit, this starting hand does have a lot of doras."
    hide hinata
    show nana at left1
    n "Yep. It’s like the gods just hand her doras just because they feel like it."
    hide yui
    if girl=="Xenia":
        show hat at right1
        k "(Wow, that really is a lot of doras. She just keeps drawing them one after another. Her hand is so rich in doras.)"
        k "(The way she carries herself while playing is kind of charming too. It’s like she’s showing off.)"
        k "(But showing off in a subtle way. The way she smiles when she declares her wins, it’s like she’s bragging to her opponents while also being polite at the same time. It’s very classy.)"
        hide hat
    n "Wow, look who gets another yakuhai dora call."
    show hinata at righthinata
    h "That’s Xenia for you."
    hide hinata
    hide nana
    "(Time passes.)"
    show yui at left1
    y "Excellent work, Xenia."
    show xenia at right1
    x "Naturally. I hope you all appreciated the uradora bomb in south 3."
    x "Good luck, Hinata."
    hide xenia
    show hinata at righthinata
    h "Thank you. I won’t waste this lead you’ve gotten us."
    y "Hinata's style of play is always really interesting to watch."
    hide yui
    show xenia at left1
    x "Indeed. I would always just call riichi as soon as possible, but she usually refrains until she’s upgraded her hand with extra yaku or dora."
    hide hinata
    if girl=="Hinata":
        show hat at right1
        k "(They’re right. The way Hinata plays is incredible.)"
        k "(If she can upgrade her hand, she’ll wait until it happens, before declaring riichi. That level of restraint is admirable.)"
        k "(It’s kind of like the way she gardens. It’s like she nurtures her hand to grow it into the strongest it can be, before declaring riichi and harvesting it.)"
        hide hat
    show nana at right1
    n "Woah. Did she seriously just pass on a ron?"
    x "Well, if she draws the 4pin here, she can discard the 1pin to upgrade her pinfu hand with tanyao and iipeikou."
    hide nana
    show yui at right1
    y "Wow, she managed to draw it. Is she going to riichi it?"
    x "Nope. I think she’s still looking to draw in the 2man too, so that she can add sanshoku doujun to her iipeikou."
    hide xenia
    show nana at left1
    n "Wow, she actually managed to draw the 2man as well."
    y "And there’s the riichi."
    hide yui
    show xenia at right1
    x "The way she plays is truly fascinating. She managed to take a measly riichi pinfu hand and turned it into riichi, pinfu, tanyao, iipeikou, and sanshoku for haneman."
    n "That’s our Hinata."
    hide nana
    hide xenia
    "(Time passes.) "
    show nana at left1
    n "Great work, Hinata. There were a lot of hands where I would have just instantly called riichi, but it looks like your delays paid off."
    show hinata at righthinata
    h "Thanks. I was a little worried about a few hands, but they all grew to their full potential in the end."
    h "Good luck, Yui."
    hide nana
    show yui at left1
    y "Thank you. I’ll make sure to preserve our lead."
    h "We’re pretty far ahead, so having someone like Yui play in the fourth position was a smart choice, Nana."
    n "Yeah, her defensive game is crazy. Unless she’s in the middle of a riichi, she’ll never deal in."
    hide yui
    show xenia at left1
    x "I can never tell if she’s lucky or if she’s just good at calculating odds though."
    h "Well, no matter what, she’ll definitely insist that all of her plays were calculated."
    x "Well, if nothing else, she certainly has a perfect poker face."
    if girl=="Yui":
        hide hinata
        show hat at right1
        k "(Yui looks so calm while playing. Like she’s got everything totally under control.)"
        k "(Other people might say that she’s just very lucky, but I think she’s just playing in a way that maximises the chances of success.)"
        k "(It’s as if she’s making a million calculations at once in regards to what could be in the wall and her opponents’ hands.)"
        hide hat
    hide hinata
    show nana at right1
    n "Yep, with a face like that she was pretty much born for either mahjong or poker."
    hide nana
    hide xenia
    "(Time passes.)"
    show hinata at lefthinata
    h "Great work, Yui. Not only did you preserve our lead, but you even extended it a bit."
    show yui at right1
    y "Thanks. Good luck, Keikumusume. Don’t be nervous, just remember what you practiced and play defensively."
    hide hinata
    show nana at left1
    n "Yep. Given that you’ve only been here for a few days, the curse shouldn’t have taken hold of you yet. You’ll do great."
    y "Don’t worry about that curse. It’s all just superstition."
    hide nana
    show hat at left1
    k "Thanks. I’m going to keep this lead and we’re going to win!"
    scene bg tablemat with fade
    show hat
    k "(Alright, I’ve got this. No need to be nervous.)"
    k "(We have a 42,000 point lead over everyone else.)"
    k "(There’s absolutely no way I can lose here.)"
    hide hat
    show hat at left1
    show cat at right1
    i "Oh Keiku, long time no see nya!"
    k "(Huh? Is that who I think it is? No way.)"
    k "Ichihime, is that you?"
    i "That’s right nya. It’s nyice to see you again!"
    k "(Oh wow, she just ran straight up and hugged me.)"
    k "(I appreciate the sentiment, but now I’ve got that gross cat hair all over me again…)"
    k "It’s nice to see you again too. How’s everyone in the shrine doing?"
    i "They’re all doing good. Riu says that she’s looking forward to working with you once you graduate highschool and join the MCD full time."
    k "Ah, maybe I’ll have to take her up on that tea offer she gave me after the Joseph incident."
    k "By the way, what are you doing here? You’re one of the top players in Japan, aren’t you a little too important for a tournament like this?"
    i "Nyat at all. Mahjong is fun, but when I’m doing it for work they’re all like ‘oh no Ichihime, you can’t pon this, can’t kan that’, and it’s very boring."
    i "So this seemed like a fun way to spend my day off."
    i "Anyway, good luck Keiku nya!"
    k "You too!"
    k "(Wait, she’s a monster player, why would I wish her good luck?)"
    k "(If anything, it’d only be fair for me to wish she has bad luck.)"
    k "(Whatever. No matter how good her luck is, I just need to play better than her.)"
    k "(We’re The Winning Team! There’s no one we can’t beat!)"
    scene bg black with fade
    "(Time passes.)"
    scene bg tablemat with fade
    show hat at left1
    show cat at right1
    k "(Alright! The hanchan’s almost over! I can’t believe I’ve actually managed to hang onto our lead.)"
    k "(I might have taken a hit here or there, but I’ve still got a lead of 20,000 points. I just need to make it through this final hand.)"
    i "Double riichi nya!"
    k "(Hoh? A double riichi? Don’t make me laugh. Even if I deal into that, we’ll still be in first.)"
    k "(But just to be sure, I’ll play around it.)"
    k "(I’ll discard this worthless Xia tile. That’ll be safe.)"
    stop music
    play sound "audio/yakumandealin.mp3"
    #{play https://www.youtube.com/watch?v=iVay367HM3Y}
    i ". . ."
    k ". . ."
    play sound "audio/ronnya.mp3"
    i "RON NYAA!"
    play sound "audio/yakunya.mp3"
    i "Kokushi musou! That’ll be 48,000 points, please."
    i "Good game everynyan!"
    k ". . ."
    k "Y-yep. Good game."
    k "T-thanks for playing guys."
    scene bg seats with fade
    show hat at left1
    stop sound
    play music "audio/wcdonalds.mp3" fadeout 1.0 fadein 1.0
    k "What were the odds! Who wouldn’t have discarded the xia against a double riichi?"
    k "(Mahjong is bullshit!)"
    show hinata at righthinata
    h "There there. It happens."
    hide hat
    show yui at left1
    y "I would have done the same. You made the right move, just not in hindsight."
    hide hinata
    show xenia at right1
    x "Yeah, that was quite unpredictable."
    hide yui
    show nana at left1
    n "You can’t fight off a curse."
    x "You can make the right play and you get hit by a daisangen just because."
    x "That’s mahjong, baby."
    hide xenia
    show hinata at righthinata
    h "So really, don’t feel too bad, Keiku. You were great out there."
    n "Really, you were just unfortunate that today happened to be Ichihime’s day off."
    hide nana
    show hat at left1
    k "Awawawawa."
    k "Thanks, guys."
    hide hinata
    show cat at right1
    i "Thanks for playing, Keiku. I had a lot of fun seeing you again."
    i "Make sure to stop by the shrine sometime nya."
    k "Call me if there’s another murder."
    hide hat
    show nana at left1
    n "Oh, can we all get autographs, Ichihime?"
    i "Of course. Anything for a beloved fanya."
    hide cat
    show yui at right1
    y "Keiku. How do you know Ichihime?"
    hide nana
    show hat at left1
    k "She was involved in the very first mahjong crime I solved. It was a murder that had occurred within the shrine."
    hide yui
    show hinata at righthinata
    h "They really just let you take a murder for your first case? Involved with the Mahjong Soul Shrine no less? Is that even legal?"
    k "Yep. You’d be surprised at what the MCD can get away with."
    k "If you’re a detective, it’s totally legal for you to just give your work to someone else with zero training."
    hide hinata
    show nana at right1
    n "Wow, what a weird system. It sounds like something out of a manga or a detective game."
    hide hat
    show cat at left1
    i "It was pretty surprising to see someone like Keiku show up instead of a typical detective."
    i "I’ve gotta get going nyao. It was nyice meeting you all. Sayonyara."
    hide cat
    show hinata at lefthinata
    h "I’m surprised at how nice a celebrity like her is in person."
    hide hinata
    show hat at left1
    k "So what happens now? There’s no award ceremony or anything?"
    n "Nope. That’s that."
    h "Thanks a lot for joining the club, Keiku. If you weren’t here we might not have been able to play. It was a lot of fun."
    k "No, thank you all for having me. I didn’t think that losing at mahjong could be this fun."
    k "What happens now, though?"
    hide hat
    show yui at left1
    y "Now it’s time for the club’s tradition."
    n "Yep. Whenever we play a tournament we go out for WcDonald’s afterwards."
    hide yui
    show xenia at left1
    x "You know, I could always pay for us to eat somewhere nicer than in WcDonald’s."
    n "Nonsense. No one else does a chicken burger as good as their WcChicken."
    hide nana
    show hinata at righthinata
    h "The food might be awful, but tradition is tradition."
label maccas:
    scene bg maccas with fade
#    {play  https://www.youtube.com/watch?v=szDKbPLq-to }
    show nana at left1
    n "Alright girls, what do you each want?"
    show hinata at righthinata
    h "I’ll just have a salad and a WcFlurry."
    hide hinata
    show xenia at right1
    x "I’ll have a black squid ink burger."
    n "For me, it’s the WcChicken."
    hide xenia
    show yui at right1
    y "I’d like a Happy Meal with the transformers toy."
    hide yui
    show hat at right1
    n "Keiku, what will you have?"
    k "Hmmmmmmm."
    k "I’m feeling pretty hungry. What’s a big burger on the menu?"
    hide nana
    show hinata at lefthinata
    h "The Big Wac?"
    k "That looks big, but I want to go bigger."
    hide hinata
    show nana at left1
    n "Well then, what about the Bigger Wac?"
    k "That does look even bigger, but not quite big enough."
    k "Hmmmhmmm."
    k "I’ll have the Biggest Wac."
    hide nana
    show yui at left1
    y "Will you really be alright eating something that big?"
    k "Of course. The fat all just goes to my thighs in the end anyway."
    scene bg maccastable with fade
    show nana
    n "Before this feast begins, I’d like to say a few words."
    n "Today you all played extremely well. Every single one of us deserves praise."
    n "Especially Keiku here, who would have won us the whole shebang, were it not for that awful curse."
    n "Mahjong is a game of skill, but also luck."
    n "So as long as each and every one of us did our best, we really don’t need to worry about whether or not we won or lost."
    n "Everyone in the tournament who sincerely played their best is a winner in my eyes."
    n "Kanpai!"

#    {The following line was originally labelled as ‘everyone else’, I’m not sure how it should be done correctly. For now I’ll keep it as just text without character but please consider changing.}
    everyone "Kanpai!"
    hide nana
    show nana at left1
    show hat at right1
    k "That was a nice speech, Nana."
    k "Although honestly I kind of feel like that was directed at me specifically. I don’t see anyone else at this table that recently dealt into a yakuman."
    n "Hehe, I simply thought you could use the reassurance."
    hide nana
    show hinata at lefthinata
    h "If you think about it though, that speech really does apply to all of us. We’ve all dealt into yakumans."
    hide hat
    show yui at right1
    y "If you extrapolate further, that speech applies to everyone who plays mahjong."
    y "Statistically speaking, everyone will eventually deal into a yakuman if they play long enough."
    hide hinata
    show xenia at left1
    x "Yui, would you say that you believe everyone is destined to deal into a yakuman? I didn’t know you believed in things like destiny."
    y "I wouldn’t say it’s like destiny. It’s more like a force of nature."
    y "It’s like dying. It’ll happen to everyone eventually."
    hide yui
    show hinata at righthinata
    h "That’s a pretty morbid comparison, but you’re not wrong."
    h "All you can really do is to try and prolong the time before your inevitable yakuman deal-in. There’s no need to feel bad about things you can’t control."
    h "I think the same thing applies to fourth places in mahjong. Eventually, everyone gets hit by a fourth place. So you shouldn’t feel bad about it when it does happen to you."
    x "But when you think about it that way, it really does beg the question of why we even play mahjong in the first place."
    x "If it’s inevitable that we’re going to get unlucky and take fourth place every now and then, isn’t it also just as valid to say that everyone will get lucky and take first eventually?"
    x "Can one truly be proud of a first place that was inevitable?"
    hide xenia
    show nana at left1
    n "Personally, I don’t really think about that. I don’t have to look for ways to cope after I take a first place, so there’s no need to think about that sort of thing, ehehehe."
    h "I suppose it goes back to the age old arguments about luck versus skill in mahjong."
    n "Remember the mahjongers’ old adage. ’It’s just luck whenever you win, and pure skill when I win!’"
    hide hinata
    show xenia at right1
    x "Nana, that’s nothing more than a coping strategy."
#    {The next line originally said ‘your average mahjong’, without ‘player’. I’m not sure whether it was intentional, please double-check.}
    x "Although your average mahjong player definitely needs plenty of those."
    hide nana
    show yui at left1
    y "True skill in mahjong is reflected in your performance over hundreds of games. A wide space is needed to eliminate the influence of flukes and chance."
    y "So I don’t think a tournament like this is really reflective of any team’s true skill. It’s just five hanchans after all."
    hide xenia
    show hinata at righthinata
    h "Exactly. Now if this was a league that went on for weeks and weeks of games, that would be a bit more accurate."
    hide yui
    show nana at left1
    n "Can you imagine if we, The Winning Team, entered a league like that and lost?"
    n "We wouldn’t even be able to blame it on bad luck. We’d look like total idiots!"
    hide hinata
    show xenia at right1
    x "Ahahahaha. Yes, indeed. At least this way we can invent a curse to blame it all on."
    hide nana
    show hinata at lefthinata
    h "Hey, Keiku’s been quiet for a while."
    h "Keiku, are you alright there?"
    hide xenia
    show hat at right1
    k "Mmmm… oh….mffff….yeah, I’m just eating, still."
    h "You’re really going at that Biggest Wac. You’re barely halfway done. Are you sure that you’re going to be able to finish that?"
    k "Well, I have to admit, I am starting to feel a bit full. I’ll be fine though."
    k "All that stuff you guys were saying was really inspiring."
    k "I always thought that games were all just like, you either win it or you lose it."
    h "The random nature of mahjong makes the line between a win and a loss a bit blurry."
    h "In some situations, you can come third and lose points, but still consider that a victory."
    hide hinata
    show yui at left1
    y "I think that it’s possible to even consider certain fourth places as victories."
    y "Given all the elements of the game that are out of your control, you could hypothesize that there is a maximum score and placement one can get in each game relative to one’s opponents."
    y "Thus your goal in each game would simply be to achieve that maximum score. Even if that score is in fourth place, you would want to achieve it so that damage can be kept to a minimum."
    k "I see, I see."
    k "Maybe you could apply this to life in general too? We’re all just trying to do our best in life. We shouldn’t be moaning about how we could have gotten more out of it, just so long as we’ve gotten the most we could have out of it."
    hide yui
    show xenia at left1
    x "I think that’s a splendid way of looking at life, Keiku."
    x "But, the trouble with that way of thinking is not knowing whether you’ve done everything you can or if you can go even higher."
    hide xenia
    show nana at left1
    n "Well, maybe it’s like, there’s no way of knowing if you’ve really done everything you can, so you should just always keep going as hard as you can to get as close to it as possible."
    k "I think I finally understand why this game is so important to people now."
    k "Mahjong is just like life, in the end. We’re all thrown about by random chance and we’re just trying to make the best of what we’re given."
    hide hat
    show hinata at righthinata
    h "Yeah, mahjong sounds like a pretty apt metaphor for life when you put it that way."
    h "Although it’s a little depressing to think about. Mahjong and life both have winners and they both have losers."
    n "That’s fine. All you have to do is just try to not be one of the losers."
    h "Maybe life would be nicer if we all just collectively decided to go noten every turn."
    hide nana
    show yui at left1
    y "But then there’d still be winners and losers based on the seating placements."
    hide hinata
    show xenia at right1
    x "I think the metaphor breaks down at that point."
    x "Keiku, how’s the burger? You’re still only halfway through."
    hide yui
    show hat at left1
    k "Yeah, this is definitely way too big."
    k "I think I’m just going to take it home with me."
    k "(I’ll just keep it under my hat.)"
    hide xenia
    show hinata at righthinata
    h "..."
    hide hat
    show nana at left1
    n "..."
    hide hinata
    show yui at right1
    y "..."
    hide nana
    show xenia at left1
    x "..."
    hide yui
    show hat at right1
    k "What? What’s wrong, guys?"
    x "Did you just put the burger under your hat?"
    k "Yep. What about it?"
    hide xenia
    show nana at left1
    n "Doesn’t that get it dirty? Doesn’t that feel gross?"
    k "Oh, don’t worry about that. It just works."
    hide nana
    show yui at left1
    y "Does it?"
    k "Yep."
    hide yui
    show hinata at lefthinata
    h "I could swear the hat just winked at me..."
    k "Anyway, it looks like everyone's done eating, so what happens now?"
    k "(It’s only 5pm and I’ve got nothing to do tonight. I might as well stay in the city a while longer.)"
    k "It’s getting a little late, but I think I’m going to hang around the city a bit."
label pre_date3:
    if girl=="Yui":
        jump yui_date3
    if girl=="Nana":
        jump nana_date3
    if girl=="Xenia":
        jump xenia_date3
    if girl=="Hinata":
        jump hinata_date3
label post_date3:
    scene bg black with fade
    "*Weeks later.*"
    scene bg classroom with fade
    show hat
    k "(Today was so draining.)"
    k "(It’s my birthday, but I haven’t gotten a single message about it.)"
    k "(This is the first time I’ve had a birthday like this.)"
    k "(In the past, Watson would always send me a little gift.)"
    k "(They were never anything huge, but the acknowledgement was nice.)"
    k "(I never knew how much I would miss that, until it was gone.)"
    k "(I thought that at least [girl] would maybe text me.)"
    k "(Normally, I feel super excited about going to club after class, but today I don’t know if I’m feeling up to it.)"
    k "(I should still go anyway, though. Everyone expects me there.)"
    scene bg clubroomblack with fade
    show hat
    k "(What the heck? Why aren’t the lights on? Where’s that switch? Where’s everyone else? Did club get cancelled?)"
    k "(Ah, here it is.)"
    hide hat
    play music "audio/keikubirthdayparty.mp3" fadeout 1.0 fadein 1.0
    scene bg clubroom
    show yuip
    y "Surprise, Keiku! Happy birthday!"
    hide yuip
    show hinatap
    h "Surprise, Keiku! Happy birthday!"
    hide hinatap
    show nanap
    n "Surprise, Keiku! Happy birthday!"
    hide nanap
    show xeniap
    x "Surprise, Keiku! Happy birthday!"
    #{Play https://www.youtube.com/watch?v=eFg4dyUuVlM }
    hide xeniap
    show hat
    k "..."
    k "This is for me?"
    hide hat
    show hat at left1
    show xeniap at right1
    x "Of course it’s for you. You’re part of this club, are you not?"
    k "I didn’t think anyone would remember or care."
    hide hat
    show hinatap at lefthp
    h "Of course we remembered. Everyone in this club is precious."
    hide xeniap
    show yuip at right1
    y "We even made a cake."
    hide hinatap
    show nanap at left1
    n "We got a keiku for Keiku."
    hide yuip
    show hat at right1
    k "..."
    k "You guys are the best."
    hide nanap
    if girl=="Hinata":
        show hinatap at lefthp
        h "Keiku, I brought you a birthday gift. See? It’s the strawberries we planted together. Happy birthday, Keiku."
        hide hinatap
    if girl=="Yui":
        show yuip at left1
        y "Keiku, I made this for you. It’s a garage kit of the main character from ‘Cry of the Seacat’. Happy birthday."
        hide yuip
    if girl=="Nana":
        show nanap at left1
        n "Keiku, check out what I got you. It’s your own karaoke machine. I had a peak at the music on your phone and loaded it up with your favourite tracks. Happy birthday."
        hide nanap
    if girl=="Xenia":
        show xeniap at left1
        x "I got something for you here, Keiku. It’s a bottle of the finest champagne I could smuggle out of the house. Don’t let the teachers catch you with it on your way out. Happy birthday."
        hide xeniap
    hide hat
    show hat
    k "Thanks, I love it, I love you, [girl]!"
    k "I can’t believe you all did this for me."
    k "I’m so happy I joined this club now."
    k "Where’s that counsellor? I owe the hag a big thank you."
    k "You guys really are the best!"
    hide hat
    show hatp
    $ renpy.pause (15.0)
    jump credits

label credits:
    scene bg credits with fade
    "Written by anon"
    "Coded by anon"
    "Spell checked by anon"
    "Miscellaneous done by anon"
    "Artwork done by anon's >wife"
    "From everyone at >The >'Winning' >Team, thanks for playing"
    stop music
    "..."
    "..."
    "..."
    "..."
    "..."
    "..."
    jump bog

label bog:
    scene bg bogged with fade
    play music "audio/bogdanoff.mp3" fadeout 1.0 fadein 1.0
    b1 "How is ze Prophecy proceeding?"
    b2 "It seems zat our agents have been able to distract her. She has totally forgotten about ze UGR."
    b1 "Excellent. It appears zat Watson has failed."
    b2 "Better luck next time, old man, nyohohohohoh."
    b1 "Have we gathered enough flow yet?"
    b2 "We have, indeed. If Keiku had begun investigating us from the start, we would have likely lost already."
    b2 "Now is ze time for us to strike. By ze time she realises her error, it will be too late."
    b1 "Love truly is ze sweetest poison of them all. Nyohohohoho."
    b2 "Perhaps one could say zat love is like a blindfold."
    b2 "With love, it cannot be seen."
    boss "Is everything proceeding according to plan?"
    b1 "Of course. Everything is going exactly as ze Dead Sea Scrolls predicted."
    boss "Ah, then our rigging was a success."
    boss "My return to the throne of the Akashic Record is inevitable."
    boss "Soon, the walls will be under my control."
    boss "OHOHOHOHOHOHO!"
    b1 "ALL HAIL THE UGR."
    b2 "ALL HAIL THE UGR."
    boss "ALL HAIL THE UGR."

    "When the Haipai Cry, Part 3: Killing Arc."
    "Release date: To be announced whenever FromSoft drops a trailer for Armored Core 6."








return
