from multiprocessing import Process
import os,time
class SubProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print(f'子进程的名称{self.name}，PID：{os.getpid()}，父进程的PID是：{os.getppid()}')

if __name__=='__main__':
    lst=[]
    print('父进程开始执行')
    for i in range(1,6):
        p1=SubProcess(f'进程：{i}')
        p1.start()
        lst.append(p1)

    #阻塞主进程
    for item in lst:
        item.join()

    print('父进程执行结束')

