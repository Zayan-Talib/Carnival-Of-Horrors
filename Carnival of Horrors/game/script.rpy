# The script of the game goes in this file.

#   # Z = Not in original book
#   # X = Redundant / Removed from original book
#   Ctrl K + Ctrl 0 (Close all drop down lists)

############################################ init block ############################################

# Transformations : Sprite Position

transform center:
    xalign 0.5
    yalign 1.0

transform closeleft:
    xalign 0.38
    yalign 1.0

transform closeright:
    xalign 0.62
    yalign 1.0

transform slightleft:
    xalign 0.3
    yalign 1.0

transform slightright:
    xalign 0.7
    yalign 1.0

transform midleft:
    xalign 0.2
    yalign 1.0
 
transform midright:
    xalign 0.8
    yalign 1.0

transform left:
    xalign 0.1
    yalign 1.0

transform right:
    xalign 0.9
    yalign 1.0

transform extremeleft:
    xalign 0.0
    yalign 1.0

transform extremeright:
    xalign 1.0
    yalign 1.0

# Transformations : Sprite Size

transform correctsizeyou:
    zoom 0.78
    yoffset 130

transform correctsizepatty:
    zoom 0.81
    yoffset 130

transform correctsizebrad:
    zoom 0.77
    yoffset 155

### Image Definitions

# You

image you normal:
    "you/you normal.png"
    correctsizeyou

image you nervous:
    "you/you nervous.png"
    correctsizeyou

image you claim2:
    "you/you claim2.png"
    correctsizeyou

image you surprised:
    "you/you surprised.png"
    correctsizeyou

image you point:
    "you/you point.png"
    correctsizeyou

image you worried:
    "you/you worried.png"
    correctsizeyou

image you scared:
    "you/you scared.png"
    correctsizeyou

image you startled:
    "you/you startled.png"
    correctsizeyou

image you think:
    "you/you think4.png"
    correctsizeyou

image you believe:
    "you/you believe.png"
    correctsizeyou

image you resolve:
    "you/you resolve.png"
    correctsizeyou

image you stressed:
    "you/you stressed.png"
    correctsizeyou

image you paralyzed:
    "you/you paralyzed.png"
    correctsizeyou

image you shout:
    "you/you shout.png"
    correctsizeyou

# Patty

image patty argue:
    "patty/patty argue.png"
    correctsizepatty
    midleft

image patty idea:
    "patty/patty idea.png"
    correctsizepatty
    midleft

image patty normal:
    "patty/patty normal.png"
    correctsizepatty
    midleft

image patty surprised:
    "patty/patty surprised.png"
    correctsizepatty
    midleft

image patty speak:
    "patty/patty speak.png"
    correctsizepatty
    midleft

image patty angry:
    "patty/patty angry.png"
    correctsizepatty
    midleft

image patty worried:
    "patty/patty worried.png"
    correctsizepatty
    midleft

image patty stern:
    "patty/patty stern.png"
    correctsizepatty
    midleft

image patty wave:
    "patty/patty wave.png"
    correctsizepatty
    midleft

image patty surprised:
    "patty/patty surprised.png"
    correctsizepatty
    midleft

image patty camera:
    "patty/patty camera.png"
    correctsizepatty
    midleft

image patty think:
    "patty/patty think.png"
    correctsizepatty
    midleft

image patty smile:
    "patty/patty smile.png"
    correctsizepatty
    midleft

# Brad

image brad normal:
    "brad/brad normal.png"
    correctsizebrad
    midright 

image brad argue:
    "brad/brad argue.png"
    correctsizebrad
    midright 

image brad retreat:
    "brad/brad retreat.png"
    correctsizebrad
    midright 

image brad laugh:
    "brad/brad laugh.png"
    correctsizebrad
    midright 

image brad speak:
    "brad/brad speak.png"
    correctsizebrad
    midright 

image brad smug:
    "brad/brad smug.png"
    correctsizebrad
    midright 

image brad sweat:
    "brad/brad sweat.png"
    correctsizebrad
    midright 

image brad point:
    "brad/brad point.png"
    correctsizebrad
    midright 

image brad surprised:
    "brad/brad surprised.png"
    correctsizebrad
    midright 

image brad think speak:
    "brad/brad think speak.png"
    correctsizebrad
    midright 

image brad scared:
    "brad/brad scared.png"
    correctsizebrad
    midright

image brad reason:
    "brad/brad reason.png"
    correctsizebrad
    midright

image brad think:
    "brad/brad think.png"
    correctsizebrad
    midright

image brad doom:
    "brad/brad doom.png"
    correctsizebrad
    midright

# Other Effects

image bg entranceflicker:
    "bg entrance.png"
    pause (0.2)
    "bg darkentrance.png"
    pause (0.2)
    repeat

transform screen_shake:
    linear 0.05 xoffset -15
    linear 0.05 xoffset 15
    repeat 3

transform shakeloop:
    block:
        linear 0.05 xoffset -10 yoffset 5
        linear 0.05 xoffset 10 yoffset -5
        linear 0.05 xoffset -7 yoffset 3
        linear 0.05 xoffset 7 yoffset -3
        linear 0.05 xoffset 0 yoffset 0
        repeat

transform correctsizeBA1:
    zoom 1.7
    yoffset 105

transform correctsizeBA2:
    zoom 1.1
    yoffset 100

transform monstersize:
    zoom 1.3
    yoffset 100

image bg doomfaces:
    "bg doomscary1.png"
    0.1
    "bg doomscary2.png"
    0.1
    "bg doomscary3.png"
    0.1
    repeat

image bg chuteblink:
    "black" with dissolve
    0.5
    "bg reunited.png" with dissolve
    0.5
    repeat 3

# Other Characters

image big al:
    "others/bigal.png"
    correctsizeBA2
    midright

image map:
    "map.png"
    xoffset 200
    yoffset -200

image bg gameover:
    "bg gameover.png"
    zoom 1.2

image hazmat1:
    "others/hazmat.png"
    zoom 1.3
    yoffset 150
    extremeright

image hazmat2:
    "others/hazmat.png"
    zoom 1.3
    yoffset 150
    extremeleft

image dwarf:
    "others/dwarf.png"
    zoom 0.8
    yoffset 100

image darkmonster:
    "others/darkmonster.png"
    monstersize

image monster:
    "others/monster.png"
    monstersize

image monstershaded:
    "others/monstershaded.png"
    monstersize

# Variables are used to make it less tedious to recall who is saying which line.
# Make sure character name colors are spelled "color" and not "colour"

define y = Character ("You", who_color = "#b08f7f")
define p = Character ("Patty", who_color = "#c981c5ff")
define b = Character ("Brad", who_color = "#725621")

define mys = Character ("???", who_color = "#999999")
define mys2 = Character ("???", who_color = "#ffffff")
define BA = Character ("Big Al", who_color = "#e44441")
define dwa = Character ("The Dwarf", who_color = "#ff0000")

####################################################################################################

# Game starts here

label start:

    scene black with fade

    "Player Beware! You choose the scare."
    "Choices do matter, and you will need to make the right ones to survive. That is, if you can."

    menu:

        "Are you sure?"

        "Yes": 
            pass

    window hide
    show text "So be it." at truecenter with dissolve
    $ renpy.pause(1.0, hard=True)
    window show

    # Page 1

    scene bg playground       # This is how to call scenes
    with fade                 # Transition

    # Calling a character sprite
    show patty argue at center with dissolve

    p "What do {i}you{/i} want to do?"    # This is how you italicize text in Ren'Py

    hide patty argue with dissolve
    
    # Internal monologues can be written like this.

    "Patty and Brad. Your two best friends. Arguing. As usual."
    "It's the last week of August. And Patty and Brad haven't stopped fighting since your summer vacation started."
    "Patty likes being bossy. You don't mind, though. It's no big deal."
    "It's hard to win a fight with her anyway. You don't know why Brad even tries."
    "You guess it's because he doesn't want to look like a wimp in front of a girl."

    show brad retreat with dissolve
    
    b "There's nothing to do. I guess I'll just go home."

    "You guess Brad is kind of a wimp - even if he is your best friend."

    show patty worried with dissolve
    
    p "You're so boring, Brad."

    "Whenever Patty complains, her freckles really pop out. Now there are about a million of them spread across her face."

    show patty idea with dissolve
    
    p "Hey! I know what we should do!"
    p "Let's bike over to Bennet's Field and watch them set up the carnival!"  # Page 2

    show you nervous with dissolve
    
    y "I don't know."
    y "It's getting dark, and Mom said I have to be in by nine."

    show brad laugh with dissolve
    
    b "It's only a quick bike ride. Are you some kind of wimp?"

    show you claim2 with dissolve
    
    "Brad calling you a wimp? You can't believe it!"

    y "Okay. Okay."
    y "But if it's as bad as last year, there won't be much to see. Don't you remember the main attraction?"
    y "The ride they called Terror Track? It turned out to be a baby choo-choo train that circled around and around and around."

    "It doesn't matter what you say. Patty's made up her mind. You're going to ride over to the carnival."

    scene black       # Show black screens like this (Built-in function)
    with dissolve

    "A hot, humid breeze blows in your face as you pedal along."
    "Patty's in the lead. No surprise. And Brad's puffing behind you."
    "It's dark by the time you reach Bennet's field."
    "You and your friends drop your bikes in the grass and race across the moonlit field, toward the huge wooden fence that sorrounds the carnival."
    
    # Page 3

    scene bg fence with fade
    
    show patty normal with dissolve
    show brad speak with dissolve
   
    "As you reach the carnival entrance, you hear music coming from inside."
    "Not the usual corny organ stuff they always play. But some really strange music. It sounds familiar and totally new at the same time."

    "Brad stretches his neck to try to peer over the fence. But no luck. The fence is way too high."

    show brad smug with dissolve

    "Patty jiggles the padlock on the gate. It's sealed shut."

    show patty wave with dissolve
    
    b "I guess we'll have to wait until tomorrow night when the carnival opens."

    show patty stern with dissolve
    
    p "No way. Let's climb the fence. Now!"

    show brad retreat with dissolve
    
    b "Are you crazy? We'll get caught!"

    p "Come on. There's probably no one in there."

    show patty angry with dissolve
    
    "Your friends turn to you to cast the deciding vote."
    "You glance at your watch. It's almost 9:00 P.M. If you're going to get home in time, you should start back now."
    
    menu:
    
        "What are you going to do?"

        "Climb the fence to get inside.":
            jump climbfence

        "Decide to go home.":
            jump gohome               # Illusion of choice

label gohome:

    scene black with fade

    "You've decided not to sneak into the carnival? You're going home instead?"
    "Well, it's a good thing Patty usually makes all the decisions. Otherwise, you'd never have any fun! And this visual novel would be over before it began!"
    "Go ahead. Take a deep breath. Then go climb the fence. You're not {i}scared{/i} - are you?"

    scene bg fence
    show patty angry
    show brad retreat

    jump climbfence

label climbfence:

    y "Let's do it!"
    y "Let's climb the fence!"

    hide patty with dissolve
    
    "Patty is halfway up before you finish speaking. You let Brad go next. You're last."

    hide brad with dissolve

    scene black with fade

    "It's a hard climb up. There's really no place on the fence to get a good drip. But you make it to the top, swing your legs over, and tumble down."
    "You land on the grass. You're inside!"

    scene bg darkentrance with fade
    
    "You and your friends gaze around. It's pretty dark - the only light comes from torches."
    "At first the carnival looks the same as it always does. Dinky rides. Hot dog wagons."

    scene bg entranceflicker

    "Then the lights start to flicker on in every corner of the field - the rides start to move."
    "It's as if the whole place is magically coming to life."

    pause (2)

    scene bg entrance

    pause (1.0)

    show patty surprised with dissolve
    show brad surprised with dissolve
    show you surprised with dissolve

    pause (0.5)

    y "What just happened?"             # Z

    pause (0.5)

    show you normal with dissolve
    
    y "Hey! Look at that giant roller coaster!"
    y "They never had a roller coaster before!"

    show brad speak with dissolve
    
    b "Yeah."
    b "And the whole place is a lot bigger than last year!"

    p "THIS IS AWESOME!"

    hide patty with dissolve

    y "What? Where's she running?"

    hide you with dissolve
    hide brad with dissolve

    jump tourstart

label tourstart:

    scene bg rollerview with fade
    
    # "You and Brad take off after Patty. You all stop in front of the rollercoaster." 

    show patty surprised with dissolve

    p "Wow!"
    p "It's like a rocket to outer space!"

    show you worried with dissolve
    show brad sweat with dissolve 

    "Beyond the roller coaster, you spy a castle surrounded by a moat. And a spooky - looking haunted house sitting high atop a hill."

    show you surprised with dissolve

    y "These are the coolest rides I've ever seen!"
    y "They still have that dumb choo-choo train over there, but we could ride this stuff all night and never go near it!"

    pause (0.8)

    show patty idea with dissolve
    hide patty with dissolve
    hide you with dissolve

    "Patty grabs your arm and tugs you over to the other side of the carnival - to the midway. Brad races after you."

    hide brad with dissolve

    scene bg midway with fade

    show patty normal with dissolve
    show you normal with dissolve
    pause (0.5)
    show brad speak with dissolve
    
    y "Hey! Where are all those dinky wooden booths from last year?"

    scene bg midway with dissolve

    "They're gone. And in their place are giant video games and huge spinning wheels with hundreds of blinking colored lights!"
    "You gawk at the amazing games of chance."

    show brad point with dissolve

    b "Get a load of that!"

    "You and Patty spin around."

    show you surprised with dissolve
    show patty surprised with dissolve

    "You can't believe what you see!"

    scene bg freakshow with dissolve

    "You're staring at a sign that reads: WORLD's FREAKIEST FREAK SHOW!"
    "The three of you gape at the pictures."
    "There's the Three-Headed Man with the ugliest collection of faces you've ever seen."
    "And the Snake Lady - a young blond girl with a beautiful face and the body of a slithering snake."

    y "This is, uh - uh -"

    scene you cg face with pixellate

    pause(0.5)

    scene bg midway
    show you startled at screen_shake
    show bg midway at screen_shake

    "A large hand comes down on your shoulder. Hard."

    show big al with dissolve

    "You slowly turn and gaze up at a huge man with shoulders wider than a refrigerator. He has coal - black eyes and a thick mustache to match."
    "He looks strong enough - and mean enough - to pitch you over the fence with one hand."

    mys "What are you doing?"
    mys "You're not allowed in here."

    "He points directly at you."

    y "We're sorry."
    y "We wanted to look around. That's all. But we'll leave. Right now."

    "His eyes stare into yours. He clamps both hands down on your shoulders."

    mys "You're not going anywhere!"

    show brad reason at midleft, Transform(yoffset=85) 
    with dissolve

    b "Wh-what do you mean?"

    mys "I just had an idea. A great idea."
    mys "I just want you kids to stay and try out the rides before the grand opening tomorrow."

    show patty camera at Transform(yoffset=80, xoffset=180) with dissolve

    p "Cool!"

    show you nervous with dissolve
    show brad sweat with dissolve

    y "Are you sure it's all right with the owner?"

    mys "I'm Big Al, the manager. And what I say around here goes."

    "Big Al digs around in his checkered jacket and pulls out three maps. He hands one to each of you."

    BA "Study them carefully. If you have any questions, ask them now."

    show you think with dissolve
    show brad think with dissolve
    show patty think with dissolve

    "Your eyes fall upon the map. You have a question. But when you gaze up," 

    hide big al with fade
    show you surprised

    "Big Al is gone. He's vanished!"

    show patty smile at Transform(xoffset=600)
    show brad think speak at Transform(xoffset=-300)
    show you normal
    with dissolve

    p "A whole carnival to ourselves!"
    p "Where should we start?"

    hide patty
    hide brad
    show you think
    with dissolve
    show map 
    with dissolve

    "You stare down at your map once again. You notice that the carnival is split in half."
    "On one side are the rides. Tons of them. On the other side is the midway, packed with games of chance and the Freak Show."
  
    hide map
    hide you
    with dissolve

    menu:
  
        "What will you try first?"

        "Go on the rides.":
            jump startrides

        "Check out the midway.":
            jump startmidway

label startrides:

    show you resolve
    with dissolve

    y "Let's go on the rides first!"
    y "That roller coaster looked awesome!"

    show patty normal
    show brad normal
    with dissolve

    p "Okay."
    p "Over this way!"

    scene bg coaster with fade

    "You can only stare in amazement. These are the most fantastic rides you've ever seen."
    "The towering roller coaster … the soaring speedboats … the twisty slides! Every one is in motion."
    "Whizzing, whirling, doing loop-the-loops."
    "And they're all empty! No riders. No people in line!"

    show you normal
    show patty smile
    show brad normal
    with dissolve

    p "Cool! We have the whole place to ourselves."

    show brad doom
    with dissolve

    "Brad's face turns a little green as his gaze swings from the Supersonic Space Coaster to the Doom Slide."
    b "Do you think they have rides that don't go upside down?"

    show patty argue
    with dissolve

    p "Come on! Let's check out the coaster!"

    hide patty
    hide brad
    with dissolve

    "You stop and crane your neck to gaze up at the coaster's first hill. And you gasp!"

    show you surprised
    with dissolve

    "The tracks stretch up so high that they seem to touch the clouds." 
    "Your gaze follows one of the cars speeding around a sharp curve. It looks like the space shuttle."
    "You notice that it has a safety harness that locks over your body — you've seen those before."
    "They keep you in when the ride turns upside down."
    "You didn't want to admit it before, but, like Brad, riding upside down is not your favorite thing."
    "Still, the coaster does look amazing. One part enters a tunnel..."
    "... and you can see that the cars go fast."
    "Really Fast!"

    "You're just about to walk through the Space Coaster gate when you hear spooky organ music coming from behind you."
    "You turn around."

    scene bg farhouse with fade

    "Looming in the distance is a dark and creepy haunted house."
    "You gaze down at your map. It's called the House of Horrors."
    "Hmm."
    "You love haunted houses. And this one really does look scary."
    "Now you're not sure what to do. You won't have time for everything. The coaster or the haunted house?"

    menu:

        "Decide now."

        "Join Patty and Brad on the Space Coaster":
            jump spacecoaster

        "Go to the House of Horrors alone":
            jump horrorhouse

label startmidway:

    show you resolve
    with dissolve

    y "Let's head for the midway and play some games!"



    return

label spacecoaster:

    scene bg coaster with fade

    y "Hey, wait up!"

    "They both ignore you and charge straight ahead."

    scene bg shuttlegate with fade

    "You follow them into a narrow tunnel that leads to the boarding area." 
    "You gaze down at the floor. Black rubber. It makes you walk with a strange bounce."
    "Every few feet there is a round porthole window." 
    "When you glance out one, you see astronauts planting flags on the moon."
    "You peer out another."
    "Now they're seated in their capsule."

    y "This is amazing. The figures look real. {i}Totally real.{/i}"

    scene you cg climb with fade

    "After a long climb, you and Patty and Brad finally arrive at the loading area."
    
    scene bg shuttleload with fade
    show you normal with dissolve
    show patty normal with dissolve
    show brad normal with dissolve
    
    "A sleek bullet-shaped capsule {i}whooshes{/i} up and stops right beside you. It has three sections."
    
    hide brad with dissolve
    
    "Brad climbs defiantly into the last section."

    hide you with dissolve

    "You leap into the front."

    hide patty with dissolve

    "Patty's left with the middle section."

    show bg shuttleload at screen_shake

    "And suddenly you're trapped!"

    "Steel bars plunge down from above and drop across your lap and chest, pinning you in place."
    "You can't move at all. Even your head is held by superstrong headphones that clamp over your ears."
    "A voice comes through them."

    mys "Five, four, three, two, one, BLAST OFF!"

    show bg shuttleload at screen_shake

    "You hear a huge bang."
    "Smoke and fireworks fill the air as your car start up the first big hill."

    scene bg skyshuttle with fade

    "Your head presses back against the seat as you climb higher and higher. That first hill is endles, but the view is awesome."
    "From the top, you can see the midway, the haunted house, and a shadowy clamp. You can't believe how big the carnival is!"

    p "Neat!"
    p "There's AHHHH...."

    "Whatever she was going to say turns into a wild scream as the rocket plunges down the other side of the hill. The wind whips at your face." 
    "You are pressed back so hard, you feel like a pancake. Everything passes in a fantastic blur."

    "As your car shoots up the top of the next hill, you're laughing and screaming at the same time."
    "This is great! But then you make a big mistake."

    scene black with fade

    "You close your eyes."

    pause (0.5)

    scene bg fastshuttle with fade

    "When you open them, you car lunges forward with a burst of speed - and you loop the loop."
    "Your mouth drops open to scream, but no sound comes out."

    "Now your car starts to plunge downward. Like an elevator out of control."
    "Your heart pounds in your chest. This is the fastest and best roller coaster you've ever been on!"
    "As you near the bottom, you slow down. You begin to catch your breath. And then you see what's up ahead."

    scene bg tunnelstart with fade

    "A huge black hole - a tunnel!"
    "As you shoot towards the open mouth of the tunnel, you begin to scream again."
    "The door of the tunnel is about to close!"

    scene black with fade
    
    "Snap! The door comes crashing down - behind your car. You breathe out a long sigh."
    
    scene bg darkrocketcrash with fade

    "But now you're in a tunnel so dark that you can't see a thing."
    "Scary! But not nearly as scary as what happens next."

    show bg darkrocketcrash at screen_shake

    "The ride stops. Dead."
    "You are sitting in the dark."
    "Nothing is moving."
    
    y "Patty! Brad!"

    "Silence."
    "Why don't they answer? They have to be there."
    "You try to twist around. But you're locked in your harness and clamped in your headrest."
    
    scene bg rocketcrash with fade
    
    "Blinking in the dim light, your eyes dart to the left. Then to the right."

    "You spot dozens of empty space rockets lining the walls."
    "They seem to come in sections, making longer and shorter space rockets."
    "Your mind starts working feverishly. Did your section detach from Patty and Brad's section?"

    "Suddenly, the silence is shattered. Your seat lock grinds open, and you are released from your harness."

label waitchoice:

    scene bg rocketcrash
    show you worried with fade

    "You quickly spin around. Patty's and Brad's cars have dissapeared!"
    "If this is all part of the ride, maybe you should hop out."
    "But if the ride is broken, maybe you should wait for help."

    menu:

        "What do you do?"

        "Wait for help to come":
            jump waithelp

        "Hop out of the car":
            jump hopout

    return

label horrorhouse:

    return

label waithelp:

    "You decide to wait. Someone should be here soon, you think."

    pause(2)

    show you stressed with dissolve

    "But after waiting in the space shuttle for at least fifteen minutes, you're not so sure."
    "No one has shown up to rescue you."

    "A chill runs down your back. You feel as if a thousand pairs of eyes are watching you from the shadows."
    "Now that you're accustomed to the darkness, you can see dozens of tracks leading in and out of the tunnel."

    show you scared with dissolve

    "And then you hear a rustling sound. You freeze. You listen hard. Could it be rats..."
    "...or something worse?"

    "You draw up your knees and wrap around them tightly. Then you hear a hissing sound - and you smell something odd."
    "It's kind of a sweet smell - like heavy perfume."
    "You hold your nose because the smell is making you feel strange. Dizzy. Sick."
    
    pause(2)

    show you paralyzed with dissolve

    "It seems as if hours have passed. Or maybe it's only minutes."
    "You try to unclasp your hands. But they won't budge. It's as if your arms are glued around your knees."
    "You try to move something. Anything."
    "But you can't blink an eyelid. Your body is paralyzed. You can't even scream."

    show hazmat1 with dissolve
    show hazmat2 with dissolve

    "A door opens and two men dressed in overalls and wearing gask marks amble in."
    "Finally. They're here to rescue you!"

    mys "Looks like the perfume worked."
    mys2 "Yeah. And just in time. We needed a new dummy for the Real-Life Space Display."

    hide you
    hide hazmat1
    hide hazmat2
    with dissolve

    "They pick up your rigid body and carry you out."
    "No wonder those astronauts in the silver tunnel looked so real!"
    
    scene black with fade

    "Sorry. You can't scream. You can't escape."
    "Next time, you promise yourself, you'll stick with the baby rides. But then you remember - "
    "there isn't going to be a next time ... because this is ..."
    
    scene bg gameover with pixellate

    window hide

    pause (2)

    $ gameover_choices = [
        ("Back to Previous Choice", Jump("waitchoice")),
        ("Start Over", Jump("start")),
        ("Main Menu", MainMenu())
    ]

    call screen game_over_menu (gameover_choices)

label hopout:

    "Your pulse pounds in your ears as you carefully lift yourself out of the car."
    "The tunnel is dark and musty and really creepy. Anything could be lurking in the shadows."

    "This must be part of the ride, you reason. And the more you think about it, the more convinced you are."
    "You're scared. But you have to admit, this is pretty cool."

    "In the distance, you spot several red lights that seem to lead to other dimly lit tunnels."

    scene bg dwarftunnel with fade
    show you worried with dissolve

    "You cautiously head toward one of them. Overhead something dark and slimy drips."
    "Splattering on the top of your head. Stinging your forehead."

    "As you desperately try to wipe the burning slime away, something grabs you by the knees!"

    show bg dwarftunnel at screen_shake
    show you startled at midleft, screen_shake
    with dissolve
    show dwarf at midright
    with dissolve

    "Aaaah! You look down. A pair of red-rimmed eyes meet yours. It's a dwarf with scraggly red hair and a toothless smile."

    dwa "Want me to lead you out of here, kid?"
    
    "You're about to follow the dwarf, but then you stop."
    "Is he part of the ride? He looks really evil."

    menu:

        "What do you do?"

        "Follow the dwarf":
            jump dwarffollow

        "Decide not to follow the dwarf":
            jump dwarfstay

    return

label dwarffollow:

    show you worried with dissolve

    y "Okay, get me out of here."
    y "Did you help my friends, too?"

    "The dwarf does not answer."

    hide dwarf with dissolve
    show you startled with dissolve

    y "Wait!"

    scene black with fade

    "He sprints off and you have to race to keep up with him."
    "Through a confusing maze of twisting tunnels. You're sure glad you have a guide."
    "The dwarf suddenly stops."

    show bg twodoors with fade
    show dwarf with dissolve

    dwa "That way."

    "He points straight ahead."

    show dwarf at screen_shake
    hide dwarf with dissolve

    "Before you can blink, he vanishes in a puff of smoke!"
    "You're left standing in front of two doors. One red. One blue."
    "The red one has a sign that reads: {i}DANGER{/i}"
    "The blue one has a sign that reads: {i}BIG DANGER{/i}"

    jump doorchoice

label dwarfstay:

    "You glance once more at the dwarf."
    "He lets out an evil cackle."
    "That's it - there's no way you can trust him. Besides, you can hear music up ahead."
    "You're sure you must be near an exit."

    show you worried with dissolve

    y "No, thanks. I don't need any help."
    dwa "Oh, yes, you do."

    show dwarf at screen_shake
    hide dwarf with dissolve

    "But then he sprints off."

    pause(2)

    scene black with fade

    "You walk into the direction of the music. But after five minutes, you realize that you're not getting anywhere."
    "Maybe you should have followed the dwarf."

    show patty camera
    show brad normal
    with pixellate

    "You start to think about Patty and Brad. Are they okay? You wonder."

    "Just when you think you'll be wandering these tunnels for the rest of your life, the passageway ends!"

    show bg twodoors with fade

    "Now you're facing two doors - one red and one blue. Which one should you try?"
    "You might as well flip a coin!"

    scene black with pixellate

    "Get a coin. Flip it and check whether it comes up heads or tails."

    menu:

        "Test your odds."

        "Heads":
            jump bluedoor

        "Tails":
            jump reddoor    

label doorchoice:

    show bg twodoors with fade

    menu:

        "Which one do you try?"

        "Try the Red Door":
            jump reddoor

        "Try the Blue Door":
            jump bluedoor

label reddoor:

    show bg twodoors with fade

    "You push open the red door." 

    show bg redtunnel with fade

    "Another tunnel lies beyond it. You follow its twists and turns, and you realize that you're sloshing through cold muddy water."
    "It grows deeper and chillier as you go."

    show you worried with dissolve
    
    "With a cold shudder, you decide to head back - until you hear a slurping noise behind you."
    "Whirling around, you watch in horrible fascination as giant earthworms crawl out of the mud. Gross!"

    "No way you're heading back there. You clench your teeth and slog onward."
    "Up ahead, you see a dim green light. Great! An exit."

    "As you reach the end of the tunnel, you hear a low growl behind you."
    "At first you try to pretend it's your imagination. But there's no mistaking the sound of thudding footsteps."
    "Getting closer. And closer."

    show you scared with dissolve

    "And now it's breathing down your neck!"
    "You're too scared to turn around. And too scared not to."
    
    show you scared at midleft 
    with dissolve
    show darkmonster at right
    with dissolve

    "Risking a glance over your shoulder, you see a large, dark shape behind you. It's a big man."
    "No. You squint hard. It's dark and hairy with muddy leaves and green vines trailing from its body."
    "It's some sort of swampy monster!"

    "You run as fast as you can. Your chest is on fire."
    "The swamp monster is gaining on you."
    
    "You know you should keep running, but your heart feels as if it's about to explode. You have to stop."
    "You turn and stare right into the swamp monster's bloody eyes."

    show you nervous with dissolve

    y "Neat costume."

    show you scared at screen_shake
    with dissolve

    hide darkmonster
    show monstershaded at right
    with dissolve

    "Good try - but the swampy monster isn't wearing a costume. He's real and this, unfortunately, is really..."

    scene bg gameover with pixellate

    window hide

    pause (2)

    $ gameover_choices = [
        ("Back to Previous Choice", Jump("doorchoice")),
        ("Start Over", Jump("start")),
        ("Main Menu", MainMenu())
    ]

    call screen game_over_menu (gameover_choices)

label bluedoor:

    show bg twodoors with fade

    "You open the blue door and peer through."

    show bg bluetunnel with fade

    "You're staring down a long dark passageway."
    "At least you think it's long. It's difficult to tell."

    "It's pitch-black. You don't know what to do."
    "Maybe I should have picked the other door. I'm getting out of here."

    show bg bluetunnel at screen_shake

    "But the blue door has locked behind you!"
    "Now you're sure you made the wrong choice. But there's nowehere to go but forward."

    "Your knees begin to tremble as you inch your way down the dark hallway."

    show bg mountainenter with fade

    "The passage ends in a bright burst of light. And in front of you, a tall purple mountain rises hundreds of feet into the air."

    "You breathe out a long sigh of relief. You're out of the dark!"
    "You study the mountain. It looks so real!"
    "But cut into its side, you spot a doorway. Above it a brightly painted sign reads:"
    "DOOM SLIDE. WILL YOU BE THE ONE TO SLIDE FOREVER?"

    show bg doomramp with fade

    "You open the door and climb a steep ramp that curves around and around."
    "It's cold and dark inside."

    "Halfway up the ramp, you stop. There's another sign:"
    "WARNING! - YOU MAY BE THE ONE TO SLIDE TO YOUR DOOM!"
    "You continue up the ramp."

    show bg doomslides with fade

    "You finally make it to the top, and find yourself standing on a wide, dimly lit platform."
    "A row of long, curving slides stretches out before you. The slides are numbered from one to seven."

    "You think hard. The Doom Slide. You know you've heard about it before. But where? Where was it?"
    "And then you remember! It was in a GOOSEBUMPS book you read! {i}One Day at HorrorLand.{/i}"

    "Now you know you're in big trouble. Because you remember all about the Doom Slide from the book."

    jump doomslidechoice

label doomslidechoice:

    show bg doomslides with fade

    "You remember that if you pick the wrong slide, you'll spend the rest of your life sliding and sliding - forever!"
    "Which number is the Doom Slide? Which One?"

    menu:

        "There are 7 slides in front of you. Which one isn't the Doom Slide?"

        "1":
            jump doomslide
        "2":
            jump doomlaugh
        "3":
            jump doomdark
        "4":
            jump doomslide
        "5":
            jump doomlaugh
        "6":
            jump doomdark
        "7":
            jump doomslide

label doomslide:

    show bg doomslide with fade

    "You slowly lower yourself onto the slide."

    show bg doomspeed at shakeloop with dissolve

    "You start to stretch out your legs when the bottom tilts underneath you and throws you forward."
    "You're sliding! Fast!"

    "The surface must be made of some kind of special material because you're zooming down at top speed."
    
    show bg doomdark with dissolve
    
    "You hold your breath as you fly through the blackness."

    "A bump sends you bouncing into the air. You scream. And scream."
    "When is it going to end?"
    
    show you scared with dissolve
    
    y "On no! Could this be the Doom Slide?"

    show bg doomend2 with dissolve

    "You hear screams echo in the darkness. You twist around. But you don't see anyone."
    "The ghostly screams grow louder - in front of you, next to you, behind you."

    "Screaming and sliding. And sliding. Never stopping."

    scene bg doomend with dissolve

    "You gasp for breath. And then you hear it."

    "A voice cuts through the blackness. Through the screams. A voice that cries,"
    mys "Welcome to the rest of your life. Welcome to the Doom Slide!"

    pause (1)

    scene bg gameover with pixellate

    window hide

    pause (2)

    $ gameover_choices = [
        ("Back to Previous Choice", Jump("doomslidechoice")),
        ("Start Over", Jump("start")),
        ("Main Menu", MainMenu())
    ]

    call screen game_over_menu (gameover_choices)

label doomlaugh:

    "Haha"

    return

label doomdark:

    show bg doomslide with fade

    "You grab the sides of the slide and lower yourself down."

    show bg doomspeed at shakeloop with dissolve

    "The second you stir, the slide's floor tilts up beneath you and propels you forward."

    show you scared at shakeloop, center with dissolve

    "You shriek."

    hide you with dissolve

    "You raise your arms and scream louder. You slide faster and faster."
    
    show bg doomdark with dissolve
    
    "In total darkness. Darkness so black, you can't even see your own feet in front of you."
    
    show bg doomend with dissolve

    "Your eyes dart frantically from side to side."

    show bg doomfaces with dissolve

    "Faces suddenly appear in the darkness in bright flashes of light. Faces of hideous monsters with deformed heads and oozing flesh."
    "But you're moving too fast to focus on them."

    show bg doomend with dissolve

    "You slide and slide - until the faces stop flashing and you're covered in the thick, heavy blackness again."
    "You scream as you round a sharp curve. Your head is spinning. You pick up speed."

    "When will it end?"
    "Then you hear the screams. Chilling screams that echo through the darkness."
    
    show you scared with dissolve
    
    "Oh no! You must have picked the Doom Slide!"

    scene black

    "Bump."

    show bg reunited with fade

    "A chute opens up. You land headfirst on soft grass."

    show bg chuteblink with dissolve

    "You blink several times. A long sigh escapes from your lips. It wasn't the Doom Slide after all."
    "As you climb to your feet, you hear someone call your name. You glance up and shout for joy."

    show bg reunited with dissolve

    show brad normal with dissolve
    show patty smile with dissolve
    
    "It's Brad! And Patty's there, too!"

    "You tell them about your scary ride on the slide - about how you thought you'd slide forever."

    show patty idea with dissolve

    p "Cool! Let's all ride it this time."

    show you shout with dissolve

    y "No!"
    y "This carnival is too weird. And dangerous. Something's not right."
    y "We have to get out of here. Now!"

    show brad smug with dissolve

    b "Yeah. The faster, the better."

    jump pattychoice

label pattychoice:

    show bg reunited with dissolve

    p "I have an idea."
    p "I spotted a back way out of here. But it's a little risky. We have to squeeze through a barbed-wire fence ..."
    p "... and it's guarded by the carnival's security forces. But we should try!"

    scene bg reunited with dissolve

    menu:

        "Are you going to listen to Patty?"

        "Follow Patty":
            jump followpatty

        "Choose not to take the back way out":
            jump rejectpatty

label rejectpatty:

    show bg

    y ""

    return

label followpatty:

    "Bruh"

    return