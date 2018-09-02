'''
# 静态方法
class Room:

    tag = 1

    def __init__(self, name, owner, width, length, heigh):
        self.name = name
        self.owner =owner
        self.width =width
        self.length = length
        self.heigh = heigh

    @staticmethod # 类的工具包，不跟类绑定，也不跟实例绑定，只是名义上的归属类管理，不能使用类变量和实例变量
    def wash_body(a, b, c):
        print('%s %s %s正在洗澡' % (a, b, c))

    # 毫无意义
    def test(x, y):
        print(x, y)


Room.wash_body('alex', 'lhf', 'wupeiqi')
print(Room.__dict__)

r1 = Room('厕所', 'alex', 100, 100, 100000)
print(r1.__dict__)
r1.wash_body('alex', 'lhf', 'wupeiqi')

Room.test(1, 2)
'''
