# 私有化属性
class Person:
    __pro = "123"

    def __init__(self):
        # 加两个下划线 将此属性私有化之后
        # 外部不能直接访问, 内部可以访问
        self.__name = 'lisi'
        self.age = 30
        pass

    def __str__(self):
        return "{}的年龄是{}".format(self.__name, self.age)


class Student(Person):
    def printInfo(self):
        # print(self.__name) 报错
        print(self.age)
        pass

    pass


obj = Person()
# print(obj.__name) 报错 AttributeError: 'Person' object has no attribute '__name'
print(obj)

stu = Student()
# print(stu.__name) AttributeError: 'Student' object has no attribute '__name'
stu.printInfo()
