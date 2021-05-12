import pygame.font        #该模块能让Pygame将文本渲染到屏幕上

class Botton:
    def __init__(self,ai_game,msg):      #msg是要在按钮中显示的文本
        '''初始化按钮属性'''
        self.screen = ai_game.screen
        self.screen.rect = self.screen.get_rect()

        #设置按钮尺寸和其他属性
        self.width,self.height = 200,50
        self.botton_color = (0,255,0)     #亮绿色
        self.text_color = (255,255,255)   #白色
        self.font = pygame.font.SysFont(None,48)          #使用什么字体来渲染文本，  none使用默认字体，  48是字号

        #创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)  #创建一个表示按钮的ract对象
        self.screen.center = self.screen_rect.center

        #按钮的标签只需创建一次
        self._prep_msg(msg)


    def _prep_msg(self,msg):
        '''将msg渲染为图像，并使其在按钮上居中'''
        # font.render将存储在msg中的文本转换为图像   True开启反锯齿
        self.msg_image = self.font.render(msg,True,self.text_color,self.botton_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_botton(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.botton_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)