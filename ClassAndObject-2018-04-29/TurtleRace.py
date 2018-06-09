import turtle
import random

ans = turtle.textinput('race', 'To start race?')

if ans != 'yes':
    exit()


frank = turtle.Pen()
tom = turtle.Pen()
ted = turtle.Pen()
sue = turtle.Pen()

frank.width(2)
tom.width(2)
ted.width(2)
sue.width(2)

frank.shape('turtle')
frank.color('red')
tom.shape('turtle')
tom.color('green')
ted.shape('turtle')
ted.color('blue')
sue.shape('turtle')

frank.left(90)
frank.write(frank.position())

tom.forward(-100)
tom.left(90)
tom.write(tom.position())

ted.forward(100)
ted.left(90)
ted.write(ted.position())

sue.forward(200)
sue.left(90)
sue.write(sue.position())

winner = 'not found'
winnerFound = False

for x in range(100):
    r1 = random.randint(0, 5)
    r2 = random.randint(0, 5)
    r3 = random.randint(0, 5)
    r4 = random.randint(0, 5)
    frank.forward(r1)
    tom.forward(r2)
    ted.forward(r3)
    sue.forward(r4)

    if winnerFound is False and frank.ycor() >= 200:
        winner = 'frank'
        winnerFound = True
        frank.write(frank.position())
    if winnerFound is False and tom.ycor() >= 200:
        winner = 'tom'
        winnerFound = True
        tom.write(tom.position())
    if winnerFound is False and ted.ycor() >= 200:
        winner = 'ted'
        winnerFound = True
        ted.write(ted.position())
    if winnerFound is False and sue.ycor() >= 200:
        winner = 'sue'
        winnerFound = True
        sue.write(sue.position())

frank.write(frank.position())
tom.write(tom.position())
ted.write(ted.position())
sue.write(sue.position())

if winner == 'frank':

    frank.shape('circle')
if winner == 'sue':

    sue.shape('circle')
if winner == 'tom':

    tom.shape('circle')
if winner == 'ted':
    ted.shape('circle')


turtle.done()
