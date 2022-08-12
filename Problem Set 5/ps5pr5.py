# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 12:03:57 2022

@author: csimo
"""
#ps5pr5: More Algorithm Design
#Wadner Simon: 7/19/22
#casseus@bu.edu

def index(elem, seq):
    """Like the index() function, it finds the index of an elem in a given
        seq
    """
    
    def index_string(elem, seq):
        """Takes the same paramter as the parent function, but checks
            if elem is in seq, and gives the index, and returns -1 if DNE
        """
        
        if seq == []:
            return -1
        elif seq == '':
            return -1
        
        else:
            rest = index_string(elem, seq[:-1])
            if rest == 0 and seq[0] == elem:
                return rest
            
            elif seq[-1] == elem:
                
                if rest > 0:
                    return rest + 0
                
                else:
                    return rest + (len(seq))
            else:
                return rest
                
    return index_string(elem, seq)
        



def jscore(s1, s2):
    """Returns the jotto score of a given s1 and s2 """
        
    #Inner function
    def score(a1, a2):
        """Finds score of a given lst"""
        if a1 == '':
            return 0
        
        else:
            rest = score(a1[:-1], a2)
            if a1[-1] in a2:
                return rest + 1
            else:
                return rest
            
    s1_score = score(s1, s2)
    s2_score = score(s2, s1)
            
    if(s1_score <s2_score):
        return s1_score
    else:
        return s2_score
            
        
        
print(jscore('aaaattte', 'eeat') )


def lcs(s1, s2):
    
    print('start', s1, s2)
    if s1 == '' or s2== '':
        print('base case', s1, s2)
        return ''
    elif s1[0] == s2[0]:
        return s1[0] + lcs(s1[1:],s2[1:])
    
    else:
        result1 = lcs(s1[1:], s2)
        
        result2 = lcs(s1, s2[1:])
        
        return 1
        


    