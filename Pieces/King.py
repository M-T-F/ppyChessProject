import pygame as pg


class King:
    def __init__(self, color):
        super().__init__()
        self.color = color
        if self.color == 'white':
            self.icon = pg.transform.scale_by(pg.image.load(r'Pieces\icons\white_king.png'), 0.35)
        else:
            self.icon = pg.transform.scale_by(pg.image.load(r'Pieces\icons\black_king.png'), 0.4)
        self.not_moved = True

    @classmethod
    def can_move(cls, x, y):
        return [(x+1, y+1), (x+1, y-1),
                (x-1, y+1), (x-1, y-1),
                (x+1, y), (x, y-1),
                (x, y+1), (x-1, y)]

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
        for tab in self.can_move(selected[0], selected[1]):
            if 0 <= tab[0] <= 7 and 0 <= tab[1] <= 7:
                if board[tab[0]][tab[1]].has_piece() and board[tab[0]][tab[1]].get_piece().get_color() != self.color:
                    board[tab[0]][tab[1]].set_take_selection()
                elif not board[tab[0]][tab[1]].has_piece():
                    board[tab[0]][tab[1]].set_move_selection()
        if self.not_moved:
            if board[selected[0], 7].get_piece().get_not_moved():
                if not board[selected[0]][6].has_piece() and not board[selected[0]][5].has_piece():
                    board[selected[0]][6].set_castle_selection()
            if board[selected[0], 0].get_piece().get_not_moved():
                if (not board[selected[0]][1].has_piece()
                        and not board[selected[0]][2].has_piece()
                        and not board[selected[0]][3].has_piece()):
                    board[selected[0]][2].set_castle_selection()

