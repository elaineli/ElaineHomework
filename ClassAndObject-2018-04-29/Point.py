# A mathematical modelling in OOP
import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return (f'({self.x}, {self.y})')

    def getDistanceFromOrigin(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def getQuadrant(self):
        if self.x > 0 and self.y > 0:
            return 'I'
        elif self.x < 0 and self.y > 0:
            return 'II'
        elif self.x < 0 and self.y < 0:
            return 'III'
        elif self.x > 0 and self.y < 0:
            return 'IV'

    def movePoint(self, deltaX, deltaY):
        self.x = self.x + deltaX
        self.y = self.y + deltaY

    @classmethod
    def getDistanceBetween(cls, p1, p2):
        dX = p2.x - p1.x
        dY = p2.y - p1.y
        return math.sqrt(dX * dX + dY * dY)

# done class definition


random = Point(-3, 4)
print(random)
print(random.getDistance())
print(random.getQuadrant())

random = Point(-3, 4)
random.movePoint(-100, -200)
print(random)

p1 = Point(2, 2)
p2 = Point(5, 6)
print('the distance between is ' + str(Point.getDistanceBetween(p1, p2)))



