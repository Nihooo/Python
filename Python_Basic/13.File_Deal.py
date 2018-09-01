# r只读 w只写
# f = open('linux', 'r', encoding='utf-8') # open找的是系统编码，windows是gbk编码，而pycharm默认保存utf-8
# data = f.read()
# print(data)

# print(f.readable()) # 判断文件是否只读

# 使用read后，光标就已经在文件最后，再使用readline就没有内容了
# print('1', f.readline(), end='') # end = ''去掉换行
# print('2', f.readline(), end='')
# print('3', f.readline())
# print('4', f.readline())
# print('5', f.readline())

# data = f.readlines() # 按行读取并放入列表里
# print(data)
# f.close()

# w会将文件清空掉再来执行,文件内容写和读都是字符串
# f = open('linux', 'w', encoding='utf-8')
# f.write('11111\n') # 写时需自己加换行
# f.write('22222\n4444\n5555\n')

# f.writable()# 判断是否可写
# f.writelines(['666\n', '777\n'])
# f.close()

# 追加操作 a
# f = open('linux', 'a', encoding='utf-8')
# f.write('the end')
# f.close()

# 可读可写
# f = open('linux', 'r+', encoding='utf-8')
# data = f.read()
# print(data)
# f.write('\nmamadesuyo')


'''
read_f = open('linux', 'r', encoding='utf-8')
# data = read_f.readlines()
data = read_f.readlines()
read_f.close()

write_f = open('linux_new', 'w', encoding='utf-8')
# write_f.writelines(data)
write_f.writelines(data[0:3])
write_f.close()
'''

# with 不用加close操作

# with open('linux', 'w') as f:
#     f.write('111\n')

# with open('linux', 'r', encoding='utf-8') as read_f,\
#         open('linux_new', 'w', encoding='utf-8') as write_f:
#     data = read_f.read()
#     write_f.write(data)

# b的方式不能指定编码 rb wb ab
# f = open('linux', 'rb')
# data = f.read()
# print(data.decode('utf-8'))
# f.close()
# windows中换行是\r\n

# 字符串----------encode------------》bytes
# bytes-----------decode------------》字符串

# f = open('linux_new', 'wb')
# f.write(bytes('vdva\n', encoding='utf-8'))
# f.write('jfaa'.encode('utf-8'))
# f.close()

# with open('linux', 'r+', encoding='utf-8', newline='') as f: # newline会读取文件中真正的换行符\r\n
# print(f.encoding) # 文件打开的编码

# f.flush() # 刷新

# print(f.tell()) # 光标所在位置
# f.readlines()
# print(f.tell())
#
# f.seek(0) # 使光标移动到指定位置
# print(f.tell())

# read读的是字符，其他读的是字节

# f.truncate(10) # 截取，属于写操作，10个字节

# 使用seek的其他功能时，要使用b的形式
# with open('linux', 'rb') as f:
#     print(f.tell())
    # f.seek(10, 1) # 从相对位置开始seek
    # print(f.tell())
    # f.seek(3, 1) # 从上次光标的位置开始
    # print(f.tell())

    # f.seek(-10, 2) # 倒着读模式，需要用负数
    # print(f.read())
    # print(f.tell())
    
# 循环文件的方式seek
#     for i in f: # 用f.readlines会将文件内容先放入列表再循环太占内存，直接用f就能要一行读一行
#         offs = -10
#         while True:
#             f.seek(offs, 2)
#             data = f.readlines()
#             if len(data) > 1:
#                 print('文件的最后一行是%s' % (data[-1].decode('utf-8')))
#                 break
#             offs *= 2
