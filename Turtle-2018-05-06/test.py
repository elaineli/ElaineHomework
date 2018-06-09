from turtle import Turtle, Screen

bg_colour = input("Enter the desired background colour: ")

wn = Screen()

rootwindow = wn.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

wn.bgcolor(bg_colour)  # Set the window background color
wn.title("Hello, Tess!")  # Set the window title

tess = Turtle()
tess.color("blue")  # Tell tess to change her color
tess.pensize(3)  # Tell tess to set her pen width

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()
