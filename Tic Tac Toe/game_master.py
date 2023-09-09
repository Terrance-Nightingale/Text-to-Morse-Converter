class TicTacToe:

    def __init__(self):
        self.positions = [" " for _ in range(0, 9)]
        self.game_board = f" ___________\n" \
                          f"| {self.positions[0]} | {self.positions[1]} | {self.positions[2]} |\n" \
                          f"|___|___|___|\n" \
                          f"| {self.positions[3]} | {self.positions[4]} | {self.positions[5]} |\n" \
                          f"|___|___|___|\n" \
                          f"| {self.positions[6]} | {self.positions[7]} | {self.positions[8]} |\n" \
                          f"|___|___|___|\n" \
