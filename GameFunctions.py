import sys
import pygame as pg
import pygame.sprite
from time import sleep
from bullet import Bullet
from tiefighter import Tiefighter


def check_events(ai_settings, screen, ship, bullets):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)



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
            fire_bullet(ai_settings, screen, ship, bullets)
        elif event.key == pg.K_q:
            sys.exit()


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

def update_bullets(ai_settings, screen, ship, tiefighters, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_tiefighter_collisions(ai_settings,screen, ship, tiefighters, bullets)


def check_bullet_tiefighter_collisions(ai_settings, screen, ship, tiefighters, bullets):
    collisions = pygame.sprite.groupcollide(bullets, tiefighters, True,True)  # i will verify this code soon, because there is a bug when you shoot at the tie fighters
    if len(tiefighters) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, tiefighters)



def get_number_tiefighters_x(ai_settings, tiefighter_width):
    available_space_x = ai_settings.screen_width - 2 * tiefighter_width
    number_tiefighters_x = int(available_space_x / (2 * tiefighter_width))
    return number_tiefighters_x

def create_tiefighter(ai_settings, screen, tiefighters, tiefighter_number, row_number):
    tiefighter = Tiefighter(ai_settings, screen)
    tiefighter_width = tiefighter.rect.width
    tiefighter.x = tiefighter_width + 2 * tiefighter_width * tiefighter_number
    tiefighter.rect.x = tiefighter.x
    tiefighter.rect.y = tiefighter.rect.height + 2 * tiefighter.rect.height * row_number
    tiefighters.add(tiefighter)

def create_fleet(ai_settings, screen, ship, tiefighters):
    tiefighter = Tiefighter(ai_settings, screen)
    number_tiefighters_x = get_number_tiefighters_x(ai_settings, tiefighter.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, tiefighter.rect.height)
    for row_number in range(number_rows):
        for tiefighter_number in range(number_tiefighters_x):
            create_tiefighter(ai_settings, screen, tiefighters, tiefighter_number, row_number)

def get_number_rows(ai_settings, ship_height, tiefighter_height):
    available_space_y = (ai_settings.screen_height - (3* tiefighter_height))
    number_rows = int(available_space_y / (2* tiefighter_height))
    return number_rows


def check_fleet_edges(ai_settings, tiefighters):
    for tiefighter in tiefighters.sprites():
        if tiefighter.check_edges():
            change_fleet_direction(ai_settings, tiefighters)
            break



def change_fleet_direction(ai_settings, tiefighters):
    for tiefighter in tiefighters.sprites():
        tiefighter.rect.y += ai_settings.fleet_drop_speed
        ai_settings.fleet_direction *= -1



def update_tiefighters(ai_settings, stats, screen, ship, tiefighters, bullets):
    check_fleet_edges(ai_settings, tiefighters)
    tiefighters.update()
    if pg.sprite.spritecollideany(ship, tiefighters):
        ship_hit(ai_settings, stats, screen, ship, tiefighters, bullets)
        print("Millennium Falcon hit!!!")

def ship_hit(ai_settings, stats, screen, ship, tiefighters, bullets):
    stats.ship_left -= 1
    tiefighters.empty()
    bullets.empty()
    create_fleet(ai_settings, screen, ship, tiefighters)
    ship.center_ship()
    sleep(0.5)

def update_screen(ai_settings, screen, ship, tiefighters, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    tiefighters.draw(screen)
    pg.display.flip()