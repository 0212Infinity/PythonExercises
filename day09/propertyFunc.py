# 属性函数

class Person:
    def __init__(self):
        __age = 10
        pass

    def getAge(self):
        return self.__age
        pass

    def setAge(self, age):
        if age < 0:
            print("年龄小于0")
        else:
            self.__age = age
            pass
        pass

    age = property(getAge, setAge)
    pass


obj = Person()
obj.age = 10
print(obj.age)


# 装饰器
class Animal:
    def __init__(self):
        __age = 10
        pass

    @property  # 提供一个getter方法
    def age(self):
        return self.__age
        pass

    @age.setter  # 提供一个setter方法
    def age(self, age):
        if age < 0:
            print("年龄小于0")
        else:
            self.__age = age
            pass
        pass

    pass


obj2 = Animal()
obj2.age = 30
print(obj2.age)
