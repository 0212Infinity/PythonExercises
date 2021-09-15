class D(object):
    def eat(self):
        print("---D---eat---")
        pass


class C(D):
    def eat(self):
        print("---C---eat---")
        pass


class B(D):
    pass


class A(B, C):
    pass


obj = A()
obj.eat()
# 查看类找方法的顺序 广度优先查找
print(A.__mro__)


# =====================================
class Animal:
    def __init__(self, name):
        self.name = name
        pass

    def getName(self):
        print("夫类名称：{}".format(self.name))
        pass


class Dog(Animal):
    def __init__(self, name):
        # Animal.__init__(self,name) 手动调用夫类方法
        # super 自动调用夫类方法
        super().__init__(name)
        pass

    def getName(self):
        super().getName()
        print("子类名称：{}".format(self.name))
        pass


dog = Dog("gouwa")
dog.getName()
