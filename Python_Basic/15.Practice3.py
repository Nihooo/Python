# 1.列举布尔值为false的值 0 None "" [] () {}


# 2.求一个范围内能被3和7整除的数，返回个数和他们的和
'''
def func(start, end):
    num = 0
    sum = 0
    for i in range(start, end):
        if i % 3 == 0 and i % 7 ==0:
            num += 1
            sum += i
    return num, sum

res = func(10, 100)
print(res, type(res))
'''


# 3.函数传递参数时。是引用还是复制？ 引用
'''
name = 'alex'
def show():
    print(id(name))
print(id(name))
show()
'''


# 4.使用set集合获取两个列表l1 = [11, 22, 33]，l2 = [22, 33, 44]中相同的元素集合
'''
l1 = [11, 22, 33]
l2 = [22, 33, 44]
s1 = set(l1)
s2 = set(l2)
res = s1.intersection(s2)
print(res)
'''


# 5.定义函数统计一个字符串中大写字母、小写字母、数字的个数，并以字典为结果返回给调用者
'''
def str_analyse(s):
    A = 0
    a = 0
    n = 0
    for i in s:
        get_str = ord(i)
        if get_str > 64 and get_str < 91:
            A += 1
        elif get_str > 96 and get_str < 123:
            a += 1
        elif i.isdecimal() == True:
            n += 1
        else:
            continue
    return dict(zip(('A', 'a', 'n'), (A, a, n)))

res = str_analyse('FAgeg_e87va')

print(res)
'''


# 6、简述对象和类的关系
# 如果值是某类型，那这个值就是这个类的对象

# 7、将字符串“老男人”转换成utf-8编码的字节类型
# name = '老男人'.encode('utf-8')
# print(name)
#
# name = bytes('老男孩', 'utf-8')


# 8、利用zip函数实现 s = "alex_is_good_guy"
# l1 = ['alex', 22, 33, 44, 55]
# l2 = ['is', 22, 33, 44, 55]
# l3 = ['good', 22, 33, 44, 55]
# l4 = ['guy', 22, 33, 44, 55]
# # res = zip(l1, l2, l3, l4)
# # tu_res = list(res)[0]
# # s = "_".join(tu_res)
# # print(s)
#
# print("_".join(list(zip(l1, l2, l3, l4))[0]))


# 9、利用递归实现1*2*3*4*5*6*7=5040
'''
def calc(n, sum=1):
    if n == 8:
        return sum

    sum *= n
    a = calc(n+1, sum)
    return a

res = calc(1)
print(res)
'''

'''
def func(n):
    if n == 1:
        return 1
    return n*func(n-1)
res = func(7)
print(res)
'''
'''
from functools import reduce
print(reduce(lambda x, y: x*y, range(1, 8)))
'''


# 同时完成两个文件的读写操作
# with open('a', 'r')as f, open('b', 'w') as y:
#     y = y.write(f.read())


# 猴子吃桃，第一天吃了一半加一个，第二天吃了一半加一个，到第10天还剩1个，问总共有几个桃
# sum = 1
# for i in range(1, 10):
#     sum = (sum+1) * 2
# print(sum)
#
# s = 1
# func = lambda x: (x+1)*2
# for i in range(9):
#     s = func(s)
# print(s)
