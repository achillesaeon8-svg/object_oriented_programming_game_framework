import pygame
from core_abstract_blueprint import GameObject

class ShipBullets(GameObject):
    def __init__(self, bullet_image, initial_position):
        
        super().__init__(bullet_image, initial_position, 10)
        
        self.rect = bullet_image.get_rect()
        self.rect.midbottom = initial_position

    def move(self):
        self.rect.top -= self.speed