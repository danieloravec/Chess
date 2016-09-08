try:
    from tkinter import *
except ImportError:
    from Tkinter import *

import settings
from hero import Hero


settings.init()


class Game:

    def __init__(self):
        self.clicks = 0
        self.board_fields_positions = {}
        self.starting_positions = {'white': {}, 'black': {}}
        self.mark_board_fields()
        self.all_heroes = []

    def draw_chessboard(self, color):
        x1 = 0
        y1 = 0
        x2 = 32
        settings.canvas.create_rectangle(0, 0, 256, 256, fill=color)

        for i in range(8):
            for j in range(4):
                if color == "black":
                    settings.canvas.create_rectangle(x1, y1, x2, y1 + 32, fill="white")
                else:
                    settings.canvas.create_rectangle(x1, y1, x2, y1 + 32, fill="black")
                x1 += 64
                if x2 + 64 <= 256:
                    x2 += 64
                else:
                    x2 += 32
            y1 += 32
            if i % 2 == 0:
                x1 = 32
                x2 = 64
            else:
                x1 = 0
                x2 = 32

    def change_chessboard(self, event = None):
        if self.clicks % 2 == 1:
            self.draw_chessboard("black")
        else:
            self.draw_chessboard("white")
        self.clicks
        self.clicks += 1

    def mark_board_fields(self):
        act_x = 0
        act_y = 0
        letter = 'A'
        number = 1
        for i in range(8):
            for j in range(8):
                self.board_fields_positions.update({(letter + str(number)): [act_x, act_y]})
                if letter == 'A' or letter == 'B':
                    self.starting_positions['white'].update({(letter + str(number)): [act_x, act_y]})
                elif letter == 'G' or letter == 'H':
                    self.starting_positions['black'].update({(letter + str(number)): [act_x, act_y]})
                act_x += 32
                number += 1
            act_x = 0
            act_y += 32
            number = 1
            letter = chr(ord(letter) + 1)

    def chess_start(self):
        for figures_color in self.starting_positions:
            for key in sorted(self.starting_positions[figures_color]):
                self.all_heroes.append(Hero(
                    self.starting_positions[figures_color].get(key)[0],
                    self.starting_positions[figures_color][key][1],
                    32, 256)
                )
        i = 0
        for cur_hero in self.all_heroes:
            i += 1
            cur_hero.draw_hero()


    def move_all(self, event = None):
        # TODO rewrite this using map()
        for cur_hero in self.all_heroes:
            cur_hero.draw_hero()

    def move_clicked(self, click_pos):
        searched_coords = [click_pos.x - (click_pos.x % 32), click_pos.y - (click_pos.y % 32)]
        for cur_hero in self.all_heroes:
            if [cur_hero.x, cur_hero.y] == searched_coords:
                cur_hero.draw_hero()


chessboard = Game()
chessboard.draw_chessboard("black")
chessboard.chess_start()
settings.canvas.bind("<Button-1>", chessboard.move_clicked)
settings.root.mainloop()
