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
        print()

    def ask_for_move(self):
        return input("Enter your move (format 'x1 y1 x2 y2'): ")

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



## howe's stuff
# import logging, datetime
# from KinkaidDecorators import log_start_stop_method
#
# logging.basicConfig(level=logging.INFO)  # simple version to the output console
# # logging.basicConfig(level=logging.DEBUG, filename=f"log {datetime.datetime.now():%m-%d@%H:%M:%S}.txt",
# #                     format="%(asctime)s %(levelname)s %(message)s",
# #                     datefmt="%H:%M:%S %p --- ")  # more robust, sent to a file cNode = Tuple[int, T]
#
# class PegSolitaireRunner:
#     def __init__(self):
#         logging.info("Initializing.")
#         # add any code you want to set up variables for the game.
#
#     @log_start_stop_method
#     def play_game(self):  # note: this is complaining (grey underline) that it could be static because it doesn't use
#         # any variables or methods from "self." Once you do, it will stop pestering you about it.
#         pass
#
# if __name__ == "__main__":
#     game = PegSolitaireRunner()
#     game.play_game()
