# 类方法和实例方法
import time


class People:
    country = "china"

    # 类方法用 classmethod 来进行修饰
    @classmethod
    def getCountry(cls):
        # 访问类属性
        return cls.country
        pass

    @classmethod
    def changeCountry(cls, data):
        cls.country = data
        pass

    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S", time.localtime())
        pass

    pass


print(People.getCountry())
obj = People()
print(obj.country)
People.changeCountry("nima")
print(People.getCountry())

print(People.showTime())
