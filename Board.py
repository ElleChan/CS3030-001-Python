'''
This module contains all of the necessary methods and objects to create and simulate
the game board.
'''

EMPTY = ' '
DOT = '.'
POWERDOT = '*'
WALL = '-'
TRANSPORT = 'T'
INKY = 'I'
PINKY = 'P'
BLINKY = 'B'
CLYDE = 'C'
PACMAN = 'M'

# A board node. Represents a single square of the board.
class Node:
    def __init__(self, initX=0, initY=0, char=EMPTY):
        self._character = char                    # The character representing what is add that node on the board.
        self._isOccupied = False                  # If a sprite can occupy the space.
        self.x = initX                            # X coordinate
        self.y = initY                            # Y coordinate


    # Used when a sprite wants to occupy a node.
    def occupy(self, char):
        self._isOccupied = True
        self._character = char

    # Used when a sprite wants to leave a node.
    def leave(self):
        self._isOccupied = False
        self._character = EMPTY

    def isWall(self):
        return self._character == WALL

# A 2D array of nodes, similuating the board.
class Board:
    def __init__(self, imageMap):
        try:
            handle = open(imageMap)

            lines = handle.read().split('\n')
            handle.close()
        except FileNotFoundError:
            print("Could not find the file", imageMap)
            exit()

        self._height = len(lines)       # Number of lines represents the height of the board.
        self._width = len(lines[0])     # Assume that there are lines and that all lines are the same length...
        print(self._height, self._width)

        # Instantiate contents of board.
        self.nodes = []
        for i in range(self._height):
            row=[]
            for j in range(self._width):
                row.append(Node(i, j, lines[i][j]))
            self.nodes.append(row)
