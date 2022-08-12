#
# ps6pr3.py (Problem Set 6, Problem 3)
#
# Estimating pi
#
# Computer Science 111
#

import random
import math

def throw_dart():
    """ Simulates the throwing of a random dart at a 2 x 2 square that.
        is centered on the origin. Returns True if the dart hits a circle
        inscribed in the square, and False if the dart misses the circle.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1.0:
        return True
    else:
        return False

### PUT YOUR WORK FOR PROBLEM 3 BELOW. ###

def for_pi(n):
    hits = 0
    throws = 0
   # result = 0
    area = 0
    # pi = area/radius**2
    #pi = 0
    for i in range(n+1):
        throws += 1
        
        if throw_dart():
            hits += 1
            area = (hits * 4)/throws
            #pi = area/ 4
            print(hits, "hits out of ", throws ,"throws so that pi is", area )
        elif throw_dart() != True:
            area = (hits * 4)/throws
           # pi = area/ 4 
            print(hits, "hits out of ", throws ,"throws so that pi is", area )
    return area

#print(for_pi(10))
#area of circle = (# of darts that hit the circle * area of square) / total # of darts thrown

def while_pi(error):
    hits = 0
    throws = 0
   # result = 0
    area = 0
    # pi = area/radius**2
    #pi = 0
    while (abs(math.pi - area) > error):
        throws += 1
        
        if throw_dart():
            hits += 1
            area = (hits * 4)/throws
            #pi = area/ 4
            print(hits, "hits out of ", throws ,"throws so that pi is", area )
        elif throw_dart() != True:
            area = (hits * 4)/throws
           # pi = area/ 4 
            print(hits, "hits out of ", throws ,"throws so that pi is", area )
    return area

print(while_pi(0.1))
    
        
    
