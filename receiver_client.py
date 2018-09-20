import socket
from datetime import datetime
from des_supplementary import *

def str_to_blocks(str):
    blocks = []
    for i in range(len(str)/64):
        blocks.append(str[i*64: i*64+64])
    return blocks
 
address = ('localhost',6789)
max_size = 1024
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(address)

data = b''
while True:
    d = client.recv(max_size)
    if not d: break
    data += d

i = data.find("X")
num_zeroes = int(data[i+1:])
data = data[0:i]

de = decrypt(str_to_blocks(data), num_zeroes)

file = raw_input("You are a receiver. We have decrypted the file you received from sender. Please enter the file name you want to save this decrypted file:")
convertBinaryToFile(de, file)
client.close()