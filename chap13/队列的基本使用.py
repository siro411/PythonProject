from multiprocessing import Queue
if __name__=='__main__':
    #创建一个队列
    q=Queue(3)
    print('队列是否为空',q.empty())
    print('队列是否为满',q.full())
    q.put('hello')
    q.put('world')
    print('队列是否为空',q.empty())
    print('队列是否为满',q.full())
    q.put('Python')
    print('队列是否为空',q.empty())
    print('队列是否为满',q.full())

    print(q.get())
    print('队列当中信息的个数：',q.qsize())
    #入队
    q.put_nowait('html')
    # q.put_nowait('sql') #报错 queue.Full
    # q.put('sql') 不报错，会一直等待，等到队列中有空位置
    if not q.empty():

        for i in range(q.qsize()):

            print(q.get_nowait()) #不等待

    print('队列是否为空',q.empty())
    print('队列是否为满',q.full())
