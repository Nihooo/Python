# 函数定义
# 为什么要用函数 1、避免代码重用 2、保持一致性，易维护 3、可扩展性


'''
def func_test(x):
    y = 2 * x + 1
    return y

v = func_test(5)
print(v)
'''


# 过程：没有返回值的函数
'''
def func_test():
    x = 3
    y = x + 3
    print(x, y)
func_test()
'''


# 返回值数=0，返回None
# 返回值数=1，返回object本身
# 返回值数>1，返回tuple元组


'''
def calc(x, y):  # 函数里x、y为形参，当给他们值时才分配内存空间，运行完就释放掉
    res = x ** y
    return res # 一碰到return函数就结束

a = 2
b = 3
r = calc(a, b)  # a、b为实参
print(r)
'''


'''
# 位置参数必须一一对应，缺一多一都不行
def number_print(x, y, z):
    print(x)
    print(y)
    print(z)

number_print(1, 2, 3)
number_print(x=3, y=1, z=2) # 关键字参数无必须一一对应，缺一多一都不行
#如混合使用，位置参数必须在关键字参数左边
number_print(2, 1, z=5)
# number_print(1, y=2, 3) # 报错
# number_print(1, 3, y=2) # 报错
'''


# def handle(x, type = 'mysql'): # type为默认参数，可不传值
#     print(x)
#     print(type)
#
# handle('hello')
# handle('hello', type='alex')
# handle('hello', 'sqlite')


'''
# 参数组：**字典，*列表
def func1(x, *args):
    print(x)
    print(args)
    # print(args[0])
    print(type(args))

func1(1, 2, 3, 4, 5, 6)
func1(1)
func1(1, [2, 3, 4]) # 元组里的列表
func1(1, *[2, 3, 4]) # 同第一个一样
'''


'''
def func1(x, **kwargs):
    print(x)
    print(kwargs)
    print(type(kwargs))

func1(1, y=2, z=3) # 加入key时，就要用**
'''


'''
def func1(x, *args, **kwargs):
    print(x)
    print(args, args[-1])
    print(kwargs, kwargs['h'])

#func1(1, 1, 2, 3, 4, 5, y=7, z=8, h=9)

func1(1, *[1, 2, 3], **{'y': 1, 'z': 5, 'h': 9})
'''


# 全局变量与局部变量
# 顶头写的变量就是全局变量


'''
name = 'alex' # 全局变量

def change_name():
    name = 'bang' # 局部变量，优先调用局部变量
    print(name)

change_name()
print(name)
'''


'''
name = 'alex'  # 全局变量

def change_name():
    global name  # 修改全局变量，当name被修改时，修改的就是全局

    name = 'bang'  # 局部变量
    print(name)

def confire_name():
    print(name)

confire_name()
change_name()
confire_name()
print(name)
'''


'''
name = ['alex', 'eric']  # 全局变量，列表为可变对象

def change_name():
    name.append('bang') # 无global只能读取不能修改，但可对可变对象进行添加、删除等方法使用
    print(name)

change_name()
'''


# 错误示例
'''
name = ['alex', 'eric']  # 全局变量，列表为可变对象

def change_name():
    name = 'bang' 
    global name
    print(name)
change_name()
'''


# 命名规则：全局变量变量名要大写，局部变量变量名要小写


'''
Name = 'alex'

def one_box():
    name = 'one'
    print(name)
    def two_box():
        name = 'two'
        print(name)
        def three_box():
            name = 'three'
            print(name)
        print(name)
        three_box()

    two_box()
    print(name)

one_box()
'''


'''
name = 'alex'

def one_box():
    name = 'one'
    def two_box():
        global name
        name = 'two'
    two_box()
    print(name) # one_box 的局部变量并没有被修改

print(name)
one_box()
print(name)
'''


'''
name = 'alex'

def one_box():
    name = 'one'
    def two_box():
        nonlocal name # nonlocal 指定上一级的变量
        name = 'two'
    two_box()
    print(name) # one_box 的局部变量就在two_box里被修改

print(name)
one_box()
print(name)
'''


'''
# 函数即变量

def foo():
    print('from foo')
    bar()

def bar():
    print('from bar')

foo()
'''


# 递归特性:调用函数自己
# 1.必须有一个明确的结束条件
# 2.每次进入更深递归时，问题规模都有所减小
# 3.执行效率不高，容易造成内存溢出


'''
def calc(n):
    print(n)
    if int(n / 2) == 0:
        return n
    return calc(int(n / 2))

v = calc(10)
print(v)
'''


'''
person_list = ['alex', 'wupeiqi', 'yuanhao', 'linhaifeng']

def ask_way(person_list):
    print(''.ljust(20, '-'))
    if len(person_list) == 0:
        return '根本没人知道'

    person = person_list.pop(0)
    if person == 'linhaifeng':
        return '%s说：我知道，就在脚下' % person
    print('hi, 美男[%s],敢问路在何方' % person)
    print('%s回答道：我不知道，但念你慧眼识猪，你等着，我帮你问问%s'%(person,person_list[0]))

    v = ask_way(person_list)
    print('%s问的结果是：%s' % (person, v))
    return v

res = ask_way(person_list)
print(res)
'''


'''
def bbb():
    print('in the test1')
def aaa():
    print('in the test')
    return bbb # 返回bbb的内存地址，加个括号就能运行
res = aaa()
print(res())
'''


'''
name = 'alex'
def foo():
    name = 'linhaifeng'
    def bar():
        name = 'wupeiqi'
        print(name)
        def tt():
            print(name)
        return tt
    return bar
# a = foo()  # 可以写成foo()()()
# bar = a()
# tt = bar()
foo()()()
'''


'''
# 匿名函数lambda


def calc(x):
    return x+1

a = calc(10)
print(a)

# 上面的函数可以用匿名函数简写成：

print(lambda  x: x+1)
print(calc)

func = lambda x: x+1 # x为形参，x+1为return的值
b = func(10)
print(b)

name = 'alex'
ch_name = lambda x, y, z: x+'_sb'+y+z
c = ch_name(name, '1', '2')
print(c)

v = lambda x, y, z: [x+1, y+1, z+1] # 元组、列表都可以
s = v(1, 2, 3)
print(s, type(s))
'''


# 编程的方法论：面向过程、面向对象、函数式编程
# 面向过程：将一个整体分成几个步骤或过程，然后一步一步一次进行
# 函数式编程：编程语言定义的函数+数学意义的函数，用编程语言去实现数学函数，比如y=2*x+1用编程语言里的函数来写


# 高阶函数，满足下面条件之一：1.函数接收的参数是一个函数名  2.返回值中包含函数
'''
# 1.把函数当作参数传给另一个函数

def foo(n):
    print(n)

def bar(name):
    print('my name is %s' % name)

foo(bar('alex'))
'''


'''
# 2.返回值中包含函数
def bar():
    print('from bar')
def foo():
    print('from foo')
    return bar()
v = foo()
print(v)
'''


'''
# map函数 处理序列中的每个元素，得到的结果是一个‘列表’（一个可迭代对象，用list转化为列表），该‘列表’元素个数及位置与原来一样

num_l = [1, 2, 10, 5, 3, 7]

def add_one(x):
    return x+1

def reduce_one(x):  # lambda x: x-1
    return x-1

def pf(x):  # lambda x: x**2
    return x**2

def calc(func, array):
    ret = []
    for i in array:
        res = func(i)
        ret.append(res)
    return ret

print(calc(add_one, num_l))

print(calc(lambda x: x+1, num_l))

res = map(lambda x: x+1, num_l)  # map处理的结果为可迭代对象，需要用list将其转化为列表
print('内置函数map', res)
print(list(res))

print('传的是自定义函数', list(map(reduce_one, num_l)))

# map(方法， 数据) 数据为可迭代对象能用for循环的
'''


'''
# filter函数  遍历序列中的每个元素，判断每个得到布尔值，如果为true则留下来

movie_people = ['sb_alex', 'sb_wupeiqi', 'yuanhao', 'sb_linhaifeng']

def sb_show(n):
    return n.startswith('sb')

def sb_back(n):
    return n.endswith('sb')

def move_sb(func, people_list):
    ret = []
    for i in people_list:
        if not func(i):
            ret.append(i)
    return ret

res = move_sb(sb_show, movie_people)
print(res)

a = move_sb(lambda x: x.startswith('sb'), movie_people)
print(a)

print(list(filter(lambda x: x.startswith('sb'), movie_people))) # 会得到有sb的字符串, 放入方法中是否得到true，为true就保留
print(list(filter(lambda x: not x.startswith('sb'), movie_people)))
'''


'''
# reduce函数 处理一个序列，把序列进行合并操作


num_1 = [1, 2, 3, 100]

def mutiply(x, y):
    return x * y

def calc(func, array, init=None):
    if init is None:
        res = array.pop(0)
    else:
        res = init
    for i in array:
        res = func(res, i)

    return res

v = calc(mutiply, num_1, 100)
print(v)

from functools import reduce
print((reduce(lambda x, y: x*y, num_1, 100)))
'''


# 一些内置函数

# print(abs(-9)) # 取绝对值

# print(pow(3, 3)) # 等于3的3次方
# print(pow(3, 3, 2)) # 等于3的3次方然后除2取余

# print(all([1, 2, 's', 'q'])) # 判断序列中的每个元素是否为true，全真就为true
# print(all('hello'))
# print(all('')) # If the iterable is empty, return True.

# print(any([1, 0, ''])) # 有一为真就为真

# print(bin(3)) # 把十进制转换为二进制
# print(hex(12)) # 把十进制转换为十六进制
# print(oct(45)) # 把十进制转换为八进制

# print(bool('')) # 判断bool值
# print(bool(None))
# print(bool(0))

# print(bytes('你好', encoding='utf-8')) # 转化为字节
# print(bytes('你好', encoding='gbk').decode('gbk'))

# print(chr(97)) # 数字转化为ascii字符
# print(ord('a')) # 字符转ascii数字

# print(dir(all)) # 打印某个对象下面有哪些方法

# a, b = divmod(10, 3)
# print(a, b)
# print(divmod(10, 3)) # 10除以3，得商，取余数，用来做分页功能

# dic = {'name': 'alex'}
# dic_str = str(dic)
# print(dic_str, type(dic_str))
#
# v = eval(dic_str)
# print(v, type(v)) # 1.提取字符串中的数据结构
#
# express = '1+2*6-8*(8/4-5)' # 2.把字符串中的数学表达式进行计算
# print(eval(express))

# 可hash的数据类型即不可变数据类型，不可hash的数据类型即可变数据类型
# print(hash('afaf544s4f5sfs54f5s')) # 得到固定长度的值，不能进行反推
# 根据hash值来判断软件是否被更改

# print(help(all)) # 打印相关解释

# print(isinstance(1, int)) # 判断前是不是后面那种类型
# print(isinstance('abc', str))

# name = 'ggggggggggfffff'
# print(globals()) # 输出全局变量
# print(locals()) # 输出局部变量

# zip 拉链方法 只要是序列（字符串，列表，字典,元组）
# print(list(zip(('a', 'b', 'c'), (1, 2, 3)))) # 列表里为一一对应的元组，多一少一都不可
# p = {'name': 'alex', 'age': 21, 'gender': 'none'}
# print(list(zip(p.keys(), p.values())))
# print(list(zip('hello', '12345')))
# print(list(zip(('a', 'b', 'c', 'd', 'e'), '12345')))

# li = [8, 45, 7, 65, 8, 5]
# print(max(li)) # 取最大值
# print(min(li)) # 取最小值

# 比较一个字典中谁的年龄最大，并得到key
# people_age = {
#     'alex_age': 18,
#     'wupeiqi_age': 55,
#     'lhf_age': 100,
#     'bang_age': 26
# }
#
# print(max(zip(people_age.values(), people_age.keys())))

# 字符串比较时是按第一个元素进行依次对比

# l = [
#     (5, 'e'),
#     (1, 'b'),
#     (3, 'a'),
#     (4, 'd')
# ]
# print(max(l))
# ll = ['a10', 'b14', 'c45', 100] # 不同类型之间不能进行比较

# 列表里面的字典比较
# people_age = [
#     {'name': 'alex', 'age': 18},
#     {'name': 'wupeiqi', 'age': 55},
#     {'name': 'lhf', 'age': 100},
#     {'name': 'bang', 'age': 26}
# ]
#
# print(max(people_age, key=lambda dict: dict['age']))

# l = [1, 2, 3, 4]
# print(list(reversed(l))) # 反转
# print(l)

# print(round(3.5)) # 四舍五入

# print(set('hello')) # 转变为集合

# r = 'hello'
# print(r[3:5])
#
# s1 = slice(3, 5) # 定义切片范围
# print(r[s1])


# n = [3, 2, 1, 5, 7]
# print(sorted(n)) # 排序，必须同一类型
#
# people_age = [
#     {'name': 'alex', 'age': 18},
#     {'name': 'wupeiqi', 'age': 55},
#     {'name': 'lhf', 'age': 100},
#     {'name': 'bang', 'age': 26}
# ]
# print(sorted(people_age, key=lambda dic: dic['age']))
#
# people_price = {
#     'alex': 1200,
#     'wupeiqi': 300,
#     'ayuanhao': 900
# }
# print(sorted(people_price, key=lambda key: people_price[key]))
# print(sorted(zip(people_price.values(), people_price.keys())))

# l = [1, 2, 3, 4]
# print(sum(l))
# print(sum(range(5)))

# print(vars(int)) # 以字典形式查看int对象

# import 不能导入字符串
# __import__ 导入的就是字符串类型
# module_name = 'test'
# m = __import__(module_name)
# print(m)
