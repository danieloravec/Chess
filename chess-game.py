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
                if 'B' in key or 'G' in key:
                    self.all_heroes.append(
                        Pawn(
                            self.starting_positions[figures_color][key][0],
                            self.starting_positions[figures_color][key][1],
                            'wheat' if 'A' in key or 'B' in key else 'snow4',
                            100, 800
                        )
                    )
                else:
                    if '1' in key or '8' in key:
                        self.all_heroes.append(
                            Rook(
                                self.starting_positions[figures_color][key][0],
                                self.starting_positions[figures_color][key][1],
                                'wheat' if 'A' in key or 'B' in key else 'snow4',
                                100, 800
                            )
                        )
                    elif '2' in key or '7' in key:
                        self.all_heroes.append(
                            Knight(
                                self.starting_positions[figures_color][key][0],
                                self.starting_positions[figures_color][key][1],
                                'wheat' if 'A' in key or 'B' in key else 'snow4',
                                100, 800
                            )
                        )
                    elif '3' in key or '6' in key:
                        self.all_heroes.append(
                            Bishop(
                                self.starting_positions[figures_color][key][0],
                                self.starting_positions[figures_color][key][1],
                                'wheat' if 'A' in key or 'B' in key else 'snow4',
                                100, 800
                            )
                        )
                    elif '4' in key:
                        self.all_heroes.append(
                            Queen(
                                self.starting_positions[figures_color][key][0],
                                self.starting_positions[figures_color][key][1],
                                'wheat' if 'A' in key or 'B' in key else 'snow4',
                                100, 800
                            )
                        )
                    else:
                        self.all_heroes.append(
                            King(
                                self.starting_positions[figures_color][key][0],
                                self.starting_positions[figures_color][key][1],
                                'wheat' if 'A' in key or 'B' in key else 'snow4',
                                100, 800
                            )
                        )
        for cur_hero in self.all_heroes:
            cur_hero.draw_hero()
        self.redraw_situation()

    def move_clicked(self, click_pos):
        searched_coords = [click_pos.x - (click_pos.x % self.field_width), click_pos.y - (click_pos.y % self.field_width)]
        for cur_hero in self.all_heroes:
            if [cur_hero.x, cur_hero.y] == searched_coords:
                settings.canvas.bind('<Button-3>', lambda event, current_hero=cur_hero: self.move_if_possible(event, current_hero))

    def move_if_possible(self, event, hero_to_move):
        prey_coords = [event.x - (event.x % self.field_width), event.y - (event.y % self.field_width)]
        hero_to_move.move(prey_coords, self.all_heroes)
        self.redraw_situation()

    def redraw_situation(self):
        settings.canvas.delete("all")
        self.draw_chessboard("black")
        for cur_hero in self.all_heroes:
            settings.canvas.create_oval(
                cur_hero.x, cur_hero.y,
                cur_hero.x + self.field_width, cur_hero.y + self.field_width,
                fill=cur_hero.color
            )
            settings.canvas.create_text(
                cur_hero.x + self.field_width // 2,
                cur_hero.y + self.field_width // 2.,
                text=cur_hero.__class__.__name__
            )


if __name__ == '__main__':
    settings.init(800, 800)
    chessboard = Game(int(settings.canvas.cget('width')) // 8)
    chessboard.draw_chessboard("black")
    chessboard.chess_start()
    settings.canvas.bind("<Button-1>", chessboard.move_clicked)
    settings.root.mainloop()
