class Person:

    def eat(self):
        print("self={}".format(id(self)))
        pass


obj = Person()
obj.eat()
print(id(obj))

# self只有在类中定义实例方法的时候才有意义,在调用时候不必传入相应的参数而是由解释器自动去指向
# self的名字是可以更改的, 可以定义成其他的名字, 只是约定俗成的定义成了self
# self指的是类实例对象本身, 相当于 java 中 this
