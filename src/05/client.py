import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8080))
data = sock.recv(1024).decode()
print(f"data received from server: {data}")
sock.close()
