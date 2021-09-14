# set 不索引和切片 无序且不重复的容器
# 类似于字典，但是没有key，只有value
set1 = {1, 2, 3}
print(set1)

set1.add("python")
print(set1)
# set1.clear()
# print(set1)

# difference 差集, intersection 交集, union 并集
set2 = {3, 4, 5, 6}
res1 = set1.difference(set2)
print(res1)
print(set1 - set2)

print(set1.intersection(set2))
print(set1 & set2)

print(set1.union(set2))
print(set1 | set2)

# pop 从集合中拿数据并且同时删除
print(set1.pop())
print(set1)

# discard() 指定移除元素 ，update()合并原来集合
set1.update(set2)
print(set1)
