# If Highscore given then replace in HiScore.txt, otherwise not.

def game():
    sc = int(input("Enter your score: "))
    return sc

score = game()
with open("HiScore.txt", "r") as f:
    hiscore = f.read()
if hiscore=="":
    print("Previous High score: None")
    print("Updating the High score!!")
    with open("HiScore.txt", "w") as f:
        f.write(str(score))
elif score>int(hiscore):
    print("Previous High score: ", hiscore)
    print("Updating the High score!!")
    with open("HiScore.txt", "w") as f:
        f.write(str(score))
else:    
    print("No Updation!!")