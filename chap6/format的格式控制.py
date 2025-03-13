s='helloworld'
print('{0:*<20}'.format(s)) #字符串的显示宽度为20，左对齐空白使用*号填充 :引导符，<左对齐，20 显示宽度
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s)) #居中对齐
print(s.center(20,'*'))

#千位分隔符 只适用于整数和浮点数
print('{0:,}'.format(987654321))
print('{0:,}'.format(987654321.7865))

#浮点数小数部分的经度
print('{0:.2f}'.format(3.1419826))
#字符串类型，。表示是最大的长度
print('{0:.5}'.format('helloworld'))

#整数类型
a=425
print('二进制：{0:b},十进制：{0:d},八进制：{0:o},十六进制：{0:x},十六进制：{0:X}'.format(a))

#浮点类型
b=3.14159
print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(b))