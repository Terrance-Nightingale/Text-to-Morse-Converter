from random import randint
from time import sleep


class TicTacToe:

    def __init__(self):
        self.playing = True
        self.positions = [(_ + 1) for _ in range(0, 9)]
        self.approved_moves = [_ for _ in range(0, 9)]
        self.game_board = f" ___________\n"
        self.update_board()
        print("Welcome to Tic Tac Toe!")

    def play_game(self):
        while self.playing:
            self.player_move()
            self.check_winner()
            if not self.playing:
                break

            self.comp_move()
            self.check_winner()
            if not self.playing:
                break

    def play_again(self):
        choice = input("Play again? Y/N: ").upper()
        if choice == "Y":
            return True
        elif choice == "N":
            return False

    def player_move(self):
        can_move = False
        try:
            chosen_pos = int(input("Please make your move by typing a number from 1-9 "
                                   "(whole numbers only): ")) - 1
            if chosen_pos in range(0, 9):
                can_move = True
                self.positions[chosen_pos] = "X"
                self.update_board()
            else:
                raise ValueError
        except ValueError:
            while not can_move:
                try:
                    chosen_pos = int(input("Incorrect input. Please make your move by typing a number from 1-9 "
                                           "(whole numbers only): ")) - 1
                    if chosen_pos in range(0, 9):
                        can_move = True
                        print(chosen_pos)
                        self.positions[chosen_pos] = "X"
                        self.update_board()
                    else:
                        raise ValueError
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
        self.board_state = [[self.positions[_] for _ in range(0,3)],
                            [self.positions[_] for _ in range(3,6)],
                            [self.positions[_] for _ in range(6,9)]]
        self.game_board = f" ___________\n"
        for _ in range(0, rows):
            count = _ * 3
            self.game_board += f"| {self.positions[count]} | {self.positions[count+1]} | {self.positions[count+2]} |\n" \
                               f"|___|___|___|\n"
        print(self.board_state)
        print(self.game_board)

    def check_winner(self):
        player_score = 0
        comp_score = 0
        player_win = False
        comp_win = False
        #--- Check columns ---#
        for row in self.board_state:
            if row[0] == "X":
                player_score += 1
            elif row[0] == "O":
                comp_score += 1
            else:
                pass

        #--- Check rows ---#
        for row in self.board_state:
            for symbol in row:
                if symbol == "X":
                    player_score += 1
                elif symbol == "O":
                    comp_score += 1
                else:
                    pass

        #--- Check diagonals ---#
        # starting_pos = 0
        # for row in self.board_state:
        #     row[starting_pos]

        #--- Return winner if any ---#
        if player_score == 3:
            print("Congratulations! You win!")
            self.play_again()
        elif comp_score == 3:
            print("You lose.")
            self.play_again()
        else:
            pass
