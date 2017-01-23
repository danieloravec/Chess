try:
    from tkinter import *
except ImportError:
    from Tkinter import *
from chess_game import Game
from menu import Menu


class Visualiser:
    def __init__(self):
        self.field_side = 100
        self.board_side = self.field_side * 8
        self.button_width = self.field_side
        self.button_height = self.field_side // 2
        self.game = Game()
        self.menu = Menu()
        self.root = Tk()
        self.save_button = Button(self.root, width=10, height=2, text='Save', bg='cyan', command=lambda: self.menu.save_game(self.game.all_heroes))
        self.load_button = Button(self.root, width=10, height=2, text='Load', bg='orange', command=lambda: self.menu.load_game(self.game.all_heroes, 'sv'))
        self.canvas = Canvas(self.root, width=self.board_side + self.button_width, height=self.board_side)
        self.canvas.grid(row=0, column=0, rowspan=8, columnspan=8)
        self.save_button.grid(row=0, column=8)
        self.load_button.grid(row=1, column=8)

    def draw_chessboard(self, color):
        fill_color = "white" if color == "black" else "black"
        self.canvas.create_rectangle(0, 0, self.board_side, self.board_side, fill=color)
        for i in range(8):
            y = i * self.field_side
            for j in range(4):
                x = (2 * j) * self.field_side
                if i % 2 == 0:
                    x += self.field_side
                self.canvas.create_rectangle(x, y, x + self.field_side, y + self.field_side, fill=fill_color)

    def move_and_redraw(self, event, hero_to_move):
        self.game.move_if_possible(
            (event.x - event.x % self.field_side) // self.field_side,
            (event.y - event.y % self.field_side) // self.field_side,
            hero_to_move
        )
        self.redraw_situation()

    def move_clicked(self, click_pos):
        searched_coords = (
            (click_pos.x - (click_pos.x % self.field_side)) // self.field_side,
            (click_pos.y - (click_pos.y % self.field_side)) // self.field_side
        )
        for cur_hero in self.game.all_heroes:
            if (cur_hero.x, cur_hero.y) == searched_coords:
                self.canvas.bind('<Button-3>', lambda event, current_hero=cur_hero: self.move_and_redraw(event, current_hero))

    def redraw_situation(self):
        self.canvas.delete("all")
        self.draw_chessboard("black")
        for cur_hero in self.game.all_heroes:
            self.canvas.create_oval(
                cur_hero.x * self.field_side, cur_hero.y * self.field_side,
                (cur_hero.x + 1) * self.field_side, (cur_hero.y + 1) * self.field_side,
                fill=cur_hero.color
            )
            self.canvas.create_text(
                cur_hero.x * self.field_side + self.field_side // 2,
                cur_hero.y * self.field_side + self.field_side // 2,
                text=cur_hero.__class__.__name__
            )
