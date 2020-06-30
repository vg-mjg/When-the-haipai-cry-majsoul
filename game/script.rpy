
define k = Character("Keikumusume")
define dk = Character("Detective Keikumusume")
define p = Character("Policeman")
define z = Character("Zan")
define sp= Character("PA speaker")
define h1 = Character("Hag")
define who=Character("???")
define y=Character("Yui")
define n = Character("Nana")
define h = Character("Hinata")
define x = Character("Xenia")

label start:

    scene bg parlor
    show dhat
    dk "(Another case of mahjong cheating huh.)"
    dk "(These mahjongers, they’re just silver room rookies. I don’t know why the mcd even bothered to send me out here.)"
    dk "Officer. Tell me about the crime scene here."
    show dhat at left1
    show police at right1
    p "This group were playing a hanchan, and they found that there was an extra haku in their set."
    p "We’ve also found that the set is missing a two sou."
    dk "Have you checked to make sure that it’s a standard issue set for silver ranked games?"
    p "Yes of course."
    dk "Hmmmmm"
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
    scene bg jail
    show dhat at left1
    show police at right1
    dk "These are all four players from the hanchan, correct?"
    p "Yes, these are the four."
    p "Presenting suspect Mai Aihara."
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
    p "Ah, yes! There was an opened bottle of vodka that belonged to Zun here."
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
    dk "(It’s just a game of mahjong, I don’t understand why everyone gets so invested in it."
    dk "Zan, uh, Zucchini? Was that the name?"
    dk "Whatever. Zan, I, mahjong detective Keikumusume, sentence you to, uhhh, twenty hours of community service."
    hide police at right1
    show zan at right1
    z "Thank you! Thank you! I owe you a life debt!"
    dk "(It’s just a gambling game, it’s NOT that big of a deal!)"
    dk "Well that wraps this case up."
    hide zan at right1
    show police at right1
    p "Excellent, I’ll send the paperwork around to you tomorrow."
    dk "(Aww, not the paperwork.)"
    dk "(I almost want to go back and shadowrealm that guy now, it always has way less paperwork.)"
    dk "(I have so much school work to do as well!)"
    p "Excellent work as always detective Keikumusume. Job well done!"
    dk "No need to thank me officer. Just doing my job."
label op_credits:
    scene bg credits
    ">The Winning Team presents…"
    "A >The Winning Team production."
label moping:
    scene bg keikunight
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
    k "('Why Keikumusume, I do think that with our brains put together, we could clear out my bosses entire paycheck in just a hanchan or two!')"
    k "(I always found those jokes so corny. I'd laugh and tell you I was busy reading.) "
    k "(If I could wish for anything, right now, I'd just wish that we could play a game of mahjong together. Just one game like you wanted to.)"
label classroom:
    scene bg classroom
    "*the next afternoon*"
    show hat
    k "(Another day at school is over, huh.)"
    k "(*abababa* *abababa*)"
    k "(Yet another call from the MCD. It’s probably another case request.)"
    k "(Muted.) "
    k "(Just because uncle left the title of mahjong detective to me, they think I'll take all these requests for them.)"
    k "(I just solved a case for them last night. Give me a break.)"
    k "(Although, it’s not like I have a particularly rosey high school life to enjoy.)"
    k "(The only thing I had to enjoy at school was the literature club, and that’s been disbanded since that guy transferred to a different school.)"
    k "(I guess that's what happens in a club with just two members.)"
    k "(Even then, it wasn't much of a club, looking back on it. I just read in silence while he used it as an excuse to play video games. I don't even remember his name.)"
    k "(Kyou... Kyouta... Kyaoutako Sugi? Was that it?)"
    sp "Keikumusume. You’re wanted in the counsellor’s office. Keikumusume, please come to the counsellor’s office before heading home."
    k "(Ugh, why do they have to announce it over the speaker system like that? It’s so embarrassing.)"
label counsellor:
    scene bg counsellor
    show hag at left1
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
    h1 "We’ve already made the arrangements with the higher ups at the division for you to take a holiday."
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
    scene bg hallway
    show hat
    k "(Ahhhhhhhh! That dumb hag!)"
    k "(I guess I have no choice. It’s decided that I’m going to be joining the mahjong club.)"
    k "(I gotta do it so I’ll just do it. Just walk in and hand in that form.)"
    k "(Easy peasey.)"
    k "(Just walk in, hand in the form. Say you want to join.)"
    k "(Aaaaa, why's this so hard!)"
    k "(What if they get mad at me because I haven't memorised all of the scoring rules? I don't even know how to count fu. Aw gosh this could be so embarrassing.)"
    k "(But there’s no use thinking about that. If I can solve a murder case then I can join a mahjong club. I just need to take these first steps inside.)"
label mahjongclub:
    scene bg clubroom
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
    show hinata at right1
    h "Hello, my name’s Hinata. Welcome to the club."
    y "My name's Yui."
    k "Ah, I'm Keiku. Keikumusume! I'm very new to mahjong but I'd really like to play with you guys."
    h "That’s no problem. We all had to start somewhere."
    hide hinata
    show nana at right1
    n "Yep. Just take a seat and do your best."
    hide nana
    show hat at right1
    k "(I guess it’s fine then? There’s nothing to be worried about?)"
    y "I'm glad you came today."
    k "Eh? Really?"
    y "Yep. I don't like playing sanma at all."
    k "(Okay. This is just like the online games of mahjong I've played. There's no need to be nervous!)"
label game:
    scene bg double
    k "What to do....."
    menu:
        "Riichi":
            k "D-daburi riichi!"
        "Riichi":
            k "D-daburi riichi!"
        "Riichi":
            k "D-daburi riichi!"
    scene bg clubroom
    show nana at right1
    show yui at left1
    n "A double riichi on your very first turn? Looks like we have a prodigy in our club."
    y "Eurgh."
    hide nana
    show hat at right1
    k "(Hmmm, I think everyone's trying to fold?)"
    k "Ah, ron! Double riichi! Pinfu! That's ummm, 3900 points!"
    hide yui
    show hinata at left1
    h "So be it then."
    hide hat
    show nana at right1
    n "Wait.. that's furiten!"
    h "Oh you’re right, that is furiten."
    hide nana
    show hat at right1
    k "Wait, if my double riichi was furiten then that means…"
    hide hinata
    show yui at left1
    y "Tenhou…"
    k "(Owwwwww. Like tiles down the drain.)"
    hide yui
    show nana at left1
    n "Wow. Yikes!"
    k "Ehehe, next hand."
#    {play tile shuffling sounds}
    k "(Hmmmm... I can riichi here for a pair wait. But which wait should I pick?)"
#    {present the following options: south wind, north wind. If North is picked, play the following dialogue.}
    menu:
        "North":
            k "(I'll go with the pair wait on the north wind!)"
            k "(...)"
            k "(...)"
            k "(Come on, come on...)"
            k "(Ah, I just drew the south wind!)"
            k "(Geez come on!)"
        "South":
            k "(I'll go with the pair wait on the south wind!)"
            k "(...)"
            k "(...)"
            k "(Come on, come on...)"
            k "(Ah! I just drew the north wind!)"
            k "(Geez come on!)"

    n "Ron! That's mangan, 12000 points!"
#    {Cut music, play https://www.youtube.com/watch?v=szDKbPLq-to}
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
    show hinata at left1
    h "Yui, that's a little..."
    hide hinata
    show xenia at left1
    x "Anyway, tell us about yourself, Keiku. Oh, can I call you that? Saying ‘Keikumusume’ every time is just a little long is all."
    hide yui
    show hat at right1
    k "Oh yeah, that's fine."
    k "Well, my hobbies include reading, writing, and I'm also technically a mahjong detective."
    hide xenia
    show hinata at left1
    h "You work for the MCD? While in high school? That’s amazing."
    k "Thanks. I've only actually solved one case though."
    hide hinata
    show nana at left1
    n "Tell us about it! Is it really like how it is in all those television dramas about MCD officers? Do you have a catchphrase you shout when you send someone to the shadowrealm?"
    k "Honestly it was pretty similar to what you'd see in a detective manga, or even a video game. As for the catchphrase, I guess it was something like..."
#    {Play KAAAAN.wav}
    k "KAAAAAAAAN!"
#    {Play SORERONDE.wav}
    k "SORE RON DE!"
#    {Play YAKUMAN.wav}
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
    scene bg clubroom
    menu:
        "Who should I talk to?"

        "Hinata":
            show hinata at left1
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
            y "...Gundam"
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


        "That's all I guess" if (q1&q2&q3&q4) == True :
            jump next

label next:
    scene bg clubroom
    "*ding dong* *ding dong*"
    show hat at left1
    k "Ah, the bell's ringing."
    show nana at right1
    n "Time to go then."
    hide hat
    show hinata at left1
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
    show hinata at right1
    h "Oh, we should probably give Keiku our numbers, right?"
    h "That way we can keep her in the loop."
    k "O-oh, thank you!"
    k "(The phone numbers of four girls in one day...)"
    k "(If I was a guy I'd be over the moon right now.)"
    #{Change bg scene, Keikus room at night. Stop music, play cricket sounds https://www.youtube.com/watch?v=Olfg9KK_bmE}
    #    {add music here: some ambivalent contemplation music, like https://www.youtube.com/watch?v=-l1W6g7UYtY}
    scene bg keikunight
    show hat
    k "(They seemed like a strange bunch.)"
    k "(But I'm really happy that they accepted me so easily.)"
    k "(I wish I knew earlier that making friends would have been as easy as just walking into a club room.)"
    k "(I still feel sorta lonely. I still really miss Watson.)"
    k "(But maybe with these people, things won't be so bad.)"
    k "(. . .)"
    k "( z z z )"
    scene bg schoolfront
    show hat
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
            "faggot"

        "Nana":
            "good taste"

        "Xenia":
            "perfect taste"

        "Hinata":
            "that's art-chan for (You)"
        






return
