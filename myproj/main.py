import pygame
import math

clock = pygame.time.Clock()
FPS = 60

# load window
WIDTH, HEIGHT = 1024, 576
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flying Plane")

# load bacgkround image
background = pygame.image.load("images/sky4.png")
background = pygame.transform.scale(background, (WIDTH , HEIGHT))
# load airplane
airplane = pygame.image.load("images/airplane.png")
PLANE_WIDTH, PLANE_HEIGHT = 90, 75
airplane = pygame.transform.scale(airplane, (90 , 75))

def main():
    plane = pygame.Rect(238, 238, 360, 300 ) #360,300 is the res of my airplane, change these to be variables and declare them above
    tiles = 3 # 2 for now, however when I have multiple images I might have to scale them correctly
    scroll = 0 # scrolling for background
    VELOCITY = 3 # velocity of plane moving up and down

    run = True
    while run:

        

        clock.tick(FPS)

        # drawing the background
        for i in range(0, tiles):
            WINDOW.blit(background, (i * WIDTH + scroll, 0))  # might have to change WIDTH so we can scale different images
        # scroll background
        scroll -= 5
        
        # reset our scroll if image is off screen

        if abs(scroll) >= WIDTH:
            scroll = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP]: # If user hits up arrow
            plane.y -= VELOCITY
        if keys_pressed[pygame.K_DOWN]: # If user hits down arrow
            plane.y += VELOCITY
        if keys_pressed[pygame.K_LEFT]: # If user hits left arrow
            plane.x -= VELOCITY
        if keys_pressed[pygame.K_RIGHT]: # If user hits right arrow
            plane.x += VELOCITY
        
        WINDOW.blit(airplane, plane)
        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()


