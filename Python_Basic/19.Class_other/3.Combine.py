# 组合 大类包含小类,类与类之间没有共同点，但有关联


'''
class Hand:
    pass

class Foot:
    pass

class Trunk:
    pass

class Head:
    pass


class Person:
    def __init__(self, id_num, name):
        self.id_num = id_num
        self.name = name
        self.hand = Hand()
        self.foot = Foot()
        self.trunk = Trunk()
        self.head = Head()


p1 = Person("1111", "alex")
print(p1.__dict__)
'''




class School:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def recurit_student(self):
        print("%s正在招生" % self.name)


class Course:
    def __init__(self, name, price, period, school):
        self.name = name
        self.price = price
        self.period = period
        self.school = school


s1 = School("oldboy", "北京")
s2 = School("oldboy", "东京")
s3 = School("oldboy", "南京")

c1 = Course("linux", 10, "1小时", s1)
print(c1.__dict__)
print(c1.school.name) # c1.school <__main__.School object at 0x000002DE44BAFA90>
print(s1) # <__main__.School object at 0x000002DE44BAFA90>

msg = '''
1 老男孩 北京小区
2 老男孩 东京小区
3 老男孩 南京小区
'''

while True:
    print(msg)
    menu = {
        '1': s1,
        '2': s2,
        '3': s3
    }
    choice = input("选择小区: ")
    school_obj = menu[choice]

    name = input("课程名:")
    price = input("课程费用:")
    period = input("课程周期:")

    new_course = Course(name, price, period, school_obj)
    print("课程【%s】 属于【%s】 学校" % (new_course.name, new_course.school.addr))
