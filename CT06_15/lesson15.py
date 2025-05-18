def turtlr(x,y):
    import turtle
    window = turtle.Screen()
    window.setup(width=600, height=400)
    t = turtle.Turtle()
    t.shape("turtle")
    t.fillcolor("orange")
# t.shape("square")
# t.fillcolor("green")
    t.pendown()
    for i in range(x):
        t.left(y)
        t.forward(y)
    window.mainloop()
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
# def square(num):
#     return num * num
# def squareadd(num,num2):
#     return num * num + num2 * num
# print(squareadd(50,100))