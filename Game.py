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
        pygame.init()                                                           # Initialize pygame
        screen =  pygame.display.set_mode((800, 800))                           # Create screen object.
        clock = pygame.time.Clock()                                             # Create game clock.

        # Create sprites. Since these are always in a game.
        self.max_levels
        self.game_over = True

    def draw_screen(self):
        # For each sprite, draw the current image at the current x and current y....
        # Draw current contents of game board.

    # Starts with the menu.
    def menu(self):
        done = False
        while(not done):
            # Print menu
            pass
            # Implement menu choice (game mode or exit/return to main)

    # Initialize params to make this mode 1.
    def start_new_regular_game(self):
        # TODO: create sprites, and other stuff.
        self.start_game()

    # Initialize params to make this mode 2.
    def start_new_inverted_game(self):
        # TODO: create sprites, and other stuff.
        self.start_game()

    # Start game.
    def start_game(self):
        self.current_level = 1
        self._game_over = False

        while not self.game_over:
            start_new_level(self.current_level)
            self.current_level += 1


    # Starts a new level.
    def start_new_level(self, level):
        board = Board('.' + sep + 'board.txt')                                  # Reset board.
        set_difficulty(level)                                                   # Set the difficulty settings.

        while True:                                                             # Main loop.
            for gameEvent in pygame.event.get():                                # Get list of events in order of occurence.
                if gameEvent.type == QUIT:
                    pygame.quit()                                               # Deactivate pygame and close program.
                    sys.exit()


            keys = pygame.key.get_pressed()
            # Handle player's actions.

            # Handle CPUs

            self.draw_screen()                                                  # Update the sprites/board.


    # Sets difficulty variables based on level.
    def set_difficulty(self, level):
        pass
