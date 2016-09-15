from chess_game import Game
import settings


class Visualiser:
    def __init__(self):
        self.field_side = 100
        self.board_side = self.field_side * 8
        self.game = Game()
        settings.init(self.board_side, self.board_side)

    def draw_chessboard(self, color):
        x1 = 0
        y1 = 0
        x2 = self.field_side
        settings.canvas.create_rectangle(0, 0, self.board_side, self.board_side, fill=color)

        for i in range(8):
            for j in range(4):
                if color == "black":
                    settings.canvas.create_rectangle(x1, y1, x2, y1 + self.field_side, fill="white")
                else:
                    settings.canvas.create_rectangle(x1, y1, x2, y1 + self.field_side, fill="black")
                x1 += self.field_side * 2
                if x2 + self.field_side * 2 <= self.board_side:
                    x2 += self.field_side * 2
                else:
                    x2 += self.field_side
            y1 += self.field_side
            if i % 2 == 0:
                x1 = self.field_side
                x2 = x1 * 2
            else:
                x1 = 0
                x2 = self.field_side

    def move_and_redraw(self, event, hero_to_move):
        self.game.move_if_possible(
            (event.x - event.x % self.field_side) // self.field_side,
            (event.y - event.y % self.field_side) // self.field_side,
            hero_to_move
        )
        self.redraw_situation()

    def move_clicked(self, click_pos):
        searched_coords = [
            (click_pos.x - (click_pos.x % self.field_side)) // self.field_side,
            (click_pos.y - (click_pos.y % self.field_side)) // self.field_side
        ]
        for cur_hero in self.game.all_heroes:
            if [cur_hero.x, cur_hero.y] == searched_coords:
                settings.canvas.bind('<Button-3>', lambda event, current_hero = cur_hero: self.move_and_redraw(event, current_hero))

    def redraw_situation(self):
        settings.canvas.delete("all")
        self.draw_chessboard("black")
        for cur_hero in self.game.all_heroes:
            settings.canvas.create_oval(
                cur_hero.x * self.field_side, cur_hero.y * self.field_side,
                cur_hero.x * self.field_side + self.field_side, cur_hero.y * self.field_side + self.field_side,
                fill=cur_hero.color
            )
            settings.canvas.create_text(
                cur_hero.x * self.field_side + self.field_side // 2,
                cur_hero.y * self.field_side + self.field_side // 2,
                text=cur_hero.__class__.__name__
            )
