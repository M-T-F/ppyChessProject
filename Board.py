import numpy as np
import pandas as pd
import sys
import pygame as pg
from Field import Field


class Board:
    def __init__(self):
        mac = np.array([[Field(x, y) for x in range(0, 8)] for y in range(0, 8)])
        self.board = pd.DataFrame(mac,["a", "b", "c", "d", "e", "f", "g", "h"])

    def run_game(self):
        pg.init()
        screen = pg.display.set_mode((1200, 800))
        screen.fill((255, 255, 255))
        pg.display.set_caption("Pygame")
        pg.draw.rect(screen, (10, 10, 10), pg.Rect(100, 100, 50, 50))
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            pg.display.flip()
