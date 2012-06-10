from day import *
import pickle

f = open('moods.pkl','r')
moods = pickle.load(f)
f.close()

period = int(input('period day: '))
happiness = int(input('happiness (0-10): '))
motivation = int(input('motivation (0-10): '))
relaxation = int(input('relaxation (0-10): '))
note = raw_input('Anything else? ')

mood = Mood(happiness, motivation, relaxation)

today = Day(mood, period, note)

moods[today.day] = today

f = open('moods.pkl','w')
pickle.dump(moods, f)
f.close()
