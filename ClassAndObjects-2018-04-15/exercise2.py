class Animal:

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.weight = kwargs['weight']
        self.sound = kwargs['sound']


