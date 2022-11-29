x = [1, 2, 1]
x[2] = 3
# x[3] = 4
print(x)
# del x[0]
# print(x)
x[0:2] = [9, 8]
print(x)

# list append clear copy count extend index insert pop remove reverse sort
x = list([1, 2, 1])
x.append(5)
print(x)
a = [1, 2, 3]
b = [4, 5, 6]
a[len(a):] = b
print(a)
print(a.pop(1))
print(a)
b = sorted([4, 5, 2, 1, 3])
print(b)
a.sort(reverse=True)
print(a)
# 元组 不可修改的序列
x = 1, 2, 3
print(x[0:2])
