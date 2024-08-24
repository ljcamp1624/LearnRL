# -*- coding: utf-8 -*-

class Player():
    
    def __init__(self, player=None, mode='Training'):
        if player is None:
            self.player = self.InitializePlayerModel()
        else:
            self.player = player
        if mode == 'Training':
            self.T = 2
        elif mode == 'Play':
            self.T = 0.01
        
    def InitializePlayerModel(self):
        import tensorflow as tf
        import keras
        player = keras.Sequential()
        player.add(keras.Input(shape=(3, 3, 1))),
        player.add(keras.layers.Conv2D(1000, (3, 3))),
        player.add(keras.layers.Flatten()),
        player.add(keras.layers.Dense(100, activation='relu')),
        player.add(keras.layers.Dense(100, activation='relu')),
        player.add(keras.layers.Dense(9, activation='sigmoid')),
        player.build()
        player.compile(
            optimizer=keras.optimizers.Adam(learning_rate=1e-3),
            run_eagerly=True,
            )
        return player

    def GetMove(self, board):
        import numpy as np
        move = self.player.predict(np.expand_dims(board, 0).astype(float))[0]
        p_func = np.sum(np.exp(-move/self.T))
        move_proba = np.exp(-move/self.T) / p_func
        cum_move_proba = np.cumsum(move_proba)
        move_list = []
        for i in range(9):
            n = np.argmax(cum_move_proba > np.random.rand())
            move_proba[n] = 0
            cum_move_proba = np.cumsum(move_proba)
            move_list.append(n)
            if np.any(np.isnan(m2c)):
                break
        return move_list
    