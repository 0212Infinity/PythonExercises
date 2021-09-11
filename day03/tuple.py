# 空元组
tupleA = ()
print(type(tupleA))
print(id(tupleA))
tupleA = ('abc', 123, 4.56, [77, 88, 99])
print(id(tupleA))
print(tupleA)

# ---查找---
print(tupleA[2])
print(tupleA[2:4])
print(tupleA[::-1])

# ---修改---
# tupleA[0] = 'qwe' 元组不可修改
# 元组里面的列表可以修改
tupleA[3][0] = 10086
print(tupleA)

# 元组创建只有一个元素的时候,要加','
tupleB = (1)
print(type(tupleB))
tupleB = (1,)
print(type(tupleB))

tupleC = (1, 2, 1, 3, 1, 4, 1, 5)
# 可以统计元素出现的次数
print(tupleC.count(1))