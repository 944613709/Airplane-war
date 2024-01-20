# -*- coding: utf-8 -*
import pygame
import sys
import traceback
import mainplane
import enemy
import bullet
from pygame.locals import *
from random import *

# 定义游戏状态
MENU = 0
INITGAME = 1
GAME_OVER = 2
PLAYING = 3
current_state = MENU  # 初始状态为主菜单
#初始化游戏
pygame.init()
#初始化混音器
pygame.mixer.init()

#载入游戏音乐
pygame.mixer.music.load("sound/game_music.ogg")
pygame.mixer.music.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.5)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.3)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.5)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.8)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.8)

bg_size=width,height=480,700
#创建窗口
screen=pygame.display.set_mode(bg_size)
#设置窗口标题
pygame.display.set_caption("Fighterfight")

#把图片载入background变量
background=pygame.image.load("images/background.png").convert()


#往机组中添加飞机的add函数实现
def add_small_enemies(group1,group2,num):
    for i in range(num):
        e = enemy.SmallEnemy(bg_size)
        group1.add(e)
        group2.add(e)

def add_mid_enemies(group1,group2,num):
    for i in range(num):
        e = enemy.MidEnemy(bg_size)
        group1.add(e)
        group2.add(e)

def add_big_enemies(group1,group2,num):
    for i in range(num):
        e = enemy.BigEnemy(bg_size)
        group1.add(e)
        group2.add(e)

def increase_speed(target,n):
    for each in target:
        each.speed += n
# 创建字体
menu_font = pygame.font.Font(None, 48)
font = pygame.font.Font(None, 36)

def render_menu(screen):
    '''
    重新渲染主菜单
    :param screen:
    :return:
    '''
    # 清空屏幕并重新绘制背景
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    start_text = menu_font.render("Start Game", True, (255, 255, 255))
    start_rect = start_text.get_rect()
    start_rect.centerx = screen.get_rect().centerx
    start_rect.centery = screen.get_rect().centery - 50

    leaderboard_text = menu_font.render("Leaderboard", True, (255, 255, 255))
    leaderboard_rect = leaderboard_text.get_rect()
    leaderboard_rect.centerx = screen.get_rect().centerx
    leaderboard_rect.centery = screen.get_rect().centery

    settings_text = menu_font.render("Settings", True, (255, 255, 255))
    settings_rect = settings_text.get_rect()
    settings_rect.centerx = screen.get_rect().centerx
    settings_rect.centery = screen.get_rect().centery + 50

    quit_text = menu_font.render("Quit Game", True, (255, 255, 255))
    quit_rect = quit_text.get_rect()
    quit_rect.centerx = screen.get_rect().centerx
    quit_rect.centery = screen.get_rect().centery + 100

    screen.blit(start_text, start_rect)
    screen.blit(leaderboard_text, leaderboard_rect)
    screen.blit(settings_text, settings_rect)
    screen.blit(quit_text, quit_rect)

    pygame.display.flip()
    return start_rect, quit_rect, leaderboard_rect, settings_rect
initial_difficulty = 1  # 初始难度
initial_life = 3  # 初始生命值
def show_menu(screen):

    while True:
        start_rect, quit_rect, leaderboard_rect, settings_rect = render_menu(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_rect.collidepoint(mouse_pos):
                    return INITGAME
                elif leaderboard_rect.collidepoint(mouse_pos):
                    show_leaderboard()
                elif settings_rect.collidepoint(mouse_pos):
                    # 进入设置界面，允许玩家设置初始难度和生命值
                    show_settings(screen)
                elif quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.flip()
def show_settings(screen):
    '''
    显示设置界面
    :param screen:
    :return:
    '''
    global initial_difficulty, initial_life
    setting_font = pygame.font.Font(None, 36)
    setting_text = font.render("Use UP/DOWN keys to adjust settings:", True, (255, 255, 255))
    difficulty_text = setting_font.render(f"Initial Difficulty: {initial_difficulty}", True, (255, 255, 255))
    life_text = setting_font.render(f"Initial Life: {initial_life}", True, (255, 255, 255))
    back_text = setting_font.render("Back to Menu", True, (255, 255, 255))

    # 设置文本的位置
    setting_rect = setting_text.get_rect()
    difficulty_rect = difficulty_text.get_rect()
    life_rect = life_text.get_rect()
    back_rect = back_text.get_rect()

    setting_rect.centerx = screen.get_rect().centerx
    setting_rect.centery = screen.get_rect().centery - 100
    difficulty_rect.centerx = screen.get_rect().centerx
    difficulty_rect.centery = screen.get_rect().centery - 50
    life_rect.centerx = screen.get_rect().centerx
    life_rect.centery = screen.get_rect().centery
    back_rect.centerx = screen.get_rect().centerx
    back_rect.centery = screen.get_rect().centery + 50



    while True:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        # 在屏幕上绘制文本
        screen.blit(setting_text, setting_rect)
        screen.blit(difficulty_text, difficulty_rect)
        screen.blit(life_text, life_rect)
        screen.blit(back_text, back_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_rect.collidepoint(mouse_pos):
                    return initial_difficulty, initial_life

        keys = pygame.key.get_pressed()
        # 如果按下 UP 键并且之前没有按下，则增加难度
        if keys[K_UP] and not key_pressed:
            initial_difficulty = min(5, initial_difficulty + 1)  # 最大难度为5
            key_pressed = True

        # 如果按下 DOWN 键并且之前没有按下，则减小难度
        elif keys[K_DOWN] and not key_pressed:
            initial_difficulty = max(1, initial_difficulty - 1)  # 最小难度为1
            key_pressed = True

        # 如果按下 LEFT 键并且之前没有按下，则减小生命值
        elif keys[K_LEFT] and not key_pressed:
            initial_life = max(1, initial_life - 1)  # 最小生命值为1
            key_pressed = True

        # 如果按下 RIGHT 键并且之前没有按下，则增加生命值
        elif keys[K_RIGHT] and not key_pressed:
            initial_life = min(5, initial_life + 1)  # 最大生命值为5
            key_pressed = True

        # 如果没有按下任何键，则将按键状态重置为 False
        elif not any(keys):
            key_pressed = False

        difficulty_text = setting_font.render(f"Initial Difficulty: {initial_difficulty}", True, (255, 255, 255))
        life_text = setting_font.render(f"Initial Life: {initial_life}", True, (255, 255, 255))
# 创建一个函数来显示排行榜
def show_leaderboard():
    global current_state

    # 读取分数记录文件
    scores = []
    with open("scores.txt", "r") as file:
        for line in file:
            scores.append(int(line))

    # 对分数进行排序
    scores.sort(reverse=True)

    # 只显示前3名玩家的最高分
    top_scores = scores[:3]

    screen.fill((0, 0, 0))  # 清空屏幕
    leaderboard_font = pygame.font.Font(None, 36)
    y = 100  # 垂直位置，用于显示排行榜
    back_text = leaderboard_font.render("Back to Menu", True, (255, 255, 255))
    back_rect = back_text.get_rect()
    back_rect.centerx = screen.get_rect().centerx
    back_rect.centery = screen.get_rect().centery + 200
    screen.blit(back_text, back_rect)
    # 显示前3名玩家的最高分
    for i, score in enumerate(top_scores):
        text = leaderboard_font.render(f"Player {i+1}: {score}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(width // 2, y))
        screen.blit(text, text_rect)
        y += 50

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_rect.collidepoint(mouse_pos):
                    current_state = MENU  # 返回到主菜单
                    return
#进入主函数
def main():
    #循环播放背景音乐
    global current_state
    pygame.mixer.music.play(-1)
    # 用于延迟
    delay = 100
    # 引入帧率
    clock = pygame.time.Clock()

    #游戏结束画面
    gameover_font = pygame.font.Font("font/font.TTF", 48)
    again_image = pygame.image.load("images/again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("images/gameover.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()


    
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        if current_state == MENU:
            # 显示主菜单，等待用户选择
            current_state = show_menu(screen)
        elif current_state == INITGAME:
            # 初始化

            # 设置分数变量
            score = 0
            global initial_difficulty, initial_life
            # 设置生命数
            life_num = initial_life
            life_image = pygame.image.load("images/life.png").convert_alpha()
            life_rect = life_image.get_rect()
            difficulty_levels = {
                1: {"small_enemy_count": 15, "mid_enemy_count": 5, "big_enemy_count": 2,
                    "small_enemy_speed": 1, "mid_enemy_speed": 1, "big_enemy_speed": 1},
                2: {"small_enemy_count": 15, "mid_enemy_count": 5, "big_enemy_count": 3,
                    "small_enemy_speed": 1, "mid_enemy_speed": 1, "big_enemy_speed": 1},
                3: {"small_enemy_count": 20, "mid_enemy_count": 12, "big_enemy_count": 4,
                    "small_enemy_speed": 3, "mid_enemy_speed": 3, "big_enemy_speed": 3},
                4: {"small_enemy_count": 15, "mid_enemy_count": 15, "big_enemy_count": 5,
                    "small_enemy_speed": 4, "mid_enemy_speed": 4, "big_enemy_speed": 4},
                5: {"small_enemy_count": 20, "mid_enemy_count": 18, "big_enemy_count": 6,
                    "small_enemy_speed": 5, "mid_enemy_speed": 5, "big_enemy_speed": 5}
            }
            current_difficulty = initial_difficulty
            if current_difficulty in difficulty_levels:
                difficulty_params = difficulty_levels[current_difficulty]
            else:
                # 如果当前难度不在字典中，使用默认参数
                difficulty_params = difficulty_levels[1]

            # 设置字体，实例化font模块的Font类
            score_font = pygame.font.Font("font/font.ttf", 38)

            # 设置难度级别
            level = 1

            # 生成我方飞机
            myplane = mainplane.MyPlane(bg_size)

            # 生成普通子弹
            bullet1 = []
            BULLET1_NUM = 4
            for i in range(BULLET1_NUM):
                bullet1.append(bullet.Bullet(myplane.rect.midtop))
            # 设置一个子弹的索引指针，在bullet列表中循环指向
            bullet1_index = 0

            # 创建敌机组，包含三类敌机，方便进行碰撞检测
            enemies = pygame.sprite.Group()

            # 生成小型敌机
            small_enemies = pygame.sprite.Group()
            # 编写添加小敌机的函数，放入两个组，每次添加15个
            add_small_enemies(small_enemies, enemies, difficulty_params["small_enemy_count"])

            # 生成中型敌机
            mid_enemies = pygame.sprite.Group()
            # 编写添加中敌机的函数，放入两个组，每次添加8个
            add_mid_enemies(enemies, mid_enemies, difficulty_params['mid_enemy_count'])

            # 生成大型敌机
            big_enemies = pygame.sprite.Group()
            # 编写添加大敌机的函数，放入两个组，每次添加2个
            add_big_enemies(enemies, big_enemies, difficulty_params['big_enemy_count'])
            current_state = PLAYING
        elif current_state == PLAYING:
            
            #增加难度
            if level == 1 and score > 30000:
                level = 2
                upgrade_sound.play()
                #增加3辆小敌机，2架中敌机，1架大敌机
                add_small_enemies(small_enemies,enemies,difficulty_params["small_enemy_count"])
                add_mid_enemies(mid_enemies,enemies,difficulty_params["mid_enemy_count"])
                add_big_enemies(big_enemies,enemies,1)
                #提升小型敌机的速度
                increase_speed(small_enemies,1)

            elif level == 2 and score > 100000:
                level = 3
                upgrade_sound.play()
                #增加5辆小敌机，3架中敌机，2架大敌机
                add_small_enemies(small_enemies,enemies,difficulty_params["small_enemy_count"])
                add_mid_enemies(mid_enemies,enemies,difficulty_params["mid_enemy_count"])
                add_big_enemies(big_enemies,enemies,difficulty_params["big_enemy_count"])
                #提升小和中型敌机的速度
                increase_speed(small_enemies,difficulty_params["small_enemy_speed"])
                increase_speed(mid_enemies,difficulty_params['mid_enemy_speed'])

            elif level == 3 and score > 600000:
                level = 4
                upgrade_sound.play()
                #增加8辆小敌机，5架中敌机，3架大敌机
                add_small_enemies(small_enemies,enemies,difficulty_params["small_enemy_count"])
                add_mid_enemies(mid_enemies,enemies,difficulty_params["mid_enemy_count"])
                add_big_enemies(big_enemies,enemies,difficulty_params["big_enemy_count"])
                #提升小和中型敌机的速度
                increase_speed(small_enemies,difficulty_params["small_enemy_speed"])
                increase_speed(mid_enemies,difficulty_params['mid_enemy_speed'])

            elif level == 4 and score > 1000000:
                level = 5
                upgrade_sound.play()
                #增加10辆小敌机，8架中敌机，5架大敌机
                add_small_enemies(small_enemies,enemies,difficulty_params["small_enemy_count"])
                add_mid_enemies(mid_enemies,enemies,difficulty_params["mid_enemy_count"])
                add_big_enemies(big_enemies,enemies,difficulty_params["big_enemy_count"])
                #提升小，中和大型敌机的速度
                increase_speed(small_enemies,difficulty_params["small_enemy_speed"])
                increase_speed(mid_enemies,difficulty_params['mid_enemy_speed'])
                increase_speed(big_enemies,difficulty_params['big_enemy_speed'])

            #如果生命值大于0，游戏继续
            if life_num:
                #导入key_press模块，接受键盘传入的序列数，返回按键的布尔值
                key_pressed = pygame.key.get_pressed()

                if key_pressed[K_UP]:
                   myplane.MOVEUP()
                elif key_pressed[K_DOWN]:
                    myplane.MOVEDOWN()
                elif key_pressed[K_LEFT]:
                    myplane.MOVELEFT()
                elif key_pressed[K_RIGHT]:
                    myplane.MOVERIGHT()


                #拷贝背景图
                screen.blit(background,(0,0))

                #检测我方飞机是否被撞，调用sprite模块里的collide_mask方式进行检测
                enemies_down = pygame.sprite.spritecollide(myplane,enemies,False,pygame.sprite.collide_mask)
                if enemies_down:
                    myplane.active = False
                    for i in enemies_down:
                        i.active = False

                #字符串显示，白色无锯齿
                score_text = score_font.render("Score : %s"%str(score),True,(255,255,255))
                screen.blit(score_text,(10,640))

                #画我方飞机
                if myplane.active:
                    screen.blit(myplane.image,myplane.rect)
                else:
                    #绘制毁灭图像
                    if not (delay%4):
                        for i in range(4):
                            screen.blit(myplane.destroy[i],myplane.rect)
                        me_down_sound.play()
                        life_num -= 1
                        myplane.reset()

                #绘制剩余生命
                if life_num:
                    for i in range(life_num):
                        screen.blit(life_image,\
                                    (width-10-(i+1)*life_rect.width,\
                                     height-10-life_rect.height))

                #每12帧绘制一次子弹的发射
                if not (delay%12):
                    bullet_sound.play()
                    bullet1[bullet1_index].reset(myplane.rect.midtop)
                    bullet1_index = (bullet1_index+1)%BULLET1_NUM

                #检测子弹是否击中敌机
                for b in bullet1:
                    if b.active:
                        b.move()
                        screen.blit(b.image,b.rect)
                        bullet_hit=pygame.sprite.spritecollide(b,enemies,False,pygame.sprite.collide_mask)
                        if bullet_hit:
                            b.active = False
                            for e in bullet_hit:
                                if e in mid_enemies or e in big_enemies:
                                    e.energy -= 1
                                    if e.energy == 0:
                                        e.active = False
                                else:
                                    e.active = False

                #画敌方飞机（按大中小的顺序进行绘制）

                #大型机
                for each in big_enemies:
                    if each.active:
                        each.move()
                        screen.blit(each.image,each.rect)
                    else:
                        #播放毁灭动画
                        if not (delay%4):
                            for i in range(4):
                                screen.blit(each.destroy[i],each.rect)
                                each.reset()
                            enemy3_down_sound.play()
                            score += 8000

                #中型机
                for each in mid_enemies:
                    if each.active:
                        each.move()
                        screen.blit(each.image,each.rect)
                    else:
                        #播放毁灭动画
                        if not (delay%4):
                            for i in range(4):
                                screen.blit(each.destroy[i],each.rect)
                                each.reset()
                            enemy2_down_sound.play()
                            score += 3000

                #小型机
                for each in small_enemies:
                    if each.active:
                        each.move()
                        screen.blit(each.image,each.rect)
                    else:
                        #播放毁灭动画
                        if not (delay%4):
                            for i in range(4):
                                screen.blit(each.destroy[i],each.rect)
                                each.reset()
                            enemy1_down_sound.play()
                            score += 1000

            #如果生命值小于0，游戏结束，返回主菜单
            else:
                #背景音乐关闭
                pygame.mixer.music.stop()

                #展示最终分数
                final_text1 = gameover_font.render("Your Score:"+str(score),True,(255,255,255))
                final_text1_rect = final_text1.get_rect()
                final_text1_rect.left,final_text1_rect.top = (width-final_text1_rect.width)//2,\
                                                             height//3
                screen.blit(final_text1,final_text1_rect)

                #将最终分数保存
                save_score(score)
                # 检测用户的鼠标操作
                # 回到主菜单
                current_state = MENU

        #每过一帧，delay自减,小于0重新定义为100
        delay = delay-1
        if not delay:
            delay=100

        #显示窗口
        pygame.display.flip()
        #帧率为60，表示每秒动作不超过60帧
        clock.tick(60)

# 在游戏结束时，将得分保存到文件中
def save_score(score):
    with open("scores.txt", "a") as file:
        file.write(str(score) + "\n")

if __name__=="__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
    
