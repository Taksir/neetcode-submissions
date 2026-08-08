# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = first = second = ListNode(-1, head)

        while n > 0:
            second = second.next
            n -= 1
        
        temp = first
        while second:
            second = second.next
            temp = first
            first = first.next

        temp.next = temp.next.next

        return ans.next