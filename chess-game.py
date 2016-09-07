import random
try:
    from tkinter import *
except ImportError:
    from Tkinter import *


class Game:

    def __init__(self):
        self.root = Tk()
        self.clicks = 0
        self.canvas = Canvas(self.root, width=256, height=256)
        self.canvas.pack()

    def draw_chessboard(self, color):
        x1 = 0
        y1 = 0
        x2 = 32
        self.canvas.create_rectangle(0, 0, 256, 256, fill=color)

        for i in range(8):
            for j in range(4):
                if color == "black":
                    self.canvas.create_rectangle(x1, y1, x2, y1 + 32, fill="white")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y1 + 32, fill="black")
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

    def __init__(self, pos_x, pos_y, field_width, board_width):
        self.x = pos_x
        self.y = pos_y
        self.field_side = field_width
        self.board_side = board_width

    def move_random(self):
        direction = random.randint(0, 4)
        # Movement right
        if direction == 0 and self.x + self.field_side <= self.board_side:
            self.x += self.field_side
        # Movement left
        elif direction == 1 and self.x - self.field_side > 0:
            self.x -= self.field_side
        # Movement up
        elif direction == 2 and self.y - self.field_side > 0:
            self.y -= self.field_side
        # Movement down
        elif direction == 3 and self.y + self.field_side <= self.board_side:
            self.y += self.field_side









chessboard = Game()

chessboard.draw_chessboard("black")

chessboard.root.mainloop()