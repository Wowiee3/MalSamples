import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('192.168.43.220', 8089))
serversocket.listen(5)  # Become a server socket, maximum 5 connections

print("Server is listening for connections...")

while True:
    connection, address = serversocket.accept()
    print(f"Connection established with {address}")

    while True:
        buf = connection.recv(64)
        if not buf:  # If the client disconnects
            print(f"Connection closed by {address}")
            break
        print(buf.decode())

