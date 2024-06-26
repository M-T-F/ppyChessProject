import pygame as pg
from Pieces import Piece


class Knight(Piece.Piece):
    icon_white = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_knight.png'), 0.35)
    icon_black = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_knight.png'), 0.4)


    def can_move(self):
        return [(self.x+2, self.y+1), (self.x+2, self.y-1),
                (self.x-2, self.y+1), (self.x-2, self.y-1),
                (self.x+1, self.y+2), (self.x+1, self.y-2),
                (self.x-1, self.y+2), (self.x-1, self.y-2)]

    def can_see(self, board=None):
        return self.can_move()

    def select_move(self, board):
        for move in self.can_move():
            if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                if (((board[move[0]][move[1]].has_piece()
                      and board[move[0]][move[1]].get_piece().get_color() != self.color)
                        or not board[move[0]][move[1]].has_piece())
                        and not self.is_pined_to_king(board, (self.x, self.y), move)):
                    board[move[0]][move[1]].set_move_selection()

    def would_see_king(self, board):
        return self.can_see(board)

    def would_see_king_after(self, board, index, move):
        return False

