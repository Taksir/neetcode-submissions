# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = first= ListNode(-1, head)
        second = head

        while n > 0:
            second = second.next
            n -= 1
        
        while second:
            first, second = first.next, second.next

        first.next = first.next.next # n is atleast 1, so first.next.next will exist

        return ans.next