import sys
import pygame
import random

from setting import Settings
from game_status import GameStats
from background import Background
from button import Button


class Game2048:
    """游戏资源类"""
    def __init__(self):
        # 游戏界面初始化
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.scree_height))

        # 标题
        pygame.display.set_caption("2048")

        # 游戏列表
        self.game_list = [[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]]

        # 游戏状态
        self.status = GameStats(self)
        self.status.load_high_score()

        # 背景
        self.background = Background(self)

        # 按钮
        self.new_game_button = Button(self, "New Game")

    def run_game(self):
        """主循环"""
        self._random()
        while True:
            self._check_event()
            self._check_game_status()
            self._update_screen()
            if self.status.is_win or self.status.is_over:
                self.status.save_high_score()

    def _check_event(self):
        """相应鼠标和键盘输入"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_button(mouse_pos)

    def _check_key_down_event(self, event):
        """检查键盘输入"""
        if event.key == pygame.K_LEFT:
            self._move_left()
        elif event.key == pygame.K_RIGHT:
            self._move_right()
        elif event.key == pygame.K_UP:
            self._move_up()
        elif event.key == pygame.K_DOWN:
            self._move_down()

        # 如果游戏没有结束就继续随机生成数字
        if not(self.status.is_win or self.status.is_over):
            self._random()

    def combination(self, temp_list):
        """结合一行或一列相同方块
           将行或列中的数字按顺序存储在temp_list列表中
           然后根据不同情况进行合并
        """
        nums = []
        ans = [0, 0, 0, 0]
        for i in temp_list:
            if i != 0:
                nums.append(i)
        length = len(nums)

        # 没有数字
        if length == 0:
            return ans
        # 只有一个数字
        elif length == 1:
            ans[0] = nums[0]
            return ans
        # 有两个数字
        elif length == 2:
            # case 1
            if nums[0] == nums[1]:
                ans[0] = nums[0] + nums[1]
                self.status.score += ans[0]
                return ans
            # case 2
            else:
                ans[0] = nums[0]
                ans[1] = nums[1]
                return ans
        # 有三个数字
        elif length == 3:
            # case 1
            if nums[0] == nums[1]:
                ans[0] = nums[0] + nums[1]
                ans[1] = nums[2]
                self.status.score += ans[0]
                return ans
            # case 2
            elif nums[1] == nums[2]:
                ans[0] = nums[0]
                ans[1] = nums[1] + nums[2]
                self.status.score += ans[1]
                return ans
            # case 3
            else:
                nums.append(0)
                return nums
        # 有四个数字
        else:
            # case 1
            if nums[0] == nums[1]:
                ans[0] = nums[0] + nums[1]
                self.status.score += ans[0]
                # 1 2和3 4位置的数字分别相等
                if nums[2] == nums[3]:
                    ans[1] = nums[2] + nums[3]
                    self.status.score += ans[1]
                    return ans
                # 只有1 2位置相等
                else:
                    ans[1] = nums[2]
                    ans[2] = nums[3]
                    return ans
            # case 2
            # 中间两个数字相等
            elif nums[1] == nums[2]:
                ans[0] = nums[0]
                ans[1] = nums[1] + nums[2]
                ans[2] = nums[3]
                self.status.score += ans[1]
                return ans
            # case 3
            # 3 4两个数字相等
            elif nums[2] == nums[3]:
                ans[0] = nums[0]
                ans[1] = nums[1]
                ans[2] = nums[2] + nums[3]
                self.status.score += ans[2]
                return ans
            # case 4
            # 四个数字都不相等
            else:
                return nums

    def _move_left(self):
        """左移操作"""
        for i in range(4):
            temp = self.combination(self.game_list[i])
            for j in range(4):
                self.game_list[i][j] = temp[j]

    def _move_right(self):
        """右移操作"""
        for i in range(4):
            temp = self.combination(self.game_list[i][::-1])
            for j in range(4):
                self.game_list[i][3 - j] = temp[j]

    def _move_up(self):
        """上移操作"""
        for i in range(4):
            temp = []
            for j in range(4):
                temp.append(self.game_list[j][i])
            temp = self.combination(temp)
            for k in range(4):
                self.game_list[k][i] = temp[k]

    def _move_down(self):
        """下移操作"""
        for i in range(4):
            temp = []
            for j in range(4):
                temp.append(self.game_list[3 - j][i])
            temp = self.combination(temp)
            for k in range(4):
                self.game_list[3 - k][i] = temp[k]

    def _check_game_status(self):
        """检查游戏状态"""
        # 判断游戏是否胜利，同时将没有数字的位置存在empty_pos列表中
        empty_pos = []
        for i in range(4):
            for j in range(4):
                if self.game_list[i][j] == 2048:
                    self.status.is_win = True
                if self.game_list[i][j] == 0:
                    empty_pos.append([i, j])

        # empty_list为空则说明方格全部填满，判断相邻方块是否有相同，没有则游戏失败
        if len(empty_pos) == 0:
            flag = True
            for i in range(4):
                for j in range(3):
                    if self.game_list[i][j] == self.game_list[i][j + 1]:
                        flag = False
            for i in range(4):
                for j in range(3):
                    if self.game_list[j][i] == self.game_list[j + 1][i]:
                        flag = False
            if flag:
                self.status.is_over = True

    def _random(self):
        """随机位置生成2或4"""
        # 列表empty_list存储没有数字的位置
        empty_pos = []
        for i in range(4):
            for j in range(4):
                if self.game_list[i][j] == 0:
                    empty_pos.append([i, j])

        # empty_list非空则继续随机生成
        if len(empty_pos) != 0:
            i_pos, j_pos = random.choice(empty_pos)
            num = random.randint(1, 2)
            self.game_list[i_pos][j_pos] = num * 2

    def _check_button(self, mouse_pos):
        """确定点击按钮"""
        # 点击New Game按钮
        button_clicked = self.new_game_button.rect.collidepoint(mouse_pos)
        if button_clicked:
            # 将游戏重置，同时随机生成一个2或4
            self.game_list = [[0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0]]
            self._random()
            self.status.reset_stats()

    def _show_game(self):
        """绘制4×4数字方块"""
        for i in range(4):
            for j in range(4):
                rect_color = self.settings.colors[self.game_list[i][j]]
                rect_pos = [(j + 1) * self.settings.grid_width + j * self.settings.size,
                            self.settings.score_height + (i + 1) * self.settings.grid_width + i * self.settings.size]
                pygame.draw.rect(self.screen, rect_color, (rect_pos, (self.settings.size, self.settings.size)), 0)

                # 如果数字是0就不绘制
                if self.game_list[i][j] != 0:
                    num_image = self.settings.num_font.render(str(self.game_list[i][j]), True,
                                                              self.settings.num_color,
                                                              rect_color)
                    num_image_rect = num_image.get_rect()
                    num_rect_pos = [(j + 1) * self.settings.grid_width + (j + 0.5) * self.settings.size,
                                    self.settings.score_height + (i + 1) * self.settings.grid_width +
                                    (i + 0.5) * self.settings.size]
                    num_image_rect.center = tuple(num_rect_pos)
                    self.screen.blit(num_image, num_image_rect)

    def _update_screen(self):
        """更新游戏屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.new_game_button.draw_button()
        self.background.draw_line()
        self._show_game()

        # 判断当前得分是否大于最高分
        if self.status.score > self.status.high_score:
            self.status.high_score = self.status.score
        self.background.draw_score()

        # 判断游戏是否结束
        if self.status.is_win:
            self.background.draw_win()
        if self.status.is_over:
            self.background.draw_over()

        pygame.display.flip()


if __name__ == '__main__':
    ai = Game2048()
    ai.run_game()
