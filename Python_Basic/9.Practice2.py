'''
# 有1, 2, 3, 4, 5, 6, 7, 8数字，能组成多少种不同且无重复数字的两位数字
li = [1, 2, 3, 4, 5, 6, 7, 8]
num = 0
numli = []
count = 0
for i in li:
    for item in li:
        if i != item:
            num = 10 * i + item
            count += 1
            numli.append(num)
        else:
            continue
print(numli)
print(count)
'''

'''
# 99乘法表
num_end = 0
out_format = "{0} * {1} = {2}"
for i in range(1, 10):
    for item in range(1, i+1):
        num_end = i * item
        v = out_format.format(item, i, num_end)
        if i == item:
            print(v)
        else:
            print(v + '\t', end= '')
'''

'''
# 公鸡5文钱一只，母鸡3文钱一只，小鸡3只1文钱，用100文钱买100只公鸡，母鸡，小鸡都必须要有，问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱
# a + b + c = 100
# 5(100-b-c)+3(100-a-c)+(100-a-b)/3 = 100
# a 公鸡 b 母鸡 
for a in range(1, 100//5):
    for b in range(1, 100//3):
        if (100-a-b) % 3 == 0 and 5*a + 3*b + (100-a-b)/3 == 100:
            print(a, b, 100-a-b)
        else:
            continue
'''

'''
# 利用下划线将列表的每一个元素拼接成字符串，li = ['alex','eric','rain']
li = ['alex', 'eric', 'rain']
v = "_".join(li)
print(v)
print(type(v))
'''

'''
tu = ('alex', 'eric', 'rain')
print(len(tu))
print(tu[1])
print(tu[0:2])
for i in tu:
    print(i)
for i in range(len(tu)):
    print(i)
for i, v in enumerate(tu, 10):
    print(i, v)
'''

'''
tu = ("alex", [11, 22,{"k1": "v1", "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])
tu[1][2]['k2'].append('Seven')
print(tu)
'''

'''
#找到列表中任意两个元素相加能够等于9的元素集合
nums = [2, 7, 11, 15, 1, 8, 7]
empty_list = []
for i in nums:
    for j in nums:
        if i+j == 9:
            empty_list.append((i, j))
print(empty_list)

#找到列表中任意两个元素相加能够等于9的元素索引的集合
nums = [2, 7, 11, 15, 1, 8, 7]
empty_list = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] + nums[j] == 9:
            empty_list.append((i, j))
print(empty_list)
'''

'''
li = ['alex', 'eric', 'rain']
# print(len(li))
# li.append('seven')
# print(li)
# li.insert(0, 'Tony')
# print(li)
# li.insert(1, 'Kelly')
# print(li)
# li.remove('eric')
# print(li)
# v = li.pop(1)
# print(v, li)
# del li[2]
# print(li)
# del li[1:3]
print(li)
li.reverse()
print(li)
for i in range(len(li)):
    print(i)
for l, n in enumerate(li, 100):
    print(l, n)
for i in li:
    print(i)
'''

'''
# 用列表
page = input("请输入要查看的页码：")
if page.isdecimal():
    page = int(page)
    normal_format = "alex-{0}    alex{0}@live.com    pwd{0}"
    all_list = []
    for i in range(302):
        all_list.append(normal_format.format(i))
    print(all_list[(page-1)*10+1:(page-1)*10+11])
else:
    print("输入内容格式错误")
'''

'''
#用字典
user_list = []
for i in range(1, 302):
    temp = {'name': 'alex' + str(i), 'email': 'alex@lve.com' + str(i), 'pwd': 'pwd' + str(i)}
    user_list.append(temp)

while True:
    s = input('请输入页码:')
    s = int(s)
    start = (s-1) * 10
    end = s * 10
    result = user_list[start:end]
    for item in result:
        print(item)
'''
