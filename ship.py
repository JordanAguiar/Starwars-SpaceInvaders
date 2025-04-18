#Atributos da nave
import pygame as pg

class Ship():
    def __init__(self, screen, ai_settings):
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pg.image.load('imagens/starship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.vertical = float(self.rect.centery)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        self.rect.centerx = self.center
        self.rect.centery = self.vertical
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.vertical -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.vertical += self.ai_settings.ship_speed_factor


    def blitme(self):
        self.screen.blit(self.image, self.rect)