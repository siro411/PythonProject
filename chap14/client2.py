#coding:utf-8
import threading
from socket import socket,AF_INET,SOCK_STREAM

import wx
class AnnClient(wx.Frame):
    def __init__(self,client_name):
        #调用父类的初始化方法
        wx.Frame.__init__(self,None,id=1001,title=client_name+'的客户端界面',pos=wx.DefaultPosition,size=(400,450))
        #None 没有父级窗口，id表示当前窗口的编号，pos 窗体打开位置，size窗体的大小，单位是像素，400宽，450高度

        # 创建面板对象
        pl=wx.Panel(self)
        # 在面板上放上盒子
        box=wx.BoxSizer(wx.VERTICAL) #垂直布局
        fgz1=wx.FlexGridSizer(wx.HSCROLL) #可伸缩的网格布局 ，水平方向布局

        #创建两个按钮
        conn_btn=wx.Button(pl,size=(200,40),label='连接')
        disconn_btn=wx.Button(pl,size=(200,40),label='断开')

        #把两个按钮放到可伸缩的网格布局中
        fgz1.Add(conn_btn,1,wx.TOP|wx.LEFT)
        fgz1.Add(disconn_btn,1,wx.TOP|wx.RIGHT)

        #添加到box中
        box.Add(fgz1,1,wx.ALIGN_CENTRE)

        #只读文本框，显示聊天内容
        self.show_text=wx.TextCtrl(pl,size=(400,210),style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.show_text,1,wx.ALIGN_CENTRE)

        #创建聊天内容的文本框
        self.chat_txt=wx.TextCtrl(pl,size=(400,120),style=wx.TE_MULTILINE)
        box.Add(self.chat_txt,1,wx.ALIGN_CENTRE)

        #可伸缩的网格布局
        fgz2=wx.FlexGridSizer(wx.HSCROLL)
        #创建两个按钮
        reset_btn=wx.Button(pl,size=(200,40),label='重置')
        send_btn=wx.Button(pl,size=(200,40),label='发送')
        fgz2.Add(reset_btn,1,wx.TOP|wx.LEFT)
        fgz2.Add(send_btn,1,wx.TOP|wx.RIGHT)
        box.Add(fgz2,1,wx.ALIGN_CENTRE)

        #将盒子放到面板当中
        pl.SetSizer(box)
        '''----------------------以上代码是客户端界面的绘制-------------------------------------'''
        self.Bind(wx.EVT_BUTTON,self.connect_to_server,conn_btn)

        #实例属性的名称
        self.client_name=client_name
        self.isConnected=False #存储客户端连接服务器的状态，默认为False
        self.client_socket=None #设置客户端的socket对象为空
        #给 发送按钮绑定一个事件
        self.Bind(wx.EVT_BUTTON,self.send_to_server,send_btn)

        self.Bind(wx.EVT_BUTTON,self.dis_conn_server,disconn_btn)
        self.Bind(wx.EVT_BUTTON,self.reset_client,reset_btn)



    def connect_to_server(self,event):
        print(f'客服端{self.client_name}连接服务器成功')
        if not self.isConnected:
            #tcp编程的步骤
            server_host_port=('127.0.0.1',8888)
            self.client_socket=socket(AF_INET,SOCK_STREAM)
            self.client_socket.connect(server_host_port)
            #只要连接成功，发送一条数据
            self.client_socket.send(self.client_name.encode('utf-8'))
            #启动一个线程，客户端的线程与服务器的会话线程进行会话
            client_thread=threading.Thread(target=self.recv_data)
            #设置成守护线程，窗体界面关掉，子线程也结束了
            client_thread.daemon=True
            #修改连接状态
            self.isConnected=True
            client_thread.start()

    def recv_data(self):
        while self.isConnected:
            #接收来自服务器的数据
            data=self.client_socket.recv(1024).decode('utf-8')
            #显示到只读文本框
            self.show_text.AppendText('-'*40+'\n'+data+'\n')

    def send_to_server(self,event):
        #判断连接状态
        if self.isConnected:
            #从可写文本框中获取
            input_data=self.chat_txt.GetValue()
            if input_data!='':
                #向服务器端发送数据
                self.client_socket.send(input_data.encode('utf-8'))
                #发送完数据清空文本框
                self.chat_txt.SetValue('')

    def dis_conn_server(self,event):
        self.client_socket.send('A-diconnect-NNA'.encode('utf-8'))
        #改变连接状态
        self.isConnected=False

    def reset_client(self,event):
        self.chat_txt.Clear()



if __name__=='__main__':
    app=wx.App()
    name=input('请输入客户端名称：')
    # client=AnnClient('Python Anna')
    client=AnnClient(name)
    client.Show()
    #循环刷新显示
    app.MainLoop()


