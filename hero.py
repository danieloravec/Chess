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


class Pawn(Hero):
    pass


class Knight(Hero):
    pass


class Bishop(Hero):
    pass


class Rook(Hero):
    pass


class Queen(Hero):
    pass


class King(Queen):
    pass
