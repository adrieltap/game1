import pygame
class Character:
 
    def __init__ (self, name, imagePath, velocity, initPosX, initPosY):
        self.name = name
        self.imagePath = imagePath
        self.velocity = velocity
        self.width = 90
        self.height = 75
        self.loadImage = pygame.image.load(self.imagePath)
        self.Image = pygame.transform.scale(self.loadImage, (self.width , self.height))
        self.charRect = pygame.Rect(initPosX, initPosY, self.width , self.height)
        self.screenHEIGHT = 576
        self.screenWIDTH = 1024

    
    # RETURNS LIST WIDTH AND HEIGHT OF ALL CHARACTERS
    # def dimensions(self):
    #     return [90,75] ## [WIDTH, HEIGHT]
    
        
        


    