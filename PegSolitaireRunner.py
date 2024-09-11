import logging
import datetime
from KinkaidDecorators import log_start_stop_method
from Board import Board

logging.basicConfig(level=logging.INFO)
import logging
import datetime
from KinkaidDecorators import log_start_stop_method
from Board import Board

#logging.basicConfig(level=logging.INFO)



class PegSolitaireRunner:
    def __init__(self):
        #logging.info("Initializing Peg Solitaire Game")
        self.board = Board()

    @log_start_stop_method
    def play_game(self):
        while True:  # main game loop
            self.board.draw()
            try:
                x1 = int(input("Enter the x coordinate of the peg you want to move: "))
                y1 = int(input("Enter the y coordinate of the peg you want to move: "))
                direction = input("Enter the direction of the move (e.g., 'right', 'left', 'top right', etc.): ")

                if self.board.check_if_legal(x1, y1, direction)[0]:  # checking move legality
                    self.board.move(x1, y1, direction)
                    #logging.info(f"Move from ({x1}, {y1}) in direction '{direction}' executed.")
                else:
                    #logging.info("Illegal move attempted.")
                    print("Illegal move. Try again.")
            except ValueError:
                print("Invalid input. Please enter valid numbers for coordinates.")
            except IndexError:
                print("Coordinates out of bounds. Please try again within the board limits.")

            if self.check_game_over():
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
