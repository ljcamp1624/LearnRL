# -*- coding: utf-8 -*-

import numpy as np

class TicTacToe():


    def __init__(self):
        self.next_player = 0
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
        print(b, self.board)
        
        
    def CheckGame(self):
        # check if the game is over
        if np.any((self.board == 1).sum(axis=0) == 3):
            self.game_over=True
        elif np.any((self.board == 1).sum(axis=1) == 3):
            self.game_over=True
        elif np.sum(np.diag(self.board) == 1) == 3:
            self.game_over=True
        elif np.sum(np.diag(np.fliplr(self.board)) == 1) == 3:
            self.game_over=True
                
            
    def MakeMove(self, pos):
        # make the move in pos, update the board and next_player
        X = np.where(self.board==0)
        Y = [3*a+b for (a,b) in zip(X[0],X[1])]
        pos_Index = 3*pos[0]+pos[1]
        if pos_Index in Y:
            self.board[pos[0],pos[1]]=1
            self.CheckGame()
            self.Update()


    def Update(self):
        if not self.game_over:
            self.next_player = (self.next_player + 1)  % 2
            self.board = -1*self.board