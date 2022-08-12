# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 15:29:18 2022

@author: csimo
"""

#File: ps4pr3.py
#Author: Wadner Simon (casseus@bu.edu), 7/17/22
#Description: Recursive operations on binary numbers
#

#Function 1
def bitwise_and(b1, b2):
    """ performs a bitwise and operation on binary numbers
        
    """
    
    #if-block tests for case of uneven lengths
    if (len(b1) > len(b2)) and len(b2) == 0:
        
        return len(b1) * '0'
    
    elif(len(b1) < len(b2)) and len(b1) == 0:
        
        return len(b2) * '0'
    
    #base case
    if b1 == '' and b2 == '':
        return ''
    else:
        
        bitwise_and_rest = bitwise_and(b1[:-1], b2[:-1])
    
        if b1[-1] == '1' and b2[-1] == '1':
            
            return bitwise_and_rest + '1'
        
        elif b1[-1] == '0' and b2[-1] == '0':
            return bitwise_and_rest + '0'
            
        else: #((b1[-1] == '1' and b2[-1] == '1') or (b1[-1] == '0' and b2[-1] == '1')):
            return bitwise_and_rest + '0'
        
        
    
#print(bitwise_and('11010', '10011'))

def add_bitwise(b1,b2):
    """Takes two binary numbers and returns the sum in binary
    """
    
    
    #I tried to do it the other way, but I failed, so I just used 
    # the code we already made in ps4pr1
    
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
        
        def add(b1, b2):
            dec_b1 = bin_to_dec(b1)
            dec_b2 = bin_to_dec(b2)
            
            b_sum = dec_to_bin(dec_b1 + dec_b2)
            
            return b_sum

        #print(add('111
    
    #Base cases 
    
print(add_bitwise('11','100'))
    