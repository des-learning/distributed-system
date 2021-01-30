import threading

def worker(name):
    for i in range(100):
        print(f"{name}: {i}")

print("program start")
threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(f"thread{i}",))
    threads.append(thread)
    thread.start()
print("program finish")
for t in threads:
    t.join()
