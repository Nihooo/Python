# 包装标准类型，定制自己的数据类型

'''
class List(list):
    def show_middle(self):
        mid_index = int(len(self)/2)
        return self[mid_index]

    def append(self, p_obj):
        if type(p_obj) is str:
            super().append(p_obj)
        else:
            print("只能添加字符串类型")

# l2 = list("helloworld")
# print(l2, type(l2))

# l1 = List("helloworld")
# print(l1, type(l1))
# print(l1.show_middle())
# l1.append("11111")
# print(l1)
'''



# 授权：也是一种包装，实现授权的关键点是通过覆盖__getattr__方法

'''
import time
class Filehandle:
    def __init__(self, filename, mode = 'r', encoding = 'utf-8'):
        # self.filename = filename
        self.file = open(filename, mode, encoding = encoding)
        self.mode = mode
        self.encoding = encoding


    # 自定义write，为每个写的内容加上时间
    def write(self, line):
        print("------->", line)
        t = time.strftime("%Y-%m-%d %X")
        self.file.write("%s %s" % (t, line))

    def __getattr__(self, item):
        print(item)
        # self.file.read
        return getattr(self.file, item)


f1 = Filehandle("a.txt", "r+")
# print(f1.file)
# f1.read # 触发__getattr__
# print(f1.read)
f1.write("111111111\n")
f1.write("22222222\n")
f1.seek(0)
print(f1.read())
'''
