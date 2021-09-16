class Student:
    # 类属性
    name = 'liming'

    def __init__(self, age):
        # 实例对象
        self.age = age
        pass


obj = Student(17)
print(obj.name)
print(obj.age)
print(Student.name)

# 类属性可以 被类对象和实例对象共同访问使用
# 实例属性只能 由实例对象所访问
