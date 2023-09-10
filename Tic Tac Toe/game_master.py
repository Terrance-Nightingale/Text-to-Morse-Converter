from random import randint


class TicTacToe:

    def __init__(self):
        self.positions = [" " for _ in range(0, 9)]
        self.game_board = f" ___________\n"\
                          f"| {self.positions[0]} | {self.positions[1]} | {self.positions[2]} |\n" \
                          f"|___|___|___|\n" \
                          f"| {self.positions[3]} | {self.positions[4]} | {self.positions[5]} |\n" \
                          f"|___|___|___|\n" \
                          f"| {self.positions[6]} | {self.positions[7]} | {self.positions[8]} |\n" \
                          f"|___|___|___|\n"
        self.chosen_pos = 0

    def player_move(self):
        pass

    def comp_move(self):
        self.chosen_pos = randint(0, len(self.positions) - 1)
        can_move = False
        while not can_move:
            if self.positions[self.chosen_pos] != " ":
                self.chosen_pos = randint(0, len(self.positions) - 1)
            else:
                can_move = True
        self.positions[self.chosen_pos] = "O"
        self.update_board()

    def update_board(self):
        self.game_board = f" ___________\n"\
                          f"| {self.positions[0]} | {self.positions[1]} | {self.positions[2]} |\n" \
                          f"|___|___|___|\n" \
                          f"| {self.positions[3]} | {self.positions[4]} | {self.positions[5]} |\n" \
                          f"|___|___|___|\n" \
                          f"| {self.positions[6]} | {self.positions[7]} | {self.positions[8]} |\n" \
                          f"|___|___|___|\n" \

