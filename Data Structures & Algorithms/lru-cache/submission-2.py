class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.map = collections.defaultdict(tuple)
        self.capacity = capacity
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        previous, nxt = node.prev, node.next
        previous.next, nxt.prev = nxt, previous

    def add(self, node): 
        previous = self.tail.prev
        previous.next, self.tail.prev = node, node
        node.prev, node.next = previous, self.tail

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove(node)
        
        node = Node(key, value)
        self.map[key] = node
        self.add(node)

        if len(self.map) > self.capacity:
            node_to_remove = self.head.next
            self.remove(node_to_remove)
            del self.map[node_to_remove.key]
