# LRU cache: 淘汰最少使用的算法.
# 每次使用时，把使用节点放在链表最前面，淘汰缓存时候，把链表尾部的节点淘汰

from doubleLinkedList import DoubleLinkedList, LinkedNode


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.list = DoubleLinkedList(self.capacity)
        self.size = 0

    def get(self, key):
        if key in self.map:
            node = self.map.get(key)
            self.list.remove(node)
            self.list.append_front(node)
            return node.val
        else:
            return -1

    def put(self, key, val):
        if key in self.map:
            node = self.map.get(key)
            self.list.remove(node)
            node.val = val
            self.list.append_front(node)
        else:
            node = LinkedNode(key, val)
            # if capacity is FULL
            if self.list.size >= self.list.capacity:
                old_node = self.list.remove()
                self.map.pop(old_node.key)
            # 解决缓存问题之后，添加节点
            self.list.append_front(node)
            self.map[key] = node

    def print(self):
        self.list.print()


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.print()
    cache.put(2, 2)
    cache.print()
    cache.put(3, 3)
    cache.print()
    cache.get(2)
    cache.print()
