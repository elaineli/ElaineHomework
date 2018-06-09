import turtle

#elaine = turtle.Turtle()

elaine = turtle.Pen()

elaine.shape('turtle')
elaine.color('red')
elaine.fillcolor('blue')

numSides = int(input("Sides?"))
angle = 180-(numSides-2)*180/numSides

# square
for i in range(4):
    for i in range(numSides):
        elaine.pendown()
        elaine.forward(30)
        elaine.left(angle)
    elaine.penup()
    elaine.forward(70)

turtle.done()
