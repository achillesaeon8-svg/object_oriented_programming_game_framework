import pygame
from improved_python_shoot_game_version.core_abstract_blueprint import GameObject

class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        
        super().__init__(bullet_img, init_pos, speed=10)
        if self.rect:
            self.rect.midbottom = init_pos

    def move(self):
        self.rect.top -= self.speed