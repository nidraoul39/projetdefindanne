from uuid import *
from uuid import uuid4


class ConnectFourGame:
    def __init__(self):
        self.id = str(uuid4())
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'

    def make_move(self, column):
        row = self.get_next_available_row(column)
        if row is not None:
            self.board[row][column] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def get_next_available_row(self, column):
        for row in range(5, -1, -1):
            if self.board[row][column] == ' ':
                return row
        return None

    def is_winner(self, player):
        # Check rows
        for row in range(6):
            for col in range(4):
                if self.board[row][col] == player and self.board[row][col+1] == player and \
                        self.board[row][col+2] == player and self.board[row][col+3] == player:
                    return True

        # Check columns
        for col in range(7):
            for row in range(3):
                if self.board[row][col] == player and self.board[row+1][col] == player and \
                        self.board[row+2][col] == player and self.board[row+3][col] == player:
                    return True

        # Check diagonals (top-left to bottom-right)
        for row in range(3):
            for col in range(4):
                if self.board[row][col] == player and self.board[row+1][col+1] == player and \
                        self.board[row+2][col+2] == player and self.board[row+3][col+3] == player:
                    return True

        # Check diagonals (bottom-left to top-right)
        for row in range(3, 6):
            for col in range(4):
                if self.board[row][col] == player and self.board[row-1][col+1] == player and \
                        self.board[row-2][col+2] == player and self.board[row-3][col+3] == player:
                    return True

        return False
