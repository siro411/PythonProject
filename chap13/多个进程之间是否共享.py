from multiprocessing import Process
a=100
def add():
    print('子进程1开始执行')
    global a
    a+=30
    print('a=',a)
    print('子进程1执行完毕')

def sub():
    print('子进程2开始执行')
    global a
    a -= 50
    print('a=', a)
    print('子进程2执行完毕')

if __name__=='__main__':
    #父进程
    print('父进程开始执行')
    print('a=',a)

    p1 = Process(target=add)
    p2 = Process(target=sub)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print('a=',a)

    print('父进程执行结束')

#父进程 a=100
#子进程1 a=100 a+=30 a=130
#子进程2 a=100 a-=50 a=50