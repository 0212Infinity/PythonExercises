# 文件操作
# 默认编码是gbk
fobj = open("./test.txt", "w", encoding="UTF-8")
fobj.write("Hello World")
fobj.close()

fobj1 = open("./test2.txt", "wb")
fobj1.write("你好".encode("UTF-8"))
fobj1.close()

fobj2 = open("./test3.txt", "w", encoding="UTF-8")
fobj2.write("好耶")
fobj2.close()

fobj3 = open("./test4.txt", "w", encoding="UTF-8")
fobj3.write("天行健，君子以自强不息")
fobj3.write("\n宇宙不停运转，人应效法天地，永远不断地前进")
fobj3.close()

# 读
rObj = open("./test.txt", "r", encoding="UTF-8")
# print(rObj.read())
print(rObj.read(1))
print(rObj.read(1))
print(rObj.readline())
rObj.close()

rObj2 = open("./test2.txt", "rb")
print(rObj2.read().decode("UTF-8"))
rObj2.close()

rObj3 = open("./test3.txt", "r", encoding="UTF-8")
print(rObj3.read())
rObj3.close()

# with上下文管理
with open("./test4.txt", "r", encoding="UTF-8") as f:
    print(f.readline())
    print(f.readline())
    pass

# tell 文件指针所在的位置
with open("./test4.txt", "r", encoding="UTF-8") as f:
    print(f.readline())
    print(f.tell())
    print(f.readline())
    pass

# truncate(字节数) 可以对源文件进行截取操作
print("截取前......................")
with open("./test4.txt", "r+", encoding="UTF-8") as f:
    print(f.read())
    f.truncate(30)
    pass
print("截取后......................")
with open("./test4.txt", "r", encoding="UTF-8") as f:
    print(f.read())
    pass

# seek(offset,from) 定位到其他位置进行操作 offset(字节数)
# from 0:文件开头 1:当前位置 2:文件末尾
# 对于"r"模式打开的文件, 从 当前位置 或者 文件末尾 计算的话,会发生异常, 应使用"rb"
with open("./test4.txt", "rb") as f:
    f.seek(3, 1)
    print(f.readline().decode("UTF-8"))
    pass
