# 封装的目的在于隐藏，本质是明确区分内外

'''
class People:

    # _star = 'earth' # 第一层面的封装，属性为单_开头的，就是一个被隐藏起来的属性，外部不能用，这只是一种约定，但还是能用，只是告诉使用者不应去调用

    __star = 'earth' # 第二层面的封装，属性为双__开头的，python会进行重命名，以 _类名__类数据名 _People__star，也只是一种约定

    def __init__(self, id, name, age, salary):
        # print('---->', self.__star) # 明确区分内外，内部能用，外部不能用
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    # 访问函数(接口函数)
    def get_id(self):
        print(self.__star)
        print("我是私有方法，我找到的id是[%s]" % self.id)

p1 = People("123", "alex", '18', 100)

# print(p1._star)

# print(p1.__star)
# print(p1._People__star)
# p1.get_id() # p1为外部，但get_id为内部，能曲线的去找到隐藏属性
'''



'''
class Room:

    def __init__(self, name, owner, width, length, high):
        self.name = name
        self.owner = owner
        self.__width = width # 仅仅举例，实际上没必要封装
        self.__length = length
        self.__high = high

    def tell_area(self):
        return self.__width * self.__length

r1 = Room('卫生间', 'alex', 100, 100, 10000)
print(r1.tell_area())
'''


# 面向对象的优点：1.通过封装明确了内外  2.通过继承+多态在语言层面支持归一化设计
