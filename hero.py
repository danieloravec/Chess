import json


class Hero:
    def __init__(self, args_list):
        self.x = args_list[0]
        self.y = args_list[1]
        self.board_side = 8
        self.color = args_list[2]

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


class Pawn(Hero):
    def move(self, prey_coords, all_heroes):
        prey = self.get_prey(prey_coords, all_heroes)
        if prey is False:
            return
        y_modificator = 1 if self.color == "wheat" else -1
        color_y_position = 1 if self.color == "wheat" else 6
        if prey_coords == [self.x, self.y + y_modificator] and prey is None:
            self.y += y_modificator
        elif self.y == color_y_position and prey_coords == [self.x, self.y + 2 * y_modificator]:
            if not self.is_obstacle(prey_coords, all_heroes):
                self.y += 2 * y_modificator
        if prey is not None:
            self.execute(prey, all_heroes)

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
                    or prey.y != (self.y + 1 if self.color == 'wheat' else self.y - 1)
                    or prey.color == self.color):
                prey = False
        return prey


class Rook(Hero):
    def move(self, prey_coords, all_heroes):
        self.move_rook(prey_coords, all_heroes)

    def move_rook(self, prey_coords, all_heroes):
        prey = self.get_rook_prey(prey_coords, all_heroes)
        if prey is False:
            return
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


class Knight(Hero):
    def move(self, prey_coords, all_heroes):
        prey = self.get_prey(prey_coords, all_heroes)
        if prey is False:
            return
        if self.can_move(prey_coords):
            self.x = prey_coords[0]
            self.y = prey_coords[1]
            if prey is not None:
                self.execute(prey, all_heroes)

    def can_move(self, prey_coords):
        if (prey_coords == [self.x + 1, self.y - 2 * 1] or
                prey_coords == [self.x - 1, self.y - 2 * 1] or
                prey_coords == [self.x - 2 * 1, self.y - 1] or
                prey_coords == [self.x - 2 * 1, self.y + 1] or
                prey_coords == [self.x - 1, self.y + 2 * 1] or
                prey_coords == [self.x + 1, self.y + 2 * 1] or
                prey_coords == [self.x + 2 * 1, self.y + 1] or
                prey_coords == [self.x + 2 * 1, self.y - 1]):
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


class Bishop(Hero):
    def move(self, prey_coords, all_heroes):
        self.move_bishop(prey_coords, all_heroes)

    def move_bishop(self, prey_coords, all_heroes):
        prey = self.get_prey(prey_coords, all_heroes)
        if self.is_obstacle(prey_coords, all_heroes):
            return
        else:
            if prey is False:
                return
            elif prey is None:
                self.x = prey_coords[0]
                self.y = prey_coords[1]
            else:
                self.execute(prey, all_heroes)

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


class Queen(Rook, Bishop):
    def move(self, prey_coords, all_heroes):
        if self.x == prey_coords[0] or self.y == prey_coords[1]:
            self.move_rook(prey_coords, all_heroes)
        else:
            self.move_bishop(prey_coords, all_heroes)


class King(Hero):
    def move(self, prey_coords, all_heroes):
        prey = self.get_prey(prey_coords, all_heroes)
        if prey is False:
            return
        if self.is_obstacle(prey_coords, all_heroes):
            return
        elif abs(prey_coords[0] - self.x) <= 1 and abs(prey_coords[1] - self.y) <= 1:
            if prey is not None:
                self.execute(prey, all_heroes)
            else:
                self.x = prey_coords[0]
                self.y = prey_coords[1]
