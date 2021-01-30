from multiprocessing import Process

def worker(name):
    for i in range(100):
        print(f"{name}: {i}")

print("program start")
threads = []
for i in range(3):
    thread = Process(target=worker, args=(f"thread{i}",))
    threads.append(thread)
    thread.start()
print("program finish")
for t in threads:
    t.join()
