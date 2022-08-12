# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 01:23:59 2022

@author: csimo
"""

#File: ps4pr1.py
#Author: Wadner Simon (casseus@bu.edu), 7/17/22
#Description: From Binary to Decimal and back!
#

#Function 1
def dec_to_bin(n):
    """converts a decimal, n,  to a binary string
    """
    #base case
    if n == 1:
        
        return '1'
    elif n == 0:
        return '0'
    
    else:
        if (n) % 2 == 0:
           
            dec_to_bin_rest = dec_to_bin(n>>1)
            
            return dec_to_bin_rest + '0'
        else:
            
            dec_to_bin_rest = dec_to_bin(n>>1)
            
            return dec_to_bin_rest + '1'
#print(dec_to_bin(0))

#Function 2
def bin_to_dec(n):
    """Converts a binary number to a decimal
    """
    
    #base case    
    if  n == '1':
        
        
        
        return 1
    
    elif n == '0':
        
        
        
        return 0
    
    else:
        
        
        bin_to_dec_rest = bin_to_dec(n[:len(n)-1])
        
        # Inner Function 1: 
        def string_to_int(n):
            """ Converts a binary string to an int, only for bniary numbers
                b/c ints and str are not compatible
            """
            #perfroming the conversion
            if n[-1] == '1':
                return 1
            else:
                return 0
        
        
        
        return 2 * bin_to_dec_rest + string_to_int(n[-1])
    
    
#print(bin_to_dec('00011010'))


        
            
        
        