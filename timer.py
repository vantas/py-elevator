class Timer:
    def __init__(self):
        self.time = 0.0

    def reset(self, config):
        self.time = 0.0

    def currentTime(self):
        return self.time

    def advanceTo(self, time):
        self.time = time

    def advanceBy(self, amount):
        self.time += amount
