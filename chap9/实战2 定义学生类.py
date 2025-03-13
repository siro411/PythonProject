class Student():
    def __init__(self,name,age,gender,score):
        self.name=name
        self.age=age
        self.gender=gender
        self.score=score

    def info(self):
        print(self.name,self.age,self.gender,self.score)

lst=[]
for i in range(1,6):
    student = input(f'请输入第{i}位录入学生信息及成绩：')
    stu_lst = student.split('#')
    stu=Student(stu_lst[0],stu_lst[1],stu_lst[2],stu_lst[3])
    lst.append(stu)

for i in range(5):
    lst[i].info()

