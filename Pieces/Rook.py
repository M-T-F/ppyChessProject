import pygame as pg
from Pieces import Piece


class Rook(Piece.Piece):
    icon_white = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_rook.png'), 0.35)
    icon_black = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_rook.png'), 0.4)


    @classmethod
    def cls_can_move(cls, x, y):
        tmp = []
        for i in range(0, x):
            tmp.append((i, y))
        for i in range(x+1, 8):
            tmp.append((i, y))
        for i in range(0, y):
            tmp.append((x, i))
        for i in range(y+1, 8):
            tmp.append((x, i))
        return tmp

    def can_move(self):
        tmp = []
        for i in range(0, self.x):
            tmp.append((i, self.y))
        for i in range(self.x+1, 8):
            tmp.append((i, self.y))
        for i in range(0, self.y):
            tmp.append((self.x, i))
        for i in range(self.y+1, 8):
            tmp.append((self.x, i))
        return tmp

    def can_see(self, board):
        tmp = []
        nmove = True
        emove = True
        smove = True
        wmove = True
        for t in range(1, 8):
            if (smove and self.x + t <= 7 and board[self.x + t, self.y].has_piece() and
                    board[self.x + t, self.y].get_piece().get_color() != self.color):
                tmp.append((self.x + t, self.y))
                smove = False

            if (nmove and self.x - t >= 0 and board[self.x - t, self.y].has_piece() and
                    board[self.x - t, self.y].get_piece().get_color() != self.color):
                tmp.append((self.x - t, self.y))
                nmove = False
            else:
                nmove = False

            if (emove and self.y + t <= 7 and board[self.x, self.y + t].has_piece() and
                    board[self.x, self.y + t].get_piece().get_color() != self.color):
                tmp.append((self.x, self.y + t))
                emove = False
            else:
                emove = False

            if (wmove and self.y - t >= 0 and board[self.x, self.y - t].has_piece() and
                    board[self.x, self.y - t].get_piece().get_color() != self.color):
                tmp.append((self.x, self.y - t))
                wmove = False
            else:
                wmove = False
        return tmp


    def select_move(self, board):
        nmove = True
        emove = True
        smove = True
        wmove = True
        for t in range(1,8):
            if smove and self.x+t <= 7 and not board[self.x+t, self.y].has_piece():
                board[self.x + t, self.y].set_move_selection()
            elif (smove and self.x+t <= 7 and board[self.x+t, self.y].has_piece()
                  and board[self.x+t, self.y].get_piece().get_color() != self.color):
                board[self.x + t, self.y].set_take_selection()
                smove = False
            else:
                smove = False

            if nmove and self.x-t >= 0 and not board[self.x-t, self.y].has_piece():
                board[self.x - t, self.y].set_move_selection()
            elif (nmove and self.x-t >= 0 and board[self.x-t, self.y].has_piece()
                  and board[self.x-t, self.y].get_piece().get_color() != self.color):
                board[self.x - t, self.y].set_take_selection()
                nmove = False
            else:
                nmove = False

            if emove and self.y + t <= 7 and not board[self.x, self.y + t].has_piece():
                board[self.x, self.y + t].set_move_selection()
            elif (emove and self.y + t <= 7 and board[self.x, self.y + t].has_piece()
                  and board[self.x, self.y + t].get_piece().get_color() != self.color):
                board[self.x, self.y + t].set_take_selection()
                emove = False
            else:
                emove = False

            if wmove and self.y - t >= 0 and not board[self.x, self.y - t].has_piece():
                board[self.x, self.y - t].set_move_selection()
            elif (wmove and self.y - t >= 0 and board[self.x, self.y - t].has_piece()
                  and board[self.x, self.y - t].get_piece().get_color() != self.color):
                board[self.x, self.y - t].set_take_selection()
                wmove = False
            else:
                wmove = False

