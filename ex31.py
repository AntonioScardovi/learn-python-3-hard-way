print("""You enter a dark room with two doors.
Do you go through door #1, #2 or door #3?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insantiy rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("You step on a rock flying in space, people with black and white wings are fighting around you. One guy with white wings is wounded on the floor.")
    print("What do you do?")
    print("1. Yell: 'Where the fuck am I?'")
    print("2. Jump off the rock.")
    print("3. Stomp on the wounded guys head.")

    abyss = input("> ")

    if abyss == "1":
        print("You get picked up by a white winged guy and he flies you through a rift in space.")
    elif abyss == "2":
        print("You start falling into the endless abyss, after a few minutes the very life force gets drained from your being and you perish.  Good job!")
    elif abyss == "3":
        print("You get picked up by a assassin with black wings and he pulls you through a rift in space.")
    else:
        print("A dude flies towards you yelling gibberish. While you stare in confusion he rips through you with his massive spikey sword so hard you become a puddle of flesh and bone.  Good job!")

else:
    print("You stumble around and fall on a knife and die.  Good job!")
#
#
#
if abyss == "1":
    print("You landed in a magnificent forest with gigantic trees. You're inside some kind of a garrison surrounded by beautiful white people. Their leader in engraved red armor apporaches you.")
    print("1. Say 'Hi!'")
    print("2. Spit on him.")
    print("3. Start running.")

    captain = input("> ")

    if captain == "1":
        print("Welcome to Atreia, mortal. Where do you come from?")
    elif captain == "2" or "3":
        print("You get shot with a massive arrow in the back. These magnificent creatures are the last things you saw.  Good job!")

    if captain == "1":

        captain1 = input("> ")

        print("You get thrown in an underground jail cell to rot forever.  Good job!")

#
#
#
if abyss == "3":
    print("You wake up in a bleak, cold fortress. A massive warrior picks you up and puts you in front of a menacing shadowy figure.")
    print("He introduces himself as Gilyun, a shadow executor. He then asks 'How did you survive, mortal?'.")
    print("1. Say: 'I stomped on paleface's head, then one of your guys picked me up.")
    print("2. Kick him in the nuts.")
    print("3. Stay silent.")

    shadow_exec = input("> ")

    if shadow_exec == "1":
        print("Most interesting! Where do you come from, little one?")
    else:
        print("The shadow executor stabs you 30 times in a second. You fall to your knees seeing blood everywhere, rapidly loosing consciousness.")
    if shadow_exec == "1":
        answer = input("> ")
        print("You get thrown in a deep, dark basement till the end of your days.")
