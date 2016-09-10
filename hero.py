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
            if cur_hero.x == prey_coords[0] and cur_hero.y == prey_coords[1]:
                prey = cur_hero
                break
        if prey is not None:
            if self.color == 'wheat':
                if abs(self.x - prey.x) != self.field_side or prey.y != self.y + self.field_side or prey.color == self.color:
                    prey = False
            else:
                if abs(self.x - prey.x) != self.field_side or prey.y != self.y - self.field_side or prey.color == self.color:
                    prey = False
        return prey


class Rook(Hero):
    def move(self, prey_coords, all_heroes):
        prey = self.get_prey(prey_coords, all_heroes)
        # I want to go forward or back
        if prey_coords[0] == self.x:
            # Do I want to go back?
            if prey_coords[1] > self.y:
                # Is there any piece in my way?
                for block_piece in self.all_heroes:
                    if prey_coords[0] == block_piece.x and prey_coords[1] > block_piece.y > self.y:
                        return
                self.y = prey_coords[1]
            # I want to go forward.
            else:
                # Is there any piece in my way?
                for block_piece in self.all_heroes:
                    if prey_coords[0] == block_piece.x and prey_coords[1] < block_piece.y < self.y:
                        return
                self.y = prey_coords[1]
        # I want to go left or right.
        elif prey_coords[1] == self.y:
            # Do I want to go left?
            if prey_coords[0] < self.x:
                # Is there any piece in my way?
                for block_piece in self.all_heroes:
                    if prey_coords[1] == block_piece.y and prey_coords[0] < block_piece.x < self.x:
                        return
                self.x = prey_coords[0]
                self.draw_hero()
            # I want to go right.
            else:
                # Is there any piece in my way?
                for block_piece in self.all_heroes:
                    if prey_coords[1] == block_piece.y and prey_coords[0] > block_piece.x > self.x:
                        return
                self.x = prey_coords[0]
                self.draw_hero()
        # Forbidden field for rook
        else:
            return
        if prey is not None:
            self.execute(prey, all_heroes)
        self.draw_hero()
        return


class Knight(Hero):
    def move(self, prey_coords, all_heroes):
        prey = self.get_prey(prey_coords, all_heroes)
        if (prey_coords == [self.x + self.field_width, self.y - 2 * self.field_width] or
                    prey_coords == [self.x - self.field_width, self.y - 2 * self.field_width] or
                    prey_coords == [self.x - 2 * self.field_width, self.y - self.field_width] or
                    prey_coords == [self.x - 2 * self.field_width, self.y + self.field_width] or
                    prey_coords == [self.x - self.field_width, self.y + 2 * self.field_width] or
                    prey_coords == [self.x + self.field_width, self.y + 2 * self.field_width] or
                    prey_coords == [self.x + 2 * self.field_width, self.y + self.field_width] or
                    prey_coords == [self.x + 2 * self.field_width, self.y - self.field_width]):
            self.x = prey_coords[0]
            self.y = prey_coords[1]
            if prey is not None:
                self.execute(prey, all_heroes)
            self.draw_hero()
            return


class Bishop(Hero):
    def move(self):
        pass


class Queen(Hero):
    def move(self):
        pass


class King(Queen):
    def move(self):
        pass