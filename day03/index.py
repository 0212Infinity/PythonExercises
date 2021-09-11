name = "zhangsan"
# 首字母大写
print(name.capitalize())
# strip:删除两边空格   lstrip:删除左边空格   rstrip:删除右边空格
txt = "   hello    "
print(txt.strip())

# 两个地址相同, 只是把txt对象的内存地址赋给了b
print(id(txt))
b = txt
print(id(b))

# 查找目标对象在序列对象中的索引值
str = "Hello"
print(str.find('e'))
# index找不到会报错, find找不到会返回-1
print(str.index('e'))

# 判断开头结尾
print(str.startswith('H'))
print(str.endswith('o'))
# 转换大小写
print(str.upper())
print(str.lower())

# 切片 str[start:end:step] 左闭右开
strMsg = "Hello World"
print(strMsg[2:7])
print(strMsg[2:])
# 0可以省略掉
print(strMsg[:3])
# 倒序输出 负数表示右到左遍历
print(strMsg[::-1])