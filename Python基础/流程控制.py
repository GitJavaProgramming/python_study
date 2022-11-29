values = 1, 2, 3
x, y, z = values
print(values)
print(x)

# if
name = 2
if name < 0:
    print('negative')
elif name > 1:
    print('larger')
else:
    print('1')

d = {'x': 1, 'y': 2, 'z': 3}
for key, value in d.items():
    print(key, '->', value)
for key in d.keys():
    print(key)
for value in d.values():
    print(value)

names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
# zip将两个序列组合起来，返回一个由元组组成的序列
r = list(zip(names, ages))
print(r)
print(dict(r))

for index, string in enumerate(names):
    if 'ann' in string:
        names[index] = 'peng'
        break
print(names)

# 简单推导
