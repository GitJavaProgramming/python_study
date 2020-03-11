# 使用matplotlib画折线
import matplotlib.pyplot as plt

input_values = list(range(1, 1001))
squares = [x ** 2 for x in input_values]
plt.plot(input_values, squares, linewidth=5)
# 绘制连续的点
plt.scatter(input_values, squares, c=squares, cmap=plt.cm.Blues, edgecolors='none', s=40)

# 坐标系设置
plt.title("Square Numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("map value", fontsize=24)
plt.tick_params(axis='both', labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 自动保存图像
# plt.savefig('plot.png', bbox_inches='tight')
plt.show()

