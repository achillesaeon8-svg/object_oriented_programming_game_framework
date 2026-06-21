import pygame
from core_abstract_blueprint import GameObject

class EnemyShips(GameObject):
    def __init__(self, enemy_image, enemy_down_image, initial_position):
        
        super().__init__(enemy_image, initial_position, 2)

        self.rect = enemy_image.get_rect()
        self.rect.topleft = initial_position
        self.down_imgs = enemy_down_image
        self.down_index = 0

    def move(self):
        self.rect.top += self.speed