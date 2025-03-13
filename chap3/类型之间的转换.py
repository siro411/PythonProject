x=10
y=3
z=x/y #在执行除法运算的时候，将运算的结果赋值给z
print(z,type(z)) #隐式转换，通过运算隐式的转了结果的类型

#float类型转为int类型，只保留整数部分
print('float类型转换为int类型',int(3.14))
print('float类型转换为int类型',int(3.9))
print('float类型转换为int类型',int(-3.14))
print('float类型转换为int类型',int(-3.9))

#int类型转为float类型
print('int类型转为float类型',float(10))

#将str转为int类型
print(int('100')+int('200'))

#将字符串转为int或float时报错的情况
#print(int('18a')) 报错 18a不是十进制数
#print(int('3.14')) 报错 3.14不是整数
#print(float('45a.987'))
print(ord('应'))
print(chr(24212))

#进制之间的转换操作，十进制与其他进制的转换

print(hex(26472)) #16进制
print(oct(26472)) #8进制
print(bin(26472)) #2进制

