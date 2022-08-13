# -*- coding: utf-8 -*-

"""
Created on Sat Aug  6 22:26:27 2022

@author: csimo
"""

# File: ps10pr1.py
# Author: Wadner Simon (casseus@bu.edu), 8/822
# Description: Creates Board Object 


class Board:

    #Function 1
    def __init__(self, height, width): # Constructor
        """a constructor for board objects"""
        self.height = height
        self.width = width
        self.slots = [[" "] * width for r in range(height)] # Board


    #Function 2
    def __repr__(self): # Reprint
        """ Returns a string representation for a Board object 
        """
        s = ''  # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'  # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        # and the numbers underneath it.

        for v in range(1, self.width * 2):
            s += "-"
            if v == (self.width * 2 - 1):
                s += "--"

        s += '\n'  # newline at the end of the row

        for v in range(self.width):

            if v < 10:
                s += " " + str(v)
            else:
                s += " " + str(v - 10)

            # put the rest of the method here

        return s

    #Function 3
    def add_checker(self, checker, col): #
        """ Takes the checker and col and puts one checker in
        """
        assert (checker == 'X' or checker == 'O') # only accepts X or O
        assert (0 <= col < self.width) # stays within bounds

        # put the rest of the method here

        for row in range(self.height - 1, -1, -1):  # goes through all rows

            if self.slots[row][col] == ' ' and row == self.height:  # first row
                self.slots[row][col] = checker
                break
            elif self.slots[row][col] == 'X' or self.slots[row][col] == 'O':  # if occupied
                continue
            # elif self.slots[0][col] != 'X' or self.slots[0][col] != 'O':
            # self.slots[row][col] = checker
            else:  # not occupied
                self.slots[row][col] = checker

                break


    #Function 4
    def reset(self): # Clears Board
        """ Takes a Board object and clears the board"""
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' ' # Sets each cell to a space


    #Function 5
    def add_checkers(self, colnums):  # Tester
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'  # start by playing 'X'

        for col_str in colnums: 
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'



    #Function 6
    def can_add_to(self, col):
        """Takes a Board Object and the specificed column, and checks whether I can add a checker
        """

        if col < 0 or col > self.width - 1: # checks if column is within bounds
            return False

        else:
            for row in range(self.height - 1): # Runs through each cell
                if row == 0 and self.slots[row][col] == 'X' or self.slots[row][col] == 'O':  # Last Row
                    return False

                elif self.slots[self.height - 1][col] == ' ': 
                    return True

                elif row == self.height - 1 and self.slots[row][col] == ' ':  # First Row
                    return True
                    
                elif self.slots[row][col] == ' ':  # any row full
                    return True
                    break

                elif self.slots[row][col] == 'X' or self.slots[row][col] == 'O':  # any row occupied
                    continue



    #Function 7
    def is_full(self):
        """Takes a Board Object anf Checks if its Full"""

        self2 = self #Deep Copy of Object

        for col in range(self2.width): #Goes through each row

            if not self2.can_add_to(col) and col == self2.width - 1:  # Checks Last Col
                return True
                break

            elif self2.can_add_to(col) and col != self2.width - 1:  # Checks a col is not full
                return False
                break

            elif self2.can_add_to(col) == False and col != self2.width - 1 and col != 0:  # Checks Any Col
                continue



    #Function 8
    def remove_checker(self, col):
        """Takes a Board Object and a column, and removes one checker at a time"""

        for row in range(self.height): #Goes through each row
            if self.slots[row][col] == 'X' or self.slots[row][col] == 'O': #checks if its X or O
                self.slots[row][col] = ' ' #Clears one checkers with Space
                break



    #Function 9
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                        self.slots[row][col + 1] == checker and \
                        self.slots[row][col + 2] == checker and \
                        self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False




    #Function 10
    def is_vertical_win(self, checker):
        """Checks for a Verticle win for the specified checker."""

        for row in range(self.height - 3): #Goes Through each Row
            for col in range(self.width): #Goes trhough each Col
                # Check if the next four columns in this row
                # contain the specified checker.

                
                if self.slots[row][col] == checker and \
                        self.slots[row + 1][col] == checker and \
                        self.slots[row + 2][col] == checker and \
                        self.slots[row + 3][col] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False


    #Function 11
    def is_diagonal_win_p(self, checker):
        """ Checks for a Postive Diagonal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                        self.slots[row + 1][col + 1] == checker and \
                        self.slots[row + 2][col + 2] == checker and \
                        self.slots[row + 3][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False


    #Function 12
    def is_diagonal_win_n(self, checker):
        """ Checks for a Negative Diagonal win for the specified checker.
        """

        for row in range(3,self.height): #Starts at row 3
            for col in range(self.width - 3): #Excludes col 5 to 7
                # Check if the next four columns in this row
                # contain the specified checker.
                
                if self.slots[row][col] == checker and \
                        self.slots[row - 1][col + 1] == checker and \
                        self.slots[row - 2][col + 2] == checker and \
                        self.slots[row - 3][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False



    #Function 13
    def is_win_for(self, checker):
        """Takes a board object and a checker and checks if its a winning case
        """
        assert (checker == 'X' or checker == 'O') # only X or O

        # call the helper functions and use their return values to
        # determine whether to return True or False
        if self.is_vertical_win(checker) == True: #Verticle Win
            return True
        elif self.is_horizontal_win(checker) == True: #Horizontal Win
            return True
        elif self.is_diagonal_win_n(checker) == True: #Diagonal Win (Negative)
            return True
        elif self.is_diagonal_win_p(checker) == True: #Diagonal Win (Postive)
            return True
        else:
            return False
