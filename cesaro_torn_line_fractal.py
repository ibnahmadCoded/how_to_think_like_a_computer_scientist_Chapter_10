import turtle

def cesaro(tortoise, order, size):
    """Draws a cesaro torn fractal of order and size"""
    if order == 0:
        tortoise.forward(size)
    else:
        for angle in [80, -160, 80, 0]:
            cesaro(tortoise, order-1, size/3)
            tortoise.right(angle)
        


window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")

cesaro(tess, 3, 1000)
