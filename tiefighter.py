import pygame as pg
from pygame.sprite import Sprite

class Tiefighter(Sprite):
    def __init__(self, ai_settings, screen):
        super(Tiefighter, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pg.image.load('imagens/tiefighter.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)


    def update(self):
        self.x += (self.ai_settings.tiefighter_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect =self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        self.screen.blit(self.image, self.rect)