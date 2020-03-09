# 外星人
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, cfg, screen):
        super(Alien, self).__init__()
        self.cfg = cfg
        self.screen = screen

        self.image = pygame.image.load('images/alien32.png')
        self.rect = self.image.get_rect()
        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.cfg.alien_speed_factor
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.cfg.alien_speed_factor * self.cfg.fleet_direction
        self.rect.x = self.x
