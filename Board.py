import numpy as np
from Pieces import Pawn
from Field import Field


class Board:
    def __init__(self):
        self._board = np.array([[Field(x, y) for x in range(100, 500, 50)] for y in range(100, 500, 50)])
        for y in range(8):
            self.board[1, y].set_piece(Pawn.Pawn('black'))
            self.board[6, y].set_piece(Pawn.Pawn('white'))

    @property
    def board(self):
        return self._board

    def move(self, s, tx, ty):
        self.board[s[0], s[1]].get_piece().sey_moved()
        self.board[tx, ty].set_piece(self.board[s[0], s[1]].get_piece())
        self.board[s[0], s[1]].set_piece(None)


