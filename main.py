import time
from pathlib import Path
from playsound3 import playsound


print("Welcome to Againly!")
sound_file = Path(__file__).parent / "sounds" / "beep.mp3"

## defines the timer duration and message that plays when it completes

def chosen_sound(sound_file):
    try:
        playsound(str(sound_file))
    except Exception as error:
        print(f"Could not play notification sound: {error}")

## defines the timer duration and prints the description of the alarm entered when it completes and hopefully makes a sound. 

def timer_loop(timer,timer_name): 
    for i in range(1,timer + 1):
        ## making a countdown may be better
        print(f"{i}...")
        time.sleep(1)
    ## play sound here later
    print(f"{timer_name}")
    chosen_sound(sound_file)
   
timer_loop(3,"Check Rs3") 