from Character import Character
import pygame
import random

class Plane(Character):

    def __init__(self, name, imagePath, velocity, bulletColor, bulletVelocity, initPosX, initPosY):
        super().__init__(name, imagePath, velocity, initPosX, initPosY)
        self.bulletColor = bulletColor
        self.bulletVelocity = bulletVelocity
        self.bullet = pygame.Rect(self.charRect.x + self.charRect.width, self.charRect.y + self.charRect.height // 2, 10, 5)
        self.planeBullets = []
        self.health = 3
        self.score = 0

    def drawCharacter(self, playWINDOW):
        playWINDOW.blit(self.Image, self.charRect)


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
    
    def fireBullet(self):
        if len(self.planeBullets) < 3:
            self.bullet = pygame.Rect(self.charRect.x + self.charRect.width, self.charRect.y + self.charRect.height // 2, 10, 5)
            self.planeBullets.append(self.bullet)
        
    def drawBullet(self, playWINDOW, allEnemies, ENEMY_HIT):
        for bullet in self.planeBullets:
            bullet.x += self.bulletVelocity
            for enemies in allEnemies:
                if enemies.charRect.colliderect(bullet):
                    pygame.event.post(pygame.event.Event(ENEMY_HIT))
                    self.planeBullets.remove(bullet)
                    enemies.respawn()
            if bullet in self.planeBullets: 
                if bullet.x + self.bulletVelocity > self.screenWIDTH + 15:
                    self.planeBullets.remove(bullet)
        for bullet in self.planeBullets:
            pygame.draw.rect(playWINDOW, self.bulletColor, bullet)
    

    
    
        
 
        



    
  


    
        
      

