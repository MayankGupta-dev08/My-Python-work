'''Healthy Programmer by Mayank Gupta'''
# Assuming user starts program at 9am and stops it at 5pm -=> 8 hrs
# Water - water.mp3 (3.5 litres) after every 25 min - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#Challenge: You will have to manage the clashes between the reminders such that no two reminders play at the same time.
# Rules - Pygame module to play audio
  
from time import time # time is a module and it has a function named as time
from datetime import datetime # datetime is a module and it has a class named as datetime
from pygame import mixer # from pygame module, mixer a submodule which is being imported


def playSong(fileName, stopper):
    mixer.init()
    mixer.music.load(fileName)
    mixer.music.set_volume(0.6)
    mixer.music.play()
    while True:
        resp = input()
        if resp == stopper:
            mixer.music.stop()
            break

def mylog(msg):
    with open(LogFile, "a") as f:
        f.write(f"{msg} [{datetime.now()}]\n")
    print("Your log is updated\n")

if __name__ == "__main__":
    startTime_water = time()
    startTime_eyes = time()
    startTime_exercise = time()
    water_interval = 25*60
    eyes_interval = 30*60
    exercise_interval = 45*60

    print("We hope that you reamain a Healthy Programmer\n")
    Name  = input("Enter your first name: ")
    LogFile = "HP/"+Name+".log"

    while True:
        if time() - startTime_water > water_interval:
            print("Water Drinking time. Enter 'drank' to stop the alarm. !!!")
            playSong("HP/water.mp3", "drank")
            startTime_water = time()
            mylog("Drank water at")

        if time() - startTime_eyes > eyes_interval:
            print("Eye Relax time. Enter 'eydone' to stop the alarm. !!!")
            playSong("HP/eye.mp3", "eydone")
            startTime_eyes = time()
            mylog("Eye Relaxed at")

        if time() - startTime_exercise > exercise_interval:
            print("Physical Activity time. Enter 'exdone' to stop the alarm. !!!")
            playSong("HP/exercise.mp3", "exdone")
            startTime_exercise = time()
            mylog("Physical Exercise at")