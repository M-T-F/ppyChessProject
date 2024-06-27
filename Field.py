import pygame as pg


class Field:
    def __init__(self, x, y, width=50, height=50):
        self.rect = pg.Rect(x, y, width, height)
        self.piece = None
        self.selection = False
        self.move_selection = False
        self.check_selection = False

    def has_piece(self):
        """ metoda zwracająca True jeśli na polu stoi figura"""
        return self.piece is not None

    def set_piece(self, piece):
        """ metoda kładąca figure na pole"""
        self.piece = piece

    def get_piece(self):
        """ getter figury stojącej na polu"""
        return self.piece

    def get_rect(self):
        """ Getter self.rect (kwadratu reprezentjący pole)"""
        return self.rect

    def set_selection(self, selection):
        """ metoda zaznaczająca pole"""
        self.selection = selection
        if not self.selection:
            self.move_selection = False
            self.check_selection = False

    def set_move_selection(self):
        """ metoda ustawiająca zaznaczenie na pole """
        self.move_selection = True

    def get_move_selection(self):
        """ metoda ustawiająca zaznaczenie na pole do ruchu"""
        return self.move_selection

    def set_check_selection(self):
        """ metoda ustawiająca zaznaczenie na pole z odsłoniętym królem"""
        self.check_selection = True

    white_color = (255, 253, 208)

    black_color = (150, 75, 0)

    white_selected_color = (155, 153, 208-50)

    black_selected_color = (100, 55, 55)

    check_selection_color = (255, 50, 50)

    def get_color(self, token):
        """ metoda zwraca kolor pola zalerznie od tokenu, tego czy jest zaznaczone i rodzaju zaznaczenia"""
        if self.check_selection:
            return self.check_selection_color
        if self.selection or self.move_selection:
            if token:
                return self.white_selected_color
            else:
                return self.black_selected_color
        else:
            if token:
                return self.white_color
            else:
                return self.black_color

