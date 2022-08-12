# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 18:23:13 2022

@author: csimo
"""

#
#ps5pr3: Algorithm Design
#Wadner Simon: 7/19/22
#casseus@bu.edu


#Function 1
def cube_all_lc(values):
    """Takes an input as lst and cubes the values in the lst, using lc"""
    
    lc_cube = [x**3 for x in values]
    
    return lc_cube

 

#Function 2  
def cube_all_rec(values):
    """Takes an input as lst and cubes the values in the lst, using 
        recursion
    """
    
    if values == []:
        return []
    
    else:
        
        return cube_all_rec(values[:-1]) + [values[-1]**3]
    


#Function 3
def num_larger(threshold, values):
    """Takes a threshold and a value, and returns the number of 
       elements in the list that are greater, hence num_larger
    """
    
    lc = [1 for x in values if x > threshold ] 
    return sum(lc)


#Function 4
def num_vowels(s):
    """ returns the number of consonants in the string s
        input: s is a string of 0 or more lowercase letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])
        if s[0] in 'aeiou':
            return 0 + num_in_rest
        else:
            return 1 + num_in_rest

#Functino 5
def most_consonants(words):
    """Takes a list a returns the word with the most consonants"""

    lc_max = [num_vowels(x) for x in words if x]
    
    lc = [x for x in words if num_vowels(x) == max(lc_max)]

    return ' '.join(lc)
     

#print(most_consonants(['python', 'is', 'such', 'fun']))
    