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
    for j in range(len(ops)):
        print("\n", end = "")
        if(ops[j] == '1'):
            modifiedSentence = client.recvfrom(2048)
            print (modifiedSentence[0].decode(), end="")
        elif(ops[j] == '2'):
            sentence = input('Directory to navigate to: ')
            client.send(sentence.encode())
            
            modifiedSentence = client.recvfrom(2048)
            print (modifiedSentence[0].decode(), end="")
        elif(ops[j] == '3'):
            modifiedSentence = client.recvfrom(2048)
            print (modifiedSentence[0].decode(), end="")
        elif(ops[j] == '6'):
            client.close()
            break

client.close()