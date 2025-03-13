import datetime


def write_log(usr):
    dt_now=datetime.datetime.now()
    dt_now_str=dt_now.strftime('%Y-%m-%d %H:%H:%S')
    with open('log.txt','a',encoding='utf-8') as file:
        file.write('用户名 '+usr+' 登录时间'+dt_now_str+'\n')

def check_log():
    with open('log.txt','r',encoding='utf-8') as file:
        print(file.read())

if __name__=='__main__':
    usr = input('请输入用户名')
    pswd = input('请输入密码')
    if usr=='admin' and pswd=='admin':
        print('登录成功')
        write_log(usr)
        while True:
            option=input('请输入提示数字，执行响应操作：0.退出 1.查看登录日志')
            if option=='0':
                print('退出成功')
                break
            elif option=='1':
                check_log()
            else:
                print('输入错误，请重新输入')
    else:
        print('用户密码不正确')
