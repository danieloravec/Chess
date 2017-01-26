from figures.hero import Hero

d8y = [1, 1, 0, -1, -1, -1, 0, 1]
d8x = [0, 1, 1, 1, 0, -1, -1, -1]
d4x = [0, 1, 0, -1]
d4y = [1, 0, -1, 0]


class Bishop(Hero):
    def move(self, prey_coords, all_heroes):
        return self.move_bishop(prey_coords, all_heroes)

    def move_bishop(self, prey_coords, all_heroes):
        prey = self.get_prey(prey_coords, all_heroes)
        if self.is_obstacle(prey_coords, all_heroes):
            return False
        else:
            if prey is False:
                return False
            elif prey is None:
                self.x = prey_coords[0]
                self.y = prey_coords[1]
            else:
                self.execute(prey, all_heroes)
        return True

    def is_obstacle(self, prey_coords, all_heroes):
        target_x = []
        target_y = []
        temp_x = self.x
        temp_y = self.y
        if temp_x < prey_coords[0]:
            while temp_x < prey_coords[0]:
                temp_x += 1
                target_x.append(temp_x)
        else:
            while temp_x > prey_coords[0]:
                temp_x -= 1
                target_x.append(temp_x)
        if temp_y < prey_coords[1]:
            while temp_y < prey_coords[1]:
                temp_y += 1
                target_y.append(temp_y)
        else:
            while temp_y > prey_coords[1]:
                temp_y -= 1
                target_y.append(temp_y)
        if len(target_x) == len(target_y) > 0:
            target_x.pop()
            target_y.pop()
        else:
            return True
        for block_piece in all_heroes:
            for i in range(len(target_x)):
                if block_piece is self:
                    continue
                if (block_piece.x, block_piece.y) == (target_x[i], target_y[i]):
                    return True
        return False

    def get_prey(self, prey_coords, all_heroes):
        prey = None
        for cur_hero in all_heroes:
            if prey_coords == [cur_hero.x, cur_hero.y]:
                prey = cur_hero
                break
        if prey is not None:
            if (prey_coords[0] == self.x and prey_coords[1] == self.y) or prey.color == self.color:
                prey = False
        return prey

    def get_valid_moves_by_direction(self, x_increment, y_increment, occupied_fields):
        direction_valid_moves = []
        cur_x = self.x + x_increment
        cur_y = self.y + y_increment
        while self.is_inside_chessboard(cur_x, cur_y) \
                and occupied_fields[cur_y][cur_x] != (1 if self.color == self.white_color else -1):
            direction_valid_moves.append([cur_x, cur_y])
            if occupied_fields[cur_y][cur_x] != 0:
                break
            cur_x += x_increment
            cur_y += y_increment
        return direction_valid_moves

    def get_valid_moves_bishop(self, occupied_fields):
        valid_moves = []
        valid_moves += self.get_valid_moves_by_direction(1, 1, occupied_fields)
        valid_moves += self.get_valid_moves_by_direction(1, -1, occupied_fields)
        valid_moves += self.get_valid_moves_by_direction(-1, 1, occupied_fields)
        valid_moves += self.get_valid_moves_by_direction(-1, -1, occupied_fields)
        return valid_moves

    def get_valid_moves(self, occupied_fields, all_heroes):
        return self.get_valid_moves_bishop(occupied_fields)
