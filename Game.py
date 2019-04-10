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
        self.game_over = True
        pass


    # Starts a new regular (mode 1) game.
    def start_new_regular_game(self):
        self.current_level = 1
        self.gameOver = False

        # Main game loop.
        while not self.game_over:
            start_new_level(self.current_level)


    # Starts a new inverted (mode 2) game.
    def start_new_inverted_game(self):
        self.current_level = 1
        self._game_over = False

        # Main game loop.
        while not self.game_over:
            start_new_level(self.current_level)


    # Starts a new level.
    def start_new_level(self, level):
        board = Board('.' + sep + 'board.txt')          # Reset board.
        set_difficulty(level)

    # Sets difficulty variables based on level.
    def set_difficulty(self, level):
        pass
