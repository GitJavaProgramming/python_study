import pygal

from visualization.die import Die

# 两个不同面数的骰子
die_1 = Die()
die_2 = Die(8)

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# print(results)
# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)
# 结果可视化
hist = pygal.Bar()
hist.title = "扔骰子1000次"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
hist.y_labels = "统计结果"
hist.add('D6 + D8', frequencies)
hist.render_to_file('die_visual.svg')
