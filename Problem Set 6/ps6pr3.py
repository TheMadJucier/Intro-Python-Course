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


#Function 1
def for_pi(n):
    
    #initalizing variables
    hits = 0 
    throws = 0
    area = 4
    
    for i in range(1,n+1): #loop
         #incrememnt
        
        throws = i
        
        
        if throw_dart(): #true
            hits = hits + 1
            area = (hits * 4)/(throws)
            print(hits, "hits out of ", throws ,"throws so that pi is", area )
            
        else: #false
            hits = hits
            area = (hits * 4)/(throws)
            
            print(hits, "hits out of ", throws ,"throws so that pi is", area )
            
    return area

print(for_pi(100))
#area of circle = (# of darts that hit the circle * area of square) / total # of darts thrown

#Function 2
def while_pi(error):
    
    #intializie variables
    hits = 0
    throws = 0
    pi = 4
    
    while (abs(math.pi - pi) >= error):
        
        
        
        if throw_dart() == True: #calling boolean func
        
            hits += 1 #inc
            throws += 1
            pi = (hits * 4)/throws #pi
            
            if abs(math.pi - pi) <= error:
                
                print(hits, "hits out of ", throws ,"throws so that pi is", pi )
                break
            else:
                print(hits, "hits out of ", throws ,"throws so that pi is", pi )

            
        else: #calling boolean func
        
            pi = (hits * 4)/throws
            throws += 1
            
            if abs(math.pi - pi) <= error:
                print(hits, "hits out of ", throws ,"throws so that pi is", pi )
                break
            
            else:
                print(hits, "hits out of ", throws ,"throws so that pi is", pi )
            
    return throws


print(while_pi(0.01))
    
        
    
