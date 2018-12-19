from sys import exit



# Make the start of the game
def start():
    print("You wake up half naked on the ground.")
    print("Around you are massive trees surrounded by magical blue mist.")
    print("Far down the hill in front, you see a little village filled with blue skinned people.")
    print("You see a guard post with two armed guards a little bit to the right.")
    print("On a clearence to the left is a strange rift in space, a portal.")
    print("You can't see clearly what's behind you because of all the mist.")

    choice = input("> ")

    if choice == "front":
        village()
    if choice == "back":
        wolf()
    if choice == "right":
        guard_post()
    if choice == "left":
        rift()
    else:
        dead("You fall over a a rock and die.")




# Make the village part
def village():
    print("After getting through some murmur in the center you approach a cloacked old lady.")
    print("She asks you: 'Left or Right?'")

    choice = input("> ")

    if choice == "left":
        print("The lady reveals herself as a witch and shoots a death spell out of her left hand.")
        dead("You turn into dust.")
    if choice == "right":
        print("The lady summons a rift from her right hand and pushes you through with a magic blast.")
        abyss()
    else:
        print("She turns into a witch screaming 'YOU FOOL!' and throws a volcano spell over you.")
        dead("You turned into fumes.")




# Make the wolf part
def wolf():
    print("You stumble through the thick fog and see two eyes shine through.")
    print("Do you go towards them or run?")

    choice = input("> ")

    if choice == "go" or "towards":
        print("A massive black wolf reveals himself and his fangs.")
        dead("You're dog food now.")
    if choice == "run":
        start()
    else:
        wolf()




# Make the rift part
def rift():
    print("1")

    choice = input("> ")




# Make the guard post part
def guard_post():
    print("1")

    choice = input("> ")


# Second Phase: The Abyss



def dead(why):
    print(why, "Good job!")
    exit(0)


start()
