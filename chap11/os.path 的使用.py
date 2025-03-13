import os.path
print('获取目录或文件的绝对路径',os.path.abspath('./b.txt'))

#判断目录或文件在磁盘上是否存在
print(os.path.exists('newb.txt'))
#拼接路径
print(os.path.join(r'C:\Users\Anna\PycharmProjects\PythonProject\chap11','b.txt'))
#分割文件的名和文件后缀名
print(os.path.splitext('b.txt'))
#提取文件名
print(os.path.basename(r'C:\Users\Anna\PycharmProjects\PythonProject\chap11\b.txt'))
#提取路径
print(os.path.dirname(r'C:\Users\Anna\PycharmProjects\PythonProject\chap11\b.txt'))
#判断一个路径是否有效
print(os.path.isdir(r'C:\Users\Anna\PycharmProjects\PythonProject\chap11'))
print(os.path.isfile(r'C:\Users\Anna\PycharmProjects\PythonProject\chap11\b.txt'))
print(os.path.isfile(r'C:\Users\Anna\PycharmProjects\PythonProject\chap11\bbb.txt'))
