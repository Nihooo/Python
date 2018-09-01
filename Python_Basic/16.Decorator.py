# 装饰器：本质就是函数，为其他函数

# 原则：1.不修改被修饰函数的源代码
#       2.不修改被修饰函数的调用方法添加附加功能

# 装饰器 = 高阶函数 + 函数嵌套 + 闭包

# 高阶函数：1.函数接收的参数是一个函数名   或
#           2.函数的返回值是一个函数名


# 不修改foo的源代码
# 不修改foo的调用方式  本来通过foo()去运行，现在通过timer(foo)来调用了

# 单独的高阶函数无法实现计算一个函数运行时间的功能
'''
import time
def foo():
    time.sleep(2)
    print('from foo')

# 多运行了一次foo
def timer(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print('函数运行时间是 %s' % (end_time-start_time))
    return func

foo = timer(foo)
foo()
'''


# 函数嵌套： 函数里def另一个函数

# def father(name):
#     print('from father %s', name)
#     def son():
#         print('from son')
#     print(locals()) # 打印当前层的局部变量name和son
#     son()
# father('alex')


# 闭包 每一层都有各自的变量，当需要使用时，优先找自己这层的，再去找上一层，这样层层递进，直到找到
# def father(name):
#     def son():
#         def grandson():
#             print('我的爷爷是 %s' % name)
#         grandson()
#     son()
# father('file')


# 装饰器的架子
'''
import time

def timer(func): # func = foo
    def wrapper():
        print(func)
        start_time = time.time()
        result = func() # 就是在运行foo（）
        end_time = time.time()
        print('运行时间是 %s' % (end_time-start_time))
        return result
    return wrapper

@timer # 就相当于foo = timer(foo)
def foo():
    time.sleep(2)
    print('foo函数运行完毕')
    return '这是foo的返回值'

# res = timer(foo) # 返回的是wrapper地址
# res() # 执行wrapper（）

# foo = timer(foo) # 返回的是wrapper地址
# foo()

# @timer # 就相当于foo = timer(foo)

res = foo() # 就是在运行wrapper
print(res)
'''


'''
import time


def timer(func): # func = foo
    def wrapper(name, age):
        print(func)
        start_time = time.time()
        result = func(name, age) # 就是在运行foo（）
        end_time = time.time()
        print('运行时间是 %s' % (end_time-start_time))
        return result
    return wrapper

@timer # 就相当于foo = timer(foo)
def foo(name, age):
    time.sleep(2)
    print('foo函数运行完毕, 名字是 %s ，年龄是 %s' % (name, age))
    return '这是foo的返回值'

res = foo('alex', 54) # 就是在运行wrapper
print(res)
'''


'''
import time

def timer(func): # func = foo
    def wrapper(*args, **kwargs):
        print(func)
        start_time = time.time()
        result = func(*args, **kwargs) # 就是在运行foo（）
        end_time = time.time()
        print('运行时间是 %s' % (end_time-start_time))
        return result
    return wrapper

@timer # 就相当于foo = timer(foo)
def foo(name, age):
    time.sleep(2)
    print('foo函数运行完毕, 名字是 %s ，年龄是 %s' % (name, age))
    return '这是foo的返回值'

@timer
def foo1(name, age, gender):
    time.sleep(2)
    print('foo1函数运行完毕, 名字是 %s ，年龄是 %s , 性别是 %s' % (name, age, gender))
    return '这是foo的返回值'

res = foo('alex', 54) # 就是在运行wrapper
foo1('lhf', 99, 'male')
'''


'''
a, b, c = (1, 2, 3)

def func2(name, age, gender):  # func2(*('alex',18,'male'),**{})
    # name,age,gender=('alex',18,'male') 一一对应
    print(name)
    print(age)
    print(gender)

def func1(*args, **kwargs):
    func2(*args, ** kwargs) # args=元组('alex',18,'male')   kwargs={}

# func1('alex', 18, 'male', 'x', 'y') # 会报错，要一一对应
func1('alex', 18, 'male')
'''


'''
# 获取开头、最后的前几个值
l = [8, 5, 10, 9, 1, 3, 4, 2, 5, 7, 9, 14, 21, 31]

a, *_, b = l
print(a, b)

a, b, *_, c, d = l
print(a, b, c, d)
'''


# 换值，不用定义另一个变量
# a = 1
# b = 5
# a, b = b, a
# print(a, b)


# 验证功能装饰器

# 用户信息
user_list = [
    {'name': 'alex', 'passwd': '123'},
    {'name': 'lhf', 'passwd': '12345'},
    {'name': 'wupeiqi', 'passwd': '54321'},
    {'name': 'bang', 'passwd': '321'}
]

# 当前用户状态
current_dict = {'name': None, 'login': False}

def auth(auth_type = ''):
    def auth_func(func):
        def wrapper(*args, **kwargs):
            print('认证类型是%s' % auth_type)
            if auth_type == 'filedb':
                if current_dict['name'] and current_dict['login']:
                    res = func(*args, **kwargs)
                    return res
                username = input('用户名:').strip()
                passwd = input('密码:').strip()
                for i in user_list:
                    if username == i['name'] and passwd == i['passwd']:
                        current_dict['name'] = username
                        current_dict['login'] = True
                        res = func(*args, **kwargs)
                        return res
                else:
                    print('用户名或密码错误')
            elif auth_type == 'ldap':
                print('鬼才特么会玩')
            else:
                print('鬼才知道你用的是什么类型')

        return wrapper
    return auth_func

@auth(auth_type='filedb') # auth_func = auth(auth_type='filedb')--->@auth_func 附加了一个auth_type
def index():
    print('欢迎来到京东主页')

@auth(auth_type='ldap')
def home(name):
    print('欢迎回家%s' % name)

@auth(auth_type='ssss')
def shopping_car(name):
    print('%s的购物车里有[%s, %s, %s]' % (name, 'alex', 'lhf', 'wupeiqi'))

# print('before---->%s' % current_dict)
index()
# print('current---->%s' % current_dict)
home('产品经理')
shopping_car('产品经理')
