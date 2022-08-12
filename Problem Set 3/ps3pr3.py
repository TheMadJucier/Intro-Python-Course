# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 19:51:39 2022

@author: csimo
"""

#File: ps3pr3.py
#Author: Wadner Simon (casseus@bu.edu), 7/12/22
#Description: Practicing Recursion with three functions
#

#Function 1
def double(s):
    
    """ Doubles a the characters within a string s recursively
    """
    
    #checking base case
    if s == '':
        
       # print("return qoutes")
        return ''
    
    else:
        
        #storing recursive result
        double_rest = double(s[1:])
        
        return s[0]* 2 + double_rest
    
    
#print(double('c'))

#Function 2
def copy(s,n):
    """ Using recursion, the function copies a string and adds it to the end
        with out using multiplication
    """
    
    #base case, and if statements to check what n is and runs accoridngly
    if(n <0 ):
        
        return ''
    
    if n == 0:
        
        #base case
        return ''
    
    else:
        
        #recursive
        copy_rest = copy(s[:], n-1)
        
        
        return copy_rest + s
    
#print(copy('hello', 2))

#Function 3
def compare(list1, list2):
    """ Takes two lists and checks each index and checks if list1 is greater
        than list2, if so it adds one, otherwise adds nothing (0)
    """
    
    #if blocks check to see the size of the lists
    if (len(list1) > len(list2)):
        
        #base case
        if list2 == []:
            
            return 0
        
        else:
            
            #recursive
            compare_rest = compare(list1[1:],list2[1:])
           
            # checks elements
            if(list1[0] < list2[0]):
                
               
                return compare_rest +1
            #checks elements
            elif(list1[0] > list2[0] or list1[0] == list2[0]):
                
               
                return compare_rest 
            
    #checks length of each        
    if(len(list1) < len(list2)):
        
        if list1 == []:
            
           # print("base case")
            return 0
        
        else:
            
            compare_rest = compare(list1[1:],list2[1:])
          
            if(list1[0] < list2[0]):
                
               
                return compare_rest +1
            
            elif(list1[0] > list2[0] or list1[0] == list2[0]):
                
               
                return compare_rest 
            
        
    else:
        if list1 == [] and list2 == []:
            
            
            return 0
        
        else:
            compare_rest = compare(list1[1:],list2[1:])
            
           
            if(list1[0] < list2[0]):
                
                
                return compare_rest +1
            
            elif(list1[0] > list2[0] or list1[0] == list2[0]):
                
                
                return compare_rest 
