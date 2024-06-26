import pygame as pg
from Pieces import Piece


class King(Piece.Piece):
    icon_white = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_king.png'), 0.35)
    icon_black = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_king.png'), 0.4)

    def __init__(self, color, x, y, enemies):
        super().__init__(color, x, y, enemies)
        self.alive = True

    def can_move(self):
        return [(self.x+1, self.y+1), (self.x+1, self.y-1),
                (self.x-1, self.y+1), (self.x-1, self.y-1),
                (self.x+1, self.y), (self.x, self.y-1),
                (self.x, self.y+1), (self.x-1, self.y)]

    def can_see(self, board=None):
        return self.can_move()

    def select_move(self, board):
        for tab in self.can_move():
            if 0 <= tab[0] <= 7 and 0 <= tab[1] <= 7:
                if not self.enemies_see(tab, board):
                    if ((board[tab[0]][tab[1]].has_piece() and board[tab[0]][tab[1]].get_piece().get_color() != self.color)
                            or not board[tab[0]][tab[1]].has_piece()):
                        board[tab[0]][tab[1]].set_move_selection()
        if self.not_moved:
            if (board[self.x, 7].has_piece() and board[self.x, 7].get_piece().get_not_moved() and
                    not self.enemies_see((self.x, 6), board)):
                if not board[self.x][6].has_piece() and not board[self.x][5].has_piece():
                    board[self.x][6].set_castle_selection()
            if (board[self.x, 0].has_piece() and board[self.x, 0].get_piece().get_not_moved() and
                    not self.enemies_see((self.x, 2), board)):
                if (not board[self.x][1].has_piece()
                        and not board[self.x][2].has_piece()
                        and not board[self.x][3].has_piece()):
                    board[self.x][2].set_castle_selection()

    def would_see_king(self, board):
        return self.can_see(board)

    def enemies_see(self, move, board):
        for enemy in self.enemies:
            if move in enemy.can_see(board):
                return True
        return False

    def get_cord(self):
        return (int(self.x), int(self.y))

    def kill(self):
        self.alive = False
    def is_alive(self):
        return self.alive

    def would_see_king_after(self, board, index, move):
        return False

