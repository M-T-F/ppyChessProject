import pygame as pg


class Field:
    def __init__(self, x, y, width=50, height=50):
        self.rect = pg.Rect(x, y, width, height)
        self.piece = None

    def has_piece(self):
        return self.piece is not None

    def set_piece(self, piece):
        self.piece = piece

    def get_piece(self):
        return self.piece

    def get_rect(self):
        return self.rect

    white_color = (255, 253, 208)

    black_color = (150, 75, 0)

    @classmethod
    def get_color(cls, token):
        if token:
            return cls.white_color
        else:
            return cls.black_color
