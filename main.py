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
            # if the area where the vaccum is is dirty, clean it. Otherwise leave it
            if Environment.location_condition[Environment.vacuum_location] == 1:
                Environment.location_condition[Environment.vacuum_location] = 0
                print('Location ', Environment.vacuum_location, ' has been cleaned.')
            else:
                print('Location ', Environment.vacuum_location, ' is already clean.')

            # move to the next location
            new_index = Environment.location.index(Environment.vacuum_location) + 1
            if new_index == 1:
                new_index = 0
                count += 1

            Environment.vacuum_location = Environment.location[new_index]
