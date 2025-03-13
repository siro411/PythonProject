class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'大家好，我叫：{self.name},今年：{self.age}岁')

class Student(Person):
    def __init__(self,name,age,stuno):
        super().__init__(name,age)
        self.stuno=stuno

    def show(self):
        #调用父类的方法
        super().show()
        print(f'我来自xxx大学，我的学号是{self.stuno}')


class Doctor(Person):
    def __init__(self,name,age,dep):
        super().__init__(name,age)
        self.dep=dep

    def show(self):
        print(f'大家好，我叫：{self.name},今年：{self.age}岁，我的工作科室是{self.dep}')

stu=Student('cmm',20,'1001')
stu.show() #调用子类自己的show()方法

doctor=Doctor('zyy',32,'外科')
doctor.show() #调用子类自己的show()方法