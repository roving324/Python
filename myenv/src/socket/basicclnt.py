import socket
#socket make(adress : IPv4,data : TCP)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect try
sock.connect(("127.0.1.1", 8080))
#data
sock.sendall("Hi Python socket programming".encode())
#end
sock.close()
