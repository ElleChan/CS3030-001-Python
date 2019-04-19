import pygame
pygame.init()

#set the game window
screen_width = 800
screen_height = 800
gameDisplay = pygame.display.set_mode((screen_width, screen_height))
#add a title

clock = pygame.time.Clock()
x = 50
y = 50

char_width = 60
char_height = 60
# Initial velocity
vel = 30
# set all controls to false
left = False
right = False
up = False
down = False
move_count = 0
# load in images for each movement 3 sprites for each direction
move_right = [pygame.image.load('Pac_Right_half.png'),pygame.image.load('Pac_Right_open.png'),pygame.image.load('Pac_CLOSED.png')]
move_left = [pygame.image.load('Pac_Left_half.png'),pygame.image.load('Pac_Left_open.png'),pygame.image.load('Pac_CLOSED.png')]
move_up = [pygame.image.load('Pac_up_half.png'),pygame.image.load('Pac_up_open.png'),pygame.image.load('Pac_CLOSED.png')]
move_down = [pygame.image.load('Pac_down_half.png'),pygame.image.load('Pac_down_open.png'),pygame.image.load('Pac_CLOSED.png')]

# set default character sprite
char = pygame.image.load('Pac_Right_open.png')

#define functionto redraw gameboard
def redraw_gamewindow():
    global move_count

    # 3 each movement, 1 sprite for 3 frames = 9 fps
    if move_count + 1 >= 9:
        move_count = 0

    if left:
        gameDisplay.blit(move_left[move_count//3], (x,y))
        move_count += 1
    elif right:
        gameDisplay.blit(move_right[move_count//3], (x,y))
        move_count += 1
    elif up:
        gameDisplay.blit(move_up[move_count//3], (x,y))
        move_count += 1
    elif down:
        gameDisplay.blit(move_down[move_count//3], (x,y))
        move_count += 1
    else:
        gameDisplay.blit(char, (x,y))

    pygame.display.update()

run = True
while run:
    #9fps
    clock.tick(9)
    for event in pygame.event.get():
        #get list of events
        # print(event)
        if event.type == pygame.QUIT:
             #stop the game if quit
             run = False

    keys = pygame.key.get_pressed()

    # Controls
    
    if keys[pygame.K_LEFT] and x > vel:
        left = True
        right = False
        up = False
        down = False
        x -= vel
        
    if keys[pygame.K_RIGHT] and x < screen_width - char_width - vel:
        left = False
        right = True
        up = False
        down = False
        x += vel

    if keys[pygame.K_UP] and y > vel:
        y -= vel
        left = False
        right = False
        up = True
        down = False

        
    if keys[pygame.K_DOWN] and y < screen_height - char_height - vel:
        y += vel
        left = False
        right = False
        up = False
        down = True
    redraw_gamewindow()


pygame.quit()



