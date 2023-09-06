import pygame
import math
from Plane import Plane

clock = pygame.time.Clock()
FPS = 60

# load window
WIDTH, HEIGHT = 1024, 576
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flying Plane!")

# colors
RED = (255, 0, 0)
# default scaling for player1's plane
PLANE_WIDTH, PLANE_HEIGHT = 90, 75

# load bacgkround image
background = pygame.image.load("images/sky4.png")
background = pygame.transform.scale(background, (WIDTH , HEIGHT))
SCROLL = 0
TILES = 3

player1 = Plane("Adriel's Plane", "images/airplane.png", PLANE_WIDTH, PLANE_HEIGHT, 3, RED, 10)

# load airplane
airplane = pygame.image.load(player1.imageStr)
airplane = pygame.transform.scale(airplane, (PLANE_WIDTH , PLANE_HEIGHT))
PLANE = pygame.Rect(150, 238, PLANE_WIDTH, PLANE_HEIGHT ) #360,300 is the res of my airplane, change these to be variables and declare them above


# This function scrolls the background from left to right until the game ends
def infScrollBack():
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

# This function controls the velocity of the player when moving their Flyer/Plane
# it also keeps the plane within bounds of the screen 

def playerMovement():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and PLANE.y - player1.velocity > 0: # If user hits up arrow
        PLANE.y -= player1.velocity # change this for when we implement OOP
    if keys_pressed[pygame.K_DOWN] and PLANE.y + player1.velocity < HEIGHT - PLANE_HEIGHT: # If user hits down arrow
        PLANE.y += player1.velocity
    if keys_pressed[pygame.K_LEFT] and PLANE.x - player1.velocity  > 0: # If user hits left arrow
        PLANE.x -= player1.velocity
    if keys_pressed[pygame.K_RIGHT] and PLANE.x + player1.velocity < WIDTH - PLANE_WIDTH : # If user hits right arrow
        PLANE.x += player1.velocity

# This function deals with the bullets being fired from PLANE
# This moves bullets and collisions
# TO DO: Have an enemy to shoot at
def fireBullet(bullet, planeBullets):
    for bullet in planeBullets:
        bullet.x += player1.bulletVelocity
        # if enemy.colliderect(bullet):
        #  pygame in 90 minutes 1:05:05 for an example



def main():
    run = True
    planeBullets = []
    bullet = pygame.Rect(PLANE.x + PLANE_WIDTH, PLANE.y + PLANE_HEIGHT // 2, 10, 5)
    print(player1.bulletVelocity)
    while run:

        clock.tick(FPS)

        infScrollBack()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # key down commands
            if event.type == pygame.KEYDOWN:
                # When user hits space bullet fire from the plane
                if event.key == pygame.K_SPACE:
                     bullet = pygame.Rect(PLANE.x + PLANE_WIDTH, PLANE.y + PLANE_HEIGHT // 2, 10, 5)
                     planeBullets.append(bullet)


        playerMovement()
        fireBullet(bullet, planeBullets)

        for bullet in planeBullets:
            pygame.draw.rect(WINDOW, player1.bulletColor, bullet)

        WINDOW.blit(airplane, PLANE)

        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()


