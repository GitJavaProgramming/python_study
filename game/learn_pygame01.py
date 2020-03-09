# _*_ coding: utf-8 _*_

from sys import exit

import pygame

background_image_filename = '葫芦娃.jpg'
mouse_image_filename = 'jmeter.ico'

# 初始化pygame，为使用硬件做准备
pygame.init()

# 创建一个窗口
screen = pygame.display.set_mode((640, 480), 0, 32)

# 设置窗口标题
pygame.display.set_caption("hello,world!")

# 加载图片并转换
background = pygame.image.load(background_image_filename)
mouse_cursor = pygame.image.load(mouse_image_filename)

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 接收到退出时间后退出程序
            exit()

    # 将背景图画上去
    screen.blit(background, (0, 0))

    # 获得鼠标位置
    x, y = pygame.mouse.get_pos()
    # 计算光标左上角位置
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2

    # 将光标画上去
    screen.blit(mouse_cursor, (x, y))

    # 刷新画面
    pygame.display.update()
