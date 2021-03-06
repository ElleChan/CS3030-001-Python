'''
This module contains all of the classes responsible for controlling the sprites
(i.e. pacman and the ghosts)
'''

import pygame
from random import randint

# Base class for all sprites.
class Sprite:
    def __init__(self, imageDir, img_num, speed=10, is_CPU=True):
        self._current_x = 0                                                     # Current x pixel of left corner.
        self._current_y = 0                                                     # Current y pixel of right corner.
        self._prev_x = 0
        self._prev_y = 0
        self._imageDir = imageDir
        self._current_image = './' + self._imageDir + '/right0.png'             # The current image that the sprite should be drawn as.
        self._image_index = 0                                                   # Index used to control movement.
        self._image_num = img_num                                               # How many images for movement in a single direction.
        self._speed = speed
        self._is_CPU_controlled=is_CPU  # Is controlled by the CPU? By default, yes.
        self.is_blue = False
        self.time_blue = int(10 * 60)

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

    # The AI algorithm to choose which direction to move.
    def ai_choice(self):
        pass

    # Draws the sprite with its current image to screen.
    def draw(self, screen):
        char = pygame.image.load(self._current_image)
        pygame.draw.rect(screen, (0,0,0), (self._prev_x, self._prev_y, 40, 40))
        screen.blit(char, (self._current_x, self._current_y))

# The ghost class.
class Ghost(Sprite):
    def __init__(self, images, is_CPU=True):
        super(Ghost, self).__init__(images, 2, is_CPU=is_CPU)
        self._states = ["ACTIVE", "SCARED", "TIMEOUT"]                          # The different states that the ghost may be in.
        self.current_state = "ACTIVE"


    def ai_choice(self):
        choice = randint(1,30)
        choice = choice % 4

        return choice

    # Turns the ghosts blue (scared)
    def turn_blue(self):
        self.current_state = "SCARED"
        self._current_image = './'+ self._imageDir + '/blue1.jpg'               # TODO: change the program so that blue is in own subfolder in ghost folder
                                                                                # Then update image_dir to include the blue subdir (this allows movement in blue)
    # Return the ghost to a normal state                                        # Then when going back to active state, return the image_dir to before
    def turn_normal(self):                                                      # Include timer in own thread to determine how long to stay blue.
        self.current_state = "ACTIVE"


# The PacMan class.
class PacMan(Sprite):
    def __init__(self, images, is_CPU=False):
        super(PacMan, self).__init__(images, 3, is_CPU=is_CPU)
