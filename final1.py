import time

def intro():
    print('''WARNING: THE FOLLOWING CONTAINS SENSITIVE THEMES SUCH AS DEPRESSION, SUICIDE, AND OTHER MENTAL
HEALTH ISSUES.''')
    time.sleep(5)
    print('''\nI wanted to talk about it. Damn it. I wanted to yell. I wanted to shout about it. But all I could
whisper was "I am fine." \n''')
    time.sleep(6)
    print('INSTRUCTIONS:')
    print('''\nThis is a text adventure game that will use your input to explore the world.
Understand that not every phrase may work. Try to keep your answers all lower case. Simple words
such as "right", "left", "enter", or object names such as "table" will help you navigate. To
leave a room, type "leave" or "leave room".''')
    print('')
    time.sleep(17)

def first():
    print('''\nLife is stressful, espicially as a junior in highschool. The only "friend" you had was Adelaide, who is
almost like your beacon of light. You knew each other since the beginning of middle school and always talked.
It was a normal day, really, other than the fact that Adelaide stopped talking to you.\n''')
    time.sleep(15)
    print('''Adelaide offered no excuse, other than the fact that she couldn't deal with you. That you're too
sad and that you two just don't connect anymore. Instead, Adelaide decides to find some other friends to hang
out with.\n''')
    time.sleep(14)
    print('''Adelaide's words stung. Didn't she know how bad you felt? The sleepless nights, the stress from family,
the constant self doubt you felt. In anger and immense sadness, you ran into the forest behind your school.\n''')
    time.sleep(9)
    print('''Entering the woods, strange noises lead you to a dilapidated mansion, surrounded by a rusty
steel fence and decaying leaves. It seems as though no one has been here for a long time, which made it the
perfect place to cry without anybody hearing you. The gate is open, so should you go in?''')
    time.sleep(14)
    while True:
        answer = input('''\nShould you enter the house? ''')
        if answer == 'go in' or answer == "enter" or answer == 'gate' or answer == "go inside" or answer == "go" or answer == "yes":
            print("You go inside, but barely jump as the gate closes behind you. Why should you care?")
            time.sleep(2)
            key()
            break
        elif answer == "leave" or answer == "run away" or answer == "exit" or answer == "no":
            print('''Some part of you just didn't care anymore, so you left and went home, feeling incredibly alone.''')
            break
        elif answer == "search the leaves" or answer == "rummage through leaves" or answer == "leaves" or answer == "search leaves":
            print('''You spend some time looking through the leaves. However, you find nothing.''')
            continue
        elif answer == "leave game" or answer == "exit game":
            break
        else:
            print('''That's not a choice.''')
            continue
def key():
    key = 0
    candle = 0
    match = 0
    knife = 0
    basekey = 0
    blood = 0
    print('''\nYou notice that the DOOR to the house is slightly ajar, and a MAILBOX is mounted
on the wall next to the door. As far as you can tell, there are no windows or other entrances.\n''')
    while True:
        answer = input("What should you do? ")
        if answer == "go through the front door" or answer == "front door" or answer == "enter through door" or answer == "door" or answer == "enter" or answer == "house":
                print('''You walk up the stairs and through the front door. As soon as you walk in, the front door
closes behind you. You try to open it but it's locked. Dim lights flicker on, and you notice that you are standing in a foyer.\n''')
                front_door(key, candle, match, knife, basekey, blood)
                break
        elif answer == "mailbox" or answer == "search mailbox" or answer == "look through mailbox" or answer == "mail":
                print('''You walk up the steps, and peer into the mailbox. Inside, you see a piece of paper. It reads: \n''')
                time.sleep(2)
                print('''We're one in the same, you can never get rid of me, and I can't exist without you. \n''')
                time.sleep(1)
                print('''You put the letter back.\n''')
                continue
        elif answer == "exit game" or answer == "leave game":
            break
        elif answer == "go out" or answer == "leave":
            print('''You can't go back.\n''')
        else:
            print('''That is not an answer.\n''')
            continue

def front_door(key, candle, match, knife, basekey, blood):
    print('''A grand staircase looms in front of where you are standing in the foyer. A hallway leads both to the
LEFT and RIGHT.\n''')
    while True:
        answer = input("What should you do? ")
        if answer == "look around foyer" or answer == "foyer" or answer == "search foyer" or answer == "look around":
            print("The foyer is mostly empty, save for a few leaves that somehow got inside.")
            continue
        elif answer == "go left" or answer == "left":
            dining(key, candle, match, knife, basekey, blood)
            break
        elif answer == "go right" or answer == "right":
            library(key, candle, match, knife, basekey, blood)
            break
        elif answer == "go up" or answer == "stairs" or answer == "go up stairs" or answer == "staircase" or answer == "upstairs" or answer == "up":
            upstairs(key, candle, match, knife, basekey, blood)
            break
        elif answer == "exit game" or answer == "leave game":
            break
        else:
            print('''That is not an answer.\n''')
            continue

def upstairs(key, candle, match, knife, basekey, blood):
    print('''You are at the top of the STAIRCASE. You notice two hallways to the LEFT and RIGHT of you.\n''')
    while True:
        answer = input("What should you do? ")
        if answer == "go left" or answer == "left":
            left_upstairs_hallway(key, candle, match, knife, basekey, blood)
            break
        elif answer == "right" or answer == "go right":
            right_upstairs_hallway(key, candle, match, knife, basekey, blood)
            break
        elif answer == "down" or answer == "go down" or answer == "downstairs" or answer == "go downstairs" or answer == "staircase":
            front_door(key, candle, match, knife, basekey, blood)
            break
        elif answer == "exit game" or answer == "leave game":
            break
        else:
            print('''That is not an answer.\n''')
            continue

def right_upstairs_hallway(key, candle, match, knife, basekey, blood):
    print('''You notice two rooms, an OFFICE and a BEDROOM. To the LEFT is the staircase.\n''')
    while True:
        answer = input("What should you do? ")
        if answer == "office" or answer == "go to the office":
            office(key, candle, match, knife, basekey, blood)
            break
        elif answer == "bedroom" or answer == "go to the bedroom":
            bedroom_right(key, candle, match, knife, basekey, blood)
            break
        elif answer == "left" or answer == "go left" or answer == "staircase" or answer == "stairs":
            upstairs(key, candle, match, knife, basekey, blood)
            break
        elif answer == "exit game" or "leave game":
            break
        else:
            print('''That is not an answer.\n''')
            continue

def left_upstairs_hallway(key, candle, match, knife, basekey, blood):
    print('''In front of you seems to be the door to a BEDROOM. To the RIGHT is the staircase.''')
    while True:
        answer = input('''\nWhat should you do? ''')
        if answer == "bedroom" or answer == "go to the bedroom" or answer == "front":
            bedroom_left(key, candle, match, knife, basekey, blood)
            break
        elif answer == "right" or answer == "go right" or answer == "staircase" or answer == "stairs":
            upstairs(key, candle, match, knife, basekey, blood)
            break
        else:
            print("That is not an answer.")
            continue

def bedroom_left(key, candle, match, knife, basekey, blood):
    letters = ["You can't do this anymore. Do you really think that ignoring me will help solve all your problems? It won't. That sense of dread filling you, the feeling of helplessness, of being unwanted in this world. That's me. And you'll never get rid of me."]
    letters1 = ["Getting help isn't going to fix this, it's not going to fix you. They've never seen something like you, they're normal, they don't feel like you - if you even feel at all. You don't deserve they're pity, if anything they should get rid of you. Ignore you, and leave you to rot. It's what you deserve."]
    print('''You find yourself in a bedroom. A stained MATTRESS is tossed to one side, blankets in a pile in the middle of the bed.
On the other side of the small room is a pile of PAPER on a desk.''')
    while True:
        answer = input('''\nWhat should you do? ''')
        if answer == "leave" or answer == "go outside" or answer == 'exit room' or answer == "leave room":
            left_upstairs_hallway(key, candle, match, knife, basekey, blood)
            break
        elif answer == "blankets" or answer == "look through blankets" or answer == "bed" or answer == "mattress":
            print('''You look through the bed, finding nothing but dust and bugs. You also see some blood and sharp GLASS.''')
            continue
        elif answer == "examine blood" or answer == "glass" or answer == "blood" or answer == "sharp glass":
            print('''You examine the blood covered glass, and find the blood to still be wet. Looking around, you don't
notice any other blood stains other than those on your arms.''')
            continue
        elif answer == "paper" or answer == 'desk' or answer == "pile of paper" or answer == "papers":
            print("You walk over to the desk, and pick up the pile of paper.")
            for num in range(len(letters)):
                answer = input('''\nDo you wish to read one? ''')
                if answer == "yes":
                    print(letters[num])
                    continue
                else:
                    break
            for num in range(len(letters1)):
                answer = input('''\nDo you wish to read one? ''')
                if answer == "yes" or answer == "yse":
                    print(letters1[num])
                    continue
                else:
                    break
            print("\nYou finished reading.")
        else:
            print("That's not an answer.")
            continue

def bedroom_right(key, candle, match, knife, basekey, blood):
    print('''You imagine this room used to be a bedroom, but there's nothing but a SLEEPING BAG to show it.
A pile of CLOTHES lie on the side.''')
    while True:
        answer = input('''\nWhat should you do? ''')
        if answer == "sleeping bag" or answer == "search sleeping bag":
            print("You go over to the sleeping bag, and check it thorougly. Other than dust and some stains, there is nothing special about it.")
            continue
        elif answer == "go back" or answer == "leave room" or answer == "go to hallway" or answer == "back" or answer == "leave":
            right_upstairs_hallway(key, candle, match, knife, basekey, blood)
            break
        elif answer == "pile of clothes" or answer == "clothes" or answer == "search clothes":
            if knife == 1:
                print("You've already checked the pile of clothes.")
                continue
            elif knife == 0:
                print("You go over to the pile of clothes. You pause right before it, then kick it down. The clothes scatter before you.")
                answer = input('''\nShould you keep checking? ''')
                if answer == "yes" or answer == "keep checking" or answer == "check":
                    print("You rummage through the mess of clothes, but still only find more and more dirty clothes.")
                    answer = input('''\nShould you keep checking? ''')
                    if answer == "yes" or answer == "keep checking" or answer == "check":
                        print("You decide to carefully check each article of clothing, taking time to make sure there truly is nothing. After an hour, you finally find a knife.")
                        answer = input('''\nShould you take it? ''')
                        if answer == "yes" or answer == "take it" or answer == "take knife":
                            print("You take the knife, sticking it into your belt. Feeling bad for the mess you made, you remake the pile of clothes.")
                            knife = 1
                            continue
                        elif answer == "no" or answer == "leave it" or answer == "leave knife":
                            print("You leave the knife, thinking it may be better not to carry a weapon around. Instead you remake the pile of clothes and leave it there.")
                            continue
                    elif answer == "no" or answer == "stop checking" or answer == "stop":
                        print('''You decide there is no use in checking. All you've seen so far is clothes and more clothes. Besides, you've already made such a big mess.
You decide to limit the mess in the room by remaking the pile of clothes.''')
                        continue
                elif answer == "no" or answer == "stop" or answer == "don't check":
                    print("Seeing nothing, you decide to put the clothes back into a pile and leave it.")
                    continue
        else:
            print("That's not an answer.")
            continue


def office(key, candle, match, knife, basekey, blood):
    print('''You are in an office. Inside you find a turned over TABLE, a broken LAMP, and PAPERS strewn about.
In the middle of this mess is a lone CHAIR.''')
    while True:
        answer = input('''\nWhat will you do? ''')
        if answer == 'sit' or answer == 'sit in chair' or answer == 'chair' or answer == "lone chair":
            print('''You ignore the mess around you and instead of doing anything, you decide the best
course of action, is no action at all. Laying back in the chair like the lazy lump you are, you look
up and find a hatch.''')
            answer = input('''\nGo up into the attic? ''')
            if answer == 'yes' or answer == "go up" or answer == "up":
                attic(key, candle, match, knife, basekey, blood)
                break
        elif answer == 'papers' or answer == 'paper':
            print('''\nYou search through the papers scattered mindlessly around on the floor. Most of the papers are about taxes,
reciepts, and unintelligible, chicken-scratch writing. You notice that the writing appears repeatedly, and slowly you string
together that it was a diary of some sort.''')
            time.sleep(2)
            answer = input('''\nDo you wish to read it? ''')
            if answer == 'yes':
                print('''The patient seems to be suffering from severe anxiety some form of depression. It seems to be caused by
outside factors such as bullying, and lack of friends. It can also be based upon genetics as well, the medication I recommended
has no effect and seems to cause more harm to the patient. Therapy seems to be the best option.''')
                continue
            elif answer == 'no':
                print('''You decide not to read the paper.''')
                continue
        elif answer == 'table':
            print("There is nothing by the table")
            continue
        elif answer == "lamp":
            print("The lamp is useless.")
            continue
        elif answer == "leave" or answer == "exit" or answer == "leave room" or answer == "exit room":
            right_upstairs_hallway(key, candle, match, knife, basekey, blood)
            break
        else:
            print("That is not an answer.")
            continue

def attic(key, candle, match, knife, basekey, blood):
    print('''\nYou have accessed the attic. Opening the door, you see light pouring through from a WINDOW, as well
as empty CARDBOARD BOXES piled up and scattered around. Near the far end of the wall, you see a splintered, ancient
WARDROBE. On your right there are sheet covered canvases and FURNITURE. You start to hear loud banging coming from
the wardrobe. ''')
    while True:
        answer = input('''\nWhat will you do? ''')
        if answer == 'search cardboard box' or answer == "cardboard boxes" or answer == 'search boxes' or answer == 'cardboard box' or answer == 'boxes' or answer == "box":
            print('''\nYou search the boxes, but unfornately you don't find anything useful in them. All you find is a journal entry.
It reads: ''')
            time.sleep(3)
            print('''\nEverything is crumbling. The world, the pictures, the art. It's disappearing ever so slowly, so subtly
that I haven't even noticed until now. I feel like cobwebs are slowly taking over my view, my sight fuzzy now that I can't see
anything at all. It's fading, the colors, the lights, the sounds. I feel so distant from everything, so far away and yet so close
that it's frustrating to know that whatever I do is absolutely useless. I hope, I pray, but words are foreign to me and I forgot
how to speak and letters are just a jumble of symbols and I can't form anything because my mouth won't move. I'm stuck, stuck
and unable to move, to call for help and all I can do is watch as "I" move and as "I" talk and yell and scream at stuff and I
don't know what happiness is anymore.''')
            time.sleep(4)
            continue
        elif answer == "go down" or answer == "down" or answer == "leave" or answer == "go back" or answer == "downstairs" or answer == 'back':
            office(key, candle, match, knife, basekey, blood)
            break
        elif answer == 'search the window' or answer == 'window' or answer == 'light' or answer == 'search window':
            print('''You look at the window, it is covered with dust and cobwebs. Near the center of the window the glass is cracked
almost as if a heavy object smashed against it. It seems recent, too, since there's no dust near it, making an oval shape.\n''')
            continue
        elif answer == 'search furniture' or answer == 'search canvases' or answer == 'furniture' or answer == 'canvases' or answer == 'sheet covered canvases' or answer == 'sheet covered furniture':
            print('''You walk over to the right side of the room, looking at the dust covered sheets protecting hidden furniture
and paintings.''')
            answer = input('''\nDo you wish to search the sheets? ''')
            if answer == 'yes':
                print("You found an old key. It looks like it can fit into the wardrobe.")
                key = 1
                continue
            else:
                print("You leave it alone.")
                continue
        elif answer == 'search wardrobe' or answer == 'wardrobe':
            print('''\nYou are in front of the wardrobe. You pull onto the handles, but they won't budge.''')
            answer = input('''\nWoud you like to open it? ''')
            if answer == 'yes' or answer == "open" or answer == "open it":
                if key == 0:
                    print('''You are unable to open the door. There should be a key around here somewhere...\n''')
                    continue
                elif key == 1:
                    if basekey == 1:
                        print('''\nYou open the door.''')
                        final_stage(key, candle, match, knife, basekey, blood)
                        break
                    else:
                        print('''\nThere is still more to explore.''')
            elif answer == "no":
                print("You leave it alone.")
                continue
        else:
            print("That's not an answer.")
            continue

def dining(key, candle, match, knife, basekey, blood):
    print('''You are in a dining area. It is dim, but you can still see. As you tread into the dining room,
you hear glass under your feet. You notice a damaged TABLE, with shattered glass and broken plates littered
around it. On the side you see an ARMOIRE and CABINETS.''')
    while True:
        answer = input('''\nWhat should you do? ''')
        if answer == "cabinet" or answer == "open cabinet" or answer == "search cabinet" or answer == "cabinets":
            if candle == 0:
                print('''You go over to the cabinet, and inside you find lots of junk and other trash. As you continue to search, you find a candle.''')
                answer = input('''\nDo you wish to take it? ''')
                if answer == "yes":
                    print("You take the candle.")
                    candle = 1
                elif answer == "no":
                    print("You leave the candle.")
                else:
                    print("That's not an answer.")
                    continue
            elif candle == 1:
                print("You already have the candle.")
        elif answer == "armoire" or answer == "check armoire":
            if match == 0:
                print("You look inside the armoire. In it you find broken china. You also happen to find a misplaced match.")
                answer = input('''\nDo you wish to take the match? ''')
                if answer == "yes":
                    match = 1
                    print("You take the match.")
                elif answer == "no":
                    print("You leave the match.")
                else:
                    print("That's not an answer.")
            elif match == 1:
                print("You find nothing else in the armoire.")
        elif answer == "table" or answer == "check table":
            print("You find nothing but broken plates and glasses on and around the table.")
        elif answer == "leave room" or answer == "exit" or answer == "go back" or answer == "back" or answer == "leave" or answer == "right":
            front_door(key, candle, match, knife, basekey, blood)
            break
        else:
            print("That's not an answer.")
            continue

def library(key, candle, match, knife, basekey, blood):
    print('''You are in a library. BOOKS are stacked everyone in shelves that surround the room. In the corner you
see a staircase down to a DARK ROOM.''')
    while True:
        answer = input('''\nWhat should you do? ''')
        if answer == "exit" or answer == "leave room" or answer == "back" or answer == "go back" or answer == "left" or answer == "exit room" or answer == "left" or answer == "leave":
            front_door(key, candle, match, knife, basekey, blood)
            break
        elif answer == "dark room" or answer == "go down" or answer == "down" or answer == "staircase" or answer == "stairs" or answer == "basement":
            if candle == 1 and match == 1:
                print("You go down the stairs.")
                time.sleep(1)
                basement(key, candle, match, knife, basekey, blood)
                break
            else:
                print("It's too dark to go down there. Find a light source first.")
                continue
        elif answer == "books" or answer == "shelves":
            print("There is nothing special about the books.")
            continue
        else:
            print("That's not an answer.")
            continue

def basement(key, candle, match, knife, basekey, blood):
    print('''\nYou find yourself in a dark room that seems to be the basement. You feel grateful for finding the candle and
match, and decide to use it. After lighting it up, you can see some CABINETS and SHELVES holding various objects and tools.
On the other side of the room is a TABLE. Covering the table is some sort of stained white sheet.''')
    while True:
        answer = input('''\nWhat should you do? ''')
        if answer == "go back" or answer == "up" or answer == "upstairs" or answer == "library" or answer == "leave room" or answer == "exit" or answer == "back" or answer == "leave":
            library(key, candle, match, knife, basekey, blood)
            break
        elif answer == "table" or answer == "check table" or answer == 'white sheet':
            if basekey == 0:
                print('''\nYou go over to the table and take off the sheet. Under it lays a pale, dead woman who slightly resembles you.
You stand in shock for a few seconds and take a step back. You notice that her hand clutches a shiny object.''')
                answer = input('''\nShould you search the body? ''')
                if answer == "yes" or answer == "search":
                    print('''\nYou move closer to the hand and realize it must be some sort of key or metal object. You try to take
it out, but the second you touch the body it jerks up. She stares at you intensely, anger coursing off her body as she stands up and
steps towards you.''')
                    time.sleep(10)
                    print('''\n(Lady): This is your fault... this is all your fault!  If only you hadn't existed, if only you hadn't taken away
everything that I had.''')
                    time.sleep(6)
                    print('''\nShe takes a ragged breath, and takes another step towards you. And another. And another. Until she has her hands
around your throat and beings squeezing. Her voice was raspy as she opened her mouth to speak again.''')
                    time.sleep(10)
                    print('''\n(Lady): You deserve this... you are all alone in the crimes you've committed. You derseve no happiness, no
joy, no forgiveness. You shall recieve nothing but pain, nothing but darkness. I mean, why do are you still even trying? Just leave. Leave.
No one would ever care. No one cares about you anyways.''')
                    time.sleep(15)
                    print('''\nYour vision was hazy, and you couldn't focus. You should try to get out, you should fight back... but why should
you? ''')
                    time.sleep(4)
                    answer = input("\nType 'f' to fight back: ")
                    if answer == 'f':
                        time.sleep(1)
                        print("\nSome part of you struggles, but nothing happens. Your body doesn't respond. The world grows dimmer...")
                        time.sleep(1)
                    else:
                        print("\nThat's right... it doesn't matter. It never does, and never well. No one will miss you.")
                        time.sleep(1)
                    answer = input("\nPerhaps it's not your time yet though. There has to be something to fight for... (type 'f' to struggle): ")
                    if answer == "f":
                        time.sleep(1)
                        print('''\nYou try, you really do. But nothing. No movement, no muscle even flinches. And why should it? There is
nothing. That's all you can tell yourself. There is nothing, nobody, that can ever change this. Your life is devoid of light, it's
meaningless. There is nothing. Your body, your soul, your mere existence is empty. ''')
                        time.sleep(15)
                    else:
                        print('''\nBut there is nothing. That's all you can tell yourself. There is nothing, nobody, that can ever change this.
your life is devoid of light, it's meaningless. There is nothing. Your body, your soul, your mere existence is empty. ''')
                        time.sleep(5)
                    print('''\nYour vision fades to darkness...\n''')

                    time.sleep(4)

                    print('''\nYou wake up on the ground. You feel that your throat is slightly swollen, and has a bruised feeling to it.
You hold a key in your hand. It seems it may work on the cabinet behind you.''')
                    basekey = 1
                else:
                  print("\nYou decide not to. Why should you? It's not like it really matters.")
                  continue
            elif basekey == 1:
                print("You have already found the key.")
                continue
        elif answer == "shelves" or answer == "check shelves":
            print('''You make your way to the shelves, and find it scattered with tools. A blanket of dust covers the objects. Out of the
corner of your eye you see a letter''')
            answer = input("\nShould you read it? ")
            if answer == "yes" or answer == "take it" or answer == "read" or answer == "read it":
                print("You pick it up and become suprised when you see how similar the handwriting is to your own.")
                time.sleep(3)
                print('''\nIt reads: \n''')
                print('''They're happy without me. I know they are. For I sit in my room, and I stay alone and all I hear
is laughter and happiness and just pure joy. I bring them nothing but pain and sadness and frustration and hatred. And so
I ask myself, what is keeping me from leaving? What is keeping me from killing myself and letting myself leave this wretched
place and let them get happiness since I can't stand the pain I bring to them. Why don't they just let me go. Why can't they
understand that I hate them all, that I just can't stand them, but yet I care about them. I am a monster.''')
                time.sleep(30)
                print('''\nSomehow you relate to whoever wrote the letter.\n''')
                time.sleep(3)
                answer = input("Would you like to read another one? ")
                if answer == "read" or answer == "yes":
                    print('''\nThis one reads: \n''')
                    print('''My eys burn with tears, and yet my face is dry, safe, from the horrors I feel inside. I feel
trapped, and I don't understand why exactly I feel such sadness inside of me. I force my laughs, make my eyes look bright
and my muscles relax and just try to live like everyone else wants me to do. Why is it so hard to not cry? Even as I write
this, tears are streaming down my face and my heart breaks and I can't feel anything but sadness and despair and pain and
what is going on with me? I am depressed, is what I want to say. Maybe there is something wrong with me, because my day
dreams are filled with self murder and running and blood and screams of agony and torture and there is no light in my life
anymore. Why is my heart just a crumpled ball of stress why can't I be liked why can't I have friends why can't I just be nice
why can't I just be normal why can't I just live and be happy and why do I have to feel so sad and angry. Perhaps this is a
punishment for something I have done, and for whatever terrible reason I just don't want to fight anymore. ''')
                    time.sleep(50)
                    continue
                else:
                    print("You leave it.")
                    continue
            else:
                print("You leave it.")
                continue
        elif answer == "cabinets" or answer == "cabinet" or answer == "check cabinets":
            if basekey == 0:
                print("You go to the cabinets, but struggle to open it. Perhaps a key may help.")
                continue
            elif key == 1:
                print('''You can't open the cabinet since it's locked. The key you have at the moment doesn't fit. There should be one
nearby...''')
                continue
            elif basekey == 1:
                if blood == 0:
                    print("You use the key you got earlier and it fits the lock perfectly. You unlock the door.")
                    answer = input('''\nWould you like to open it? ''')
                    if answer == "yes" or answer == "open":
                        print('''You open the cabinet and stifle a scream. A dead man lays inside, his face and body so bloody and mutilated you can't tell
who this is. However, you can't shake the feeling you know who this person is.''')
                        answer = input('''\nShould you search the body? ''')
                        if answer == "yes" or answer == "search":
                            print('''You steady your breath as you quickly pat the body down. In his pocket you find a wallet. Inside it is
filled with pictures of family and friends that seems familiar. Unfortunately, your vision goes blurry as you try to focus on the family.
You decide to take the wallet with you, since you never know what it could be used for.''')
                            blood = 1
                            continue
                        elif answer == "no" or answer == "don't search":
                            print('''Disgusted, you close the cabinet up again.''')
                            continue
                    else:
                        print("Something told you not to open the door. You decide to leave it closed.")
                        continue
                else:
                    print('''\nYou already searched the body.''')
        else:
            print("That's not an answer.")
            continue

def final_stage(key, candle, match, knife, basekey, blood):
  print('''\nYou open up the door slowly and look inside. Despite the dark, empty interior, you can feel an intimidating force surrounding you.
You step inside, and the doors close behind you. A light flickers on, and you find yourself in a room. It was overwhelming, almost to the
point of suffocation. It begins to take shape into a humanoid figure.... into Adelaide. But her smile is inhumane, stretching past her
checks. You stumble backwards, tripping and moving the boxes around you. \n''')
  time.sleep(23)
  print('''Why is she here? She left you behind, she said that she didn't want to be around you anymore! \n ''')
  time.sleep(5)
  print('''Adelaide creeps closer, pushing you into corner. She grabs you by your arm, and you know by her grip it's bruising.
She brings you to her face, her warm breath smelling rancid.''')
  time.sleep(7)
  print('''\n(Adelaide): Do you really think you could actually get rid of me? You're NOTHING! Everybody leaves you in the end, just like I did.
I just can't believe that you thought I was your friend. A loser like you cannot even begin to understand how worthless your existence
is. You shouldn't even be here. In fact, would anyone really care if you disappered? Why don't you just come away with me, never feel again,
no pain, nothing. Just stay here in this house... with me. It's not like anyone will miss you. \n''')
  time.sleep(15)
  answer = input("Do you want to go with her? ")
  if answer == 'yes' or answer == 'go with her':
      print('''\nShe's right. There's no point in you even trying to deny it. There is no point in you even trying. It's not like you care about
anything anyways.''')
      stay(knife)
  else:
    if blood == 1:
      print('''\nSome part of you feels that you try to leave... but why should you? Suddenly remembering the pictures you found,
you decide to take them out and look at them. And you saw... yourself. Smiling. Laughing. With so many other people, who all are laughing
with you. And you decide that maybe you can try. For these people. And for yourself. For your younger self. You'll try for her. \n''')
      time.sleep(14)
      print('''You wake up the next morning, feeling somehow... fresh. Slightly more awake and alive. With a small smile, you get ready for
the day. ''')
    else:
      print('''\nSome small part of you feels that you should at least try to leave... but why should you? Adelaide is right. There's no point
in you trying to do anything.''')
      stay(knife)


def stay(knife):
  time.sleep(8)
  print('''\nYou decide to stay, since, honestly, who would really care about your disappearance? She begins to close in on you, opening up
her arms in what seems to be a hug. \n''')
  time.sleep(8)
  answer = input('''Will you accept her hug? ''')
  if answer == 'yes' or answer == 'accept' or answer == 'hug':
    print('''\nYou wrap your arms around her, accepting her hug. You've come to realize it doesn't matter what you feel, how others feel,
it's better to just not feel at all. It's not like you really care anyways. You lose your sense of happiness forever.''')
    time.sleep(4)
  else:
    print('''\nYou step back, and walk away from her. This... monster dares to try to hug you? To mock you like this? She shouldn't have
played with your emotions, shouldn't have walked all over you like that. But perhaps what she said was right. No one cares, not even her. So
why should you? ''')
    if knife == 1:
      time.sleep(9)
      print('''\nYou take out the knife you found, turning it over in your hand. Without hesitation, without any thought or control, you
plunge it downards, right into your heart. Warm blood poured out, but you felt relief. You close your eyes and collapse.''')
      time.sleep(7)
      print("\nGoodbye cruel world")
    else:
      time.sleep(9)
      print('''\nYou look around, and feel defeated. You don't care about anything, nothing, and it's not like anyone has ever cared about
you. You rummage through some of the scrap in the corner of the room, and find a piece of rope. You stare at it, and are suprised to find your
eyes slightly moist. Why should you care? Why do you care? It doesn't matter.''')
      time.sleep(15)
      print('''\nNothing matters\n''')
      time.sleep(3)
      print('''You tie yourself up, and look one last time at Adelaide. You let go.''')
      time.sleep(4)
      print('''\nAnd you never touch the ground again.''')

intro()
while True:
  first()
  time.sleep(4)
  answer = input('''\nThe End. Thanks for playing our game! If you wish to play again, type 'yes'. Otherwise, type 'no' ''')
  if answer == 'yes':
    continue
  else:
    break
print("Thanks for playing!")

time.sleep(2)

print('''\nDepression and mental health problems is a real issue in the world we live in today. Many kids and adults all suffer from
depression, which can include suicidal thoughts. However, we (the creators) wish for you to know that you are not alone. There are
people out there, friends, families, even those you may not consider close, that care about you. So please, please, please get help.
It's a good idea to open up to others. If you ever need help or you want to talk to someone anonymously or just someone who will listen,
please call one of these numbers: ''')
time.sleep(23)
print('''\nSuicide Prevention Lifeline: 1-800-273-8255''')
time.sleep(2)
print('''\nSubstance Abuse and Mental Health Services Administration: 1-800-662-HELP (4357)''')
time.sleep(2)
print('''\nNational Hopeline Network: 1-800-SUICIDE (784-2433)''')
time.sleep(2)
print('''\nNational Youth Crisis Hotline: 1-800-488-4663''')
time.sleep(2)
print('''\nCrisis Call Center: 775-784-8090''')
time.sleep(2)
print('''\nDisaster Distress Helpline: 1-800-985-5990''')
time.sleep(2)
print('''\nDepression Hotline: 630-482-9296''')
time.sleep(2)
print('''\nThere are many other more hotlines you can call. If you ever need someone to talk to, please call one
of the numbers above. Remember that you are not alone, and that there are people out there who will help you.''')
