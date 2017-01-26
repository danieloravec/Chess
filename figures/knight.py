from figures.hero import Hero

d8y = [1, 1, 0, -1, -1, -1, 0, 1]
d8x = [0, 1, 1, 1, 0, -1, -1, -1]
d4x = [0, 1, 0, -1]
d4y = [1, 0, -1, 0]


class Knight(Hero):
    def move(self, prey_coords, all_heroes):
        prey = self.get_prey(prey_coords, all_heroes)
        if prey is False:
            return False
        if self.can_move(prey_coords):
            self.x = prey_coords[0]
            self.y = prey_coords[1]
            if prey is not None:
                self.execute(prey, all_heroes)
        return True

    def can_move(self, prey_coords):
        if (prey_coords == [self.x + 1, self.y - 2] or
                prey_coords == [self.x - 1, self.y - 2] or
                prey_coords == [self.x - 2, self.y - 1] or
                prey_coords == [self.x - 2, self.y + 1] or
                prey_coords == [self.x - 1, self.y + 2] or
                prey_coords == [self.x + 1, self.y + 2] or
                prey_coords == [self.x + 2, self.y + 1] or
                prey_coords == [self.x + 2, self.y - 1]):
            return True
        else:
            return False

    def get_prey(self, prey_coords, all_heroes):
        prey = None
        for cur_hero in all_heroes:
            if cur_hero.x == prey_coords[0] and cur_hero.y == prey_coords[1]:
                prey = cur_hero
                if prey.color == self.color:
                    prey = False
                break
        return prey

    def get_valid_moves_by_direction(self, x_increment, y_increment, occupied_fields):
        direction_valid_moves = []
        if self.is_inside_chessboard(self.x + x_increment, self.y + y_increment)\
                    and occupied_fields[self.y + y_increment][self.x + x_increment] != (1 if self.color == self.white_color else -1):
            direction_valid_moves.append([self.x + x_increment, self.y + y_increment])
        return direction_valid_moves

    def get_valid_moves(self, occupied_fields, all_heroes):
        valid_moves = []
        valid_moves += self.get_valid_moves_by_direction(1, -2, occupied_fields)
        valid_moves += self.get_valid_moves_by_direction(-1, -2, occupied_fields)
        valid_moves += self.get_valid_moves_by_direction(-2, -1, occupied_fields)
        valid_moves += self.get_valid_moves_by_direction(-2, 1, occupied_fields)
        valid_moves += self.get_valid_moves_by_direction(-1, 2, occupied_fields)
        valid_moves += self.get_valid_moves_by_direction(1, 2, occupied_fields)
        valid_moves += self.get_valid_moves_by_direction(2, -1, occupied_fields)
        valid_moves += self.get_valid_moves_by_direction(2, 1, occupied_fields)
        return valid_moves
