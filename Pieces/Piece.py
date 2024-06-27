from abc import ABC, abstractmethod


class Piece(ABC):
    icon_white = None
    icon_black = None

    def __init__(self, color, x, y, enemies = None):
        """ konstruktor
            color - kolor figury (black/white)
            x - wspułżendna x
            y - wspułżendna y
            enemies - lista wrogicg figur
         """
        if enemies is None:
            enemies = [[]]
        self.color = color
        self.not_moved = True
        self.x = x
        self.y = y
        self.enemies = enemies[0]

    @abstractmethod
    def can_see(self, board=None):
        """ zwraca liste ruchów kture figura/pionek widzi na boadr"""
        pass

    @abstractmethod
    def select_move(self, board):
        """ zaznacza ruchy kture widzi na board"""
        pass

    @abstractmethod
    def would_see_king_after(self, board, index, move):
        """ metoda stwierdzająca czy figura/pionek będzie widzieć króla po rochy figury/pionka z index na move"""
        pass

    def is_pined_to_king(self, board, index, move):
        """ metoda stwierdzaja czy figura/pionek może się ruszyć z index na move i nie odsłoni króla"""
        for enemy in self.enemies:
            if index in enemy.can_see(board):
                if enemy.would_see_king_after(board, index, move):
                    return True
        return False

    def get_icon(self):
        """ metoda zwraca ikone danej figury/pionka"""
        if self.color == 'white':
            return self.icon_white
        else:
            return self.icon_black

    def set_moved(self):
        """ metoda ustawia pole self.not_moved na False"""
        self.not_moved = False

    def get_not_moved(self):
        """ getter pola self.not_moved"""
        return self.not_moved

    def get_color(self):
        """ getter pola self.color"""
        return self.color

    def move(self, x, y):
        """ metoda zmienia wspułżendne an x, y"""
        self.x = x
        self.y = y

    def get_x_coordinate(self):
        """ getter pola self.x"""
        return self.x

    def get_y_coordinate(self):
        """ getter pola self.y"""
        return self.y

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " "+ str(self.color)

    def __repr__(self):
        return str(type(self)) + " " + str(self.x) + " " + str(self.y) + " "+ str(self.color)

    def set_enemies(self, enemies):
        """ setter pola self.enemies"""
        self.enemies = enemies


