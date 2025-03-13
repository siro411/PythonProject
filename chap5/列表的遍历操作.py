lst=['hello','world','python','anna']
for item in lst:
    print(item)

for i in range(0,len(lst)):
    print(i,'-->',lst[i])

for idx,item in enumerate(lst,start=1): #手动设置起始序号
    print(idx,item)

for idx,item in enumerate(lst,1): #手动设置起始序号,可以不写start
    print(idx,item)