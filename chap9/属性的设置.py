class Student():
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender #私有的实例属性

    #使用@property 修改方法，将方法转成属性使用
    @property
    def gender(self):
        return self.__gender

    #将gender设置为可写属性
    @gender.setter
    def gender(self,value):
        if value!='男' and value!='女':
            print('性别有误，已将性别设置为默认值 男')
            self.__gender='男'
        else:
            self.__gender=value



stu=Student('cmm','女')
print(stu.name,stu.gender) #stu.gender就会去执行stu.gender()

# stu.gender='男' #AttributeError: property 'gender' of 'Student' object has no setter
stu.gender='其他'
