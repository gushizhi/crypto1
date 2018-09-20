import socket
from datetime import datetime
from des_supplementary import *
import pickle

address = ('localhost',6789)
max_size = 1024
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(address)

file = raw_input("You are a sender. Please input your file directory to be encrypted and then sent to receiver:")

m = convertFileToBinary(file)
data = encrypt(m)

tobesent = ""
for d in data[0]:
    tobesent += d
print tobesent
tobesent += "X"
tobesent += str(data[1])

client.sendall(tobesent)

client.close()