import turtle

j = turtle.Turtle()

# j.penup()
# j.backward(100)
# j.left(90)
# j.forward(100)
# j.right(90)

j.penup()
j.goto(-100, 100)

j.pendown()
j.speed(1)

j.backward(100)
j.right(90)
j.forward(200)
j.left(90)
j.forward(100)
j.penup()
j.forward(200)
j.pendown()
j.forward(100)
j.left(90)
j.forward(100)
j.left(90)
j.forward(100)
j.right(90)
j.forward(100)
j.right(90)
j.forward(100)

turtle.done()
