import logging
import datetime
from KinkaidDecorators import log_start_stop_method

logging.basicConfig(level=logging.INFO)

class Board:
    def __init__(self):
        self.board = [['_'] * 5 for _ in range(5)]  # example board setup (adjust size and initialization as necessary)
        self.setup_board()

    def setup_board(self):
        # initialize the board with pegs (except one empty hole for starting the game)
        for i in range(5):
            for j in range(5):
                self.board[i][j] = 'o'
        self.board[2][2] = '_'  # empty middle spot for example

    def draw(self):
        for row in self.board:
            print(' '.join(row))

    def ask_for_move(self):
        return input("Enter your move (format 'x1 y1 direction'): ")  ## change to include direction

    def make_move(self, x1, y1, direction):
        # is this right?
        directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        dx, dy = directions[direction]
        x2, y2 = x1 + 2 * dx, y1 + 2 * dy
        self.board[x2][y2] = 'o'
        self.board[x1][y1] = '_'
        self.board[x1 + dx][y1 + dy] = '_'  # remove the jumped peg

    def is_move_legal(self, x1, y1, direction):
        # add the logic to check if a move is legal
        directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        dx, dy = directions[direction]
        x2, y2 = x1 + 2 * dx, y1 + 2 * dy
        if 0 <= x2 < 5 and 0 <= y2 < 5 and self.board[x1 + dx][y1 + dy] == 'o' and self.board[x2][y2] == '_':
            return True
        return False

    def count_pegs(self):
        # Count how many pegs are left on the board
        return sum(row.count('o') for row in self.board)

    def has_any_legal_moves(self):
        # Check if there are any legal moves left on the board
        directions = ['up', 'down', 'left', 'right']
        for x1 in range(5):
            for y1 in range(5):
                if self.board[x1][y1] == 'o':  # find pegs
                    for direction in directions:
                        if self.is_move_legal(x1, y1, direction):
                            return True
        return False

class PegSolitaireRunner:
    def __init__(self):
        logging.info("Initializing Peg Solitaire Game")
        self.board = Board()

    @log_start_stop_method
    def play_game(self):
        ## move and check if legal input is the x and the y coordinate of the peg you're trying to move and the direction as a string you are trying to move
        while True:  # simple loop --> needs more conditions based on actual game rules
            self.board.draw()
            move = self.board.ask_for_move().split()
            x1, y1, direction = int(move[0]), int(move[1]), move[2]
            if self.board.is_move_legal(x1, y1, direction):
                self.board.make_move(x1, y1, direction)
                logging.info(f"Move from ({x1}, {y1}) in direction '{direction}' executed.")
            else:
                logging.info("Illegal move attempted.")
                print("Illegal move. Try again.")
            if self.check_game_over():  # define this method (determine game end condition)
                print("Game over!")
                break

    def check_game_over(self):
        # Game over if only one peg is left or no legal moves remain
        peg_count = self.board.count_pegs()
        if peg_count == 1:
            print("Congratulations, you won!")
            return True
        if not self.board.has_any_legal_moves():
            print("No legal moves left. You lost.")
            return True
        return False

if __name__ == "__main__":
    game = PegSolitaireRunner()
    game.play_game()
