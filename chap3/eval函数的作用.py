s='3.14+3'
print(s,type(s))
x=eval(s)
print(x,type(x))

#eval函数经常与input()函数一起使用，用来获取用户输入的数据
age=eval(input('请输入您的年龄：')) #将字符串类型转换成int类型
print(age,type(age))
height=eval(input('您的身高是：'))
print(height,type(height))

hello='北京欢迎你'
print(hello)
print(eval('hello')) #hello是变量
print(eval('北京欢迎你')) #北京欢迎你没有被定义