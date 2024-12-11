import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))

while True:
    msg = input("What to send?: ")
    clientsocket.send(msg.encode())
