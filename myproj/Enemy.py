
from Character import Character
import pygame

class Enemy(Character):

    def __init__(self, name, imagePath, velocity, bulletColor, bulletVelocity, initPosX, initPosY):
        super().__init__(name, imagePath, velocity, initPosX, initPosY)
        self.bulletColor = bulletColor
        self.bulletVelocity = bulletVelocity




    

