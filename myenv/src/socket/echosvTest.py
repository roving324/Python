import sys
import socket
from threading import Thread
BUFSIZE = 1024
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def run_server(port):
	ip = "192.168.0.55"
	print("server %s: %s start..." % (ip,port))
	serv.bind((ip, int(port)))
	serv.listen()
	while True:
		clnt, addr = serv.accept()
		try:
			th = (Thread(target = in_run, args = (clnt,addr[0])))
			th.start()
		except KeyboardInterrupt:
			serv.close()
def in_run(clnt,ip):
	print("%s client connected..." % ip)
	while True:
		data = clnt.recv(BUFSIZE)
		if data.decode() == 'bye':
			print("%s end" % ip)
			clnt.close()
			return
		elif data.decode() == '':
			print("$s disconnected" % ip)
			clnt.close()
			return
		print("%s: %s" % (ip, data.decode()))
		clnt.sendall(data)

if __name__ == '__main__':
	try:
		run_server(sys.argv[1])
	except (IndexError,NameError) as e:
		print("Execute: %s <port>" % sys.atgv[0])
