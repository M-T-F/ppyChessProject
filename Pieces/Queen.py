import pygame as pg
from Pieces import Rook, Bishop,Piece


class Queen(Piece.Piece):
    icon_white = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_queen.png'), 0.35)
    icon_black = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_queen.png'), 0.4)


    def can_move(self):
        tmp = Rook.Rook.cls_can_move(self.x, self.y)
        for move in Bishop.Bishop.cls_can_move(self.x, self.y):
            tmp.append(move)
        return tmp

    def can_see(self, board):
        tmp = []
        nmove = True
        emove = True
        smove = True
        wmove = True
        for t in range(1, 8):
            if (smove and self.x+ t <= 7 and board[self.x + t, self.y].has_piece() and
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
            nemove = True
            semove = True
            swmove = True
            nwmove = True
            for t in range(1, 8):
                if (semove and 0 <= self.x + t <= 7 and 0 <= self.y + t <= 7
                        and board[self.x + t, self.y + t].has_piece()
                        and board[self.x + t, self.y + t].get_piece().get_color() != self.color):
                    tmp.append((self.x + t, self.y + t))
                    semove = False
                else:
                    semove = False

                if (swmove and 0 <= self.x + t <= 7 and 0 <= self.y - t <= 7
                        and board[self.x + t, self.y - t].has_piece()
                        and board[self.x + t, self.y - t].get_piece().get_color() != self.color):
                    tmp.append((self.x + t, self.y - t))
                    swmove = False
                else:
                    swmove = False

                if (nemove and 0 <= self.x - t <= 7 and 0 <= self.y + t <= 7
                        and board[self.x - t, self.y + t].has_piece()
                        and board[self.x - t, self.y + t].get_piece().get_color() != self.color):
                    tmp.append((self.x - t, self.y + t))
                    nemove = False
                else:
                    nemove = False

                if (nwmove and 0 <= self.x - t <= 7 and 0 <= self.y - t <= 7
                        and board[self.x - t, self.y - t].has_piece()
                        and board[self.x - t, self.y - t].get_piece().get_color() != self.color):
                    tmp.append((self.x - t, self.y - t))
                    nwmove = False
                else:
                    nwmove = False
        return tmp

    def select_move(self, board):
        nemove = True
        semove = True
        swmove = True
        nwmove = True
        for t in range(1, 8):
            if (semove and 0 <= self.x + t <= 7 and 0 <= self.y + t <= 7
                    and not board[self.x + t, self.y + t].has_piece()):
                board[self.x + t, self.y + t].set_move_selection()
            elif (semove and 0 <= self.x + t <= 7 and 0 <= self.y + t <= 7
                  and board[self.x + t, self.y + t].has_piece()
                  and board[self.x + t, self.y + t].get_piece().get_color() != self.color):
                board[self.x + t, self.y + t].set_take_selection()
                semove = False
            else:
                semove = False

            if (swmove and 0 <= self.x + t <= 7 and 0 <= self.y - t <= 7
                    and not board[self.x + t, self.y - t].has_piece()):
                board[self.x + t, self.y - t].set_move_selection()
            elif (swmove and 0 <= self.x + t <= 7 and 0 <= self.y - t <= 7
                  and board[self.x + t, self.y - t].has_piece()
                  and board[self.x + t, self.y - t].get_piece().get_color() != self.color):
                board[self.x + t, self.y - t].set_take_selection()
                swmove = False
            else:
                swmove = False

            if (nemove and 0 <= self.x - t <= 7 and 0 <= self.y + t <= 7
                    and not board[self.x - t, self.y + t].has_piece()):
                board[self.x - t, self.y + t].set_move_selection()
            elif (nemove and 0 <= self.x - t <= 7 and 0 <= self.y + t <= 7
                  and board[self.x - t, self.y + t].has_piece()
                  and board[self.x - t, self.y + t].get_piece().get_color() != self.color):
                board[self.x - t, self.y + t].set_take_selection()
                nemove = False
            else:
                nemove = False

            if (nwmove and 0 <= self.x - t <= 7 and 0 <= self.y - t <= 7
                    and not board[self.x - t, self.y - t].has_piece()):
                board[self.x - t, self.y - t].set_move_selection()
            elif (nwmove and 0 <= self.x - t <= 7 and 0 <= self.y - t <= 7
                  and board[self.x - t, self.y - t].has_piece()
                  and board[self.x - t, self.y - t].get_piece().get_color() != self.color):
                board[self.x - t, self.y - t].set_take_selection()
                nwmove = False
            else:
                nwmove = False
        nmove = True
        emove = True
        smove = True
        wmove = True
        for t in range(1, 8):
            if smove and self.x + t <= 7 and not board[self.x + t, self.y].has_piece():
                board[self.x + t, self.y].set_move_selection()
            elif (smove and self.x + t <= 7 and board[self.x + t, self.y].has_piece()
                  and board[self.x + t, self.y].get_piece().get_color() != self.color):
                board[self.x + t, self.y].set_take_selection()
                smove = False
            else:
                smove = False

            if nmove and self.x - t >= 0 and not board[self.x - t, self.y].has_piece():
                board[self.x - t, self.y].set_move_selection()
            elif (nmove and self.x - t >= 0 and board[self.x - t, self.y].has_piece()
                  and board[self.x - t, self.y].get_piece().get_color() != self.color):
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

