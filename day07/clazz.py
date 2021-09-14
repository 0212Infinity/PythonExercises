# 类名 属性 方法
class Person:
    # 类属性
    name = "zhangsan"
    age = 17

    def __init__(self):
        # 实例属性
        pro = "nima"
        pass

    # 实例方法
    def eat(self):
        print("吃饭...")
        pass


# 创建对象
obj = Person()
obj.eat()


class Car:
    def __init__(self, name, other):
        self.name = name
        self.other = other
        pass

    def run(self):
        print(self.name + "行驶中")
        pass


carObj = Car("lalala", "123")
print(carObj.name)
print(carObj.other)
carObj.run()