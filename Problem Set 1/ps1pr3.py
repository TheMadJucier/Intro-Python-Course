#
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#My contact info
#Wadner Simon
#casseus@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

# function 1
def cube(x): 
    """ returns the cube of its input x: any number (int or float)"""
    return x**3


# function 2
def convert_to_inches(yards, feet):
    """returns the number of inches in a given number of feet and yards"""
    yards_inches = yards * 36
    feet_inches = feet * 12
    sum_of_inches = yards_inches + feet_inches
    
    return sum_of_inches



#function 3
def area_sq_inches(height_yds, height_ft, width_yds, width_ft):
    """ returns area_sq_inches given four parameters, height in yards and ft, 
        and width, in yards and feet
    """
    height = convert_to_inches(height_yds, height_ft)
    width = convert_to_inches(width_yds, width_ft)
    area = height * width
    
    return area



# optional but encouraged: add test calls for your functions, indented below
if __name__ == '__main__':

    # sample test call for function 0
    print('opposite(-8) returns', opposite(-8))
    print('cube(8) returns', cube(2))
    print("convert_to_inches(4,2)", convert_to_inches(4, 2))
    print('area_sq_inches(1,2,3,1)', area_sq_inches(1, 2, 3, 1))

