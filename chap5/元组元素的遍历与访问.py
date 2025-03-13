t=('python','hello','world')

#根据索引访元组
print(t[0])
t2=t[0:3:2]
print(t2)

for item in t:
    print(item)

for i in range(len(t)):
    print(i,t[i])

for idx,item in enumerate(t,start=1):
    print(idx,'-->',item)