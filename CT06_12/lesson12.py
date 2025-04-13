# if num % 3 == 0 and num % 5 == 0:
#     print("The number is divisible by 3 and 5!")
# else:
#     print("The number is not divisible by 3 and 5!")
# visitors = int(input("num of current visitors?"))
# max = int(input("max num of visitors?"))
# while True:
#     inputu = input("add visitor?")
#     if inputu == "y":
#         visitors += 1
#         print(visitors)
#     if visitors == max:
#         print("max reached")
#         break
order = ""
while True:
    item = input("what u want?")
    if item == "end":
        print(order)
        break
    else:
        order  += "," + item