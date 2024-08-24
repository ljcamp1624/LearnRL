# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:24:06 2024

@author: nicho
"""
import numpy as np
class Player(object):
    def __init__(self):
        return self
    
    def action(self,boardState):
        
    def move(self,boardState):
        # boardState is a numpy array of 1, -1
        emptySpots=[]
        for ii in range(3):
            for jj in range(3):
                if boardState[ii,jj]==0:
                    emptySpots.append((ii,jj))
        randIdx = np.random.randint(0,len(emptySpots))
        boardState[emptySpots[randIdx]]=1