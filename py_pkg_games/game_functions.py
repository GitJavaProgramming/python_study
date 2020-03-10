# 游戏公共函数模块
import sys
from time import sleep

import pygame

from game.alien import Alien
from game.bullet import Bullet

''' 事件处理
'''


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
def check_events(cfg, screen, ship, bullets, aliens, stats, play_button, sb):
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
        elif e_type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(cfg, screen, ship, bullets, aliens, stats, play_button, sb, mouse_x, mouse_y)


def check_play_button(cfg, screen, ship, bullets, aliens, stats, play_button, sb, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        cfg.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重新统计游戏信息
        stats.reset_stats()
        stats.game_active = True
        # 重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        create_fleet(cfg, screen, aliens, ship)
        ship.center_ship()


''' 更新子弹相关信息
'''


# 更新子弹的位置，并删除已消失的子弹
def update_bullets(cfg, screen, ship, bullets, aliens, stats, sb):
    bullets.update()
    # 从内存bullets中删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))
    check_bullet_alien_collisions(cfg, screen, ship, bullets, aliens, stats, sb)


# 判断子弹是否击中外星人
def check_bullet_alien_collisions(cfg, screen, ship, bullets, aliens, stats, sb):
    # 碰撞检测，子弹击中就删除外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += cfg.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
        # stats.reset_stats()

    if len(aliens) == 0:
        bullets.empty()
        # 加快游戏节奏，创建一群新的外星人
        cfg.increase_speed()
        # 通关提高等级
        stats.level += 1
        sb.prep_level()

        create_fleet(cfg, screen, aliens, ship)


# 开火
def fire(cfg, screen, ship, bullets):
    if len(bullets) < cfg.bullets_allowed:  # 限制子弹数量
        new_bullet = Bullet(cfg, screen, ship)
        bullets.add(new_bullet)


'''
外星人
'''


# 计算屏幕上一行可生成的外星人数
def get_number_aliens_x(cfg, alien_width):
    available_space_x = cfg.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))  # 创建的外星人数，外星人之间间隔
    return number_aliens_x


# 计算屏幕上可以容纳多少行外星人
def get_number_rows(cfg, ship_height, alien_height):
    available_space_y = (cfg.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


# 制造一个外星人放入列表aliens
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


# 外星人是否撞墙 撞墙后的外星人改变移动方向
def check_fleet_edges(cfg, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(cfg, aliens)
            break


# 改变一群外星人方向
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


def check_alien_bottom(cfg, screen, ship, bullets, aliens, stats):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(cfg, screen, ship, bullets, aliens, stats)
            break


''' 游戏的统计信息
'''


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
        pygame.mouse.set_visible(True)


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


''' 更新屏幕信息
'''


# 更新屏幕
def update_screen(cfg, screen, ship, bullets, aliens, stats, play_button, sb):
    screen.fill(cfg.bg_color)

    # 重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # 显示得分
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
