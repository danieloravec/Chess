from datetime import datetime
import json
from figures.hero import Hero
from figures.bishop import Bishop
from figures.king import King
from figures.knight import Knight
from figures.pawn import Pawn
from figures.queen import Queen
from figures.rook import Rook


class Menu:
    def __init__(self):
        pass

    # save_game and load_game need saves directory created
    # save_name_from_user and file_name are now always 'saved_game'
    #  -> it is set in visualisation.py __init__ and load_button_pressed
    def save_game(self, all_heroes, save_name_from_user):
        save_name_from_user += '.json'
        with open('saves/' + save_name_from_user, 'w') as save_file:
            json.dump([o.dump() for o in all_heroes], save_file)

    def load_game(self, file_name):
        file_name += '.json'
        coords = [0, 0]
        all_heroes = []
        json_data = open('saves/' + file_name).read()
        json_object = json.loads(json_data)
        for figure in json_object:
            coords[0] = figure['x']
            coords[1] = figure['y']
            color = figure['color']
            constructor_args = [coords[0], coords[1], color]
            all_heroes.append(globals()[figure['type']](constructor_args))
        return all_heroes
