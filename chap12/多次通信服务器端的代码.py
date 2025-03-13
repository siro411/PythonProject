import socket

socket_obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_obj.bind(('127.0.0.1',8888))

socket_obj.listen(5)

client_socket,client_addr=socket_obj.accept()

info=client_socket.recv(1024).decode('utf-8')
while info!='bye':
    if info!='':
        print('接收到的数据是：',info)
    data=input('请输入要发送的数据：')

    client_socket.send(data.encode('utf-8'))
    if data=='bye':
        break
    info=client_socket.recv(1024).decode('utf-8')

client_socket.close()
socket_obj.close()

