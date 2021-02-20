import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
sock.bind(('127.0.0.1', 8080)) # pasangkan socket ke ip & port tertentu
sock.listen() # set state ke listen untuk menerima koneksi dari network
while True:
    conn, addr = sock.accept() # terima koneksi dari client
    print(f"accept connection from {addr}")
    time.sleep(5)
    conn.sendall(b'Hello') # send data to client
    conn.close() # close connection
sock.close() # close socket

# used with context manager
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#    sock.bind(('127.0.0.1', 8080)) # pasangkan socket ke ip & port tertentu
#    sock.listen() # set state ke listen untuk menerima koneksi dari network
#    while True:
#        conn, addr = sock.accept() # terima koneksi dari client
#        print(f"accept connection from {addr}")
#        time.sleep(5)
#        conn.sendall(b'Hello') # send data to client
#        conn.close() # close connection
