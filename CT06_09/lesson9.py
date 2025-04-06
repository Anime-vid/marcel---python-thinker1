# pos_days = 0
# num_days = int(input("how many days?"))
# temp_days = 0
# for i in range(1,num_days + 1):
#     temp_days = int(input("temp of day " + str(i) + ":"))
#     if temp_days > 30:
#         pos_days = pos_days + 1
# print(pos_days)
good = 0
num_cus = int(input("how many customers?"))
bad = 0
rating = 0
for i in range(1,num_cus + 1):
    rating = int(input("rating of customer? " + str(i) + ":"))
    if rating > 3:
        good = good + 1
    else:
        bad = bad + 1  
print("amount of good reviews")
print(good)
print("amount of bad reviews")
print(bad)