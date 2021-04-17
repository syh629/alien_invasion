# 姓名 ： 孙炎昊
# 时间 ：  15:27
import sys

import pygame

class AlienInvasion:
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏并且创建游戏资源'''
        pygame.init()   #initialize all imported pygame modules

        self.screen = pygame.display.set_mode((1200,800))   #创建游戏窗口
        pygame.display.set_caption('Alien Invasion')   #设置游戏标题
        self.bg_color = (230,230,230)  #设置背景色   RGB

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            #监视键盘和鼠标事件
            for event in pygame.event.get():    #pygame.event.get 返回一个列表，包含上次被调用后发生的所有事件
                if event.type == pygame.QUIT:
                    sys.exit()

            #每次循环时都重绘屏幕
            self.screen.fill(self.bg_color)

            #让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == '__main__':      #在自己的文件里__name__ == '__main__' 如果import别的module里就不等于，不会运行
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()

    fdsfsdf