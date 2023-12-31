"""
dict 服务端
功能：业务逻辑处理
模型：多进程tcp并发
"""

from socket import *
from multiprocessing import Process
import signal, sys


# 全局变量
HOST = '0.0.0.0'
PORT = 8001
ADDR = (HOST, PORT)


# 接受客户端请求，分配处理函数
def request(c):
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(), ':', data)


# 搭建网络
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(3)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    # 循环等待客户端连接
    print('Listen the port 8000')
    while True:
        try:
            c, addr = s.accept()
            print('Connect from', addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            print(e)
            continue

        # 创建子进程
        p = Process(target=request, args=(c,))
        p.daemon = True
        p.start()

