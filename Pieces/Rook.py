import pygame as pg

import Pieces.King
from Pieces import Piece


class Rook(Piece.Piece):
    icon_white = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_rook.png'), 0.35)
    icon_black = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_rook.png'), 0.4)

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

    def would_see_king_after(self, board, index, move):
        if (self.x, self.y) == move:
            return False
        if index[0] == self.x:
            if index[0] == move[0] and not type(board[index[0], index[1]].get_piece()) is Pieces.King.King:
                return False
            elif index[0] == move[0] and type(board[index[0], index[1]].get_piece()) is Pieces.King.King:
                return True
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
            if index[1] == move[1] and not type(board[index[0], index[1]].get_piece()) is Pieces.King.King:
                return False
            elif index[1] == move[1] and type(board[index[0], index[1]].get_piece()) is Pieces.King.King:
                return True
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
