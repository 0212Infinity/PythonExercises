# 空列表
li = []

# 切片
listA = ['abc', 789, 456, 123, True]
print(listA)
print(listA[0])
print(listA[::-1])
# 输出多次列表中的数据
print(listA * 2)

# ---增加---
# 追加
listA.append(['zxc'])
print(listA)
# 插入
listA.insert(1, 'haoye')
print(listA)
# 强制转换
rangeData = range(10)
print(type(rangeData))
rangeData = list(rangeData)
print(type(rangeData))
# 扩展, 即批量插入
listA.extend(rangeData)
listA.extend([1, 2, 3])
print(listA)

# ---修改---
listA[0] = 'qwe'
print(listA)

# ---删除---
del listA[0]
print(listA)
# 批量删除
del listA[1:4]
print(listA)
# remove 移除元素(寻找value删除,测试可得 True代表1)
listA.remove(1)
listA.remove(2)
print(listA)
# pop 移除索引值位置的元素(index)
listA.pop(2)
print(listA)

# 查找 index(val,indexStart,indexEnd)
print(listA.index('haoye'))