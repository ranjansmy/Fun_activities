"""from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5)
        while(1):                                   # This is an infinite loop
            (clientsocket, address) = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if (len(pieces) > 0) : print(pieces[0])

            data = "HTTP/1.1 200 OK \r\n"
            data += "Content-Type: text/html; charset=utf-8 \r\n"
            data += "\r\n"
            data += "<html><body>Beloved Programmer!!</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())     # Encode before you send it with UTF-8
            clientsocket.shutdown(SHUT_WR)          # Protocol connection should be closed

    except KeyboardInterrupt :
        print("\nShutting Down..\n");
    except Exception as exc : 
        print("Error..\n");
        print(exc)

    serversocket.close()

print("Access http://localhost:9000")
createServer()
"""
from socket import *

def createServer():
    with socket(AF_INET, SOCK_STREAM) as serversocket:
        serversocket.bind(('localhost', 9000))
        serversocket.listen(5)

        print("Access http://localhost:9000")

        while True:
            clientsocket, address = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            if rd:
                print(rd.split('\n')[0])

            data = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n<html><body>Beloved Programmer!!</body></html>\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

if __name__ == '__main__':
    try:
        createServer()
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error:", exc)
