from socket import socket,AF_INET,SOCK_DGRAM
send_socket=socket(AF_INET,SOCK_DGRAM)
while True:
    data = input('客户说：')
    if data=='bye':
        break
    ip_port = ('127.0.0.1', 8888)
    send_socket.sendto(data.encode('utf-8'),ip_port)
    recv_data, addr = send_socket.recvfrom(1024)
    print('客服说：', recv_data.decode('utf-8'))

send_socket.close()
