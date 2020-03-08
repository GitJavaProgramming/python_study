read_filename = 'py_class.py'
write_filename = 'README.md'
# 文件读取
try:
    with open(read_filename, encoding='utf-8') as file_object:
        contents = file_object.read()
        print(contents)
    print('-----------------------------------------------逐行读取-----------------------------------------------')
    # 逐行读取
    with open(read_filename, encoding='utf-8') as file_object:
        for line in file_object:
            # 去除多余的空白符
            print(line.rstrip())
    print('-----------------------------------------创建一个按行读取的列表-----------------------------------------')
    # 按行读取并存入列表
    with open(read_filename, encoding='utf-8') as file_object:
        # lines = file_object.readline()
        lines = file_object.readlines()
    # 文件切片 读取前10行
    for line in lines[:10]:
        print(line.rstrip())

    # 文件写入
    with open(write_filename, 'a', encoding='utf-8') as file_object:
        file_object.write('由py_file.py写入：python一个完全看不到类型的动态语言.\n')
        file_object.write('由py_file.py写入：python模块与ES6模块，C语言的库类似，它们都是为了更好的组织软件结构.\n')
        file_object.write('由py_file.py写入：这是领域设计思想的具体应用.\n')

except FileNotFoundError:
    print("FileNotFoundError")
    # pass
else:
    print("文件读写完成.")
