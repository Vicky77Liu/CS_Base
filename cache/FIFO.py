# FIFO缓存置换算法，需要淘汰缓存时把最先进入链表的节点淘汰

from doubleLinkedList import DoubleLinkedList, LinkedNode


class FIFOCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.list = DoubleLinkedList(self.capacity)

    def get(self, key):
        if key not in self.map:
            return -1
        else:
            node = self.map.get(key)
            return node.val

    def put(self, key, val):
        if self.capacity == 0:
            return

        if key in self.map:
            node = self.map.get(key)
            self.list.remove(node)
            node.val = val
            self.list.append(node)
        else:
            if self.size == self.capacity:
                node = self.list.pop()
                del self.map[node.key]
                self.size-=1
            node = LinkedNode(key, val)
            self.list.append(node)
            self.map[key] = node
            self.size += 1

    def print(self):
        self.list.print()


if __name__ == '__main__':
    cache = FIFOCache(2)
    cache.put(1, 1)
    cache.print()
    cache.put(2, 2)
    cache.print()
    print(cache.get(1))
    cache.put(3, 3)
    cache.print()
    print(cache.get(2))
    cache.print()
