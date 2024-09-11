import logging
import datetime
from KinkaidDecorators import log_start_stop_method
from Board import Board

logging.basicConfig(level=logging.INFO)
import logging
import datetime
from KinkaidDecorators import log_start_stop_method
from Board import Board

logging.basicConfig(level=logging.INFO)


def count_pegs(self):
    # Count how many pegs are left on the board
    return sum(1 for row in self.board for peg in row if peg[1])

def has_any_legal_moves(self):
    # Check if there are any legal moves left on the board
    directions = ['right', 'left', 'top right', 'top left', 'bottom right', 'bottom left']
    for y1, row in enumerate(self.board):
        for x1, peg in enumerate(row):
            if peg[1]:  # Checking if the peg is present
                for direction in directions:
                    if self.check_if_legal(x1, y1, direction)[0]:  # Assuming check_if_legal returns a tuple where the first item is a boolean indicating legality
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


def count_pegs(self):
    # count how many pegs are left on the board
    return sum(1 for row in self.board for peg in row if peg[1])

def has_any_legal_moves(self):
    # check if there are any legal moves left on the board
    directions = ['right', 'left', 'top right', 'top left', 'bottom right', 'bottom left']
    for y1, row in enumerate(self.board):
        for x1, peg in enumerate(row):
            if peg[1]:  # checking if the peg is present
                for direction in directions:
                    if self.check_if_legal(x1, y1, direction)[0]:  # Assuming check_if_legal returns a tuple where the first item is a boolean indicating legality
                        return True
    return False


class PegSolitaireRunner:
    def __init__(self):
        logging.info("Initializing Peg Solitaire Game")
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
                    logging.info(f"Move from ({x1}, {y1}) in direction '{direction}' executed.")
                else:
                    logging.info("Illegal move attempted.")
                    print("Illegal move. Try again.")
            except ValueError:
                print("Invalid input. Please enter valid numbers for coordinates.")
            except IndexError:
                print("Coordinates out of bounds. Please try again within the board limits.")

            if self.check_game_over():
                print("Game over!")
                break

    def check_game_over(self):
        # game over if only one peg is left or no legal moves remain
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
