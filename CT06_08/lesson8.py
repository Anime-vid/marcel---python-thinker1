# import time
# count = int(input("Countdown?"))
# for i in range(count,0,-1):
#     print(i)
#     time.sleep(1)
# print("liftoff")
import random
# print(random.randint(1,6))
# for i in range(20):
#     print(random.randint(0,9999))
# var1 = True
# var2 = False
# print(var1 == var2)
# var1 = True
# var2 = True
# print(var1 == var2)

questions = input("how many questions?")
for i in range(questions):
    num1 = (random.randint(1,50))
    num2 = (random.randint(1,50))
    ans = input("what is " + str(num1) + "+" + str(num2))
    print(num1 + num2 == int(ans))