# The script of the game goes in this file.

#   # Z = Not in original book
#   # X = Redundant / Removed from original book
#   Ctrl K + Ctrl 0 (Close all drop down lists)

############################################ init block ############################################

# Transformations : Sprite Position

transform closeleft:
    xalign 0.38
    yalign 1.0

transform closeright:
    align 0.62
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

# Brad

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

# Other Effects

image bg entranceflicker:
    "bg entrance.png"
    pause (0.2)
    "bg darkentrance.png"
    pause (0.2)
    repeat
    
# Variables are used to make it less tedious to recall who is saying which line.
# Make sure character name colors are spelled "color" and not "colour"

define y = Character ("You", who_color = "#584747")
define p = Character ("Patty", who_color = "#59862e")
define b = Character ("Brad", who_color = "#503d19")

define mys = Character ("???")
define BA = Character ("Big Al", who_color = "#ffffff")

####################################################################################################

# Game starts here

label start:

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

    "You're staring at a sign that reads: WORLD's FREAKIEST FREAK SHOW!"
    "The three of you gape at the pictures."
    "There's the Three-Headed Man with the ugliest collection of faces you've ever seen."
    "And the Snake Lady - a young blond girl with a beautiful face and the body of a slithering snake."

    y "This is, uh - uh -"
    
    "A large hand comes down on your shoulder. Hard."
    "You slowly turn and gaze up at a huge man with shoulders wider than a refrigerator. He has coal - black eyes and a thick mustache to match."
    "He looks strong enough - and mean enough - to pitch you over the fence with one hand."

    mys "What are you doing?"
    mys "You're not allowed in here."

    "He points directly at you."

    y "We're sorry."
    y "We wanted to look around. That's all. But we'll leave. Right now."

    "His eyes stare into yours. He clamps both hands down on your shoulders."

    mys "You're not going anywhere!"

    b "Wh-what do you mean?"

    mys "I just had an idea. A great idea."
    mys "I just want you kids to stay and try out the rides before the grand opening tomorrow."

    p "Cool!"

    y "Are you sure it's all right with the owner?"

    mys "I'm Big Al, the manager. And what I say around here goes."

    "Big Al digs around in his checkered jacket and pulls out three maps. He hands one to each of you."

    BA "Study them carefully. If you have any questions, ask them now."

    "Your eyes fall upon the map. You have a question. But when you gaze up," 

    # hide BA with dissolve

    "Big Al is gone. He's vanished!"

    p "A whole carnival to ourselves!"
    p "Where should we start?"

    "You stare down at your map once again. You notice that the carnival is split in half."
    "On one side are the rides. Tons of them. On the other side is the midway, packed with games of chance and the Freak Show."
  
    menu:
  
        "What will you try first?"

        "Go on the rides.":
            jump startrides

        "Check out the midway.":
            jump startmidway

label startrides:

    return

label startmidway:

    return




