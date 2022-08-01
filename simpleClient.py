import socket

HOST = input("Enter Server IP : ")
PORT = int(input("Enter Server PORT : "))

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST,PORT))

msg = input("Send message to server : ")
socket.send(msg.encode('utf-8'))

print((socket.recv(1024).decode('utf-8')))