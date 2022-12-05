# open read write close
f = open('file.txt', 'w')
print(f.write('hello\n'))
print(f.write('hello\n'))
f.close()

f = open('file.txt', 'r')
print(f.read(4))
print(f.read())
f.close()

# readlines writelines
f = open('file.txt', 'r')
lines = f.readlines()
print(type(lines))
f.close()
lines[1] = 'world'
print(lines)
f = open('file.txt', 'w')
f.writelines(lines)
f.close()


# 按行读取
def process(line):
    print(line)


with open('file.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        process(line)
