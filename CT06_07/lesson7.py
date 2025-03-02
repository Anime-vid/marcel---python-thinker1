# for i in range(1,11,1):
#     print(i)
# for i in range(2,20,2):
#     print(i)
# for b in range(10,0,-1):
#     print(b)
# reperat = int(input("how many times repert"))
# word = input("word to repeat?")

# for i in range(reperat):
#     print(word)
# sum = 0
# for i in range(1,6):
#     sum = sum + int(input("what is number #" + str(i) + "?"))
# print("Sum of the five numbers is " + str(sum))
times = int(input("times?"))
for i in range(1,13):
    answer = times * i
    print(str(times) +  "x "  + str(i) + "=" + answer)