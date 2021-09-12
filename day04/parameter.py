# 参数的分类： 必选参数，默认参数【缺省参数】，可变参数，关键字参数
# 缺省参数(默认参数) 始终位于参数列表的尾部
def sum(a=10, b=20):
    sum = a + b
    print(sum)
    pass


# 未赋值的时候使用默认值
sum()
sum(20)


# 不定长参数(可变参数) 个数不确定的时候使用
def getComputer(*args):
    print(args)
    pass


getComputer(1, 2, 3)


# 关键字参数 在函数体内，参数关键字是字典类型，key是字符串
def keyFunc(**kwargs):
    print(kwargs)
    pass


dictA = {'name': "zhangsan", 'age': 17}
keyFunc(**dictA)
keyFunc()
keyFunc(name="lisi", age=18)


def complexFunc(*args, **kwargs):
    print(args)
    print(kwargs)
    pass


complexFunc()
complexFunc(1, 2, 3, 4)
complexFunc(1, 2, 3, 4, name='nima')
complexFunc(age=17)

# 语法错误，可变参数必须放在关键字参数前面
# def testParameter(**kwargs,*args):
