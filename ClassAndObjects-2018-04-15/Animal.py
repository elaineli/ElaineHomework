# Parent Class Animal
class Animal:

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.weight = kwargs['weight']
        self.sound = kwargs['sound']

    def __str__(self):
        return f'{self.name} is an animal' # a string format with variable inside

cat = Animal(name='cat', weight=10, sound='meow')
dog = Animal(name='dog', weight=20, sound='bark')

# Child Class Cat
class Cat(Animal):

    def __init__(self, **kwargs):
        self.breed = kwargs['breed'] # its own class init method
        super().__init__(**kwargs)  # Call parent class init method

    def __str__(self):
        return f'{self.name} is a {self.breed} cat'

cat1 = Cat(name='tom', weight='7', sound='meow', breed='Persian')
# Create an object from class Cat as cat2
cat2 = Cat(name='jerry 2', weight='3', sound='meow', breed='Russian Blue')
# Create an object from class Animal as cat2
cat3 = Animal(name='jerry 3', weight='3', sound='meow', breed='Russian Blue')

print(cat2)
print(cat3)

# Child Class Dog/Horse/Bird or ...



