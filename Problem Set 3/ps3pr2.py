# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 19:08:15 2022

@author: csimo
"""

#File: ps3pr2.py
#Author: Wadner Simon (casseus@bu.edu), 7/12/22
#Description: Writing more functions that don't involve recursion
#

# Function 1
def flipside(s):
    """
    flips a given string, that is, cuts the string in half and puts the first
    half in the back and the seconf half in the front
    """
    #varaible for string evenness
    lenEO = len(s) % 2
    
    # The next three variables help to create clean look in loops
    half = len(s)//2
    
    
    half_beg = s[:half]
    
    half_end = s[half:]
    
    # checking if the string is even, greater than 0, or odd
    if(lenEO == 0):
        
        #flipping element, eventhough I don't need it i think it looks better
        flip = half_end + half_beg
        
        return flip
    
    elif(len(s) <= 0):
        
        return print("please insert a number that is greater than 0")
    
    else:
        
        flip = half_end + half_beg
        
        return flip
    
#Function 2 
def adjust(s, length):
    
    """
    takes a string a and adjust the length with white space to bring it to the
    desired length parameter
    """
    
    #if block chosen b/c to see whether or not the length is > or < than s
    if(len(s) >= length):
        
        return s[0:length]
            
    else:
        
        space_need = " " *(length - len(s))
        
        return space_need + s
        
        
    
    
#print(flipside('carpets'))
#print(adjust("compute",7))