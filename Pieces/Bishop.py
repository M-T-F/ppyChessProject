import pygame as pg


class Bishop:
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        if self.color == 'white':
            self.icon = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_bishop.png'), 0.35)
        else:
            self.icon = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_bishop.png'), 0.4)
        self.not_moved = True
        self.x = x
        self.y = y

    @classmethod
    def cls_can_move(cls, x, y):
        tmp = []
        for i in range(1,8):
            if x + i < 8:
                if y + i < 8:
                    tmp.append((x + i, y + i))
                if 0 <= y - i:
                    tmp.append((x + i, y - i))
            elif 0 <= x-1:
                if y + i < 8:
                    tmp.append((x - i, y + i))
                if 0 <= y - i:
                    tmp.append((x - i, y - i))
        return tmp

    def can_move(self):
        tmp = []
        for i in range(1,8):
            if self.x + i < 8:
                if self.y + i < 8:
                    tmp.append((self.x + i, self.y + i))
                if 0 <= self.y - i:
                    tmp.append((self.x + i, self.y - i))
            elif 0 <= self.x-1:
                if self.y + i < 8:
                    tmp.append((self.x - i, self.y + i))
                if 0 <= self.y - i:
                    tmp.append((self.x - i, self.y - i))
        return tmp

    def can_see(self, board):
        tmp = []
        nemove = True
        semove = True
        swmove = True
        nwmove = True
        for t in range(1, 8):
            if (semove and 0 <= self.x + t <= 7 and 0 <= self.y + t <= 7
                  and board[self.x + t, self.y + t].has_piece()
                  and board[self.x + t, self.y + t].get_piece().get_color() != self.color):
                tmp.append((self.x + t, self.y + t))
                semove = False
            else:
                semove = False

            if (swmove and 0 <= self.x + t <= 7 and 0 <= self.y - t <= 7
                  and board[self.x + t, self.y - t].has_piece()
                  and board[self.x + t, self.y - t].get_piece().get_color() != self.color):
                tmp.append((self.x + t, self.y - t))
                swmove = False
            else:
                swmove = False

            if (nemove and 0 <= self.x - t <= 7 and 0 <= self.y + t <= 7
                  and board[self.x - t, self.y + t].has_piece()
                  and board[self.x - t, self.y + t].get_piece().get_color() != self.color):
                tmp.append((self.x - t, self.y + t))
                nemove = False
            else:
                nemove = False

            if (nwmove and 0 <= self.x - t <= 7 and 0 <= self.y - t <= 7
                  and board[self.x - t, self.y - t].has_piece()
                  and board[self.x - t, self.y - t].get_piece().get_color() != self.color):
                tmp.append((self.x - t, self.y - t))
                nwmove = False
            else:
                nwmove = False
        return tmp

    def get_icon(self):
        return self.icon

    def set_moved(self):
        self.not_moved = False

    def get_color(self):
        return self.color

    def select_move(self, board):
        nemove = True
        semove = True
        swmove = True
        nwmove = True
        for t in range(1, 8):
            if (semove and 0 <= self.x + t <= 7 and 0 <= self.y + t <= 7
                    and not board[self.x + t, self.y + t].has_piece()):
                board[self.x + t, self.y + t].set_move_selection()
            elif (semove and 0 <= self.x + t <= 7 and 0 <= self.y + t <= 7
                  and board[self.x + t, self.y + t].has_piece()
                  and board[self.x + t, self.y + t].get_piece().get_color() != self.color):
                board[self.x + t, self.y + t].set_take_selection()
                semove = False
            else:
                semove = False

            if (swmove and 0 <= self.x + t <= 7 and 0 <= self.y - t <= 7
                    and not board[self.x + t, self.y - t].has_piece()):
                board[self.x + t, self.y - t].set_move_selection()
            elif (swmove and 0 <= self.x + t <= 7 and 0 <= self.y - t <= 7
                  and board[self.x + t, self.y - t].has_piece()
                  and board[self.x + t, self.y - t].get_piece().get_color() != self.color):
                board[self.x + t, self.y - t].set_take_selection()
                swmove = False
            else:
                swmove = False

            if (nemove and 0 <= self.x - t <= 7 and 0 <= self.y + t <= 7
                    and not board[self.x - t, self.y + t].has_piece()):
                board[self.x - t, self.y + t].set_move_selection()
            elif (nemove and 0 <= self.x - t <= 7 and 0 <= self.y + t <= 7
                  and board[self.x - t, self.y + t].has_piece()
                  and board[self.x - t, self.y + t].get_piece().get_color() != self.color):
                board[self.x - t, self.y + t].set_take_selection()
                nemove = False
            else:
                nemove = False

            if (nwmove and 0 <= self.x - t <= 7 and 0 <= self.y - t <= 7
                    and not board[self.x - t, self.y - t].has_piece()):
                board[self.x - t, self.y - t].set_move_selection()
            elif (nwmove and 0 <= self.x - t <= 7 and 0 <= self.y - t <= 7
                  and board[self.x - t, self.y - t].has_piece()
                  and board[self.x - t, self.y - t].get_piece().get_color() != self.color):
                board[self.x - t, self.y - t].set_take_selection()
                nwmove = False
            else:
                nwmove = False

    def move(self, x, y):
        self.x = x
        self.y = y
