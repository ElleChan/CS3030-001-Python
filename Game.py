'''
This module contains all of the methods and objects needed to control the game.
This is the main loop and master of the game. It is also responsible for refreshing
the game screen with the appropriate images.
'''
import Sprites, Board
import pygame
from os import sep

class Game:
    # Create a game master.
    def __init__(self):
        # Create sprites. Since these are always in a game.
        self.max_levels
        self.game_over = True

    # Starts with the menu.
    def menu(self):
        done = False
        while(not done):
            # Print menu

            # Implement menu choice (game mode or exit/return to main)

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
