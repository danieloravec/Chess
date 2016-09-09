import random
import settings


class Hero:
    def __init__(self, pos_x, pos_y, field_width, board_width):
        self.x = pos_x
        self.y = pos_y
        self.field_side = field_width
        self.board_side = board_width
        self.hero = None

    def __str__(self):
        return str(self.x) + str(self.y)

    def move_random(self):
        if self.hero is not None:
            direction = random.randint(0, 3)
            # Movement right
            if direction == 0 and self.x + self.field_side < self.board_side:
                self.x += self.field_side
                settings.canvas.delete(self.hero)
                self.hero = None
            # Movement left
            elif direction == 1 and self.x - self.field_side >= 0:
                self.x -= self.field_side
                settings.canvas.delete(self.hero)
                self.hero = None
            # Movement up
            elif direction == 2 and self.y - self.field_side >= 0:
                self.y -= self.field_side
                settings.canvas.delete(self.hero)
                self.hero = None
            # Movement down
            elif direction == 3 and self.y + self.field_side < self.board_side:
                self.y += self.field_side
                settings.canvas.delete(self.hero)
                self.hero = None

    def draw_hero(self, event = None):
        self.move_random()
        if self.hero is None:
            self.hero = settings.canvas.create_oval(
                self.x, self.y,
                self.x + self.field_side, self.y + self.field_side,
                fill='red'
            )
