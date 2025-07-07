#how to retrive the headers and content in a web
import socket                                                               #1st import the socket
                                       #use a stream(a series of characters that just keep coming back)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                  #2nd set a connection point that has not yet been connected 
                       #hookup the things across the internet
mysock.connect(('data.pr4e.org', 80))                                       #3rd conncet the "host" and "port"
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()  #4th GET   (encode: convert strings into bytes objects)
mysock.send(cmd)                                                            #5th made the phone call

while True:
    data = mysock.recv(200)                                                 #recv: receive the headers and content in bytes objects 512characters utmost
    if len(data) < 1:                                                       #length<1 means rereiving was over then break
        break
    print(data.decode(),end='')                                             #decode: convert bytes objects back to strings

mysock.close()
