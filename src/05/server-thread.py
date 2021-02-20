import socket
import time
import threading

# handler yang menghandle request dari client
def hello(conn, addr):
    print(f"accept connection from {addr}")
    time.sleep(5)
    conn.sendall(b'Hello') # send data to client
    conn.close() # close connection

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
sock.bind(('127.0.0.1', 8080)) # pasangkan socket ke ip & port tertentu
sock.listen() # set state ke listen untuk menerima koneksi dari network
while True:
    conn, addr = sock.accept() # terima koneksi dari client
    threading.Thread(target=hello, args=(conn, addr)).start()
sock.close() # close socket
