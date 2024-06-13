import numpy as np
import pandas as pd
import sys
import pygame as pg
from Field import Field


class Board:
    def __init__(self):
        mac = np.array([[Field(x, y) for x in range(100, 700, 75)] for y in range(100, 700, 75)])
        #print(mac)
        self.board = pd.DataFrame(mac, ["a", "b", "c", "d", "e", "f", "g", "h"])
        #print(self.board)

    def run_game(self):
        pg.init()
        screen_white = pg.display.set_mode((800, 800))
        screen_white.fill((255, 255, 255))
        pg.display.set_caption("White")
        ##pg.draw.rect(screen_white, (10, 10, 10), Field(100, 100))
        while True:
            for x in range(0,8):
                for y in range(0,8):
                    pg.draw.rect(screen_white, (10, 10, 10), self.board.loc[chr(x+ord("a")), y])
                #print(field)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            pg.display.flip()
