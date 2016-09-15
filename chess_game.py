from hero import *


class Game:
    # TODO remove graphics
    def __init__(self):
        self.board_side = 1 * 8
        self.clicks = 0
        self.board_fields_positions = {}
        self.starting_positions = {'white': {}, 'black': {}}
        self.mark_board_fields()
        self.all_heroes = []

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
                act_x += 1
                number += 1
            act_x = 0
            act_y += 1
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
                            'wheat' if 'A' in key or 'B' in key else 'snow4'
                        )
                    )
                else:
                    if '1' in key or '8' in key:
                        self.all_heroes.append(
                            Rook(
                                self.starting_positions[figures_color][key][0],
                                self.starting_positions[figures_color][key][1],
                                'wheat' if 'A' in key or 'B' in key else 'snow4'
                            )
                        )
                    elif '2' in key or '7' in key:
                        self.all_heroes.append(
                            Knight(
                                self.starting_positions[figures_color][key][0],
                                self.starting_positions[figures_color][key][1],
                                'wheat' if 'A' in key or 'B' in key else 'snow4'
                            )
                        )
                    elif '3' in key or '6' in key:
                        self.all_heroes.append(
                            Bishop(
                                self.starting_positions[figures_color][key][0],
                                self.starting_positions[figures_color][key][1],
                                'wheat' if 'A' in key or 'B' in key else 'snow4'
                            )
                        )
                    elif '4' in key:
                        self.all_heroes.append(
                            Queen(
                                self.starting_positions[figures_color][key][0],
                                self.starting_positions[figures_color][key][1],
                                'wheat' if 'A' in key or 'B' in key else 'snow4'
                            )
                        )
                    else:
                        self.all_heroes.append(
                            King(
                                self.starting_positions[figures_color][key][0],
                                self.starting_positions[figures_color][key][1],
                                'wheat' if 'A' in key or 'B' in key else 'snow4'
                            )
                        )

    def move_selected(self, x, y):
        for cur_hero in self.all_heroes:
            if cur_hero.x == x and cur_hero.y == y:
                self.move_if_possible()

    def move_if_possible(self, prey_x, prey_y, hero_to_move):
        prey_coords = [prey_x, prey_y]
        hero_to_move.move(prey_coords, self.all_heroes)
