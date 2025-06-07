class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.store = dict()
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        
        node = self.store[key]
        self._remove(node)
        self._append_head(node)
        return node.value
    

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            node.value = value
            self._remove(node)
            self._append_head(node)
        else:
            if len(self.store) >= self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.store[lru.key]
            
            new_node = Node(key, value)
            self.store[key] = new_node
            self._append_head(new_node)
        
    def _remove(self, node):
        n_prev = node.prev        
        n_next = node.next
        n_prev.next = n_next
        n_next.prev = n_prev
    
    def _append_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)