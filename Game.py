import pygame as pg
import sys

from Board import Board


class Game:

    def __init__(self):
        self.board = Board()
    def run_game(self):
        pg.init()
        screen_white = pg.display.set_mode((600, 600))
        screen_white.fill((150, 150, 150))
        pg.display.set_caption("Chess")
        ##pg.draw.rect(screen_white, (10, 10, 10), Field(100, 100))
        while True:
            color = False
            for x in range(0, 8):
                color = color == False
                for y in range(0, 8):
                    pg.draw.rect(screen_white, self.board.board[x,y].get_color(color), self.board.board[x, y].get_rect())
                    color = color == False
                #print(field)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    for x in range(0, 8):
                        for y in range(0, 8):
                            if self.board.board[x, y].get_rect().collidepoint(pg.mouse.get_pos()):
                                self.board.board[x, y].set_selection(True)
            pg.display.flip()