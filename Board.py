import numpy as np
from Pieces import Pawn, Rook, Knight, Bishop, Queen, King
from Field import Field


class Board:
    def __init__(self):
        self._board = np.array([[Field(x, y) for x in range(100, 500, 50)] for y in range(100, 500, 50)])
        self.selected = None
        self.white_pieces = []
        self.black_pieces = []
        for y in range(8):
            black = Pawn.Pawn('black', 1, y, [self.white_pieces])
            self.board[1, y].set_piece(black)
            self.black_pieces.append(black)

            white = Pawn.Pawn('white', 6, y, [self.black_pieces])
            self.board[6, y].set_piece(white)
            self.white_pieces.append(white)
            if y == 0 or y == 7:
                black = Rook.Rook('black', 0, y, [self.white_pieces])
                self.board[0, y].set_piece(black)
                self.black_pieces.append(black)

                white = Rook.Rook('white', 7, y, [self.black_pieces])
                self.board[7, y].set_piece(white)
                self.white_pieces.append(white)
            elif y == 1 or y == 6:
                black = Knight.Knight('black', 0, y, [self.white_pieces])
                self.board[0, y].set_piece(black)
                self.black_pieces.append(black)

                white = Knight.Knight('white', 7, y, [self.black_pieces])
                self.board[7, y].set_piece(white)
                self.white_pieces.append(white)
            elif y == 2 or y == 5:
                black = Bishop.Bishop('black', 0, y, [self.white_pieces])
                self.board[0, y].set_piece(black)
                self.black_pieces.append(black)

                white = Bishop.Bishop('white', 7, y, [self.black_pieces])
                self.board[7, y].set_piece(white)
                self.white_pieces.append(white)
            elif y == 3:
                black = Queen.Queen('black', 0, y, [self.white_pieces])
                self.board[0, y].set_piece(black)
                self.black_pieces.append(black)

                white = Queen.Queen('white', 7, y, [self.black_pieces])
                self.board[7, y].set_piece(white)
                self.white_pieces.append(white)
            elif y == 4:
                self.black_king = King.King('black', 0, y, [self.white_pieces])
                self.board[0, y].set_piece(self.black_king)
                self.black_pieces.append(self.black_king)

                self.white_king = King.King('white', 7, y, [self.black_pieces])
                self.board[7, y].set_piece(self.white_king)
                self.white_pieces.append(self.white_king)

    @property
    def board(self):
        return self._board

    def move(self, s, tx, ty):
        """ metoda przemieszcza figure z s na (tx, ty)"""
        self.board[s[0], s[1]].get_piece().set_moved()
        self.board[s[0], s[1]].get_piece().move(tx, ty)
        if self.board[tx, ty].has_piece():
            if self.board[tx, ty].get_piece().get_color() == 'white':
                self.white_pieces.remove(self.board[tx, ty].get_piece())
            else:
                self.black_pieces.remove(self.board[tx, ty].get_piece())
        if type(self.board[tx, ty].get_piece()) is King.King:
            self.board[tx, ty].get_piece().kill()
        self.board[tx, ty].set_piece(self.board[s[0], s[1]].get_piece())
        self.board[s[0], s[1]].set_piece(None)
        self.unselect()

    def promote(self, s, piece):
        """ promuje pienek na dany piece"""
        if self.board[s[0], s[1]].get_piece().get_color() == 'white':
            self.white_pieces.remove(self.board[s[0], s[1]].get_piece())
            self.white_pieces.append(piece)
            piece.set_enemies(self.black_pieces)
        else:
            self.black_pieces.remove(self.board[s[0], s[1]].get_piece())
            self.black_pieces.append(piece)
            piece.set_enemies(self.white_pieces)
        self.board[s[0], s[1]].set_piece(piece)
        self.move(s, piece.get_x_coordinate(), piece.get_y_coordinate())

    def castle(self, s, tx, ty):
        """ wykonuje ruch krula lub roszadę"""
        self.board[s[0], s[1]].get_piece().set_moved()
        self.board[s[0], s[1]].get_piece().move(tx, ty)
        if self.board[tx, ty].has_piece():
            if self.board[tx, ty].get_piece().get_color() == 'white':
                self.white_pieces.remove(self.board[tx, ty].get_piece())
            else:
                self.black_pieces.remove(self.board[tx, ty].get_piece())
        self.board[tx, ty].set_piece(self.board[s[0], s[1]].get_piece())
        self.board[s[0], s[1]].set_piece(None)
        if ty == 6:
            self.board[tx, 7].get_piece().move(tx, 5)
            self.board[tx, 5].set_piece(self.board[tx, 7].get_piece())
            self.board[tx, 7].set_piece(None)
            self.board[tx, 5].get_piece().set_moved()
        elif ty == 2:
            self.board[tx, 0].get_piece().move(tx, 3)
            self.board[tx, 3].set_piece(self.board[tx, 0].get_piece())
            self.board[tx, 0].set_piece(None)
            self.board[tx, 3].get_piece().set_moved()
        self.unselect()

    def select_move(self, selected):
        """ zaznacza pola na kture morze się ruszyć figura na wspułżędnych selected"""
        self.board[selected[0], selected[1]].get_piece().select_move(self.board)

    def unselect(self):
        """ metoda czyści zaznaczenie z całej planszy"""
        for x in self.board:
            for y in x:
                y.set_selection(False)

    def can_move(self, x, y):
        """ metoda stwierdza czy na pole jest zaznaczone by się ruszyć"""
        return self.board[x, y].get_move_selection()

    def check_check(self):
        """ metoda zaznacza pole na kturym stoi król jeśli jest w polu bicia figury przeciwnego gracza"""
        for piece in self.black_pieces:
            if self.white_king.get_cord() in piece.can_see(self.board):
                cord = self.white_king.get_cord()
                self.board[cord[0], cord[1]].set_check_selection()

        for piece in self.white_pieces:
            if self.black_king.get_cord() in piece.can_see(self.board):
                cord = self.black_king.get_cord()
                self.board[cord[0], cord[1]].set_check_selection()

    def play(self):
        """ metoda sprawdza czy obaj królowie żyją"""
        return self.white_king.is_alive() and self.black_king.is_alive()

    def get_wining_colors(self):
        """ metoda zwraca palete kolorów dla napisu końca gry"""
        if self.white_king.is_alive():
            return [(0, 0, 0), (255, 255, 255)]
        else:
            return [(255, 255, 255), (0, 0, 0)]

    def get_win_msg(self):
        """ metoda zwraca wiadomość zalerzną od tego ktura strona wygrała"""
        if self.white_king.is_alive():
            return "white win"
        else:
            return "black win"
