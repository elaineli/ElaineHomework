import turtle
import random

t = turtle.Turtle()
t.speed(1)
def createRectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def createStar(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('yellow')
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.left(216)
    t.end_fill()

def createCircle(x, y, radius, color):
    t.penup()
    t.color(color)
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# create tree trunk
createRectangle(0, 0, 5, 20, 'brown')

# create tree branches
for i in range(20):
    startingX = -200 + 5 * i
    startingY = 20 + 5 * i
    width = 400 - 10 * i
    createRectangle(startingX, startingY, width, 5, 'green')


# createStar(0, 0, 50)
#
# createCircle(20, -20, 10, 'blue')

turtle.done()
