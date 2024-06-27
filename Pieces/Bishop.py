import pygame as pg

import Pieces.King
from Pieces import Piece


class Bishop(Piece.Piece):
    icon_white = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_bishop.png'), 0.35)
    icon_black = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_bishop.png'), 0.4)

    def can_see(self, board=None):
        tmp = []
        nemove = True
        semove = True
        swmove = True
        nwmove = True
        for t in range(1, 8):
            if (semove and 0 <= self.x + t <= 7 and 0 <= self.y + t <= 7
                    and not board[self.x + t, self.y + t].has_piece()):
                tmp.append((self.x + t, self.y + t))
            elif (semove and 0 <= self.x + t <= 7 and 0 <= self.y + t <= 7
                  and board[self.x + t, self.y + t].has_piece()
                  and board[self.x + t, self.y + t].get_piece().get_color() != self.color):
                tmp.append((self.x + t, self.y + t))
                semove = False
            else:
                semove = False

            if (swmove and 0 <= self.x + t <= 7 and 0 <= self.y - t <= 7
                    and not board[self.x + t, self.y - t].has_piece()):
                tmp.append((self.x + t, self.y - t))
            elif (swmove and 0 <= self.x + t <= 7 and 0 <= self.y - t <= 7
                  and board[self.x + t, self.y - t].has_piece()
                  and board[self.x + t, self.y - t].get_piece().get_color() != self.color):
                tmp.append((self.x + t, self.y - t))
                swmove = False
            else:
                swmove = False

            if (nemove and 0 <= self.x - t <= 7 and 0 <= self.y + t <= 7
                    and not board[self.x - t, self.y + t].has_piece()):
                tmp.append((self.x - t, self.y + t))
            elif (nemove and 0 <= self.x - t <= 7 and 0 <= self.y + t <= 7
                  and board[self.x - t, self.y + t].has_piece()
                  and board[self.x - t, self.y + t].get_piece().get_color() != self.color):
                tmp.append((self.x - t, self.y + t))
                nemove = False
            else:
                nemove = False

            if (nwmove and 0 <= self.x - t <= 7 and 0 <= self.y - t <= 7
                    and not board[self.x - t, self.y - t].has_piece()):
                tmp.append((self.x - t, self.y - t))
            elif (nwmove and 0 <= self.x - t <= 7 and 0 <= self.y - t <= 7
                  and board[self.x - t, self.y - t].has_piece()
                  and board[self.x - t, self.y - t].get_piece().get_color() != self.color):
                tmp.append((self.x - t, self.y - t))
                nwmove = False
            else:
                nwmove = False
        return tmp

    def select_move(self, board):
        for move in self.can_see(board):
            if not self.is_pined_to_king(board, (self.x, self.y), move):
                board[move[0], move[1]].set_move_selection()

    def would_see_king_after(self, board, index, move):
        if (self.x, self.y) == move:
            return False
        if (abs(move[0] - self.x) == abs(move[1] - self.y)
                and not type(board[index[0], index[1]].get_piece()) is Pieces.King.King):
            return False
        elif (abs(move[0] - self.x) == abs(move[1] - self.y)
            and type(board[index[0], index[1]].get_piece()) is Pieces.King.King):
            return True
        if index[0] < self.x:
            if index[1] < self.y:
                for t in range(1, 8):
                    if (index[0] - t >= 0 and index[1] - t >= 0
                            and board[index[0]-t, index[1]-t].has_piece()
                            and type(board[index[0]-t, index[1] - t].get_piece()) is Pieces.King.King
                            and board[index[0]-t, index[1]-t].get_piece().get_color() != self.color):
                        return True
                    elif (index[0] - t >= 0 and index[1] - t >= 0
                            and board[index[0]-t, index[1]-t].has_piece()
                            and not type(board[index[0] - t, index[1] - t].get_piece()) is Pieces.King.King):
                        return False
            elif index[1] > self.y:
                for t in range(1, 8):
                    if (index[0] - t >= 0 and index[1] + t < 8
                            and board[index[0] - t, index[1] + t].has_piece()
                            and type(board[index[0] - t, index[1] + t].get_piece()) is Pieces.King.King
                            and board[index[0] - t, index[1] + t].get_piece().get_color() != self.color):
                        return True
                    elif (index[0] - t >= 0 and index[1] + t < 8
                            and board[index[0] - t, index[1] + t].has_piece()
                            and not type(board[index[0] - t, index[1] + t].get_piece()) is Pieces.King.King):
                        return False
        elif index[0] > self.x:
            if index[1] < self.y:
                for t in range(1, 8):
                    if (index[0] + t < 8 and index[1] - t >= 0
                            and board[index[0]+t, index[1]-t].has_piece()
                            and type(board[index[0]+t, index[1] - t].get_piece()) is Pieces.King.King
                            and board[index[0]+t, index[1]-t].get_piece().get_color() != self.color):
                        return True
                    elif (index[0] + t < 8 and index[1] - t >= 0
                            and board[index[0]+t, index[1]-t].has_piece()
                            and not type(board[index[0] + t, index[1] - t].get_piece()) is Pieces.King.King):
                        return False
            elif index[1] > self.y:
                for t in range(1, 8):
                    if (index[0] + t < 8 and index[1] + t < 8
                            and board[index[0] + t, index[1] + t].has_piece()
                            and type(board[index[0] + t, index[1] + t].get_piece()) is Pieces.King.King
                            and board[index[0] + t, index[1] + t].get_piece().get_color() != self.color):
                        return True
                    elif (index[0] + t < 8 and index[1] + t < 8
                            and board[index[0] + t, index[1] + t].has_piece()
                            and not type(board[index[0] + t, index[1] + t].get_piece()) is Pieces.King.King):
                        return False




