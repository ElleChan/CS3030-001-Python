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
        self._height = 800
        self._width = 860
        self._screen =  pygame.display.set_mode((self._width, self._height))    # Create screen object.
        self._clock = pygame.time.Clock()                                       # Create game clock.
        self._board = Board.Board()                                             # Reset board.

        self._pacman = Sprites.PacMan('PacMan')

        self.score = 0
        self.highscore = 10000
        self.lives = 3

        #self.scoreTextFont = pygame.font.Font("freesansbold.ttf", 20)

        #self.max_levels
        self.game_over = True


    def text_objects(self, text, font):
        textSurface = font.render(text, True, WHITE)
        return textSurface, textSurface.get_rect()

    def draw_text(self, surface, msg, x_index, y_index):    
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = (x_index, y_index)
        surface.blit(textSurf, textRect)

    def getScoreSurface (self):
        '''in - (self)
        Creates surface object of pacman's score.
        out - Surface'''
        return pygame.font.SysFont (None, 22). render ("Score: " + str (self.score), True, WHITE)

    # Starts with the menu.
    def menu(self):
        self.start_new_regular_game()


    # Initialize params to make this mode 1.
    def start_new_regular_game(self):
        # TODO: create sprites, and other stuff.
        print("Starting new regular game")
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
        self.score = 0
        self._game_over = False

        while not self._game_over:
            self.start_new_level(self.current_level)
            self.current_level += 1


    # Starts a new level.
    def start_new_level(self, level):
        print("Starting new level")

        self._board.reset(self._screen)
        self._pacman._current_x = self._pacman._prev_x = 320
        self._pacman._current_y = self._pacman._prev_y = 440

        for sprite in self._sprites:
            sprite.draw(self._screen)

        self.draw_text(self._screen, "High Score", 785, 50)
        self.draw_text(self._screen, str(self.highscore), 785, 72)
        self.draw_text(self._screen, "Score", 785, 200)
        self.draw_text(self._screen, str(self.score), 785, 222)
        self.draw_text(self._screen, "Lives", 785, 350)
        self.draw_text(self._screen, str(self.lives), 785, 372)
        pygame.display.update()
        #set_difficulty(level)                                                  # Set the difficulty settings.



        soundObj = pygame.mixer.Sound('./Music/pacman_beginning.wav')
        soundObj.play()
        sleep(4)
        soundObj.stop()

        while len(self._board.cur_dots) > 0:                                    # Main loop.
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


            if self._board.isDot(self._player._current_x, self._player._current_y):
                self.score += 10
                soundObj = pygame.mixer.Sound('./Music/pacman_chomp.wav')
                soundObj.play()
                #print(self.score)

            # Handle opponents.

            self._clock.tick(10)

            # Draw sprites.
            for sprite in self._sprites:
                # Handle side transports.
                if sprite._current_x < 0:
                    sprite._current_x = self._board.width
                elif sprite._current_x > self._board.width:
                    sprite._current_x = 0

                # Draw sprites at final coords.
                sprite.draw(self._screen)
                self.draw_text(self._screen, str(self.score), 785, 222)
                #self.scoreSurface = self.scoreTextFont.render(str(self.score), True, WHITE)
                #self._screen.blit(self.scoreSurface, (785, 222))
            pygame.display.update()


    # Sets difficulty variables based on level.
    def set_difficulty(self, level):
        pass
        # maybe can set the speed
