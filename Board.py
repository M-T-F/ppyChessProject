import numpy as np
import pandas as pd
import sys
import pygame as pg
from Field import Field


class Board:
    def __init__(self):
        self._board = np.array([[Field(x, y) for x in range(100, 500, 50)] for y in range(100, 500, 50)])
        #print(mac)
         #= pd.DataFrame(mac, ["a", "b", "c", "d", "e", "f", "g", "h"])
        #print(self.board)

    @property
    def board(self):
        return self._board
