"""
menggunakan lock/mutex untuk mengsinkronisasi akses ke shared resource
"""
import threading, time, random

counter = 0
lock = threading.Lock() # lock untuk mendapatkan akses ke shared resource

def worker(name):
    global counter
    for _ in range(10):
        if lock.acquire():               # lock resource, only this thread can access resource
            c = counter                  # critical code, possible race condition
            time.sleep(random.random())  # critical code, possible race condition
            counter = c + 1              # critical code, possible race condition
            print(f"{name}: {counter}")  # critical code, possible race condition
            lock.release()               # release lock, other thread can now try to lock resource

threads = []
for i in ['budi', 'susi', 'iwan']:
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

print(f"counter: {counter}")