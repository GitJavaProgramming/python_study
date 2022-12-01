def show(name, age=22):
    """ 显示名称：年龄 """
    print('name=', name)
    print('age=', age)


show('peng')
show(name='haha', age=10)
show(age=10, name='haha')


def test(_names):
    _names[0] = 'balabala'
    _names = [1, 2, 3]


names = ['anne', 'beth', 'george', 'damon']
print(names)
test(names)
print(names)
