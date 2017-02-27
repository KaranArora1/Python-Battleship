for i in Player1_Locations:
    i.setFill("gray")

for i in confirmlistP1:
    i.setFill("gray")

experiment with dictionaries

A1_1=1
A2_1=2
A3_1=3
A4_1=4

dic={'A1':A1_1, "A2":A2_1, "A3":A3_1, "A4":A4_1}
P1=["A1", "A2", "A3", "A4", "A5"]

for i in dic|P1:
    print(i)

#PLAN
#APPEND VARIABLES (A1_1) to LISTS INSTEAD OF STRINGS
#USE FOR LOOPS (FOR i IN P1LOC i.setFill)
#OR
#USE DICIONARIES OR SETS AND UNIONS, MAPPING APPENDED STRINGS TO VARS AND
#                                                         v has strings mapped to vals
#SETFILLING THOSE, UNIONS TO SEE COMMONS BETWEEN LIST AND DICT AND SET THOSE
#                                                ^has the strings
#                                                 FINDING INTERSECT
#THAT DOESNT WORK SO EXPLORE SETS


'''import time
from multiprocessing import Pool
from multiprocessing import Process

li=[]

def f():
    for i in range(50):
        li.append('5')

def ff():
    for i in range(25):
        li.append('6')


p = Pool(f())
pp= Pool(ff())
thread=[p, pp]



for i in thread:
    i.start()
    

print(li)'''






    

