import turtle

import pygame as pg
import sys

import Field
from Pieces import King
from Board import Board
from Pieces import Pawn
from Pieces.Bishop import Bishop
from Pieces.Knight import Knight
from Pieces.Queen import Queen
from Pieces.Rook import Rook


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
        choose_upgrade = False
        choose_buttons = [Field.Field(50, 50),
                          Field.Field(50, 100),
                          Field.Field(50, 150),
                          Field.Field(50, 200)]
        while True:
            color = False
            if self.board.play():
                self.board.check_check()
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
                for button in choose_buttons:
                    if choose_upgrade:
                        pg.draw.rect(screen, (100,100,100),
                                     button)
                        screen.blit(button.get_piece().get_icon(),
                                    (button.get_rect().centerx -
                                     button.get_piece().get_icon().get_rect().centerx,
                                         button.get_rect().centery -
                                     button.get_piece().get_icon().get_rect().centery))
                    else:
                        pg.draw.rect(screen, (150, 150, 150),
                                     button)
            else:
                colors = self.board.get_wining_colors()
                msg_imige = pg.font.SysFont(None, 48).render(self.board.get_win_msg(),
                                                             True, colors[0], colors[1])
                msg_rect = msg_imige.get_rect()
                msg_rect.center = screen.get_rect().center
                screen.blit(msg_imige, msg_rect)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN and self.board.play():
                    if choose_upgrade:
                        for button in choose_buttons:
                            if button.get_rect().collidepoint(pg.mouse.get_pos()):
                                self.board.promote(self.selected, button.get_piece())
                                choose_upgrade = False
                                player_turn = 'black' if player_turn == 'white' else 'white'
                                for button_clear in choose_buttons:
                                    button_clear.set_piece(None)
                    for x in range(0, 8):
                        for y in range(0, 8):
                            if self.board.board[x, y].get_rect().collidepoint(pg.mouse.get_pos()):
                                if self.board.can_move(x, y):
                                    if (type(self.board.board[self.selected[0], self.selected[1]].get_piece())
                                            is King.King
                                            and self.board.board[
                                                self.selected[0], self.selected[1]].get_piece().get_not_moved()):
                                        self.board.castle(self.selected, x, y)
                                        player_turn = 'black' if player_turn == 'white' else 'white'
                                    elif (type(self.board.board[self.selected[0], self.selected[1]].get_piece())
                                            is Pawn.Pawn and (x == 0 or x == 7)):
                                        choose_buttons[0].set_piece(Queen(player_turn, x, y))
                                        choose_buttons[1].set_piece(Knight(player_turn, x, y))
                                        choose_buttons[2].set_piece(Bishop(player_turn, x, y))
                                        choose_buttons[3].set_piece(Rook(player_turn, x, y))
                                        choose_upgrade = True
                                    else:
                                        self.board.move(self.selected, x, y)
                                        player_turn = 'black' if player_turn == 'white' else 'white'
                                elif not choose_upgrade and self.board.board[x, y].has_piece():
                                    if self.board.board[x, y].get_piece().get_color() == player_turn:
                                        self.board.unselect()
                                        self.board.board[x, y].set_selection(True)
                                        self.selected = (x, y)
                                        self.board.select_move(self.selected)
            pg.display.flip()
