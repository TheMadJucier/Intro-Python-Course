# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 16:31:17 2022

@author: csimo
"""

from ps9pr1 import Date

def get_age_on(self, other):
    """accepts two Date objects as parameters: one to represent a person’s birthday, and one to represent an arbitrary date. The function should then return the person’s age on that date as an integer."""
    age = 0
    
    self2 = self.copy()
    date = other.copy()
    
    age = (other.year - self2.year) -1
    
   
    
    
    if  self2.day > date.day and self2.month > date.month or self2.month > date.month:
       
        return age
    elif self2.month < date.month:
        
        age += 1
        return age
    elif self2.month == date.month and self2.day == date.day:
        
        age += 1
        return age
    else:
        
        return age
    
    
def print_birthdays(filename):
        """accepts a string filename as a parameter. The function should then open the file that corresponds to that filename, read through the file, and print some information derived from that file."""
        #words = open(filename, 'r')
        #words_text = words.read()
        
    
        
        lst_birthday = [ line.replace("\n","").split(',') for line in open(filename, 'r')]
        
        
        for r in range(len(lst_birthday)):
            name = lst_birthday[r][0]
            month = lst_birthday[r][1]
            day = lst_birthday[r][2]
            year = lst_birthday[r][3]
            
            birthday = Date(int(month), int(day),int(year))
            str_birthday = str(birthday)
            day_week = birthday.day_name()
            
            
            
            print(name, '('+ str_birthday + ')','(' + day_week +')' )
                

        
        
        
       
        
        
    
        
        
        
        
       
    
            
            
            
            
        
    
    

    
    