import datetime
#输入日期
def input_date():
    inputdate=input('请输入开始日期：')
    datestr=inputdate[0:4]+'-'+inputdate[4:6]+'-'+inputdate[6:]
    dt=datetime.datetime.strptime(datestr,'%Y-%m-%d')
    return dt

if __name__=='__main__':
    date=input_date()
    int_num=eval(input('请输入间隔天数:'))
    date=date+datetime.timedelta(days=int_num)
    print('您推算的日期是：',date)
