from multiprocessing import  Queue
if __name__=='__main__':
    q=Queue(3)
    #入队
    q.put('hello')
    q.put('world')
    q.put('Python')

    q.put('html',block=True,timeout=2) #等待2s，队列还没有空位就抛出异常
