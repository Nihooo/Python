# re模块 正则表达式 ：对字符串进行处理（模糊匹配）

# 元字符： . ^ $ * + ? {} [] | () \

# . 通配符，一个点代表任意一个字符
import re
# v = re.findall("a..x", "faafwaxdxffwgb")
# print(v)

# v = re.findall("a..x", "afaxfwaxdxffwgb")
# print(v)


# ^ 以。。。开头，必须在字符串的开头去匹配
# v = re.findall("^a..x", "faafwaxdxffwgb")
# print(v)

# v = re.findall("^a..x", "afaxfwaxdxffwgb")
# print(v)


# $ 以。。。结尾，必须在字符串的结尾去匹配
# v = re.findall("a..x$", "afaxfwaxdxffwgb")
# print(v)

# v = re.findall("a..x$", "afaxfwaxdxfwagbx")
# print(v)


# * 按着紧挨着的字符匹配 0-无穷次
# v = re.findall("d*", "adgedgeefadddddddddwgb")
# print(v)

# v = re.findall("alex*", "afagagwalexxxxx")
# print(v)


# + 按着紧挨着的字符匹配 1-无穷次
# v = re.findall("alex+", "afagagwalexxxxx")
# print(v)


# ? 匹配0次或者1次
# v = re.findall("alex?", "afagagwalexxx")
# print(v)

# v = re.findall("alex?", "afagagwale")
# print(v)


# {} 可自定义范围匹配  {0,} == *, {1,} == +, {0,1} == ?
# v = re.findall("alex{6}", "afagagwalexxxxxxxxx")
# print(v)

# v = re.findall("alex{1,6}", "afagagwalexxxxxxx")
# print(v)


# *,+,?等都是贪婪匹配，就是尽可能多的匹配，后面加？号使其变成惰性匹配，尽可能少的匹配
# v = re.findall("alex*?", "afagagwalexxxxx")
# print(v)

# v = re.findall("alex+?", "afagagwalexxxxx")
# print(v)


# [] 字符集,在字符集里没有特殊符号,除了几个特别的 - ^非 \
'''
v = re.findall("x[yz]", "xyfafsfasxz")
print(v)

v = re.findall("x[yz]p", "xypfafsfasxz")
print(v)

v = re.findall("x[y,z]p", "xyfafsfasx,ptjt")
print(v)

v = re.findall("q[a*z]", "sghdsqaaa")
print(v)

v = re.findall("q[a*z]", "sghdsq*aaa")
print(v)

v = re.findall("q[a-z]", "sgqhdsqaaa")
print(v)

v = re.findall("q[a-z]*", "sgqhdsqaaa9")
print(v)

v = re.findall("q[0-9]*", "sgqhdsqaaa9hfghq88")
print(v)

v = re.findall("q[^a-z]", "sgqhdsqaaahfghq88") # q[非a-z]就能匹配
print(v)

v = re.findall("\([^()]*\)", "12+(34*6+2-5*(2-1))") # \( 就表示普通的左括号
print(v)
'''


# \ 转义符
# \d 匹配任何十进制数，相当于[0-9]
# v = re.findall("\d", "12+(34*6+2-5*(2-1))")
# print(v)

# v = re.findall("\d+", "12+(34*6+2-5*(2-1))")
# print(v)


# \D 匹配任何非数字字符，相当于[^0-9]
# v = re.findall("\D", "12+(34*6+2-5*(2-1))")
# print(v)


# \s 匹配任何空白字符，相当于[\t\n\r\f\v]
# v = re.findall("\s", "hello world")
# print(v)


# \S 匹配任何非空白字符，相当于[^\t\n\r\f\v]
# v = re.findall("\S+", "hello world")
# print(v)


# \w 匹配任何字母数字字符，相当于[a-zA-Z0-9_]
# v = re.findall("\w+", "he4llo wor1ld_")
# print(v)


# \W 匹配任何非字母数字字符，相当于[^a-zA-Z0-9_]
# v = re.findall("\W+", "he*4llo wor@1ld_")
# print(v)


# \b 匹配一个特殊字符边界，如空格，&，#等
# v = re.findall(r"I\b", "hello I@am LIST")
# print(v)

# v = re.findall(r"\d+\b", "204860599@qq.com")
# print(v)

# v = re.findall(r"I\b", "hello I am LIST") # r" ", r表示原生字符串，加上表示" "里的内容不做任何转义
# print(v)

# v = re.findall("I\\b", "hello I am LIST")
# print(v)

# v = re.findall("c\\\\l", "abc\lret") # python解释器先拿去两个\\,re拿去\\，还剩一个\
# print(v) # 本来是c\l，但经过python又加了个\,变成c\\l

# v = re.findall(r"c\\l", "abc\lret")
# print(v)



# v = re.findall("www.baidu", "www/baidu")
# print(v)
#
# v = re.findall("www\.baidu", "www.baidu")
# print(v)
#
# v = re.findall("www\*baidu", "www*baidu")
# print(v)


# | 管道符,或
# v = re.findall(r"ka|b", "ghagbeha")
# print(v)

# v = re.findall(r"ka|b", "ghka|beha")
# print(v)

# v = re.findall(r"ka\|b", "ghka|beha")
# print(v)


# () 分组
# v = re.findall("(ad)+", "add")
# print(v)

# v = re.findall("(abc)+", "abcccc")
# print(v)

# v = re.findall("(abc)+", "abcabcabc") # 只显示括号里的
# print(v)

# v = re.findall("(?:abc)+", "abcabcabc")# 都显示
# print(v)


# findall 所有能匹配的放到一个列表里,匹配不成功返回空列表
# v = re.findall("(?P<name>\w+)", "abcabcabc")
# print(v)


# search 只找第一个，匹配不成功返回空None
# v = re.search("(?P<name>\w+)", "abcabcabc")
# print(v)


# v = re.search("\d+", "abc46abc767abc")
# print(v)

# v = re.search("\d+", "abc46abc767abc").group() # 只返回查找值
# print(v)

# v = re.search("[a-z]+", "alex36wusir34xialv33").group()
# # print(v)

# v = re.search("(?P<name>[a-z]+)", "alex36wusir34xialv33").group()
# print(v)

#  ?P<name> 就是一种格式，目的是进行分组

# v = re.search("(?P<name>[a-z]+)\d+", "alex36wusir34xialv33").group()
# print(v)

# v = re.search("(?P<name>[a-z]+)\d+", "alex36wusir34xialv33").group("name")
# print(v)

# v = re.search("(?P<name>[a-z]+)(?P<age>\d+)", "alex36wusir34xialv33").group("age")
# print(v)


# match相当于在search的基础上加上一个^，只匹配开头，无时返回None
# v = re.match("\d+", "alex36wusir34xialv33")
# print(v)

# v = re.match("\d+", "45alex36wusir34xialv33").group()
# print(v)


# 按空格去拿值
# v = re.split(" ", "hello abc def")
# print(v)

# v = re.split("[ |]", "hello abc|def")
# print(v)

# v = re.split("[ab]", "asdabcd")
# print(v) # 先a分一次得["","sdabcd]，再a分一次["","sd","bcd"]，最后b分一次['', 'sd', '', 'cd']


# 将字符串中所有数字换成A
# v = re.sub("\d+", "A", "gdgg54ag5454gs13s8gegr798")
# print(v)

# 将字符串中所有数字换成A,匹配4次
# v = re.sub("\d+", "A", "gdgg54ag5454gs13s8gegr798", 4)
# print(v)

# 将字符串中所有数字换成A,同时返回匹配次数
# v = re.subn("\d+", "A", "gdgg54ag5454gs13s8gegr798")
# print(v)

# compile可以先制定规则
# v = re.compile("\d+")
# res = v.findall("gdfg156gaf223") # 与re.findall("\d+","gdfg156gaf223")一样
# print(res)


# v = re.findall("\d+", "gdfg156gaf223")
# print(v)
#
# v = re.finditer("\d+", "gdfg156gaf223") # 返回一个迭代对象
# res = next(v).group()
# print(res)
# for i in v:
#     print(i)

# v = re.findall("www\.(baidu|163)\.com", "feffeg3twww.baidu.comgsgds")
# print(v) # 匹配成功，但只会优先将组里的baidu给你

# v = re.findall("www\.(?:baidu|163)\.com", "feffeg3twww.baidu.comgsgds")
# print(v)  # ?: 会去除掉优先级组里的


# v = re.search("abc|bcd", "abcd").group()
# # print(v)

# v = re.findall("abc|bcd", "abcbcd")
# print(v)
