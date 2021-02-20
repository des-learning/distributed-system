import socket
import time
import threading
import queue

q = queue.Queue()

# handler yang menghandle request dari client
def hello():
    while True:
        conn, addr = q.get()
        print(f"accept connection from {addr}")
        time.sleep(5)
        conn.sendall(b'Hello') # send data to client
        conn.close() # close connection
        q.task_done()

for i in range(5):
    threading.Thread(target=hello).start()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
sock.bind(('127.0.0.1', 8080)) # pasangkan socket ke ip & port tertentu
sock.listen() # set state ke listen untuk menerima koneksi dari network
while True:
    conn, addr = sock.accept() # terima koneksi dari client
    q.put((conn, addr))

sock.close() # close socket
