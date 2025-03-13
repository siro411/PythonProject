def happy_birthday(name='jzj',age=18):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')

happy_birthday()
happy_birthday('cmm') #位置传参
happy_birthday(age=19) #关键字传参，name采用默认值

# happy_birthday(19) #TypeError: can only concatenate str (not "int") to str

def fun(a,b=20):
    pass

def fun(a=20,b): #SyntaxError: non-default argument follows default argument
    pass #当位置参数在后时会报错