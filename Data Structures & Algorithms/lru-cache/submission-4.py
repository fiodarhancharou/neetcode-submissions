class Node:
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
    
    def append(self, new_node):
        new_node.nxt = self.tail
        new_node.prev = self.tail.prev
        self.tail.prev.nxt = new_node
        self.tail.prev = new_node
    
    def pop_left(self):
        node = self.head.nxt
        self.head.nxt = node.nxt
        node.nxt.prev = self.head
        node.nxt = None
        node.prev = None
        return node

    def remove_node(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev
        node.prev = None
        node.nxt = None


    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node:
            self.remove_node(node)
            self.append(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.get(key)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            if not self.capacity:
                lru_node = self.pop_left()
                del self.cache[lru_node.key]
            else:
                self.capacity -= 1
            
            self.append(new_node)
