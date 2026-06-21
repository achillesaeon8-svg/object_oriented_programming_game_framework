import pygame
from core_abstract_blueprint import GameObject

class Enemy(GameObject):
    def __init__(self, enemy_img, enemy_down_imgs, init_pos):
       super().__init__(enemy_img, init_pos, speed=2)

    def move(self):
        self.rect.top += self.speed