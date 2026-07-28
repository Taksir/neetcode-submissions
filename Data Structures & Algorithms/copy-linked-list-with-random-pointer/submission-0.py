"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodedict =  {None : None}
        ans = head 

        while head:
            node = Node(head.val)
            nodedict[head] = node
            head = head.next
        
        head = ans
        while head:
            node = nodedict[head]
            node.next = nodedict[head.next]
            node.random = nodedict[head.random]
            head = head.next
        
        return nodedict[ans]