#
# ps5pr2.py (Problem Set 5, Problem 2)
#
# List Comprehension
#

## INSTRUCTIONS: Uncomment these lines as you go, and test them at the console
#
lc1 = [ x*2 for x in range(5)]

#print(lc1)
#
#
#
words = ['hello', 'world', 'how', 'goes', 'it?']
lc2 = [ w[1] for w in words]
#print(lc2)
#
#
#
lc3 = [ word[::-1]*2 for word in ['hello', 'bye', 'no']]
#print(lc3)
#
#
#
#
lc4 = [  x**2  for x in range(1, 10) if  x %2 == False]

#
#
#
lc5 = [ c in'b' for c in 'bu be you']
#
#
#


## continue with writing functions below:

#Function 1
def powers_of(base, count):
    """Takes a number base and raises to count, starting from 0"""
    
    lc_Power = [base **x for x in range(count)]
    
    return lc_Power

#Function 2

print(powers_of(3, 4)) 

def shorter_than(n, wordlist):
    """Takes a word list and a number n, and removes all words shorter 
        than n
    """
    lc_shorter = [x for x in wordlist if len(x) < n]
    return lc_shorter

print(shorter_than(7, ['Boston', 'Chicago', 'Washington', 'Houston']))

if __name__ == '__main__':
    
    
    # test code below, do not modify!
    for x in ['lc1', 'lc2', 'lc3', 'lc4', 'lc5']:
        if x in dir():
            print(x + ' = ', eval(x))
            

