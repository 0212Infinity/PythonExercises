# 局部变量 就是在函数内部定义的变量 [作用域仅限在函数内部]
def printInfo():
    name = 'zhangsan'
    print(name)
    pass


def printInfo2():
    name = 'lisi'
    print(name)
    pass


printInfo()
printInfo2()

# 全局变量
pro = "计算机管理"


# 当全局和局部出现重复定义的时候，优先使用函数内部定义 的变量
def test01():
    pro = "计算机专业"
    print(pro)
    pass


def test02():
    print(pro)
    pass


def changeGloal():
    global pro
    pro = "nima"
    pass


test01()
changeGloal()
test02()
