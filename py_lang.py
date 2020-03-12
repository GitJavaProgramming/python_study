"""python语言总结"""
import keyword

# 0 语法规则
# 1
"""python关键字"""
print(keyword.kwlist)

# 2
"""python数据类型 None|数字|序列|映射|集合"""
"""
数字  int|float|complex|boll
序列  str|unicode|list|tuple|xrange
映射  dict
集合  set|frozenset
类    object  所有类型和类的祖先 类型的继承--见面向对象python
类型  type    内置类型和类的类型
"""


def compare(a, b):
    if a is b:
        return True
    elif a == b:
        # a和b具有相同的值
        return True
    elif type(a) is type(b):
        return True
    else:
        if isinstance(a, list):
            return True


# 3
"""python函数"""


# 自定义函数
def foo(x, y):
    return x + y


# 函数作为参数
def callf(func, *args):
    return func(*args)


print("x+y=" + str(callf(foo, 1, 2)))

# lambda
bar = lambda x, y: x + y
v = bar(1, 2)
print(v)

"""打印自定义函数的属性"""
p_list = [foo.__doc__,
          foo.__name__,
          foo.__dict__,
          foo.__code__,
          foo.__defaults__,
          foo.__closure__,
          foo.__globals__,
          bar.__globals__]
print(p_list)

# 4
"""面向对象的python"""


class Foo(object):
    def instance_method(self, arg):
        pass

    @classmethod
    def class_method(cls, arg):
        pass

    @staticmethod
    def static_method(arg):
        pass


# 继承体系 object
class Account(object):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def super_method(self):
        print(self.name)


class SubAccount(Account):
    name = ""
    balance = ""

    def __init__(self, name, balance, other):
        super(SubAccount, self).__init__(name, balance)
        # Account.__init__(self, name, balance)
        self.other = other

    @classmethod
    def init_method(cls, account):
        cls.name = account.name
        cls.balance = account.balance
        cls.super_method(account)
        return cls

    @staticmethod
    def static_method(*args):
        print(*args)
        pass


account = Account("浦发", "1GBit")
sub_account = SubAccount("工行", "10GBit", "中国")
print(type(account))
print(type(sub_account))
sub_account.super_method()

# class method
new_type = SubAccount.init_method(account)
print(new_type.name)
print(new_type.balance)
# print(new_type.other)
print(sub_account.name)

# static method
SubAccount.static_method("12", "43", "98")
