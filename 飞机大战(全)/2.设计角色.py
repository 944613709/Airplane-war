import pygame
from pygame.locals import *
import random
import time
"""加载图片"""
app_icon=pygame.image.load('res/app.ico')  #飞机logo的图片
bg=pygame.image.load('res/img_bg_level_4.jpg')
hero_img=pygame.image.load('res/hero2.png')
logo_1=pygame.image.load('img/LOGO.png')
#      等比例缩放图片           原图     新的大小
logo1=pygame.transform.scale(logo_1,(460,143))
sg=pygame.image.load('img/startGame.png')   #开始游戏的图
pau=pygame.image.load('img/game_pause_nor.png')  #暂停状态的图
b8=pygame.image.load('res/bullet_8.png')  #子弹的图
e1=pygame.image.load('res/img-plane_5.png')
e2=pygame.image.load('res/img-plane_4.png')
e3=pygame.image.load('res/img-plane_7.png')
over=pygame.image.load('img/over.png')
#等比例缩放gameover图片
over1=pygame.transform.scale(over,(460,143))

#pygame工具先初始化（检查）
pygame.init()
#创建窗口
window=pygame.display.set_mode((512,768))
#设置标题
pygame.display.set_caption('小陈的飞机大战')
#设置logo
pygame.display.set_icon(app_icon)

#生成空列表，装子弹对象
bullets=[]
#生成空列表，装敌飞机对象
enemies=[]

#  处理事件的方法
def handleEvent():
    global state
    #获取所有的事件
    list_event=pygame.event.get()
    for event in list_event:
        #判断如果当前这个事件列表中type为退出事件  QUIT=X
        if event.type==QUIT:
            #关闭pygame窗口
            pygame.quit()
            #关闭程序
            exit()
        #如果事件的类型是鼠标移动事件
        if event.type==MOUSEMOTION:
            if state==states['running']:
                #把鼠标的x坐标给玩家的x坐标
                player.x=event.pos[0]-player.width/2
                # 把鼠标的y坐标给玩家的y坐标
                player.y=event.pos[1]-player.height/2
                #如果鼠标移出界面，则把状态切换至 pause状态
                if MouseOut(event.pos[0],event.pos[1]):
                    state=states['pause']
            elif state==states['pause']:
                if MouseOver(event.pos[0],event.pos[1]):
                    state=states['running']


        if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    #如果鼠标点左键且现在是在ready状态下，如果鼠标点的是以下这个范围，则切换到running状态
                    if state==states['ready']:
                        if 143<=event.pos[0]<=369 and 470<=event.pos[1]<=530:
                            state=states['running']
                            print(state)
                    elif state==states['running']:
                        player.shoot()



#写文字的方法  写什么  大小  写到哪
def fillText(text,size,position):
    #先设置字体的样式及大小
    # TextFont=pygame.font.SysFont('微软雅黑',size)
    TextFont = pygame.font.Font('res/font1.ttf',size)
    # 对设置好的字体样式进行渲染
    #               内容  抗锯齿   颜色
    TF=TextFont.render(text,True,(255,255,255))
    #最后传输到窗口上
    window.blit(TF,position)

#时间间隔方法
lastTime=0  #游戏刚开始时，是0
interval=1 #时间间隔
def isAction(lastTime,interval):
    if lastTime==0:
        return True
    # 记录实时时间
    currentTime=time.time()
    #   如果当前时间-上一次发车时间超过时间间隔，则达到发车条件
    return currentTime-lastTime>=interval

#敌飞机的生成方法
def componentBirth():
    global lastTime
    if isAction(lastTime,interval):
        lastTime=time.time()
        #用随机数控制敌飞机生成的概率
        n=random.randint(1,10)
        #这三个代表随机x坐标
        x1=random.randint(0,412)
        x2=random.randint(0,412)
        x3=random.randint(0,412)
        #不同随机数生成不同类型的飞机
        if n<=6:
            enemies.append(Enemy(100,68,x1,-68,e1,1,1))
        elif 7<=n<=9:
            enemies.append(Enemy(100, 68, x2, -68, e2,3,10))
        else:
            enemies.append(Enemy(100, 68, x3, -68, e3,5,20))



#让组件显示的方法
def componentPaint():
    for bullet in bullets:
        bullet.paint()
    for enemy in enemies:
        enemy.paint()


#让组件移动的方法
def componentStep():
    for bullet in bullets:
        bullet.step()
    for enemy in enemies:
        enemy.move()



"""
背景类
玩家类
敌飞机类
子弹类
"""
class Background():
    #设计属性  游戏五要素
    def __init__(self,width,height,x,y,img):
        #宽
        self.width=width
        #高
        self.height=height
        #x坐标
        self.x=x
        #y坐标
        self.y=y
        #图片
        self.img=img

        #第二张背景
        self.x2=0
        self.y2=-768
    #设计功能--显示功能
    def paint(self):
        #窗口使用传输方法  传谁   传到哪个位置
        window.blit(self.img,(self.x,self.y))
        #显示第二张背景
        window.blit(self.img,(self.x2,self.y2))
    #移动功能
    def move(self):
        self.y+=1
        self.y2+=1
        if self.y>=768:
            self.y=-768
        if self.y2>=768:
            self.y2=-768

#玩家类
class Player():
    # 设计属性  游戏五要素
    def __init__(self, width, height, x, y, img,life):
        # 宽
        self.width = width
        # 高
        self.height = height
        # x坐标
        self.x = x
        # y坐标
        self.y = y
        # 图片
        self.img = img
        #玩家飞机的生命
        self.life = life
        # 设计功能--显示功能
    def paint(self):
        # 窗口使用传输方法  传谁   传到哪个位置
        window.blit(self.img, (self.x, self.y))
    def shoot(self):
        #生成子弹对象
        bullets.append(Bullet(20,56,self.x+self.width/2-10,self.y-20-56,b8))

#创建子弹类
class Bullet():
    # 设计属性  游戏五要素
    def __init__(self, width, height, x, y, img):
        # 宽
        self.width = width
        # 高
        self.height = height
        # x坐标
        self.x = x
        # y坐标
        self.y = y
        # 图片
        self.img = img
    def paint(self):
        # 窗口使用传输方法  传谁   传到哪个位置
        window.blit(self.img, (self.x, self.y))
    def step(self):
        self.y-=2
        #如果子弹碰到上边界，删除当前子弹对象
        if self.y<=0:
            bullets.remove(self)
#创建敌飞机类
class Enemy():
    # 设计属性  游戏五要素
    def __init__(self, width, height, x, y, img,life,score):
        # 宽
        self.width = width
        # 高
        self.height = height
        # x坐标
        self.x = x
        # y坐标
        self.y = y
        # 图片
        self.img = img
        #敌机的生命值
        self.life=life
        #敌机的分数
        self.score=score

    def paint(self):
        # 窗口使用传输方法  传谁   传到哪个位置
        window.blit(self.img, (self.x, self.y))
    def move(self):
        self.y+=2
    #定义碰撞功能
    def hit(self,w):
        #         敌机在左                   敌机在右
        return self.x+self.width>=w.x and w.x+w.width>=self.x and \
            self.y+self.height>=w.y and w.y+w.height>=self.y   #敌机在上  敌机在下


#根据背景类创建对象
background=Background(512,768,0,0,bg)

#根据玩家类创建玩家
player=Player(120,78,196,640,hero_img,10)

#游戏中的初始分数为0
score=0
#设置游戏的三种状态
states={'ready':0,'running':1,'pause':2,'over':3,'leaderboard': 4, 'settings': 5, 'quit': 6}
#游戏的初始状态 是 'ready':0
state=states['ready']

#鼠标移出
def MouseOut(x,y):
    if x<=0 or x>=507 or y<=0 or y>=763:
        return True
    else:
        return False
#鼠标移入
def MouseOver(x,y):
    if x>=0 and x<=512 and y>=0 and y<=768:
        return True
    else:
        return False

#专门定义一个方法来检测碰撞
def checkHit():
    global state,score
    #敌机和玩家碰撞
    for enemy in enemies:
        if enemy.hit(player):
            score+=enemy.score
            enemies.remove(enemy)
            player.life-=1
            if player.life<=0:
                state=states['over']
        #取得每一颗子弹
        for bullet in bullets:
            #如果敌机和子弹碰撞到了
            if enemy.hit(bullet):
                bullets.remove(bullet)
                #那么敌机的生命值-1
                enemy.life-=1
                #如果敌机的生命值<=0了，
                if enemy.life<=0:
                    score+=enemy.score
                    #那么敌机删除
                    enemies.remove(enemy)



#  创建 控制状态方法，专门在这里设计各个状态要做的事
def controlState():
    if state==states['ready']:
        # 背景调用显示功能
        background.paint()
        background.move()
        window.blit(logo1,(26,313))
        window.blit(sg,(143,470))
    elif state==states['running']:
        # 背景调用显示功能
        background.paint()
        background.move()
        # 玩家调用显示功能
        player.paint()
        #调用敌飞机生成方法
        componentBirth()
        #调用组件显示的方法
        componentPaint()
        #调用组件移动的方法
        componentStep()
        #调用碰撞检测方法
        checkHit()
        fillText('LIFE:' + str(player.life), 30, (10, 0))
        fillText('SCORE:' + str(score), 30, (10, 30))
    elif state==states['pause']:
        # 背景调用显示功能
        background.paint()
        background.move()
        # 调用敌飞机生成方法
        componentBirth()
        # 调用组件显示的方法
        componentPaint()
        # 玩家调用显示功能
        player.paint()
        fillText('LIFE:' + str(player.life), 30, (10, 0))
        fillText('SCORE:' + str(score), 30, (10, 30))
        window.blit(pau,(191,319))
    elif state==states['over']:
        # 背景调用显示功能
        background.paint()
        background.move()
        window.blit(over1,(26,313))
    elif state == states['leaderboard']:
        # 显示排行榜界面
        background.paint()
        fillText('Leaderboard', 50, (180, 50))
        # 在这里可以读取并显示排行榜数据
    elif state == states['settings']:
        # 显示设置界面
        background.paint()
        fillText('Settings', 50, (200, 50))
        # 在这里可以添加设置选项
    elif state == states['quit']:
        # 退出
        pygame.quit()


while True:
    controlState()

    #延迟10毫秒
    pygame.time.delay(10)
    #不断刷新界面
    pygame.display.update()
    handleEvent()

