import turtle
import random


wn = turtle.Screen()

rootwindow = wn.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

wn.title("Hello, Tess!")  # Set the window title

e = turtle.Turtle()
e.shape('turtle')
e.color('red')
e.pencolor('blue')
e.width(10)

e2 = turtle.Turtle()
e2.shape('turtle')

e2.color('green')
e2.pencolor('blue')

e2.width(10)
e2.penup()
e2.goto(0, 20)
e2.pendown()

diff1 = 0
diff2 = 20

for i in range(10):

    e.speed(random.randint(1, 5))
    e2.speed(random.randint(1, 5))

    e.forward(200)
    e2.forward(200-20)

    e.circle(100, 180)
    e2.circle(100-20, 180)

    e.forward(400)
    e2.forward(400-40)

    e.circle(100, 180)
    e2.circle(100-20, 180)

    e.forward(200)
    e2.forward(200-20)




wn.mainloop()
