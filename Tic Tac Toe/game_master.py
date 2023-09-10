from random import randint
from time import sleep


class TicTacToe:

    def __init__(self):
        self.player_score = 0
        self.comp_score = 0
        self.playing = True
        self.positions = []
        self.approved_moves = [_ for _ in range(1, 10)]
        self.board_state = []
        self.game_board = None

    def play_game(self):
        self.positions = [(_ + 1) for _ in range(0, 9)]
        self.update_board()
        print("Welcome to Tic Tac Toe!")
        while self.playing:
            self.player_move()
            self.check_winner()
            if not self.playing:
                return

            self.comp_move()
            self.check_winner()
            if not self.playing:
                return

    def player_move(self):
        can_move = False
        try:
            chosen_pos = int(input("Please make your move by typing a number from 1-9 "
                                   "(whole numbers only): ")) - 1
            if chosen_pos not in range(0, 9) or self.positions[chosen_pos] not in self.approved_moves:
                raise ValueError
            else:
                can_move = True
                self.positions[chosen_pos] = "X"
                self.update_board()
        except ValueError:
            while not can_move:
                try:
                    chosen_pos = int(input("Incorrect input. Please make your move by typing a number from 1-9 "
                                           "(whole numbers only): ")) - 1
                    if chosen_pos not in range(0, 9) or self.positions[chosen_pos] not in self.approved_moves:
                        raise ValueError
                    else:
                        can_move = True
                        self.positions[chosen_pos] = "X"
                        self.update_board()
                except ValueError:
                    pass

    def comp_move(self):
        print("Computer is thinking...")
        sleep(2)
        chosen_pos = randint(0, len(self.positions) - 1)
        print(f"Computer's move: Position {chosen_pos + 1}")
        can_move = False
        while not can_move:
            if self.positions[chosen_pos] not in self.approved_moves:
                chosen_pos = randint(0, len(self.positions) - 1)
                print(f"Chosen comp position now = {chosen_pos + 1}")
            else:
                can_move = True
        self.positions[chosen_pos] = "O"
        self.update_board()

    def update_board(self):
        rows = 3
        self.board_state = [[self.positions[_] for _ in range(0,3)],
                            [self.positions[_] for _ in range(3,6)],
                            [self.positions[_] for _ in range(6,9)]]
        self.game_board = f" ___________\n"
        for _ in range(0, rows):
            count = _ * 3
            self.game_board += f"| {self.positions[count]} | {self.positions[count+1]} | {self.positions[count+2]} |\n" \
                               f"|___|___|___|\n"
        print(self.game_board)

    def check_winner(self):
        #--- Check columns ---#
        self.player_score = 0
        self.comp_score = 0
        for row in self.board_state:
            if row[0] == "X":
                self.player_score += 1
            elif row[0] == "O":
                self.comp_score += 1
            else:
                continue
        if self.player_score == 3 or self.comp_score == 3:
            self.playing = False
            self.declare_winner()
            return

        #--- Check rows ---#
        self.player_score = 0
        self.comp_score = 0
        for row in self.board_state:
            for symbol in row:
                if symbol == "X":
                    self.player_score += 1
                elif symbol == "O":
                    self.comp_score += 1
                else:
                    continue
        if self.player_score == 3 or self.comp_score == 3:
            self.playing = False
            self.declare_winner()
            return

        #--- Check diagonals ---#
        # starting_pos = 0
        # for row in self.board_state:
        #     row[starting_pos]

    def declare_winner(self):
        #--- Return winner if any ---#
        if self.player_score == 3:
            print("Congratulations! You win!")
            self.play_again()
        elif self.comp_score == 3:
            print("You lose.")
            self.play_again()

    def play_again(self):
        legal_choices = ("Y", "N")
        choice = input("Play again? Y/N: ").upper()
        while choice not in legal_choices:
            choice = input("Incorrect input. Play again? Y/N: ").upper()
        if choice == "Y":
            self.playing = True
            self.play_game()
        elif choice == "N":
            print("Thank you for playing!")
            self.playing = False
