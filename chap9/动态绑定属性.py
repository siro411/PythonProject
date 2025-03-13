class Student:
    school='北京某教育'
    def __init__(self,xm,age): #xm,age是方法的参数，是局部变量，xm，age的作用域是整个__init__方法
        self.name=xm #左侧是实例属性，xm是局部变量，将局部变量的值xm复制给实例属性
        self.age=age
    #定义在类中的函数，称为方法，自带一个参数self
    def show(self):
        print(f'我叫：{self.name}，我今年{self.age}')


stu=Student('jsj',18)
stu2=Student('cmm',20)
stu2.gender='男'
print(stu.name,stu.age)
print(stu2.name,stu2.age)
print(stu2.gender)
# print(stu.gender) #AttributeError: 'Student' object has no attribute 'gender'

def introduce():
    print('我是一个普通的函数，我被动态绑定了stu2对象的方法')
stu2.fun=introduce #函数的一个赋值

stu2.fun()