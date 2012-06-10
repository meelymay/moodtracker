import datetime

class Mood:
    def __init__(self, happiness, motivation, relaxation):
        self.happiness = happiness
        self.motivation = motivation
        self.relaxation = relaxation

    def display(self):
        print "\thappiness",self.happiness
        print "\tmotivation",self.motivation
        print "\trelaxation",self.relaxation

    def to_string(self):
        s = ""
        s += str(self.happiness)
        s +=  " "+str(self.motivation)
        s +=  " "+str(self.relaxation)
        return s

class Day:

    def __init__(self, mood, period, notes):
        # date
        self.day = datetime.date.today()
        # mood of the day
        self.mood = mood
        # day of period (0 if not on per)
        self.period = period
        # a short note (like of an event, or a specific emotion
        self.note = notes

    def display(self):
        print self.day,
        if self.period > 0:
            print "(period",self.period,")"
        else:
            print
        self.mood.display()
        print "notes:",self.note

    def to_string(self):
        s = ""
        s += str(self.day)
        s += ' '+str(self.period)
        s += ' '+self.mood.to_string()
        return s
