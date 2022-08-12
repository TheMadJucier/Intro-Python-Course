#
# ps8pr1.py - starter code for Problem Set 8, problem 1
#
#


s1 = 'Three little kittens lost their mittens'
s2 = 'Star light, star bright'


# count all occurrences of the letter T (both upper-case and lower-case) in s1, 
# and assign the count to the variable answer0
answer0 = s1.count('T') + s1.count('t')

# do your work here!

# Puzzel 1

answer1 = s1.replace('tt', 'pp')
answer2 = s2.split('r')
answer3 = s2.upper().replace('STAR', 'NIGHT')
answer4 = s1.split('Th')
answer5 = s2.replace('ight', 'ook')






# put any print statements/test code inside this controlled block:
if __name__ == '__main__':
    
    print('s1 =', s1)
    print('s2 =', s2)
    
    print('answer0 =', answer0)
    print('answer1 =', answer1)
    print('answer2 =', answer2)
    print('answer3 =', answer3)
    print('answer4 =', answer4)
    print('answer5 =', answer5)
    
    # optional: add your test code here
    
#>>> s1.upper()
#>>> s1
#>>> s2.lower()
#>>> s2
#>>> s2.count('s')
#>>> s2.lower().count('s')
#>>> s1.count('tt')
#>>> s1.split()
#>>> s1.split('t')
#>>> s1.upper().split('T')
#>>> s1.replace('th', 'f')
#>>> s1.lower().replace('th', 'f')
#>>> s2.replace('r', 'x')
#>>> s2.replace('ar', 'amp')
#>>> s1
#>>> s2

