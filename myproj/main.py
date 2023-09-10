import pygame
import math
from Plane import Plane
from Character import Character
from Enemy import Enemy
import random

pygame.font.init()

clock = pygame.time.Clock()
FPS = 60
maxScore = 0
# CREATE EVENTS FOR COLLISIONS
PLAYER1_HIT = pygame.USEREVENT + 1
ENEMY_HIT = pygame.USEREVENT + 2
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

# FONTS
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
LOSE_FONT = pygame.font.SysFont('comicsans', 40)

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
def displayLose(playWINDOW, score):
    lose_text = LOSE_FONT.render("YOU LOSE, SCORE:  " + str(score) + "  HIGH SCORE: " + str(maxScore), 1, COLORS["black"])
    playWINDOW.blit(lose_text, (WIDTH // 2 - lose_text.get_width() / 2, HEIGHT / 2 - lose_text.get_height() /2 ))
    pygame.display.update()
    pygame.time.delay(5000)
    

def displayHealth(playWINDOW, player1):
    health_text = HEALTH_FONT.render("Health: " + str(player1.health) + " Score: " + str(player1.score), 1, COLORS["black"])
    playWINDOW.blit(health_text, (0,0))

def main():
    
    run = True
    playWINDOW = loadWindow()
    player1 = Plane("Player1", "images/airplane.png", 3, COLORS["red"], 10, 150, 238)
    enemy1 = Enemy("Enemy1", "images/enemy1.png", COLORS[random.choice(list(COLORS.keys()))], 10)
    enemy2 = Enemy("Enemy2", "images/enemy2.png", COLORS[random.choice(list(COLORS.keys()))], 10)
    enemy3 = Enemy("Enemy3", "images/enemy3.png", COLORS[random.choice(list(COLORS.keys()))], 10)
    allEnemies = Enemy.instances

    global maxScore
    while run:

        clock.tick(FPS)

        infScrollBack(playWINDOW)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # key down commands 
            if event.type == pygame.KEYDOWN:
                # When user hits space bullet fire from the plane
                if event.key == pygame.K_SPACE: 
                    player1.fireBullet()
            
            if event.type == PLAYER1_HIT: 
                player1.health -= 1
            if event.type == ENEMY_HIT:
                player1.score += 1 
                maxScore = max(maxScore, player1.score)

        if player1.health <= 0:
            displayLose(playWINDOW, player1.score)
            allEnemies.clear()
            break
        
        displayHealth(playWINDOW, player1)
        # Initialize the character and its functions and draw on screen
        player1.movement()
        player1.drawBullet(playWINDOW, allEnemies, ENEMY_HIT)
        player1.drawCharacter(playWINDOW)

        for enemies in allEnemies:
            enemies.movement()
            enemies.fireBullet()
            enemies.drawBullet(playWINDOW, player1, PLAYER1_HIT)
            enemies.drawCharacter(playWINDOW)
            enemies.collision(player1, PLAYER1_HIT)

        pygame.display.update()
    
    main()


if __name__ == "__main__":
    main()


