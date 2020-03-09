# 飞船(在屏幕上的属性，行为)
import pygame


class Ship():
    def __init__(self, cfg, screen):
        self.cfg = cfg
        self.screen = screen

        # load
        self.image = pygame.image.load('images/ship32.bmp')

        # 飞船放在屏幕底部中央
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 左右移动飞船
        self.moving_right = False
        self.moving_left = False

        # center属性存储float值
        self.center = float(self.rect.centerx)

    def update(self):
        # print("ship updating...")  # 一直重画？？
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.cfg.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.cfg.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        # 指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
