'''
This module contains all of the methods and objects needed to control the game.
This is the main loop and master of the game. It is also responsible for refreshing
the game screen with the appropriate images.
'''
import Sprites, Board
import pygame
from pygame.locals import *
from os import sep
from time import sleep
from sys import exit

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0, 0, 128)


class Game:
    # Create a game master.
    def __init__(self):
        pygame.init()                                                           # Initialize pygame
        self._height = self._width = 800
        self._screen =  pygame.display.set_mode((self._width, self._height))    # Create screen object.
        self._clock = pygame.time.Clock()                                       # Create game clock.
        self._board = Board.Board()                                             # Reset board.

        self._sprite_size = 40                                                  # Sprites should be 40x40 pixels

        #self.max_levels
        self.game_over = True


    # Starts with the menu.
    def menu(self):
        self.start_new_regular_game()
        '''
        done = False
        while(not done):
            # Print menu
            pass
            # Implement menu choice (game mode or exit/return to main)
'''


    # Initialize params to make this mode 1.
    def start_new_regular_game(self):
        # TODO: create sprites, and other stuff.
        print("Starting new regular game")
        self._pacman = Sprites.PacMan('PacMan', 20, 20, 'P')
        self._sprites = [self._pacman]
        self._player = self._pacman

        self.start_game()


    # Initialize params to make this mode 2.
    def start_new_inverted_game(self):
        # TODO: create sprites, and other stuff.
        self.start_game()


    # Start game.
    def start_game(self):

        print("Starting new game")
        self.current_level = 1
        self._game_over = False

        while not self._game_over:
            self.start_new_level(self.current_level)
            self.current_level += 1


    # Starts a new level.
    def start_new_level(self, level):
        print("Starting new level")

        self._board.draw(self._screen)
        for sprite in self._sprites:
            sprite.draw(self._screen)
        pygame.display.update()
        #set_difficulty(level)                                                  # Set the difficulty settings.


        soundObj = pygame.mixer.Sound('./Music/pacman_beginning.wav')
        soundObj.play()
        sleep(4)
        soundObj.stop()

        while True:                                                             # Main loop.
            for gameEvent in pygame.event.get():                                # Get list of events in order of occurence.
                if gameEvent.type == QUIT:
                    pygame.quit()                                               # Deactivate pygame and close program.
                    exit()


            # Handle player.
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self._board.isWalkable(self._player._current_x - self._player._speed, self._player._current_y):
                self._player.move_left()
            elif keys[pygame.K_RIGHT] and self._board.isWalkable(self._player._current_x + self._player._speed, self._player._current_y):
                self._player.move_right()
            elif keys[pygame.K_UP] and self._board.isWalkable(self._player._current_x, self._player._current_y - self._player._speed):
                self._player.move_up()
            elif keys[pygame.K_DOWN] and self._board.isWalkable(self._player._current_x, self._player._current_y + self._player._speed):
                self._player.move_down()

            # Handle opponents.

            self._clock.tick(10)

            # Draw sprites.
            for sprite in self._sprites:
                if sprite._current_x < 0:
                    sprite._current_x = self._board.width
                elif sprite._current_x > self._board.width:
                    sprite._current_x = 0
                sprite.draw(self._screen)
            pygame.display.update()                                             # Update the sprites/board.


    # Sets difficulty variables based on level.
    def set_difficulty(self, level):
        pass
        # maybe can set the speed
