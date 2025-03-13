import os
import time

from chap5.列表的相关操作 import new_lst

print('当前的工作路径',os.getcwd())
print(type(os.getcwd()))
lst=os.listdir()
print('当前路径下的所有目录及文件',lst)
print(type(lst))
# print('指定路径下所有目录及文件',os.listdir('D:/pythonpro'))
# os.mkdir('好好学习')#FileExistsError: [WinError 183] Cannot create a file when that file already exists: '好好学习'
# os.makedirs('./aa/bb/cc')
# os.rmdir('./好好学习')
# os.removedirs('./aa/bb/cc')
# os.chdir('D:/pythonpro')
# print('当前的工作路径',os.getcwd()) #再写代码，工作路径就是上面的

#遍历目录树，相当于递归
for dirs,dirlst,filelst in os.walk(os.getcwd()):
    print(dirs)
    print(dirlst)
    print(filelst)

def date_format(lt):
    s=time.strftime('%Y-%m-%d',time.localtime(lt))
    return s

# os.remove('./a.txt') #如果要删除的文件不存在，程序报错
# os.rename('./aa.txt','newaa.txt')
info=os.stat('./newaa.txt')

print(type(info))
print(info)

print('最近一次访问时间',date_format(info.st_atime))
print('在windows操作系统重显示的文件的创建时间',date_format(info.st_ctime))
print('最后一次修改时间',date_format(info.st_mtime))
print('文件的大小/字节',info.st_size)

#启动路径下的文件
os.startfile('calc.exe')
