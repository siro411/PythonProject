class Person():
    pass

class Cat():
    pass

class Dog:
    pass

class Student:
    school='北京某教育'
    def __init__(self,xm,age): #xm,age是方法的参数，是局部变量，xm，age的作用域是整个__init__方法
        self.name=xm #左侧是实例属性，xm是局部变量，将局部变量的值xm复制给实例属性
        self.age=age
    #定义在类中的函数，称为方法，自带一个参数self
    def show(self):
        print(f'我叫：{self.name}，我今年{self.age}')

    @staticmethod
    def sm():
        print('这是一个静态方法，不能调用实例属性，也不能调用实例方法')

    @classmethod
    def cm(cls):
        print('这是一个类方法，不能调用实例属性，也不能调用实例方法')

person=Person()
c=Cat()
d=Dog()
stu=Student('jsj',18)
print(type(person))
#实例属性，使用对象进行打点调用
print(stu.name,stu.age)
#类属性，直接使用类名，打点调用
print(Student.school)
#实例方法，使用对象名进行打点调用
stu.show()
#类方法/静态方法。直接使用类名称打点调用
Student.cm()
Student.sm()

