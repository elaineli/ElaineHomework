import turtle

pie = turtle.Turtle()

pie.shape('turtle')
pie.color('red')
pie.fillcolor('blue')

numSides = 4
angle = 90
size = 30

# square
for i in range(4):
    for i in range(numSides):
        pie.pendown()
        pie.forward(size)
        pie.left(angle)
    pie.penup()
    pie.forward(70)

turtle.done()
