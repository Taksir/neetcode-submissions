class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:      
    def __init__(self, capacity: int):
        self.map = dict()
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.remove(self.map[key])
        self.add(self.map[key])
        return self.map[key].val
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        node = Node(key,value)
        self.map[key] = node
        self.add(self.map[key])

        if len(self.map) > self.capacity:
            toRemove = self.head.next
            self.remove(toRemove)
            del self.map[toRemove.key]
    def add(self, node):
        previous = self.tail.prev
        previous.next = node
        self.tail.prev = node
        node.prev, node.next = previous, self.tail
    def remove(self, node):
        previous, nxt = node.prev, node.next
        previous.next, nxt.prev = nxt, previous

