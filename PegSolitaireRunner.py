import logging
import datetime
from KinkaidDecorators import log_start_stop_method
from Board import Board

logging.basicConfig(level=logging.INFO)


class PegSolitaireRunner:
    def __init__(self):
        logging.info("Initializing Peg Solitaire Game")
        self.board = Board()

    @log_start_stop_method
    def play_game(self):
        ## move and check if legal input is the x and the y coordinate of the peg youre trying to move and the direction as a string you are trying to move
        while True:  # simple loop --> needs more conditions based on actual game rules
            self.board.draw()
            move = self.board.move().split()
            x1, y1, direction = int(move[0]), int(move[1]), move[2]
            if self.board.check_if_legal(x1, y1, direction):
                self.board.move(x1, y1, direction)
                logging.info(f"Move from ({x1}, {y1}) in direction '{direction}' executed.")
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
