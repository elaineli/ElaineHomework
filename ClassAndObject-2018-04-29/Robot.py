# Learn how to use decorator to define a Class function

class Robot:

    count = 0  # Class variable

    def __init__(self, name):
        self.name = name
        Robot.count += 1
        print(f'Created robot {name}')

    def sayHi(self):
        print(f'Hi My name is a {self.name}')

    def die(self):
        Robot.count -= 1
        print(f'Destroying {self.name}')

    @classmethod
    def howMany(cls):
        print(f'There are {cls.count} robots in my universe')


robot1 = Robot('R2D2')
robot2 = Robot('Moonwalker')
Robot.howMany()
robot1.die()
Robot.howMany()
