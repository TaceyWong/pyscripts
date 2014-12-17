#coding:utf-8
import socket

if __name__ == '__main__':
    soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    soc.connect(('localhost',8002))
    import time
    time.sleep(2)
    soc.send("1")
    print soc.recv(1024)
    soc.send("0")
    print soc.recv(1024)
    soc.close()
