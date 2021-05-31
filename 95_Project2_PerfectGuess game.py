'''Game of Perfect Guess'''

import random
randNum = random.randint(1,100) #chooses randomly feom 1 to 100 including both.
'''randChoice = random.choice([1,11,5,9,7])
print(randChoice)
Chooses randomly from the list.'''

# print(randNum)
print("<<<The Game of Perfect Guess>>>\n")
count = 1
while True:
    print("Press q to Quit")
    userGuess = input("Enter you guess: ")
    if userGuess == "q":
        break
    try:
        print("Trying....")
        userGuess = int(userGuess)
        if randNum == userGuess:
            print(f"\n**You guessed it right!! in Guess {count}**")
            break
        else:
            count +=1
            if randNum > userGuess:
                print("Your guess is too low")
            else:    
                print("Your guess is too high")
    except Exception as e:
        print(f"Your input resulted in an error: {e}")

print("Thanks for playing this Game.")
if userGuess in range(1,101):
    with open("highscore.txt") as f:
        highScore = int(f.read())

    if (count<highScore):
        print("Congrats!! You have just broken the High score.")
        with open("highscore.txt", "w") as f:
            f.write(str(count))