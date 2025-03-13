import os

def mkdirs(path,num):
    for i in range(1,num+1):
        os.mkdir(path+'/'+str(i))

if __name__=='__main__':
    new_dir='./newdir'
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)

    num = eval(input('请输入要创建的目录个数'))
    mkdirs(new_dir,num)
