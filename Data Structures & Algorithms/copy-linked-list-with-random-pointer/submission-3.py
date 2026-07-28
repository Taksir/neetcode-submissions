"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import collections
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2new = collections.defaultdict(lambda: Node(0))
        old2new[None] = None

        curr = head
        while curr:
            old2new[curr].val = curr.val
            old2new[curr].next = old2new[curr.next]
            old2new[curr].random = old2new[curr.random]
            curr = curr.next
        
        return old2new[head]