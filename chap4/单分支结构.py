number=eval(input('请输入6位数字'))
if number==987654:
    print('恭喜您，中奖了')

if number!=987654:
    print('您未中本次大奖')

print('---以上if判断的表达式，是通过比较运算计算出来的，结果是布尔值类型')
n=98
if n%2:
    print(n,'是奇数') #由于98%2为0，所以该行代码不执行

if not n%2:
    print(n,'是偶数')

print('---判断一个字符串是否是空字符串---')
x=input('请输入一个字符串')
if x: #python中一切皆对象，每个对象都有一个布尔值，而非空字符串的布尔值为True，空字符串的布尔值为False
    print('x是一个非空字符串')

if not x: #空字符串的布尔值位False，取反，not False的结果为True
    print('x是空字符串')

print('---表达式也可以是一个单纯的布尔型对象')
flag=eval(input('请输入一个布尔类型的值'))
if flag:
    print('flag的值是True')
if not flag:
    print('flag的值是False')

print('---使用if语句时，如果语句块中只有一句代码，可以将语句块直接卸载：后面')
a=10
b=5
if a>b: max=a
print('a和b的最大值为',max)
