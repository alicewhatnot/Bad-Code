class Player:
    def __init__(self, name, symbol):
        self.__name = name
        self.__symbol = symbol
        self.__moves_left = 21  # assuming 7x6 board

    def get_name(self):
        return self.__name

    def get_symbol(self):
        return self.__symbol

    def make_move(self, board):
        if self.__moves_left <= 0:
            print(f"{self.__name} has no moves left.")
            return False

        while True:
            try:
                column = int(input(f"{self.__name} ({self.__symbol}), choose a column (0-{board.get_width() - 1}): "))
                if board.add_token(column, self.__symbol):
                    self.__moves_left -= 1
                    return True
                else:
                    print("Column full or invalid. Try again.")
            except ValueError:
                print("Please enter a valid number.")


class Board:
    def __init__(self, columns=7, rows=6):
        self.__columns = columns
        self.__rows = rows
        self.__board = [[" " for _ in range(rows)] for _ in range(columns)]

    def get_width(self):
        return self.__columns

    def display(self):
        print("\nBoard:")
        for row in reversed(range(self.__rows)):
            print(" | ".join(self.__board[col][row] for col in range(self.__columns)))
        print("-" * (self.__columns * 4 - 1))
        print("   ".join(str(i) for i in range(self.__columns)))

    def add_token(self, column, symbol):
        if column < 0 or column >= self.__columns:
            return False
        for row in range(self.__rows):
            if self.__board[column][row] == " ":
                self.__board[column][row] = symbol
                return True
        return False

    def board_full(self):
        return all(self.__board[col][self.__rows - 1] != " " for col in range(self.__columns))

    def check_winner(self):
        for col in range(self.__columns):
            for row in range(self.__rows):
                symbol = self.__board[col][row]
                if symbol == " ":
                    continue
                if (
                    self.__check_direction(col, row, 1, 0, symbol) or  # Horizontal
                    self.__check_direction(col, row, 0, 1, symbol) or  # Vertical
                    self.__check_direction(col, row, 1, 1, symbol) or  # Diagonal /
                    self.__check_direction(col, row, 1, -1, symbol)    # Diagonal \
                ):
                    return symbol
        return None

    def __check_direction(self, start_col, start_row, delta_col, delta_row, symbol):
        for i in range(4):
            col = start_col + i * delta_col
            row = start_row + i * delta_row
            if (
                col < 0 or col >= self.__columns or
                row < 0 or row >= self.__rows or
                self.__board[col][row] != symbol
            ):
                return False
        return True


def play_game():
    board = Board(7, 6)
    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "O")
    players = [player1, player2]

    current_turn = 0
    while not board.board_full():
        board.display()
        current_player = players[current_turn % 2]
        move_made = current_player.make_move(board)

        if move_made:
            winner = board.check_winner()
            if winner:
                board.display()
                print(f"{current_player.get_name()} wins!")
                return

            current_turn += 1

    board.display()
    print("It's a draw!")

play_game()
