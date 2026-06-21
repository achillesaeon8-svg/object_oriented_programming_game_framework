import pygame
from core_abstract_blueprint import GameObject

class ShipBullets(pygame.sprite.Sprite):
    def __init__(self, bullet_imgage, initial_position):
        
        super().__init__(bullet_imgage, initial_position, speed=10)
        if self.rect:
            self.rect.midbottom = initial_position

    def move(self):
        self.rect.top -= self.speed