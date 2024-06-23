import pygame as pg


class Knight:
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        if self.color == 'white':
            self.icon = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_knight.png'), 0.35)
        else:
            self.icon = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_knight.png'), 0.4)
        self.not_moved = True
        self.x = x
        self.y = y

    def can_move(self):
        return [(self.x+2, self.y+1), (self.x+2, self.y-1),
                (self.x-2, self.y+1), (self.x-2, self.y-1),
                (self.x+1, self.y+2), (self.x+1, self.y-2),
                (self.x-1, self.y+2), (self.x-1, self.y-2)]

    def can_see(self, board):
        tmp = []
        for move in self.can_move():
            if (0 <= move[0] <= 7 and 0 <= move[1] <= 7 and board[move[0]][move[1]].has_piece() and
                    board[move[0]][move[1]].get_piece().get_color() != self.color):
                tmp.append(move)
        return tmp

    def get_icon(self):
        return self.icon

    def set_moved(self):
        self.not_moved = False

    def get_color(self):
        return self.color

    def select_move(self, board):
        for tab in self.can_move():
            if 0 <= tab[0] <= 7 and 0 <= tab[1] <= 7:
                if board[tab[0]][tab[1]].has_piece() and board[tab[0]][tab[1]].get_piece().get_color() != self.color:
                    board[tab[0]][tab[1]].set_take_selection()
                elif not board[tab[0]][tab[1]].has_piece():
                    board[tab[0]][tab[1]].set_move_selection()

    def move(self, x, y):
        self.x = x
        self.y = y

