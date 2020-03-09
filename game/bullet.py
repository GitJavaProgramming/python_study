# 飞船的子弹
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, cfg, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, cfg.bullet_width, cfg.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = cfg.bullet_color
        self.speed_factor = cfg.bullet_speed_factor

    def update(self, *args):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
