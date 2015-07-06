class Course():
    """TODO: docstring for Course"""
    def __init__(self, name, section, credits, slots, demand):
        self.name = name
        self.section = section
        self.credits = credits
        self.slots = slots
        self.demand = demand

    def __repr__(self):
        s = 'Class [Slots/Demand]\tCredits\n'
        s += str(self.name) + ' ' + str(self.section) + ' [' + str(self.slots) + '/' + str(self.demand) + ']\t' + str(self.credits) + '.0'
        return s