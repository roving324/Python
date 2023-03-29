import socket
# socket make(adress: IPv4, data : TCP)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
# ip = socket.gethostbyname(host)
# adress (host, port)
sock.bind(("",8080))
# in time
sock.listen()
# connect ok
c_sock, addr = sock.accept()
# data
receive_data = c_sock.recv(1024)
print("recv data: %s" % receive_data.decode())
# end
c_sock.close()
sock.close()
