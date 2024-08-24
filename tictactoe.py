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
        for i in range(3):
            if all(self.board[i,:])==1 or all(self.board[:,i])==1:
                self.game_over=True
        if all(np.diag(self.board))==1  or all(np.diag(np.fliplr(self.board)))==1:
            self.game_over=True
                
    def MakeMove(self, pos):
        # make the move in pos, update the board and next_player
        X= self.avaiableSpots()
        Y = [3*a+b for (a,b) in zip(X[0],X[1])]
        pos_Index = 3*pos[0]+pos[1]
        if pos_Index==any(Y):
            self.board[pos[0],pos[1]]=1
            if self.next_player==1:
                self.next_player=2
            else:
                self.next_player=1
        else:
            return 0
        
    def avaiableSpots(self):
        return np.where(self.board==0)
        

    def update(self,learningParams):
        if not self.game_over:
            self.MakeMove(self.board)
            self.board = -1*self.board
            

    