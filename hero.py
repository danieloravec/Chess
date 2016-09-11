import settings


class Hero:
    def __init__(self, pos_x, pos_y, hero_color, field_width, board_width):
        self.x = pos_x
        self.y = pos_y
        self.field_side = field_width
        self.board_side = board_width
        self.hero = None
        self.color = hero_color

    def __str__(self):
        return str(self.x) + str(self.y)

    def remove_old(self):
        settings.canvas.delete(self.hero)
        self.hero = None

    def draw_hero(self, event=None):
        self.remove_old()
        self.hero = settings.canvas.create_oval(
            self.x, self.y,
            self.x + self.field_side, self.y + self.field_side,
            fill=self.color
        )

    def execute(self, prey, all_heroes):
        self.x = prey.x
        self.y = prey.y
        settings.canvas.delete(prey.hero)
        all_heroes.remove(prey)

    def get_prey(self, prey_coords, all_heroes):
        prey = None
        for cur_hero in all_heroes:
            if cur_hero.x == prey_coords[0] and cur_hero.y == prey_coords[1]:
                prey = cur_hero
                break
        return prey


class Pawn(Hero):
    def move(self, prey_coords, all_heroes):
        prey = self.get_prey(prey_coords, all_heroes)
        if prey is False:
            return
        if self.color == 'wheat':
            if prey_coords == [self.x, self.y + self.field_side] and prey is None:
                self.y += self.field_side
            elif self.y == self.field_side and prey_coords == [self.x, self.y + 2 * self.field_side]:
                self.y += 2 * self.field_side
        else:
            if prey_coords == [self.x, self.y - self.field_side] and prey is None:
                self.y -= self.field_side
            elif self.y == 6 * self.field_side and prey_coords == [self.x, self.y - 2 * self.field_side]:
                self.y -= 2 * self.field_side
        if prey is not None:
            self.execute(prey, all_heroes)
        self.draw_hero()

    def get_prey(self, prey_coords, all_heroes):
        prey = None
        for cur_hero in all_heroes:
            if [cur_hero.x, cur_hero.y] == prey_coords:
                prey = cur_hero
                break
        if prey is not None:
            if (abs(self.x - prey.x) != self.field_side
                    or prey.y != (self.y + self.field_side if self.color == 'wheat' else self.y - self.field_side)
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
                if prey_coords[1] > self.y:
                    if not self.is_rook_obstacle(prey_coords, all_heroes):
                        self.y = prey_coords[1]
                else:
                    if not self.is_rook_obstacle(prey_coords, all_heroes):
                        self.y = prey_coords[1]
            elif prey_coords[1] == self.y:
                if prey_coords[0] < self.x:
                    if not self.is_rook_obstacle(prey_coords, all_heroes):
                        self.x = prey_coords[0]
                else:
                    if not self.is_rook_obstacle(prey_coords, all_heroes):
                        self.x = prey_coords[0]
        self.draw_hero()
        if prey:
            if not self.is_rook_obstacle(prey_coords, all_heroes):
                self.execute(prey, all_heroes)
        self.draw_hero()
        return

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
        if (prey_coords == [self.x + self.field_side, self.y - 2 * self.field_side] or
                    prey_coords == [self.x - self.field_side, self.y - 2 * self.field_side] or
                    prey_coords == [self.x - 2 * self.field_side, self.y - self.field_side] or
                    prey_coords == [self.x - 2 * self.field_side, self.y + self.field_side] or
                    prey_coords == [self.x - self.field_side, self.y + 2 * self.field_side] or
                    prey_coords == [self.x + self.field_side, self.y + 2 * self.field_side] or
                    prey_coords == [self.x + 2 * self.field_side, self.y + self.field_side] or
                    prey_coords == [self.x + 2 * self.field_side, self.y - self.field_side]):
            self.x = prey_coords[0]
            self.y = prey_coords[1]
            if prey is not None:
                self.execute(prey, all_heroes)
            self.draw_hero()
            return

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
        self.draw_hero()

    def is_obstacle(self, prey_coords, all_heroes):
        target_x = []
        target_y = []
        temp_x = self.x
        temp_y = self.y
        if temp_x < prey_coords[0]:
            while temp_x < prey_coords[0]:
                temp_x += self.field_side
                target_x.append(temp_x)
        else:
            while temp_x > prey_coords[0]:
                temp_x -= self.field_side
                target_x.append(temp_x)
        if temp_y < prey_coords[1]:
            while temp_y < prey_coords[1]:
                temp_y += self.field_side
                target_y.append(temp_y)
        else:
            while temp_y > prey_coords[1]:
                temp_y -= self.field_side
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
    def move(self):
        pass
