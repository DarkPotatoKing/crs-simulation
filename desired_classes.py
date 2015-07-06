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
        # print args
        self.enlisted_classes.append(Course(*args))

    def print_classes(self):
        print self

    def save(self, filename = 'save'):
        if not filename:
            print 'Unable to save, please enter a filename'
        else:
            with open(filename + '.csv', 'w') as f:
                out = []
                for x in xrange(1, len(self.enlisted_classes)):
                    line = [x] + self.enlisted_classes[x].attributes()
                    line = ','.join([str(x) for x in line])
                    out.append(line)
                f.write('\n'.join(out))

    def load(self, filename = 'save'):
        if not filename:
            print 'Unable to load, please enter a filename'
        else:
            with open(filename + '.csv', 'r') as f:
                for x in f.readlines():
                    x = x.strip()
                    x = x.split(',')[1:]
                    self.add(*x)