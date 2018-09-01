# pickle模块 与json使用方式完全一样，dumps时，json处理成json字符串，pickle处理成字节
# pickle更全面，但一般用json就够了

import pickle

'''
dic = {'name': 'alvin', 'age': 23, 'sex': 'male'}
# 序列化
p_dic = pickle.dumps(dic) # class 'bytes'

print(p_dic, type(p_dic))

f = open('pickle.txt', 'wb')
f.write(p_dic)

f_read = open("pickle.txt", "rb")
'''

# 反序列化
data = pickle.loads(f_read.read())
print(data["name"], type(data))
