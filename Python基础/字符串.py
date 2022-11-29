from math import pi

print("{foo} {1} {bar} {0}".format(1, 2, bar=4, foo=3))
fullname = [1, 2]
print("Mr {name[1]}".format(name=fullname))
print("{num:b}".format(num=42))
print("{num:10}".format(num=3))
print("{num:10}".format(num="Bob"))
print("{pi:.2f}".format(pi=pi))
# center find join lower replace split strip translate
