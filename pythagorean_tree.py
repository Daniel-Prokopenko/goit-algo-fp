import turtle


def draw_fractal(depth, size=80):
    if depth:
        t.forward(size)
        t.left(45)
        draw_fractal(depth - 1, size / 1.25)
        t.right(90)
        draw_fractal(depth - 1, size / 1.25)
        t.left(45)
        t.backward(size)


depth = int(input("What depth? ===>  "))


t = turtle.Turtle()
t.left(90)
t.pendown()
t.speed(0)
draw_fractal(depth)

turtle.mainloop()
