import time


seconds = int(input("Enter countdown time in seconds: "))


if seconds <= 0:
    print("Time's up!")
else:
    # Countdown loop
    while seconds > 0:
        print(seconds)
        time.sleep(1)   # 1 second wait
        seconds -= 1    
    print("Time's up!")
