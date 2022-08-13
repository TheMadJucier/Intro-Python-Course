#
# ps10pr2.py (Problem Set 10, Problem 2)
#
# A Connect Four Player class 
#
# File: ps10pr2.py
# Author: Wadner Simon (casseus@bu.edu), 8/822
# Description: Creates Player Object 

from ps10pr1 import Board


# Write your class below.

class Player:

    #Function 1
    def __init__(self, checker):
        """Constructor"""
        assert (checker == 'X' or checker == 'O') #only X or O
        self.checker = checker
        self.num_moves = 0


    #Function 2
    def __repr__(self):
        """Replaces print"""
        return 'Player ' + self.checker


    #Function 3
    def opponent_checker(self):
        """Returns opponents checker"""

        if self.checker == 'X': 
            return 'O'
        else:
            return 'X'



    #Function 4
    def next_move(self, b): 
        """ that accepts a Board object b as a parameter and returns
             the column where the player wants to make the next move.
        """
        self.num_moves += 1 # increases num moves
        
        while True:
            
            col = int(input('Enter a column: ')) #Taking User col input

            if b.can_add_to: #Checks if col is full
                return int(col)
            else: 
                print('Try again')
                continue
