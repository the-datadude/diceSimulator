import random


class dice():
    def __init__(self, numSides):
        self.numSides = numSides

    def roll(self, numSides):
        return random.randint(1, numSides)
