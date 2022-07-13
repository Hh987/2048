import pygame


class Background:
    """管理游戏背景的类"""
    def __init__(self, ai_game):
        """游戏背景初始化"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.status = ai_game.status

    def draw_score(self):
        """绘制得分和最高得分"""
        # 绘制得分
        score_str = "得分:{:,}".format(self.status.score)
        self.score_image = self.settings.score_font.render(score_str, True,
                                                           self.settings.score_text_color,
                                                           self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left
        self.score_rect.top = self.screen_rect.top

        # 绘制最高得分
        high_score_str = "最高分:{:,}".format(self.status.high_score)
        self.high_score_image = self.settings.score_font.render(high_score_str, True,
                                                                self.settings.score_text_color,
                                                                self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left
        self.high_score_rect.top = self.score_rect.bottom + 10

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def draw_line(self):
        """绘制网格"""
        grid_width_half = int(self.settings.grid_width / 2)

        # 绘制横线
        for i in range(5):
            pygame.draw.line(self.screen, self.settings.grid_color,
                             (0, grid_width_half +
                              i * (self.settings.size + self.settings.grid_width) + self.settings.score_height),
                             (self.settings.screen_width, grid_width_half +
                              i * (self.settings.size + self.settings.grid_width) + self.settings.score_height),
                             self.settings.grid_width)
        # 绘制竖线
        for j in range(5):
            pygame.draw.line(self.screen, self.settings.grid_color,
                             (grid_width_half + j * (self.settings.size + self.settings.grid_width),
                              self.settings.score_height),
                             (grid_width_half + j * (self.settings.size + self.settings.grid_width),
                              self.settings.scree_height),
                             self.settings.grid_width)

    def draw_win(self):
        """绘制胜利提示语"""
        win_str = "You Win!"
        self.win_str_image = self.settings.score_font.render(win_str, True,
                                                            self.settings.score_text_color,
                                                            self.settings.bg_color)

        self.win_str_image_rect = self.win_str_image.get_rect()
        self.win_str_image_rect.center = self.screen_rect.center
        self.screen.blit(self.win_str_image, self.win_str_image_rect)

    def draw_over(self):
        """绘制失败提示语"""
        over_str = "Game Over!"
        self.over_str_image = self.settings.score_font.render(over_str, True,
                                                            self.settings.score_text_color,
                                                            self.settings.bg_color)

        self.over_str_image_rect = self.over_str_image.get_rect()
        self.over_str_image_rect.center = self.screen_rect.center
        self.screen.blit(self.over_str_image, self.over_str_image_rect)
