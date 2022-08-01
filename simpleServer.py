import socket

#get private ip dynamic
HOST = socket.gethostbyname(socket.gethostname())

#static ip
#HOST = '127.0.0.1'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen(5) #listen to 5 client

print(f"Server:Port  {HOST}:{PORT}")    #print server address & port

while True:
    communication_socket, address = server.accept()

    print(f"Connected to => {address}") #print connected client address

    #get client message
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client : {message}")


    #send message to client
    communication_socket.send(f"Thanks for messaging".encode('utf-8'))

    #if no need more
    communication_socket.close()
    print(f"Connection with {address} ended")