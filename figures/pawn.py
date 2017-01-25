from figures.hero import Hero

d8y = [1, 1, 0, -1, -1, -1, 0, 1]
d8x = [0, 1, 1, 1, 0, -1, -1, -1]
d4x = [0, 1, 0, -1]
d4y = [1, 0, -1, 0]


class Pawn(Hero):
    def move(self, prey_coords, all_heroes):
        prey = self.get_prey(prey_coords, all_heroes)
        if prey is False:
            return False
        y_modificator = 1 if self.color == self.white_color else -1
        color_y_position = 1 if self.color == self.white_color else 6
        if prey_coords == [self.x, self.y + y_modificator] and prey is None:
            self.y += y_modificator
        elif self.y == color_y_position and prey_coords == [self.x, self.y + 2 * y_modificator]:
            if not self.is_obstacle(prey_coords, all_heroes):
                self.y += 2 * y_modificator
        if prey is not None:
            self.execute(prey, all_heroes)
        return True

    def is_obstacle(self, prey_coords, all_heroes):
        for block_piece in all_heroes:
            if block_piece.x == self.x and (prey_coords[1] > block_piece.y > self.y or prey_coords[1] < block_piece.y < self.y):
                return True
        return False

    def get_prey(self, prey_coords, all_heroes):
        prey = None
        for cur_hero in all_heroes:
            if [cur_hero.x, cur_hero.y] == prey_coords:
                prey = cur_hero
                break
        if prey is not None:
            if (abs(self.x - prey.x) != 1
                    or prey.y != (self.y + 1 if self.color == self.white_color else self.y - 1)
                    or prey.color == self.color):
                prey = False
        return prey

    # TODO find more elegant way..
    def get_valid_moves(self, occupied_fields, all_heroes):
        valid_positions = []
        is_black = self.color == self.black_color
        if self.is_inside_chessboard(self.x, self.y - (1 if is_black else -1))\
                and occupied_fields[self.y - (1 if is_black else -1)][self.x] == 0:
            valid_positions.append([self.x, self.y - (1 if is_black else -1)])
        if self.is_inside_chessboard(self.x, self.y - (2 if is_black else -2))and self.y == (6 if is_black else 1)\
                and occupied_fields[self.y - (2 if is_black else -2)][self.x] == 0\
                and occupied_fields[self.y - (1 if is_black else -1)][self.x] == 0:
            valid_positions.append([self.x, self.y - (2 if is_black else -2)])
        if self.is_inside_chessboard(self.x + (1 if is_black else -1), self.y - (1 if is_black else -1))\
                and occupied_fields[self.y - (1 if is_black else -1)][self.x + (1 if is_black else -1)] == (1 if is_black else -1):
            valid_positions.append([self.x + (1 if is_black else -1), self.y - (1 if is_black else -1)])
        if self.is_inside_chessboard(self.x - (1 if is_black else -1), self.y - (1 if is_black else -1))\
                and occupied_fields[self.y - (1 if is_black else -1)][self.x - (1 if is_black else -1)] == (1 if is_black else -1):
            valid_positions.append([self.x - (1 if is_black else -1), self.y - (1 if is_black else -1)])
        return valid_positions

    # Returns set of fields that can be only attacked by Pawns of opposite color
    # with fields that are taken by Pawns of same color
    def get_threaten_fields(self, all_heroes, king_color):
        threaten_fields = []
        for hero in all_heroes:
            if hero.__class__.__name__ == 'Pawn':
                if hero.color != king_color:
                    if self.is_inside_chessboard(hero.x + 1, hero.y + (1 if hero.color == self.white_color else -1)):
                        if [hero.x + 1, hero.y + 1 if hero.color == self.white_color else -1] not in threaten_fields:
                            threaten_fields.append([hero.x + 1, hero.y + (1 if hero.color == self.white_color else -1)])
                    if self.is_inside_chessboard(hero.x - 1, hero.y + (1 if hero.color == self.white_color else -1)):
                        if [hero.x - 1, hero.y + (1 if hero.color == self.white_color else -1)] not in threaten_fields:
                            threaten_fields.append([hero.x - 1, hero.y + (1 if hero.color == self.white_color else -1)])
                else:
                    threaten_fields.append([hero.x, hero.y])
        return threaten_fields
