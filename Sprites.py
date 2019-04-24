'''
This module contains all of the classes responsible for controlling the sprites
(i.e. pacman and the ghosts)
'''

class Sprite:
    def __init__(self, imageDir, start_x, start_y, char, speed=10, is_CPU=True):
        self._current_x = start_x                                               # Current x coord.
        self._current_y = start_y                                               # Current y coord.
        self._prev_x = start_x
        self._prev_y = start_y
        self._character = char                                                  # The board character.
        self._imageDir = imageDir
        self._current_image = './' + self._imageDir + '/right1.png'             # The current image that the sprite should be drawn as.
        self._image_index = 0
        self._speed = speed
        self._is_CPU_controlled=is_CPU                                          # Is controlled by the CPU? By default, yes.

    # Move sprite left..
    def move_left(self):
        self._prev_x = self._current_x
        self._prev_y = self._current_y
        self._current_x -= 1
        self._current_image = './' + self._imageDir + '/left' + str(self._image_index) + '.png'
        self._image_index = (self._image_index + 1) % 3

    # Move sprite right
    def move_right(self):
        self._prev_x = self._current_x
        self._prev_y = self._current_y
        self._current_x += 1
        self._current_image = './' + self._imageDir + '/right' + str(self._image_index) + '.png'
        self._image_index = (self._image_index + 1) % 3

    # Move sprite up
    def move_up(self):
        self._prev_x = self._current_x
        self._prev_y = self._current_y
        self._current_y -= 1
        self._current_image = './' + self._imageDir + '/up' + str(self._image_index) + '.png'
        self._image_index = (self._image_index + 1) % 3

    # Move sprite down.
    def move_down(self):
        self._prev_x = self._current_x
        self._prev_y = self._current_y
        self._current_y += 1
        self._current_image = './' + self._imageDir + '/down' + str(self._image_index) + '.png'
        self._image_index = (self._image_index + 1) % 3

    def decide_action(self):
        if self._is_CPU_controlled:
            self.ai_choice()
        else:
            self.user_choice()

    def ai_choice(self):
        pass

    def user_choice(self):
        pass

class Ghost(Sprite):
    def __init__(self, images, start_x, start_y, is_CPU=True):
        Sprite.__init__(images, start_x, start_y, is_CPU)
        self._states = ["ACTIVE", "SCARED", "TIMEOUT"]                          # The different states that the ghost may be in.
        self.current_state = "ACTIVE"

    # Decides which space to move to next.
    def decide_action(self):
        pass


class PacMan(Sprite):
    def __init__(self, images, start_x, start_y, is_CPU=False):
        super(PacMan, self).__init__(images, start_x, start_y, is_CPU)
