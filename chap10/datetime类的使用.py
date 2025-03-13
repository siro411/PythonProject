from datetime import datetime
dt=datetime.now()
print('当前的系统时间为：',dt)

#datetime是一个类，手动创建这个类的对象
dt2=datetime(2008,8,8,20,8)
print('dt2的数据类型',type(dt2),'dt2所表示的日期时间：',dt2)
print('年：',dt2.year,'月',dt2.month,'日',dt2.day)
print('时：',dt2.hour,'分：',dt2.minute,'秒：',dt2.second)

labor_day=datetime(2028,5,1,0,0,0)
national_day=datetime(2028,10,1,0,0,0)
print('2028年5月1日比2028年10月1日早吗？',labor_day<national_day) #True

#datetime类型与字符串进行转换
nowdt=datetime.now()
nowdt_str=nowdt.strftime('%Y/%m/%d %H:%M:%S')
print('nowdt的数据类型:',type(nowdt),'nowdt所表示的数据是什么',nowdt)
print('nowdt_str的数据类型:',type(nowdt_str),'nowdt所表示的数据是什么',nowdt_str)

str_data='2028年8月8日 20点8分'
dt3=datetime.strptime(str_data,'%Y年%m月%d日 %H点%M分')
print(dt3)