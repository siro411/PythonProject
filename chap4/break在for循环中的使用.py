for i in 'hello':
    if i=='e':
        break
    print(i)

print('------------')
for i in range(3):
    user_name=input('请输入您的用户名')
    pwd=input('请输入您的密码')
    if user_name=='ysj' and pwd=='888888':
        print('系统正在登录，请稍后')
        break
    else:
        if i<2:
            print('您还有',2-i,'次机会')
else:
    print('您的账户被冻结，请稍后再试')