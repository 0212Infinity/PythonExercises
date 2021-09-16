# slots属性限制

class Student(object):
    __slots__ = ('name', 'age')

    def __str__(self):
        return "{}:{}".format(self.name, self.age)

    pass


obj = Student()
obj.name = 'zhangsan'
obj.age = 17
print(obj)


# 没定义__slots__变量之前, 所有可以用的属性都在这里存储, 不足:占用内存空间大
# print(obj.__dict__)

# 在继承关系中
# 当子类未声明 __slots__, 那么不会继承父类的 __slots__, 子类可以随意的属性赋值
# 当子类声明 __slots__ 时, 会继承父类的 __slots__, 也就是 子类+父类的__slots__
class subStudent(Student):
    __slots__ = ('pro')
    pass


subObj = subStudent()
subObj.pro = "123"
subObj.name = "456"
print(subObj.pro)
