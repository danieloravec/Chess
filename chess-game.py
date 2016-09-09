try:
    from tkinter import *
except ImportError:
    from Tkinter import *

import settings
from hero import *


class Game:

    def __init__(self, field_side):
        self.field_width = field_side
        self.board_side = self.field_width * 8
        self.clicks = 0
        self.board_fields_positions = {}
        self.starting_positions = {'white': {}, 'black': {}}
        self.mark_board_fields()
        self.all_heroes = []

    def draw_chessboard(self, color):
        x1 = 0
        y1 = 0
        x2 = self.field_width
        settings.canvas.create_rectangle(0, 0, self.board_side, self.board_side, fill=color)

        for i in range(8):
            for j in range(4):
                if color == "black":
                    settings.canvas.create_rectangle(x1, y1, x2, y1 + self.field_width, fill="white")
                else:
                    settings.canvas.create_rectangle(x1, y1, x2, y1 + self.field_width, fill="black")
                x1 += self.field_width * 2
                if x2 + self.field_width * 2 <= self.board_side:
                    x2 += self.field_width * 2
                else:
                    x2 += self.field_width
            y1 += self.field_width
            if i % 2 == 0:
                x1 = self.field_width
                x2 = x1 * 2
            else:
                x1 = 0
                x2 = self.field_width

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
                self.board_fields_positions.update(
                    {(letter + str(number)): [
                        act_x,
                        act_y,
                        1 if letter == 'A' or letter == 'B' or letter == 'G' or letter == 'H' else 0
                    ]})
                if letter == 'A' or letter == 'B':
                    self.starting_positions['white'].update({(letter + str(number)): [act_x, act_y]})
                elif letter == 'G' or letter == 'H':
                    self.starting_positions['black'].update({(letter + str(number)): [act_x, act_y]})
                act_x += self.field_width
                number += 1
            act_x = 0
            act_y += self.field_width
            number = 1
            letter = chr(ord(letter) + 1)

    def chess_start(self):
        for figures_color in self.starting_positions:
            for key in sorted(self.starting_positions[figures_color]):
                self.all_heroes.append(Hero(
                    self.starting_positions[figures_color].get(key)[0],
                    self.starting_positions[figures_color][key][1],
                    100, 800)
                )
        i = 0
        for cur_hero in self.all_heroes:
            i += 1
            cur_hero.draw_hero()
        self.update_figures_counter()

    def move_all(self, event = None):
        # TODO rewrite this using map()
        for cur_hero in self.all_heroes:
            cur_hero.draw_hero()

    def move_clicked(self, click_pos):
        searched_coords = [click_pos.x - (click_pos.x % self.field_width), click_pos.y - (click_pos.y % self.field_width)]
        for cur_hero in self.all_heroes:
            if [cur_hero.x, cur_hero.y] == searched_coords:
                cur_hero.draw_hero()
        self.update_figures_counter()

    def update_figures_counter(self):
        coord_list = []
        for cur_hero in self.all_heroes:
            coord_list.append([cur_hero.x, cur_hero.y])
        for key in self.board_fields_positions.keys():
            self.board_fields_positions[key][2] = 0
        for key, value in self.board_fields_positions.items():
            for coords in coord_list:
                if value[0] == coords[0] and value[1] == coords[1]:
                    self.board_fields_positions[key][2] += 1
        settings.canvas.delete('current_text')
        for key, value in self.board_fields_positions.items():
            settings.canvas.create_text(
                value[0] + self.field_width // 2,
                value[1] + self.field_width // 2,
                text=value[2],
                fill='purple',
                tag='current_text',
                font=('calibri', self.field_width // 2)
            )


# Main
settings.init(800, 800)
chessboard = Game(int(settings.canvas.cget('width')) // 8)
chessboard.draw_chessboard("black")
chessboard.chess_start()
# fm = Pawn(400, 400, 100, 800)
# settings.canvas.bind("<Button-3>", fm.draw_hero)
kn = Knight(400, 400, 100, 800)
settings.canvas.bind("<Button-3>", kn.draw_hero)
settings.canvas.bind("<Button-1>", chessboard.move_clicked)
settings.root.mainloop()
