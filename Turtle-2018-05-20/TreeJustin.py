import turtle
import random

t = turtle.Turtle()
t.speed(100)
turtle.bgcolor('blue')
t.pencolor('blue')
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


# create tree trunk
createRectangle(0, 0, 5, 20, 'brown')

# create tree branches

for i in range(40):

    startingX = -200 + 5 * i
    startingY = 20 + 5 * i
    width = 400 - 10 * i
    createRectangle(startingX, startingY, width, 5, 'green')


def createStar(x, y, l, color):
    t.penup()
    t.goto(x, y)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    t.left(36)
    for i in range(5):
        t.forward(l)
        t.left(144)
    t.end_fill()

createStar(-30, 200, 100, 'yellow')


def createCircle(x, y, r, color):
    t.penup()
    t.goto(x, y)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()

createCircle(500, 200, 75, 'white')
createCircle(450, 200, 75, 'blue')

for i in range(20):
    createStar(random.randint(-500, 500), random.randint(200, 400), random.randint(15,50), 'white')




turtle.done()



