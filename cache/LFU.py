#LFU缓存置换算法：最不经常使用算法
#淘汰缓存时，把使用频率最小的淘汰
#相同频率节点用一个双链表装起来，用fifo淘汰

from doubleLinkedList import DoubleLinkedList,LinkedNode

class LFUNode(LinkedNode):
    def __init__(self,key,val):
        self.freq = 0 # 增加频率这个属性
        super (LFUNode,self).__init__(key,val)

class LFUCache(object):
    def __init__(self,capacity):
        self.capacity = capacity
        self.map = {}
        # key： 频率  val:频率对应的双向链表
        self.freq_map = {}
        self.size = 0

    #更新节点的频率
    def _update_freq(self,node):
        freq = node.freq
        # delete
        node = self.freq_map[freq].remove(node)
        if self.freq_map[freq].size == 0:
            del self.freq_map[freq]
        #update
        freq += 1
        node.freq = freq
        if freq not in self.freq_map:
            self.freq_map[freq] = DoubleLinkedList()
        self.freq_map[freq].append(node)

    def get(self,key):
        if key not in self.map:
            return -1
        node = self.map.get(key)
        self._update_freq(node)
        return node.val

    def put(self,key,val):
        if self.capacity == 0:
            return
        #缓存命中
        if key in self.map:
            node = self.map.get(key)
            node.val = val
            self._update_freq(node)

        #缓存没有命中
        else:
            if self.capacity == self.size:
                min_freq = min(self.freq_map)
                node = self.freq_map[min_freq]
                del self.map[node.key]
                self.size -= 1
            node = LFUNode(key,val)
            node.freq = 1
            self.map[key] = node
            if node.freq not in self.freq_map:
                self.freq_map[node.freq] = DoubleLinkedList()
            self.freq_map[node.freq].append(node)
            self.size += 1


    def print(self):
        for k,v in self.freq_map.items():
            print('Frequency is {}'.format(k))
            self.freq_map[k].print()
            print('**')


if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(1,1)
    cache.print()
    cache.put(2,2)
    cache.print()










