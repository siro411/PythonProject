import threading
import time
from threading import Thread,Lock
ticket=50
lock_obj=Lock() #创建锁对象
def sale_ticket():
    global ticket
    for i in range(100):
        lock_obj.acquire()
        if ticket>0:
            print(f'{threading.current_thread().name}正在出售第{ticket}张票')
            ticket-=1
        time.sleep(1)

        lock_obj.release() #释放锁

if __name__=='__main__':
    for i in range(3): #创建三个线程，代表三个窗口
        t=Thread(target=sale_ticket)
        t.start()


