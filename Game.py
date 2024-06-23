import turtle

import pygame as pg
import sys
from Pieces import King
from Board import Board


class Game:

    def __init__(self):
        self.board = Board()
        self.selected = None
        self.cmove = []
        self.csee = []

    def run_game(self):
        pg.init()
        screen = pg.display.set_mode((600, 600))
        screen.fill((150, 150, 150))
        pg.display.set_caption("Chess")
        ##pg.draw.rect(screen_white, (10, 10, 10), Field(100, 100))
        player_turn = "white"
        while True:
            color = False
            for x in range(0, 8):
                color = color == False
                for y in range(0, 8):
                    pg.draw.rect(screen, self.board.board[x, y].get_color(color),
                                 self.board.board[x, y].get_rect())
                    if self.board.board[x, y].has_piece():
                        screen.blit(self.board.board[x, y].get_piece().get_icon(),
                                    (self.board.board[x, y].get_rect().centerx
                                     - self.board.board[x, y].get_piece().get_icon().get_rect().centerx,
                                     self.board.board[x, y].get_rect().centery
                                     - self.board.board[x, y].get_piece().get_icon().get_rect().centery))
                    color = color == False

                # print(field)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    for x in range(0, 8):
                        for y in range(0, 8):
                            if self.board.board[x, y].get_rect().collidepoint(pg.mouse.get_pos()):
                                if self.board.can_move(x, y):
                                    if (type(self.board.board[self.selected[0], self.selected[1]].get_piece())
                                            is King.King
                                            and self.board.board[
                                                self.selected[0], self.selected[1]].get_piece().get_not_moved()):
                                        self.board.castle(self.selected, x, y)
                                    else:
                                        self.board.move(self.selected, x, y)
                                    player_turn = 'black' if player_turn == 'white' else 'white'
                                elif self.board.board[x, y].has_piece():
                                    if self.board.board[x, y].get_piece().get_color() == player_turn:
                                        self.board.unselect()
                                        self.board.board[x, y].set_selection(True)
                                        self.selected = (x, y)
                                        self.board.select_move(self.selected)

            pg.display.flip()
