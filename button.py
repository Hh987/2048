import pygame.font


class Button:
    """游戏按钮类"""
    def __init__(self, ai_game, msg):
        """初始化按钮"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        self.rect = pygame.Rect(0, 0, self.settings.button_width, self.settings.button_height)
        self.rect.right = self.screen_rect.right
        self.rect.top = self.screen_rect.top

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """将msg渲染为图像"""
        self.msg_image = self.settings.button_font.render(msg, True, self.settings.button_text_color,
                                                          self.settings.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制按钮"""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
