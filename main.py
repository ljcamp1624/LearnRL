# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 20:44:32 2024

@author: Lenny
"""

#%% Start game
player = Player()

import numpy as np

def RunGame():
    game=TicTacToe()
    
    # play the game and store the moves
    data = []
    while not game.game_over:
        b = np.array(game.board)
        p = int(game.next_player)
        move = player.GetMove(game.board)
        for m in move:
            pos = [m // 3, m % 3]
            valid = game.MakeMove(pos)
            if valid:
                break
        data.append([b, m, p])
        
    # assert the outcome
    for i, d in enumerate(data):
        vec = np.zeros((9, 1)) + 0.5        
        if d[2] == game.outcome:
            vec[d[1]] = 1
        elif game.outcome != 0.5:
            vec[d[1]] = 0
        data[i].append(vec)
        
    return data


def RunTrials(trials=1):
    data = []
    for t in range(trials):
        data += RunGame()
    return data
    
    
    
    
x = RunTrials(1)
