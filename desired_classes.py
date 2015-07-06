from course import Course
from utils import *

class DesiredClasses:
    """docstring for DesiredClasses"""
    def __init__(self):
        self.enlisted_classes = [Course("Class", 'XYZ', 0, 0, 0.0)]

    def __repr__(self):
        s = ' '.join([center(x) for x in ['Rank', 'Class [Slots/Demand]', 'Credits']])
        s += '\n'
        first = True
        for x in xrange(1,len(self.enlisted_classes)):
            if not first:
                s += '\n'
            else:
                first = False
            s += center(x) + str(self.enlisted_classes[x])
        return s

    def add(self, *args):
        self.enlisted_classes.append(Course(*args))

    def print_classes(self):
        print self