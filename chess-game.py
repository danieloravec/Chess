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
        self.update_figures_counter()

    def move_all(self, event = None):
        # TODO rewrite this using map()
        for cur_hero in self.all_heroes:
            cur_hero.draw_hero()

    def move_clicked(self, click_pos):
        searched_coords = [click_pos.x - (click_pos.x % self.field_width), click_pos.y - (click_pos.y % self.field_width)]
        for cur_hero in self.all_heroes:
            if [cur_hero.x, cur_hero.y] == searched_coords:
                # TODO update counter after calling move_if_possible()
                settings.canvas.bind('<Button-3>', lambda event, current_hero=cur_hero: self.move_if_possible(event, current_hero))
                self.update_figures_counter()

    def move_if_possible(self, event, hero_to_move):
        piece_type = hero_to_move.__class__.__name__
        destination = [event.x - (event.x % self.field_width), event.y - (event.y % self.field_width)]
        # Check, if there is anybody on destination field
        for cur_hero in self.all_heroes:
            # Is there a piece already?
            if [cur_hero.x, cur_hero.y] == destination:
                # I can't execute my teammate
                if cur_hero.color == hero_to_move.color:
                    return
                # I want to execute him, but can I?
                else:
                    # Am I pawn?
                    if piece_type == 'Pawn':
                        # Am I white? If so, I can only move down.
                        if hero_to_move.color == 'wheat':
                            # Can I get him?
                            if (destination == [hero_to_move.x + self.field_width, hero_to_move.y + self.field_width]
                                    or destination == [hero_to_move.x - self.field_width, hero_to_move.y + self.field_width]):
                                # Execute him!
                                hero_to_move.x = destination[0]
                                hero_to_move.y = destination[1]
                                settings.canvas.delete(cur_hero.hero)
                                self.all_heroes.remove(cur_hero)
                                hero_to_move.draw_hero()
                            return
                        # I am black, so I can only move up.
                        else:
                            if (destination == [hero_to_move.x + self.field_width, hero_to_move.y - self.field_width]
                                    or destination == [hero_to_move.x - self.field_width, hero_to_move.y - self.field_width]):
                                # Execute him!
                                hero_to_move.x = destination[0]
                                hero_to_move.y = destination[1]
                                settings.canvas.delete(cur_hero.hero)
                                self.all_heroes.remove(cur_hero)
                                hero_to_move.draw_hero()
                            return
                    # Am I rook?
                    elif piece_type == 'Rook':
                        # I want to go forward or back
                        if destination[0] == hero_to_move.x:
                            # Do I want to go back?
                            if destination[1] > hero_to_move.y:
                                # Is there any piece in my way?
                                for block_piece in self.all_heroes:
                                    if destination[0] == block_piece.x and destination[1] > block_piece.y > hero_to_move.y:
                                        return
                                # Execute him!
                                hero_to_move.y = destination[1]
                                settings.canvas.delete(cur_hero.hero)
                                self.all_heroes.remove(cur_hero)
                                hero_to_move.draw_hero()
                                return
                            # I want to go forward.
                            else:
                                # Is there any piece in my way?
                                for block_piece in self.all_heroes:
                                    if destination[0] == block_piece.x and destination[1] < block_piece.y < hero_to_move.y:
                                        return
                                # Execute him!
                                hero_to_move.y = destination[1]
                                settings.canvas.delete(cur_hero.hero)
                                self.all_heroes.remove(cur_hero)
                                hero_to_move.draw_hero()
                                return
                        # I want to go left or right.
                        elif destination[1] == hero_to_move.y:
                            # Do I want to go left?
                            if destination[0] < hero_to_move.x:
                                # Is there any piece in my way?
                                for block_piece in self.all_heroes:
                                    if destination[1] == block_piece.y and destination[0] < block_piece.x < hero_to_move.x:
                                        return
                                # Execute him!
                                hero_to_move.x = destination[0]
                                settings.canvas.delete(cur_hero.hero)
                                self.all_heroes.remove(cur_hero)
                                hero_to_move.draw_hero()
                                return
                            # I want to go right.
                            else:
                                # Is there any piece in my way?
                                for block_piece in self.all_heroes:
                                    if destination[1] == block_piece.y and destination[0] > block_piece.x > hero_to_move.x:
                                        return
                                # Execute him!
                                hero_to_move.x = destination[0]
                                settings.canvas.delete(cur_hero.hero)
                                self.all_heroes.remove(cur_hero)
                                hero_to_move.draw_hero()
                                return
                        # Forbidden field for rook
                        else:
                            return
                    # Am I knight?
                    elif piece_type == 'Knight':
                        # Forward-right motion
                        if (destination == [hero_to_move.x + self.field_width, hero_to_move.y - 2 * self.field_width] or
                                 destination == [hero_to_move.x - self.field_width, hero_to_move.y - 2 * self.field_width] or
                                 destination == [hero_to_move.x - 2 * self.field_width, hero_to_move.y - self.field_width] or
                                 destination == [hero_to_move.x - 2 * self.field_width, hero_to_move.y + self.field_width] or
                                 destination == [hero_to_move.x - self.field_width, hero_to_move.y + 2 * self.field_width] or
                                 destination == [hero_to_move.x + self.field_width, hero_to_move.y + 2 * self.field_width] or
                                 destination == [hero_to_move.x + 2 * self.field_width, hero_to_move.y + self.field_width] or
                                 destination == [hero_to_move.x + 2 * self.field_width, hero_to_move.y - self.field_width]):
                            #Execute him!
                            hero_to_move.x = destination[0]
                            hero_to_move.y = destination[1]
                            settings.canvas.delete(cur_hero.hero)
                            self.all_heroes.remove(cur_hero)
                            hero_to_move.draw_hero()
                            return
                    # Am I bishop?
                    elif piece_type == 'Bishop':
                        temp_x = hero_to_move.x
                        temp_y = hero_to_move.y
                        # Do I want to go to rigth?
                        if hero_to_move.x < destination[0]:
                            # Do I want to go forward?
                            if hero_to_move.y > destination[1]:
                                # Is there other piece in my way?
                                temp_x += self.field_width
                                temp_y -= self.field_width
                                while temp_x < destination[0] and temp_y > destination[1]:
                                    for block_piece in self.all_heroes:
                                        if block_piece.x == temp_x:
                                            if block_piece.y == temp_y:
                                                return
                                    temp_x += self.field_width
                                    temp_y -= self.field_width
                                # Can I reach him?
                                if destination == [temp_x, temp_y]:
                                    # Execute him!
                                    hero_to_move.x = destination[0]
                                    hero_to_move.y = destination[1]
                                    settings.canvas.delete(cur_hero.hero)
                                    self.all_heroes.remove(cur_hero)
                                    hero_to_move.draw_hero()
                                    return



        # Am I pawn?
        if piece_type == 'Pawn':
            if hero_to_move.color == 'wheat':
                if destination == [hero_to_move.x, hero_to_move.y + self.field_width]:
                    hero_to_move.y += self.field_width
                elif hero_to_move.y == self.field_width and destination == [hero_to_move.x, hero_to_move.y + 2 * self.field_width]:
                    hero_to_move.y += 2 * self.field_width
                hero_to_move.draw_hero()
                return
            else:
                if destination == [hero_to_move.x, hero_to_move.y - self.field_width]:
                    hero_to_move.y -= self.field_width
                elif hero_to_move.y == 6 * self.field_width and destination == [hero_to_move.x, hero_to_move.y - 2 * self.field_width]:
                    hero_to_move.y -= 2 * self.field_width
                hero_to_move.draw_hero()
                return
        # Am I rook?
        elif piece_type == 'Rook':
            # I want to go forward or back
            if destination[0] == hero_to_move.x:
                # Do I want to go back?
                if destination[1] > hero_to_move.y:
                    # Is there any piece in my way?
                    for block_piece in self.all_heroes:
                        if destination[0] == block_piece.x and destination[1] > block_piece.y > hero_to_move.y:
                            return
                    hero_to_move.y = destination[1]
                    hero_to_move.draw_hero()
                    return
                # I want to go forward.
                else:
                    # Is there any piece in my way?
                    for block_piece in self.all_heroes:
                        if destination[0] == block_piece.x and destination[1] < block_piece.y < hero_to_move.y:
                            return
                    hero_to_move.y = destination[1]
                    hero_to_move.draw_hero()
                    return
            # I want to go left or right.
            elif destination[1] == hero_to_move.y:
                # Do I want to go left?
                if destination[0] < hero_to_move.x:
                    # Is there any piece in my way?
                    for block_piece in self.all_heroes:
                        if destination[1] == block_piece.y and destination[0] < block_piece.x < hero_to_move.x:
                            return
                    hero_to_move.x = destination[0]
                    hero_to_move.draw_hero()
                    return
                # I want to go right.
                else:
                    # Is there any piece in my way?
                    for block_piece in self.all_heroes:
                        if destination[1] == block_piece.y and destination[0] > block_piece.x > hero_to_move.x:
                            return
                    hero_to_move.x = destination[0]
                    hero_to_move.draw_hero()
                    return
            # Forbidden field for rook
            else:
                return
        # Am I knight?
        elif piece_type == 'Knight':
            # Forward-right motion
            if (destination == [hero_to_move.x + self.field_width, hero_to_move.y - 2 * self.field_width] or
                        destination == [hero_to_move.x - self.field_width, hero_to_move.y - 2 * self.field_width] or
                        destination == [hero_to_move.x - 2 * self.field_width, hero_to_move.y - self.field_width] or
                        destination == [hero_to_move.x - 2 * self.field_width, hero_to_move.y + self.field_width] or
                        destination == [hero_to_move.x - self.field_width, hero_to_move.y + 2 * self.field_width] or
                        destination == [hero_to_move.x + self.field_width, hero_to_move.y + 2 * self.field_width] or
                        destination == [hero_to_move.x + 2 * self.field_width, hero_to_move.y + self.field_width] or
                        destination == [hero_to_move.x + 2 * self.field_width, hero_to_move.y - self.field_width]):
                hero_to_move.x = destination[0]
                hero_to_move.y = destination[1]
                hero_to_move.draw_hero()
                return









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
settings.canvas.bind("<Button-1>", chessboard.move_clicked)
settings.root.mainloop()
