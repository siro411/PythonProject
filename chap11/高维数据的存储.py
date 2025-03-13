import json
lst=[
    {'name':'jsj','age':18,'score':98},
    {'name':'xxx','age':19,'score':90},
    {'name':'cmm','age':20,'score':99},
]
s=json.dumps(lst,ensure_ascii=False,indent=4) #ensure_ascii 正常显示中文，indent 增加数据的缩进
print(type(s)) #编码lst->>str
print(s)
#解码
lst2=json.loads(s)
print(type(lst2))
print(lst2)

#编码到文件中
with open('student.txt','w',encoding='utf-8') as file:
    json.dump(lst,file,ensure_ascii=False,indent=4)

#解码到程序
with open('student.txt','r') as file:
    lst3=json.load(file)
    print(type(lst3))
    print(lst3)
    