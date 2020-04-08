import turtle

def sierpinski_triangle(tortoise, order, size):
    colorChangeDepth = 0
    colors = ["Red", "Magenta", "Blue"]
    if order == 0:
        for i in range(3):
            tortoise.forward(size)
            tortoise.left(120)
    else:
        

        sierpinski_triangle(tortoise, order-1, size/2)
        tortoise.forward(size/2)
        colorChangeDepth += 1
        tess.color(colors[colorChangeDepth])
        sierpinski_triangle(tortoise, order-1, size/2)
        tortoise.backward(size/2)
        tortoise.left(60)
        tortoise.forward(size/2)
        tortoise.right(60)
        colorChangeDepth += 1
        tess.color(colors[colorChangeDepth])
        sierpinski_triangle(tortoise, order-1, size/2)
        tortoise.left(60)
        tortoise.backward(size/2)
        tortoise.right(60)
        
        


window = turtle.Screen()
window.bgcolor("lightgreen")

color = "blue"
tess = turtle.Turtle()
tess.color(color)

order = int(input("what order do you want? "))


sierpinski_triangle(tess, order, 400)
