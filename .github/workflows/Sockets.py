#1.import socket module
import socket

#2.create a socket name mysocket
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#3.connect that socket to the web page
mysocket.connect(('data.pr4e.org',80))

#4.get the web page, encode the data in bytes and store it in cmnd
cmnd='GET https://data.pr4e.org/romeo.txt HTTP/1.1\n\n'.encode()

#5.send the cmnd through mysocket and request the web page
mysocket.send(cmnd)

while(True):
    data=mysocket.recv(500)#receive 500 charecter
    if len(data)<1:#End of file
        break
    print(data.decode())#Byte is decoded to unicode string
mysocket.close()#close socket connection
