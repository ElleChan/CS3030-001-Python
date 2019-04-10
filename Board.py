'''
This module contains all of the necessary methods and objects to create and simulate
the game board.
'''

EMPTY = ' '
DOT = '.'
POWERDOT = '*'
WALL = '-'
TRANSPORT = 'T'

# A board node. Represents a single square of the board.
class Node:
    def __init__(self, initX=0, initY=0, char=EMPTY):
        self._character = char                    # The character representing what is add that node on the board.
        self._isOccupied = False                  # If a sprite can occupy the space.
        self.x = initX                            # X coordinate
        self.y = initY                            # Y coordinate

    # Determines if a sprite may occupy some node.
    def isOccupiable(self):
        if self._character != WALL and not self._isOccupied:
            return True
        else:
            return False

    # Used when a sprite wants to occupy a node.
    def occupy(self, char):
        self._isOccupied = True
        self._character = char

    # Used when a sprite wants to leave a node.
    def leave(self):
        self._isOccupied = False
        self._character = EMPTY


# A 2D array of nodes, similuating the board.
class Board:
    def __init__(self, imageMap):
        try:
            handle = open(imageMap)

            lines = handle.read().split('\n')
            handle.close()

            self._height = len(lines)       # Number of lines represents the height of the board.
            self._width = len(lines[0])     # Assume that there are lines and that all lines are the same length...

            # Instantiate contents of board.
            for i in range(self._height):
                for j in range(self._width):
                    self._nodes[i][j] = Node(i, j, lines[i][j])         # (i,j) represents (x,y) of the node.

        except:
            #ERROR
            print("Could not instantiate the board")
            exit()
