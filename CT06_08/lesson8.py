import time
count = input("Countdown?")
for i in range(count,0,-1):
    print(i)
    time.sleep(1)
print("liftoff")