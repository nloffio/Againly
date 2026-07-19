import time
import winsound
print("Welcome to Againly!")


def timer_loop(timer,timer_name): 
    for i in range(1,timer + 1):
        print(f"{i}...")
        time.sleep(1)
    #if i <= timer:
    winsound.Beep(28000,1200)
    print(f"{timer_name}")

timer_loop(15,"Check Rs3")