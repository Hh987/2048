class GameStats:
    """跟踪游戏状态的类"""
    def __init__(self, ai_game):
        """初始化游戏状态"""
        self.settings = ai_game.settings
        self.is_win = False
        self.is_over = False
        self.reset_stats()

        self.score = 0

    def reset_stats(self):
        """重置游戏状态"""
        self.score = 0
        self.is_win = False
        self.is_over = False

    def load_high_score(self):
        """载入最高分"""
        with open("high_score.txt", "r") as f:
            self.high_score = int(f.read())

    def save_high_score(self):
        """存储最高分"""
        with open("high_score.txt", "w") as f:
            f.write(str(self.high_score))
