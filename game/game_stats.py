# 游戏统计信息
class GameStats():
    def __init__(self, cfg):
        self.cfg = cfg
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.cfg.ship_limit
