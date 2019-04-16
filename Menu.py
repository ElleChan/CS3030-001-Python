#This file contains the menu. It will probably contain the main game function later

import pygame, sys
from pygame.locals import *

pygame.init()

testRed = (255,0,0)

#Initialize the game board
mainSurface = pygame.display.set_mode ((650, 600), 0, 32)
pygame.display.set_caption('Pacman')

background = pygame.image.load("background.png").convert()

intro = True

while intro:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Display the board as a background image
    mainSurface.fill((0,0,0))
    mainSurface.blit(background, (100,0))
    pygame.display.update()