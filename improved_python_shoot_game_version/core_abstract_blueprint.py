from abc import ABC, abstractmethod
import pygame

class GameObject(pygame.sprite.Sprite, ABC):
    def __init__(self, image, initial_position, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.image = self.image.get_rect = self.image.get_rect() if hasattr(image, 'get_rect') else None

        self._speed = speed 

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError('Speed cannot be negative')
        self._speed = value

    @abstractmethod
    def move(self):
        pass