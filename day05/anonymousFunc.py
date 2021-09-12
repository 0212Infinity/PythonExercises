# 匿名函数
# 匿名函数冒号后面的表达式有且只有一个
# 匿名函数自带return
result = lambda a, b, c: a * b * c
print(result(1, 2, 3))

age = 18
print("可以参军" if age >= 18 else "继续上学")

funTest = lambda x, y: x if x > y else y
print(funTest(12, 10))

funTest2 = (lambda x, y: x if x > y else y)(1, 2)
print(funTest2)
