# 异常处理
# try ... except
try:
    # print(b)
    li = [1, 2, 3]
    print(li[10])
    pass
except NameError as msg:
    print(msg)
    pass
except IndexError as msg:
    print(msg)
    pass
except Exception as msg:
    print(msg)
    pass

# try ... except ... else
try:
    print("123")
    pass
except Exception as msg:
    print(msg)
    pass
else:
    print("当try没有出现异常, 才会执行")

# # try ... except ... finally
try:
    print("123")
    pass
except Exception as msg:
    print(msg)
    pass
finally:
    print("不管有没有错误, 都执行, 一般用于释放资源")


# 自定义异常
class LeNumException(Exception):
    def __init__(self, length):
        self.len = length
        pass

    def __str__(self):
        return "您输入的数据长度是{}, 超过长度了...".format(self.len)

    pass


def nameTest():
    name = input("请输入姓名")
    if len(name) > 5:
        raise LeNumException(len(name))
    else:
        print(name)
        pass
    pass

# nameTest()
