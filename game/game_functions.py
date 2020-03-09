# 游戏公共函数模块
import sys

import pygame

from game.bullet import Bullet


def check_keydown_events(e_key, cfg, screen, ship, bullets):
    if e_key == pygame.K_RIGHT:
        ship.moving_right = True
    elif e_key == pygame.K_LEFT:
        ship.moving_left = True
    elif e_key == pygame.K_SPACE:
        fire(cfg, screen, ship, bullets)


def check_keyup_events(e_key, ship):
    if e_key == pygame.K_RIGHT:
        ship.moving_right = False
    elif e_key == pygame.K_LEFT:
        ship.moving_left = False


# 事件  事件类型、事件key -- 函数在当前文件内，没有访问控制权限public private
def check_events(cfg, screen, ship, bullets):
    for event in pygame.event.get():
        e_type = event.type
        if e_type == pygame.QUIT:
            sys.exit()
        elif e_type == pygame.KEYDOWN:
            e_key = event.key
            print("event type: " + str(e_key))
            check_keydown_events(e_key, cfg, screen, ship, bullets)
        elif e_type == pygame.KEYUP:
            e_key = event.key
            print("event type: " + str(e_key))
            check_keyup_events(e_key, ship)


# 更新屏幕
def update_screen(cfg, screen, ship, bullets):
    screen.fill(cfg.bg_color)

    # 重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    pygame.display.flip()


# 更新子弹的位置，并删除已消失的子弹
def update_bullets(bullets):
    bullets.update()
    # 从内存bullets中删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))


# 开火
def fire(cfg, screen, ship, bullets):
    if len(bullets) < cfg.bullets_allowed:  # 限制子弹数量
        new_bullet = Bullet(cfg, screen, ship)
        bullets.add(new_bullet)
