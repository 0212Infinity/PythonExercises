# 不可变类型 int str 元组
a = 1


def test01(x):
    print("test01 Method x: {}".format(id(x)))
    x = 2
    print("test01 Method x: {}".format(id(x)))
    pass


print("a: {}".format(id(a)))
test01(a)
print("a: {}".format(id(a)))

# 可变类型 列表 字典
list = []


def test02(params):
    print("test02 Method params: {}".format(id(params)))
    # params = [1,2,3] 会变
    params.append([1, 2, 3])
    print("test02 Method params: {}".format(id(params)))
    pass


print("list: {}".format(id(list)))
test02(list)
print("list: {}".format(id(list)))
print(list)

# 万物皆对象
# 函数调用时，实参传递的就是对象的引用
