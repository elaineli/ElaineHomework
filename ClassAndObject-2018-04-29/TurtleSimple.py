import turtle

elaine = turtle.Turtle()
elaine.shape('turtle')
elaine.color('red')
elaine.fillcolor('blue')

elaine.begin_fill()

# square
elaine.forward(100)
elaine.left(90)
elaine.forward(100)
elaine.left(90)
elaine.forward(100)
elaine.left(90)
elaine.forward(100)

elaine.end_fill()

# triangle
jen = turtle.Turtle()
jen.forward(100)
jen.left(135)
jen.forward(100)
jen.left(90)
jen.forward(100)

#
tom = turtle.Turtle()
print(tom.distance(3,4))
turtle.done()
