# Abstracat class for olane in the game.
# Vehicle should have velocity up, velocity down, left, right and other properties that all vehicles share
from abc import ABC, abstractmethod


class Plane(ABC):
    
    def __init__(self, name, velocity, bulletVelocity):
        self.name = name
        self.velocity = velocity
        self.bulletVelocity = bulletVelocity

    
    @abstractmethod
    def movement(self):
        pass
    @abstractmethod
    def bullet(self):
        pass
    

