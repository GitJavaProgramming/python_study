# 游戏整体的封装
class OverAll:
    def __init__(self, cfg, screen, ship, bullets, aliens, stats, sb):
        self.cfg = cfg
        self.screen = screen
        self.ship = ship
        self.bullets = bullets
        self.aliens = aliens
        self.stats = stats
        self.sb = sb
