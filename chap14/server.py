import threading
import time
from socket import socket,AF_INET,SOCK_STREAM
from threading import main_thread

import wx
class AnnServer(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,id=1002,title='ANNA服务器端界面',pos=wx.DefaultPosition,size=(400,450))
        #窗口放一个面板
        pl=wx.Panel(self)
        #面板上放一个盒子
        box=wx.BoxSizer(wx.VERTICAL) #垂直放向上自动排版
        fgz1=wx.FlexGridSizer(wx.HSCROLL) #可伸缩的网格布局 ，水平方向布局

        start_server_btn=wx.Button(pl,size=(133,40),label='启动服务')
        save_log_btn=wx.Button(pl,size=(133,40),label='保存聊天记录')
        stop_server_btn=wx.Button(pl,size=(133,40),label='停止服务')

        #将按钮放到可伸缩的网格布局中
        fgz1.Add(start_server_btn,1,wx.TOP)
        fgz1.Add(save_log_btn,1,wx.TOP)
        fgz1.Add(stop_server_btn,1,wx.TOP)

        #可伸缩的网格布局放到box中

        box.Add(fgz1,wx.ALIGN_CENTER)
        #只读的多行文本框
        self.show_text = wx.TextCtrl(pl, size=(400, 410), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.show_text, 1, wx.ALIGN_CENTRE)

        pl.SetSizer(box)

        '''-----------------以上代码都是界面的绘制代码--------------------------'''
        self.isOn=False #存储服务器的启动状态，默认值False，默认没有启动
        #服务器绑定的ip地址和端口号
        self.host_port=('',8888) #空的字符串代码是本机的所有IP
        #创建socket对象
        self.server_socket=socket(AF_INET,SOCK_STREAM)
        self.server_socket.bind(self.host_port)
        self.server_socket.listen(5)
        #创建一个字典，存储与客户端对话的会话线程
        self.session_thread_dict={} #key {客户端的名称} value {整个会话线程}

        #当鼠标点击“启动服务“时，要执行的操作
        self.Bind(wx.EVT_BUTTON,self.start_server,start_server_btn)
        # 保存聊天记录按钮
        self.Bind(wx.EVT_BUTTON,self.save_record,save_log_btn)

        self.Bind(wx.EVT_BUTTON,self.stop_server,stop_server_btn)

    def stop_server(self,event):
        print('服务器停止服务')
        self.isOn=False



    def save_record(self,event):
        record=self.show_text.GetValue()
        with open ('record.log','w',encoding='utf-8') as file:
            file.write(record)






    def start_server(self,event):
        # print('启动服务的按钮被点击了')
        #判断服务器是否已经启动
        if not self.isOn:
            self.isOn=True
            #创建主线程对象，创建函数式创建主线程
            main_thread=threading.Thread(target=self.do_work)
            #设置为守护线程，父线程执行结束（窗体节目）子线程也自动关闭
            main_thread.daemon=True
            main_thread.start()


    def do_work(self):
        while self.isOn:
            #接收客户端的连接请求
            session_socket,client_addr=self.server_socket.accept()
            #客户端发送连接请求之后，发送过来的第一条数据为客户端的名称，作为字典的key
            usr_name=session_socket.recv(1024).decode('utf-8')
            #创建一个会话线程对象
            session_thread=SessionThread(session_socket,usr_name,self)
            #存储到字典当中
            self.session_thread_dict[usr_name]=session_thread
            #启动会话线程
            session_thread.start()
            #输出服务器的提示信息
            self.show_info_and_send_client('服务器通知',f'欢迎{usr_name}进入聊天室',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        #当self.isOn的值为False时，执行关闭socket对象
        self.server_socket.close()

    def show_info_and_send_client(self, data_source, data, date_time):
        # 字符串的拼接操作
        send_data = f'{data_source}:{data}\n时间：{date_time}'
        # 只读文本框
        self.show_text.AppendText('-' * 40 + '\n' + send_data + '\n')
        #每个客户端都发送一次
        for client in self.session_thread_dict.values():
            #client是否开启状态
            if client.isOn:
                client.client_socket.send(send_data.encode('utf-8'))


#服务器端会话线程的类
class SessionThread(threading.Thread):
    def __init__(self,client_socket,usr_name,server):
        threading.Thread.__init__(self)
        self.client_socket=client_socket
        self.usr_name=usr_name
        self.server=server
        self.isOn=True #会话线程是否启动，当创建SessionThread对象时会话线程即启动

    def run(self) -> None:
        print(f'客户端:{self.usr_name}已经和服务器连接成功，服务器启动一个会话线程')
        while self.isOn:
            #从客户端接收数据，存储到data
            data=self.client_socket.recv(1024).decode('utf-8')
            #如果客户端点击断开按钮，先给服务器发送一句话，消息自定义,A-diconnect-NNA 自定义的结束词
            if data=='A-diconnect-NNA':
                self.isOn=False
                self.server.show_info_and_send_client('服务器通知',f'{self.usr_name}离开了聊天室',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

            else:
                #其他聊天信息显示给所有的客户端，包含服务器也显示
                #调用
                self.server.show_info_and_send_client(self.usr_name,data,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        #关闭socket
        self.client_socket.close()




if __name__=='__main__':
    app=wx.App()
    server=AnnServer()
    server.Show()

    app.MainLoop()



