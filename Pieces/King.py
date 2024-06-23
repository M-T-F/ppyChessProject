import pygame as pg


class King:
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        if self.color == 'white':
            self.icon = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_king.png'), 0.35)
        else:
            self.icon = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_king.png'), 0.4)
        self.not_moved = True
        self.x = x
        self.y = y

    def can_move(self):
        return [(self.x+1, self.y+1), (self.x+1, self.y-1),
                (self.x-1, self.y+1), (self.x-1, self.y-1),
                (self.x+1, self.y), (self.x, self.y-1),
                (self.x, self.y+1), (self.x-1, self.y)]

    def can_see(self, x, y):
        return self.can_move(x, y)

    def get_icon(self):
        return self.icon

    def set_moved(self):
        self.not_moved = False

    def get_not_moved(self):
        return self.not_moved

    def get_color(self):
        return self.color

    def select_move(self, board):
        for tab in self.can_move():
            if 0 <= tab[0] <= 7 and 0 <= tab[1] <= 7:
                if board[tab[0]][tab[1]].has_piece() and board[tab[0]][tab[1]].get_piece().get_color() != self.color:
                    board[tab[0]][tab[1]].set_take_selection()
                elif not board[tab[0]][tab[1]].has_piece():
                    board[tab[0]][tab[1]].set_move_selection()
        if self.not_moved:
            if board[self.x, 7].get_piece().get_not_moved():
                if not board[self.x][6].has_piece() and not board[self.x][5].has_piece():
                    board[self.x][6].set_castle_selection()
            if board[self.x, 0].get_piece().get_not_moved():
                if (not board[self.x][1].has_piece()
                        and not board[self.x][2].has_piece()
                        and not board[self.x][3].has_piece()):
                    board[self.x][2].set_castle_selection()

    def move(self, x, y):
        self.x = x
        self.y = y

