import pygame as pg


class Field:
    def __init__(self, x, y, width=50, height=50):
        self.rect = pg.Rect(x, y, width, height)
        self.piece = None
        self.selection = False

    def has_piece(self):
        return self.piece is not None

    def set_piece(self, piece):
        self.piece = piece

    def get_piece(self):
        return self.piece

    def get_rect(self):
        return self.rect

    def set_selection(self, selection):
        self.selection = selection

    white_color = (255, 253, 208)

    black_color = (150, 75, 0)

    white_selected_color = (100, 200, 50)

    black_selected_color = (200, 50, 100)

    def get_color(self, token):
        if self.selection:
            if token:
                return self.white_selected_color
            else:
                return self.black_selected_color
        else:
            if token:
                return self.white_color
            else:
                return self.black_color
