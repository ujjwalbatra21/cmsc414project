import socket
import os
server_port = 12001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', server_port))
server.listen(1)
while 1:
    print ("The server is ready to receive")
    print ("Waiting ...")
    connection_socket, addr = server.accept()
    print ("accept")
    end = 'false'
    while 1:
        if(end == 'true'):
            connection_socket.close()
            break
        end = 'false'
        
        operations = connection_socket.recv(2048).decode()
        print ("Cleaning disk " + operations)
        arr = operations.split()
        i = 0
        for i in range(len(arr)):
            if(arr[i] == '1'):
                currentDirectory = "Current Directory: " + os.getcwd() + "\n"
                connection_socket.send(currentDirectory.encode())
            elif(arr[i] == '2'):
                sentence = connection_socket.recv(2048).decode()
                print("Message Received: " + sentence)
                os.chdir(sentence)
                currentDirectory = "Current Directory: " + os.getcwd() + "\n"
                connection_socket.send(currentDirectory.encode())
            elif(arr[i] == '3'):
                sentence = os.getcwd()
                contents = str(os.listdir(sentence))
                connection_socket.send(contents.encode())
            elif(arr[i] == '6'):
                end = 'true';
            else:
                ErrorMessage = arr[i] + ") Unknown instruction\n"
                connection_socket.send(ErrorMessage.encode())
