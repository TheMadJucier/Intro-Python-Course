#
# ps11pr3.py (Problem Set 11, Problem 3)
#
# An RandomPlayer for use in Connect Four
#


# File: ps11pr3.py
# Author: Wadner Simon , 8/12/22
# Description: Creating Random Client


import random
from ps10pr3 import * # to use the connect_four and process_move functions

class RandomPlayer(Player):
    """Creates a Random Player"""

    #Function 1
    def next_move(self, board):
        """ that accepts a Board object b as a parameter and returns
            the column where the player wants to make the next move.
        """
        self.num_moves += 1 # increases num moves
        
        while True:
            
             #Random 
            lst = []
            for i in range(board.width): #checks each columns to get numbers
                if board.can_add_to(i) == True:
                    lst.append(i)
                    #print()
                elif board.is_full():
                    break
                else:
                    continue

            random_col = random.choice(lst)
            return random_col