# 姓名 ： 孙炎昊
# 时间 ：  15:27
import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _create_fleet(self):
        '''创建外星人群'''
        #创建一个外星人并计算一行可容纳多少个外星人
        #外星人的间距为外星人宽度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - 3 * alien_height - ship_height
        number_rows = available_space_y // (2 * alien_height)

        #创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._creat_alien(alien_number,row_number)

    def _creat_alien(self,alien_number,row_number):
        '''创建一个外星人并将其加入当前行'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien_height * row_number
        self.aliens.add(alien)


    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''更新子弹的位置并删除消失的子弹'''
        #更新子弹的位置
        self.bullets.update()

        #删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_aliens(self):
        '''更新外星人群中所有外星人的位置'''
        self.aliens.update()

    def _update_screen(self):
        '''更新屏幕上的图像，并切换到新屏幕'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():        #bullets.sprites()返回一个列表，包含编组bullets中所有的精灵
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':      #在自己的文件里__name__ == '__main__' 如果import别的module里就不等于，不会运行
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()

