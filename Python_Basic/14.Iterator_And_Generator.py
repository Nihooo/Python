# 迭代器协议：对象必须提供一个next方法，执行该方法要么返回\
# 迭代中的下一项，要么就引起一个Stoplteration异常，以终止迭代（只能往后不能往前）

# 可迭代对象：实现了迭代器协议的对象

# （字符串，列表，元组，字典，集合，文件对象）这些都不是可迭代对象\
# ，只不过在for循环时，调用了他们内部的__iter__方法，把他们变成了可迭代对象\
# 然后for循环调用可迭代对象的__next__方法取值，而且for循环会捕捉Stoplteration以终止迭代

# for循环就是遵循迭代器协议


'''
x = 'hello'
# print(x)
iter_test = x.__iter__() # 遵循迭代器协议，生成可迭代对象，一定有next方法

print(iter_test)
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__())
print(iter_test.__next__()) # StopIteration

# print(next(iter_test)) # 就是函数next()-----》iter_test.__next__()
# print(next(iter_test))
# print(next(iter_test))
# print(next(iter_test))
# print(next(iter_test))
'''


# l = [1, 2, 3]
# for i in l: # i_l = l.__iter__()  i_l.__next__()
#     print(i)

# dic = {'a': 1, 'b': 2}
# iter_d = dic.__iter__()
# print(iter_d.__next__()) # 会得到字典的key值

# f = open('linux', 'r+', encoding='utf-8')
# iter_f = f.__iter__() # 要一次用一次next
# print(iter_f.__next__(), end='')
# print(iter_f.__next__(), end='')

# for循环模拟
# l = [1, 2, 3, 4, 5]
# iterator_l = l.__iter__()
# while True:
#     try:
#         print(iterator_l.__next__())
#     except StopIteration: # 捕捉异常
#         # print('迭代完毕，循环终止')
#         break


# 生成器：可以理解为一种数据类型，这种数据类型自动实现了迭代器协议，可直接调用__next__方法

# 生成器的表现形式:1.生成器函数（使用yield语句而不是return语句）
# 2.生成器表达式

# 生成器的第一种形式：生成器函数
# def func():
#     yield 1
#     yield 2
#     yield 3
#
# g = func()
# print('来自函数', g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# 三元表达式
# # name = 'alex'
# name = 'lhf'
# res = 'sb' if name == 'alex' else 'badman'
# print(res)


# 列表解析
# egg_list = []  # 平常写法
# for i in range(1, 11):
#     egg_list.append('鸡蛋%s' % i)
# print(egg_list)

# l = ['鸡蛋%s' % i for i in range(1, 11)]
# l1 = ['鸡蛋%s' % i for i in range(1, 11) if i > 5]
# # l2 = ['鸡蛋%s' % i for i in range(1, 11) if i > 5 else i] # 会报错，最高三元，没有四元
# print(l)
# print(l1)


# 生成器的第二种形式：生成器表达式
# laomuji = ('鸡蛋%s' % i for i in range(1, 11))
# print(laomuji)
# print(laomuji.__next__())
# print(laomuji.__next__())
# print(laomuji.__next__())
# print(next(laomuji))
# print(next(laomuji))


# print(sum([1,2,3,4.........1000000000000000]))  # 会将整个列表放入内存空间中，占用大量内存空间
# print(sum(i for i in range(1000000000000000)))  # 生成器一个一个进行


# def func():
#     print('开始打人了')
#     print('开始打人了')
#     print('开始打alex')
#     yield 'alex'
#     print('开始打lhf')
#     yield 'lhf'
#     print('开始打wupeiqi')
#     yield 'wupeiqi'
#     yield 4
#
# res = func()
# print(res)
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())


# def product_baozi():
#     for i in range(1, 101):
#         print('正在生产包子%s' % i)
#         yield '一屉包子%s' % i
#         print('开始卖包子%s' % i)
#
# product_b = product_baozi()
#
# for baozi in product_b:
#     print(baozi)

# baozi1 = product_b.__next__()
# print(baozi1)
# baozi2 = product_b.__next__()
# print(baozi2)


# def get_info():
#     with open('人口普查', 'r', encoding='utf-8') as f:
#         for i in f:
#             yield i
#
# g = get_info()
# info_list = []
# sum = 0
# for i in g:
#     info_dict = eval(i)
#     info_list.append(info_dict)
#     sum += info_dict['population']
#
# # all_p = sum(eval(i)['population'] for i in g)
#
# for i in range(len(info_list)):
#     name = info_list[i]['name']
#     p_num = info_list[i]['population']
#     print('%s:%.2f%%' % (name, (p_num/sum)*100))


# 触发生成器运行的第三种方法send

# yield 3 相当于return控制的是函数的返回值
# x = yield 的另一个特性是接收send传过来的值，赋值给x


# def func():
#     print('开始啦')
#     first = yield 1 # return 1  first = None
#     print('第一次', first)
#     yield 2
#     print('第二次')
#
#
# f = func()
# res = f.__next__()
# print(res)
# res = f.send('もしもし')
# print(res)


# 生产者消费者模型，生产者生产东西，消费者消费东西
# import time
#
# def consumer(name):
#     print('我是【%s】，我准备开始吃包子了' % name)
#     while True:
#         baozi = yield
#         time.sleep(5)
#         print('%s 很开心地把【%s】' % (name, baozi))
#
# def product_baozi():
#     c1 = consumer('alex')
#     c2 = consumer('lhf')
#     c1.__next__()
#     c2.__next__()
#     for i in range(1, 11):
#         time.sleep(5)
#         c1.send('包子%s' % i)
#         c2.send('包子%s' % i)
#
# product_baozi()


# 生成器只能遍历一次，然后就死了
# def func():
#     for i in range(4):
#         yield i
#
# t = func()
#
# t1 = (i for i in t)
# print(t1) # 并没有拿取出t里面的值
# t2 = (i for i in t)
# print(list(t2))
