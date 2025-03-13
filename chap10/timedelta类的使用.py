from datetime import datetime
from datetime import timedelta

delta=datetime(2008,10,1)-datetime(2008,5,1)
print('delta的数据类型是：',type(delta),'delta锁所表示的数据：',delta)
print('2008年5月1日之后的153天是：',datetime(2008,5,1)+delta)

td1=timedelta(10)
print('创建一个10天的delta对象',td1)
td2=timedelta(10,11)
print('创建一个10天11秒的timedelta对象',td2)