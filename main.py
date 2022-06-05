import random

class Environment(object):
    def __init__(self):
        self.location = ['a', 'b']
        self.location_condition = {'a':'0',
                                   'b':'0'}
        self.vacuum_location = random.choice(self.location)
        self.location_condition['a'] = random.randint(0, 1)
        self.location_condition['b'] = random.randint(0, 1)