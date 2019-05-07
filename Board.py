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
        self.cur_dots = []


    def place_dots(self):
        self._dots += [(i,40) for i in range(40,700,30) if i not in (340,370)]                      # Row 2
        self._dots += [(40,70), (160,70), (310,70), (400,70), (550,70), (670,70)]                   # Row 3
        self._dots += [(160,100), (310,100), (400,100), (550,100)]                                  # Row 4
        self._dots += [(i,130) for i in range(40,700,30)]                                           # Row 5
        self._dots += [(40,160), (160,160), (250,160), (460,160), (550,160), (670,160)]             # Row 6
        self._dots += [(40,190), (160,190), (250,190), (460,190), (550,190), (670,190)]             # Row 7
        self._dots += [(i,220) for i in range(40,700,30) if i not in (190,220,340,370,490,520)]     # Row 8
        self._dots += [(160,250), (310,250), (400,250), (550,250)]                                  # Row 9
        self._dots += [(160,280), (310,280), (400,280), (550,280)]                                  # Row 10
        self._dots += [(160,310), (550,310)] + [(i,310) for i in range(250,461,30)]                  # Row 11
        self._dots += [(160,340), (250,340), (460,340), (550,340)]                                  # Row 12
        self._dots += [(i,370) for i in range(40,580,30) if i not in range(280,431,30)]               # Row 13



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
                self.dots.append((i,40))

        # 2
        for i in range (40, 700, 30):
            if (i == 40) | (i == 160) | (i == 310) | (i ==400) | (i ==550) | (i==670):
                pygame.draw.circle(screen, WHITE, (i, 70), 5)
                self.dots.append((i,70))
            else:
                pygame.draw.circle(screen, BLUE, (i, 70), 5)
                self.walls.append((i,70))

        # 3
        for i in range (40, 700, 30):
            if (i == 160) | (i == 310) | (i ==400) | (i ==550):
                pygame.draw.circle(screen, WHITE, (i, 100), 5)
                self.dots.append((i,100))
            elif (i == 40) | (i == 670):
                pygame.draw.circle(screen, WHITE, (i, 100), 10)
            else:
                pygame.draw.circle(screen, BLUE, (i, 100), 5)
                self.walls.append((i,100))
        # 4
        for i in range (40, 700, 30):
            pygame.draw.circle(screen, WHITE, (i, 130), 5)
            self.dots.append((i,130))

        # 5
        for i in range(40, 700, 30):
            if (i == 40) | (i ==160) | (i == 250) | (i == 460) | (i ==550) |(i==670):
                pygame.draw.circle(screen, WHITE, (i, 160), 5)
                self.dots.append((i,160))
            else:
                pygame.draw.circle(screen, BLUE, (i, 160), 5)
                self.walls.append((i,160))

        # 6
        for i in range(40, 700, 30):
            if (i == 40) | (i ==160) | (i == 250) | (i == 460) | (i ==550) |(i==670):
                pygame.draw.circle(screen, WHITE, (i, 190), 5)
                self.dots.append((i,190))
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
                self.dots.append((i,220))

        # 8
        for i in range(40, 700, 30):
            if (i == 160) | (i == 310) | (i == 400) | (i == 550):
                pygame.draw.circle(screen, WHITE, (i, 250), 5)
                self.dots.append((i,250))
            else:
                pygame.draw.circle(screen, BLUE, (i, 250), 5)
                self.walls.append((i,250))

        # 9
        for i in range(40, 700, 30):
            if (i == 160) | (i == 310) | (i == 400) | (i == 550):
                pygame.draw.circle(screen, WHITE, (i, 280), 5)
                self.dots.append((i,280))
            else:
                pygame.draw.circle(screen, BLUE, (i, 280), 5)
                self.walls.append((i,280))

        # 10
        for i in range(40, 700, 30):
            if (i == 160) | (i==250) | (i ==280) | (i == 310) | (i == 340) | (i == 370) | (i == 400) | (i==430) | (i==460) | (i == 550):
                pygame.draw.circle(screen, WHITE, (i, 310), 5)
                self.dots.append((i,310))
            else:
                pygame.draw.circle(screen, BLUE, (i, 310), 5)
                self.walls.append((i,310))

        # 11
        for i in range(40, 700, 30):
            if (i == 160) | (i == 250) | (i == 460) | (i == 550):
                pygame.draw.circle(screen, WHITE, (i, 340), 5)
                self.dots.append((i,340))
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
                self.dots.append((i,370))

        #13
        for i in range(40, 700, 30):
            if (i ==160) | (i == 250) | (i == 460) | (i ==550):
                pygame.draw.circle(screen, WHITE, (i, 400), 5)
                self.dots.append((i,400))
            else:
                pygame.draw.circle(screen, BLUE, (i, 400), 5)
                self.walls.append((i,400))


        #14
        for i in range(40, 700, 30):
            if (i == 160) | (i==250) | (i ==280) | (i == 310) | (i == 340) | (i == 370) | (i == 400) | (i==430) | (i==460) | (i == 550):
                pygame.draw.circle(screen, WHITE, (i, 430), 5)
                self.dots.append((i,430))
            else:
                pygame.draw.circle(screen, BLUE, (i, 430), 5)
                self.walls.append((i,430))

        #15
        for i in range(40, 700, 30):
            if (i ==160) | (i == 250) | (i == 460) | (i ==550):
                pygame.draw.circle(screen, WHITE, (i, 460), 5)
                self.dots.append((i,460))
            else:
                pygame.draw.circle(screen, BLUE, (i, 460), 5)
                self.walls.append((i,4600))

        #16
        for i in range(40, 700, 30):
            if (i ==160) | (i == 250) | (i == 460) | (i ==550):
                pygame.draw.circle(screen, WHITE, (i, 490), 5)
                self.dots.append((i,490))
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
                self.dots.append((i,520))

        # 18
        for i in range (40, 700, 30):
            if (i == 40) | (i == 160) | (i == 310) | (i ==400) | (i ==550) | (i==670):
                pygame.draw.circle(screen, WHITE, (i, 550), 5)
                self.dots.append((i,550))
            else:
                pygame.draw.circle(screen, BLUE, (i, 550), 5)
                self.walls.append((i,550))

        # 19
        for i in range (40, 700, 30):
            if (i == 40) | (i == 160) | (i == 310) | (i ==400) | (i ==550) | (i==670):
                pygame.draw.circle(screen, WHITE, (i, 580), 5)
                self.dots.append((i,580))
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
                self.dots.append((i,610))

        # 21
        for i in range(40, 700, 30):
            if (i==70) |(i ==160) | (i == 250) | (i == 460) | (i ==550) | (i==640):
                pygame.draw.circle(screen, WHITE, (i, 640), 5)
                self.dots.append((i,640))
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
                self.dots.append((i,670))

        # 23
        for i in range (40, 700, 30):
            if (i == 310) | (i ==400):
                pygame.draw.circle(screen, WHITE, (i, 700), 5)
                self.dots.append((i,700))
            elif (i == 40) | (i == 670):
                pygame.draw.circle(screen, WHITE, (i, 700), 10)
            else:
                pygame.draw.circle(screen, BLUE, (i, 700), 5)
                self.walls.append((i,700))

        # 24
        for i in range (40, 700, 30):
            if (i == 40) | (i == 310) | (i ==400) | (i==670):
                pygame.draw.circle(screen, WHITE, (i, 730), 5)
                self.dots.append((i,730))
            else:
                pygame.draw.circle(screen, BLUE, (i, 730), 5)
                self.walls.append((i,730))

        # 25
        for i in range (40, 700, 30):
            pygame.draw.circle(screen, WHITE, (i, 760), 5)
            self.dots.append((i,760))

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
