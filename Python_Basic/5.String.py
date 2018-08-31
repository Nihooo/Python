# 字符串用str来表示

'''
test = 'alex'
v = test.capitalize() #首字母大写
test1 = "ALEX"
v1 = test1.casefold() #整个变，casefold更牛逼，很多未知的对应变小写
v2 = test1.lower() #整个变小写
print(v1)
print(v2)
'''

'''
test = 'alex'
print(test.center(20,'中')) #设置宽度，并将内容居中，‘中’可不写，写上表示空白位置的显示
'''

'''
test = 'alex'
v = test.ljust(20,'*') #设置宽度，并将内容放左边,'*'为填充
v1 = test.rjust(20,'*') #设置宽度，并将内容右边
print(v,v1)
'''

'''
test = 'alex'
v = test.zfill(20) #填充，默认为0
print(v)
'''

'''
test = 'aLexalexr'
v = test.count('ex') #计算字符串中有多少个‘ex’
v1 = test.count('e',5,8) #从第5个开始到第8个结束
print(v)
'''

'''
test = 'alex'
v = test.endswith('a') #是否以‘a’结尾
v1 = test.startswith('a') #是否以‘a’开始
print(v)
'''

'''
test = 'alexalex'
v = test.find('ex') #从开始往后找，找到第一个后获取其位置，找不到默认返回-1
v1 = test.find('ex', 5, 8) #指定位置，>=5  <8
print(v)
print(v1)
'''

'''
test = 'alexalex'
v = test.index('ex') #从开始往后找，找到第一个后获取其位置,找不到会报错
v1 = test.index('ex', 5, 8) #指定位置，>=5  <8
print(v)
'''

'''
test = 'i am {name}, age {a}'
print(test)
v = test.format(name = 'alex', a = 19) #格式化，将一个字符串中的占位符替换为指定值
print(v)
test1 = "i am {0}, age {1}" #第二种形式
print(test1)
v1 = test1.format('alex',11)
print(v1)
'''

'''
test = 'i am {name},age {a}'
v = test.format(name = 'df',a=10)
v1 = test.format_map({'name': 'alex','a':19}) #格式化，传入的值格式不同
print(v1)
'''

'''
test = 'usfhf5645456_='
v = test.isalnum() #字符串中是否只包含 字母和数字
print(v)
'''

'''
test = '1234567\t89' #六个为一组，有\t时\t自动补全6位
v = test.expandtabs(6)
print(v, len(v))

test = "username\temail\tpassword\nalex\talex@q.com\t123\ntom\ttom@qq.com\t123456\nNito\tNito@q.com\t795" #\n为换行符
v = test.expandtabs(20)
print(v)
'''

'''
test = 'tegegh仲'
v = test.isalpha() #是否都为字母（包括汉字）
print(v)
'''

'''
test = "4658d" 
test1 = '②'
v1 = test.isdecimal() #判断一个字符串是否为数字
v2 = test.isdigit() #判断一个字符串是否为数字，可判断特殊数字,但不支持中文
v3 = test1.isdecimal()
v4 = test1.isdigit()
v5 = test1.isnumeric #判断一个字符串是否为数字，可判断特殊数字,支持中文
print(v1,v2,v3,v4)
'''

'''
test = '_123'
test1 = '123'
v = test.isidentifier() #判断是否为标识符，由字母数字下划线组成，等于判断是否是一个正确的变量名
v1 = test1.isidentifier()
print(v,v1)
'''

'''
test = 'ALEX'
v = test.lower() #转化为小写
v1 = test.islower() #islower #判断是否都为小写
v2 = v.islower()
print(v,v1,v2)
# isupper  upper判断是否为大写和转换为大写
'''

'''
test = 'gsrhrh'
test1 = 'gsgsg\tsgsd\n' # \t制表符，tab
v = test.isprintable() #判断是否可以打印,如果存在不可显示的字符则为false
v1 = test1.isprintable()
print(v,v1)
'''

'''
test = 'faasg'
test1 = '    '
v = test.isspace() #判断是否全是空格
v1 = test1.isspace()
print(v, v1)
'''

'''
test = 'are you Ok'
v = test.istitle() #判断是否为标题，也就是每个字母首字母大写
v1 = test.title() #变为标题格式
v2 = v1.istitle()
print(v)
'''

'''
test = '嘎嘎嘎个好'
print(test)
t = ' '
v = t.join(test)
v1 = '+'.join(test) #将字符串的每一个元素按照指定分隔符进行拼接
print(v, v1)
'''

'''
# test = ' alex '
test1 = 'xalxex'
# v = test.lstrip() #默认去除左边空白，包括 \t \n，可指定去除内容
# v1 = test.rstrip() #去除右边空白
# v2 = test.strip() #去除两边空白
v3 = test1.strip('x')
# v4 = test1.rstrip('9lexal') #匹配删除，优先匹配最多
# #print(v,v1,v2,v3)
print(v3)
'''

'''
test = '咕嘟博格闪光灯'
test1 = '怪兽杀手风格分'
m = str.maketrans(test,test1) #做一个对应关系
v = "咕嘟博格闪光灯,ffffddf"
new_v = v.translate(m) #进行替换
print(new_v)
'''

'''
test = 'tesstsfsdgdsg'
v = test.partition('s') #按照s进行分割,不能传参数
# '1*2' partition能拿到 1 * 2 ，split能拿到 1 2
v1 = test.rpartition('s') #按照s进行分割,从右往左
v2 = test.split('s', 2) #按照s进行分割,能传参数,但不能拿到s
v3 = test.rsplit() #从右往左
print(v, v1, v2)
'''

'''
test = 'ffsgsg\nsdgsdgseg\ngsgg'
v = test.splitlines() #只能根据换行分割
v1 = test.splitlines(True) #true和false是否保留换行符
print(v, v1)
'''

'''
test = 'alexalexalex'
v = test.replace('ex', 'bbb', 1) #替换，1代表只替代第一个
print(v)
'''

# 七个基本 join split find strip upper lower replace

'''
test = 'alex'
v = test[0] #索引，下标，获取字符串中的某一个字符
print(v)
'''

'''
test = 'alex'
v = test[0:2] #切片，下标范围, 大于等于0 小于2
v1 = test[0:-1]
v2 = test[1:] # [1:]表示1到后面所有
print(v, v1, v2)
'''

'''
test = 'alex'
v = len(test) #查看字符串中有多少个字符(python3里按字符计算，比如‘李杰’，len就是2，而python2.7里len就是6)
print(v)
'''

'''
test = 'alexwangbadan'

index = 0
while index < len(test):
    v = test[index]
    print(v)
    index += 1
print('==========')

#for 循环
for index in test:
    print(index)
'''

'''
v = range(100) # 创建连续数字0-99
v1 = range(0, 100, 5) # 设置步长
for item in v:
    print(item)
'''

'''
test = input('>>>')
print(test)
l = len(test)
print(l)
r = range(0,l) #0到字母l
for item in r:
    print(item, test[item])
'''

# test = input('>>>')
# for item in range(0, len(test)):
#     print(item + 1, test[item])

# 索引，切片，len，for其他数据类型也能用

# 字符串一旦创建就不可修改，一旦修改或者拼接都会重新生成字符串
# 字符串可以通过索引去取值，但不可修改
