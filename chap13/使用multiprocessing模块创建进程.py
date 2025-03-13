from multiprocessing import Process
import os,time
def test():
    print(f'我是子进程，我的PID是：{os.getpid()}，我的父进程是：{os.getppid()}')
    time.sleep(1)

if __name__=='__main__':
    print('主进程开始执行')
    lst=[]
    #创建五个子进程
    for i in range(5):
        #创建子进程
        p=Process(target=test)
        #启动子进程
        p.start()
        lst.append(p)
    #遍历lst
    for item in lst:
        item.join() #阻塞子进程

    print('主进程执行结束')
