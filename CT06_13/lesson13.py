# withd = 0
# Balence = 1
# usrinp = 0
# addmoney = 0
# while True:
#     print("1.Withdraw ")
#     print("2.Deposit ")
#     print("3.Check Balance ")
#     print("4.Exit ")
#     usrinp = int(input("what would you like to do? "))
#     if usrinp == 1:
#         withd = int(input("HOW MUCH TO WITHDRAW? "))
#         if Balence >= withd:
#             Balence = Balence - withd
#             print(Balence)
#         else:
#             print("yOu vErY BrOkE ")
#             print(Balence)
#     if usrinp == 2:
#         withd = int(input("HOW MUCH TO deposit? "))
#         Balence = Balence + withd
#         print(Balence)
#     if usrinp == 3:
#         print(Balence)
#     if usrinp == 4:
#         print("THE BANK IS BROKE NOW ")
#         break
# THONKTOBUY = [
#     "Apples",
#     "Bread",
#     "Carrots",
#     "Dates",
#     "Eggs",
#     "Grapes",
#     "Honey",
# ]
# print(THONKTOBUY)
# THONKTOBUY.append("ICE")
# THONKTOBUY.insert(1,"BANANA")
# print(THONKTOBUY)
# del(THONKTOBUY[2])
# THONKTOBUY.pop(2)

# for i in THONKTOBUY:
#     if i == "Apples":
#         print(i + " we need five")
REALTOPINGS = []
counter = 1
topings = [
    "Mushrooms",
    "Pepperoni",
    "Pineapple",
]
for i in topings:
    print(str(counter) + ". " + str(i))
    counter = counter + 1
while True:
    user_topings = input("what topings would you like? Give me the number: ")
    if user_topings == "end":
        break
    else:
        REALTOPINGS.append(topings[int(user_topings) - 1])
for item in REALTOPINGS:
    print(item)