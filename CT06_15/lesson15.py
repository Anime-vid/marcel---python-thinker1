import turtle
def turtlr(x,y,z):
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
        t.left(z)
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
# turtlr(6,50,60)

def screensetup(a,b):
    global window
    window = turtle.Screen()
    window.setup(width=a, height=b)
    return window
def bule_ball():
    global t
    t = turtle.Turtle()
    t.shape("circle")
    t.fillcolor("blue")
    t.penup()
def MOVE_BALL(dx,dy):

    t.setx(t.xcor() + dx)
    t.sety(t.ycor() + dy)
window = screensetup(300,500)
ball = bule_ball()
while True:
    MOVE_BALL(2,2)

window.mainloop()