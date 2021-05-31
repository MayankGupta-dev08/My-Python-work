# 53_Project1_Rock-Paper-Scissor Version2

import random

def RPS_Game(comp, user):
    if user not in ["r","s","p"]:
        print("Invalid input!!")
        a = startGame()
        return a
    elif comp == user:
        print("Computer's Choice: ", comp)
        print("Your Choice: ", user)
        print("Try Again! Both have the same choice")
        b = startGame()
        return b
    else:
        print("Computer's Choice: ", comp)
        print("Your Choice: ", user)
        
        if comp == "r":
            if user == "p":
                return True
            elif user == "s":
                return False
        elif comp == "p":
            if user == "s":
                return True
            elif user == "r":
                return False
        elif comp == "s":
            if user == "r":
                return True
            elif user == "p":
                return False


def startGame():
    print("\nComputer's turn: I'm done!!")
    randNo = random.randint(1,3)
    if randNo == 1:
        c_o = "s"
    elif randNo == 2:
        c_o = "r"
    elif randNo == 3:
        c_o = "p"

    u_o = input("What's you choice - Rock(r), Paper(p) or Scissor(s)??\n")
    return RPS_Game(c_o, u_o) 


result = startGame()
if result == True:
    print("You Won!!")
else:    
    print("Computer Won!!")