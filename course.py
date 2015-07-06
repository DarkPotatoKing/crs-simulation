class Course():
    """TODO: docstring for Course"""
    def __init__(self, rank, name, section, credits, slots, demand):
        self.rank = rank
        self.name = name
        self.section = section
        self.credits = credits
        self.slots = slots
        self.demand = demand

    def __repr__(self):
        s = 'Rank\tClass [Slots/Demand]\tCredits\n'
        s += str(self.rank) + '\t' + str(self.name) + ' [' + str(self.slots) + '/' + str(self.demand) + ']\t\t' + str(self.credits)
        return s