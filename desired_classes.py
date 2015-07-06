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
            print 'saved as {0}.cvs'.format(filename)

    def load(self, filename = 'save'):
        if not filename:
            print 'Unable to load, please enter a filename'
        else:
            with open(filename + '.csv', 'r') as f:
                for x in f.readlines():
                    x = x.strip()
                    x = x.split(',')[1:]
                    self.add(*x)
            print 'loaded {0}.cvs'.format(filename)

    def run(self):
        granted_classes = []

        for x in self.enlisted_classes[1:]:
            if x.is_granted() and self.no_conflict(x, granted_classes):
                granted_classes.append(x)

        print 'Granted classes:'
        print '\n'.join([str(x) for x in granted_classes])
        print 'Total units: {}'.format(sum([x.credits for x in granted_classes]))

    def no_conflict(self, course, granted_classes):
        # check if overload
        units = sum([x.credits for x in granted_classes])
        if units + course.credits > 20.0:
            return False
        else:
            # check if conflict with same subject or sched
            for x in granted_classes:
                if x.name == course.name or x.section == course.section:
                    return False

            # if no conflicts, return True
            return True
