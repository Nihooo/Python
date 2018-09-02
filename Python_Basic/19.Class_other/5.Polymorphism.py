# 多态：指出了对象如何通过他们共同的属性和动作来操作及访问，而不需考虑他们具体的类
# str1 = "123" str1.__len__()  l1 = [1,2 3] l1.__len__()

 # 继承与多态相辅相成
class H2O:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature

    def turn_ice(self):
        if self.temperature < 0:
            print("[%s]温度太低结冰了" % self.name)
        elif self.temperature > 0 and self.temperature < 100:
            print("[%s]液化成水" % self.name)
        elif self.temperature > 100:
            print("[%s]温度太高变成了水蒸气" % self.name)

class Water(H2O):
    pass

class Ice(H2O):
    pass

class Steam(H2O):
    pass

w1 = Water('水', 25)

i1 = Ice('冰', -20)

s1 =Steam('蒸汽', 3000)


# 不同对象去调用相同方法，执行逻辑不一样，就是多态的体现
w1.turn_ice()
i1.turn_ice()
s1.turn_ice()


def func(obj):
    obj.turn_ice()

# 多态反应的是执行时候的状态
func(w1)
func(i1)
func(s1)
'''
