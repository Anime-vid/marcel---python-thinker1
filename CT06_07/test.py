# name = input("What is your name?")
# # asks what is your name
# print("Nice to meet you, " + name)
# # says nice to meet (the persons name)
# # next code

start = input("Start:")
end = input("end:")
increment = input("increment:")
start = int(start)
end = int(end)
increment = int(increment)
for i in range(start,end,increment):
    print(i)