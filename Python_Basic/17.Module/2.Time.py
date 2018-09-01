# time模块
import time

# 时间戳 计算
print(time.time()) # 1534666471.3955536 从1970年1月1日凌晨0点开始算到现在经历的秒数

# 结构化时间--当地时间
t = time.localtime() # 里面默认传递参数是time.time()
print(t.tm_year)
print(t.tm_wday) # 这一周的第几天，从星期一 零开始算

print(time.gmtime()) # 结构化时间--世界标准时间（英国格林尼治时间）


# 结构化时间转换成时间戳
print(time.mktime(time.localtime()))

# 将结构化时间转换为字符串时间
print(time.strftime('%Y-%m-%d %X', time.localtime())) # %X就是时分秒

# 将字符串时间转换为结构化时间
print(time.strptime('2018:8:24:16:50:36', '%Y:%m:%d:%X'))

print(time.asctime())
print(time.ctime())


import datetime
print(datetime.datetime.now())
