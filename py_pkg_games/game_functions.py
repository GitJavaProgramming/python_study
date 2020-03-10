# 游戏公共函数模块
import sys
from time import sleep

import pygame

from game.alien import Alien
from game.bullet import Bullet


def check_keydown_events(e_key, cfg, screen, ship, bullets):
    if e_key == pygame.K_RIGHT:
        ship.moving_right = True
    elif e_key == pygame.K_LEFT:
        ship.moving_left = True
    elif e_key == pygame.K_SPACE:
        fire(cfg, screen, ship, bullets)
    elif e_key == pygame.K_q:
        sys.exit()


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
def update_screen(cfg, screen, ship, bullets, aliens, stats, play_button):
    screen.fill(cfg.bg_color)

    # 重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


# 更新子弹的位置，并删除已消失的子弹
def update_bullets(cfg, screen, ship, bullets, aliens):
    bullets.update()
    # 从内存bullets中删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))
    check_bullet_alien_collisions(cfg, screen, ship, bullets, aliens)


def check_bullet_alien_collisions(cfg, screen, ship, bullets, aliens):
    # 碰撞检测，子弹击中就删除外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(cfg, screen, aliens, ship)


# 开火
def fire(cfg, screen, ship, bullets):
    if len(bullets) < cfg.bullets_allowed:  # 限制子弹数量
        new_bullet = Bullet(cfg, screen, ship)
        bullets.add(new_bullet)


# 外星人数
def get_number_aliens_x(cfg, alien_width):
    available_space_x = cfg.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))  # 创建的外星人数，外星人之间间隔
    return number_aliens_x


# 计算屏幕上可以容纳多少行外星人
def get_number_rows(cfg, ship_height, alien_height):
    available_space_y = (cfg.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


# 制造外星人
def create_alien(cfg, screen, aliens, alien_number, row_number):
    alien = Alien(cfg, screen)
    alien_width = alien.rect.width  # 一个外星人的宽度
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


# 创建一群外星人
def create_fleet(cfg, screen, aliens, ship):
    # 创建一个外星人，并计算一行可容纳多少个外星人
    alien = Alien(cfg, screen)
    number_aliens_x = get_number_aliens_x(cfg, alien.rect.width)
    number_rows = get_number_rows(cfg, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(cfg, screen, aliens, alien_number, row_number)


def check_fleet_edges(cfg, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(cfg, aliens)
            break


def change_fleet_direction(cfg, aliens):
    for alien in aliens.sprites():
        alien.rect.y += cfg.fleet_drop_speed
    cfg.fleet_direction *= -1


# 检测是否有外星人位于屏幕边缘，并更新整群外星人的位置
def update_aliens(cfg, screen, ship, bullets, aliens, stats):
    check_fleet_edges(cfg, aliens)
    aliens.update()

    # 撞机
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit!!!")
        ship_hit(cfg, screen, ship, bullets, aliens, stats)

    # 外星人到底屏幕底端
    check_alien_bottom(cfg, screen, ship, bullets, aliens, stats)


# 统计信息
def ship_hit(cfg, screen, ship, bullets, aliens, stats):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        create_fleet(cfg, screen, aliens, ship)
        ship.center_ship()
        # time.sleep 暂停
        sleep(0.5)
    else:
        stats.game_active = False


def check_alien_bottom(cfg, screen, ship, bullets, aliens, stats):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(cfg, screen, ship, bullets, aliens, stats)
            break
