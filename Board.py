import numpy as np
from Pieces import Pawn, Rook, Knight
from Field import Field


class Board:
    def __init__(self):
        self._board = np.array([[Field(x, y) for x in range(100, 500, 50)] for y in range(100, 500, 50)])
        self.selected = None
        for y in range(8):
            self.board[1, y].set_piece(Pawn.Pawn('black'))
            self.board[6, y].set_piece(Pawn.Pawn('white'))
            if y == 0 or y == 7:
                self.board[0, y].set_piece(Rook.Rook('black'))
                self.board[7, y].set_piece(Rook.Rook('white'))
            elif y == 1 or y == 6:
                self.board[0, y].set_piece(Knight.Knight('black'))
                self.board[7, y].set_piece(Knight.Knight('white'))


    @property
    def board(self):
        return self._board

    def move(self, s, tx, ty):
        self.board[s[0], s[1]].get_piece().set_moved()
        self.board[tx, ty].set_piece(self.board[s[0], s[1]].get_piece())
        self.board[s[0], s[1]].set_piece(None)
        self.unselect()

    def select_move(self, selected):
        self.board[selected[0], selected[1]].get_piece().select_move(self.board, selected)
        #can_see = self.board[selected].can_see()

    def unselect(self):
        for x in self.board:
            for y in x:
                y.set_selection(False)

    def can_move(self, x, y):
        return self.board[x,y].cen_move()
