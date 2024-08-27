import numpy as np
import tensorflow as tf
import keras

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
        player = keras.Sequential()
        player.add(keras.Input(shape=(3, 3, 1))),
        player.add(keras.layers.Conv2D(1000, (3, 3))),
        player.add(keras.layers.Flatten()),
        player.add(keras.layers.Dense(100, activation='relu')),
        player.add(keras.layers.Dense(20, activation='relu')),
        player.add(keras.layers.Dense(9, activation='relu')),
        player.build()
        player.compile(
            optimizer=keras.optimizers.Adam(learning_rate=1e-3),
            run_eagerly=True,
            loss=keras.losses.MeanSquaredError(),
            )
        return player

    def GetMove(self, board):
        move_q_score = self.player.predict(
            np.expand_dims(board, 0).astype(float))[0]
        x, y = np.where(board == 0)
        idx = np.argsort(move_q_score[3*x + y])[::-1]
        move_list = (3*x + y)[idx]
        # p_func = np.sum(
        #     np.exp(-move_q_score/self.T))
        # move_proba = np.exp(-move_q_score/self.T) / p_func
        # cum_move_proba = np.cumsum(move_proba)
        # move_list = []
        # for i in range(9):
        #     n = int(np.argmax(cum_move_proba > np.random.rand()))
        #     move_list.append(n)
        #     move_proba[n] = 0
        #     if np.sum(move_proba) == 0:
        #         break
        #     move_proba = move_proba / np.sum(move_proba)
        #     cum_move_proba = np.cumsum(move_proba)
        return move_list
    