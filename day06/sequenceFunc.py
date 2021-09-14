# all() 对象中的元素除了 0，空，FALSE 外都算 TRUE
# 空元组，空列表 返回TRUE
print(all(()))
print(all([]))
print(all([1, 2, 3, False]))
print(all([1, 2, 3, 0]))

# any() 类似于逻辑运算符or的判断 只要一个为True，结果为True
print(any((1, 2, False)))
print(any((0, False)))

# sort应用在list方法上，sorted可以对可迭代对象进行排序
li = [1, 2, 3, 5, 6, 8, 0]
# sort 直接修改的是原始对象 默认升序
# li.sort()
print(li)
# sorted 排序之后返回一个新的list
# newLi = sorted(li)
newLi = sorted(li, reverse=True)
print(newLi)

# zip() 用来打包
s1 = ["a", "b", "c"]
s2 = ["你", "我", "它"]
print(zip(s1, s2))
print(list(zip(s1, s2)))

books = []
id = input("请输入编号，多个空格隔开")
name = input("请输入名称，多个空格隔开")
pos = input("请输入位置，多个空格隔开")
idSplit = id.split(" ")
nameSplit = name.split(" ")
posSplit = pos.split(" ")
res = zip(idSplit, nameSplit, posSplit)
for item in res:
    dicInfo = {'编号': item[0], '名称': item[1], '位置': item[2]}
    books.append(dicInfo)
    pass
print(books)

# enumerate
list = ['a', 'b', 'c']
for index, item in enumerate(list):
    print(index, item)
    pass
