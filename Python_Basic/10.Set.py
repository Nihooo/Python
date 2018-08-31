# 集合 1.不同元素组成 2.无序 3.集合中元素必须是不可变类型（数字，字符串，元组）

# s = {1, 'as', 68, 2, 3, 'bang', 1, 2, 2}  # 自动去除重复元素
# print(s, type(s))

# s = set("hello")
# print(s)

# s = set(['alex', 'alex', 'sb'])
# print(s)

# 集合的内置方法
'''
s = {1, 2, 3, 4, 5, 6}
s.add('s') # 添加一个元素
s.add('3')
print(s)

s1 = s.copy() # 拷贝
print(s1)

s.clear() # 清空
print(s)
'''

'''
s = {'sb', 1, 2, 3, 4, 5, 6}
# v = s.pop() # 随机删除
# print(s, v)
# s.remove('sb') # 指定删除，不存在时会报错
# print(s)
s.discard('sb') #指定删除，不存在时不会报错
s.discard('bbbb')
print(s)
'''

'''
python_l = ['alex', 'eric', 'rain']
linux_l = ['alex', 'rain', 'sb']

p_s = set(python_l)
l_s = set(linux_l)

print(p_s, l_s)

# 求交集
print(p_s.intersection(l_s))
print(p_s & l_s)
p_s.intersection_update(l_s) # 等于 p_s = p_s & l_s
print(p_s)

# 求并集
print(p_s.union(l_s))
print(p_s | l_s)

# 差集(存在于前不存在于后的元素)
print('差集', p_s - l_s)
print('差集', l_s - p_s)
print(p_s.difference(l_s))
p_s.difference_update(l_s) # 等于 p_s = p_s - l_s
print(p_s)

# 交叉补集（先合到一块，再减去都有的部分）
print(p_s.symmetric_difference(l_s))
print('交叉补集', p_s^l_s)
'''

'''
s1 = {1, 2}
s2 = {3, 5}
print(s1.isdisjoint(s2)) # 如果两个集合没有共同的元素，返回True，有则返回False
'''

'''
s1 = {1, 2}
s2 = {1, 2, 3}
print(s1.issubset(s2)) # s1里的元素是否全在s2里
print(s2.issuperset(s1)) # s1里的元素是否全在s2里
print(s1.issuperset(s2))  # s2里的元素是否全在s1里
'''

'''
s1 = {1, 2}
s2 = {1, 2, 3}
# s1.update(s2) # 更新多个值
s1.update([3, 4, 5])
print(s1)
'''

# 集合可增加可删除，但不可修改

# 定义不可变集合
# s = frozenset('hello')
# print(s)

# 去重但会改变列表顺序
# names = ['alex', 'alex', 'wupeiqi']
# s = set(names)
# names = list(s)
# print(names)
