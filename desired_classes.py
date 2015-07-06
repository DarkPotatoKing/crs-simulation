from __future__ import division 
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

    def run(self, num_times = 1, filename = ''):
        num_times = int(num_times)
        run_total_units = 0.0
        num_times_granted = dict()

        for x in self.enlisted_classes:
            num_times_granted[x] = 0

        if filename:
            # delete contents of file
            f = open(filename, 'w')
            f.close()

        for ctr in xrange(num_times):
            granted_classes = []

            for x in self.enlisted_classes[1:]:
                if x.is_granted() and self.no_conflict(x, granted_classes):
                    granted_classes.append(x)
                    num_times_granted[x] += 1

            units = sum([x.credits for x in granted_classes])
            run_total_units += units

            if filename:
                with open(filename + '.txt', 'a+') as f:
                    f.write('Run #%d:\n' % (ctr+1))
                    f.write('\n'.join([str(x) for x in granted_classes]) + '\n')
                    f.write('Total units: {}\n\n'.format(sum([x.credits for x in granted_classes])) + '\n')
            else:
                print 'Run #%d:' % (ctr+1)
                print '\n'.join([str(x) for x in granted_classes])
                print 'Total units: {}\n\n'.format(units)

        run_average_units = run_total_units / num_times

        if filename:
            with open(filename + '.txt', 'a+') as f:
                f.write('Run summary (%d run/s)\n' % num_times)
                f.write('Average units: %f\n' % (run_average_units))
                f.write('Course summary:\n')
                for x in self.enlisted_classes[1:]:
                    f.write(str(x) + ' {}/{} times ({})\n'.format(num_times_granted[x],num_times,num_times_granted[x]/num_times))          
            print 'results logged to %s.txt' % filename
        else:
            print 'Run summary (%d run/s)' % num_times
            print 'Average units: %f' % (run_average_units)
            print 'Course summary:'
            for x in self.enlisted_classes[1:]:
                print x, '{}/{} times ({})'.format(num_times_granted[x],num_times,num_times_granted[x]/num_times)
                

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
