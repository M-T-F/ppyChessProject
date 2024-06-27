import pygame as pg
from Pieces import Piece


class King(Piece.Piece):
    icon_white = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_king.png'), 0.35)
    icon_black = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_king.png'), 0.4)

    def __init__(self, color, x, y, enemies):
        super().__init__(color, x, y, enemies)
        self.alive = True

    def can_see(self, board=None):
        return [(self.x+1, self.y+1), (self.x+1, self.y-1),
                (self.x-1, self.y+1), (self.x-1, self.y-1),
                (self.x+1, self.y), (self.x, self.y-1),
                (self.x, self.y+1), (self.x-1, self.y)]

    def select_move(self, board):
        for move in self.can_see():
            if 0 <= move[0] <= 7 and 0 <= move[1] <= 7:
                if not self.enemies_see(move, board):
                    if (((board[move[0]][move[1]].has_piece() and
                        board[move[0]][move[1]].get_piece().get_color() != self.color)
                            or not board[move[0]][move[1]].has_piece())
                            and not self.is_pined_to_king(board, (self.x, self.y), move)):
                        board[move[0]][move[1]].set_move_selection()
        if self.not_moved:
            if (board[self.x, 7].has_piece() and board[self.x, 7].get_piece().get_not_moved() and
                    not self.enemies_see((self.x, 6), board)):
                if not board[self.x][6].has_piece() and not board[self.x][5].has_piece():
                    board[self.x][6].set_move_selection()
            if (board[self.x, 0].has_piece() and board[self.x, 0].get_piece().get_not_moved() and
                    not self.enemies_see((self.x, 2), board)):
                if (not board[self.x][1].has_piece()
                        and not board[self.x][2].has_piece()
                        and not board[self.x][3].has_piece()):
                    board[self.x][2].set_move_selection()

    def enemies_see(self, move, board):
        """ metoda zwraca True jeśli pole move jest w zasięgu wzroku wrogiej figury"""
        for enemy in self.enemies:
            if move in enemy.can_see(board):
                return True
        return False

    def get_cord(self):
        """ zwraca współrzędne króla na planszy"""
        return int(self.x), int(self.y)

    def kill(self):
        """ metoda zabijająca króla"""
        self.alive = False

    def is_alive(self):
        """ metoda zwracająca to czy król jest żywy"""
        return self.alive

    def would_see_king_after(self, board, index, move):
        return False

