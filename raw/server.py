#coding:utf-8

import socket

#Step1:创建socket对象，调用socket构造函数

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM )#(family,type)

'''
family:代表地址家族，可为AF_INET(internet地址)\AF_UNIX（本机进程间通信）
type:代表套接字类型，可谓SOCKET_STREAM(流套接字)和SOCKET_DGRAM(数据报套接字)
'''

#Step2:将socket绑定到指定的地址。这是通过socket对象的bind方法来实现的

soc.bind(('localhost',8002))#(host,port)

'''
①由AF_INET所建立的套接字，地址必须为一个双元素数组（host，port）
'''

#Step3:使用socket套接字的listen方法接受链接请求

soc.listen(5)

'''
backing指定最多允许多少个客户连接到服务器。它的值至少为1.收到请求后，
这些请求需要队列，如果队列满，就拒绝请求
'''

while True:
    
#Step4：服务器套接字通过socket的accept方法等待客户请求一个链接
    
    connection,address = soc.accept()

    '''
    调用accept方法时，socket会进入waiting状态
    '''
    try:
        connection.settimeout(5)
        buf = connection.recv(1024)
        if buf == '1':
            connection.send("欢迎到访")

        else:
            connection.send("你是谁")

    except socket.timeout:
        print "time out"
    connection.close()

    
