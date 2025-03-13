s='HelloWorld'
new_s=s.replace('o','你好',1)
#最后一个参数是替换次数，默认是全部替换
print(new_s)

print(s.center(20,'*'))# 字符串在指定的宽度范围内居中

s='    Hello    World       '
print(s.strip())
print(s.lstrip()) #去掉字符串左侧的空格
print(s.rstrip()) #去掉字符串右侧的空格

#去掉指定的字符
s3='dl-Helloworld'
print(s3.strip('ld')) #与顺序无关
print(s3.lstrip('ld'))