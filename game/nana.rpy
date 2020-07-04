label nana_date1:
    scene bg schoolfront with fade
    show hat
    play music "audio/fencingwithnana.mp3" fadeout 1.0 fadein 1.0

    k "(Nana seemed like a fun person to be around. I’ll call and ask her if she wants to hang out.)"
    "* abababa* *abababa*"

    n "Yo! Who’s this?"
    k "Oh, it’s me, Keikumusume."
    n "Ah, the new girl! What’s up?"
    k "Well, I’ve got nothing on tonight, so I was wondering if you’d want to hang out."
    n "You’ve called with great timing."
    n "I was actually planning on doing some fencing, but my usual partner for that is away sick today."
    n "Until you called up I wasn’t sure if I was going to be able to do it today."
    n "Meet me in the gym asap!"
    k "(Wait, fencing? Isn’t that the sport with the swords? I didn’t think she would just invite me to something like that right off the bat.)"
#    {bg change to the gym. Consider having hat png and nana png with png fencing masks over their faces and (blunted sport) fencing blades, mite b funny}
#    {Play https://files.catbox.moe/i91fhx.ogg }
    hide hat
    scene bg gym with fade
    show hatfence at left1
    show nanafence at right1
    n "Keiku, have you ever done this before?"
    k "Nope. I don’t know the rules at all. What am I meant to be doing here?"
    n "It’s simple. You just try to hit the other person with the end of the blade."
    k "How do you tell when a point is scored?"
    n "Each blade has a button on the end of it. When it gets pushed against another person, it plays a big buzzer sound."
    k "Isn’t this dangerous? Aren’t there safety precautions or something that we should be going over?"
    n "Nah. Look, they bend to soften the impact. Totally harmless."
    n "First to ten points wins. Get ready!"
#    {play schwing sound effect, then buzzer.}
    n "Point one to me~"
    k "(S-she’s fast!)"
#    {Play clank then schwing sound effect}
    n "Nice work! You’ve only just started, but you already figured out what a parry is. Although you’re still a little too slow."
    k "(Damnit, when she talks like that, I really want to beat her!)"
#    {Play continuous sword clanging noises}
    k "(Kgh, she’s so fast!)"
    k "(But I’m starting to get the hang of this. I can keep up with her!)"
#    {Play BZZT sound}
    k "(Ah! She got me again!)"
    n "Honestly, you’re learning pretty quick. You only just started, but it looks like you’ve intuitively worked out the proper way to space your feet already."
#    {Moar sword noises}
#    {BZZT}
#    {BZZT}
#    {BZZT}
#    {BZZT}
#    {BZZT}
#    {BZZT}

    k "(She keeps complimenting me whenever she scores, but I can’t get a hit on her at all.)"
    k "(I’m not sure if that’s encouraging or just annoying.)"
    k "(I think that there’s only one way I’m going to get a hit on her...)"
    k "(...and that’s to engage in some unconventional tactics!)"
    n "Are you ready? This will finish it off!"
    k "(Here she comes, she’s charging in like usual…)"
    k "Nana, behind you, WATCH OUT!"
    n "Huh?"
    k "Gotcha!"
#    {BZZT}
    k "(I can’t believe that worked!)"
    n "Aaaaaa, I can’t believe I fell for that. What a dirty trick."
    k "Sorry, is that frowned upon in fencing? Can’t blame a novice for not knowing."
    n "Hehe, that’s fine. All’s fair in love and war after all."
    n "9-1! Next bout! Go!"
    k "(I doubt that last technique is going to work again, but there’s still no way I’ll be able to take her head on.)"
    k "(I can see how she attacks now. She always points high! Like she’s aiming for the head.)"
    k "(I think it’s called a lunge? When she leaps forwards with her arm outstretched, like a scorpion stinging its prey.)"
    k "(Honestly, it’s kind of beautiful in a way. She’s so fast. The form is perfect. You can tell she’s practiced it a lot.)"
    k "(But today that’s going to be her downfall.)"
    play sound "audio/thud.mp3"
#    {play thud noise}
#    {BZZT}
    n "What!"
    play music "audio/sliceoflife.mp3" fadeout 1.0 fadein 1.0
    n "I don’t believe it. You dived right onto the floor. You went prone just as I lunged, and ducked under the blade."
    n "That’s ridiculous, but it worked."
    k "(I won’t be caught by those lunges anymore. This is it, it’s time for my counter attack!)"
    k "(Next I’m going to do something even more ridiculous.)"
    k "(Nana called this a blade, but that couldn’t be further from the truth.)"
    k "(A blade is designed for cutting and slicing things.)"
    k "(But in this game, you score so long as the button on the tip pushes against your opponent.)"
    k "(So in truth, this isn’t a blade at all!)"
    k "(It’s a javelin!)"
#    {woosh sound effect}
#    {BZZT}
    n "What the hell! You can’t throw your blade at someone, that’s against the rules."
    k "Sorry, but all I remember about the rules was being told that I score whenever my blade’s tip pushes against my opponent!"
    n " . . . "
    n "Ahahaha, I guess I can’t argue with that."
    k "3-9!"
    k "(This time, I’m going to counter that same lunge again.)"
    k "(I’ve got an absolutely ingenious strategy too. I’ll simply hold my blade in front of me, and then she’ll jump into it!)"
    n "Uwooooooooh!"
    k "(Here it is, her lunge! I’ll just hold my blade out like this and…)"
    k "(Wait, she’s not pointing the tip at me?)"
    k "(She just forced my blade out of the way!)"
#    {BZZT}
    n "Those were some fancy tricks, but they weren’t going to beat good old fashioned practice."
    n "GG. Well played."
    k "D-don’t think this means you’ve won!"
    k "We’re going again!"
#    {sword noises, fade into black. Stop sword noises, show outside the gym at sunset}
#    {Play https://www.youtube.com/watch?v=iawEZ2ejWm8&list=PLeKSx7u-0kRiJqH14dswC-lHh8Nuu0APx&index=22}
    hide hatfence
    hide nanafence
    play music "audio/nanadate1.mp3" fadeout 1.0 fadein 1.0
    show hat at left1
    show nana at right1
    k "(I feel so sweaty. I’m all out of breath. I think I’ve even got a bruise or two.)"
    k "(So why do I feel so good? It’s like there’s electricity popping off in my head.)"
    k "(Ah, Nana looks worn out too.)"
    n "Aaaaaaa, that was great. Wait there, I’ll be right back."
    hide nana
    k "(Eh? Where’s she going?)"
    k "(. . .)"
    k "(. . .)"
    k "(It’s been five minutes, where’d she go?)"
    show nana at right1
    n "Keiku, catch."
    k "(This is a can of juice?)"
    k "Is this for me?"
    n "Yep. I owe you for coming out at such short notice."
    n "That was a tonne of fun."
    k "I wasn’t even very good at it though."
    n "That’s fine, that’s fine! It doesn’t matter if you’re good or not. What matters to me is just that you gave it a go."
    n "I wouldn’t have been able to play at all if you weren’t here."
    n "Also, you’ve never done this before, so it would have been really embarrassing if I lost."
    k "Couldn’t you have just joined the fencing club if you wanted to do this?"
    n "No way. It’s like I said before. I can’t commit to any clubs other than the mahjong club."
    n "So I just do this stuff whenever I happen to have the time."
    k "Why’s the mahjong club the exception then?"
    n "Well, the mahjong club is a little less maintenance, and I could potentially make a career out of it."
    n "Also, I actually find it to be the most fun out of all the sports clubs. Also there isn’t a skateboarding club."
    k "Hmm, I see."
    n "Anyway, I have study to do now. I’ll catch ya later."
    k "(I guess it’s about time I got going too.)"
    k "(Hey, this juice is actually pretty good. She has good taste.)"
#    {Background transition to Keikus room at night, with crickets playing.}
#        {same as above. Never gonna date nana in my life ;_;}
    scene bg keikunight with fade
    play music "audio/crickets.mp3" fadeout 1.0 fadein 1.0
    show hat
    k "(That was really tiring.)"
    k "(But I guess that’s a good thing.)"
    k "(With what happened to Watson, I’ve been struggling to sleep lately.)"
    k "(So tiring myself out before bed seems like a good strategy.)"
    k "(That was really fun. I’d like to play with Nana again soon.)"
    k "(I wonder if I could be as fit as her?)"
    k "(Nah, no way. I’m too uncoordinated.)"
    k "(. . .)"
    k "( z z z )"
    stop music
    jump post_date1


label nana_date2:
    show hat
    k "(Time to head off to the library.)"
    k "(It seems weird that she’d want to meet me in the library, but I was planning on asking her to meet me there anyway.)"
    scene bg library with fade
    play music "audio/nanadate2.mp3" fadeout 1.0 fadein 1.0
    show nana at right1
    show hat at left1
    n "Ah, Keiku!"
    k "Hey, Nana."
    n "Listen, I need to talk to you about something personal. Come over here."
    k "(What could it be? With the way she’s yanking me over, it has to be important.)"
    scene bg bookshelf with fade
    show nana at right1
    show hat at left1
    k "Alright, what’s up?"
    n "Keep your voice down. I don’t want people to overhear this."
    k "Okay, I gotcha."
    n "I need to talk to you about something weird."
    k "But why me specifically?"
    n "Well, it’s to do with a boy. I don’t think anyone else in the mahjong club has much experience with boys."
    n "Hinata is always too busy with her gardening to have a boyfriend, Xenia’s parents are way too strict to let her ever have a boyfriend, and Yui is… well, she’s Yui."
    k "Ah, well, I don’t actually have any experience with boys either. Do you?"
    n "You don’t? Ahhh, that’s a shame. Oh well, I’ll ask you anyway."
    n "And yeah, I totally have experience with boys. Tonnes."
    n "Anyway, it’s about this guy in the year below me. He’s another member of the student council."
    n "I think he really likes me."
    k "Oh, that’s great. Congratulations."
    n "No, that’s not great. I don’t like him at all."
    n "It’s not like he’s a bad guy or anything, but… he’s just not someone who could keep up with me, y’know?"
    n "It’s like, there’s no tension there, or excitement."
    k "Well, I’m sure it’ll be fine so long as you just tell him that you’re not into him."
    n "I know that’s what I probably should do, but I still don’t want to make him feel bad."
    n "Also, what if I just misread him, and he doesn’t actually like me at all? I think that’d be even worse."
    n "Like, imagine if you told someone that you didn’t have any romantic interest in them and they just said ‘yeah that’s cool, I wasn’t interested in you either.’"
    n "That’d just be way too embarrassing."
    k "(Hmmm. For someone who claims to have a lot of experience with boys, she sure doesn’t seem to have her finger on this guy’s pulse.)"
    k "Well, what makes you think he likes you?"
    n "Lots of little things. Like for example, I once made a joke about him going to the store and buying me an energy drink, and he actually did it."
    n "He said that he was planning on going down there to buy one for himself anyway, but I’ve never seen him drink an energy drink before in his life."
    n "Oh, and he’s always complimenting me when we’re doing student council stuff."
    n "Like ‘wow Nana, that’s an amazing idea.’ or ‘ah Nana, the way you think about that sort of thing is so smart.’"
    n "There was another time when there was a mugging in my neighbourhood, and he offered to walk me home. Do you think this guy likes me?"
    k "Yep, it definitely sounds like he likes you."
    n "Urgh. I really don’t want to have to go through letting him down. Like I said, he’s not a bad guy, but he’s certainly not someone I want to be with."
    k "Well, I think you should just tell him. It’s better to let him know early on, right?"
    n "Yeah. You’re right. I just gotta do it."
    n "Besides, I’ve got plenty of friends outside the student council and the mahjong club. I can probably just introduce him to one of them."
    k "If you have so many friends why’d you ask me?"
    n "Well, you just seem like a trustworthy person."
    n "Still though, thanks. Even though I was kind of sure that I needed to tell him, I feel like my head’s really cleared up now that I’ve heard someone else say it out loud."
    k "No worries. Now let’s play a game."
    n "Hoh? A game? What’ll it be?"
    k "(Hehe. I’ve picked out a game that this sports nut wouldn’t be able to beat me at.)"
    k "We’re going to be playing chess."
    n "Oh great, I love chess. I’m a big fan of it."
    k "(What the hell? That’s so out of character! I thought for sure I picked something I could win at this time.)"
    n "Don’t tell me you thought that I was just good at physical sports."
    n "I did join the mahjong club after all."
    n "Would you rather start as white or black? I’ll let you pick."
    k "No no, I challenged you, so you should pick."
    n "Well, if that’s the case, I pick black."
#    {Background transition to chessboard}
    scene bg chess with fade
    k "(She sure seems confident in herself.)"
    k "(Shoot, I’m not actually that good at chess. I should have picked shogi instead.)"
    k "(I guess I’ll start with this pawn.)"
    k "(Next the other pawn.)"
    k "(. . .)"
    scene bg chessend with fade
#    {fade to black, then transition to chessboard in a late stage game with white winning.}
    k "(We’ve been playing for a while now.)"
    k "(I’m sort of surprised that I’m winning.)"
    k "(At the start she was so confident.)"
    k "(She takes so long to make all of her moves.)"
    n "Hmmmm… ummm... ermmmm…"
    k "(I feel like the last hour has just been spent staring at her face.)"
    k "(Her hair looks so nice and soft. I wonder what brand of shampoo she uses.)"
    k "(It’s kind of funny watching her think. She stares at the board so intensely.)"
    k "(As if staring at it hard enough will make a miracle.)"
    k "Nana, do you want to forfeit the game?"
    n "No way. I could still definitely turn this around."
    n "Winners don’t give up."
    n "Hmmmmm…"
    k "Alright, take your time then."
    k "(I should have brought a book or something.)"
    n "There, that’s my move. This will turn it all around."
    k "I see."
    k "I move my rook. Check."
    n "Oof. I didn’t notice that possibility."
    n "Hmmmmm."
    k "(She looks so surprised. Back to thinking then, I guess. Yep, just keep on staring at the board, I’m sure you’ll find some sort of way out.)"
    k "(...)"
    k "(Nana has such nice eyes. I wish my eyes were green, like hers.)"
    k "They’re so pretty…"
    n "Did you say something?"
    k "Ah! No, I was just talking about the, uh, the chess pieces."
    n "I see. Hmmmm, maybe this piece?"
    k "Nana, it’s getting kind of late. Shouldn’t we pack this up?"
    n "Eh? But it’s fun. I feel like I’ve almost figured out a way I could win."
    n "Maybe we could just leave it here and finish the game on monday?"
    k "(This girl…)"
    k "(Well, I can definitely respect not wanting to give up on something.)"
    k "Why don’t we call it a draw then?"
    n "No way. That definitely wouldn’t be fair on you."
    k "Well, what if I forfeit then?"
    n "No, that’d be even worse!"
    k "(Geh.)"
    k "(It seems like there’s only one way to solve this.)"
    k "Nana, I’m putting in a new rule."
    n "Huh? A new rule?"
    k "Yep. Each move now has a timer of ten seconds."
    k "10... 9... 8..."
    n "Aaaah! Maybe I could move the, wait, no, that’d put me in check, grh."
    k "7... 6... 5..."
    n "This pawn, I’ll move this pawn!"
    k "Okay, checkmate. GG."
    n "Ah, good game."
    k "Nana, how often do you play chess?"
    n "To tell you the truth, I’ve only ever actually played it once before."
    k "Huh? But you said you were a big fan of it."
    n "Well, of course. It’s more fun to play against someone who pretends they’re good at the game, right?"
    n "If I came out and said I didn’t know what I was doing, then it wouldn’t be interesting at all."
    n "Also, if I told you I was a total novice and somehow beat you, then you’d feel pretty bad about it, right?"
    k "I guess that is true."
    k "(So that’s just her way of trying to make things interesting, is it?)"
    k "Anyway, it’s time I headed off. Loser has to pack up the game. Laters."
    scene bg train with fade
    show hat
    k "(Hmmm, that was a lot of fun.)"
    k "(Even if I spent most of the game just looking for something interesting to stare at while she thought about her moves.)"
    k "(I hope she’s able to let that boy down gently too.)"
    hide hat
    show hat at left1
    show nana at right1
    n "Oh hey, Keiku."
    k "Eh? Nana, are you on the same train line as me?"
    n "Yep. Not sure how I didn’t realise it until today though."
    k "Do you live around this area?"
    n "I think my stop is a bit further down the line than yours."
    n "By the way, thanks for hanging out with me this afternoon."
    n "I had a lot of fun. I’m sorry if I took a little long to make my moves in that game."
    n "If I’m playing a game, I just get wrapped up in it and want to do the best I can."
    n "I also really appreciate your advice from earlier. I don’t think I’m very good with emotionally sensitive stuff like that."
    n "If I told anyone else, I feel like they would have spread weird rumours around."
    n "But you just have an honest vibe to you, y’know?"
    k "Don’t worry about it. Talk to me about anything, any time you want."
    k "Anyway, my stop’s coming up. I’ll see you tomorrow at the tournament."
    n "Yep, see you tomorrow. Good luck!"
    scene bg keikunight with fade
    play music "audio/crickets.mp3" fadeout 1.0 fadein 1.0
    show hat
    k "(Well, that was a lot of fun.)"
    k "(At the very least, I can definitely say I got back at her for that fencing match.)"
    k "(I really wasn’t expecting her to ask me for advice though. On the surface she seemed like the sort of person who’s super confident in herself and wouldn’t need advice.)"
    k "(Oh well. I better go to sleep soon.)"
    k "(. . .)"
    k "( z z z )"
    stop music
    jump post_date2

label nana_date3:
    scene bg maccastable
    show xenia at left1
    x "Time to leave, I suppose."
    show hinata at righthinata
    h "Yep. Bye, everyone, see you all on monday."
    hide xenia
    show yui at left1
    y "Bye bye."
    hide hinata
    show nana at right1
    n "I actually don’t have anything I need to do at home. Do you want to hang out in the city, Keiku?"
    hide yui
    show hat at left1
    k "I’d love to. Is there anywhere in particular you’d like to go?"
    n "I know of an excellent rock climbing place near here. That’d be fun."
    k "It would be, except we’re both wearing skirts."
    n "I don’t particularly mind that, but I understand if that’s an issue. Hmmmm..."
    n "Oh, what about karaoke then!"
    k "Ah, I’m really not a good singer, and I’ve never done karaoke before."
    n "You’ve seriously never done karaoke before?"
    n "Karaoke with friends is a key part in the social life of any Japanese high schooler."
    n "Come on, it’ll be fun."
    n "Besides, no one actually expects you to be good at singing for karaoke."
    scene bg karaoke with fade
    #{Stop playing previous music}
    show hat at left1
    show nana at right1
    n "Oh look, they’ve got a bunch of anime songs on this track list."
    n "We should have invited Yui to come here. She likes these sorts of songs."
    k "Isn’t she more of the quiet type, though?"
    n "True, but you can bring anyone out of their shell if you’re enthusiastic enough."
    n "And if that doesn’t work then there’s always alcohol."
    n "Alright, I’ve picked out my song. ‘Mirai wa bokura no te no naka’."
    #{Play https://www.youtube.com/watch?v=j7myzgxz9nI }
    play music "audio/futureisinourhands.mp3" fadeout 1.0 fadein 1.0
    n "THE FUTURE IS IN OUR HAAAAAAAAANDS."
    k "(Wow, she’s even bringing out the pretend air guitar on stage.)"
    n "WE DON’T NEED ANYONE’S RULES."
    n "WE DON’T NEED ANYONE ELSE’S MORALS."
    k "(Nana’s singing is so…)"
    k "(Her singing is so…)"
    k "(Her singing is so awful!)"
    k "(She’s completely off key and can’t hold a consistent tone.)"
    k "(It’s more like shouting than singing.)"
    k "(But even in spite of that, it makes me feel all fired up!)"
    k "(Her singing is awful, but she’s up there belting it out, anyway.)"
    k "(And she’s having a great time, too. That’s amazing confidence.)"
    k "(What the hell, why was I worried about embarrassing myself.)"
    n "DAAAAAA"
    n "OOOOOO"
    n "AAAAAAAA"
    n "..."
    stop music
    #{cut music}
    n "Alright, how was that?"
    k "Amazing! You look so cool up there."
    n "Hehe, naturally."
    n "Alright, I’ve embarrassed myself, now it’s your turn."
    k "Right. Hmmm, what to sing, though."
    k "This song looks nice. ‘Nantokanare’."
    k "Ahem."
    #{play https://www.youtube.com/watch?v=NvJGKyiGPyQ }
    play music "audio/nantokanare.mp3" fadeout 1.0 fadein 1.0
    k "Y-yaseeeeeee."
    k "G-gaman bakkari deee."
    k "Mou…"
    k "(. . .)"
    k "(Crap, I stopped following the lyrics!)"
    k "Nantoka-"
    n "Sing it louder!"
    k "NANTOKANAREEEEEEE"
    n "YEAH, THAT’S IT."
    #{‘nk’ = both at the same time}
    n "NANTOKANAREEEE"
    k "WOAAAAAAAH"
    n "NANTOKANAREEEEEEEE"
#    {cut music}
    stop music
    n "Great stuff, Keiku. See how much fun it is to just belt it out?"
    n "Let’s do a proper duet this time."
    k "Hmmm, hmmm..."
    n "Oh, how about this song?"
    n "‘You wa shock’."
    k "Alright, let’s do it."
    k ". . ."
    #{Play https://www.youtube.com/watch?v=sPPVgHQu09Y }
    play music "audio/youwashock.mp3" fadeout 1.0 fadein 1.0
    n "YOU ARE SHOCK!"
    k "Because of your love, even the sky collapses..."
    n "YOU ARE SHOCK!"
    k "...as you fall down into my embrace."
    n "YOU ARE SHOCK!"
    k "Even if someone ties my heart into chains."
    n "It’s no use!"
    k "With a flick of my finger, I’ll knock down anyone in my way."
    n "YOU ARE SHOCK!"
    k "(Karaoke really is fun! I’m so glad Nana dragged me into this.)"
    n "Keiku, let’s sing all night!"
#    {fade bg to black, fade to train night time.}
#    {play https://www.youtube.com/watch?v=sdpmAAuR1N0&list=PL3-XFrU0Gj6lCJmooIqRJX-kYwhP3fOce&index=14 }
    scene bg train with fade
    play music "audio/keikunanatrain.mp3" fadeout 1.0 fadein 1.0
    show hat at left1
    show nana at right1
    k "Phew, that was a lot of fun, but my voice is all tired out now."
    n "Yeah, that was great. I didn’t know that you had such a loud voice in you, Keiku."
    k "I didn’t know I had it in me either, ehehehe."
    k "Oh yeah, whatever happened between you and that guy who had a crush on you?"
    n "I followed your advice, of course."
    n "He was pretty heartbroken at first, but I was able to hook him up with another one of my friends, so it all worked out."
    n "So thanks. That’s a load off my back."
    n "Say, do you want to hang out again tomorrow?"
    k "Of course. What do you want to do?"
    n "Just meet me on the train. Make sure you’re wearing something you can move freely in."
    k "Alright then. I’ll see you tomorrow."
    n "I’m looking forward to it."
    scene bg keikunight with fade
    play music "audio/crickets.mp3" fadeout 1.0 fadein 1.0
    show hat
    k "(That whole tournament today was a lot of fun.)"
    k "(Especially watching Nana play. The way she plays is so cool!)"
    k "(I’m really looking forward to hanging out with her tomorrow. I want to know what she has planned.)"
    k "(She’s a really great friend. A week ago I’d never have thought I’d be doing karaoke with anyone.)"
    k "(She looks so cool singing, too. Even if her singing was worse than that idol girl’s from the shrine, she was so carefree that it didn’t even matter.)"
    k ". . ."
    k ". . ."
    k "(Ugh, I’m having trouble sleeping. I can’t stop thinking of Nana.)"
    k "(I guess that just means I’m excited to see her tomorrow.)"
    k "(. . .)"
    k "( z z z )"
    stop music
    scene bg keiku with fade
    "*Kikikanri!* *Kikikanri!*"
    show hat
    k "*Yawwwwwn*"
    #{play https://www.youtube.com/watch?v=yN77vYbXLB4 }
    play music "audio/keikunanatrain2.mp3" fadeout 1.0 fadein 1.0
    k "(Time to get up and go.)"
    k "(That’s funny. I’m not having any trouble getting out of bed this morning like I normally do on a Sunday.)"
    #{bg fade to black and into train daytime.}
    scene bg train with fade
    show hat at left1
    k "(If I’ve timed this right, I should be on the same train as Nana.)"
    show nanab at right1
    n "Yo, Keiku!"
    k "Hey, Nana! So what are we doing today?"
    n "I’m going to teach you how to skateboard."
    k "To skateboard? Isn’t that dangerous?"
    n "Yeah, a little. But it’s a lot of fun, too."
    n "I don’t think either of us are going to get injured, but I’ve got medical stuff in my bag along with the boards, so it should be fine."
    n "I’m gonna teach you how to do all sorts of tricks."
    n "Don’t worry, though, we’ll start out with just the basic stuff, of course."
    n "Y’know, ollies, kickflips, heelflips."
    n "The basics."
    k "You only said to dress lightly, so I’m just wearing my usual skirt. Is that an issue?"
    n "Nope, no issue at all."
    k "(I’m really nervous about this.)"
    k "(But I felt the same way about fencing and karaoke, and those were a lot of fun.)"
    k "(So I’m just going to trust Nana and give it my all.)"
    scene bg skate with fade
    show nanab at left1
    show hat at right1
    n "Alright, let’s just start by getting you used to the way the board moves."
    k "Standing on this board feels so wobbly, I feel like I’m about to fall over."
    n "Don’t worry, I’ve got you. Just get used to how the board feels, for now."
    k "(Nana’s hands are wrapped around my waist. They feel so warm.)"
    k "(It feels a lot smoother rolling alone with her behind me.)"
    n "See? It’s not so hard. You’re getting it."
    n "I’m going to let go now. Try just keeping your balance while rolling down this slope."
    k "Okay. I’ve got this."
    k "Aaaaaah!"
    #{Play a woosh sound effect or something}
    k "(I didn’t fall off?)"
    k "(That was actually pretty fun, let’s do it again.)"
    k "Woo!"
    n "That’s it, Keiku! You’re a natural at this."
    n "Alright, now I’m going to show you how to do a kickflip."
    n "Watch this."
    #{Play another swoosh sound effect or something}
    k "Wow, you like, flipped the skateboard. There’s no way I can do that. That looked awesome."
    n "Hehe, you’re underestimating yourself. It’s actually easy. Let me take you through the steps."
    n "First, just put your back foot at the back of the board, so that the front points upwards."
    n "Then, kick your front foot against the side of the board, to flip it."
    n "Then, once it’s been flipped, you slam your back foot down to land back on the board."
    k "I see. Point the board up, flip it, slam the back foot down on it."
    n "Yep. Three simple steps."
    k "Alright, let me try this."
    k "Ah, the board just flipped and I landed on the ground instead."
    n "That’s fine, just give it a few more goes."
    k ". . ."
    k ". . ."
    k "Grrrr."
    k ". . ."
    k "Ah, I got it this time!"
    n "Wow, you really are a natural. What happened to that klutzy Keiku from before?"
    n "Alright, now see if you can do that while moving."
    k "Okay, here I go..."
    k "Just move..."
    k "Point up..."
    k "Flip it..."
    #{Play sound effect that sounds like someone falling over.}
    n "Keiku! Are you alright?"
    k "Ugh, yeah, I’m fine. I just had a little fall."
    n "Are you hurt anywhere?"
    k "Just a bruise, but that’s fine. I wanna try this again, anyway."
    k "Just move…"
    k "Point the board up…"
    k "Flip it…"
    k "…"
    k "I got it!"
    n "Good job! That’s really impressive for a first timer."
    k "Thanks. I didn’t think I’d be able to do it."
    k "Actually, pulling that off felt like such a rush."
    n "Yeah, it’s pretty great when you master a trick."
    k "Nana, you’ve been skateboarding for years, right?"
    k "I wanna see your best, most insane trick."
    n "My best trick, huh..."
    n "Watch this. See those stairs over there?"
    k "Yeah. What about them?"
    n "I’m gonna jump ‘em!"
    k "No way. There’s, like, ten steps there. There’s absolutely no way you could make that jump."
    n "Maybe not, but I’d sure look cool if I did. So I’m gonna do it."
    n "Keiku, I hereby declare that in the event that I bungle this trick and die, which I won’t, I leave all my belongings to you."
    n "Also, please be sure to delete my internet search history from my phone!"
    n "Alright, here we go!"
    k "(Oh wow, she’s really going for it.)"
    k "(She has a lot of distance between her and the stairs, though.)"
    k "(She’s building up a lot of speed.)"
    k "(Maybe she’ll actually pull this off…)"
    stop music
    n "WOOOOO!"
    #{Play noise that sounds like a crash}
    #{cut music}
    play sound "audio/thud.mp3"
    n "Ah, shit!"
    k "Nana! Are you alright?"
    n "Owwwwwww."
    n "I definitely don’t feel alright. Something’s wrong with my ankle."
    k "Can you walk okay?"
    n "Yeah, I should still be able to… ow!"
    k "I don’t think you’ll be walking anywhere."
    n "Yeah. This really sucks, though. I would have looked so cool if I actually made that jump."
    k "Do you need an ambulance?"
    n "Nah. I just need to go home and rest."
    n "I’ll just have to hop back to the train station, I guess."
    k "Don’t be ridiculous."
    k "Here, get on."
    k "I’ll take the bag, too."
    n "Keiku, what are you doing?"
    k "I’m going to carry you back to the trainstation. Come on, hop on my back."
    n ". . ."
    n "Alright, then."
    play music "audio/keikunanatrain3.mp3" fadeout 1.0 fadein 1.0
    #{play https://www.youtube.com/watch?v=OviLl5o4l64&list=PL3-XFrU0Gj6labD69JOO6I1mjKaun2-Q-&index=6 }
    k "(She’s a lot lighter than I expected.)"
    k "(Ah, I can feel her chest pushing against my back.)"
    k "(What’s this feeling? It’s as if I can feel her heart pounding against my back.)"
    k "(I can feel her face buried in my hair, too. Her breath on my shoulders feels so warm.)"
    k "(It feels like tingles are trickling down my spine.)"
    n "Thanks for carrying me, Keiku. Really. It’s a big help."

    scene bg train with fade
    show nanab at right1
    show hat at left1
    n "I really don’t like going home this early, but it can’t be helped."
    k "Are you comfortable sitting down like this?"
    n "Honestly, no, I feel like I need to lie down. My leg hurts a little when I’m sitting down."
    n ". . ."
    n "Keiku, can I ask you something that might be a little weird?"
    k "Sure."
    n "Do you mind if I use your lap as a pillow?"
    n "It’s just that my head feels really uncomfortable like this."
    n "I can’t use the bag since it has the skateboards in it, which would be even more uncomfortable."
    k "Of course, I don’t mind at all."
    n "Thanks. This is actually really comfortable. I bet you could make a career out of being a lap pillow."
    k "Oh, Nana, your ankle, it’s bleeding a little."
    k "I should bandage it just in case. There’s medical supplies in this bag, right?"
    n "Wait, don’t look in there!"
    k "Huh, what’s this?"
    k "‘Lovely Complex Heart Skip Pop’…"
    n "Gah! Put that away."
    k "Bandage your leg up first."
    n "Fine, fine."
    k "I didn’t know you were into shoujo manga. I thought you said it was too mushy for you."
    n "Yeah, I actually really like those sorts of love stories."
    n "But if people found out I read those sorts of manga, it’d totally ruin my public image."
    k "Hehehe. There’s nothing wrong with reading those sorts of manga, Nana."
    n "Hmph."
    k "(Ah, that’s so cute.)"
    k "(I wanna take a big risk.)"
    k "(I’m always going out of my comfort zone when I’m around Nana.)"
    k "(So let’s go outside the comfort zone one more time.)"
    k "Mwah."
    n "K-keiku, did you just kiss me?"
    k "Oh god, I’m sorry. I’m sorry, Nana, I shouldn’t have done that, I just felt so caught up and I..."
    n "No, it’s fine. I’m actually glad that you made the first move there."
    scene bg nanaart with fade
    $ renpy.pause (10.0)
    n "Keiku, I love you."
    k "I’m so happy to hear that. I love you too."
    n "I really wasn’t expecting to have my first kiss today, though."
    k "Your first kiss? Didn’t you say a few days ago that you had tonnes of experience with guys?"
    n "Oh, shoot. You caught me in another lie."
    n "I was just saying that because I thought I’d look immature if I didn’t have any sort of romantic experience."
    k "Ahahahaha. I thought it was weird that someone with experience would ask for romantic advice from me of all people."
    n "But you know, I’m glad that was a lie. I’m really glad to have you as my first, Keiku."
    k "Me too, Nana."
    n "I’m gonna have to lie down like this for the whole day, so you better stay with me, alright!"
    k "Of course. There’s no way I’d leave you now."

    scene bg black with fade
    stop music
    show hat
    k "(Since I joined the mahjong club, my life has become a lot brighter.)"
    k "(In just one week, I’ve not only made friends, but also met a lover.)"
    k "(I’m not sure how long me and Nana will last.)"
    k "(Once we graduate, she’ll probably have to go start her sports career, and I’ll be super busy working for the MCD.)"
    k "(But that’s fine. That’s sort of just how highschool relationships go.)"
    k "(For now, I want to treasure this year with her.)"
    k "(I need to visit Watson’s grave again soon. In a way, he taught me to not close myself off. I need to thank him for that.)"
    k "(I can’t go back in time and spend more time with him. But I’ll be sure to treasure the time I have with Nana now.)"
    jump post_date3
