# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:43:12 2022

@author: csimo
"""

#File: ps3pr4.py
#Author: Wadner Simon (casseus@bu.edu), 7/12/22
#Description: Practicing Recursion with three functions part II
#

#Function 1
def letter_score(letter):
    
    """assigns scores to letters based on their usage, letter is checked 
       and assigned the score
    """
    assert(len(letter) == 1)
    
    #the if-else block checks to see what catagory letter is in, and assigns 
    #points
    if letter in ['a','e','i','l','n','o','r','s','t','u']:
        
        return 1
    
    elif letter in ['g','d','b','c','m','p']:
        
        if (letter == 'd' or letter == 'g'):
            
            return 2
        
        else:
            
            return 3
        
    elif letter in ['h','f','v','w','y']:
        
        return 4
    
    elif letter in ['x','j','q','z']:
        
        if (letter == 'x' or letter == 'j'):
            
            return 8
        
        else:
            
            return 10
    else:
        
        return 0
    
#print(letter_score('A'))

#function 2 
def scrabble_score(word):
    """takes a string and calls letter_score() and assigns the letters
        points, this is done recursively by starting with an empty string
    """
    #base case
    if word == '':
        
        return 0
    
    else:
        
        #stores recursive value
        scrabble_score_rest = scrabble_score(word[1:])
        
        return scrabble_score_rest + letter_score(word[0])
    
#print(scrabble_score('D?'))

#Function 3
def add(vals1, vals2):
    """ Takes two lists and adds the corresponding indexs and creates a single
        list, this a essentially matrix addition
    """
    
    #base case
    if vals1 == [] and vals2 ==[]:
        
        return []
    
    else:
        
        #stores recursive value
        add_rest = add(vals1[1:],vals2[1:])
        
        return [vals2[0]+vals1[0]] + add_rest
        
#print(add([1,2,3],[3,5,8])) 

#Function 4
def weave(s1, s2):
    """Takes two strings and takes their corresponding indices and alternates 
        them to create one string
    """
    
    #if block is to check the length of the strings, so the correct operation 
    #can be performed
    if (len(s1) > len(s2) and len(s2) != 0):
        
        #base case
        if s2 == '':
            
            return ''
        
        else:
            #stores recursive value
            weave_rest = weave(s1[1:],s2[1:])
            
            # sees if the length is equal to the smaller one
            if len(weave_rest) == len(s2):
                
                return (s1[0] + s2[0]) + weave_rest + s1[len(s1)-len(s2):]
            
            else:  
                
                return (s1[0] + s2[0]) + weave_rest 
    # checks to see if s2 is bigger
    # same recursion occurs as the first if block but for this case       
    elif (len(s1) < len(s2) and len(s1) != 0):
        
        if s1 == '':
            
            return ''
        
        else:
            
            weave_rest = weave(s1[1:],s2[1:])
            
            if len(weave_rest) == len(s1):
                
                return (s1[0] + s2[0]) + weave_rest + s2[len(s2)-len(s1):]
            
            else:  
                
                return (s1[0] + s2[0]) + weave_rest 
            
    elif (len(s1) == 0 and len(s2) > 0):
        
        return s2[:] + ''
    
    elif (len(s2) == 0 and len(s1) > 0):
        
        return s1[:] + ''
    
    elif s1 == '' and s2 == '':
        
        return ''
    
    else:
        
        weave_rest = weave(s1[1:],s2[1:])
        
        return (s1[0] + s2[0]) + weave_rest
    
#print(weave('my name is jeff','my name is simon'))
#print(weave('',''))
#print(weave('aaaa','bbbbbb'))

       
    