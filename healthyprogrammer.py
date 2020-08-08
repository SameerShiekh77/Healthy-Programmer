"""
Exercise no 7
9am to 5pm
Water - water.mp3 (3.5 litres) - Drank - log
Eyes - Eyes.mp3 - every 30min - EyDone - log
Physical activity - physical.mp3 - every 45 min - ExDone - log
"""

from pygame import mixer
from datetime import datetime
from time import time


print("\t\t\t\tDEVELOP BY MUHAMMAD SAMEER\n")
print(datetime.now())
name = input("Enter your name: ")
print(f"Hi! {name.capitalize()}, Welcome to My Healthy Programm")

def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

        
def logg(msg):
    with open("Statics.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n\n")
init_water = time()
init_eyes = time()
init_physical = time()
init_gametime = time()

eyessec = 3600  
watersec =7200 
physicalsec = 14400
gamesec = 10800
while True:
    if time() - init_water > watersec:
        print("Water Time, Enter 'drank' to stop water alarm ")
        musicloop("water.mp3", "drank")
        init_water = time()
        logg("Drank water at")
        
    elif time() - init_eyes > eyessec:
        print("Eyes exercise Time, Enter 'Eydone' to stop eye alarm ")
        musicloop("eyes.mp3", "Eydone")
        init_eyes = time()
        logg("Eyes exercise at")
        
    elif time() - init_physical > physicalsec:
        print("Exercise Time, Enter 'Exdone' to stop exercise alarm ")
        musicloop("exe.mp3", "Exdone")
        init_physical = time()
        logg("Drank water at")
        
    # elif time() - init_gametime > gamesec:
    #     print("Game Time, Enter 'Play' to stop exercise alarm ")
    #     musicloop("game.mp3", "Play")
    #     init_gametime = time()
    #     logg("Play at")
    