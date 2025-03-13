class Cpu():
    pass

class Disk():
    pass

class Computer():
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

cpu=Cpu()
disk=Disk()

com=Computer(cpu,disk)
#变量(对象)的赋值
com1=com
print(com,'子对象的内存地址：',com.cpu,com.disk)
print(com1,'子对象的内存地址：',com1.cpu,com1.disk)

#类对象的浅拷贝
import copy
com2=copy.copy(com)
print(com,'子对象的内存地址：',com.cpu,com.disk)
print(com2,'子对象的内存地址：',com2.cpu,com2.disk)

com3=copy.deepcopy(com)
print(com3,'子对象的内存地址：',com3.cpu,com3.disk)

