'''
This module contains all of the classes responsible for controlling the sprites
(i.e. pacman and the ghosts)
'''

class Sprite:
    def __init__(self, images, start_x, start_y):
        self._images = images                                                   # List/array of the images to use to render sprite.
        self._current_x = start_x
        self._current_y = start_y
        self._current_image                                                     # The current image that the sprite should be drawn as.

    # If sprite can move left, decrement x by 1. Else, don't move.
    def move_left(self):
        if self.can_move(self._current_x - 1, self._current_y):
            self._current_x -= 1

    # If sprite can move right, increment x by 1. Else, don't move.
    def move_right(self):
        if self.can_move(self._current_x + 1, self._current_y):
            self._current_x += 1

    # If sprite can move up, decrement y by 1. Else, don't move.
    def move_up(self):
        if self.can_move(self._current_x, self._current_y - 1):
            self._current_y -= 1

    # If sprite can move down, increment y by 1. Else, don't move.
    def move_down(self):
        if self.can_move(self._current_x, self._current_y + 1):
            self._current_y += 1

    # If sprite can move to (x,y) from (current_x, current_y), return true, else false.
    def can_move(self, x, y):
        pass

    # Returns the current position of the sprite as a tuple (i.e. coordinate)
    def current_position(self):
        return (self._current_x, self._current_y)

    # Draws the sprite to a surface object. Maybe move this to the game board class and just get the coords and image instead?
    def draw_sprite(self, surfaceObj):
        pass

class Ghost(Sprite):
    def __init__(self, images, start_x, start_y):
        Sprite.__init__(images, start_x, start_y)
        self._states = ["ACTIVE", "SCARED", "TIMEOUT"]                          # The different states that the ghost may be in.

    # Decides which space to move to next.
    def decide_action(self):
        pass
