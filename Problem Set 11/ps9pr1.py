#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A class to represent calendar dates


#import sqlite3



class Date:
    """ A class that stores and manipulates dates,
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, new_month, new_day, new_year):
        """ The constructor for objects of type Date. """
        self.month = new_month
        self.day = new_day
        self.year = new_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

    #### Put your code below. ####

    def advance_one(self):
        """changes the called object so that it represents one calendar day 
            after the date that it originally represented.
        """

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # is_31 = self
        if self.day == 31 and self.month == 12:
            self.year += 1
            self.month = 1
            self.day = 1
        elif self.day == 31:
            self.month += 1
            self.day = 1
        elif self.day == 30 and days_in_month[self.month - 1] == 31:
            # self.month += 1
            self.day += 1
        elif self.day == 30:
            self.month += 1
            self.day = 1
        elif self.month == 2:
            if self.is_leap_year() == True and self.day == 28:
                self.day = self.day + 1
            elif self.day == 29:
                self.month += 1
                self.day = 1
            elif self.day == 28 and self.is_leap_year() == False:
                self.month += 1
                self.day = 1
            else:

                self.day += 1

        elif self.day > 0 and (self.month != 2):
            self.day = self.day + 1

    def advance_n(self, n):  ####NEEEDS TO BE UPDATED
        """changes the called object so that it represents n calendar day 
            after the date that it originally represented.
        """
        # days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        print(self)

        for o in range(n):
            if self.day == 31 and self.month == 12:
                self.year += 1
                self.month = 1
                self.day = 1
                print(self)

            elif self.day == 30:
                self.month = 1
                self.day = 1
                print(self)

            elif self.month == 2 and self.day == 28:
                if self.is_leap_year() == True:
                    self.month = 1
                    self.day += 1
                    print(self)

                else:
                    self.month += 1
                    self.day = 1
                    print(self)

            elif self.day > 0:
                self.day += 1
                print(self)

    def __eq__(self, other):
        """Write a method __eq__(self, other) that returns True if the called object (self) and the argument (other) represent the same calendar date (i.e., if the have the same values for their day, month, and year attributes). Otherwise, this method should return False"""
        if self.day == other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False

    def is_before(self, other):
        """ returns True if the called object represents a calendar date that occurs before the calendar date that is represented by other."""
        if self.year < other.year:
            return True
        elif self.month < other.month and self.year == other.year:
            return True
        elif self.day < other.day and self.month == other.month and self.year == other.year:
            return True

        else:
            return False

    def is_after(self, other):
        """returns True if the calling object represents a calendar date that occurs after the calendar date that is represented by other"""
        if self.year > other.year:
            return True
        elif self.month > other.month and self.year == other.year:
            return True
        elif self.day > other.day and self.month == other.month and self.year == other.year:
            return True

        else:
            return False

    def days_between(self, other):
        """  returns an integer that represents the number of days between self and other."""
        self2 = self.copy()
        other2 = other.copy()

        if self.is_before(other):

            days_between = 0
            while True:
                self2.advance_one()
                days_between += 1

                if self2 == other2:
                    break
                else:
                    continue

            return 0 - days_between

        elif self.is_after(other):

            days_between = 0
            while True:
                days_between += 1
                # print(other2)
                other2.advance_one()

                if self2 == other2:
                    break
                else:
                    continue

            return days_between

        else:
            return 0

    def day_name(self):
        """returns a string that indicates the name of the day of the week of the Date object that calls it. In other words, the method should return one of the following strings: 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'."""
        self2 = self.copy()
        reference_date = Date(6, 14, 2021)
        day_of_week = self2.days_between(reference_date) % 7

        

        day_names = [ 'Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday', 'Sunday']

        return day_names[day_of_week]


    
    
