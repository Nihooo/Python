# 静态属性
'''
class Room:

    tag = 1

    def __init__(self, name, owner, width, length, heigh):
        self.name = name
        self.owner =owner
        self.width =width
        self.length = length
        self.heigh = heigh

    @property
    def cal_area(self):
        # print('%s 住的 %s 总面积%s' % (self.owner, self.name, self.width * self.length))
        return self.width * self.length

    @property #把函数封装成数据属性的形式，让外部在调用的时候看不到内部的逻辑，类似于调用类的数据属性,能访问到实例属性和类属性
    def cal_volume(self):
        return self.width * self.length * self.heigh



    @classmethod # 类方法，类名.方法，自动传类名进方法，只能访问到类属性
    def tell_info(cls, x):
        print(cls)
        print('--->', cls.tag, 2) # 相当于Room.tag




r1 = Room('厕所', 'alex', 100, 100, 100000)

# r1.cal_area # @property加了之后，不需要加()了,将其背后的属性隐藏起来
# print(r1.cal_area)
# print(r1.cal_volume)
# pring(r1.tag) # 类似于调用类的数据属性

# 跟实例无关，只是类来调用自己的方法
Room.tell_info(2)

r1.tell_info(10)
'''

