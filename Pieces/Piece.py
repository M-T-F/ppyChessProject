from abc import ABC, abstractmethod


class Piece(ABC):
    icon_white = None
    icon_black = None

    def __init__(self, color, x, y):
        self.color = color
        self.not_moved = True
        self.x = x
        self.y = y

    @abstractmethod
    def can_move(self):
        pass

    @abstractmethod
    def can_see(self):
        pass

    @abstractmethod
    def select_move(self, board):
        pass

    def get_icon(self):
        if self.color == 'white':
            return self.icon_white
        else:
            return self.icon_black

    def set_moved(self):
        self.not_moved = False

    def get_not_moved(self):
        return self.not_moved

    def get_color(self):
        return self.color

    def move(self, x, y):
        self.x = x
        self.y = y

    def get_x_coordinate(self):
        return self.x

    def get_y_coordinate(self):
        return self.y
