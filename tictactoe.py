# -*- coding: utf-8 -*-



class TicTacToe():
    
    import numpy as np
    
    def __init__(self):
        self.next_player = 1
        self.game_over = False
        self.board = np.zeros((3,3))
        
    def PrintBoard(self):
        b = ''
        for i in range(3):
            for j in range(3):
                spot = self.board[i, j]
                if spot == 0:
                    b += '   '
                elif spot == 1:
                    b += ' x '
                elif spot == -1:
                    b += ' o '
                if j < 2:
                    b += '|'
            b += '\n'
            if i < 2:
                b += 11*'_' + '\n'
        print(b)
        
    def CheckGame(self):
        # check if the game is over
        return False
                
    def MakeMove(self, pos):
        # make the move in pos, update the board and next_player
        
    