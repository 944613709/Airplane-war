import pygame
from pygame.locals import *


"""加载图片"""
app_icon=pygame.image.load('res/app.ico')  #飞机logo的图片



#pygame工具先初始化（检查）
pygame.init()
#创建窗口
window=pygame.display.set_mode((512,768))
#设置标题
pygame.display.set_caption('小陈的飞机大战')
#设置logo
pygame.display.set_icon(app_icon)


#  处理事件的方法
def handleEvent():
    #获取所有的事件
    list_event=pygame.event.get()
    for event in list_event:
        #判断如果当前这个事件列表中type为退出事件  QUIT=X
        if event.type==QUIT:
            #关闭pygame窗口
            pygame.quit()
            #关闭程序
            exit()



while True:
    #不断刷新界面
    pygame.display.update()
    handleEvent()

