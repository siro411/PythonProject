import time
now=time.time()
print(now)

local_time=time.localtime() #struct_time对象
print(local_time)

local_time2=time.localtime(60)
print(local_time2,type(local_time2)) #1970年，1月1日，1时，1分，0秒 （东一区）

print('年份：',local_time2.tm_year)
print('月份：',local_time2.tm_mon)
print('日期：',local_time2.tm_mday)
print('时：',local_time2.tm_hour)
print('分：',local_time2.tm_min)
print('秒：',local_time2.tm_sec)
print('星期：',local_time2.tm_wday) #[0,6] 3表示星期四
print('今年的多少天：',local_time2.tm_yday)

print(time.ctime()) #Tue Mar 11 11:24:51 2025

#日期时间格式化
print(time.strftime('%Y-%m-%d',time.localtime()))
print(time.strftime('%H:%M:%S',time.localtime()))
print(time.strftime('月份的名称%B',time.localtime()))
print(time.strftime('星期的名称%A',time.localtime()))

#字符串转成struct_time
print(time.strptime('2008-08-08','%Y-%m-%d'))

time.sleep(10)
print('helloworld')