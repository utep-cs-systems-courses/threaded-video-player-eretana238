import threading


class Queue(object):
    """Creating threading Queue."""

    def __init__(self):
        self.queue = []
        self.empty = threading.Semaphore(20)
        self.full = threading.Semaphore(4)
        self.lock = threading.Lock()

    def enqueue(self, item):
        self.empty.acquire()
        with self.lock:
            self.queue.append(item)
        self.full.release()

    def dequeue(self):
        self.full.acquire()
        self.lock.acquire()
        item = self.queue.pop(0)
        self.lock.release()
        self.empty.release()
        return item

    def size(self):
        return len(self.queue)
