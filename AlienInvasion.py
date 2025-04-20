import pygame as pg
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import GameFunctions as gf

#Inicialização do game
def run_game():
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen, ai_settings)
    bullets = Group()
    pg.display.set_caption("Alien Invasion")
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        
run_game()

