# 游戏统计信息
class GameStats():
    def __init__(self, cfg):
        self.cfg = cfg
        self.reset_stats()
        self.game_active = False  # 游戏开始由外部控制

        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.cfg.ship_limit
        self.score = 0
