from abc import ABC, abstractmethod


class Piece(ABC):
    icon_white = None
    icon_black = None

    def __init__(self, color, x, y, enemies = []):
        self.color = color
        self.not_moved = True
        self.x = x
        self.y = y
        self.enemies = enemies

    @abstractmethod
    def can_move(self):
        pass

    @abstractmethod
    def can_see(self, board=None):
        pass

    @abstractmethod
    def select_move(self, board):
        pass

    @abstractmethod
    def would_see_king(self, board):
        pass

    @abstractmethod
    def would_see_king_after(self, board, index, move):
        pass

    def is_pined_to_king(self, board, index, move):
        for enemy in self.enemies:
            if index in enemy.can_see(board):
                if enemy.would_see_king_after(board, index, move):
                    return True
        return False

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

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " "+ str(self.color)

    def __repr__(self):
        return str(type(self)) + " " + str(self.x) + " " + str(self.y) + " "+ str(self.color)

    def set_enemies(self, enemies):
        self.enemies = enemies


