'''
This module contains all of the necessary methods and objects to create and simulate
the game board.
'''

import pygame
from math import sqrt

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0, 0, 128)


class Board:
    def __init__(self):
        self.text = './board.txt'
        self.image = './board.png'
        self.height = 810
        self.width = 700
        self.walls = []
        self.dots = []
        self.power_dots = [(40,100), (670,100), (40,700), (670,700)]
        self.cur_dots = []

        self.place_dots()
        self.place_walls()

    def place_dots(self):
        self.dots += [(i,40) for i in range(40,700,30) if i not in (340,370)]                      # Row 2
        self.dots += [(40,70), (160,70), (310,70), (400,70), (550,70), (670,70)]                   # Row 3
        self.dots += [(160,100), (310,100), (400,100), (550,100)]                                  # Row 4
        self.dots += [(i,130) for i in range(40,700,30)]                                           # Row 5
        self.dots += [(40,160), (160,160), (250,160), (460,160), (550,160), (670,160)]             # Row 6
        self.dots += [(40,190), (160,190), (250,190), (460,190), (550,190), (670,190)]             # Row 7
        self.dots += [(i,220) for i in range(40,700,30) if i not in (190,220,340,370,490,520)]     # Row 8
        self.dots += [(160,250), (310,250), (400,250), (550,250)]                                  # Row 9
        self.dots += [(160,280), (310,280), (400,280), (550,280)]                                  # Row 10
        self.dots += [(160,310), (550,310)] + [(i,310) for i in range(250,461,30)]                 # Row 11
        self.dots += [(160,340), (250,340), (460,340), (550,340)]                                  # Row 12
        self.dots += [(i,370) for i in range(40,580,30) if i not in range(280,431,30)]             # Row 13
        self.dots += [(160,400), (250,400), (460,400), (550,400)]
        self.dots += [(160,430), (250,430), (460,430), (550,430)]
        self.dots += [(160,460), (550,460)] + [(i,460) for i in range(250,461,30)]
        self.dots += [(160,490), (250,490), (460,490), (550,490)]
        self.dots += [(i,520) for i in range(40,700,30) if i not in (340,370)]
        self.dots += [(40,550), (160,550), (310,550), (400,550), (550,550), (670,550)]
        self.dots += [(40,580), (160,580), (310,580), (400,580), (550,580), (670,580)]
        self.dots += [(i,610) for i in range(40,700,30) if i not in (100,130,580,610)]
        self.dots += [(70,640), (160,640), (250,640), (460,640), (550,640), (640,640)]
        self.dots += [(i,670) for i in range(40,700,30) if i not in (190,220,340,370,490,520)]
        self.dots += [(310,700), (400,700)]
        self.dots += [(40,730), (310,730), (400,730), (670,730)]
        self.dots += [(i,760) for i in range(40,700,30)]

    def place_walls(self):
        self.walls += [(i,10) for i in range(10,730,30)]
        self.walls += [(10,40), (340,40), (370,40), (700,40)]
        self.walls += [(i,70) for i in range(10,730,30) if i not in (40,160,310,400,550,670)]
        self.walls += [(i,100) for i in range(10,730,30) if i not in (40,160,310,400,550,670)]
        self.walls += [(10,130), (700,130)]
        self.walls += [(i,160) for i in range(10,730,30) if i not in (40,160,250,460,550,670)]
        self.walls += [(i,190) for i in range(10,730,30) if i not in (40,160,250,460,550,670)]
        self.walls += [(10,220), (190,220), (220,220), (340,220), (370,220), (490,220), (520,220), (700,220)]
        self.walls += [(i,250) for i in range(10,730,30) if i not in (160,310,400,550)]
        self.walls += [(i,280) for i in range(10,730,30) if i not in (160,310,400,550)]
        self.walls += [(i,310) for i in range(10,730,30) if i not in (160,250,280,310,340,370,400,430,460,550)]
        self.walls += [(i,340) for i in range(10,730,30) if i not in (160,250,460,550)]
        self.walls += [(280,370), (430,370)]
        self.walls += [(i,400) for i in range(10,730,30) if i not in (160,250,310,340,370,400,460,550)]
        self.walls += [(i,430) for i in range(10,730,30) if i not in (160,250,460,550)]
        self.walls += [(i,460) for i in range(10,730,30) if i not in (160,250,280,310,340,370,400,430,460,550)]
        self.walls += [(i,490) for i in range(10,730,30) if i not in (160,250,460,550)]
        self.walls += [(10,520), (340,520), (370,520), (700,520)]
        self.walls += [(i,550) for i in range(10,730,30) if i not in (40,160,310,400,550,670)]
        self.walls += [(i,580) for i in range(10,730,30) if i not in (40,160,310,400,550,670)]
        self.walls += [(10,610), (100,610), (130,610), (580,610), (610,610)]
        self.walls += [(i,640) for i in range(10,730,30) if i not in (70,160,250,460,550,640)]
        self.walls += [(10,670), (190,670), (220,670), (340,670), (370,670), (490,670), (520,670)]
        self.walls += [(i,700) for i in range(10,730,30) if i not in (310,400,40,670)]
        self.walls += [(i,730) for i in range(10,730,30) if i not in (40,310,400,670)]
        self.walls += [(10,760), (700,760)]
        self.walls += [(i,790) for i in range(10,730,30)]


    # Draws the board.
    def draw(self, screen):

        bg = pygame.image.load(self.image)
        screen.blit(bg, (0, 0))

        for dot in self.dots:
            pygame.draw.circle(screen, WHITE, (dot[0], dot[1]), 5)
        for wall in self.walls:
            pygame.draw.circle(screen, BLUE, (wall[0], wall[1]), 5)
        for power_dot in self.power_dots:
            pygame.draw.circle(screen, WHITE, (power_dot[0], power_dot[1]), 10)



    def isWalkable(self, x, y):
        for wall in self.walls:
            circ_rect = pygame.Rect(wall[0]-10, wall[1]-10, 20, 20)
            rect = pygame.Rect(x,y,40,40)
            if rect.colliderect(circ_rect):
                return False
        return True


    def isRegularDot(self, x, y):
        for i in range(0, len(self.dots)):
            circ_rect = pygame.Rect(self.dots[i][0]-10, self.dots[i][1]-10, 20, 20)
            rect = pygame.Rect(x,y,40,40)
            if rect.colliderect(circ_rect):
                del self.dots[i]
                return True
        return False
