# 姓名 ： 孙炎昊
# 时间 ：  15:27
import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏并且创建游戏资源'''
        pygame.init()   #initialize all imported pygame modules
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))   #创建游戏窗口
        pygame.display.set_caption('Alien Invasion')   #设置游戏标题

        self.ship = Ship(self)  #因为Ship还有个参数ai_game 这里把AlienInvasion实例赋给ai_game

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        '''相应按键和鼠标事件'''
        for event in pygame.event.get():    #pygame.event.get 返回一个列表，包含上次被调用后发生的所有事件
             if event.type == pygame.QUIT:
                sys.exit()
             elif event.type == pygame.KEYDOWN:  #KEYDOWN是按键事件
                 if event.type == pygame.K_RIGHT:
                     self.ship.moving_right = True
                 elif event.type == pygame.KEYUP:
                     if event.type == pygame.K_RIGHT:
                         self.ship.moving_right = False



    def _update_screen(self):
        '''更新屏幕上的图像，并切换到新屏幕'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':      #在自己的文件里__name__ == '__main__' 如果import别的module里就不等于，不会运行
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()

