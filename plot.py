from day import *
import pickle

f = open('moods.pkl','r')
days = pickle.load(f)
f.close()

days_sort = [d for d in days]
days_sort.sort()


f = open('moods.txt','w')
for d in days_sort:
    s = days[d].to_string()
    f.write(s+'\n')
f.close()
