#1.输出1，2，3，4，5，6，8，9，10
'''
num = 1
while num < 11:
    if num != 7:
        print(num)
    else:
        pass
    num += 1
'''

#2.1-100的和
'''
num = 1
sum = 0
while num < 101:
    sum = sum + num
    num += 1
print(sum)
'''

#1-100所有奇数
'''
num = 1
while num < 101:
    if num % 2 == 1:
        print(num)
    num += 1
'''

'''
#1-100所有偶数
num = 1
while num <101:
    if num % 2 == 0:
        print(num)
    num += 1
'''


#1-2+3-4+5-6.....+99的和
'''
num = 1
sum = 0
while num <100:
    if num % 2 == 1:
        sum = sum + num
    else:
        sum = sum - num
    num += 1
print(sum)
'''


#用户登录三次机会重试
num = 0
chance = 3
while num < 3:
    name = input("请输入用户名:")
    passwd = input("请输入密码:")
    if name == "root":
        if passwd == "123":
            print("登陆成功")
            break
        else:
            chance -= 1
            if chance == 0:
                break
            num += 1
            print("密码错误")
            print("您还有%d次机会" % chance)
            continue
    else:
        chance -= 1
        if chance == 0:
            break
        num += 1
        print("请输入正确的用户名和密码")
        print("您还有%d次机会" % chance)
