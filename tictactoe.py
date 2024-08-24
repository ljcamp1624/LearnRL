# -*- coding: utf-8 -*-

import numpy as np

class TicTacToe():
    
    import numpy as np
    
    def __init__(self):
        self.next_player = 1 # 1 or 2
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
        spots = self.avaiableSpots(pos)
        emptySpots = len(spots[0])
        randIdx = np.random.randint(0,emptySpots)
        pos[spots[0][randIdx],spots[1][randIdx]]=1
        if self.next_player==1:
            self.next_player=2
        else:
            self.next_player=1
        
    def avaiableSpots(self,pos):
        return np.where(pos==0)
        
    def update(self,learningParams):
        if not self.CheckGame():
            self.MakeMove(self.board)
            self.board = -1*self.board
            

    