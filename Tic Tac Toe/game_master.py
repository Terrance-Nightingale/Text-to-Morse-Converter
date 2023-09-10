from random import randint
from time import sleep


class TicTacToe:

    def __init__(self):
        self.positions = [(_ + 1) for _ in range(0, 9)]
        self.approved_moves = [_ for _ in range(0, 9)]
        self.win_con = [3, 9, 12, 15, 21]
        self.board_state = [[]]
        self.game_board = f" ___________\n"
        self.update_board()
        print("Welcome to Tic Tac Toe!")

    def play_game(self):
        pass

    def player_move(self):
        can_move = False
        try:
            chosen_pos = int(input("Please make your move by typing in a number from 1-9 "
                                        "(whole numbers only): ")) - 1
            can_move = True
            self.positions[chosen_pos] = "X"
            self.update_board()
        except ValueError:
            while not can_move:
                try:
                    chosen_pos = int(input("Incorrect input. Please make your move by typing in a number from 1-9 "
                                                "(whole numbers only): ")) - 1
                    can_move = True
                    self.positions[chosen_pos] = "X"
                    self.update_board()

                except ValueError:
                    pass

    def comp_move(self):
        print("Computer is thinking...")
        sleep(2)
        chosen_pos = randint(0, len(self.positions) - 1)
        print(f"Computer's move: Position {chosen_pos}")
        can_move = False
        while not can_move:
            if self.positions[chosen_pos] not in self.approved_moves:
                chosen_pos = randint(0, len(self.positions) - 1)
                print(f"Chosen comp position now = {chosen_pos}")
            else:
                can_move = True
        self.positions[chosen_pos] = "O"
        self.update_board()

    def update_board(self):
        rows = 3
        self.game_board = f" ___________\n"
        for _ in range(0, rows):
            count = _ * 3
            self.game_board += f"| {self.positions[count]} | {self.positions[count+1]} | {self.positions[count+2]} |\n" \
                               f"|___|___|___|\n"
        print(self.game_board)
