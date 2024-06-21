import pygame as pg


class Knight:
    def __init__(self, color):
        super().__init__()
        self.color = color
        if self.color == 'white':
            self.icon = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_knight.png'), 0.35)
        else:
            self.icon = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_knight.png'), 0.4)
        self.not_moved = True

    def can_move(self, x, y):
        return [(x+2, y+1), (x+2, y-1),
                (x-2, y+1), (x-2, y-1),
                (x+1, y+2), (x+1, y-2),
                (x-1, y+2), (x-1, y-2)]

    def can_see(self, x, y):
        return self.can_move(x, y)

    def get_icon(self):
        return self.icon

    def set_moved(self):
        self.not_moved = False

    def get_color(self):
        return self.color

    def select_move(self, board, selected):
        for tab in self.can_move(selected[0], selected[1]):
            if 0 <= tab[0] <= 7 and 0 <= tab[1] <= 7:
                if board[tab[0]][tab[1]].has_piece() and board[tab[0]][tab[1]].get_piece().get_color() != self.color:
                    board[tab[0]][tab[1]].set_take_selection()
                elif not board[tab[0]][tab[1]].has_piece():
                    board[tab[0]][tab[1]].set_move_selection()
