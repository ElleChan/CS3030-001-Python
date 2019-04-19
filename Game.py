'''
This module contains all of the methods and objects needed to control the game.
This is the main loop and master of the game. It is also responsible for refreshing
the game screen with the appropriate images.
'''
import Sprites, Board
import pygame
from pygame.locals import *
from os import sep

class Game:
    # Create a game master.
    def __init__(self):
        pygame.init()                                                           # Initialize pygame
        self._height = self._width = 800
        self._screen =  pygame.display.set_mode((self._width, self._height))          # Create screen object.
        self._clock = pygame.time.Clock()                                             # Create game clock.
        self._vel = 30

        self._pacman_images = ("./PacMan/Pac_Right_open.png")


        # Create sprites. Since these are always in a game.
        #self.max_levels
        self.game_over = True

    def draw_screen(self):
        # For each sprite, draw the current image at the current x and current y....
        # Draw current contents of game board.
        for sprite in self._sprites:
            self._screen = pygame.display.set_mode((self._width, self._height))
            char = pygame.image.load(sprite._current_image)
            self._screen.blit(char, (sprite._current_x, sprite._current_y))

        pygame.display.update()

    def draw_board(self):
        pass

    def draw_initial(self):
        #board = pygame.image.load('./board.png')
        #self._screen = pygame.display.set_mode((self._width, self._height))
        self.draw_screen()


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
        self._pacman = Sprites.PacMan('PacMan', 400, 400, 'P')
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

        self.draw_initial()
        #self._board = Board.Board('./board.txt')                                # Reset board.
        #set_difficulty(level)                                                  # Set the difficulty settings.

        while True:                                                             # Main loop.
            for gameEvent in pygame.event.get():                                # Get list of events in order of occurence.
                if gameEvent.type == QUIT:
                    pygame.quit()                                               # Deactivate pygame and close program.
                    sys.exit()


            # Handle player's actions.
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self._player._current_x > self._vel:
                #if self._board.nodes[self._player._current_x - 1][self._player._current_y].isOccupiable():
                self._player.move_left()
                self._player._current_x -= self._vel
                #self._board.nodes[self._player_current_x][self._player._current_y].occupy(self._player._character)

            elif keys[pygame.K_RIGHT] and self._player._current_x < self._width - self._vel:
                self._player.move_right()
                self._player._current_x += self._vel

            elif keys[pygame.K_UP] and self._player._current_y > self._vel:
                self._player.move_up()
                self._player._current_y -= self._vel

            elif keys[pygame.K_DOWN] and self._player._current_y < self._height - self._vel:
                self._player.move_down()
                self._player._current_y += self._vel


            # Handle CPUs

            self.draw_screen()                                                  # Update the sprites/board.


    # Sets difficulty variables based on level.
    def set_difficulty(self, level):
        pass
