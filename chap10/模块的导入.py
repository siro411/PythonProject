import my_info
print(my_info.name)
my_info.info()

import my_info as a
print(a.name)
a.info()

from my_info import name #导入的是一个具体的变量的名称
print(name)

from my_info import info
info()

#同时导入多个模块
import math,time,random
