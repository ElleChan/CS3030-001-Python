'''
This module contains all of the necessary methods and objects to create and simulate
the game board.
'''

import pygame
from math import sqrt

# Special node chars.
EMPTY = ' '
DOT = '.'
POWERDOT = '*'
WALLS = '-'
TRANSPORT = 'T'
INKY = 'I'
PINKY = 'P'
BLINKY = 'B'
CLYDE = 'C'
PACMAN = 'M'

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0, 0, 128)


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
        return self._character == WALLS

class Board:
    def __init__(self):
        self.text = './board.txt'
        self.image = './board.png'
        self.height = 24
        self.width = 24
        self.walls = []
        self.dots = []
        self.cur_dots = []


    # Draws the board.
    def draw(self, screen):

        bg = pygame.image.load(self.image)
        screen.blit(bg, (0, 0))

        # Top Row
        for i in range (40, 700, 30):
            if (i == 340) | (i == 370):
                pygame.draw.circle(screen, BLUE, (i, 40), 5)
                self.walls.append((i,40))
            else:
                pygame.draw.circle(screen, WHITE, (i, 40), 5)

        # 2
        for i in range (40, 700, 30):
            if (i == 40) | (i == 160) | (i == 310) | (i ==400) | (i ==520) | (i==670):
                pygame.draw.circle(screen, WHITE, (i, 70), 5)
            else:
                pygame.draw.circle(screen, BLUE, (i, 70), 5)
                self.walls.append((i,70))

        # 3
        for i in range (40, 700, 30):
            if (i == 160) | (i == 310) | (i ==400) | (i ==520):
                pygame.draw.circle(screen, WHITE, (i, 100), 5)
            elif (i == 40) | (i == 670):
                pygame.draw.circle(screen, WHITE, (i, 100), 10)
            else:
                pygame.draw.circle(screen, BLUE, (i, 100), 5)
                self.walls.append((i,100))
        # 4
        for i in range (40, 700, 30):
            pygame.draw.circle(screen, WHITE, (i, 130), 5)

        # 5
        for i in range(40, 700, 30):
            if (i == 40) | (i ==160) | (i == 250) | (i == 460) | (i ==550) |(i==670):
                pygame.draw.circle(screen, WHITE, (i, 160), 5)
            else:
                pygame.draw.circle(screen, BLUE, (i, 160), 5)
                self.walls.append((i,160))

        # 6
        for i in range(40, 700, 30):
            if (i == 40) | (i ==160) | (i == 250) | (i == 460) | (i ==550) |(i==670):
                pygame.draw.circle(screen, WHITE, (i, 190), 5)
            else:
                pygame.draw.circle(screen, BLUE, (i, 190), 5)
                self.walls.append((i,190))

        # 7
        for i in range(40,700, 30):
            if (i == 190) | (i == 220) | (i == 340) | (i == 370) | (i == 490) | ( i== 520):
                pygame.draw.circle(screen, BLUE, (i, 220), 5)
                self.walls.append((i,220))
            else:
                pygame.draw.circle(screen, WHITE, (i, 220), 5)

        # 8
        for i in range(40, 700, 30):
            if (i == 160) | (i == 310) | (i == 400) | (i == 550):
                pygame.draw.circle(screen, WHITE, (i, 250), 5)
            else:
                pygame.draw.circle(screen, BLUE, (i, 250), 5)
                self.walls.append((i,250))

        # 9
        for i in range(40, 700, 30):
            if (i == 160) | (i == 310) | (i == 400) | (i == 550):
                pygame.draw.circle(screen, WHITE, (i, 280), 5)
            else:
                pygame.draw.circle(screen, BLUE, (i, 280), 5)
                self.walls.append((i,280))

        # 10
        for i in range(40, 700, 30):
            if (i == 160) | (i==250) | (i ==280) | (i == 310) | (i == 340) | (i == 370) | (i == 400) | (i==430) | (i==460) | (i == 550):
                pygame.draw.circle(screen, WHITE, (i, 310), 5)
            else:
                pygame.draw.circle(screen, BLUE, (i, 310), 5)
                self.walls.append((i,310))

        # 11
        for i in range(40, 700, 30):
            if (i == 160) | (i == 250) | (i == 460) | (i == 550):
                pygame.draw.circle(screen, WHITE, (i, 340), 5)
            elif ((i == 340) | (i == 370)):
                continue
            else:
                pygame.draw.circle(screen, BLUE, (i, 340), 5)
                self.walls.append((i,340))

        # 12
        for i in range(160, 580, 30):
            if (i == 280) | (i == 430):
                pygame.draw.circle(screen, BLUE, (i, 370), 5)
                self.walls.append((i,370))
            elif ((i == 310) |(i == 340) | (i == 370) | (i ==400)):
                continue
            else:
                pygame.draw.circle(screen, WHITE, (i, 370), 5)

        #13
        for i in range(40, 700, 30):
            if (i ==160) | (i == 250) | (i == 460) | (i ==550):
                pygame.draw.circle(screen, WHITE, (i, 400), 5)
            else:
                pygame.draw.circle(screen, BLUE, (i, 400), 5)
                self.walls.append((i,400))


        #14
        for i in range(40, 700, 30):
            if (i == 160) | (i==250) | (i ==280) | (i == 310) | (i == 340) | (i == 370) | (i == 400) | (i==430) | (i==460) | (i == 550):
                pygame.draw.circle(screen, WHITE, (i, 430), 5)
            else:
                pygame.draw.circle(screen, BLUE, (i, 430), 5)
                self.walls.append((i,430))

        #15
        for i in range(40, 700, 30):
            if (i ==160) | (i == 250) | (i == 460) | (i ==550):
                pygame.draw.circle(screen, WHITE, (i, 460), 5)
            else:
                pygame.draw.circle(screen, BLUE, (i, 460), 5)
                self.walls.append((i,4600))

        #16
        for i in range(40, 700, 30):
            if (i ==160) | (i == 250) | (i == 460) | (i ==550):
                pygame.draw.circle(screen, WHITE, (i, 490), 5)
            else:
                pygame.draw.circle(screen, BLUE, (i, 490), 5)
                self.walls.append((i,490))

        #17
        for i in range (40, 700, 30):
            if (i == 340) | (i == 370):
                pygame.draw.circle(screen, BLUE, (i, 520), 5)
                self.walls.append((i,520))
            else:
                pygame.draw.circle(screen, WHITE, (i, 520), 5)

        # 18
        for i in range (40, 700, 30):
            if (i == 40) | (i == 160) | (i == 310) | (i ==400) | (i ==550) | (i==670):
                pygame.draw.circle(screen, WHITE, (i, 550), 5)
            else:
                pygame.draw.circle(screen, BLUE, (i, 550), 5)
                self.walls.append((i,550))

        # 19
        for i in range (40, 700, 30):
            if (i == 40) | (i == 160) | (i == 310) | (i ==400) | (i ==550) | (i==670):
                pygame.draw.circle(screen, WHITE, (i, 580), 5)
            else:
                pygame.draw.circle(screen, BLUE, (i, 580), 5)
                self.walls.append((i,580))

        #20
        for i in range (40, 700, 30):
            if (i == 100) | (i == 130) | (i ==580) | (i==610):
                pygame.draw.circle(screen, BLUE, (i, 610), 5)
                self.walls.append((i,610))
            else:
                pygame.draw.circle(screen, WHITE, (i, 610), 5)

        # 21
        for i in range(40, 700, 30):
            if (i==70) |(i ==160) | (i == 250) | (i == 460) | (i ==550) | (i==640):
                pygame.draw.circle(screen, WHITE, (i, 640), 5)
            else:
                pygame.draw.circle(screen, BLUE, (i, 640), 5)
                self.walls.append((i,640))

        # 22
        for i in range(40,700, 30):
            if (i == 190) | (i == 220) | (i == 340) | (i == 370) | (i == 490) | ( i== 520):
                pygame.draw.circle(screen, BLUE, (i, 670), 5)
                self.walls.append((i,670))
            else:
                pygame.draw.circle(screen, WHITE, (i, 670), 5)

        # 23
        for i in range (40, 700, 30):
            if (i == 310) | (i ==400):
                pygame.draw.circle(screen, WHITE, (i, 700), 5)
            elif (i == 40) | (i == 670):
                pygame.draw.circle(screen, WHITE, (i, 700), 10)
            else:
                pygame.draw.circle(screen, BLUE, (i, 700), 5)
                self.walls.append((i,700))

        # 24
        for i in range (40, 700, 30):
            if (i == 40) | (i == 310) | (i ==400) | (i==670):
                pygame.draw.circle(screen, WHITE, (i, 730), 5)
            else:
                pygame.draw.circle(screen, BLUE, (i, 730), 5)
                self.walls.append((i,730))

        # 25
        for i in range (40, 700, 30):
            pygame.draw.circle(screen, WHITE, (i, 760), 5)

        #borders
        #top
        for i in range (10, 730, 30):
            pygame.draw.circle(screen, BLUE, (i, 10), 5)
            self.walls.append((i,10))
        #bottom
        for i in range (10, 730, 30):
            pygame.draw.circle(screen, BLUE, (i, 790), 5)
            self.walls.append((i,790))
        #left
        for j in range (10, 810, 30):
            if (j== 370):
                continue
            else:
                pygame.draw.circle(screen, BLUE, (10, j), 5)
                self.walls.append((10,j))
        #right
        for j in range (10, 810, 30):
            if (j== 370):
                continue
            else:
                pygame.draw.circle(screen, BLUE, (700, j), 5)
                self.walls.append((700,j))


    def isWalkable(self, x, y):
        #if self.getCoord(x,y) in self.walls:
        for wall in self.walls:
            circ_rect = pygame.Rect(wall[0]-10, wall[1]-10, 20, 20)
            rect = pygame.Rect(x,y,40,40)
            if rect.colliderect(circ_rect):
                return False
        return True
