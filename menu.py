from datetime import datetime
import json
from hero import *


class Menu:
    def __init__(self):
        pass

    def save_game(self, all_heroes):
        date = datetime.now()
        save_name = 'sv.json'
        # save_name = 'chess_save' + str(date.year) + '_' + str(date.day) + '_'\
        #             + str(date.month) + '_' + str(date.hour) + '_' + str(date.minute) + '_' + str(date.second) + '.json'
        with open(save_name, 'w') as save_file:
            json.dump([o.dump() for o in all_heroes], save_file)

    def load_game(self, all_heroes, file_name):
        file_name += '.json'
        coords = [0, 0]
        all_heroes = []
        json_data = open(file_name).read()
        json_object = json.loads(json_data)
        for figure in json_object:
            coords[0] = figure['x']
            coords[1] = figure['y']
            color = figure['color']
            constructor_args = [coords[0], coords[1], color]
            if figure['type'] == 'Pawn':
                all_heroes.append(Pawn(constructor_args))
            elif figure['type'] == 'Knight':
                all_heroes.append(Knight(constructor_args))
            elif figure['type'] == 'Bishop':
                all_heroes.append(Bishop(constructor_args))
            elif figure['type'] == 'Rook':
                all_heroes.append(Rook(constructor_args))
            elif figure['type'] == 'Queen':
                all_heroes.append(Queen(constructor_args))
            else:
                all_heroes.append(King(constructor_args))