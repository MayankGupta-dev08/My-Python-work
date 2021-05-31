#Healthy Programmer
# Assuming user starts program at 9am and stops it at 5pm -=> 8 hrs
# Water - water.mp3 (3.5 litres) after every 25 min - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#Challenge:
# You will have to manage the clashes between the reminders such that no two reminders play at the same time.
# Rules
# Pygame module to play audio
  
import time
import datetime
# import pygame
from pygame import mixer
# mixer is a submodule in pygame which is being imported using pygame


# timeStart = time.time()
def getDateTime():
    return datetime.datetime.now()
# datetime is a submodule in datetime which is used to call now() function of submodule.


def start():
    file_mp3 =["HP/water.mp3", "HP/eye.mp3", "HP/exercise.mp3"]
    file_txt = ["HP/water.txt", "HP/eye.txt", "HP/exercise.txt"]
    while (time.time() - startTime) <= 45:
        if (time.time() - startTime) == 1:
            mixer.init()    # Starting music
            mixer.music.load(file_mp3[0]) # Loading the song
            mixer.music.set_volume(0.7) # Setting the volume
            mixer.music.play() # Start playing the song
            resp1 = input("Press 'p' if you have drink water: ")
            if resp1 == "p":
                mixer.music.stop()
                with open(file_txt[0], "a") as f:
                    f.write(f"Drank water @ [{str(getDateTime())}]")
                print("Entry in water.txt successful.")
        elif (time.time() - startTime) == 30:
            mixer.init()    # Starting music
            mixer.music.load(file_mp3[1]) # Loading the song
            mixer.music.set_volume(0.7) # Setting the volume
            mixer.music.play() # Start playing the song
            resp2 = input("Press 'p' if you have given rest to your eyes: ")
            if resp2 == "p":
                mixer.music.stop()
                with open(file_txt[1], "a") as f:
                    f.write(f"Given rest to eyes @ [{str(getDateTime())}]")
                print("Entry in eye.txt successful.")
        elif (time.time() - startTime) == 45:
            mixer.init()    # Starting music
            mixer.music.load(file_mp3[2]) # Loading the song
            mixer.music.set_volume(0.7) # Setting the volume
            mixer.music.play() # Start playing the song
            resp2 = input("Press 'p' if you have given rest to your eyes: ")
            if resp2 == "p":
                mixer.music.stop()
                with open(file_txt[2], "a") as f:
                    f.write(f"Done exercise @ [{str(getDateTime())}]")
                print("Entry in exercise.txt successful.")



startTime = time.time()
start()
