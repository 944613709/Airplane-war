# -*- coding: utf-8 -*
import pygame
from random import *

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(small,bg_size):
        pygame.sprite.Sprite.__init__(small)

        #加载图片
        small.image = pygame.image.load("images/enemy1.png").convert_alpha()
        small.destroy = [pygame.image.load("images/enemy1_down1.png").convert_alpha(),\
                         pygame.image.load("images/enemy1_down2.png").convert_alpha(),\
                         pygame.image.load("images/enemy1_down3.png").convert_alpha(),\
                         pygame.image.load("images/enemy1_down4.png").convert_alpha()]
        #获取图片所在矩形位置信息
        small.rect = small.image.get_rect()

        small.width,small.height = bg_size[0],bg_size[1]

        #定义一个active属性
        small.active = True

        small.speed = 2

        small.rect.left,small.rect.top = randint(0,small.width-small.rect.width),\
                                         randint(-5*small.height,0)

        #获取mask值
        small.mask = pygame.mask.from_surface(small.image)

    #定义敌机的移动方式
    def move(small):
        if small.rect.top < small.height:
            small.rect.top += small.speed
        else:
           small.reset()
            
    def reset(small):
        small.active = True
        small.rect.left,small.rect.top = randint(0,small.width-small.rect.width),\
                                         randint(-10*small.height,-small.height)

class MidEnemy(pygame.sprite.Sprite):
    energy = 8
    def __init__(small,bg_size):
        pygame.sprite.Sprite.__init__(small)

        #加载图片
        small.image = pygame.image.load("images/enemy2.png").convert_alpha()
        small.destroy = [pygame.image.load("images/enemy2_down1.png").convert_alpha(),\
                         pygame.image.load("images/enemy2_down2.png").convert_alpha(),\
                         pygame.image.load("images/enemy2_down3.png").convert_alpha(),\
                         pygame.image.load("images/enemy2_down4.png").convert_alpha()]
        #获取图片所在矩形位置信息
        small.rect = small.image.get_rect()

        small.width,small.height = bg_size[0],bg_size[1]

        small.active = True

        small.speed = 1

        small.rect.left,small.rect.top = randint(0,small.width-small.rect.width),\
                                         randint(-10*small.height,-small.height)

        small.mask = pygame.mask.from_surface(small.image)

        small.energy = MidEnemy.energy

    #定义敌机的移动方式
    def move(small):
        if small.rect.top < small.height:
            small.rect.top += small.speed
        else:
            small.reset()
            
    def reset(small):
        small.active = True
        small.energy = MidEnemy.energy
        small.rect.left,small.rect.top = randint(0,small.width-small.rect.width),\
                                         randint(-10*small.height,-small.height)


class BigEnemy(pygame.sprite.Sprite):
    energy = 16
    def __init__(big,bg_size):
        pygame.sprite.Sprite.__init__(big)

        #加载图片
        big.image = pygame.image.load("images/enemy3_n1.png").convert_alpha()
        big.destroy = [pygame.image.load("images/enemy3_down2.png").convert_alpha(),\
                       pygame.image.load("images/enemy3_down3.png").convert_alpha(),\
                       pygame.image.load("images/enemy3_down4.png").convert_alpha(),\
                       pygame.image.load("images/enemy3_down6.png").convert_alpha()]
        #获取图片所在矩形位置信息
        big.rect = big.image.get_rect()

        big.width,big.height = bg_size[0],bg_size[1]

        big.active = True

        big.speed = 1

        big.rect.left,big.rect.top = randint(0,big.width-big.rect.width),\
                                     randint(-10*big.height,-5*big.height)

        big.mask = pygame.mask.from_surface(big.image)

        big.energy = BigEnemy.energy

    #定义敌机的移动方式
    def move(big):
        if big.rect.top < big.height:
            big.rect.top += big.speed
        else:
            big.reset()
            
    def reset(big):
        big.active = True
        big.energy = BigEnemy.energy
        big.rect.left,big.rect.top = randint(0,big.width-big.rect.width),\
                                     randint(-10*big.height,-5*big.height)



