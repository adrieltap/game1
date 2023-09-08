import pygame
import math
from Plane import Plane
from Character import Character

clock = pygame.time.Clock()
FPS = 60
# CREATE EVENTS FOR COLLISIONS
PLAYER1_HITS = pygame.USEREVENT + 1
ENEMY_HITS = pygame.USEREVENT + 2
# colors
COLORS = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "gray": (128, 128, 128),
    "orange": (255, 165, 0)
}

WIDTH = 1024
HEIGHT = 576


def loadWindow():
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flying Plane!")
    return WINDOW
    

# load bacgkround image
background = pygame.image.load("images/sky4.png")
background = pygame.transform.scale(background, (WIDTH , HEIGHT))
SCROLL = 0
TILES = 3

def loadBackGround(image):
    # load bacgkround image
    background = pygame.image.load("images/sky4.png")
    background = pygame.transform.scale(background, (WIDTH , HEIGHT))
    SCROLL = 0
    TILES = 3

# # load airplane
# def loadPlane(player1):
#     airplane = pygame.image.load(player1.imagePath)
#     airplane = pygame.transform.scale(airplane, (player1.width , player1.height))
#     PLANE = pygame.Rect(150, 238, player1.width , player1.height ) #360,300 is the res of my airplane, change these to be variables and declare them above

# This function scrolls the background from left to right until the game ends
def infScrollBack(WINDOW):
    global TILES
    global SCROLL
        
    # drawing the background
    for i in range(0, TILES):
        WINDOW.blit(background, (i * WIDTH + SCROLL, 0))  # might have to change WIDTH so we can scale different images
    
    # scroll background
    SCROLL -= 5

    # reset our scroll if image is off screen
    if abs(SCROLL) >= WIDTH:
        SCROLL = 0

# This function deals with the bullets being fired from PLANE
# This moves bullets and collisions
# TO DO: Have an enemy to shoot at
def fireBullet(bullet, planeBullets, player1):
    for bullet in planeBullets:
        bullet.x += player1.bulletVelocity
        if bullet.x + player1.bulletVelocity > player1.screenWIDTH + 15:
            planeBullets.remove(bullet)
        # if enemy.colliderect(bullet):
        #  pygame in 90 minutes 1:05:05 for an example
        # if enemy1.charRect.colliderect(bullet):
        #     pygame.event.post(pygame.event.Event(ENEMY_HIT))
        #     planeBullets.remove(bullet)




def main():
    
    run = True
    playWINDOW = loadWindow()
    player1 = Plane("Player1", "images/enemy1.png", 3, COLORS["red"], 10)
    
    planeBullets = []
    bullet = pygame.Rect(player1.charRect.x + player1.width, player1.charRect.y + player1.height // 2, 10, 5)
    
    while run:

        clock.tick(FPS)

        infScrollBack(playWINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # key down commands
            if event.type == pygame.KEYDOWN:
                # When user hits space bullet fire from the plane
                if event.key == pygame.K_SPACE:
                     bullet = pygame.Rect(player1.charRect.x + player1.charRect.width, player1.charRect.y + player1.charRect.height // 2, 10, 5)
                     planeBullets.append(bullet)
 

        player1.movement()
        fireBullet(bullet, planeBullets, player1)

        for bullet in planeBullets:
            pygame.draw.rect(playWINDOW, player1.bulletColor, bullet)

        playWINDOW.blit(player1.Image, player1.charRect)

        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()


