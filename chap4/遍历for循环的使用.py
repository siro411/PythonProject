for i in 'hello':
    print(i)

#range函数，python中的内置函数，产生一个【n，m）的整数序列，包含n，但是不包含m
for i in range(1,11):
    #print(i)
    if i%2==0:
        print(i,'是偶数')


#计算1-10之间的累加和
s=0 #用于存储累加和
for i in range(1,11):
    s+=i

print('1-10之间的累加和是：',s)
print('-----------100-999之间的水仙花数----')
'''
153=3*3*3+5*5*5+1*1*1
'''
for i in range(100,1000):
    sd=i%10 #获取个位上的数字
    tens=i//10%10 #获取十位上的数字
    hundred=i//100
    if sd**3+tens**3+hundred**3==i:
        print(i)