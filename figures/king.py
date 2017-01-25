from figures.hero import Hero

d8y = [1, 1, 0, -1, -1, -1, 0, 1]
d8x = [0, 1, 1, 1, 0, -1, -1, -1]
d4x = [0, 1, 0, -1]
d4y = [1, 0, -1, 0]


class King(Hero):
    def move(self, prey_coords, all_heroes):
        prey = self.get_prey(prey_coords, all_heroes)
        if prey is False:
            return False
        if self.is_obstacle(prey_coords, all_heroes):
            return
        elif abs(prey_coords[0] - self.x) <= 1 and abs(prey_coords[1] - self.y) <= 1:
            if prey is not None:
                self.execute(prey, all_heroes)
            else:
                self.x = prey_coords[0]
                self.y = prey_coords[1]
        return True

    def get_prey(self, prey_coords, all_heroes):
        for hero in all_heroes:
            if prey_coords == [hero.x, hero.y]:
                if hero.color == self.color:
                    return False
                else:
                    return hero
        return None

    def get_valid_moves(self, occupied_fields, all_heroes):
        check_or_mate, valid_moves = self.check_mate(all_heroes, occupied_fields)
        return valid_moves

    # Returns 0 if none, 1 if check, 2 if mate and returns also list of valid moves
    def check_mate(self, all_heroes, occupied_fields):
        impossible_moves = []
        valid_moves = []
        found_pawn = False
        result = 0
        for hero in all_heroes:
            if hero.__class__.__name__ == 'King':
                if self.color == hero.color:
                    continue
                opposite_king_fields = []
                for i in range(4):
                    if self.is_inside_chessboard(hero.x + d4x[i], hero.y + d4y[i])\
                            and occupied_fields[hero.y + d4y[i]][hero.x + d4x[i]] != (1 if hero.color == self.white_color else -1):
                        opposite_king_fields.append([hero.x + d4x[i], hero.y + d4y[i]])
                impossible_moves += opposite_king_fields
            elif hero.__class__.__name__ == 'Pawn':
                if not found_pawn:
                    found_pawn = True
                    pawn_fields = hero.get_threaten_fields(all_heroes, self.color)
                    for pf in pawn_fields:
                        if pf not in impossible_moves:
                            impossible_moves.append(pf)
            else:
                if hero.color == self.color:
                    impossible_moves.append([hero.x, hero.y])
                    continue
                moves = hero.get_valid_moves(occupied_fields, all_heroes)
                for move in moves:
                    if move not in impossible_moves:
                        impossible_moves.append(move)
        if [self.x, self.y] in impossible_moves:
            result = 1
        for i in range(8):
            if self.is_inside_chessboard(self.x + d8x[i], self.y + d8y[i])\
                    and [self.x + d8x[i], self.y + d8y[i]] not in impossible_moves:
                valid_moves.append([self.x + d8x[i], self.y + d8y[i]])
        if valid_moves == list() and result == 1:
            result = 2
        return result, valid_moves
