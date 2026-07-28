# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        ans = prev = ListNode(-1, head)
        curr = head

        length = length - n

        while length > 0:
            prev, curr = prev.next, curr.next
            length -= 1
        
        prev.next = curr.next

        return ans.next