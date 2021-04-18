# 姓名 ： 孙炎昊
# 时间 ：  15:27
import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏并且创建游戏资源'''
        pygame.init()   #initialize all imported pygame modules
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)  #全屏
        self.settings.screen_width = self.screen.get_rect().width    #预先无法知道屏幕尺寸，所以创建全屏后更新settings
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')   #设置游戏标题

        self.ship = Ship(self)  #因为Ship还有个参数ai_game 这里把AlienInvasion实例赋给ai_game
        self.bullet = pygame.sprite.Group()

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            self._check_events()
            self.ship.update()
            self.bullet.update()
            self._update_screen()

    def _check_events(self):
        '''相应按键和鼠标事件'''
        for event in pygame.event.get():    #pygame.event.get 返回一个列表，包含上次被调用后发生的所有事件
             if event.type == pygame.QUIT:
                sys.exit()
             elif event.type == pygame.KEYDOWN:  #KEYDOWN是按键事件
                 self._check_keydown_events(event)
             elif event.type == pygame.KEYUP:
                 self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        '''相应按键'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        '''响应松开'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''创建一颗子弹，并将其加入编组bullets中'''
        new_bullet = Bullet(self)
        self.bullet.add(new_bullet)

    def _update_screen(self):
        '''更新屏幕上的图像，并切换到新屏幕'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullet.sprites():        #bullet.sprites()返回一个列表，包含编组bullets中所有的精灵
            bullet.draw_bullet()

        #让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':      #在自己的文件里__name__ == '__main__' 如果import别的module里就不等于，不会运行
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()

