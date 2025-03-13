class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return '这是一个人类，具有name和age两个实例属性'


per=Person('cmm',20)
print(per) #自动调用了__str__方法
print(per.__str__()) #手动调用__str__方法

        