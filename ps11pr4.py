#
# ps11pr4.py (Problem Set 11, Problem 4)
#
# An AI Player for use in Connect Four
#



# File: ps11pr4.py
# Author: Wadner Simon , 8/12/22
# Description: Creating AI player of connect 4

import random
from ps10pr3 import * # to use the connect_four and process_move functions

class AIPlayer(Player):
    """Creates an AI player"""
    
    #Method 1
    def __init__(self, checker, tiebreak, lookahead):
        """__init__(self, checker, tiebreak, lookahead) that constructs 
            a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    #Method 2
    def __repr__(self):
        """ that returns a string representing an AIPlayer object."""
        return 'Player ' + self.checker + ' (' +self.tiebreak +', ' + str(self.lookahead) + ')'
    
    #Method 3
    def max_score_column(self,scores):
        """max_score_column(self, scores) takes a list 
            scores containing a score for each column of the board, and that 
            returns the index of the column with the maximum score. 
        """
        max_score = max(scores)
        
        lst = []
        
        for i in range(len(scores)):
            if scores[i] == max_score:
                lst.append(i)
            else:
                continue
        
        if self.tiebreak == "LEFT":
            return lst[0]
        elif self.tiebreak == "RIGHT":
            return lst[-1]
        else:
            return random.choice(lst)
        
        
    #Method 4
    def scores_for(self, board):
        """scores_for(self, board) that takes a Board object 
            board and determines the called AIPlayer‘s scores for the columns in board. 
        """
        scores = [50] * board.width 
        for col in range(board.width):
            if not board.can_add_to(col): #full
                scores[col] = -1
                
            elif board.is_win_for(self.checker): #Is win for AI
                scores[col] = 100
               # print('C',col, "win checker", scores[col])
                
            elif board.is_win_for(self.opponent_checker()) == True: #Is loss for AI
                
                scores[col] = 0
                #print('B',col, "win opponent", scores[col])
                
                
            elif self.lookahead == 0:
                scores[col] == 50
                #print('A',col, "lookahead 0", scores[col])
            else:
                board.add_checker(self.checker,col) #checker added at col
                opponent = AIPlayer(self.opponent_checker(),self.tiebreak, self.lookahead-1)
                # opponent created 
                opp_scores = opponent.scores_for(board)
                #scores[col] = opp_scores[opponent.max_score_column(opp_scores)]
                if max(opp_scores) == 100: #win of oppoennt
                    scores[col] = 0  # ai won't go there
                elif max(opp_scores) == 0:#loss of opponent
                    scores[col] = 100 # ai will go there
                elif max(opp_scores) == 50: #nothing
                    scores[col] = 50 #nothion
                
                    
               # print(scores[col])
                board.remove_checker(col)
                
        return scores
    
    #Method 5
    def next_move(self, board):
        """next_move(self, board) overrides (i.e., replaces) the next_move 
            method that is inherited from Player
        """
        
        self.num_moves += 1 # incrementing
        scores = self.scores_for(board) # calling scores_for function for the current board
        return self.max_score_column(scores) # max score of scores 
    
    






            
        
        
        
    
