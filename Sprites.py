'''
This module contains all of the classes responsible for controlling the sprites
(i.e. pacman and the ghosts)
'''

class Sprite:
    def __init__(self, images, start_x, start_y):
        self._images = images                                                   # List/array of the images to use to render sprite.
        self._current_x = start_x
        self._current_y = start_y

    # If sprite can move left, decrement x by 1. Else, don't move.
    def move_left(self):
        pass

    # If sprite can move right, increment x by 1. Else, don't move.
    def move_right(self):
        pass

    # If sprite can move up, decrement y by 1. Else, don't move.
    def move_up(self):
        pass

    # If sprite can move down, increment y by 1. Else, don't move.
    def move_down(self):
        pass

    # Draw sprite to screen surface object.
    def draw_sprite(self, image):
        pass


class Ghost(Sprite):
    def __init__(self, images, start_x, start_y):
        Sprite.__init__(images, start_x, start_y)
        self._states = ["ACTIVE", "SCARED", "TIMEOUT"]                          # The different states that the ghost may be in.

    # Decides which space to move to next.
    def decide_action(self):
        pass
