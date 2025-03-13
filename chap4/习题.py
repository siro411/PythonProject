'''
year=eval(input('请输入一个四位数的年份'))

if year%400==0 or (year%4==0 and year%100!=0):
    print(year,'是闰年')
else: print(year,'不是闰年')

print('----------欢迎进入查询系统')
print('1.查询当前余额')
print('2.查询当前的剩余流量')
print('3.查询当前的剩余通话时长')
print('0.退出系统')
mode=eval(input('请输入要查询的功能'))
while True:
    if mode==1:
        print('当前余额40元')
    elif mode==2:
        print('当前的剩余流量40GB')
    elif mode==3:
        print('当前的剩余通话时长400分钟')
    elif mode==0:
        print('程序正在退出，感谢使用')
        break
    else:
        print('请重新输入')
    mode = eval(input('请输入要查询的功能'))

print('-----九九乘法表-----')

for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,' = ',i*j,end='\t')
    print()
'''

print('-----猜数游戏-----')
import random
rand=random.randint(1,100)
while True:
    guess=eval(input('请输入您猜的数字'))
    if rand==guess:
        print('猜中了')
        break
    elif rand>guess:
        print('小了')
    else:
        print('大了')