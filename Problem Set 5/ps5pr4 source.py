#
# ps5pr4.py (Problem Set 5, Problem 4)
#
# Caesar cipher / decipher
#

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


# print(rot('A'))

def encipher(s, n):
    """Takes an abritrary String and a non integer, and rotates each
        character by a couple
    """

    if s == '':
        return ''
    else:
        rest = encipher(s[:-1], n)
        return rest + rot(s[-1], n)

# print(encipher('python',25))


def decipher(s):
    """Takes an encrypted string of characters a deciphers it"""

    lc_print = [s for x in range(25)]
    
    def string_probs(word):
        """takes a string and calls letter_score() and assigns the letters
            points, this is done recursively by starting with an empty string
        """
        #base case
        if word == '':
            
            return 0
        
        else:
            
            #stores recursive value
            rest = string_probs(word[1:])
            
            return rest + letter_probability(word[0])

    def recursive(lst):
        # print('start')
        if lst == []:
            #print('base case', lst)
            return []
        else:
            #print('recrusive', lst)
            rest = recursive(lst[:-1])
            #print('rest', rest)
            #print('length',len(lst) )
            return rest + [encipher(lst[-1], len(lst))]

    def best_word(words):
        #lc_score = [letter_probability(w) for w in words]
        scored_word = [[string_probs(w), w] for w in words]
        print(scored_word)
        bestpair = max(scored_word)
        return bestpair[1]
    

    english_ness = best_word(recursive(lc_print))

    #lc_range = [x for x in range(25)]

    #lc_cipher = [encipher(x, ) for x in lc_print]

    return english_ness




#print(decipher('python'))
#print(decipher('Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.'))
#print(decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla lclyfaopun dl ohcl slhyulk.'))
#print(decipher('kwvozibctibqwva izm qv wzlmz nwz iv mfkmttmvb rwj'))
#print(decipher('ncscniwc cndojscndos cdspcn picds cdsopw cdso lnpw cd cw da odsk '))