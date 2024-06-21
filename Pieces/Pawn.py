import pygame as pg


class Pawn:
    def __init__(self, color):
        super().__init__()
        self.color = color
        if self.color == 'white':
            self.icon = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_pawn.png'), 0.35)
        else:
            self.icon = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_pawn.png'), 0.4)
        self.not_moved = True

    def can_move(self, x, y):
        if self.not_moved:
            if self.color == 'black':
                return [(x+1, y), (x+2, y)]
            else:
                return [(x-1, y), (x-2, y)]
        else:
            if self.color == 'black':
                return [(x+1, y)]
            else:
                return [(x-1, y)]

    def can_see(self, x, y):
        if self.color == 'black':
            return [(x+1, y+1), (x+1, y-1)]
        else:
            return [(x-1, y+1), (x-1, y-1)]

    def get_icon(self):
        return self.icon

    def set_moved(self):
        self.not_moved = False

    def select_move(self, board, selected):
        if self.not_moved:
            tmp = True
            for t in range(1,3):
                if self.color == 'black':
                    if not board[selected[0]+t, selected[1]].has_piece() and tmp:
                        board[selected[0]+t, selected[1]].set_move_selection()
                    else:
                        tmp = False
                else:
                    if not board[selected[0]-t, selected[1]].has_piece() and tmp:
                        board[selected[0]-t, selected[1]].set_move_selection()
                    else:
                        tmp = False
        else:
            if self.color == 'black':
                if not board[selected[0]+1, selected[1]].has_piece():
                    board[selected[0] + 1, selected[1]].set_move_selection()
            else:
                if not board[selected[0] - 1, selected[1]].has_piece():
                    board[selected[0] - 1, selected[1]].set_move_selection()
        for see in self.can_see(selected[0], selected[1]):
            if 0 <= see[1] <= 7:
                if board[see[0], see[1]].has_piece():
                    board[see[0], see[1]].set_take_selection()

    def get_color(self):
        return self.color
