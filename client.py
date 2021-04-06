import socket
server_name = '192.168.109.129'
server_port = 12001

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_name, server_port))

while 1:
    print('\nChoose from operations 1 through 5, seperate each with a space')
    print('\t1 - Print current directory path')
    print('\t2 - Change current working directory')
    print('\t3 - List contents of current directory')
    print('\t6 - close connection')
    operations = input('Selected operations: ')
    client.send(operations.encode())
    
    ops = operations.split()
    ops.sort()
    
    if(operations == '6'):
        break
    elif(operations == '2'):
        sentence = input('Directory to navigate to: ')
        client.send(sentence.encode())


    i = 0
    print("\n", end="")
    for i in range(len(ops)):
        modifiedSentence = client.recvfrom(2048)
        print (modifiedSentence[0].decode(), end="")
    
client.close()
