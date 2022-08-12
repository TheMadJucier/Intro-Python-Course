# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 19:39:18 2022

@author: csimo
"""
#function 1
def mirror(s):
    """Takes a string s, and mirrors it, and returns the mirror"""
    lengthS = len(s)
    reverse = s[lengthS::-1]
    mirrorVar = s + reverse
    return mirrorVar

#function 2
def is_mirror(s):
    """takes the mirror s, and sees if its a mirror"""
    #str = s
    #lengthS = len(s)
    #half_lengthS = len(s)//2
    if(len(s)%2 == 0 ):
        return True
    else:
        return False
 #function 3   
def replace_end(values, new_end_values):
    """takes 2 list, values and new_end_values, and replaces last indexs of values
        with new end values if its not longer
    """
    lenNEV = len(new_end_values)
    lenV = len(values)
    lenDiff = lenV - lenNEV
    if (lenNEV > lenV):
        return values
    else:
        replace = values[:lenDiff]+new_end_values
        return replace

#Function 4
def repeat_elem(values, index, num_times):
    """
    
    """
    multi = [values[index]] * num_times
    newList = values[:index] + multi + values[index+1:]
    return newList


print("mirror('bacon'):", mirror('bacon'))
print("is_mirror('bacon'):", is_mirror('baconnoca'))
print("replace_end([1,2,3,4,5],[10,11]):", replace_end([1,2,3,4,5],[10,11,12,13,14, 15]))
print("repeat_elem([10,11,12,13],2,6)", repeat_elem([10,11,12,13],2,4))