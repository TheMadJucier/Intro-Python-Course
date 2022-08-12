#
# ps5pr4.py (Problem Set 5, Problem 4)
# 
# Caesar cipher / decipher
#
#ps5pr4:Caesar cipher and decipher
#Wadner Simon: 7/19/22
#casseus@bu.edu

# A template for a helper function called rot that we recommend writing
# as part of your work on the encipher function.
def rot(c, n):
    """rotate c forward by n characters, wrapping as needed; 
        only letters change
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    # Put the rest of your code for this function below.

    if 'a' <= c <= 'z':
        new_ord = ord(c) + n
        if new_ord > ord('z'):
            new_ord = new_ord - 26
    elif 'A' <= c <= 'Z':
        new_ord = ord(c) + n
        if new_ord > ord('Z'):
            new_ord = new_ord - 26
    else:
        new_ord = ord(c)

    return chr(new_ord)


#### Put your code for the encipher function below. ####


# A helper function that could be useful when assessing
# the "Englishness" of a phrase.
# You do *NOT* need to modify this function.
def letter_probability(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for English);
        returns 1.0 for any other character.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ':
        return 0.1904
    if c == 'e' or c == 'E':
        return 0.1017
    if c == 't' or c == 'T':
        return 0.0737
    if c == 'a' or c == 'A':
        return 0.0661
    if c == 'o' or c == 'O':
        return 0.0610
    if c == 'i' or c == 'I':
        return 0.0562
    if c == 'n' or c == 'N':
        return 0.0557
    if c == 'h' or c == 'H':
        return 0.0542
    if c == 's' or c == 'S':
        return 0.0508
    if c == 'r' or c == 'R':
        return 0.0458
    if c == 'd' or c == 'D':
        return 0.0369
    if c == 'l' or c == 'L':
        return 0.0325
    if c == 'u' or c == 'U':
        return 0.0228
    if c == 'm' or c == 'M':
        return 0.0205
    if c == 'c' or c == 'C':
        return 0.0192
    if c == 'w' or c == 'W':
        return 0.0190
    if c == 'f' or c == 'F':
        return 0.0175
    if c == 'y' or c == 'Y':
        return 0.0165
    if c == 'g' or c == 'G':
        return 0.0161
    if c == 'p' or c == 'P':
        return 0.0131
    if c == 'b' or c == 'B':
        return 0.0115
    if c == 'v' or c == 'V':
        return 0.0088
    if c == 'k' or c == 'K':
        return 0.0066
    if c == 'x' or c == 'X':
        return 0.0014
    if c == 'j' or c == 'J':
        return 0.0008
    if c == 'q' or c == 'Q':
        return 0.0008
    if c == 'z' or c == 'Z':
        return 0.0005
    return 1.0


#### Put your code for the decipher function below. ####

#Function 1
def encipher(s, n):
    """Takes an abritrary String and a non integer, and rotates each
        character by a couple
    """

    if s == '':
        return ''
    else:
        rest = encipher(s[:-1], n)
        return rest + rot(s[-1], n)


#Function 2
def decipher(s):
    """Takes an encrypted string of characters a deciphers it"""

    lc_print = [s for x in range(25)]
    
    #Inner Function 1
    def string_probs(word):
        """takes a string and calls letter_score() and assigns the letters
            points, this is done recursively by starting with an empty string
        """
        
        if word == '':
            return 0
        
        else:
            rest = string_probs(word[1:])
            
            return rest + letter_probability(word[0])

    # Inner Function 2
    def recursive(lst):
        """Cycles through the a list"""
        if lst == []:
            return []
        
        else:
            rest = recursive(lst[:-1])
            
            return rest + [encipher(lst[-1], len(lst))]
        
        #Inner Function 3
    def best_word(words):
        """Finds the string witht the most weight
        """
        
        scored_word = [[string_probs(w), w] for w in words] 
        
        print(scored_word)
        
        bestpair = max(scored_word)
        
        return bestpair[1]
    

    english_ness = best_word(recursive(lc_print)) # calling everthing



    return english_ness 




