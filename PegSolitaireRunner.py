import logging
import datetime
from KinkaidDecorators import log_start_stop_method
from Board import Board


import logging
import datetime
from KinkaidDecorators import log_start_stop_method
from Board import Board

#logging.basicConfig(level=logging.INFO)

from Referee import Referee
if __name__ == "__main__":
    game = Referee()
    game.play_game()
