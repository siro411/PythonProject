#format()
print(format(3.14,'20')) #数值默认右对齐
print(format('hello','20')) #字符串默认左对齐
print(format('hello','*<20')) #<表示左对齐，*表示填充符，20表示的是显示的宽度
print(format('hello','*>20'))
print(format('hello','*^20'))

print(format(3.1415926,'.2f'))
print(format(20,'b')) #二进制
print(format(20,'o'))
print(format(20,'x'))
print(format(20,'X'))

print('-'*40)
print(len('helloworld'))
print(len([10,20,30,40,50]))

print(id(10))
print(id('helloworld'))
print(type('hello'),type(10))

print(eval('10+30'))
print(eval('10>30')) #False
