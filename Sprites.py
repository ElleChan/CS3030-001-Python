'''
This module contains all of the classes responsible for controlling the sprites
(i.e. pacman and the ghosts)
'''

import pygame
#from pygame.locals import *

class Sprite:
    def __init__(self, imageDir, speed=10, is_CPU=True):
        self._current_x = 0                                                     # Current x pixel of left corner.
        self._current_y = 0                                                     # Current y pixel of right corner.
        self._prev_x = 0
        self._prev_y = 0
        self._imageDir = imageDir
        self._current_image = './' + self._imageDir + '/right1.png'             # The current image that the sprite should be drawn as.
        self._image_index = 0
        self._speed = speed
        self._is_CPU_controlled=is_CPU                                          # Is controlled by the CPU? By default, yes.


    # Move sprite left..
    def move_left(self):
        self._prev_x = self._current_x
        self._prev_y = self._current_y
        self._current_x -= self._speed
        self._current_image = './' + self._imageDir + '/left' + str(self._image_index) + '.png'
        self._image_index = (self._image_index + 1) % 3

    # Move sprite right
    def move_right(self):
        self._prev_x = self._current_x
        self._prev_y = self._current_y
        self._current_x += self._speed
        self._current_image = './' + self._imageDir + '/right' + str(self._image_index) + '.png'
        self._image_index = (self._image_index + 1) % 3

    # Move sprite up
    def move_up(self):
        self._prev_x = self._current_x
        self._prev_y = self._current_y
        self._current_y -= self._speed
        self._current_image = './' + self._imageDir + '/up' + str(self._image_index) + '.png'
        self._image_index = (self._image_index + 1) % 3

    # Move sprite down.
    def move_down(self):
        self._prev_x = self._current_x
        self._prev_y = self._current_y
        self._current_y += self._speed
        self._current_image = './' + self._imageDir + '/down' + str(self._image_index) + '.png'
        self._image_index = (self._image_index + 1) % 3

    def ai_choice(self):
        pass

    def draw(self, screen):
        char = pygame.image.load(self._current_image)
        pygame.draw.rect(screen, (0,0,0), (self._prev_x, self._prev_y, 40, 40))
        screen.blit(char, (self._current_x, self._current_y))

    def taken(self):
        taken = []
        for i in range(0, self._size):
            taken.append((self._current_x + i, self._current_y))
            taken.append((self._current_x, self._current_y + i))
        return taken

class Ghost(Sprite):
    def __init__(self, images, start_x, start_y, is_CPU=True):
        Sprite.__init__(images, start_x, start_y, is_CPU)
        self._states = ["ACTIVE", "SCARED", "TIMEOUT"]                          # The different states that the ghost may be in.
        self.current_state = "ACTIVE"

    # Decides which space to move to next.
    def decide_action(self):
        pass


class PacMan(Sprite):
    def __init__(self, images, is_CPU=False):
        super(PacMan, self).__init__(images, is_CPU=is_CPU)
