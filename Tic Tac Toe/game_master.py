from random import randint


class TicTacToe:

    def __init__(self):
        self.positions = [(_ + 1) for _ in range(0, 9)]
        self.approved_moves = [_ for _ in range(0, 9)]
        self.game_board = f" ___________\n"\
                          f"| {self.positions[0]} | {self.positions[1]} | {self.positions[2]} |\n" \
                          f"|___|___|___|\n" \
                          f"| {self.positions[3]} | {self.positions[4]} | {self.positions[5]} |\n" \
                          f"|___|___|___|\n" \
                          f"| {self.positions[6]} | {self.positions[7]} | {self.positions[8]} |\n" \
                          f"|___|___|___|\n"
        self.chosen_pos = 0
        print(self.game_board)
        print("Welcome to Tic Tac Toe!")

    def play_game(self):
        pass

    def player_move(self):
        can_move = False
        try:
            self.chosen_pos = int(input("Please make your move by typing in a number from 1-9 "
                                        "(whole numbers only): ")) - 1
            can_move = True
            self.positions[self.chosen_pos] = "X"
            self.update_board()
        except ValueError:
            while not can_move:
                try:
                    self.chosen_pos = int(input("Incorrect input. Please make your move by typing in a number from 1-9 "
                                                "(whole numbers only): ")) - 1
                    can_move = True
                    self.positions[self.chosen_pos] = "X"
                    self.update_board()

                except ValueError:
                    pass

    def comp_move(self):
        self.chosen_pos = randint(0, len(self.positions) - 1)
        print(f"Chosen comp position = {self.chosen_pos}")
        can_move = False
        while not can_move:
            if self.positions[self.chosen_pos] not in self.approved_moves:
                self.chosen_pos = randint(0, len(self.positions) - 1)
                print(f"Chosen comp position now = {self.chosen_pos}")
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
                          f"|___|___|___|\n"
        print(self.game_board)
