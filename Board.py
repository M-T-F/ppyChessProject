import numpy as np
from Pieces import Pawn, Rook, Knight, Bishop, Queen, King
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
            elif y == 2 or y == 5:
                self.board[0, y].set_piece(Bishop.Bishop('black'))
                self.board[7, y].set_piece(Bishop.Bishop('white'))
            elif y == 3:
                self.board[0, y].set_piece(Queen.Queen('black'))
                self.board[7, y].set_piece(Queen.Queen('white'))
            elif y == 4:
                self.board[0, y].set_piece(King.King('black'))
                self.board[7, y].set_piece(King.King('white'))


    @property
    def board(self):
        return self._board

    def move(self, s, tx, ty):
        self.board[s[0], s[1]].get_piece().set_moved()
        self.board[tx, ty].set_piece(self.board[s[0], s[1]].get_piece())
        self.board[s[0], s[1]].set_piece(None)
        self.unselect()

    def castle(self, s, tx, ty):
        self.board[s[0], s[1]].get_piece().set_moved()
        self.board[tx, ty].set_piece(self.board[s[0], s[1]].get_piece())
        self.board[s[0], s[1]].set_piece(None)
        if ty == 6:
            self.board[tx, 5].set_piece(self.board[tx, 7].get_piece())
            self.board[tx, 7].set_piece(None)
            self.board[tx, 5].get_piece().set_moved()
        elif ty == 2:
            self.board[tx, 3].set_piece(self.board[tx, 0].get_piece())
            self.board[tx, 0].set_piece(None)
            self.board[tx, 3].get_piece().set_moved()
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
