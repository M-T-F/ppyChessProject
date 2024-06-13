import pygame as pg


class Field(pg.rect.RectType):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.piece = None

    def has_piece(self):
        return self.piece is not None

    def set_piece(self, piece):
        self.piece = piece
