from Character import Character
import pygame

class Plane(Character):

    def __init__(self, name, imagePath, velocity, bulletColor, bulletVelocity):
        self.initPosX = 150
        self.initPosY = 238
        super().__init__(name, imagePath, velocity, self.initPosX, self.initPosY)
        self.bulletColor = bulletColor
        self.bulletVelocity = bulletVelocity

        

    # This function controls the velocity of the player when moving their Flyer/self
# it also keeps the self within bounds of the screen 
    def movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_UP] and self.charRect.y - self.velocity > 0: # If user hits up arrow
            self.charRect.y -= self.velocity 
        if keys_pressed[pygame.K_DOWN] and self.charRect.y + self.velocity < self.screenHEIGHT - self.height: # If user hits down arrow
            self.charRect.y += self.velocity
        if keys_pressed[pygame.K_LEFT] and self.charRect.x - self.velocity  > 0: # If user hits left arrow
            self.charRect.x -= self.velocity
        if keys_pressed[pygame.K_RIGHT] and self.charRect.x + self.velocity < self.screenWIDTH - self.height : # If user hits right arrow
            self.charRect.x += self.velocity
    


    
  


    
        
      

