import pygame
from core_abstract_blueprint import GameObject
from bullet_sprite import ShipBullets
from global_configuration_constants import SCREEN_WIDTH, SCREEN_HEIGHT

class PlayerShip(GameObject):
    def __init__(self, plane_image, player_rectangles, initial_position):

        surface_frames = [plane_image.subsurface(rect).convert_alpha() for rect in player_rectangles]

        super().__init__(surface_frames[0], initial_position, speed=8)

        self.image = surface_frames

        self.rect = self.image[0].get_rect()
        self.rect.topleft = initial_position

        self.bullets = pygame.sprite.Group()
        self.img_index = 0
        self.is_hit = False

    @property
    def is_hit(self):
        return self._is_hit

    @is_hit.setter
    def is_hit(self, value):
        self._is_hit = bool(value)

    def shoot(self, bullet_image):
        new_bullet = ShipBullets(bullet_image, self.rect.midtop)
        self.bullets.add(new_bullet)

    def move(self):
        pass

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed