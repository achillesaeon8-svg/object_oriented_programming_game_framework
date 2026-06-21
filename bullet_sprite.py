import pygame
from core_abstract_blueprint import GameObject

class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        
        super().__init__(bullet_img, init_pos, speed=10)

    def move(self):
        self.rect.top -= self.speed