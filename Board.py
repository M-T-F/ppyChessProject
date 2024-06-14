import numpy as np
import pandas as pd
import sys
import pygame as pg
from Field import Field


class Board:
    def __init__(self):
        mac = np.array([[Field(x, y) for x in range(100, 500, 50)] for y in range(100, 500, 50)])
        #print(mac)
        self.board = pd.DataFrame(mac, ["a", "b", "c", "d", "e", "f", "g", "h"])
        #print(self.board)

    def run_game(self):
        pg.init()
        screen_white = pg.display.set_mode((600, 600))
        screen_white.fill((170, 170, 170))
        pg.display.set_caption("Chess")
        ##pg.draw.rect(screen_white, (10, 10, 10), Field(100, 100))
        while True:
            color = False
            for x in range(0, 8):
                color = color == False
                for y in range(0, 8):
                    pg.draw.rect(screen_white, Field.get_color(color), self.board.loc[chr(x+ord("a")), y])
                    color = color==False
                #print(field)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            pg.display.flip()
