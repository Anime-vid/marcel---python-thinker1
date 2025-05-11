# def funsd():
#     import turtle
#     window = turtle.Screen()
#     window.setup(width=600, height=400)
#     t = turtle.Turtle()
#     t.shape("turtle")
#     t.fillcolor("orange")
# # t.shape("square")
# # t.fillcolor("green")
#     t.pendown()

#     for i in range(360):
#         t.left(100)
#         t.forward(100)
#     window.mainloop()
# funsd()
# counter = 0
# def cou():
#     global counter
#     counter = counter + 1
# cou()
# cou()
# cou()
# print(counter)
# def espar(num):
#     return num % 2 == 0
# numbers = [3,9,2,8,5,4]
# for numbers in numbers:
#     if espar(numbers):
#         print(str(numbers) + " is even")
# else:
#     print(str(numbers) + " is odd")
def square(num,num2):
    return num * num + num2 * num2

print(square(50))