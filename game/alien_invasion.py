# 游戏入口
import pygame
from pygame.sprite import Group

import py_pkg_games.game_functions as game_funcs
from game.button import Button
from game.game_stats import GameStats
from game.settings import Settings
from game.ship import Ship


# 配置类|screen|sprite(飞船|子弹|外星人)
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
    # 创建外星人
    # alien = Alien(cfg, screen)
    aliens = Group()
    game_funcs.create_fleet(cfg, screen, aliens, ship)

    # 游戏统计信息
    stats = GameStats(cfg)

    # 按钮控制
    play_button = Button(cfg, screen, "Play")

    # usage
    print("started game. press keyboard to start playing.")
    while True:
        game_funcs.check_events(cfg, screen, ship, bullets, aliens, stats, play_button)
        if stats.game_active:
            ship.update()
            game_funcs.update_bullets(cfg, screen, ship, bullets, aliens)
            game_funcs.update_aliens(cfg, screen, ship, bullets, aliens, stats)
        game_funcs.update_screen(cfg, screen, ship, bullets, aliens, stats, play_button)


# main entry
run_game()
