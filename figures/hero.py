class Hero:
    def __init__(self, args_list):
        self.x = args_list[0]
        self.y = args_list[1]
        self.board_side = 8
        self.color = args_list[2]
        self.black_color = 'snow4'
        self.white_color = 'wheat'

    def execute(self, prey, all_heroes):
        self.x = prey.x
        self.y = prey.y
        all_heroes.remove(prey)

    def get_prey(self, prey_coords, all_heroes):
        prey = None
        for cur_hero in all_heroes:
            if cur_hero.x == prey_coords[0] and cur_hero.y == prey_coords[1]:
                prey = cur_hero
                break
        return prey

    def is_obstacle(self, prey_coords, all_heroes):
        pass

    def dump(self):
        return {
            "x": self.x,
            "y": self.y,
            "color": self.color,
            "type": self.__class__.__name__
        }

    def get_valid_moves(self, occupied_fields, all_heroes):
        pass

    def is_inside_chessboard(self, x_coord, y_coord):
        return 0 <= x_coord < self.board_side and 0 <= y_coord < self.board_side
