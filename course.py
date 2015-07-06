from utils import *

class Course():
    """TODO: docstring for Course"""
    def __init__(self, name, section, credits, slots, demand):
        self.name = name
        self.section = section
        self.credits = credits
        self.slots = slots
        self.demand = demand

    def __repr__(self):
        s = '{0} {1} [{2}/{3}]'.format(str(self.name), str(self.section), str(self.slots), str(self.demand))
        return center(s) + ' ' + center(self.credits)