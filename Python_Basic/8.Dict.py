# 字典 dict，无序

'''
info = {
    'k1': 'v1', # 键值对
    'k2': 'v2'
}
print(info)
'''

'''
# 字典的value可以是任何值
info = {
    'k1': 18,
    'k2': True,
    'k3': [
        11,
        [22],
        (33,),
        {
            'aaa': 'bbb',
            'ccc': 'ddd',
            'www': (11, 22),
        }
    ],
    'k4': (11, 22, 33, 44)
}
print(info)
'''

'''
# 列表、字典不能作为字典的key
info = {
    1: 'dfsd',
    'k1': 'ffaf',
    False: 'AAA', # 布尔值可能会和1和0重复
    (11, 22): 123,
}
print(info)
'''

'''
# 索引找到指定元素
info = {
    'k1': 18,
    'k2': True,
    'k3': [
        11,
        [22],
        (33,),
        {
            'aaa': 'bbb',
            'ccc': 'ddd',
            'www': (11, 22),
        }
    ],
    'k4': (11, 22, 33, 44)
}
print(info['k1'])
print(info['k3'][3]['www'][0])
'''

'''
# 字典支持 del 删除
info = {
    'k1': 18,
    'k2': True,
    'k3': [
        11,
        [22],
        (33,),
        {
            'aaa': 'bbb',
            'ccc': 'ddd',
            'www': (11, 22),
        }
    ],
    'k4': (11, 22, 33, 44)
}
del info['k1']
del info['k3'][3]['aaa']
print(info)
'''

'''
info = {
    'k1': 18,
    'k2': True,
    'k3': [
        11,
        [22],
        (33,),
        {
            'aaa': 'bbb',
            'ccc': 'ddd',
            'www': (11, 22),
        }
    ],
    'k4': (11, 22, 33, 44)
}
# for item in info:
#     print(item, info[item])

# for item in info.keys():
#     print(item)

# for item in info.values():
#     print(item)

# for k, v in info.items():
#     print(k, v)
'''

'''
# 根据序列，创建字典，并指定统一的值
v = dict.fromkeys(['k1', 123, '999'], 123)
print(v)
'''

'''
dic = {
    'k1': 'v1'
}
# v = dic['k11111'] # 无相应key时会报错
# print(v)
v = dic.get('kooooo', 1111111) # 根据key获取值，key不存在时，可以指定默认值，默认为None
print(v)
'''

'''
dic = {
    'k1': 'v1',
    'k2': 'v2'
}
v = dic.pop('k1') # 删除,会得到value值
v1 = dic.pop('kllll', 123) # 当无对应删除内容时，会将123赋予v，不添加参数时会报错
print(dic)
print(v)
print(v1)
# k, v = dic.popitem() #随机删除dic里的内容，并获取删去的key和value
# print(k, v)
'''

'''
dic = {
    'k1': 'v1',
    'k2': 'v2'
}
v = dic.setdefault('k22222', '123')
# 设置值，已存在时，不设置，获取当前key对应的值
# 不存在时，进行设置，获取当前key对应的值
print(dic, v)
'''

'''
dic = {
    'k1': 'v1',
    'k2': 'v2'
}
# dic.update({'k1': '11111', 'k3': 123}) # 更新
dic.update(k1=123, k3=586, k5= 'fafaf')
print(dic)
'''

# keys() values() items() get update

'''
dic = {
    'k1': 'v1',
    'k2': 'v2'
}
v = 'k1' in dic
v1 = 'v1' in dic.values()
print(v)
print(v1)
'''

# 布尔值
# 为假的 None "" () [] {} 0  ==> False

# 可变：列表、字典
# 不可变：字符串、数字、元组

# 访问顺序:
# 顺序访问：字符串、列表、元组
# 映射：字典（查询速度比列表快，但占用内存高）
# 直接访问：数字

# 存放元素个数
# 容器类型：列表、元组、字典
# 原子类型（只能存放一个值）：数字、字符串
