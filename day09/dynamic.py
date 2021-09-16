# 动态属性/方法
class Student:
    def __init__(self, name):
        self.name = name
        pass

    def __str__(self):
        return "姓名是{}".format(self.name)

    pass


obj = Student("zhangsan")
# 动态添加
obj.age = 17
print(obj.age)

# 动态添加方法
import types


def dymicMethod(self):
    print("姓名是{}, 年龄是{}".format(self.name, self.age))
    pass


@classmethod
def dymicClazzMethod(cls):
    print("这是个类方法")
    pass


obj.printInfo = types.MethodType(dymicMethod, obj)
obj.printInfo()

# 绑定类方法
Student.dymicClazzMethod = dymicClazzMethod
Student.dymicClazzMethod()
obj.dymicClazzMethod()
