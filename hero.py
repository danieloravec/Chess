import random
import settings


# TODO remove duplicate code
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

    # def move_random(self, direction=None):
    #     if direction is None:
    #         direction = random.randint(0, 3)
    #     if self.hero is not None:
    #         # Movement right
    #         if direction == 0 and self.x + self.field_side < self.board_side:
    #             self.x += self.field_side
    #         # Movement left
    #         elif direction == 1 and self.x - self.field_side >= 0:
    #             self.x -= self.field_side
    #         # Movement up
    #         elif direction == 2 and self.y - self.field_side >= 0:
    #             self.y -= self.field_side
    #         # Movement down
    #         elif direction == 3 and self.y + self.field_side < self.board_side:
    #             self.y += self.field_side
    #         self.remove_old()

    def draw_hero(self, event=None):
        self.remove_old()
        self.hero = settings.canvas.create_oval(
            self.x, self.y,
            self.x + self.field_side, self.y + self.field_side,
            fill=self.color
        )


class Pawn(Hero):
    pass
    # def move_random(self):
    #     if self.color is 'snow4':
    #         super(Pawn, self).move_random(2)
    #     else:
    #         super(Pawn, self).move_random(3)


class Knight(Hero):
    pass
    # def move_random(self, direction=None):
    #     if direction is None:
    #         direction = random.randint(0, 7)
    #     if self.hero is not None:
    #         # Forward-right motion
    #         if direction == 0 and self.x + self.field_side < self.board_side and self.y - 2 * self.field_side >= 0:
    #             self.x += self.field_side
    #             self.y -= 2 * self.field_side
    #         # Forward-left motion
    #         elif direction == 1 and self.x - self.field_side >= 0 and self.y - 2 * self.field_side >= 0:
    #             self.x -= self.field_side
    #             self.y -= 2 * self.field_side
    #         # Left-forward motion
    #         elif direction == 2 and self.x - 2 * self.field_side >= 0 and self.y - self.field_side >= 0:
    #             self.x -= 2 * self.field_side
    #             self.y -= self.field_side
    #         # Left-back motion
    #         elif direction == 3 and self.x - 2 * self.field_side >= 0 and self.y + self.field_side < self.board_side:
    #             self.x -= 2 * self.field_side
    #             self.y += self.field_side
    #         # Back-left motion
    #         elif direction == 4 and self.x - self.field_side >= 0 and self.y + 2 * self.field_side < self.board_side:
    #             self.x -= self.field_side
    #             self.y += 2 * self.field_side
    #         # Back-right motion
    #         elif direction == 5 and self.x + self.field_side <= self.board_side and self.y + 2 * self.field_side < self.board_side:
    #             self.x += self.field_side
    #             self.y += 2 * self.field_side
    #         # Right-back motion
    #         elif direction == 6 and self.x + 2 * self.field_side < self.board_side and self.y + self.field_side < self.board_side:
    #             self.x += 2 * self.field_side
    #             self.y += self.field_side
    #         # Right-forward motion
    #         elif direction == 7 and self.x + 2 * self.field_side < self.board_side and self.y - self.field_side >= 0:
    #             self.x += 2 * self.field_side
    #             self.y -= self.field_side
    #         self.remove_old()


class Bishop(Hero):
    pass
    # def move_random(self, direction=None):
    #     if direction is None:
    #         direction = random.randint(0, 3)
    #     if self.hero is not None:
    #         # Forward-right movement
    #         if direction == 0 and self.x + self.field_side < self.board_side and self.y - self.field_side >= 0:
    #             self.x += self.field_side
    #             self.y -= self.field_side
    #         # Forward-left movement
    #         elif direction == 1 and self.x - self.field_side >= 0 and self.y - self.field_side:
    #             self.x -= self.field_side
    #             self.y -= self.field_side
    #         # Back-left movement
    #         elif direction == 2 and self.x - self.field_side >= 0 and self.y + self.field_side < self.board_side:
    #             self.x -= self.field_side
    #             self.y += self.field_side
    #         # Back-right motion
    #         elif direction == 3 and self.x + self.field_side < self.board_side and self.y + self.field_side < self.board_side:
    #             self.x += self.field_side
    #             self.y += self.field_side
    #         self.remove_old()


class Rook(Hero):
    pass


class Queen(Hero):
    pass
    # def move_random(self, direction=None):
    #     if direction is None:
    #         direction = random.randint(0, 7)
    #     if self.hero is not None:
    #         # Forward-right movement
    #         if direction == 0 and self.x + self.field_side < self.board_side and self.y - self.field_side >= 0:
    #             self.x += self.field_side
    #             self.y -= self.field_side
    #         # Forward-left movement
    #         elif direction == 1 and self.x - self.field_side >= 0 and self.y - self.field_side:
    #             self.x -= self.field_side
    #             self.y -= self.field_side
    #         # Back-left movement
    #         elif direction == 2 and self.x - self.field_side >= 0 and self.y + self.field_side < self.board_side:
    #             self.x -= self.field_side
    #             self.y += self.field_side
    #         # Back-right motion
    #         elif direction == 3 and self.x + self.field_side < self.board_side and self.y + self.field_side < self.board_side:
    #             self.x += self.field_side
    #             self.y += self.field_side
    #         elif direction == 4 and self.x + self.field_side < self.board_side:
    #             self.x += self.field_side
    #         # Movement left
    #         elif direction == 5 and self.x - self.field_side >= 0:
    #             self.x -= self.field_side
    #         # Movement up
    #         elif direction == 6 and self.y - self.field_side >= 0:
    #             self.y -= self.field_side
    #         # Movement down
    #         elif direction == 7 and self.y + self.field_side < self.board_side:
    #             self.y += self.field_side
    #         self.remove_old()


class King(Queen):
    pass




















