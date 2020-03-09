# 游戏入口
import pygame
from pygame.sprite import Group

import game.game_functions as game_funcs
from game.settings import Settings
from game.ship import Ship


def run_game():
    # init
    pygame.init()

    # config
    cfg = Settings()
    screen = pygame.display.set_mode((cfg.screen_width, cfg.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(cfg, screen)

    # 创建子弹
    bullets = Group()

    # usage
    print("started game. press keyboard to start playing.")
    while True:
        game_funcs.check_events(cfg, screen, ship, bullets)
        ship.update()
        game_funcs.update_bullets(bullets)
        game_funcs.update_screen(cfg, screen, ship, bullets)


# main entry
run_game()
