#
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions on Strings and lists, part 1
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#I did not work with anyone
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

#Function 1
def first_and_last (values):
    """ this functions takes a list as an input and returns the first and
        last value of the list
    """
    first = [values[0]]
    last = [values[-1]]
    
    return first + last

#Function 2
def longer_len(s1, s2):
    """
    takes list s1 and s2 and compares lengths
    Parameters
    ----------
    s1 : list
    s2 : list

    Returns: the list that has the longest length
    -------
    """
    length1 = s1
    length2 = s2
    if (len(length1) > len(length2)):
        return len(length1)
    else:
        return len(length2)
    
#Function 3
def move_to_end(s,n):
    """"takes two inputs, string s, integer n, and returns the new string 
        the first n characters of s have been moved to the end of the string
    """
    if ((len(s) > n) and n != 0):
        str = s[n:] + s[:n]
        return str
    else:
        return s
    


# optional but encouraged: add test calls for your functions, indented below
if __name__ == '__main__':

    # sample test call for function 0
    print('opposite(-8) returns', opposite(-8))
    print('first_and_last([1,2,3,4])', first_and_last([1,2,3,4]))
    print('first_and_last([1,2,3,4])', first_and_last([7]))
    print('longer_len("computer", "compute"):', longer_len('computer', 'compute' ))
    print('longer_len("hi", "hello"):', longer_len('hi', 'hello' ))
    print('longer_len("begin", "on"):', longer_len('begin', 'on' ))
    print('move_to_end)"hi")', move_to_end('hi', 5))
    print('move_to_end)"hi")', move_to_end('computer', 5))

