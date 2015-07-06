from desired_classes import DesiredClasses

class CLI:
    """TODO docstring"""
    desired_classes = DesiredClasses()

    def start(self):
        try: # to catch me fighting dirty
            f = open('save.csv')
            f.close()
            self.load()
        except:
            pass
            

        while True:
            line_input = raw_input('> ').strip()

            if line_input == 'exit':
                self.save()
                return

            self.execute(line_input)

    def execute(self, line_input):
        cmd, args = line_input.split()[0], line_input.split()[1:]

        if cmd == 'add':
            self.add(args)
        elif cmd == 'print':
            self.print_classes(args)
        elif cmd == 'save':
            self.save(args)
        elif cmd == 'load':
            self.load(args)
        else:
            print '\'{}\' is not a valid command.'.format(cmd)

    def add(self, args):
        try:
            self.desired_classes.add(*args)
        except:
            print 'unable to add class'

    def print_classes(self, args):
        self.desired_classes.print_classes()

    def save(self, args = []):
        if not args:
            args = ['save']
        self.desired_classes.save(args[0])

    def load(self, args = []):
        if not args:
            args = ['save']
        self.desired_classes.load(args[0])