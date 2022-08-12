# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 04:13:35 2022

@author: csimo
"""

#Function 1
def print_squares(values):
    """takes as a parameter a list of numbers called values, and 
    uses an element-based loop to compute and print out the 
    square of each value.
    """
    result = 0 #accumultor
    
    for i in values: #loop
        result = i**2 #square
        print(result)
        
#print(print_squares([1,2,3]))
   



#Function 2
def print_multiples(n, m): 
    """that will print out the first m multiples of 
    the integer n, one per line.
    """
    result = 0
    for i in range(m):
        
        result = n * i
        print(result)
    
        
#Function 3
def num_vowels(s):
    """which will process a string s and return
    the number of vowels (letters that are in 
    the string aeiou) in that string.
    """
    
    result = 0  #accumaltor
    for x in s: #loop
    
        if x in 'aeiou':
            result +=1
            #print(result)
            
    return result

