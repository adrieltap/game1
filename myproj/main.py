import pygame
import math

clock = pygame.time.Clock()
FPS = 60

# load window
WIDTH, HEIGHT = 1024, 576
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Running Game!")

# load bacgkround image
background = pygame.image.load("sky4.png")
background = pygame.transform.scale(background, (WIDTH , HEIGHT))

def main():

    tiles = 3 # 2 for now, however when I have multiple images I might have to scale them correctly
    scroll = 0 # scrolling for background

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
        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()


