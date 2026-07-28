# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev, curr = None, second
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        # prev is the 2nd list head
        second = prev
        first = head
        while second:
            tmp = first.next
            first.next = second
            tmp2 = second.next
            second.next = tmp
            first, second = tmp, tmp2

            


