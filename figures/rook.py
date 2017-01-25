from figures.hero import Hero

d8y = [1, 1, 0, -1, -1, -1, 0, 1]
d8x = [0, 1, 1, 1, 0, -1, -1, -1]
d4x = [0, 1, 0, -1]
d4y = [1, 0, -1, 0]


class Rook(Hero):
    def move(self, prey_coords, all_heroes):
        return self.move_rook(prey_coords, all_heroes)

    def move_rook(self, prey_coords, all_heroes):
        prey = self.get_rook_prey(prey_coords, all_heroes)
        if prey is False:
            return False
        if not prey:
            if prey_coords[0] == self.x:
                if not self.is_rook_obstacle(prey_coords, all_heroes):
                    self.y = prey_coords[1]
            elif prey_coords[1] == self.y:
                if not self.is_rook_obstacle(prey_coords, all_heroes):
                    self.x = prey_coords[0]
        if prey:
            if not self.is_rook_obstacle(prey_coords, all_heroes):
                self.execute(prey, all_heroes)
        return True

    def is_rook_obstacle(self, prey_coords, all_heroes):
        for block_piece in all_heroes:
            if block_piece.x == self.x == prey_coords[0]:
                if prey_coords[1] > self.y:
                    if self.y < block_piece.y < prey_coords[1]:
                        return True
                else:
                    if prey_coords[1] < block_piece.y < self.y:
                        return True
            elif block_piece.y == self.y == prey_coords[1]:
                if prey_coords[0] > self.x:
                    if prey_coords[0] > block_piece.x > self.x:
                        return True
                else:
                    if prey_coords[0] < block_piece.x < self.x:
                        return True
        return False

    def get_rook_prey(self, prey_coords, all_heroes):
        prey = None
        for cur_hero in all_heroes:
            if cur_hero.x == prey_coords[0] and cur_hero.y == prey_coords[1]:
                prey = cur_hero
                break
        if prey is not None:
            if ((prey_coords[0] == self.x and prey_coords[1] == self.y)
                    or cur_hero.color == self.color
                    or (self.x != cur_hero.x and self.y != cur_hero.y)):
                prey = False
        return prey

    def get_valid_moves_by_direction(self, x_increment, y_increment, occupied_fields):
        direction_valid_positions = []
        cur_x = self.x + x_increment
        cur_y = self.y + y_increment
        while self.is_inside_chessboard(cur_x, cur_y)\
                and occupied_fields[cur_y][cur_x] != (1 if self.color == self.white_color else -1):
            direction_valid_positions.append([cur_x, cur_y])
            if occupied_fields[cur_y][cur_x] != 0:
                break
            cur_x += x_increment
            cur_y += y_increment
        return direction_valid_positions

    def get_valid_moves_rook(self, occupied_fields):
        valid_positions = []
        for i in range(4):
            valid_positions += self.get_valid_moves_by_direction(d4x[i], d4y[i], occupied_fields)
        return valid_positions

    def get_valid_moves(self, occupied_fields, all_heroes):
        return self.get_valid_moves_rook(occupied_fields)
