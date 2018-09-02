# 反射：程序自己检测自己

'''
class BlackMedium:
    feture = "Ugly"

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def sell_house(self):
        print("[%s] 正在卖房子，傻逼才买呢" % self.name)

    def rent_house(self):
        print("[%s] 正在租房子，傻逼才租呢" % self.name)

b1 = BlackMedium("万成置地", "天露园")

# 实现自省功能(适用于类和对象)

# print(hasattr(b1, 'name')) # hasattr判断object中有没有一个name字符串对应的方法或属性
# print(hasattr(b1, "sell_house"))
# print(hasattr(BlackMedium, "feture"))
# print(hasattr(BlackMedium, "rent_house"))


# 获取当前模块，查看里面的内容
import sys
x = 11
obj = sys.modules[__name__]
print(hasattr(obj, "x"))



# print(getattr(b1, 'name')) # getattr找到object中name字符串对应的方法或属性，没有就报错
# print(getattr(b1, "rent_house"))
# print(getattr(b1, "rent_housefegaba", '没有这个属性或方法')) # 加个默认参数找不到也不会报错，会将其输出

# setattr(b1, "sb", True) # 设置（加入）一个数据属性
# print(b1.__dict__)
# setattr(b1, "name", "SB") # 已经有时就变为修改
# print(b1.__dict__)

# del b1.name
# delattr(b1, "name")
# print(b1.__dict__)

# setattr加函数属性
# setattr(b1, "func", lambda x: x+1)
# setattr(b1, "func1", lambda self: self.name + "sb")
# print(b1.__dict__)
# print(b1.func)
# print(b1.func(10))
# print(b1.func1(b1))
'''



'''
class FTPClient:
    'ftp客户端，但是还没有实现具体的功能'
    def __init__(self, addr):
        print("正在连接服务器[%s]" % addr)
        self.addr = addr

    def put(self):
        print("正在上传文件")

# from module import FTPClient(就是上面那个)
# 可插拔处理
f1 = FTPClient("192.168.1.1")
if hasattr(f1, "put"):
    func_get = getattr(f1, "put")
    func_get()
else:
    print("---->不存在此方法")
    print("处理其他的逻辑")
'''


# 动态导入模块
# __import__后面跟字符串调用路径
# m = __import__("123.t") # 不管123后面跟多少层，都只会得到顶级的模块名module 123
# m.t.test()

# import importlib
# m = importlib.import_module("123.t") # 使用importlib，就能拿到你想调用的123.t
# m.test()

# 在模块里有一个_test2()函数，在被调用的时候，不能进行from xxx import * 调用，只能用from xxx import _test2的形式调用，才能对其使用




# 下划线开头的attr方法(类内置的)，重写了就用自己写的，没有就用系统内置的, __getattr__,__delattr__, __setattr__(要实例化才能用)
'''
class Foo:
    x = 1

    def __init__(self, y):
        self.y = y

    def __getattr__(self, item): # 当调用一个不存在的属性时触发
        print("执行__getattr__")

f1 = Foo(10)
print(f1.y)
f1.aaaaaaa
'''


'''
class Foo:
    x = 1

    def __init__(self, y):
        self.y = y

    def __delattr__(self, item): # 删除的时候会触发
        print("执行__getattr__")
        # del self.item # 无限递归了
        self.__dict__.pop(item)

f1 = Foo(10)
del f1.y
del f1.x
'''


'''
class Foo:
    x = 1

    def __init__(self, y):
        self.y = y

    def __setattr__(self, key, value): # 设置或修改属性的时候会触发
        print("__setattr__执行")
        # self.key = value # 会进入一个死递归
        self.__dict__[key] = value

f1 = Foo(10)
print(f1.__dict__)
f1.z = 2
print(f1.__dict__)
'''



'''
class Foo:

    def __init__(self, name):
        self.name = name

    def __getattr__(self, item): # f1传给self，age传给item
        print("你找的属性【%s】不存在" % item)

    def __setattr__(self, k, v): # k得到age，v得到18
        print("执行setattr", k, v)
        if type(v) is str:
            print("开始设置")
            self.__dict__[k] = v
        else:
            print("必须是字符串类型")

    def __delattr__(self, item): # item为name
        print("执行delattr", item)
        self.__dict__.pop(item)

f1 = Foo("alex")
# f1.age = 18
# f1.gender = "male"
# print(f1.__dict__) # 当进行属性的赋值或修改时，系统的__setattr__会自动将值传入进字典属性里，由于对其进行了自定义，所以没有了这些功能，只能自己添加
# print(f1.name)
# print(f1.age)
# print(f1.gender)
print(f1.__dict__)
del f1.name
print(f1.__dict__)
'''
