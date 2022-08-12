#
# ps9pr3.py (Problem Set 9, Problem 3)
#
# More Date clients programs
#

# this import statement will allow your to use the Date class from ps9pr1.py
from ps9pr1 import Date

def nye_counts(start, end):
    """ounts how many times New Year’s Eve (December 31st) falls on each day of the week between the years start and end, inclusive of both endpoints, and that returns a dictionary containing those counts."""

    d = {} # create an empty dictionary
    d = {'Saturday': 0, 'Thursday': 0, 'Monday': 0, 'Sunday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Friday': 0}

    # add your code here
    years = end - start
    
    for y in range(years+1):
        
        ny_obj = Date(12,31,start+y)
        day = ny_obj.day_name()
        d[day] = d[day] +1
         
    return d

