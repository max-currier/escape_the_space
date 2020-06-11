from sys import exit

def start(cash, gear):
    choice = input(">>> ")

    if "left" in choice:
        punk(cash, gear)

    elif "right" in choice:
        friend(cash, gear)

    else:
        print("Couldn't hear you over the metal band across the hall. Left or right?")
        start(cash, gear)


def punk(cash, gear):
    cash_taken = 20
    print("\nYou walk left out the door down the musty hallway.")
    print("You round a corner and reach a dead end. A jittery punk comes out of a practice room clutching a small knife.")
    print("He grabs your shoulder and whispers into your ear \"*sniff* Gimme your money...or that guitar...*sniff* and my little friend goes right back in my pocket ... *sniff*\"")
    print(f"\nYou look in your wallet and see you have ${cash}.")
    print("What do you do?")

    choice = input(">>> ")

    if ("money" in choice or "pay" in choice) and not "don't" in choice and not "not" in choice and not "dont" in choice:
        cash -= cash_taken
        print(f"\nThe punk snatches ${cash_taken} from your wallet and goes back into his practice room.")
        print("You turn around and go back the way you came, down the hall past your practice room.")

        friend(cash, gear)

    elif "guitar" in choice and gear == True and not "don't" in choice and not "not" in choice and not "dont" in choice:
        gear = False
        print("\nThe punk snatches your guitar and goes back into his rehearsal space.")
        print("You turn around and go back the way you came, down the hall past your practice room.")
        friend(cash, gear)

    elif "run" in choice or "flee" in choice:
        print("\nYou turn tail and bolt before he can do anything about it.")

        friend(cash, gear)

    else:
        lose("\nWhile you stumble on your words, the shifty punk makes real on his threat after all and stabs you in the throat.\n")


def friend(cash, gear):
    gig_debt = 10
    print("\nYou run into your old bandmate standing outside the bathroom.")
    print(f"He reminds you that you still owe him ${gig_debt} from your last gig.")
    print(f"\nYou look in your wallet and see you have ${cash}.")
    print("What do you do?")

    choice = input(">>> ")

    if (("give" in choice or "pay" in choice) and cash >= gig_debt) and not "don't" in choice and not "not" in choice and not "dont" in choice:
        cash -= gig_debt
        print("\nYou hand him a ten and shuffle past him. He blew it at that gig but it's not worth the trouble at this point.")

        office(cash, gear)

    else:
        print("\nYour friend give you a familiar look of disappointment as he walks away empty handed.")
        print("You shuffle past him and continue down the musty hall.")

        office(cash, gear)



def office(cash, gear):
    rent = 30
    print("\nYou round the corner and see the main payment desk just in front of the exit to the street.")
    print("The manager looks from his computer with no expression.")
    print(f'"That will be ${rent} for the hour," he says flatly.')
    print(f"\nYou look in your wallet and see you have ${cash}.")

    if cash < rent and gear == True:
        print("\n'If you're short on cash I guess can hold your guitar as a deposit.")
        print("What do you do?")

        choice = input(">>> ")

        if "give" in choice or "hand" in choice:
            gear = False
            print("\nThe manager takes your guitar and you exit the smokey maze hallways.")

            meter(cash, gear)

        else:
            lose("\nNo free lunch today. The manager locks the door and calls the police.")


    elif cash < rent and gear == False:
        lose("\nYou don't have enough to pay for your space. The manager locks the door and calls the police.")

    else:
        print("What do you do?")
        unpaid = True
        while unpaid == True:

            choice = str(input(">>> "))

            if "pay" in choice or "give" in choice:
                cash -= rent
                unpaid = False
                print("\nYou pay him the $30 and exit the smokey maze hallways.")

                meter(cash, gear)

            else:
                print("Couldn't hear you over the drummer playing next door. Can you say that more clearly?")


def meter(cash, gear):
    print("\nYou see your van and now all you have to do is put $5 into the parking meter and you're home free.")
    print(f"\nYou look in your wallet and see you have ${cash}.")

    if cash >= 5 and gear == True:
        cash -= 5
        print("You put $5 in the meter, throw your guitar in the back of the van, and head toward the gig.")
        print("\nYou have successfully escaped the practice space.")
        print("* * * * * You win! * * * * *")

    elif cash >= 5 and gear == False:
        lose("... but without a guitar for the gig, you're going to need to go back into the practice space to try to borrow someone else's for the night...")

    else:
        lose("\n...without enough cash to pay for parking, you have no choice but to go back into the practice space to try to borrow some cash...")


def lose(reason):
    print(reason, "Now you will NEVER escape the practice space.")
    print("You LOSE.")

    exit(0)


print("*** Welcome to ESCAPE THE PRACTICE SPACE ***")
print("Your ears are bleeding. You're head is throbbing. You've got to get out of this rehearsal space.")
print("You exit your room. But which did you come from to get back to the van... \nleft or right?")

starting_cash = 37 # starting funds
guitar = True # True means player has guitar, False means they do not

start(starting_cash, guitar)
