#
# ps2pr3.py - Problem Set 2, Problem 3
#
# Validating Data
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
# I worked by myself
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

# Function 1

def is_valid_month(month):
    """ checks whether month can be an actual month """
    if (month > 0 and month <= 12):
        return True
    else:
        print("That month:" ,month, "is not a month.")
        return False
        
def is_leap_year(year):
    """checks whether or not the input paramter, year, satisifies the condition
        of being a leap year and returns the boolean values True or false given
    """
    if(year%400 == 0):
        return True
    elif (year%4 == 0 and (year%100 != 0)):
        return True
    else:
        return False
        
 
    
def is_valid_day_in_month(month, day, year):
    if(is_valid_month(month)):
        leapYear = is_leap_year(year)
        if (leapYear == True and month == 2):
            if((day <= 29 and day > 0)): 
                return True
            else:
                print("Either", month, " this is not Februaary or this day does not exist in February")
                return False
        elif(month == 2):
            if(day <= 28 and day > 0):
                return True
            else:
                #print("There are not ", day, "in Febrary")
                return False
        elif(month%2 != 0 or (month == 8 or month == 12)):
            if(day <= 31 and day > 0):
                return True
            else:
                return False
        elif (month%2 == 0 or (month == 9 or month == 11)):
            if(day <= 30 or day > 0):
                return True
            else:
                
                return False
    else:
        return False
    
def get_month_name(month):
  
    if (month == 1):
        return 'January'
    elif(month == 2):
        return 'February'
    elif(month == 3):
        return 'March'
    elif(month == 4):
        return 'April'
    elif(month == 5):
        return 'May'
    elif(month == 6):
        return 'June'
    elif(month == 7):
        return 'July'
    elif(month == 8):
        return 'August'
    elif(month == 9):
        return 'September'
    elif(month == 10):
        return 'October'
    elif(month == 11):
        return 'Novemeber'
    elif(month == 12):
        return 'December'
    elif(is_valid_month(month) == False):
        return 'Not Valid Month'
    
def is_valid_date(month, day, year):
    if(is_valid_month(month)):
        if(is_valid_day_in_month(month, day, year)):
            return True
        else:
            print('The day does not exist in that month')
            return False 
        return False
   
    
    
        
    
# optional but encouraged: add test calls for your functions, indented below
if __name__ == '__main__':

    # sample test call for function 0
    print('opposite(-8) returns', opposite(-8))
    print("is_leap_year('2017'):", is_leap_year(2017))
    print("is_valid_date(13,32,2018): ", is_valid_date(1, 32, 2018))
    

