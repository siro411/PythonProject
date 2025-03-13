class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f'大家好，我叫：{self.name},我今年：{self.age}岁')


per=Person('cmm',20)
per.show()
print(dir(per))
print(per) #自动调用了__str__方法