import pygame as pg

import Pieces.King
from Pieces import Rook, Bishop,Piece


class Queen(Rook.Rook, Bishop.Bishop):
    icon_white = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_queen.png'), 0.35)
    icon_black = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_queen.png'), 0.4)

    def can_see(self, board=None):

        tmp = Rook.Rook.can_see(self, board)
        for move in Bishop.Bishop.can_see(self, board):
            tmp.append(move)
        return tmp

    def select_move(self, board):
        for move in self.can_see(board):
            if not self.is_pined_to_king(board, (self.x, self.y), move):
                board[move[0], move[1]].set_move_selection()

    def would_see_king_after(self, board, index, move):
        return (Rook.Rook.would_see_king_after(self,board, index, move)
                or Bishop.Bishop.would_see_king_after(self, board, index, move))

