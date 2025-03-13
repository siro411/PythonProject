import threading
from threading import Thread
import time



def test():
    for i in range(3):
        time.sleep(1)
        print(f'线程：{threading.current_thread().name}正在执行{i}')

if __name__=='__main__':
    start=time.time()
    print('主线程开始执行')
    lst=[Thread(target=test) for i in range(2)]
    for item in lst:
        #启动线程
        item.start()

    for item in lst:
        item.join()

    print('一共耗时：',time.time()-start)

    #三个线程并行执行的任务是什么？ 主线程负责执行，main中的代码。Thread-1线程执行三次循环 ，Thread-2线程执行三次循环