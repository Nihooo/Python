# random模块
import random

ret = random.random() # 随机生成0-1的浮点数
print(ret)

print(random.randint(1, 3)) # 随机生产1，2，3中的一个

print(random.randrange(1, 3)) # 随机生产1，2中的一个

print(random.choice([11, 22, 33, 44, 55])) # 随机生成一个序列里的数

print(random.sample([11, 22, 33, 44, 55], 2)) # 随机生成一个序列里的两个数

print(random.uniform(1, 3)) # 随机生成一个任意范围的浮点型

item = [1, 3, 5, 7, 9]
random.shuffle(item) # 打乱一个序列里的值
print(item)


# 随机生成验证码
'''
def v_code():
    ret = ''
    for i in range(5):
        num = str(random.randint(0, 9))
        while True:
            alf = random.randint(65, 122) # 65-122 从大到小 91-96不算
            if alf > 90 and alf < 97:
                continue
            else:
                break
        alf = chr(alf)
        value_i = random.choice([num, alf])
        ret += value_i
    return ret

res = v_code()
print(res)
'''
