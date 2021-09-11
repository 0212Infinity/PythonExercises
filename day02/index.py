score = 60
# 单分支
if score <= 60:
    print("成绩不是很理想, 要继续加油")
    pass  # 空语句
print("单分支结束")

# 双分支
score = 100
if score <= 60:
    print("成绩不是很理想, 要继续加油")
    pass
else:
    print("还行")
    pass
print("双分支结束")

# 多分支
score = 75
if score <= 60:
    print("成绩不是很理想, 要继续加油")
    pass
elif score > 60 and score < 90:
    # elif 60 < score < 90:
    print("还行")
    pass
else:
    print("优秀")
    pass
print("多分支结束")

# while循环 打印九九乘法表
row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("{}*{}={}".format(col, row, row * col), end=" ")
        col += 1
        pass
    print()
    row += 1
    pass

# for循环
# range 此函数可以生成一个数据集合列表
# range(起始:结束:步长) 步长不能为0 左包右不包
for data in range(1, 101):
    print(data)
    pass

# break退出循环 continue 跳出本次循环
# for--else
for item in range(1, 11):
    print(item)
    if item >= 5:
        break
        pass
    pass
else:
    print('上面循环只要执行了break, 那么else不再执行')
# while---else
index = 1
while index <= 10:
    index += 1
    if index == 5:
        break
        pass
    pass
else:
    print('else执行')
