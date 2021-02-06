"""
semaphore dapat digunakan untuk menentukan berapa banyak proses yang dapat
mengakses shared resource
semaphore dengan nilai 1, cuma mengizinkan satu proses untuk mengakses shared
resource (sama dengan lock)
"""
import threading, time, random

counter = 0
sem = threading.Semaphore(1)

def worker(name):
    global counter
    for _ in range(10):
        if sem.acquire(timeout=0.1):
            counter = counter + 1
            print(f"{name}: {counter}")
            time.sleep(random.random())
            sem.release()
        else:
            print(f"{name} skipping")

threads = []
for i in ['budi', 'agus', 'rudi']:
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()