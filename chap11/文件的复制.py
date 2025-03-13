def copy(src,des):
    file1=open(src,'rb')
    file2=open(des,'wb')
    s=file1.read()
    file2.write(s) #向目标文件写入所有
    file2.close() #先打开的后关，后打开的先关
    file1.close()

if __name__ == '__main__':
        src='./logo.png'
        des='../chap10/copy_logo.png' #..表示上层目录
        copy(src,des)
        print('文件复制完毕')