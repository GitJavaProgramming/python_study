import py_class as cls
from collections import OrderedDict

# 对象属性与方法
your_dog = cls.Dog("dog", 2)
print(your_dog.name)
print(your_dog.roll_over())
# 直接修改属性
your_dog.name = "big dog"
print(your_dog.name)
# new_dog = cls.Dog("dog", 2)
# print(new_dog.name)
# 方法修改
your_dog.__setattr__("name", "new big dog")
print(your_dog.name)
# new_dog = cls.Dog("dog", 2)
# print(new_dog.name)

# 对象继承
your_wolf = cls.Wolf("狼", "狼狗", 3);
your_wolf.sit()
your_wolf.dog.sit()
your_wolf.tansform()

# python 标准库
print("Python 标准库.")
favorite_languages = OrderedDict()

favorite_languages['c'] = 'C'
favorite_languages['java'] = 'Java'
favorite_languages['js'] = 'JavaScript'
favorite_languages['py'] = 'Python'
favorite_languages['sql'] = 'SQL'
favorite_languages['shell'] = 'SHELL'

for name, language in favorite_languages.items():
    print(language)
