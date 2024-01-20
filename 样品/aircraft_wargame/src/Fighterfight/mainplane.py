# -*- coding: utf-8 -*
import pygame

#新类plane表示玩家控制机，继承自sprite类，用于碰撞检测
class MyPlane(pygame.sprite.Sprite):
    def __init__(plane,bg_size):
        #初始化
        pygame.sprite.Sprite.__init__(plane)

        #加载图片
        plane.image = pygame.image.load("images/me1.png").convert_alpha()
        plane.destroy = [pygame.image.load("images/me_destroy_1.png").convert_alpha(),\
                         pygame.image.load("images/me_destroy_2.png").convert_alpha(),\
                         pygame.image.load("images/me_destroy_3.png").convert_alpha(),\
                         pygame.image.load("images/me_destroy_4.png").convert_alpha()]
        #获取图片所在矩形位置信息
        plane.rect = plane.image.get_rect()

        plane.width,plane.height = bg_size[0],bg_size[1]
        #设置我机所在的初始位置（固定左上角）
        plane.rect.left,plane.rect.top = (plane.width-plane.rect.width)//2,\
                                          plane.height-plane.rect.height-60
        #设置飞机移动速度,即每次移动的像素
        plane.speed = 8

        #默认设置飞机状态为true
        plane.active = True

        #获取飞机的mask值
        plane.mask = pygame.mask.from_surface(plane.image)

    #定义飞机移动的四个方向
    def MOVEUP(plane):
        if plane.rect.top > 0:
            plane.rect.top -= plane.speed
        else:
            plane.rect.top = 0

    def MOVEDOWN(plane):
        if plane.rect.bottom < plane.height-60:
            plane.rect.top += plane.speed
        else:
            plane.rect.bottom = plane.height-60

    def MOVELEFT(plane):
        if plane.rect.left > 0:
            plane.rect.left -= plane.speed
        else:
            plane.rect.left = 0

    def MOVERIGHT(plane):
        if plane.rect.right < plane.width:
            plane.rect.left += plane.speed
        else:
            plane.rect.right = plane.width

    def reset(plane):
         plane.rect.left,plane.rect.top = (plane.width-plane.rect.width)//2,\
                                          plane.height-plane.rect.height-60
         plane.active = True
