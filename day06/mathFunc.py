print(abs(-3.14))

# round近似值，返回值跟python版本和浮点数的精度有关
print(round(2.61, 1))

# pow求指数
print(pow(3, 2))

# divmod求商和余 返回元组
print(divmod(1, 3))

# max最大值 min最小值 sum求和

# eval 用来执行一个字符串表达式，并返回表达式的值
a, b, c = 1, 2, 3
print(eval("a*b*c"))
print(eval("a*b*c", {'a': 7, 'b': 8, 'c': 9}))

