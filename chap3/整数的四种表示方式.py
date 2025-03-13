num=987 #默认是十进制，表示整数
num2=0b1010101
num3=0o765
num4=0x87ABF
print(num)
print(num2)
print(num3)
print(num4)

height=187.6
print(height)
print(type(height))

x=10
y=10.1
print(type(x)) #int
print(type(y)) #float

x=1.99E1413
print('科学技术数',x)
print(0.1+0.2) #0.30000000000000004
print(round(0.1+0.2,1))

x=123+456j
print('实数部分',x.real)
print('虚数部分',x.imag)