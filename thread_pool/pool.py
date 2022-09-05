import threading
import psutil
from operate_system.thread_pool.task import Task, AsyncTask
from operate_system.thread_pool.queue import ThreadSafeQueue


# 任务处理线程
class ProcessThread(threading.Thread):
    def __init__(self, task_queue, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        # 线程停止的标记
        self.dismiss_flag = threading.Event()
        # 任务队列（处理线程不断从队列取出元素处理）
        self.task_queue = task_queue
        self.args = args
        self.kwargs = kwargs

    def run(self):
        while True:
            # 判断线程是否被要求停止
            if self.dismiss_flag.is_set():
                break
            task = self.task_queue.pop()
            if not isinstance(task, Task):
                continue
            # 执行task实际逻辑（通过函数调用引进来）
            result = task.callable(*task.args, **task.kwargs)
            if isinstance(task, AsyncTask):
                task.set_result(result)

    def stop(self):
        self.dismiss_flag.set()


# 线程池
class ThreadPool:
    def __init__(self, size=0):
        # 约定线程池大小为cpu核数的两倍
        if not size:
            size = psutil.cpu_count() * 2
        # 线程池
        self.pool = ThreadSafeQueue(size)
        # 任务队列
        self.task_queue = ThreadSafeQueue()
        for i in range(size):
            self.pool.put(ProcessThread(self.task_queue))

    def start(self):
        for i in range(self.pool.size()):
            thread = self.pool.get(i)
            thread.start()

    def join(self):
        for i in range(self.pool.size()):
            thread = self.pool.get(i)
            thread.stop()
        while self.pool.size():
            thread = self.pool.pop()
            thread.join()

    # 往线程池提交任务
    def put(self, item):
        if not isinstance(item, Task):
            raise TaskTypeErrorException
        self.task_queue.put(item)

    def batch_put(self, item_list):
        if not isinstance(item_list, list):
            item_list = list(item_list)
        for i in item_list:
            self.put(i)

    def size(self):
        return self.pool.size()


class TaskTypeErrorException(Exception):
    pass
