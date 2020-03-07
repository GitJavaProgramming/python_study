# ****************字符串****************
message = "Hello Python World!"
print(message)

message = "new senetence"
print(message)

banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(user.title())

print("Languages:\n\tJAVA\n\tPython\n\tJavaScript")
print(0.2 + 0.1)
age = 23
print("Happy " + str(age) + "rd Birthday.")

# ****************列表****************
names = ["001", "002", "003", "004"]
print("name:" + names[0].title())

names.append("005")
print(names)

# names.insert(1, "000")
names.insert(3, "321")
print(names)

# 删除该元素 无法访问
del names[3]
print(names)

your_name = names.pop()
print(your_name)
print(names)

# 列表遍历
for t_name in names:
    print(t_name)

numbers = list(range(1, 6))
print(numbers)
numbers = list(range(2, 11, 2))
print(numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
# 列表解析 切片
squares = [value ** 1 for value in range(1, 6)]
print(squares[1:3])
print(squares)
print(squares[:3])
print(squares[1:])
print(squares[-2:])

# 列表复制
squares2 = squares[:]
squares.append("900")
squares2.append("911")
print(squares)
print(squares2)
# squares2 squares 指向同一个列表
squares2 = squares
squares.append("922")
print(squares)
print(squares2)

# 元组->不可变的列表
dimension = (100, 200)
print(dimension[0])
# dimension[0] = 222  # 不可改变
# print(dimension[0])

# 字典
alien_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}
print(alien_0['color'])
print(alien_0['points'])

alien_0['color'] = 'red'
print(alien_0['color'])
del alien_0['color']
# print(alien_0['color'])
print(alien_0)

print('字典|列表')
aliens = []
for alien_number in range(30):
    new_alien = alien_0
    aliens.append(new_alien)
for alien_number in aliens[:5]:
    print(alien_number)
print('...')
print("Total number of aliens： " + str(len(aliens)))

