# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 20:44:32 2024

@author: Lenny
"""

#%% Set up player
from player import *
from tictactoe import *

#%% Collect data

import numpy as np

def RunGame(player):
    game=TicTacToe()
    
    # play the game and store the moves
    data = []
    moves = 0
    while not game.game_over:
        b = np.array(game.board)
        p = int(game.next_player)
        move = player.GetMove(game.board)
        valid = False
        for m in move:
            pos = [m // 3, m % 3]
            valid = game.MakeMove(pos)
            if valid:
                moves +=1
                break
        if (moves > 9) or not valid:
            return []
        data.append([b, m, p])
        
    # assert the outcome
    for i, d in enumerate(data[:-2]):
        vec = np.zeros((9, 1))
        data[i].append(vec)
        
    vec = np.zeros((9, 1))
    vec[data[-2][1]] = -1
    data[-2].append(vec)
    
    vec = np.zeros((9, 1))
    vec[data[-1][1]] = 1
    data[-1].append(vec)
        
    return data


def RunGameTrials(player, num_games=1):
    data = []
    for t in range(num_games):
        data += RunGame(player)
    return data


def ExtractTrainingData(game_data):
    # symmetry idx
    lr_idx = [2,1,0,5,4,3,8,7,6]
    ud_idx = [6,7,8,3,4,5,0,1,2]
    diag_idx = [0,3,6,1,4,7,2,5,8]
    odiag_idx = [8,5,2,7,4,1,6,3,0]
    x = []
    y = []
    for v in game_data:
        b = v[0]
        t = v[3]
        x.append(b)
        x.append(np.fliplr(b))
        x.append(np.flipud(b))
        y.append(t)
        y.append(t[lr_idx])
        y.append(t[ud_idx])
    return np.array(x), np.array(y)
    

def RunTraining(player, num_games=1, num_repeats=1, drop_rate=0.0):
    player.mode = 'Play'
    game_data = RunGameTrials(player, num_games)
    board_positions, move_outcomes = ExtractTrainingData(game_data)
    player.player.fit(
        board_positions,
        move_outcomes,
        batch_size = 50,
        epochs = 50,
        validation_split = 0.25,
        )

#%% Train the machine
player = Player()
for i in range(10):
    RunTraining(player, num_games=10)

#%% Play the machine
player.mode = 'Play'
game = TicTacToe()
while not game.game_over:
    game.PrintBoard()
    move = input()
    game.MakeMove(eval(move))
    move = player.GetMove(game.board)
    valid = False
    for m in move:
        pos = [m // 3, m % 3]
        valid = game.MakeMove(pos)
        if valid:
            break