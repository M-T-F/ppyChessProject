import pygame as pg


class Pawn:
    def __init__(self, color):
        super().__init__()
        self.color = color
        if self.color == 'white':
            self.icon = pg.transform.scale_by(pg.image.load('Pieces\icons\white_pawn.png'), 0.35)
        else:
            self.icon = pg.transform.scale_by(pg.image.load('Pieces\icons\\black_pawn.png'), 0.4)
        self.not_moved = True

    def can_move(self, y, x):
        if self.not_moved:
            if self.color == 'black':
                return [(y+1, x), (y+2, x)]
            else:
                return [(y-1, x), (y-2, x)]
        else:
            if self.color == 'black':
                return [(y+1, x)]
            else:
                return [(y-2, x)]

    def can_see(self, y, x):
        if self.color == 'white':
            return [(y+1, x+1), (y-1, x+1)]
        else:
            return [(y+1, x-1), (y-1, x-1)]

    def get_icon(self):
        return self.icon

    def sey_moved(self):
        self.not_moved = False