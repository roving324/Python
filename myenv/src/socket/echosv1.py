# port manager
import sys
import socket

def run_server (port=(sys.argv[1])):
	with socket.socket() as serv:
		print(socket.gethostname())
		serv.bind((socket.gethostname(),int(port)))
		serv.listen(1)
		print("server start...")
		clnt, addr = serv.accept()
		print("client connected...")
		while True:
			data = clnt.recv(1024)
			print("recv data: %s" % data.decode())
			clnt.sendall(data)
		clnt.close()

if __name__ == '__main__':
	run_server()
