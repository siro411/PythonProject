s=lambda a,b:a+b
print(s(1,2),type(s))

lst=[10,20,30,40]
for i in range(len(lst)):
    print(lst[i])
print()

lst=[10,20,30,40]
for i in range(len(lst)):
    result = lambda x:x[i]
    print(result(lst))

student_score=[
    {'name':'cmm','score':98},
    {'name': 'xmm','score': 88},
    {'name':'mmm','score':68},
    {'name': 'hmm','score': 78}
]
#按成绩排
student_score.sort(key=lambda x:x.get('score'),reverse=True)
print(student_score)