luck_number=8

my_name='anna'
print('luck_number的数据类型是',type(luck_number))
print(my_name,'的幸运数字是',luck_number)

luck_number='北京欢迎你'
print('luck_number的数据类型是',type(luck_number))

#在python中允许多个变量指向同一个值
no=number=1024 #no和number都指向1024这个值
print(id(no)) #id()查看对象的内存地址
print(id(number))


