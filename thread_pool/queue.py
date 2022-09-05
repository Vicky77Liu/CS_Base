import threading
import time


class ThreadSafeQueueException(Exception):
    pass


# 线程安全队列
class ThreadSafeQueue(object):

    def __init__(self, max_size=0):
        self.queue = []
        self.max_size = max_size
        self.lock = threading.Lock()
        self.condition = threading.Condition()

    def size(self):
        self.lock.acquire()
        size = len(self.queue)
        self.lock.release()
        return size

    def put(self, item):
        if self.max_size != 0 and self.size() > self.max_size:
            raise ThreadSafeQueueException
        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        self.condition.acquire()
        self.condition.notify()
        self.condition.release()

    def batch_put(self, item_list):
        if not isinstance(item_list, list):
            item_list = list(item_list)
        for i in item_list:
            self.put(i)

    # block 是否阻塞， timeout 等待时间
    def pop(self, block=False, timeout=0):
        if self.size() == 0:
            # 需要阻塞等待
            if block:
                self.condition.acquire()
                self.condition.wait(timeout=timeout)
                self.condition.release()
            else:
                return None
        self.lock.acquire()
        # 等待后还是为空，直接返回none
        item = None
        if self.size() > 0:
            item = self.queue.pop()
        self.lock.release()
        return item

    def get(self, index, block=False, timeout=0):
        if self.size() == 0:
            # 需要阻塞等待
            if block:
                self.condition.acquire()
                self.condition.wait(timeout=timeout)
                self.condition.release()
            else:
                return None
        # 等待后还是为空，直接返回none
        if self.size() == 0:
            return None
        if 0 <= index <= self.size():
            self.lock.acquire()
            item = self.queue[index]
            self.lock.release()
            return item
        else:
            raise ThreadSafeQueueException


if __name__ == '__main__':
    queue = ThreadSafeQueue(max_size=100)

    def producer():
        while True:
            queue.put(1)
            time.sleep(3)

    def costumer():
        while True:
            item = queue.pop(block=True, timeout=1)
            print('get item from queue:{}'.format(item))
            time.sleep(1)

    thread1 = threading.Thread(target=producer)
    thread2 = threading.Thread(target=costumer)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()