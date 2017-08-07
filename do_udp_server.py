import socket
import time, threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 指定该Socket类型是UDP
# 绑定端口:
s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')

def tcplink(data, addr):
	print('Received from %s:%s.' % addr)
	s.sendto(b'Hello, %s!' % data, addr)

while True:
	# 接收数据:
	data, addr = s.recvfrom(1024)
	# 创建新线程来处理UDP连接:
	t = threading.Thread(target=tcplink, args=(data, addr))
	t.start()