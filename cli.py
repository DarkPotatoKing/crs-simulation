from desired_classes import DesiredClasses

class CLI:
    """TODO docstring"""
    desired_classes = DesiredClasses()

    def start(self):
        print '----------------'
        print '|CRS Simulation|'
        print '----------------'
        print '\ntype \'tutorial\' for interactive guide. (recommended for 1st timers)'
        print 'type \'{}\' to show the help menu.\ntype \'{}\' to terminate program.'.format('help', 'exit')
        print '(note: program auto loads and saves)\n'

        try: # to catch me fighting dirty
            f = open('save.csv')
            f.close()
            self.load()
        except:
            pass
            

        while True:
            try:
                line_input = raw_input('> ').strip()
            except:
                self.save()
                return

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
        elif cmd == 'run':
            self.run(args)
        elif cmd == 'help':
            self.help(args)
        elif cmd == 'tutorial':
            self.tutorial(args)
        else:
            print '\'{}\' is not a valid command.'.format(cmd)

    def add(self, args):
        try:
            self.desired_classes.add(*args)
        except:
            print 'unable to add class'

    def print_classes(self, args = []):
        self.desired_classes.print_classes()

    def save(self, args = []):
        if not args:
            args = ['save']
        self.desired_classes.save(args[0])

    def load(self, args = []):
        if not args:
            args = ['save']
        self.desired_classes.load(args[0])

    def run(self, args = [1]):
        self.desired_classes.run(*args)

    def help(self, args):
        print '\nCommands'
        print '--------'
        print 'help:'
        print '\tshow this help menu'
        print ''
        print 'tutorial:'
        print '\tstart the interactive tutorial (recommended for 1st timers)'
        print ''
        print 'exit:'
        print '\tterminates program'
        print ''
        print 'save [filename]:'
        print '\tsaves current subjects to [filename].csv\n\t(or save.csv if no filename is provided)'
        print ''
        print 'load [filename]:'
        print '\tloads [filename].csv\n\t(or save.csv if no filename is provided)'
        print ''
        print 'add [subject] [section] [slots] [demand] [units]:'
        print '\tadd a subject to desired classes (type \'tutorial\' for more info)'
        print ''
        print 'print:'
        print '\tprints list of desired classes by ranking'
        print ''
        print 'run [num_times] [filename]'
        print '\tsimulate a batch run once (or num_times if provided)'
        print '\tif filename is provided, results will be logged to [filename].txt'
        print ''

    def tutorial(self, args):
        print ''
        print 'Welcome to the interactive tutorial!'
        print 'Heyyyy %s! ;)\n' % raw_input('Enter your name to prove you\'re human: ')
        raw_input('(say \'heyyyy\')\n> ')
        print ''
        print 'Alright, let\'s start with the tutorial. :)'
        print 'First of, you need to know how to view your desired classes.'
        self.desired_classes.reset()
        while True:
            print ''
            print 'type \'print\' to show your classes'
            if raw_input('> ').strip() == 'print':
                break
            else:
                print 'follow the instructions dammit!!!'
                print 'it\'s hard to make this tutorial you know'
                print 'please don\'t try to be a smartass'
        self.print_classes()
        print ''
        print 'good job! as you can see you currently have no classes'
        print 'thankfully, I already prepared a save file you for you\n(because you\'re special)'
        while True:
            print ''
            print r"type 'load sample' to load the sample.csv file"
            if raw_input('> ').strip() == 'load sample':
                break
        self.load(['sample'])

        print ''
        print 'You can open the .csv on a text editor and edit it manually.'
        print 'Or you can also write your own .csv, just follow the format.'
        print 'You can try it later, but for now let\'s go back to the tutorial'

        while raw_input('\nnow type \'print\' to show your desired classes\n> ').strip() != 'print':
            continue
            
        self.print_classes()
        print '\nYou can also add classes using the \'add\' command,'
        print 'but first you have to know the arguments.\n'

        print 'The first argument is the class name.'
        print 'This is the name of the subject.'
        print 'Please be consistent in naming the subjects'
        print r"(e.g. if you add a subject called 'Math17', don't add 'M17' later on)"
        print r"The program will think they're different subjects."
        print r"(this is important in solving conflicts during the batch run)"
        print ''

        subject = ''
        while True:
            subject = raw_input('Enter a subject (do not put spaces in between):\n> ')
            if len(subject.split()) > 1 or subject == '':
                continue
            else:
                break

        print ''
        print 'Next is the section, it\'s the code that tells the subjects timeslot.'
        print 'Again, please be consistent. Subjects with the same timeslot should have the same section'
        print 'The program uses this to know the schedule and to resolve conflicts'
        print 'type only the letters and not the numbers (e.g. HTUV instead HTUV1)'
        print ''
        section = ''
        while True:
            section = raw_input('Enter section\n> ')
            if section:
                break
        print ''
        print 'Next is the available slots.'
        print 'Make sure to enter the available slots and not the total slots.'
        print r"It's the first number that appears in (available slots/total slots/demand)"
        print r"(e.g. 10/15/15, type 10)"
        print ''
        print 'The next two arguments is the demand and the number of units.'
        print 'Type 0.0 if the subject is an NSTP or PE'
        print ''
        print 'Assuming {} {} has 10 available slots and 20 demand, and is worth 3.0 units...'.format(subject, section)
        print ''
        while True:
            if raw_input('type \'add ' + str(subject) + ' ' + str(section) + ' 10 20 3.0\'\n> ').strip() == 'add ' + str(subject) + ' ' + str(section) + ' 10 20 3.0':
                break
        self.add([subject, section, 10, 20, 3.0])
        print ''
        while raw_input('now type \'print\'\n> ').strip() != 'print':
            continue
        self.print_classes()
        print ''
        print 'See, now your class has been added'
        print ''
        print 'now you\'re ready to simulate a batch run'
        print ''

        while raw_input('simply type \'run\'\n> ').strip() != 'run':
            continue

        self.run()
        print ''
        print 'It simulates a batch run, the first part shows which subjects you got.'
        print 'you can run multiple times by typing \'run [number]\', e.g. \'run 100\''
        print 'At the end there\'s a summary of stats regarding the subjects'
        print 'It shows you how many times you got each subject during multiple batch runs'
        print 'Try running multiple times (> 100) to see the chance of getting each individual subject on average.'
        print ''

        print 'And you\'re done :)'
        print 'type \'save (optional: filename)\' to save your current subjects so you can load it later'
        print 'type \'exit\' to terminate program'



