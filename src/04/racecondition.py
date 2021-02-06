"""
simulasi race condition
race condition dikarenakan beberapa thread mengakses dan mengubah share
resource tanpa ada sinkronisasi akses
"""
import threading, time, random

counter = 0

def worker(name):
    global counter
    for _ in range(10):
        c = counter                  # critical code, possible race condition
        time.sleep(random.random())  # critical code, possible race condition
        counter = c + 1              # critical code, possible race condition
        print(f"{name}: {counter}")  # critical code, possible race condition

threads = []
for i in ['budi', 'susi', 'iwan']:
    thread = threading.Thread(target=worker, args=(i,))
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

print(f"counter: {counter}")