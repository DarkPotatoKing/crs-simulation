from course import Course
from utils import *

class DesiredClasses:
    """docstring for DesiredClasses"""
    def __init__(self):
        self.enlisted_classes = [Course("Class", 'XYZ', 0.0, 0, 0)]

    def __repr__(self):
        s = ' '.join([center(x) for x in ['Rank', 'Class [Slots/Demand]', 'Credits']])
        s += '\n'
        for x in xrange(0,len(self.enlisted_classes)):
            s += center(x) + str(self.enlisted_classes[x])
        return s
