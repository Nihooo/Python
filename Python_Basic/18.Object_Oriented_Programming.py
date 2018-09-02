# 面向过程的步骤：把一个大的问题，分成几个小的问题，从第一步执行到最后一步

# 函数式编程：用python里面的东西，将一个数学模型表现出来

# 面向对象设计：对象：动作和特征的集合，类中具体的存在  类：抽象的概念，动作和特征的集合，把一类事物的相同的特征和动作整合到一起
# 面向对象编程：用class来进行面向对象设计


# 用嵌套函数来了解面向对象
'''
def dog(name, gender, type): # 定义狗类，将分离的动作和特征放到一个作用域里
    def bark(dog_info): # 动作
        print("%s狗[%s] 汪汪大叫" % (dog_info["gender"], dog_info["name"]))

    def eat_shit(dog_info):
        print("%s狗[%s] 正在eat_shit" % (dog_info["gender"], dog_info["name"]))

    def init(name, gender, type):
        my_dog = {
            "name" : name, # 特征
            "gender": gender,
            "type": type,
            "bark": bark,
            "eat_shit": eat_shit
        }
        return my_dog

    res = init(name, gender, type)
    return res # (  init(name, gender, type)    )

dog1 = dog('lhf', '公', '吉娃娃')
dog1["bark"](dog1) # dog1["bark"](为dog1字典键bark里对应的值，为一个内存地址
dog2 = dog('alex', '母', '腊肠')
dog2["eat_shit"](dog2)
'''



# 定义学校类
'''
def school(name, addr, type): # 定义狗类

    def init(name, addr, type): # 采用这种方式可将特征和动作放前面
        school_info = {
            "name" : name, # 特征
            "gender": addr,
            "type": type,
            "exam": examination,
            "recruit": recruit_student
        }
        return school_info

    def examination(school_info): # 动作
        print("%s 正在考试" % school_info["name"])

    def recruit_student(school_info):
        print("%s %s正在招生" % (school_info["type"], school_info["name"]))

    return init(name, addr, type)

school1 = school('oldboy', '沙河', '私立学校')
print(school1)
school1["recruit"](school1)
'''


# 面向对象编程

# 属性：1.数据属性:就是变量 2.函数属性:就是函数，也叫方法



'''
class Chinese: # 这是一个中国人的类，类名要大写（规范）

    '这是一个中国人的类'

    government = "中国政府" # 数据属性

    def sui_di_tu_tan(): # 函数属性
        print("朝着墙上就是一口痰")

    def cha_dui(self): # 函数属性
        print("插到了前面")

print(Chinese.government) # 调用数据属性

p1 = Chinese() # 实例化
print(p1)
Chinese.sui_di_tu_tan() # 调用函数属性
Chinese.cha_dui("lhf")

print(dir(Chinese)) # 查看属性
print(Chinese.__dict__) # 查看类的属性字典
print(Chinese.__dict__["government"])
Chinese.__dict__["sui_di_tu_tan"]() # Chinese.__dict__["sui_di_tu_tan"]为内存地址
Chinese.__dict__["cha_dui"](1) # (1)为随便传的一个参数


# 没什么用
# print(Chinese.__name__) # 类名
# print(Chinese.__doc__) # 文档，就是'这是一个中国人的类'
# print(Chinese.__base__) # 所有的类都有一个共同的祖先叫object
# print(Chinese.__bases__) # 意思同上，但以元组的形式显示出来
# print(Chinese.__module__) # 模块
# print(Chinese.__class__) # 类型
'''



'''
class Chinese:
    '这是一个中国人的类'

    government = "中国政府" # 数据属性

    def __init__(self, name, age, gender):
        print("我是init初始化函数")
        self.name = name # 数据属性，都封装到self里，等于p1.name = name
        self.age = age # 等于p1.age = age
        self.gender = gender
        print("我结束了")

        # 不需要加return，class会自动return

    def sui_di_tu_tan(self): # 函数属性
        print(self)
        print("%s朝着墙上就是一口痰" % self.name)

    def cha_dui(self): # 函数属性
        print("%s插到了前面" % self.name)

    # 不需要加return，class会自动return

p1 = Chinese("lhf", 18, 'female')  # 会触发__init__函数运行,实际上就是在执行 p1 = Chinese.__init__(p1, name, age, gender)
print(p1)
print(p1.__dict__) # 实例字典，并不包含函数属性，函数属性属于类
print(p1.__dict__["name"])
print(p1.name) # 同上

print(Chinese.__dict__)
Chinese.sui_di_tu_tan(p1)

p1.sui_di_tu_tan() # 相当于闭包，def __init__找不到，就会去外一层找类里找
# p1就会默认传给sui_di_tu_tan()的第一个参数

# 实例只能访问数据属性，函数属性是找类要的
'''



'''
class Chinese:
    '这是一个中国人的类'

    government = "中国政府" # 数据属性

    def __init__(self, name, age, gender): # 数据属性
        self.name = name
        self.age = age
        self.gender = gender

    def sui_di_tu_tan(self): # 函数属性

        print("%s朝着墙上就是一口痰" % self.name)

    def cha_dui(self): # 函数属性
        print("%s插到了前面" % self.name)

    def eat_food(self, food): # 函数属性
        print("%s 正在吃%s" % (self.name, food))

# p1 = Chinese("lhf", 18, 'female')
# p1.eat_food("鸡腿")
#
# p2 = Chinese("wupeiqi", 100, "菇凉")
# p2.eat_food("韭菜馅饼")


# 查看类属性
print(Chinese.government)
# 修改类属性
Chinese.government = "CHINA"
print(Chinese.government)
# 删除类属性
del Chinese.government
# 增加类属性
Chinese.country= "China"
Chinese.location = "Asia"
print(Chinese.__dict__)

p1 = Chinese("alex", 45, "male")
print(p1.country)
print(p1.location)

# 增加函数
def drink_water(self, water):
    print("%s 正在吃%s" % (self.name, water))

Chinese.drink = drink_water

p1.drink("cola")


# 修改函数
def test(self):
    print('test')

Chinese.cha_dui = test
p1.cha_dui()
'''



'''
# 实例属性的增删改查

class Chinese:
    country = "China"
    def __init__(self, name):
        self.name = name

    def play_ball(self, ball):
        print("%s 正在打 %s" % (self.name, ball))

p1 = Chinese("alex")
print(p1.__dict__)

# 查看实例属性
# print(p1.name)
# print(p1.play_ball)

# 增加
p1.age = 18
print(p1.__dict__)
print(p1.age)

# 不要这样去修改底层的属性字典
# p1.__dict__["sex"] = "male"
# print(p1.__dict__)
# print(p1.sex)

# 修改
p1.age = 19
print(p1.__dict__)
print(p1.age)

# 删除
del p1.age
print(p1.__dict__)
'''



# 定义一个类，只当一个作用域去用
'''
class Mydata:
    pass

x = 10
y = 20
Mydata.x = 1
Mydata.y = 2

print(x, y)
p1 = Mydata()
print(p1.x, p1.y)
print(Mydata.x, Mydata.y)
print(Mydata.x + Mydata.y)
'''



'''
class Chinese:
    country = "China"
    def __init__(self, name):
        self.name = name

    def play_ball(self, ball):
        print("%s 正在打 %s" % (self.name, ball))

p1 = Chinese("alex")
print(p1.country)
p1.country = "日本" # 在p1的字典加，与类的无关
print("类的---》", Chinese.country)
print("实例的---》", p1.country)
'''



'''
country = 'china'
class Chinese:
    country = "中国"
    def __init__(self, name):
        self.name = name
        print('--->', country) # 此刻和类与实例都没有任何关系，没有用到 p1.  Chinese. 来调用,只是一个变量,没有从实例和类的字典里去找

    def play_ball(self, ball):
        print("%s 正在打 %s" % (self.name, ball))

p1 = Chinese("alex")
# print(p1.country) # p1会先找自己的，然后找类的，如果没有就报错
'''



'''
class Chinese:
    country = "China"
    l = ['a', 'b']
    def __init__(self, name):
        self.name = name

    def play_ball(self, ball):
        print("%s 正在打 %s" % (self.name, ball))


p1 = Chinese("alex")
print(p1.l)
# p1.l = [1, 2, 3] # 存在于p1的字典里
p1.l.append('c') # 类里的l
print(p1.__dict__)
print(Chinese.l)
'''
