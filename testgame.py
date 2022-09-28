##import libarry
import pygame


# intialize the pygame
pygame.init()


# set screen size
# screen size set in (()) dual brackets
Screen = pygame.display.set_mode((800, 600))

# change window caption and logo
# change the window name
pygame.display.set_caption('Space Hunter')

# set veriable for icon & change icon
logo = pygame.image.load('startup.png')
pygame.display.set_icon(logo)


# player charactor
playercharac = pygame.image.load('player.png')
# adding position to player image
playerX = 370
playerY = 480

playerX_change = 0



#define player image
def player(x, y):
    Screen.blit(playercharac, (x, y))

   

# game loop
# event in pygame *event in an antynig happens in pygame screen
# this controls buttons events in pygame screen
running = True
while running:

    # set bg colors .it must RGB colors
    Screen.fill((0, 0, 51))

    #set the player image speed and movement
    #playerY -= 0.2

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Movment in player
        #keyboard events left and right buttons 
        if event.type == pygame.KEYDOWN:
            print('key presed')
            if event.key == pygame.K_LEFT:
               playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = - 0.1
    #  5 = 5 + 0.1

    playerX += playerX_change
    #Define function to show player
    player(playerX, playerY )
    pygame.display.update()
  
