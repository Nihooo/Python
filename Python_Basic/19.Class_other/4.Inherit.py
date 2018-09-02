# 面向对象的三大特性：继承，多态，封装，他们只是一种思想

# 继承
'''
class Father:
    pass

class Mother:
    pass

# class Son(Father): # 单继承
#     pass

class Son(Father, Mother): # 多继承
    pass
'''



'''
class Father:
    '这是父类'
    money = 10
    def __init__(self, name):
        print("father")
        self.name = name

    def hit_son(self, son):
        print("%s 正在打儿子%s" % (self.name, son))

class Son(Father): # 自己没有去父类找

    money = 111111

    def __init__(self, name, age):
        self.name =name
        self.age = age

    def hit_son(self, son):
        print("来自儿子类")

# print(Son.money)
# Son.hit_son()

# print(Father.__dict__)
# print(Son.__dict__)

# s1 = Son('alex')
# s1.hit_son('lhf')

# s1 = Son('alex')
# print(s1.money)
# print(Father.money)

s1 = Son('alex', 18)
s1.hit_son('lhf2')
'''



# 什么时候用继承
# 1.当类之间有显著不同，并且较小的类是较大的类所需要的组件时，用组合比较好
# 2.当类之间有很多相同的功能，提取这些共同的功能做成基类，用继承比较好

# 例如：猫：喵喵叫，吃喝拉撒  狗：汪汪叫，吃喝拉撒  就可以提取相同的功能作为基类（动物类）
# 派生，在继承的基础上，衍生出新的功能



'''
# 接口:就是一个函数
# 接口继承：定义一个基类，基类当中，把自己的方法定义成接口函数,只要来一个子类继承他，那子类当中就必须实现父类的方法，不实现就没办法实例化

import abc

class All_file(metaclass=abc.ABCMeta):
    @abc.abstractmethod # 定义接口函数
    def read(self): # 基类里的方法没必要实现，只是为了规范子类
        pass

    @abc.abstractmethod
    def write(self):
        pass

class Disk(All_file): # 继承All_file的子类必须实现All_file中接口化了的方法
    def read(self):
        print("Disk read")
    def write(self):
        print("Disk write")

class Cdrom(All_file):
    def read(self):
        print("Cdrom read")
    def write(self):
        print("Cdrom write")

class Mem(All_file):
    def read(self):
        print("Mem read")
    def write(self):
        print("Mem write")

# 归一化，方便管理
m1 = Mem()
m1.read()
m1.write()
'''



'''
class A:
    def test(self):
        print("A")

class B(A):
    # def test(self):
    #     print("B")
    pass

class C(A):
    # def test(self):
    #     print("C")
    pass

class D(B):
    # def test(self):
    #     print("D")
    pass

class E(C):
    # def test(self):
    #     print("E")
    pass

class F(D, E):
    # def test(self):
    #     print("F")
    pass

f1 = F()
f1.test() # F-->D-->B-->E-->C-->A 这是广度优先，深度优先F-->D-->B-->A-->E-->C

# MRO列表存放着继承顺序
print(F.__mro__)
'''



'''
# 子类中调用父类

class Vehicle:
    country = "China"
    def __init__(self, name, speed, load, power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print("开动啦。。。")

class Subway(Vehicle):
    def __init__(self, name, speed, load, power, line):
        # self.name = name
        # self.speed = speed
        # self.load = load
        # self.power = power
        # Vehicle.__init__(self, name, speed, load, power) # 同上
        # super(Subway, self).__init__(name, speed, load, power)  # super(__class__, self).__init__(name, speed, load, power)
        super().__init__(name, speed, load, power) # 通过super就可调到父类的方法，当父类名更改时，只需改调用就行，而且不用加self参数
        self.line = line

    def show_info(self):
        print(self.name,self.line)


    def run(self):
        # Vehicle.run(self) # 调用父类方法
        super().run()
        print("%s %s 线开动啦" % (self.name, self.line))

s1 = Subway('北京地铁', '10km/s', 100000, '电', 13)
s1.show_info()
s1.run()
'''
