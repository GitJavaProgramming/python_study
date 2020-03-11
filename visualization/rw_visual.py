# 随机生成点
import matplotlib.pyplot as plt

from visualization.random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    # 设置绘图窗口的尺寸 figure指定图标的宽度、高度、分辨率和背景色
    plt.figure(figsize=(10, 6), dpi=128)
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏图形区的标签  MatplotlibDeprecationWarning  未来可能不是单例？？
    # p_axes = plt.axes()
    # p_axes.get_xaxis().set_visible(False)
    # p_axes.get_yaxis().set_visible(False)

    # 关闭坐标轴
    # plt.axis('off')
    # 关闭坐标轴的刻度
    plt.xticks([])
    plt.yticks([])

    plt.show()

    if_continue = input("Make another walk?(y/n):")
    if if_continue == 'n':
        break
