# json模块 用于不同语言间数据交换
import json

dic = {'name': 'alex'}
n = 8
s = 'hello'
ll = [11, 22]

'''
# 将有引号的变为双引号,变为json字符串
n = json.dumps(n) # ---》'8'
s = json.dumps(s) # ---》"hello" ---> '"hello"'
ll = json.dumps(ll) # ---》"[11, 22]"
data = json.dumps(dic) # ---》{"name": "alex"} ---> '{"name": "alex"}'

print(data, type(data))
print(n, type(n))
print(s, type(s))
print(ll, type(ll))
'''


'''
dic = {'name': 'alex'}
dic_str = json.dumps(dic)
f_write = open("hello", "w", encoding="utf-8")
f_write.write(dic_str)
f_write.close()

f_read = open("hello", "r", encoding="utf-8")
data = json.loads(f_read.read()) # json字符串只能通过json.loads()去转换为相应类型
print(data, type(data))
'''


# dump与load，dumps与loads

import json
dic = {'name': 'alex'}
f_write = open("hello", "w", encoding="utf-8")
dic_str = json.dumps(dic)
f_write.write(dic_str)
f_write.close()

# 用dump时是这样,他只能用于文件的读写
dic = {'name': 'alex'}
f_write = open("hello", "w", encoding="utf-8")
json.dump(dic, f_write) # 直接写了
f_write.close()

f_read = open("hello", "r", encoding="utf-8")
data = json.load(f_read) # 等于json.loads(f_read.read())
print(data, type(data))


# 建议使用dumps和loads

# 注意：当在文件中手动输入 {"name": "alvin"} （json样式字符串）时，依然能用loads读取出来

# f_read = open("linux_new", "r", encoding="utf-8")
# data = json.loads(f_read.read())
# print(data["name"])
