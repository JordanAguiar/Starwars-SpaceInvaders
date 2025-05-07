import pygame as pg
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import GameFunctions as gf
from game_stats import GameStats



#Inicialização do game
def run_game():
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen, ai_settings)
    tiefighters = Group()
    gf.create_fleet(ai_settings, screen, ship, tiefighters)
    bullets = Group()
    pg.display.set_caption("Millennium x TieFighters")
    stats = GameStats(ai_settings)
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, tiefighters, bullets)
        gf.update_tiefighters(ai_settings, stats, screen, ship, tiefighters, bullets)
        gf.update_screen(ai_settings, screen, ship, tiefighters, bullets)

run_game()

