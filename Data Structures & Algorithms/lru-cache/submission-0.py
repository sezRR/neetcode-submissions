class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.val = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.lru = Node()
        self.mru = Node()

        self.lru.next = self.mru
        self.mru.prev = self.lru

    def remove(self, node):
        nxt, prev = node.next, node.prev
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        nxt, prev = self.mru, self.mru.prev
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)
        if len(self.cache) > self.cap:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]

        
