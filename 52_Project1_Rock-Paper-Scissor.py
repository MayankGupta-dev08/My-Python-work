# 52_Project1_Rock-Paper-Scissor Version1

import random

choices = ['r','p','s']

def RPS_Game(comp, user):
    if user not in choices:
        print("Invalid input!!")
        b = startGame()
        return b
    elif comp == user:
        print("Computer's Choice: ", comp)
        print("Your Choice: ", user)
        print("Try Again! Both have the same choice")
        a = startGame()
        return a
    else:
        print("Computer's Choice: ", comp)
        print("Your Choice: ", user)
        
        u_index = choices.index(user)
        c_index = choices.index(comp)

        if u_index < c_index:
            if u_index == 0 and c_index == len(choices)-1:
                return True
            return False
        else:
            if c_index == 0 and u_index == len(choices)-1:
                return False
            return True

def startGame():
    print("\nComputer's turn: I'm done!!")
    randNo = random.randint(1,3) #will generate randomly a number from 1,2 and 3, each time it is called.
    c_o = choices[randNo-1]
    u_o = input("What's you choice - Rock(r), Paper(p) or Scissor(s)??\n")
    return RPS_Game(c_o, u_o) 

result = startGame()
if result == True:
    print("You Won!!")
else:    
    print("Computer Won!!")