from figures.bishop import Bishop
from figures.king import King
from figures.knight import Knight
from figures.pawn import Pawn
from figures.queen import Queen
from figures.rook import Rook


class Game:
    def __init__(self):
        self.board_side = 8
        self.board_fields_positions = []
        self.starting_positions = {'white': [], 'black': []}
        self.mark_board_fields()
        self.all_heroes = []
        self.is_occupied = []
        self.last_move = False
        for i in range(8):
            self.is_occupied.append([])
            for j in range(8):
                # -1 is black, 0 is empty, 1 is white
                self.is_occupied[i].append(1 if i < 2 else (-1 if i > 5 else 0))

    def mark_board_fields(self):
        for i in range(8):
            for j in range(8):
                self.board_fields_positions.append([j, i])
                if i < 2:
                    self.starting_positions['white'].append([j, i])
                elif i > 5:
                    self.starting_positions['black'].append([j, i])

    def chess_start(self):
        for figures_color in self.starting_positions:
            for coords in self.starting_positions[figures_color]:
                constructor_args = [coords[0], coords[1], 'wheat' if coords[1] == 0 or coords[1] == 1 else 'snow4']
                if coords[1] == 1 or coords[1] == 6:
                    self.all_heroes.append(Pawn(constructor_args))
                else:
                    if coords[0] == 0 or coords[0] == 7:
                        self.all_heroes.append(Rook(constructor_args))
                    elif coords[0] == 1 or coords[0] == 6:
                        self.all_heroes.append(Knight(constructor_args))
                    elif coords[0] == 2 or coords[0] == 5:
                        self.all_heroes.append(
                            Bishop(constructor_args))
                    elif coords[0] == 3:
                        self.all_heroes.append(Queen(constructor_args))
                    else:
                        self.all_heroes.append(King(constructor_args))

    def move_if_possible(self, prey_x, prey_y, hero_to_move):
        if (self.last_move and hero_to_move.color == hero_to_move.white_color)\
                or (not self.last_move and hero_to_move.color == hero_to_move.black_color)\
                or ([prey_x, prey_y] == [hero_to_move.x, hero_to_move.y]):
            return
        prey_coords = [prey_x, prey_y]
        occupation_number = 1 if hero_to_move.color == hero_to_move.white_color else -1
        old_x = hero_to_move.x
        old_y = hero_to_move.y
        move_performed = hero_to_move.move(prey_coords, self.all_heroes)
        if move_performed:
            self.is_occupied[old_y][old_x] = 0
            self.is_occupied[hero_to_move.y][hero_to_move.x] = occupation_number
            if hero_to_move.__class__.__name__ == 'Pawn'\
                    and hero_to_move.y == (0 if hero_to_move.color == hero_to_move.black_color else self.board_side - 1):
                constructor_args = [hero_to_move.x, hero_to_move.y, hero_to_move.color]
                self.all_heroes.remove(hero_to_move)
                self.all_heroes.append(Queen(constructor_args))
        self.last_move = not self.last_move
