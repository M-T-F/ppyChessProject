import pygame as pg
import sys

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
                    for y in range(0, 8):
                        for x in range(0, 8):
                            if self.board.board[x, y].get_rect().collidepoint(pg.mouse.get_pos()):
                                if (x, y) in self.cmove and not self.board.board[x, y].has_piece():
                                    self.board.move(self.selected, x, y)
                                elif self.board.board[x, y].has_piece():
                                    for xi in range(0, 8):
                                        for yi in range(0, 8):
                                            self.board.board[xi, yi].set_selection(False)
                                    self.board.board[x, y].set_selection(True)
                                    self.selected = (x, y)
                                    self.cmove = self.board.board[x, y].get_piece().can_move(x,y)
                                    self.csee = self.board.board[x, y].get_piece().can_see(x,y)
                                    for xi in range(0, 8):
                                        for yi in range(0, 8):
                                            if (xi, yi) in self.cmove and not self.board.board[xi, yi].has_piece():
                                                self.board.board[xi, yi].set_selection(True)


            pg.display.flip()
