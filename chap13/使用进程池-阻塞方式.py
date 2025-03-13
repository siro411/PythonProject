from multiprocessing import Pool
import time,os
def task(name):
    print(f'子进程的PID：{os.getpid()},执行的任务:{name}')
    time.sleep(1)

if __name__=='__main__':
    start=time.time()
    print('父进程启动')
    p=Pool(3)
    for i in range(10):
        p.apply(func=task,args=(i,))

    p.close()
    p.join()
    print('所有子进程执行完毕，父进程执行结束')
    print(time.time()-start)