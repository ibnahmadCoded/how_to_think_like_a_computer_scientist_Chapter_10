import turtle 
def koch(tortoise, order, size):
    """
    Make turtle tortoise draw Koch fractal of 'order' and 'size'.
    Leave the turtle facing the same direction.
    """

    if order == 0:
        tortoise.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(tortoise, order-1, size/3)
            tortoise.left(angle)
        

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.speed(10)

for i in range(3):
    koch(tess, 2, 200)
    tess.left(-120)

window.mainloop()
