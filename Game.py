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
        self._screen =  pygame.display.set_mode((self._width, self._height))          # Create screen object.
        self._clock = pygame.time.Clock()                                             # Create game clock.

        self._sprite_size = 40                                                  # Sprites should be 40x40 pixels
        self._pixel_coord_ratio = 40

        # Create sprites. Since these are always in a game.
        #self.max_levels
        self.game_over = True

    def draw_sprites(self):
        # Draw sprites.
        for sprite in self._sprites:
            char = pygame.image.load(sprite._current_image)
            pygame.draw.rect(self._screen, BLACK, (sprite._prev_x, sprite._prev_y, 40, 40))
            self._screen.blit(char, (sprite._current_x, sprite._current_y))

        pygame.display.update()

    def draw_board(self):
        bg = pygame.image.load('./board.png')
        self._screen.blit(bg, (0, 0))

        WALL = []
        DOTS = []

        # Top Row
        for i in range (40, 700, 30):
            if (i == 340) | (i == 370):
                pygame.draw.circle(self._screen, BLUE, (i, 40), 4)
                WALL.append((i,40))
            else:
                pygame.draw.circle(self._screen, WHITE, (i, 40), 4)

        # 2
        for i in range (40, 700, 30):
            if (i == 40) | (i == 160) | (i == 310) | (i ==400) | (i ==520) | (i==670):
                pygame.draw.circle(self._screen, WHITE, (i, 70), 4)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 70), 4)
                WALL.append((i,70))

        # 3
        for i in range (40, 700, 30):
            if (i == 160) | (i == 310) | (i ==400) | (i ==520):
                pygame.draw.circle(self._screen, WHITE, (i, 100), 4)
            elif (i == 40) | (i == 670):
                pygame.draw.circle(self._screen, WHITE, (i, 100), 10)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 100), 4)
                WALL.append((i,100))
        # 4
        for i in range (40, 700, 30):
            pygame.draw.circle(self._screen, WHITE, (i, 130), 4)

        # 5
        for i in range(40, 700, 30):
            if (i == 40) | (i ==160) | (i == 250) | (i == 460) | (i ==550) |(i==670):
                pygame.draw.circle(self._screen, WHITE, (i, 160), 4)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 160), 4)
                WALL.append((i,160))

        # 6
        for i in range(40, 700, 30):
            if (i == 40) | (i ==160) | (i == 250) | (i == 460) | (i ==550) |(i==670):
                pygame.draw.circle(self._screen, WHITE, (i, 190), 4)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 190), 4)
                WALL.append((i,190))

        # 7
        for i in range(40,700, 30):
            if (i == 190) | (i == 220) | (i == 340) | (i == 370) | (i == 490) | ( i== 520):
                pygame.draw.circle(self._screen, BLUE, (i, 220), 4)
                WALL.append((i,220))
            else:
                pygame.draw.circle(self._screen, WHITE, (i, 220), 4)

        # 8
        for i in range(40, 700, 30):
            if (i == 160) | (i == 310) | (i == 400) | (i == 550):
                pygame.draw.circle(self._screen, WHITE, (i, 250), 4)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 250), 4)
                WALL.append((i,250))

        # 9
        for i in range(40, 700, 30):
            if (i == 160) | (i == 310) | (i == 400) | (i == 550):
                pygame.draw.circle(self._screen, WHITE, (i, 280), 4)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 280), 4)
                WALL.append((i,280))

        # 10
        for i in range(40, 700, 30):
            if (i == 160) | (i==250) | (i ==280) | (i == 310) | (i == 340) | (i == 370) | (i == 400) | (i==430) | (i==460) | (i == 550):
                pygame.draw.circle(self._screen, WHITE, (i, 310), 4)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 310), 4)
                WALL.append((i,310))

        # 11
        for i in range(40, 700, 30):
            if (i == 160) | (i == 250) | (i == 460) | (i == 550):
                pygame.draw.circle(self._screen, WHITE, (i, 340), 4)
            elif ((i == 340) | (i == 370)):
                continue
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 340), 4)
                WALL.append((i,340))

        # 12
        for i in range(160, 580, 30):
            if (i == 280) | (i == 430):
                pygame.draw.circle(self._screen, BLUE, (i, 370), 4)
                WALL.append((i,370))
            elif ((i == 310) |(i == 340) | (i == 370) | (i ==400)):
                continue
            else:
                pygame.draw.circle(self._screen, WHITE, (i, 370), 4)

        #13
        for i in range(40, 700, 30):
            if (i ==160) | (i == 250) | (i == 460) | (i ==550):
                pygame.draw.circle(self._screen, WHITE, (i, 400), 4)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 400), 4)
                WALL.append((i,400))


        #14
        for i in range(40, 700, 30):
            if (i == 160) | (i==250) | (i ==280) | (i == 310) | (i == 340) | (i == 370) | (i == 400) | (i==430) | (i==460) | (i == 550):
                pygame.draw.circle(self._screen, WHITE, (i, 430), 4)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 430), 4)
                WALL.append((i,430))

        #15
        for i in range(40, 700, 30):
            if (i ==160) | (i == 250) | (i == 460) | (i ==550):
                pygame.draw.circle(self._screen, WHITE, (i, 460), 4)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 460), 4)
                WALL.append((i,4600))

        #16
        for i in range(40, 700, 30):
            if (i ==160) | (i == 250) | (i == 460) | (i ==550):
                pygame.draw.circle(self._screen, WHITE, (i, 490), 4)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 490), 4)
                WALL.append((i,490))

        #17
        for i in range (40, 700, 30):
            if (i == 340) | (i == 370):
                pygame.draw.circle(self._screen, BLUE, (i, 520), 4)
                WALL.append((i,520))
            else:
                pygame.draw.circle(self._screen, WHITE, (i, 520), 4)

        # 18
        for i in range (40, 700, 30):
            if (i == 40) | (i == 160) | (i == 310) | (i ==400) | (i ==550) | (i==670):
                pygame.draw.circle(self._screen, WHITE, (i, 550), 4)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 550), 4)
                WALL.append((i,550))
        
        # 19
        for i in range (40, 700, 30):
            if (i == 40) | (i == 160) | (i == 310) | (i ==400) | (i ==550) | (i==670):
                pygame.draw.circle(self._screen, WHITE, (i, 580), 4)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 580), 4)
                WALL.append((i,580))

        #20
        for i in range (40, 700, 30):
            if (i == 100) | (i == 130) | (i ==580) | (i==610):
                pygame.draw.circle(self._screen, BLUE, (i, 610), 4)
                WALL.append((i,610))
            else:
                pygame.draw.circle(self._screen, WHITE, (i, 610), 4)

        # 21
        for i in range(40, 700, 30):
            if (i==70) |(i ==160) | (i == 250) | (i == 460) | (i ==550) | (i==640):
                pygame.draw.circle(self._screen, WHITE, (i, 640), 4)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 640), 4)
                WALL.append((i,640))

        # 22
        for i in range(40,700, 30):
            if (i == 190) | (i == 220) | (i == 340) | (i == 370) | (i == 490) | ( i== 520):
                pygame.draw.circle(self._screen, BLUE, (i, 670), 4)
                WALL.append((i,670))
            else:
                pygame.draw.circle(self._screen, WHITE, (i, 670), 4)
        
        # 23
        for i in range (40, 700, 30):
            if (i == 310) | (i ==400):
                pygame.draw.circle(self._screen, WHITE, (i, 700), 4)
            elif (i == 40) | (i == 670):
                pygame.draw.circle(self._screen, WHITE, (i, 700), 10)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 700), 4)
                WALL.append((i,700))
        
        # 24
        for i in range (40, 700, 30):
            if (i == 40) | (i == 310) | (i ==400) | (i==670):
                pygame.draw.circle(self._screen, WHITE, (i, 730), 4)
            else:
                pygame.draw.circle(self._screen, BLUE, (i, 730), 4)
                WALL.append((i,730))

        # 25
        for i in range (40, 700, 30):
            pygame.draw.circle(self._screen, WHITE, (i, 760), 4)
        
        #borders
        #top
        for i in range (10, 730, 30):
            pygame.draw.circle(self._screen, BLUE, (i, 10), 4)
            WALL.append((i,10))
        #bottom
        for i in range (10, 730, 30):
            pygame.draw.circle(self._screen, BLUE, (i, 790), 4)
            WALL.append((i,790))
        #left
        for j in range (10, 810, 30):
            if (j== 370):
                continue
            else:
                pygame.draw.circle(self._screen, BLUE, (10, j), 4)
                WALL.append((10,j))
        #right
        for j in range (10, 810, 30):
            if (j== 370):
                continue
            else:
                pygame.draw.circle(self._screen, BLUE, (700, j), 4)
                WALL.append((700,j))





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

    def move_player(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self._player.move_left()

        elif keys[pygame.K_RIGHT] and self._player._current_x < self._width - self._player._speed:
            self._player.move_right()

        elif keys[pygame.K_UP] and self._player._current_y > self._player._speed:
            self._player.move_up()

        elif keys[pygame.K_DOWN] and self._player._current_y < self._height - self._player._speed:
            self._player.move_down()

        print('Previous:', self._player._prev_x, self._player._prev_y, "Current:", self._player._current_x, self._player._current_y)

    # Initialize params to make this mode 1.
    def start_new_regular_game(self):
        # TODO: create sprites, and other stuff.
        print("Starting new regular game")
        self._pacman = Sprites.PacMan('PacMan', 350, 430, 'P')
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

        self._board = Board.Board('./board.txt')                               # Reset board.
        #set_difficulty(level)                                                  # Set the difficulty settings.

        self.draw_board()
        self.draw_sprites()

        soundObj = pygame.mixer.Sound('./Music/pacman_beginning.wav')
        soundObj.play()
        sleep(4)
        soundObj.stop()

        while True:                                                             # Main loop.
            for gameEvent in pygame.event.get():                                # Get list of events in order of occurence.
                if gameEvent.type == QUIT:
                    pygame.quit()                                               # Deactivate pygame and close program.
                    exit()


            # Handle player's actions.
            self.move_player()


            # Handle CPUs

            self._clock.tick(10)
            self.draw_sprites()                                                  # Update the sprites/board.


    # Sets difficulty variables based on level.
    def set_difficulty(self, level):
        pass
        # maybe can set the speed
