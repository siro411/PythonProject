def my_read(filename):
    file=open(filename,'w+',encoding='utf-8')
    file.write('你好啊')
    #seek修改文件指针的位置
    file.seek(0)
    # s=file.read() 读取全部
    # s=file.read(2) 你好，2指的2个字符
    # s=file.readline() #读取一行数据
    # s=file.readline(2) #读取一行中的2个字符
    # s=file.readlines() #读取所有，一行为列表中的一个元素，s是列表类型
    file.seek(3) #3个字节，一个中文占三个字节
    s=file.read()
    print(type(s),s)

    file.close()

if __name__ == '__main__':
    my_read('d.txt')