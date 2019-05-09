#Menu and menu functions

import pygame, sys, Game
from pygame.locals import *

pygame.init()

testRed = (255,0,0)
baseRed = (200,0,0)
black = (0,0,0)

#Function that defines the text used in the Menu Buttons
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#Function that controls parameters and actions for menu buttons
def button(msg, x_index, y_index, width, height, inactive_color, active_color, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x_index + width > mouse[0] > x_index and y_index + height > mouse[1] > y_index:
        pygame.draw.rect(mainSurface, active_color, (x_index, y_index, width, height))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(mainSurface, inactive_color, (x_index, y_index, width, height))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x_index + (width / 2)), (y_index + (height / 2)) )
    mainSurface.blit(textSurf, textRect)

#Function that quits the game when called
def quitgame():
    pygame.quit()
    sys.exit()


