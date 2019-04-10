'''
This module contains all of the methods and objects needed to control the game.
This is the main loop and master of the game.
'''
import Sprites, Board
from os import sep

class Game:
    # Create a game master.
    def __init__(self):
        # Create sprites. Since these are always in a game.
        self.max_levels
        pass


    # Starts a new game.
    def start_new_game(self):
        self.current_level = 1

        while self.current_level <= self.max_levels:
            start_new_level(self._current_level)


    # Starts a new level.
    def start_new_level(self, level):
        board = Board('.' + sep + 'board.txt')          # Reset board.
