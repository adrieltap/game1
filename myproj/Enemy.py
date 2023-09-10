
from Plane import Plane
from Character import Character
import pygame
import random


class Enemy(Plane):
    instances = []
   
    def __init__(self, name, imagePath, bulletColor, bulletVelocity):
        self.bulletVelocity = random.randint(4, 8)
        self.velocity = random.randint(1, 3)
        initPosX = 1024
        initPosY = random.randint(0, 288)
        Enemy.instances.append(self)
        
        self.vertical_speed = 0.5
        super().__init__(name, imagePath, self.velocity, bulletColor, bulletVelocity, initPosX, initPosY)
    
        
    def respawn(self):
        self.charRect.x = self.screenWIDTH + self.width
        self.charRect.y = random.randint(0, self.screenHEIGHT)

    def movement(self):
        # enemy plane will always move right to left, but we can randomize the vertical movement
        # we also need to make sure the plane doesnt go off the screen
        self.vertical_direction = random.choice([-1, 1])
        if self.charRect.x - self.velocity < 0 - self.width or self.charRect.y < 0  or self.charRect.y > self.screenHEIGHT:
            self.respawn()
        self.charRect.x -= self.velocity
        self.charRect.y += self.vertical_direction * self.vertical_speed
    
    def fireBullet(self):
        fire = random.choice([0, 1])
        if fire and len(self.planeBullets) < 1:
            self.bullet = pygame.Rect(self.charRect.x, self.charRect.y + self.charRect.height // 2, 10, 5)
            self.planeBullets.append(self.bullet)
    
    
    def drawBullet(self, playWINDOW, player1, PLAYER1_HIT):
        for bullet in self.planeBullets:
            bullet.x -= self.bulletVelocity
            if player1.charRect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(PLAYER1_HIT))
                self.planeBullets.remove(bullet)
            elif bullet.x + self.bulletVelocity < 0 - self.screenWIDTH // 3:
                self.planeBullets.remove(bullet)
        for bullet in self.planeBullets:
            pygame.draw.rect(playWINDOW, self.bulletColor, bullet)
        

        
    
        

    






    

