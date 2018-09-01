# %s 能接收任意类型
# msg = 'i am %s my hobby is %s' % ('lhf', 'alex')
# print(msg)

# msg = 'i am %s my hobby is %d' % ('lhf', 20)
# print(msg)

# name = 'alex'
# age = 18
# msg = 'i am %s, age is %d' % (name, age)
# print(msg)

# 打印百分比
# tp1 = "percent %.2f%%" % 99.57845415854742
# print(tp1)

# tp1 = 'i am %(name)s age %(age)d' % {'name': 'alex', 'age': 18}
# print(tp1)

# tp1 = 'i am %(pp).2f' % {'pp': 123.445854}
# print(tp1)

# print('root', 'x', '0', '0', sep=':') # sep=':'表示字符串的拼接，每个字符串用‘:’号拼接，只能用于print时
# a = 'afafaf'
# b = 'ffff'
# print(a, b, sep=':')

# tp1 = 'i am {},age {},{}'.format('seven', 18, 'alex')
# print(tp1)

# tp1 = 'i am {0},age {1},{2}'.format('seven', 18, 'alex')
# tp2 = 'i am {2},age {1},{0}'.format('seven', 18, 'alex')
# tp3 = 'i am {1},age {1},{1}'.format('seven', 18, 'alex')
# print(tp1)
# print(tp2)
# print(tp3)

# tp1 = 'i am {name},age {age},{name}'.format(name='seven', age=18)
# tp2 = 'i am {name},age {age},{name}'.format(**{'name': 'seven', 'age': 18})
# print(tp1)
# print(tp2)

# tp1 = 'i am {:s}, age {:d}, money {:f}'.format('alex', 18, 888888.1)
# print(tp1)

# l = ['alex', 18]
# tp1 = 'i am {:s}, age {:d}'.format(*l)  # 等于format('alex', 18),而不是在里面再嵌套一个列表
# print(tp1)

# tp1 = 'i am {name:s}, age {age:d}'.format(name='alex', age=18)
# print(tp1)

# tp1 = 'numbers: {:b}, {:o}, {:d}, {:x}, {:X}, {:%}'.format(15, 15, 15, 15, 15, 18.857554, 2) # 2为多的
# print(tp1)
