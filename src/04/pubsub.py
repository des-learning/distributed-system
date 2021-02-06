"""
pattern publisher subscriber
thread producer mengirimkan task ke thread consumer/worker menggunakan queueg
"""
import threading
import queue

jobs = queue.Queue() # thread safe

def producer():
    for i in range(1, 1001, 2):
        jobs.put(i) # kirimkan data untuk di-consume

def producer1():
    for i in range(0, 1001, 2):
        jobs.put(i)

def worker(name):
    print(f"start thread {name}")
    while True:
        data = jobs.get() # block until ada data yang dikirim lewat jobs
        if data is None: # sentinel value sebagai signal bahwa proses telah selesai
            jobs.task_done()
            break
        print(f"{name}: {data * 10}")
        jobs.task_done()
    print(f"thread {name} finished")

threads = []
for i in ['budi', 'agus', 'iwan']:
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

pthreads = []
thread = threading.Thread(target=producer) # send data to jobs, to be consume by consumer
pthreads.append(thread)
thread.start()
thread = threading.Thread(target=producer1) # send data to jobs, to be consume by consumer
pthreads.append(thread)
thread.start()

for t in pthreads:
    t.join()
# finish produce jobs, send finish signal to all consumer
for i in range(len(threads)):
    jobs.put(None)


for i in threads:
    i.join() # block until thread finish

