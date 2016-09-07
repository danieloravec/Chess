import random
try:
    from tkinter import *
except ImportError:
    from Tkinter import *


root = Tk()
canvas = Canvas(root, width=256, height=256)
canvas.pack()

class Game:

    def __init__(self):
        self.clicks = 0

    def draw_chessboard(self, color):
        x1 = 0
        y1 = 0
        x2 = 32
        canvas.create_rectangle(0, 0, 256, 256, fill=color)

        for i in range(8):
            for j in range(4):
                if color == "black":
                    canvas.create_rectangle(x1, y1, x2, y1 + 32, fill="white")
                else:
                    canvas.create_rectangle(x1, y1, x2, y1 + 32, fill="black")
                x1 += 64
                if x2 + 64 <= 256:
                    x2 += 64
                else:
                    x2 += 32
            y1 += 32
            if i % 2 == 0:
                x1 = 32
                x2 = 64
            else:
                x1 = 0
                x2 = 32

    def change_chessboard(self, pos):
        if self.clicks % 2 == 1:
            self.draw_chessboard("black")
        else:
            self.draw_chessboard("white")
        self.clicks
        self.clicks += 1


class Hero:

    def __init__(self, field_width, board_width):
        self.x = board_width / 2
        self.y = board_width / 2
        self.field_side = field_width
        self.board_side = board_width
        self.act_hero = None

    def move_random(self):
        direction = random.randint(0, 4)
        # Movement right
        if direction == 0 and self.x + self.field_side <= self.board_side:
            print("0")
            self.x += self.field_side
            canvas.delete(self.act_hero)
            self.act_hero = None
        # Movement left
        elif direction == 1 and self.x - self.field_side > 0:
            print("1")
            self.x -= self.field_side
            canvas.delete(self.act_hero)
            self.act_hero = None
        # Movement up
        elif direction == 2 and self.y - self.field_side > 0:
            print("2")
            self.y -= self.field_side
            canvas.delete(self.act_hero)
            self.act_hero = None
        # Movement down
        elif direction == 3 and self.y + self.field_side <= self.board_side:
            print("3")
            self.y += self.field_side
            canvas.delete(self.act_hero)
            self.act_hero = None

    def draw_hero(self, pos):
        print("drawing")
        hero.move_random()
        if self.act_hero is None:
            self.act_hero = canvas.create_rectangle(hero.x, hero.y, hero.x + 32, hero.y + 32, fill='red')

chessboard = Game()
hero = Hero(32, 256)
chessboard.draw_chessboard("black")
canvas.bind("<Button-1>", hero.draw_hero)
root.mainloop()
