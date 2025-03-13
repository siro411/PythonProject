print('非空字符串的布尔值：',bool('hello'))
print('空字符串的布尔值：',bool(''))
print('空列表的布尔值：',bool([]))
print('空元组的布尔值：',bool(()))
print('空元组的布尔值：',bool(tuple()))
print('空集合的布尔值：',bool(set()))
print('空字典的布尔值：',bool({}))
print('空字典的布尔值',bool(dict()))
print('-'*40)
print('非0数值的布尔值：',bool(123))
print('整数0的布尔值：',bool(0))
print('浮点数0.0的布尔值：',bool(0.0)) #False

#将其他类型转换成字符串类型
lst=[10,20,30]
print(type(lst),lst)

s=str(lst)
print(type(s),s)
print('-'*40)
print('float类型和str类型转成int类型：')
print(int(98.7))
print(int('90'))
# print(int('98.7')) #ValueError: invalid literal for int() with base 10: '98.7'
# print(int('a'))  #ValueError: invalid literal for int() with base 10: 'a'
print('-'*40)
print('int,str类型转成float类型')
print(float(90)+float('3.14'))

print('-'*40)
s='hello'
print(list(s))

seq=range(1,10)
print(tuple(seq))
print(set(seq))
print(list(seq))