# py_list.py python线性表

# 线性表结点结构
from random import randint

from datastruct.py_exception import LinkedListUnderflow


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


# 单链表结构
class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                # 参考 https://docs.python.org/zh-cn/3.8/reference/expressions.html#grammar-token-yield-expression
                yield p.elem
            p = p.next


# 使用
my_list1 = LList()
if my_list1.is_empty():
    my_list1.prepend(99)
for i in range(11, 20):
    my_list1.append(randint(1, 20))
for x in my_list1.filter(lambda y: y & 1 == 1):
    print(x)
