class Person:
    def __init__(self):
        print("---init---")
        pass

    def __new__(cls, *args, **kwargs):
        print("---new---")
        return object.__new__(cls)
        pass

    def __str__(self):
        return "__str__ 类似java的toString方法"
        pass

obj = Person()
print(obj)

# __new__类的实例化方法, 必须要返回该实例, 否则对象就创建不成功
# __init__用来做数据属性的初始化工作, 也可以认为是实例的构造方法, 接受类的实例self并对其进行构造
# __new__至少有一个参数是 cls 代表要实例化的类, 此参数在实例化是由 python解释器自动提供
# __new__函数 执行要早于 __init__函数
