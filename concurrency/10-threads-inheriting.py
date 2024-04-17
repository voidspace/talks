import threading
import queue
import time, random

WORKERS = 2

# Subclassing Thread
class Worker(threading.Thread):

    def __init__(self, num, queue):
        self._num = num
        self._queue = queue
        super().__init__()

    def run(self):
        while 1:
            item = self._queue.get()
            if item is None:
                print(f"Worker {self._num} completed.")
                break # reached end of queue

            # pretend we're doing something that takes 10—100 ms
            time.sleep(random.randint(10, 100) / 1000.0)

            print(f"Task {item} finished from worker {self._num}.")

queue = queue.Queue(0)

workers = []
for i in range(WORKERS):
    worker = Worker(i, queue)
    worker.start() # start a worker
    workers.append(worker)

for i in range(10):
    queue.put(i)

for i in range(WORKERS):
    queue.put(None) # add end-of-queue markers
