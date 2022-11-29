# 第一个程序
print('\nHello world!')

# 索引、切片、相加、相乘、成员资格检查
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
month = input('Month(1-12):')
month_name = months[int(month) - 1]
print(month_name)
print(months[2:4])
print(months[-3:-1])
# 打印列表最后三个元素
print(months[-3:])
# 切片、步长
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0:10:2])
print(numbers[0:10:-2])
print(numbers[10:0:-2])
print(numbers[::-2])
# 输入用户密码，如果成功匹配则打印Access granted
database = [
    ['albert', '1234'],
    ['dilbert', '1234'],
    ['smith', '1234'],
    ['jones', '1234']
]
username = input('username:')
password = input('password:')
if [username, password] in database:
    print('Access granted')