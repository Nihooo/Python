# 面向对象进阶


'''
class Foo:
    pass

f1 = Foo()
print(isinstance(f1, Foo)) # 检查f1是否是由Foo实例化而来


class Bar(Foo):
    pass

print(issubclass(Bar, Foo)) # 判断Bar是否是Foo的子类
'''



'''
class Foo:
    def __init__(self, x):
        self.x = x

    def __getattr__(self, item): # getattribute抛出异常后执行
        print("执行的是__getattr__")

    def __getattribute__(self, item): # 属性有或没有都会触发
        print("执行的是__getattribute__")
        raise AttributeError("抛出异常了") # 抛出AttributeError异常后才会去找__getattr__
        # raise 抛出异常
        
f1 = Foo(10)
# f1.x
f1.xxxxx
'''



'''
class Foo:
    pass

class Bar(Foo):
    pass

b1 = Bar()
print(isinstance(b1, Bar))
print(isinstance(b1, Foo))
print(type(b1))
print(type([1, 2, 3]))
'''



'''
class Foo:
    def __getitem__(self, item):
        print("getitem")
        return self.__dict__[item]

    def __setitem__(self, key, value):
        print("setitem")
        self.__dict__[key] = value

    def __delitem__(self, key):
        print("delitem")
        self.__dict__.pop(key)

f1 = Foo()
print(f1.__dict__)

f1["name"] = "egon" # 原来赋值是f1.name = "egon",用了setitem后可以这样，并执行__setitem__
f1["age"] = 18 # 通过操作字典的方式才能触发item
print(f1.__dict__)
# del f1.name # 只能触发__delattr__
del f1["name"] # 触发__delitem__
print(f1.__dict__)

print(f1.age)
print(f1["age"]) # 触发__getitem__

# 通过 x.x 的方式操作属性与__xxxattr__相关,通过x["x"]的方式操作属性就与__xxxitem__相关
'''



# 改变对象的字符串显示
'''
# l = [1, 2, 3] # l为对象
# print(l)

# file = open("a.txt", "r") # file为对象
# print(file)

class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self): # 系统默认有
    #     return "自定制的对象显示方式"

    def __str__(self):
        return "str 名字是%s 年龄是%s" % (self.name, self.age)

    def __repr__(self): # repr在解释器中触发
        return "repr 名字是%s 年龄是%s" % (self.name, self.age)


# f1 = Foo('alex', 45)
# print(f1) # print调用的是__str__,str(f1)--->f1.__str__()


# 共存情况下，优先找__str__，如果没有str就会去找__repr__作为替代品
f1 = Foo('alex', 45)
print(f1) # repr(f1)--->f1.__repr__()，解释器里显示
'''



'''
# 自制格式化方式format

format_dic = {
    "ymd": "{0.year} {0.month} {0.day}",
    "m:d:y": "{0.month}:{0.day}:{0.year}",
    "d-m-y": "{0.day}-{0.month}-{0.year}",
}
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        print("format")
        print("--->", format_spec)
        if not format_spec or format_spec not in format_dic:
            format_spec = "ymd"
        fm = format_dic[format_spec]
        return fm.format(self)

d1 = Date(2016, 12, 26)
# format(d1) # 执行__format__
print(format(d1))
print(format(d1, "d-m-y"))

# x = "{0.year} {0.month} {0.day}".format(d1) # 触发的就是__format__
# y = "{0.year}:{0.month}:{0.day}".format(d1)
# print(x)
# print(y)
'''



# __slots__,如果一个类有很少的属性，但却有很多的实例，就会为每个实例开辟内存空间，会大大浪费内存空间
# 所以用 __slots__去取代__dict__，他通过为实例构建一个很小的固定大小的数组来实现更加紧凑的内部表示

'''
class Foo:
    # __slots__ = ["name", "age"] # ["name":None, "age":None]
    __slots__ = "name" # 由他生成的实例不再具有__dict__属性

f1 = Foo()
f1.name = "alex"
print(f1.name)

# print(f1.__dict__)
# f1.age = 18 # --->setattr--->f1.__dict__["age] = 18,但用slots没有__dict__
print(f1.__slots__)
print(Foo.__slots__)
'''

'''
class Foo:
    __slots__ = ["name", "age"] # ["name":None, "age":None]

f1 = Foo()
f1.name = "alex"
f1.age = 18
print(f1.name)
print(f1.age)

f2 = Foo()
f2.name = "lhf"
f2.age = 15
print(f2.name)
print(f2.age)
'''



'''
class Foo:
    '我是描述信息'
    pass

class Bar(Foo):
    pass

print(Foo.__doc__)
print(Bar.__doc__) # 该属性无法继承给子类
'''



'''
from lib.aa import C

c1 = C()
print(c1.name)

print(c1.__module__) # lib.aa
print(c1.__class__) # <class 'lib.aa.C'>
'''



'''
# 析构方法，当对象在内存中被释放时，自动触发执行

class Foo:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("我执行啦")

f1 = Foo("alex")
# 1.del f1.name
# 2.del f1 # 实例被删除就会触发
print("--------------------")
# 3.执行完毕，也会执行
'''



'''
# __call__ 对象后面加括号，触发执行
class Foo:
    def __call__(self, *args, **kwargs):
        print("实例执行啦 obj()")

f1 = Foo()

f1() # Foo下的__call__

Foo() # abc(假设的)下的__call__
'''



'''
# 迭代器协议
class Foo:
    def __init__(self, n):
        self.n = n

    def __iter__(self): # 迭代器一：将对象变为可迭代对象
        return self

    def __next__(self): # 迭代器二：必须要有next方法
        if self.n == 10:
            raise StopIteration("终止了")
        self.n += 1
        return self.n

f1 = Foo(5)
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())
# print(next(f1))
# print(next(f1))
# print(next(f1))

for i in f1: # iter(f1) == f1.__iter__()
    print(i)
'''



'''
# 斐波那契数列

class Fib:
    def __init__(self):
        self._a = 1
        self._b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._a > 100:
            raise StopIteration("end")
        self._a, self._b = self._b, self._a + self._b
        return self._a

f1 = Fib()
print(f1.__next__())
print(f1.__next__())
print(f1.__next__())
print(next(f1))
print(next(f1))
print(next(f1))
'''



# 描述符 __get__, __set__, __delete__
# __get__():调用一个属性时,触发
# __set__():为一个属性赋值时,触发
# __delete__():采用del删除属性时,触发

# 描述符是干什么的:描述符的作用是用来代理另外一个类的属性的(必须把描述符定义成这个类的类属性，不能定义到构造函数中)

'''
class Foo:

    def __get__(self, instance, owner):
        print('触发get', instance, owner)

    def __set__(self, instance, value):
        print('触发set', instance, value)
        instance.__dict__["x"] = value

    def __delete__(self, instance):
        print('触发del')

class Bar:
    x = Foo() # 在何地?
    def __init__(self, n):
        self.x = n # b1.x = 10 ,x被Foo给代理了,实际就去找了__set__

b1 = Bar(10)
# print(b1.__dict__)
# b1.x = 1111111
# print(Bar.__dict__)
# print(b1.__dict__)
# print(b1.x)


#包含这三个方法的新式类称为描述符,由这个类产生的实例进行属性的调用/赋值/删除,并不会触发这三个方法
# f1=Foo()
# f1.name='egon'
# f1.name
# del f1.name
'''



'''
#描述符Str
class Str:
    def __get__(self, instance, owner):
        print('Str调用')
    def __set__(self, instance, value):
        print('Str设置...')
    def __delete__(self, instance):
        print('Str删除...')

#描述符Int
class Int:

    def __get__(self, instance, owner):
        print('Int调用')

    def __set__(self, instance, value):
        print('Int设置...')

    def __delete__(self, instance):
        print('Int删除...')

class People:
    name = Str()
    age = Int()

    def __init__(self,name,age): #name被Str类代理,age被Int类代理,
        self.name = name
        self.age = age

#何地？：定义成另外一个类的类属性

#何时？：且看下列演示

p1=People('alex',18)

#描述符Str的使用
p1.name
p1.name='egon'
del p1.name

#描述符Int的使用
p1.age
p1.age=18
del p1.age

#我们来瞅瞅到底发生了什么
print(p1.__dict__)
print(People.__dict__)

#补充
print(type(p1))
print(type(p1) == People) #type(obj)其实是查看obj是由哪个类实例化来的
print(type(p1).__dict__ == People.__dict__)

#那既然描述符被定义成了一个类属性,直接通过类名也一定可以调用吧,没错
People.name #恩,调用类属性name,本质就是在调用描述符Str,触发了__get__()
'''



'''
# 数据描述符：至少有__get__()和__set__()
class Foo:

    def __get__(self, instance, owner):
        print('触发get')

    def __set__(self, instance, value):
        print('触发set')

    def __delete__(self, instance):
        print('触发del')

class Bar:
    x = Foo()


# 要严格遵循该优先级,优先级由高到底分别是
# 1.类属性
# 2.数据描述符
# 3.实例属性
# 4.非数据描述符
# 5.找不到的属性触发__getattr__()

# print(Bar.x)
# print(Bar.__dict__)
# Bar.x = 1 # 因为优先级，覆盖了x = Foo()
# print(Bar.__dict__)
# print(Bar.x)

b1 = Bar()
b1.x # 触发get
b1.x = 1 # 触发set
del b1.x # 触发del
'''



'''
# 上下文管理协议

class Open:
    def __init__(self, name):
        self.name = name

    def __enter__(self): # with Open运行时触发
        print("执行enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb): # with Open运行结束触发
        print("执行exit")
        print(exc_type) # 异常的类 <class 'NameError'>
        print(exc_val) # 异常的值 name 'fhajfgahjfgahjgfhj' is not defined
        print(exc_tb) # 异常的追踪信息 <traceback object at 0x000001F1C2FA0908>
        return True # 存在return True时，不会报错，但依然会进行异常步骤，而且随后还会去运行with Open以外下面的代码

with Open("a.txt") as f: # enter返回的值会赋值给f
    print(f)
    print(fhajfgahjfgahjgfhj) # 存在异常直接触发exit，并输出错误信息
    print(f.name)
    print("111111111111111")
    print("222222222222222")

print("------------->")


# 用途或者说好处：
# 
# 1.使用with语句的目的就是把代码块放入with中执行，with结束后，自动完成清理工作，无须手动干预
# 2.在需要管理一些资源比如文件，网络连接和锁的编程环境中，可以在__exit__中定制自动释放资源的机制，你无须再去关系这个问题，这将大有用处
'''



'''
# 描述符的应用

class Typed:
    def __init__(self, key, expected_type):
        self.key = key
        self.expected_type = expected_type

    def __get__(self, instance, owner): # instance接收的就是实例
        print("get")
        # print("instance", instance)
        # print("owner", owner)
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print("set")
        print("instance", instance)
        print("value", value)
        if not isinstance(value, self.expected_type): # 判断传入的是否是字符串
            # print("你传入的类型不是字符串，错误")
            # return
            raise TypeError("%s 传入的类型不是 %s" % (self.key, self.expected_type))
        instance.__dict__[self.key] = value # 将你想赋予的值写入实例化对象的字典里

    def __delete__(self, instance):
        print("delete")
        # print("instance", instance)
        instance.__dict__.pop(self.key)


class People:
    name = Typed("name", str) # 让代理去完成操作
    age = Typed("age", int)
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


p1 = People("lhf", 18, 33.3)
print(p1.__dict__)
# p2 = People(213, 15, 56)
# print(p2.__dict__)
# print(p1.name)
# p1.name = "alex"
# print(p1.__dict__)
# del p1.name
# print(p1.__dict__)
'''



# 类的装饰器
'''
def deco(func):
    print("========")
    return func

# @deco # calc = deco(calc)
# def calc():
#     print("calc")
# calc.x = 1
# # calc.y = 2
# calc()
# print(calc.__dict__)

# @deco # Foo = deco(Foo)
# class Foo:
#     pass
#
# f1 = Foo()
# print(f1)
'''


'''
def deco(obj):
    print("==========", obj)
    obj.x = 1
    obj.y = 2
    obj.z = 3
    return obj

# 一切皆对象
@deco
class Foo: # Foo = deco(Foo) 以后调用Foo就是被deco处理过的Foo
    pass

print(Foo.__dict__)
'''



'''
def typed(**kwargs):
    def deco(obj):
        print("--->", kwargs)
        print("类名---》", obj)
        for k, v in kwargs.items():
            setattr(obj, k, v)
        return obj
    return deco

@typed(x = 1, y = 2, z = 3) # @1.typed(x = 1, y = 2, z = 3)--->返回deco      2.@deco---->Foo = deco(Foo)
class Foo:
    pass

@typed(name = "alex")
class Bar:
    pass

print(Foo.__dict__)
print(Bar.name)
'''



'''
class Typed:
    def __init__(self, key, expected_type):
        self.key = key
        self.expected_type = expected_type

    def __get__(self, instance, owner): # instance接收的就是实例
        print("get")
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print("set")
        if not isinstance(value, self.expected_type): # 判断传入的是否是字符串
            raise TypeError("%s 传入的类型不是 %s" % (self.key, self.expected_type))
        instance.__dict__[self.key] = value # 将你想赋予的值写入实例化对象的字典里

    def __delete__(self, instance):
        print("delete")
        # print("instance", instance)
        instance.__dict__.pop(self.key)


def deco(**kwargs):
    def wrapper(obj):
        for k, v in kwargs.items(): # (("name", str),("age", int)....)
            v = Typed(k, v) # name = Typed("name", str)
            setattr(obj, k, v)
        return obj
    return wrapper


@deco(name=str, age=int, salary=float, gender=str)
class People:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender


p1 = People("lhf", 18, 33.3, "male")
print(People.__dict__)
'''



'''
# 利用描述符自定制property

class lazyproperty:
    def __init__(self, func):
        print("=========>", func)
        self.func = func

    def __get__(self, instance, owner):
        print(self)
        if instance is None:
            return self
        print(instance) # 类调用时，instance为None
        print(owner)
        res = self.func(instance)
        setattr(instance, self.func.__name__, res)
        return res

class Room:
    def __init__(self, name, width, length):
        self.name = name
        self.width = width
        self.length = length

    # @property # area = property(area)
    @lazyproperty # area = lazyproperty(area)
    def area(self):
        return self.width * self.length

# 实例调用
r1 = Room("厕所", 1, 1)
print(r1.area)
print(r1.__dict__)
print(r1.area) # 要用非数据描述符，这时实例字典里已经有了，所以直接从其里面找
print(r1.area)
print(r1.area)
# 类调用 没什么用，直接返回的就是对象
# print(Room.area)
'''



# property补充
'''
class Foo:
    @property # 没有他，其他就不存在 @AAA.setter @AAA.deleter
    def AAA(self):
        print("get的时候运行我")

    @AAA.setter # 设置AAA这个属性的时候触发他下面的方法
    def AAA(self, value):
        print("set的时候运行我", value)

    @AAA.deleter
    def AAA(self):
        print("delete的时候运行我")


f1 = Foo()
f1.AAA
f1.AAA = "aaa" # 赋值操作触发@AAA.setter
del f1.AAA # 删除操作触发@AAA.deleter


# 另一种方式
class Foo:

    def get_AAA(self):
        print("get的时候运行我")

    def set_AAA(self, value):
        print("set的时候运行我", value)

    def del_AAA(self):
        print("delete的时候运行我")

    AAA = property(get_AAA, set_AAA, del_AAA)

f1 = Foo()
f1.AAA
f1.AAA = "aaa" # 赋值操作触发@AAA.setter
del f1.AAA # 删除操作触发@AAA.deleter
'''



'''
class Goods:

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


obj = Goods()
print(obj.price)         # 获取商品价格
obj.price = 200   # 修改商品原价
print(obj.price)
del obj.price     # 删除商品原价
'''



'''
class Foo:
    pass

f1 = Foo()
print(type(f1))
print(type(Foo)) # 类的类就是type

# 元类：类的类，是类的模板
# 元类的实例为类，正如类的实例为对象（f1对象是Foo类的一个实例，Foo类是type类的一个实例）
'''


'''
class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

print(Foo)
print(Foo.__dict__)



#  元类创建类的方式
def __init__(self, name, age):
    self.name = name
    self.age = age

def func(self):
    print("func")

FFo = type("FFo", (object,), {"x": 1, "__init__": __init__, "func": func})
print(FFo)
print(FFo.__dict__)

f1 = FFo("alex", 18)
print(f1.name)
f1.func()
'''


# 自定制元类
'''
class Mytype(type): # 指定自己的元类是type，当然默认就为type type("Foo", (object,),{})
    def __init__(self, a, b, c):
        print("元类的构造函数执行")
        # print(a)
        # print(b)
        # print(c)

    def __call__(self, *args, **kwargs):
        # print("========>")
        # print(self) # self为Foo
        # print(*args, **kwargs)
        obj = object.__new__(self) # 创建一个新的对象 object.__new__(Foo),这一步就是来产生f1的
        self.__init__(obj, *args, **kwargs) # Foo.__init__() 为f1封装属性
        return obj # 赋值给f1，此时f1已经完成属性封装

class Foo(metaclass=Mytype): # Foo = Mytype(4个参数self, "Foo", (), {})--> 触发元类__init__
    def __init__(self, name):
        self.name = name # f1.name = name

print(Foo)
f1 = Foo("alex") # Foo()触发__call__
print(f1)
'''
