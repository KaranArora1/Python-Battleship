from zellegraphics import *
import time
from multiprocessing import Pool

'''class MyClass():
    global var
    var=100
    def ja():
        print(var)

MyClass.ja()'''

'''import threading

def hi():
    for i in range(50):
        print("hi")

def ja():
    for i in range(50):
        print("ja")

thread1= hi()
thread2= ja()

thread1.start()
thread2.start()

thread1.join()  
thread2.join()'''

import threading
'''from random import randint
from time import sleep


def print_number(number):
    # Sleeps a random 1 to 10 seconds
    rand_int_var = randint(1, 10)
    sleep(rand_int_var)
    print ("Thread " + str(number) + " slept for " + str(rand_int_var) + " seconds")

thread_list = []

for i in range(1, 10):
    # Instantiates the thread
    # (i) does not make a sequence, so (i,)
    t = threading.Thread(target=print_number, args=(i,))
    # Sticks the thread in a list so that it remains accessible
    thread_list.append(t)

# Starts threads
for thread in thread_list:
    thread.start()

# This blocks the calling thread until the thread whose join() method is called is terminated.
# From http://docs.python.org/2/library/threading.html#thread-objects
for thread in thread_list:
    thread.join()

# Demonstrates that the main process waited for threads to complete
print ("Done")'''

from multiprocessing import Process

def f(name):
    print('hello', name)


p = Process(f("bob"))
p.start()
p.join()






    

