from datetime import datetime
import socket

 
address = ('localhost', 6789)
max_size = 1024
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(address)
server.listen(2)

print('Waiting for the sender now !')
sender, addr1 = server.accept()

print('Waiting for the receiver now !')
receiver, addr2 = server.accept()

data = b''
while True:
    d = sender.recv(max_size)
    if not d: break
    data += d
print "Received: data from sender"
receiver.sendall(data)
print "Sent: data to receiver"

sender.close()
receiver.close()
server.close()