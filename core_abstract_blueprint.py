from abc import ABC, abstractclassmethod
import pygame

class GameObject(pygame.sprite.Sprite, ABC):
    def __init__(self, image, init_pos, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = imageself.rect = self.image.get_rect() if hasattr(image, 'get_rect') else None

        self._speed = speed