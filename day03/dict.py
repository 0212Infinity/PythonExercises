# 空字典
dictA = {}
print(type(dictA))
print(id(dictA))
dictA['name'] = "zhangsan"
print(id(dictA))
print(dictA)
print(len(dictA))

# 获取
print(dictA['name'])
# ---修改---
dictA['name'] = 'lisi'
print(dictA)
# 不存在的key添加, 已存在的key修改
dictA.update({'name': "nima"})
# 获取所有的键
print(dictA.keys())
# 获取所有的值
print(dictA.values())
# 获取所有的键值对
print(dictA.items())

dictA['age'] = 10
for key, value in dictA.items():
    print("key:{}, value:{}".format(key, value))

# ---删除---
del dictA['name']
print(dictA)
dictA.pop('age')
print(dictA)

# ---排序---
dictA = {'name': "zhangsan", 'age': 50}
print(id(dictA))
print(sorted(dictA.items(), key=lambda d: d[0]))
