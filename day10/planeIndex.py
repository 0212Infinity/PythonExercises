import pygame
import random
from pygame.locals import *


class MePlane:
    def __init__(self, screen):
        self.screen = screen
        # 初始化玩家的位置
        self.x = 200
        self.y = 600
        # 载入玩家的飞机图片
        self.me = pygame.image.load("./material/me1.png")
        # 用来存放子弹列表
        self.bulletList = []
        pass

    def moveLeft(self):
        if self.x > 0:
            self.x -= 10
        pass

    def moveRight(self):
        if self.x < 378:
            self.x += 10
        pass

    def display(self):
        self.screen.blit(self.me, (self.x, self.y))
        # 处理越界子弹
        needDelList = []
        for item in self.bulletList:
            if item.juge():
                needDelList.append(item)
        for i in needDelList:
            self.bulletList.remove(i)
        # 重新展示子弹
        for item in self.bulletList:
            item.display()
            item.move()
        pass

    # 发射子弹
    def shootBullet(self):
        newBullet = Bullet(self.x, self.y, self.screen)
        self.bulletList.append(newBullet)
        pass

    pass


def keyControl(meObj):
    # 获取键盘事件
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print("退出")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                meObj.moveLeft()
            elif event.key == K_d or event.key == K_RIGHT:
                meObj.moveRight()
            elif event.key == K_SPACE:
                meObj.shootBullet()
    pass


class Bullet(object):
    def __init__(self, x, y, screen):
        self.x = x + 50
        self.y = y - 20
        self.screen = screen
        self.bullet = pygame.image.load("./material/bullet2.png")
        pass

    def display(self):
        self.screen.blit(self.bullet, (self.x, self.y))
        pass

    def move(self):
        self.y -= 1
        pass

    # 是否越界
    def juge(self):
        return self.y < 0
        pass

    pass


class EnemyPlane:
    def __init__(self, screen):
        # 默认方向
        self.direction = 'left'
        self.screen = screen
        # 初始化玩家的位置
        self.x = 0
        self.y = 0
        # 载入飞机图片
        self.enemy = pygame.image.load("./material/enemy2.png")
        # 用来存放子弹列表
        self.bulletList = []
        pass

    def display(self):
        self.screen.blit(self.enemy, (self.x, self.y))
        # 处理越界子弹
        needDelList = []
        for item in self.bulletList:
            if item.juge():
                needDelList.append(item)
        for i in needDelList:
            self.bulletList.remove(i)
        # 重新展示子弹
        for item in self.bulletList:
            item.display()
            item.move()
        pass
        pass

    # 随机发射子弹
    def shootBullet(self):
        num = random.randint(1, 20)
        if num == 3:
            newBullet = EnemyBullet(self.x, self.y, self.screen)
            self.bulletList.append(newBullet)
        pass

    def move(self):
        if self.direction == 'right':
            self.x += 10
        elif self.direction == 'left':
            self.x -= 10
        if self.x > 378:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'
        pass

    pass


class EnemyBullet(object):
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y + 10
        self.screen = screen
        self.bullet = pygame.image.load("./material/bullet1.png")
        pass

    def display(self):
        self.screen.blit(self.bullet, (self.x, self.y))
        pass

    def move(self):
        self.y += 1
        pass

    # 是否越界
    def juge(self):
        return self.y > 700
        pass

    pass


def main():
    screen = pygame.display.set_mode((480, 700))
    background = pygame.image.load("./material/background.png")
    # 设置标题
    pygame.display.set_caption("飞机大战")
    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load("./material/wind1.wav")
    pygame.mixer.music.set_volume((0.5))  # 音量
    pygame.mixer.music.play(-1)  # 循环播放

    me = MePlane(screen)
    enemy = EnemyPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        me.display()
        enemy.display()
        enemy.move()
        enemy.shootBullet()
        keyControl(me)
        # 更新显示内容
        pygame.display.update()
        pygame.time.Clock().tick(80)
    pass


main()
