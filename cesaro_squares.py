import turtle

def cesaro(tortoise, order, size):
    """Draws a cesaro torn fractal of order and size"""
    if order == 0:
        for i in range (4):
            tortoise.forward(size)
            tortoise.right(90)
    else:
        for i in range (4):
            tortoise.forward(size)
            tortoise.right(90)
            
            #for angle in [80, -160, 80, 0]:
                #cesaro(tortoise, order-1, size/3)
                #tortoise.right(angle)
            #tortoise.right(90)
        


window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue")

cesaro(tess, 1, 100)
