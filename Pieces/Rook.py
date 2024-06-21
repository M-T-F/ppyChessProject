import pygame as pg


class Rook:
    def __init__(self, color):
        super().__init__()
        self.color = color
        if self.color == 'white':
            self.icon = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_rook.png'), 0.35)
        else:
            self.icon = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_rook.png'), 0.4)
        self.not_moved = True

    @classmethod
    def can_move(cls, x, y):
        tmp = []
        for i in range(0, x):
            tmp.append((i, y))
        for i in range(x+1, 8):
            tmp.append((i, y))
        for i in range(0, y):
            tmp.append((x, i))
        for i in range(y+1, 8):
            tmp.append((x, i))
        return tmp

    def can_see(self, x, y):
        return self.can_move(x, y)

    def get_icon(self):
        return self.icon

    def set_moved(self):
        self.not_moved = False

    def get_not_moved(self):
        return self.not_moved

    def get_color(self):
        return self.color

    def select_move(self, board, selected):
        nmove = True
        emove = True
        smove = True
        wmove = True
        for t in range(1,8):
            if smove and selected[0]+t <= 7 and not board[selected[0]+t, selected[1]].has_piece():
                board[selected[0] + t, selected[1]].set_move_selection()
            elif (smove and selected[0]+t <= 7 and board[selected[0]+t, selected[1]].has_piece()
                  and board[selected[0]+t, selected[1]].get_piece().get_color() != self.color):
                board[selected[0] + t, selected[1]].set_take_selection()
                smove = False
            else:
                smove = False

            if nmove and selected[0]-t >= 0 and not board[selected[0]-t, selected[1]].has_piece():
                board[selected[0] - t, selected[1]].set_move_selection()
            elif (nmove and selected[0]-t >= 0 and board[selected[0]-t, selected[1]].has_piece()
                  and board[selected[0]-t, selected[1]].get_piece().get_color() != self.color):
                board[selected[0] - t, selected[1]].set_take_selection()
                nmove = False
            else:
                nmove = False

            if emove and selected[1] + t <= 7 and not board[selected[0], selected[1] + t].has_piece():
                board[selected[0], selected[1] + t].set_move_selection()
            elif (emove and selected[1] + t <= 7 and board[selected[0], selected[1] + t].has_piece()
                  and board[selected[0], selected[1] + t].get_piece().get_color() != self.color):
                board[selected[0], selected[1] + t].set_take_selection()
                emove = False
            else:
                emove = False

            if wmove and selected[1] - t >= 0 and not board[selected[0], selected[1] - t].has_piece():
                board[selected[0], selected[1] - t].set_move_selection()
            elif (wmove and selected[1] - t >= 0 and board[selected[0], selected[1] - t].has_piece()
                  and board[selected[0], selected[1] - t].get_piece().get_color() != self.color):
                board[selected[0], selected[1] - t].set_take_selection()
                wmove = False
            else:
                wmove = False

    def is_king(self):
        return False
