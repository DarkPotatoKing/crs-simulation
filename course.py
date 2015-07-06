from __future__ import division

from utils import *
import random

class Course():
    """TODO: docstring for Course"""
    def __init__(self, name, section, slots, demand, credits = 3.0, *args):
        self.name = str(name)
        self.section = str(section)
        self.credits = float(credits)
        self.slots = int(slots)
        self.demand = int(demand)

    def __repr__(self):
        s = '{0} {1} [{2}/{3}]'.format(str(self.name), str(self.section), str(self.slots), str(self.demand))
        return center(s) + ' ' + center(self.credits)

    def attributes(self):
        return [self.name, self.section, self.slots, self.demand, self.credits]

    def is_granted(self):
        random.seed()
        return random.random() <= self.slots / self.demand
