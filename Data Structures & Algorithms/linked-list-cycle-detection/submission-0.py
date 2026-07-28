# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashTable = set()
        while head:
            if head in hashTable:
                return True
            hashTable.add(head)
            head = head.next
        
        return False