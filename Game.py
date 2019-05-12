'''
This module contains all of the methods and objects needed to control the game.
This is the main loop and master of the game. It is also responsible for refreshing
the game screen with the appropriate images.
'''
import Sprites, Board, Game_Menu
import pygame, shelve
from pygame.locals import *
from os import sep
from time import sleep
from sys import exit

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0, 0, 128)
ACTIVE_RED = (255,255,204)
INACTIVE_RED = (255,255,0)

class Game:
    # Create a game master.
    def __init__(self):
        pygame.init()                                                           # Initialize pygame
        self.height = 800
        self.width = 860
        self.screen =  pygame.display.set_mode((self.width, self.height))    # Create screen object.
        self.clock = pygame.time.Clock()                                       # Create game clock.
        self.board = Board.Board()                                             # Reset board.

        self.pacman = Sprites.PacMan('PacMan')
        self.blinky = Sprites.Ghost('Blinky')
        self.inky = Sprites.Ghost('Inky')
        self.pinky = Sprites.Ghost('Pinky')
        self.clyde = Sprites.Ghost('Clyde')
        self.sprites = [self.pacman, self.blinky, self.inky, self.pinky, self.clyde]

        self.menu_image = './board.png'
        self.title_image = './title.png'

        #self.initial_high_score = 500
        #d = shelve.open('highscore.txt')
        #d['score'] = self.initial_high_score
        #d.close()

        #self.max_levels
        self.game_over = True

    #Function for formatting text on the main surface
    def text_objects(self, text, font):
        textSurface = font.render(text, True, WHITE)
        return textSurface, textSurface.get_rect()

    #Function for displaying text on the main surface
    def draw_text(self, surface, msg, x_index, y_index):
        pygame.draw.rect(self.screen, (0,0,0), (x_index-(self.width-x_index)/2, y_index-11, self.width - x_index, 22))
        smallText = pygame.font.Font("freesansbold.ttf", 22)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = (x_index, y_index)
        surface.blit(textSurf, textRect)


    # Starts with the menu.
    def menu(self):
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            #Display the board as a background image
            self.screen.fill((0,0,0))
            bg = pygame.image.load(self.menu_image)
            title = pygame.image.load(self.title_image)
            self.screen.blit(bg, (0,0))
            self.screen.blit(title, (100,300))

            #New Game Pacman - Clicking on the button starts a new regular game
            Game_Menu.button("Play as Pac Man!", 715, 50, 140, 50, INACTIVE_RED, ACTIVE_RED, self.start_new_regular_game)

            #New Game Ghost - Clicking on the button starts a new ghost game
            Game_Menu.button("Play as Ghost!", 715, 150, 140, 50, INACTIVE_RED, ACTIVE_RED, self.start_new_inverted_game)

            #Quit - Clicking on the button quits the game
            Game_Menu.button("Quit", 715, 250, 140, 50, INACTIVE_RED, ACTIVE_RED, Game_Menu.quitgame)

            pygame.display.update()


    # Initialize params to make this mode 1.
    def start_new_regular_game(self):
        # TODO: create sprites, and other stuff.
        print("Starting new regular game")
        self.player = self.pacman
        self.enemies = [self.inky, self.pinky, self.blinky, self.clyde]

        self.start_game()


    # Initialize params to make this mode 2.
    def start_new_inverted_game(self):
        # TODO: create sprites, and other stuff.
        self.start_game()


    # Start game.
    def start_game(self):

        print("Starting new game")
        self.current_level = 1
        self.score = 0
        self.game_over = False
        self.get_high_score = shelve.open('highscore.txt')
        self.highscore = self.get_high_score['score']
        self.lives = 3

        while not self.game_over:
            self.start_new_level(self.current_level)
            self.current_level += 1


    # Starts a new level.
    def start_new_level(self, level):
        print("Starting new level")

        # Set up board and sprites.
        self.board.reset(self.screen)
        self.pacman._current_x, self.pacman._current_y = self.pacman._prev_x, self.pacman._prev_y = 330,440
        self.blinky._current_x, self.blinky._current_y = self.blinky._prev_x, self.blinky._prev_y = 340,360
        self.inky._current_x, self.inky._current_y = self.inky._prev_x, self.inky._prev_y = 300,360
        self.pinky._current_x, self.pinky._current_y = self.pinky._prev_x, self.pinky._prev_y = 380,360
        self.clyde._current_x, self.clyde._current_y = self.clyde._prev_x, self.clyde._prev_y = 340,320

        for sprite in self.sprites:
            sprite.draw(self.screen)

        self.draw_text(self.screen, "High Score", 785, 50)
        self.draw_text(self.screen, str(self.highscore), 785, 72)
        self.draw_text(self.screen, "Score", 785, 200)
        self.draw_text(self.screen, str(self.score), 785, 222)
        self.draw_text(self.screen, "Lives", 785, 350)
        self.draw_text(self.screen, str(self.lives), 785, 372)
        pygame.display.update()


        #set_difficulty(level)                                                  # Set the difficulty settings.

        # Play intro sound.
        soundObj = pygame.mixer.Sound('./Music/pacman_beginning.wav')
        soundObj.play()
        sleep(4)
        soundObj.stop()

        # Background music.
        pygame.mixer.music.load('./Music/pacman_chomp.wav')
        pygame.mixer.music.play(-1)


        while len(self.board.cur_dots) > 0:                                     # Main loop.
            for gameEvent in pygame.event.get():                                # Get list of events in order of occurence.
                if gameEvent.type == QUIT:
                    pygame.quit()                                               # Deactivate pygame and close program.
                    exit()

            if self.lives <= 0:
                self.game_over = True
                pygame.mixer.music.stop()
                
                if self.score > self.highscore:
                    self.get_high_score = shelve.open('highscore.txt')
                    self.get_high_score['score'] = self.score
                    self.get_high_score.close()
                    return
                else:
                    return


            # Handle player.
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.board.isWalkable(self.player._current_x - self.player._speed, self.player._current_y):
                self.player.move_left()
            elif keys[pygame.K_RIGHT] and self.board.isWalkable(self.player._current_x + self.player._speed, self.player._current_y):
                self.player.move_right()
            elif keys[pygame.K_UP] and self.board.isWalkable(self.player._current_x, self.player._current_y - self.player._speed):
                self.player.move_up()
            elif keys[pygame.K_DOWN] and self.board.isWalkable(self.player._current_x, self.player._current_y + self.player._speed):
                self.player.move_down()

            # Handle opponents.
            pacRect =  pygame.Rect(self.pacman._current_x, self.pacman._current_y,40,40)
            for enemy in self.enemies:
                choice = enemy.ai_choice()
                if choice == 0 and self.board.isWalkable(enemy._current_x - enemy._speed, enemy._current_y):
                    enemy.move_left()
                elif choice == 1 and self.board.isWalkable(enemy._current_x + enemy._speed, enemy._current_y):
                    enemy.move_right()
                elif choice == 2 and self.board.isWalkable(enemy._current_x, enemy._current_y - enemy._speed):
                    enemy.move_up()
                elif choice == 3 and self.board.isWalkable(enemy._current_x, enemy._current_y + enemy._speed):
                    enemy.move_down()

                # Collided with pacman?
                enemyRect = pygame.Rect(enemy._current_x, enemy._current_y,40,40)
                if enemyRect.colliderect(pacRect):
                    self.lives -= 1
                    self.pacman._current_x, self.pacman._current_y = 330,440
                    self.blinky._current_x, self.blinky._current_y = 340,360
                    self.inky._current_x, self.inky._current_y = 300,360
                    self.pinky._current_x, self.pinky._current_y = 380,360
                    self.clyde._current_x, self.clyde._current_y = 340,320
                    self.draw_text(self.screen, str(self.lives), 785, 372)

                    pygame.mixer.music.pause()
                    soundObj = pygame.mixer.Sound('./Music/pacman_death.wav')
                    soundObj.play()
                    sleep(2)
                    soundObj.stop()
                    pygame.mixer.music.unpause()
                    #pygame.display.update()
                    break


            # Handle dot collisions
            if self.board.collideDot(self.player._current_x, self.player._current_y):
                if self.board.isPowerDot(self.player._current_x, self.player._current_y):
                    self.score += 50
                else:
                    self.score += 10

            # Handle side transports and draw sprites..
            for sprite in self.sprites:
                if sprite._current_x < 0:
                    sprite._current_x = self.board.width
                elif sprite._current_x > self.board.width:
                    sprite._current_x = 0

                sprite.draw(self.screen)

            self.draw_text(self.screen, str(self.score), 785, 222)
            self.clock.tick(10)
            pygame.display.update()


    # Sets difficulty variables based on level.
    def set_difficulty(self, level):
        pass
        # maybe can set the speed of ghosts
