from multiprocessing import Process
import os,time
def sub_process(name):
    print(f'子进程PID：{os.getpid()}，父进程的PID是：{os.getppid()}，--------{name}')
    time.sleep(1)

def sub_process2(name):
    print(f'子进程PID：{os.getpid()}，父进程的PID是：{os.getppid()}，--------{name}')
    time.sleep(1)

if __name__=='__main__':
    print('父进程开始执行')
    for i in range(5):
        # p1=Process() #没有给定target参数，不会执行自己编写的函数中的代码，会调用Process类中的run()方法
        p1=Process(target=sub_process,args=('ysj',))
        p2=Process(target=sub_process2,args=(18,))
        p1.start()
        p2.start()

        # 终止进程
        p1.terminate()
        p2.terminate()

    print('父进程结束')


