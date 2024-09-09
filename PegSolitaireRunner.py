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
        return input("Enter your move (format 'x1 y1 x2 y2'): ") ## print without gaps --> x1, y1 direction

    def make_move(self, x1, y1, x2, y2):
        # is this right?
        self.board[x2][y2] = 'o'
        self.board[x1][y1] = '_'

    def is_move_legal(self, x1, y1, x2, y2):
        # add the logic to check if a move is legal
        return True

class PegSolitaireRunner:
    def __init__(self):
        logging.info("Initializing Peg Solitaire Game")
        self.board = Board()

    @log_start_stop_method
    def play_game(self):
        ## move and check if legal input is the x and the y coordinate of the peg youre trying to move and the direction as a string you are trying to move
        while True:  # simple loop --> needs more conditions based on actual game rules
            self.board.draw()
            move = self.board.ask_for_move().split()
            x1, y1, x2, y2 = map(int, move)
            if self.board.is_move_legal(x1, y1, x2, y2):
                self.board.make_move(x1, y1, x2, y2)
                logging.info(f"Move from ({x1}, {y1}) to ({x2}, {y2}) executed.")
            else:
                logging.info("Illegal move attempted.")
                print("Illegal move. Try again.")
            if self.check_game_over():  # define this method (determine game end condition)
                print("Game over!")
                break

    def check_game_over(self):
        # placeholder for game over logic
        return False

if __name__ == "__main__":
    game = PegSolitaireRunner()
    game.play_game()
