import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 8080))
server.listen(1)

print("Server started... Waiting for connection")

conn, addr = server.accept()
print("Connected by:", addr)

request = conn.recv(1024).decode()
print("Request from client:")
print(request)

file = open("index.html", "r")
content = file.read()

response = "HTTP/1.1 200 OK\n\n" + content

conn.send(response.encode())

conn.close()
server.close()
