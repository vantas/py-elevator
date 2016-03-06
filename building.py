class Building:
    def __init__(self):
        self.elevators = {} # set
        self.floors = [] # list

    def reset(self, config):
        self.elevators = config.elevators
        self.floors = config.floors
