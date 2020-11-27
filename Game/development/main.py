
import sys
import pygame
from pygame.locals import *

# Necessary setup before you can start using pygame functionalities:
pygame.init()


KEYS_DOWN = []

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN  = pygame.display.set_mode(SCREEN_SIZE)

CLOCK   = pygame.time.Clock()
FPS     = 30

BG_COLOUR = [0, 0, 0]
IS_RUNNING = True


playerSprite = pygame.image.load("../art/spr_Player.png")
playerRect = playerSprite.get_rect()
playerSpeed = 5

enemySprite = pygame.image.load("../art/spr_Enemy.png")
enemyRect = enemySprite.get_rect()
enemySpeed = 5


while IS_RUNNING:


    # ------------------------------------------------
    # INPUT REGISTRATION:
    # ------------------------------------------------
    KEYS_DOWN = pygame.key.get_pressed()


    # ------------------------------------------------
    # EVENT HANDLING:
    # ------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_RUNNING = False


    # ------------------------------------------------
    # UPDATE GAME LOGIC:
    # ------------------------------------------------
    if (KEYS_DOWN[K_UP]):
        playerSprite = pygame.image.load("../art/spr_Player.png");
        playerRect.y -= playerSpeed
        playerSprite = pygame.image.load("../art/spr_Player1.png");
    elif (KEYS_DOWN[K_DOWN]):
        playerSprite = pygame.image.load("../art/spr_Player1.png");
        playerRect.y += playerSpeed
        playerSprite = pygame.image.load("../art/spr_Player.png");
       

    if (KEYS_DOWN[K_LEFT]):
        playerSprite = pygame.image.load("../art/spr_Player.png");
        playerRect.x -= playerSpeed
        playerSprite = pygame.image.load("../art/spr_Player1.png");
    elif (KEYS_DOWN[K_RIGHT]):
        playerSprite = pygame.image.load("../art/spr_Player1.png");
        playerRect.x += playerSpeed
        playerSprite = pygame.image.load("../art/spr_Player.png");
    

    # ------------------------------------------------
    # DRAWING INSTRUCTIONS
    # ------------------------------------------------
    # First clear the screen with a background color.
    # If you don't, you'll draw on top of what was previously drawn. See for yourself by removing/commenting this line... :)
    SCREEN.fill(BG_COLOUR)
    
    # Then draw sprites on the current location:
    SCREEN.blit(playerSprite, playerRect)
    
    # Finally refresh the entire screen of this application window:
    pygame.display.flip()


    # Prevent the game from running way too fast by restricting the amount of update cycles made per second.
    # The program basically waits a certain amount of time before it continues.
    # This function converts the desired result, which is expressed in "frames per second", into the exact nanoseconds wait time.
    CLOCK.tick(FPS)
