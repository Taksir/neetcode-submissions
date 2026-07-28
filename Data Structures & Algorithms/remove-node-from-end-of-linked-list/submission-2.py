# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = node = ListNode(-1, head)
        curr = head
        while n > 0:
            curr = curr.next
            n -= 1
        
        # node, curr moves together
        while curr:
            node, curr = node.next, curr.next
        
        node.next = node.next.next

        return ans.next
