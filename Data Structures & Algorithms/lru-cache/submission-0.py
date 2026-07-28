class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.add(self.map[key])
            return self.map[key].val # treturn val not node itself
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        self.map[key] = Node(key, value)
        self.add(self.map[key])

        if len(self.map) > self.capacity:
            toRemove = self.head.next
            self.remove(toRemove)
            del self.map[toRemove.key]

    def add(self, node):
        prev = self.tail.prev
        self.tail.prev = node
        prev.next = node
        node.prev, node.next = prev, self.tail

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
