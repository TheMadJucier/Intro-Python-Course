# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 02:27:53 2022

@author: csimo
"""

#Function 1
def double(s):
    """takes a string s and doubles each character and returns the string"""
    
    result = '' #accumalor initialized
    
    for i in range(len(s)):
        
        result =result + s[i] * 2
       
    return result
    

#print(double('python'))

#Function 2
def weave(s1, s2):
    """ takes two strings, s1 and s2, and mixes each index after another """
    result = ''
    len_shorter = min(len(s1), len(s2)) #checking which str is shorter

    for i in range(len_shorter):
            
        if len_shorter-1 == i and len(s1) == len_shorter:# s1 is longer
             result = result+ s1[i]+ s2[i:]
             
        elif len_shorter-1 == i and len(s2) == len_shorter: #s2  is shorter
            result = result +s1[i]+ s2[i] + s1[i:]
            
        else:  # equal len strs
            result = result+ s1[i]+ s2[i]
            
    return result

#print(weave('aaaaaa', 'bbbbbb'))


#Function 3
def square_evens(values):
    """takes a list of integers called values, and that modifies
    the list so that all of its even elements are replaced with 
    their squares, but all of its odd elements are left unchanged
    """
    #result = [] #accumaltor set to empty lst
    for i in range(len(values)): 
        
        if values[i] % 2 == 0: #even
            values[i] =  values[i]**2 #builing lst
            
        elif values[i] % 2 == 1:#odd
            values[i] = values[i]
    
    
#print(square_evens([7,3,10,8]))

#Function 4
def index(elem,seq):
    """that takes as inputs an element elem and a sequence seq, 
    and that uses a loop to find and return the index of the 
    first occurrence of elem in seq.
    """
    
    result = 0 #accumaltor
    for i in range(len(seq)): #defintie loop
    
        if elem == seq[i]:
            result = result + i #setting index
            break # you told us we can use this so...
        
        elif elem == seq[i] and i == 0:
            result = 0
            break #exits out of the for loop
        
        elif i == len(seq)-1:  #
            result = -1
            break
        
    return result
    
#print(index(5,[4,10,8,4,3,4]))
#print(index('7', 'banana7'))
    
    


        