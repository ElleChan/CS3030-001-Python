'''
This module contains all of the classes responsible for controlling the sprites
(i.e. pacman and the ghosts)
'''

import pygame
from random import randint
#from pygame.locals import *

class Sprite:
    def __init__(self, imageDir, img_num, speed=10, is_CPU=True):
        self._current_x = 0                                                     # Current x pixel of left corner.
        self._current_y = 0                                                     # Current y pixel of right corner.
        self._prev_x = 0
        self._prev_y = 0
        self._imageDir = imageDir
        self._current_image = './' + self._imageDir + '/right0.png'             # The current image that the sprite should be drawn as.
        self._image_index = 0
        self._image_num = img_num
        self._speed = speed
        self._is_CPU_controlled=is_CPU  # Is controlled by the CPU? By default, yes.
        self.is_blue = False
        self.time_blue = int(10 * 60)

    def turn_blue(self):
        self.is_blue = True
        #while self.is_blue == True:
        self._current_image = './blue.jpg'
        self.check_blue()       

    def check_blue(self):
        self.time_ticking = self.time_blue
        self.time_ticking -= 1

        if self.time_ticking <= 0:
            self.turn_normal()

    def turn_normal(self):
        self.is_blue = False

    # Move sprite left..
    def move_left(self):
        self._prev_x = self._current_x
        self._prev_y = self._current_y
        self._current_x -= self._speed
        self._current_image = './' + self._imageDir + '/left' + str(self._image_index) + '.png'
        self._image_index = (self._image_index + 1) % self._image_num

    # Move sprite right
    def move_right(self):
        self._prev_x = self._current_x
        self._prev_y = self._current_y
        self._current_x += self._speed
        self._current_image = './' + self._imageDir + '/right' + str(self._image_index) + '.png'
        self._image_index = (self._image_index + 1) % self._image_num

    # Move sprite up
    def move_up(self):
        self._prev_x = self._current_x
        self._prev_y = self._current_y
        self._current_y -= self._speed
        self._current_image = './' + self._imageDir + '/up' + str(self._image_index) + '.png'
        self._image_index = (self._image_index + 1) % self._image_num

    # Move sprite down.
    def move_down(self):
        self._prev_x = self._current_x
        self._prev_y = self._current_y
        self._current_y += self._speed
        self._current_image = './' + self._imageDir + '/down' + str(self._image_index) + '.png'
        self._image_index = (self._image_index + 1) % self._image_num

    def ai_choice(self):
        pass

    def draw(self, screen):
        char = pygame.image.load(self._current_image)
        pygame.draw.rect(screen, (0,0,0), (self._prev_x, self._prev_y, 40, 40))
        screen.blit(char, (self._current_x, self._current_y))


class Ghost(Sprite):
    def __init__(self, images, is_CPU=True):
        super(Ghost, self).__init__(images, 2, is_CPU=is_CPU)
        self._states = ["ACTIVE", "SCARED", "TIMEOUT"]                          # The different states that the ghost may be in.
        self.current_state = "ACTIVE"
        

    def ai_choice(self):
        choice = randint(1,30)
        choice = choice % 4

        return choice



class PacMan(Sprite):
    def __init__(self, images, is_CPU=False):
        super(PacMan, self).__init__(images, 3, is_CPU=is_CPU)
