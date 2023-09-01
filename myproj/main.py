import pygame
import math

clock = pygame.time.Clock()
FPS = 60

# load window
WIDTH, HEIGHT = 1024, 576
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flying Plane!")

# load bacgkround image
background = pygame.image.load("images/sky4.png")
background = pygame.transform.scale(background, (WIDTH , HEIGHT))
SCROLL = 0
TILES = 3

# load airplane
airplane = pygame.image.load("images/airplane.png")
PLANE_WIDTH, PLANE_HEIGHT = 90, 75
airplane = pygame.transform.scale(airplane, (90 , 75))
PLANE = pygame.Rect(150, 238, 360, 300 ) #360,300 is the res of my airplane, change these to be variables and declare them above
VELOCITY = 3

# load bullets
myBullet = pygame.image.load("images/bullet.png")
# myBullet - pygame.transform.scale(myBullet, (10, 5))
BULLET_VEL = 7

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
    if keys_pressed[pygame.K_UP] and PLANE.y - VELOCITY > 0: # If user hits up arrow
        PLANE.y -= VELOCITY # change this for when we implement OOP
    if keys_pressed[pygame.K_DOWN] and PLANE.y + VELOCITY < HEIGHT - PLANE_HEIGHT: # If user hits down arrow
        PLANE.y += VELOCITY
    if keys_pressed[pygame.K_LEFT] and PLANE.x - VELOCITY  > 0: # If user hits left arrow
        PLANE.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and PLANE.x + VELOCITY < WIDTH - PLANE_WIDTH : # If user hits right arrow
        PLANE.x += VELOCITY

# This function deals with the bullets being fired from PLANE
def fireBullet():
    planeBullets = []
    
    bullet = pygame.Rect(PLANE.x + PLANE_WIDTH, PLANE.y + PLANE_HEIGHT // 2, 10, 5)
    planeBullets.append(bullet)
    print(bullet)
    WINDOW.blit(myBullet, bullet)




def main():
    run = True

    while run:

        clock.tick(FPS)

        infScrollBack()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # key down commands
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fireBullet()


        playerMovement()

        WINDOW.blit(airplane, PLANE)
        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()


