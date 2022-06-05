import random

class Environment(object): # create the environmrnt
    def __init__(self):
        self.location = ['a', 'b']
        self.location_condition = {'a':'0',
                                   'b':'0'}
        self.vacuum_location = random.choice(self.location)
        self.location_condition['a'] = random.randint(0, 1)
        self.location_condition['b'] = random.randint(0, 1)

class Agent(Environment): # create the agent
    def __init__(self, Environment):
        print('Vacuum location: ', Environment.vacuum_location) # find the vacuum
        print('Location condition: ', Environment.location_condition) # show the condition of the area

        count = 0
        while count < 2:
            if Environment.location_condition[Environment.vacuum_location] == 1:
                Environment.location_condition[Environment.vacuum_location] = 0
