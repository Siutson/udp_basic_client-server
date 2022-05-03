import random
import socket

localIP     = "127.0.0.1"

localPort   = 20001

bufferSize  = 1024

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

print("UDP server")

# Listen for incoming datagrams

while(True):

    msgFromServer       = ["Hello UDP Client", "Eldoka na fristajlu", "Serwerinio wita", "Essa", "Uszanowanko", "Yo boiii"]
    index = random.randint(0,5)
    bytesToSend         = str.encode(msgFromServer[index])
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    # clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    # print(clientIP)
    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)