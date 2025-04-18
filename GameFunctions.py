import sys
import pygame as pg
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_RIGHT:
            ship.moving_right = True
        if event.key == pg.K_LEFT:
            ship.moving_left = True
        if event.key == pg.K_UP:
            ship.moving_up = True
        if event.key == pg.K_DOWN:
            ship.moving_down = True
        elif event.key == pg.K_SPACE:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.type == pg.KEYUP:
        if event.key == pg.K_RIGHT:
            ship.moving_right = False
        if event.key == pg.K_LEFT:
            ship.moving_left = False
        if event.key == pg.K_UP:
            ship.moving_up = False
        if event.key == pg.K_DOWN:
            ship.moving_down = False


def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pg.display.flip()