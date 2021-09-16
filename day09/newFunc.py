# new实例化
class Animal:
    def __init__(self):
        self.color = "红色"
        pass

    # 如果不重写 __new__ 默认结构如下
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
        # return object.__new__(cls, *args, **kwargs)
        pass

    pass


obj = Animal()


# 在新式类中 __new__ 才是真正的实例化方法 , 为类提供外壳制造出实例框架
# 然后调用该框架内的构造方法 __init__ 进行丰富操作

# 单例模式
class SingleCase(object):
    def __new__(cls, *args, **kwargs):
        # hasattr 如果对象有该属性返回 True，否则返回 False。
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
            pass
        return cls._instance
        pass

    pass


obj1 = SingleCase()
print(id(obj1))
obj2 = SingleCase()
print(id(obj2))
obj3 = SingleCase()
print(id(obj3))
