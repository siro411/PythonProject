s=0
for i in range(1,11):
    s+=i
else: #只有在循环正常结束之后才会执行，非正常终止循环 break语句
    print('1-10之间的累加和为：',s)