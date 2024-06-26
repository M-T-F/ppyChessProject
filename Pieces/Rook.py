import pygame as pg

import Pieces.King
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
        return self.cls_can_move(self.x, self.y)

    def can_see(self, board=None):
        tmp = []
        nmove = True
        emove = True
        smove = True
        wmove = True
        for t in range(1, 8):
            if smove and self.x + t <= 7 and not board[self.x + t, self.y].has_piece():
                tmp.append((self.x + t, self.y))
            elif (smove and self.x + t <= 7 and board[self.x + t, self.y].has_piece() and
                    board[self.x + t, self.y].get_piece().get_color() != self.color):
                tmp.append((self.x + t, self.y))
                smove = False
            else:
                smove = False

            if nmove and self.x - t >= 0 and not board[self.x - t, self.y].has_piece():
                tmp.append((self.x - t, self.y))
            elif (nmove and self.x - t >= 0 and board[self.x - t, self.y].has_piece() and
                    board[self.x - t, self.y].get_piece().get_color() != self.color):
                tmp.append((self.x - t, self.y))
                nmove = False
            else:
                nmove = False

            if emove and self.y + t <= 7 and not board[self.x, self.y + t].has_piece():
                tmp.append((self.x, self.y + t))
            elif (emove and self.y + t <= 7 and board[self.x, self.y + t].has_piece() and
                    board[self.x, self.y + t].get_piece().get_color() != self.color):
                tmp.append((self.x, self.y + t))
                emove = False
            else:
                emove = False

            if wmove and self.y - t >= 0 and not board[self.x, self.y - t].has_piece():
                tmp.append((self.x, self.y - t))
            elif (wmove and self.y - t >= 0 and board[self.x, self.y - t].has_piece() and
                    board[self.x, self.y - t].get_piece().get_color() != self.color):
                tmp.append((self.x, self.y - t))
                wmove = False
            else:
                wmove = False

        return tmp

    def select_move(self, board):
        for move in self.can_see(board):
            if not self.is_pined_to_king(board, (self.x, self.y), move):
                board[move[0], move[1]].set_move_selection()

    def would_see_king(self, board):
        tmp = []
        nmove = True
        nsee = True
        emove = True
        esee = True
        smove = True
        ssee = True
        wmove = True
        wsee = True
        for t in range(1, 8):
            if (smove and self.x + t <= 7 and board[self.x + t, self.y].has_piece()
                  and board[self.x + t, self.y].get_piece().get_color() != self.color):
                smove = False
            elif (ssee and self.x + t <= 7 and board[self.x + t, self.y].has_piece()
                  and board[self.x + t, self.y].get_piece().get_color() != self.color
                  and type(board[self.x + t, self.y].get_piece()) is Pieces.King.King):
                tmp.append((self.x + t, self.y))
                ssee = False

            if (nmove and self.x - t >= 0 and board[self.x - t, self.y].has_piece()
                  and board[self.x - t, self.y].get_piece().get_color() != self.color):
                nmove = False
            elif (nsee and self.x - t >= 0 and board[self.x - t, self.y].has_piece()
                  and board[self.x - t, self.y].get_piece().get_color() != self.color
                  and type(board[self.x - t, self.y].get_piece()) is Pieces.King.King):
                tmp.append((self.x - t, self.y))
                nsee = False

            if (emove and self.y + t <= 7 and board[self.x, self.y + t].has_piece()
                  and board[self.x, self.y + t].get_piece().get_color() != self.color):
                emove = False
            elif (esee and self.y + t <= 7 and board[self.x, self.y + t].has_piece()
                  and board[self.x, self.y + t].get_piece().get_color() != self.color
                  and type(board[self.x, self.y + t].get_piece()) is Pieces.King.King):
                tmp.append((self.x, self.y + t))
                esee = False

            if (wmove and self.y - t >= 0 and board[self.x, self.y - t].has_piece()
                  and board[self.x, self.y - t].get_piece().get_color() != self.color):
                wmove = False
            elif (wsee and self.y - t >= 0 and board[self.x, self.y - t].has_piece()
                  and board[self.x, self.y - t].get_piece().get_color() != self.color
                  and type(board[self.x, self.y - t].get_piece()) is Pieces.King.King):
                tmp.append((self.x, self.y - t))
                wsee = False

        return tmp

    def would_see_king_after(self, board, index, move):
        if index[0] == self.x:
            if index[0] == move[0]:
                return False
            if index[1] > self.y:
                for t in range(index[1] + 1,8):
                    if (board[index[0], t].has_piece()
                            and type(board[index[0], t].get_piece()) is Pieces.King.King
                            and board[index[0], t].get_piece().get_color() != self.color):
                        return True
                    elif (board[index[0], t].has_piece()
                            and not type(board[index[0], t].get_piece()) is Pieces.King.King):
                        return False
            else:
                for t in range(index[1]-1, -1, -1):
                    if (board[index[0], t].has_piece()
                            and type(board[index[0], t].get_piece()) is Pieces.King.King
                            and board[index[0], t].get_piece().get_color() != self.color):
                        return True
                    elif (board[index[0], t].has_piece()
                            and not type(board[index[0], t].get_piece()) is Pieces.King.King):
                        return False
        elif index[1] == self.y:
            if index[1] == move[1]:
                return False
            if index[0] > self.x:
                for t in range(index[0]+1,8):
                    if (board[t, index[1]].has_piece()
                            and type(board[t, index[1]].get_piece()) is Pieces.King.King
                            and board[t, index[1]].get_piece().get_color() != self.color):
                        return True
                    elif (board[t, index[1]].has_piece()
                            and not type(board[t, index[1]].get_piece()) is Pieces.King.King):
                        return False
            else:
                for t in range(index[0]-1, -1, -1):
                    if (board[t, index[1]].has_piece()
                            and type(board[t, index[1]].get_piece()) is Pieces.King.King
                            and board[t, index[1]].get_piece().get_color() != self.color):
                        return True
                    elif (board[t, index[1]].has_piece()
                            and not type(board[t, index[1]].get_piece()) is Pieces.King.King):
                        return False
