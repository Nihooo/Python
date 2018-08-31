# list类
# 中括号括起来
# ，分割每个元素
# 列表中的元素可以是 数字， 字符串， 列表， 布尔值。。。所有的都能放进去
# “集合”，内部放置任何东西
# li = [1, 2, 5, 'alex', ['政府', '日期'], 'tom'] # 通过list类创建的对象li

'''
li = [1, 2, 5, 'alex', ['政府', '日期'], 'tom']
print(li[3]) # 索引
print(li[2:5]) # 切片
for item in li:
    print(item)
'''

'''
# 列表元素可以被修改
li = [1, 2, 5, 'alex', ['政府', '日期'], 'tom']

li[2] = [112, 25, 36]
print(li)
li[1:3] = [12, 9]
print(li)

# 删除
del li[2]
print(li)
del li[2:4]
print(li)

# in 操作
v = 12 in li
print(v)
'''

'''
li = [1, 5, 48, ['郭德纲', ['19', 10], 'red'], 'alex', True]
print(li[3][1][0])
print(li[3][1][0][1])
'''

'''
# 字符串转列表，字符串中的每个字符为一个单位 for循环
s = 'ggegehsgdnfhjthdfsa'
new_li = list(s)
print(new_li)

print(list(map(lambda x: x, s)))
'''

'''
# 列表转字符串需要自己写一个for循环：既有数字又有字符串
li = [11, 22, '123', 'alex']
s = ""
for i in li:
    s += str(i)
print(s)
'''

'''
#列表中只有字符串用join
li = ['123', 'alex']
r = "".join(li)
print(r)
'''

# list类中提供的方法
'''
li = [11, 22, 33, 44] # 这叫li对象调用append方法
li.append(5) # 在原来值最后追加
li.append([111, 222, 333])
print(li)
'''

'''
li = [11, 22, 33, 44]
li.clear() # 清空列表
print(li)
'''

'''
li = [11, 22, 33, 44]
v = li.copy() # 拷贝，浅拷贝
print(v)
'''

'''
li = [11, 22, 33, 44, 22]
v = li.count(22) # 计算元素出现的次数，需加参数
print(v)
'''

'''
li = [11, 22, 33, 44]
li1 = [11, 22, 33, 44]
li2 = [11, 22, 33, 44]
li.extend([9898, '德布拉']) # 扩展原列表，参数为可迭代对象，不会将[9898, '德布拉']的列表加入
li2.extend('alex')
li1.append([9898, '德布拉']) # 这个append是直接在列表里加列表
print(li)
print(li1)
print(li2)
'''

'''
li = [11, 22, 33, 44, 22]
v = li.index(22) # 根据值获取当前索引位置（从左往右）
v1 = li.index(22, 2, ) # 2为第二个22的位置
print(v)
print(v1)
'''

'''
li = [11, 22, 33, 44, 22]
li.insert(2, 99) # 指定索引位置插入元素
print(li)
'''

'''
li = [11, 22, 33, 44, 22]
li1 = [11, 22, 33, 44, 22]
v = li.pop() # 默认删除最后一个元素，并且可以获取到删除的值
v1 = li1.pop(2) #也可指定索引
print(li)
print(v)
print(li1)
print(v1)
'''

'''
li = [11, 22, 33, 44, 22]
li.remove(22) # 删除列表中的指定值，从左往右的第一个
print(li)
# PS: pop remove del li[0] del[2:5] clear 都有删除功能
'''

'''
li = [11, 22, 33, 44, 22]
li.reverse() # 将当前列表进行反转
print(li)
'''

'''
li = [11, 22, 88, 44, 22]
li1 = [11, 22, 88, 44, 22]
li.sort() # 列表元素排序，默认从小到大，只能相同类型
li1.sort(reverse=True) # 从大到小
print(li)
print(li1)
'''
