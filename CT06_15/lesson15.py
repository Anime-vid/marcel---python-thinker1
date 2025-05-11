def funsd():
    import turtle
    window = turtle.Screen()
    window.setup(width=600, height=400)
    t = turtle.Turtle()
    t.shape("turtle")
    t.fillcolor("orange")

# t.shape("square")
# t.fillcolor("green")
    t.pendown()

    for i in range(360):
        t.left(100)
        t.forward(100)
    window.mainloop()
funsd()