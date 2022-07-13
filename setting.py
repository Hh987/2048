import pygame.font


class Settings:
    """游戏设置类"""
    def __init__(self):
        # 方块设置
        self.size = 100
        self.colors = {0: (205, 193, 180),
                       2: (238, 228, 218),
                       4: (237, 224, 200),
                       8: (242, 177, 121),
                       16: (245, 149, 99),
                       32: (246, 142, 95),
                       64: (246, 94, 59),
                       128: (237, 207, 114),
                       256: (237, 204, 98),
                       512: (237, 200, 80),
                       1024: (237, 197, 63),
                       2048: (225, 187, 0)
                       }

        self.num_font = pygame.font.Font(None, 50)
        self.num_color = (0, 0, 0)

        # 分界线设置
        self.grid_width = 10
        self.grid_color = (255, 222, 173)

        # 得分区设置
        self.score_height = 100
        self.score_width = 140
        self.score_text_color = (242, 177, 121)
        self.score_font = pygame.font.SysFont('SimHei', 30)

        # 按钮设置
        self.button_width = 150
        self.button_height = 40
        self.button_color = (205, 193, 180)
        self.button_text_color = (0, 0, 0)
        self.button_font = pygame.font.SysFont(None, 40)

        # 游戏界面设置
        self.screen_width = ((self.size + self.grid_width) * 4) + self.grid_width
        self.scree_height = ((self.grid_width + self.size) * 4) + self.score_height + self.grid_width
        self.bg_color = (255, 239, 213)
