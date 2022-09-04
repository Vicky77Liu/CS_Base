class LinkedNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self):
        val = '{}:{}'.format(self.key, self.val)
        # val = '{%d:%d} % {self.key,self.val}'
        return val

    def __repr__(self):
        val = '{}:{}'.format(self.key, self.val)
        return val


class DoubleLinkedList:
    def __init__(self, capacity=0xffff):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

    # add from head
    def _add_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.head.prev = None
            self.tail.next = None
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = None
        self.size += 1
        return node

    # add from tail
    def _add_tail(self, node):
        if not self.tail:
            self.tail = node
            self.head = node
            self.tail.next = None
            self.head.prev = None
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = None
        self.size += 1
        return node

    #delete from head
    def _remove_head(self):
        if not self.head:
            return
        node = self.head
        if node.next:
            self.head = node.next
            self.head.prev = None
        else:
            self.head = self.tail = None
        self.size -= 1
        return node

    # delete from tail
    def _remove_tail(self):
        if not self.tail:
            return
        node = self.tail
        if node.prev:
            self.tail = node.prev
            self.tail.next = None
        else:
            self.tail = self.head = None
        self.size -= 1
        return node

    def _remove(self, node):
        # if node is None,default remove tail
        if not node:
            node = self.tail
        if node == self.tail:
            self._remove_tail()
        elif node == self.head:
            self._remove_head()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        return node

    # pop the head
    def pop(self):
        return self._remove_head()

    # add node
    def append(self, node):
        return self._add_tail(node)

    # add node from head
    def append_front(self, node):
        return self._add_head(node)

    #delete node
    def remove(self, node=None):
        return self._remove(node)

    def print(self):
        p = self.head
        line = ''
        while p:
            line += '%s' % p
            p = p.next
            if p:
                line += '-->'
        print(line)

if __name__ == '__main__':
    l = DoubleLinkedList(10)
    nodes = []
    for i in range(10):
        node = LinkedNode(i,i)
        nodes.append(node)
    print(nodes)

    l.append(nodes[0])
    l.print()
    l.append(nodes[1])
    l.print()
    l.pop()
    l.print()
    l.append(nodes[2])
    l.print()
    l.append_front(nodes[4])
    l.print()
    l.remove(nodes[2])
    l.print()






