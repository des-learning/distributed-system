"""
membagi task secara manual ke 3 thread
masing-masing thread mengakses shared memory `data`
"""
import threading
import time
import random

data = range(1, 1001)

def worker(name, data):
    for i in data:
        time.sleep(random.random())
        print(f"{name}: {i*10}")

threads = []
thread = threading.Thread(target=worker, args=('thread1', data[0:300]))
threads.append(thread)
thread.start()

thread = threading.Thread(target=worker, args=('thread2', data[300:700]))
threads.append(thread)
thread.start()

thread = threading.Thread(target=worker, args=('thread3', data[700:]))
threads.append(thread)
thread.start()

for t in threads:
    t.join()