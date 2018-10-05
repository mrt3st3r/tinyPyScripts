import time


# simple countDown which counts down from 00:59:59 to 00:00:00

def countDown():
    c = 0
    hours = 0
    while c < 1:
        for minutes in reversed(range(0, 60)):
            for seconds in reversed(range(0, 60)):
                time.sleep(1)
                print(hours, ":", minutes, ":", seconds, end="\r")
        c += 1
        print("Times up!")


countDown()


