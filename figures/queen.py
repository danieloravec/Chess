from figures.rook import Rook
from figures.bishop import Bishop

d8y = [1, 1, 0, -1, -1, -1, 0, 1]
d8x = [0, 1, 1, 1, 0, -1, -1, -1]
d4x = [0, 1, 0, -1]
d4y = [1, 0, -1, 0]


class Queen(Rook, Bishop):
    def move(self, prey_coords, all_heroes):
        if self.x == prey_coords[0] or self.y == prey_coords[1]:
            return self.move_rook(prey_coords, all_heroes)
        else:
            return self.move_bishop(prey_coords, all_heroes)

    def get_valid_moves(self, occupied_fields, all_heroes):
        valid_moves = self.get_valid_moves_bishop(occupied_fields)
        valid_moves += self.get_valid_moves_rook(occupied_fields)
        return valid_moves
