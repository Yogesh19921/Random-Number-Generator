import sys
import threading
import time


#Global variables
i=0 # the incrementer
rand=0 # the random value holder
t= None # to check whether increment thread has been initiated

#Method to increment the i value until the maximum value of Integer.
def increment():
    global i
    while (1):
        if (i >= sys.maxint): #Self explanatory
            i = 0
        else:
            i = i + 1

#Method to return the value of generated Random number.
def getRand(min,max):
    global i
    global rand
    global t

    #If the increment thread has already not been created, create it.
    if(t is None):
        t = threading.Thread(target=increment)
        t.daemon = True
        t.start()

    #let this thread sleep for 5 ms so that other thread can run for a while.
    time.sleep(0.005)

    #just simple math
    rand = min + (i % (max-min))
    return rand


