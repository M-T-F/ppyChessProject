import pygame as pg


class Field:
    def __init__(self, x, y, width=50, height=50):
        self.rect = pg.Rect(x, y, width, height)
        self.piece = None
        self.selection = False
        self.move_selection = False
        self.check_selection = False
        self.castle_selection = False
        #print(self.rect.x, self.rect.y, self.rect.centery)

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
        if not self.selection:
            self.move_selection = False
            self.castle_selection = False
            self.check_selection = False

    def is_selected(self):
        return self.selection

    def set_move_selection(self):
        self.move_selection = True

    def get_move_selection(self):
        return self.move_selection

    def set_check_selection(self):
        self.check_selection = True

    def set_castle_selection(self):
        self.castle_selection = True

    def cen_move(self):
        return self.move_selection or self.castle_selection

    white_color = (255, 253, 208)

    black_color = (150, 75, 0)

    white_selected_color = (155, 153, 208-50)

    black_selected_color = (100, 55, 55)

    check_selection_color = (255, 50, 50)

    def get_color(self, token):
        if self.check_selection:
            return self.check_selection_color
        if self.selection or self.move_selection or self.castle_selection:
            if token:
                return self.white_selected_color
            else:
                return self.black_selected_color
        else:
            if token:
                return self.white_color
            else:
                return self.black_color

    #def blit(self, screen):
     #   screen.blit(self.piece.get_icon(), self.rect)



