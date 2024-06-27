import pygame as pg
from Pieces import Piece


class Pawn(Piece.Piece):
    icon_white = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_pawn.png'), 0.35)
    icon_black = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_pawn.png'), 0.4)

    def can_see(self, board=None):
        if self.color == 'black':
            return [(self.x+1, self.y+1), (self.x+1, self.y-1)]
        else:
            return [(self.x-1, self.y+1), (self.x-1, self.y-1)]

    def select_move(self, board):
        if self.not_moved:
            tmp = True
            for t in range(1,3):
                if self.color == 'black':
                    if (not board[self.x+t, self.y].has_piece() and tmp
                            and not self.is_pined_to_king(board, (self.x, self.y), (self.x+t, self.y))):
                        board[self.x+t, self.y].set_move_selection()
                    else:
                        tmp = False
                else:
                    if (not board[self.x-t, self.y].has_piece() and tmp
                            and not self.is_pined_to_king(board, (self.x, self.y), (self.x-t, self.y))):
                        board[self.x-t, self.y].set_move_selection()
                    else:
                        tmp = False
        else:
            if self.color == 'black':
                if (not board[self.x+1, self.y].has_piece()
                        and not self.is_pined_to_king(board, (self.x, self.y), (self.x+1, self.y))):
                    board[self.x + 1, self.y].set_move_selection()
            else:
                if (not board[self.x - 1, self.y].has_piece()
                        and not self.is_pined_to_king(board, (self.x, self.y), (self.x-1, self.y))):
                    board[self.x - 1, self.y].set_move_selection()
        for see in self.can_see():
            if 0 <= see[1] <= 7:
                if (board[see[0], see[1]].has_piece() and board[see[0], see[1]].get_piece().get_color() != self.color
                        and not self.is_pined_to_king(board, (self.x, self.y), see)):
                    board[see[0], see[1]].set_move_selection()

    def would_see_king_after(self, board, index, move):
        return False




