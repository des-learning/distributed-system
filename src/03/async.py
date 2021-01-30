import time
import threading
import queue

# synchronous
def process():
    time.sleep(5)
    return 10

print(process())
print("finish sync")

# async with simple thread
def asyncfn(fn, args=(), kwargs={}):
    threading.Thread(target=fn, args=args, kwargs=kwargs).start()

asyncfn(lambda: print(process()))
print("finish async simple thread")

# async with event loop
events = queue.Queue()
def publish_event(fn):
    events.put(fn)

def event_worker(events):
    while True:
        event = events.get()
        if event is None:
            events.task_done()
            break
        event()
        events.task_done()

# event processor
threading.Thread(target=event_worker, args=(events,)).start()

publish_event(lambda: print(process()))
publish_event(lambda: print('hello worood'))
publish_event(lambda: print('yuhuuu'))
publish_event(None) # sentinel value to signal that the events already finished
print("finish async eventloop")
# wait for event to drain
events.join()
