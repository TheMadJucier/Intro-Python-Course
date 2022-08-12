# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 14:39:30 2022

@author: csimo
"""

#File: ps4pr2.py
#Author: Wadner Simon (casseus@bu.edu), 7/17/22
#Description: Using your conversion functions

from ps4pr1 import *

def add(b1, b2):
    dec_b1 = bin_to_dec(b1)
    dec_b2 = bin_to_dec(b2)
    
    b_sum = dec_to_bin(dec_b1 + dec_b2)
    
    return b_sum

#print(add('11100','11110'))

def increment(n):
    """Takes an 8-character string representation of a binary number 
        and returns the next larger binary number as an 8-character string
    """
    
    
    if n == '11111111':
        return '00000000'
    
    else:
        
        dec_n = bin_to_dec(n) + 1
        bin_decn = dec_to_bin(dec_n)
        
        if len(bin_decn) < 8:
            add_zeros = (8 - len(bin_decn)) *'0'
            return add_zeros + bin_decn
        else:
            return bin_decn

    