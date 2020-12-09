
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

class link:

     lives = 3
     def __init__(self, lives):
         self.lives = lives
         
print("You have", link.lives, "lives")

player1 = link
player1.lives = 190

print("player1.lives", link.lives)


class Character :

    speed = 10
    points = 0
    sprite = None
    iq = 100

    def __init__(self) : 
        print("De constructor van de character")

    def Walk(self):
        print("Character loopt nu met snelheid ", self.speed)


class Mario(Character):
    
    lives = 4
    item = None
    

    def __init__(self):
        # We vullen aan op de constructor van de Character
        super().__init__()

        #de snelheid van mario is standaard hoger
        self.speed = 30
        self.iq = 125

    def Jump(self) :
        print("Mario Springt!")

    def Walk(self):
        print("Mario loop heel anders, maar wel met de snelheid ", self.speed)

    def life(self):
        print("Hij heeft in levens totaal ", self.lives)


class Goomba(Character):

    chase = 1
    item = None
    iq = 90
    

    def __init__(self):
        super().__init__()

        self.speed = 5
        self.points = 2

    def Walk(self) :
        print("Goomba's speed is", self.speed)
    def point(self):
        print("The points of a goomba are ", self.points)
    def iq(self):
        print("The iq of a goomba are ", self.iq)

#instanties maken
characterA = Character()
MarioX = Mario()
GoombaX = Goomba()


characterA.Walk()
MarioX.Walk()
GoombaX.Walk()
MarioX.life()
GoombaX.point()
GoombaX.iq()

print(MarioX.speed)
print(characterA.speed)
print(MarioX.lives)
print(GoombaX.speed)
print(GoombaX.point)
print(GoombaX.iq)

# Het resultaat in de console geeft een geheugenadres weer.
# Dit geheigenadres verwijst naar de locatie van het volledige object:
print(MarioX)

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
