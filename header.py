import time
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
    

print(li)






    

