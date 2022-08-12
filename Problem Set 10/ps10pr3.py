#
# ps10pr3.py (Problem Set 10, Problem 3)
#
# Playing the game
#
# File: ps10pr3.py
# Author: Wadner Simon (casseus@bu.edu), 8/822
# Description: Process Moves of Players

from ps10pr1 import Board
from ps10pr2 import Player
import random



#Function 1
def process_move(p,b):
    """Runs the Move Based on the the two objects p and b"""

    checker = p.checker #checker intialization
    move = p.next_move(b) # finds move
    b.add_checker(checker, move) #adds a checker on Board

    print() #print Blank Line
    print(b) #print Board Objects
    
    if b.is_win_for(checker): #Checks if its a Win
        print('Player X wins in 8 moves.Congratulations!')
        return True

    elif b.is_full(): # Checks if its a Tie
        print("It's a tie!")
        return True

    else: # Returns False if Loss
        return False


#Function 2
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board
