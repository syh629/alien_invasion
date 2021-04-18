# 姓名 ： 孙炎昊
# 时间 ：  10:11
import pygame

class Ship:
    '''管理飞船的类'''

    def __init__(self,ai_game):
        '''初始化飞船并设置其初始位置'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #对于每艘新飞船，都将其放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        #在飞船的属性x中存储小数值
        self.x = float(self.rect.x)    #因为 self.rect.x 只能存储整数值

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据移动标志调整飞船位置'''
        #更新飞船而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:       #如果使用elif代码，则向右会有优先地位，如果同时按住左右，会向右
            self.x -= self.settings.ship_speed

        #根据self.x更新rect对象
        self.rect.x = self.x

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)

