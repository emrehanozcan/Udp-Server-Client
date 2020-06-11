from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',12345))
print("UDP Server Started...")

while True:
    message, address = serverSocket.recvfrom(4096)
    message = message.upper()
    serverSocket.sendto(message, address)