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
# times = int(input("times?"))
# for i in range(1,13):
#     answer = times * i
#     print(str(times) +  "x "  + str(i) + "=" + str(answer))
# layers = int(input("number of layers?"))
# for i in range(1,layers + 1):
    
# print(str(i) * i)
num = int(input("how many students you have?"))
num = num + 1
sum = 0
for i in range(1,num):
    sum += int(input("what is student " + str(i) + " score?"))
avg = sum / (num - 1)
print(avg)