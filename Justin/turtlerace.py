import turtle
import random
winner = ''

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

t1.shape('turtle')
t1.color('violet')
t2.shape('circle')
t2.color('cyan')
t3.shape('triangle')
t3.color('yellow')

t1.setposition(0,0)
t2.setposition(100,0)
t3.setposition(200,0)
t1.left(90)
t2.left(90)
t3.left(90)

for i in range(100):
    t1.forward(random.randint(0,5))
    t2.forward(random.randint(0,5))
    t3.forward(random.randint(0,5))

    t1p = t1.position()
    if t1p[1] >= 100 and winner == '':
        winner = 't1'
        t1.write('winning')
    t2p = t2.position()
    if t2p[1] >= 100 and winner == '':
        winner = 't2'
        t2.write('winning')
    t3p = t3.position()
    if t3p[1] >= 100 and winner == '':
        winner = 't3'
        t3.write('winning')
print(winner)
turtle.done()
