# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# why is second list shorter? important

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        shead = slow.next
        slow.next = None

        prev, curr = None, shead
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        # prev is the new head
        second = prev
        first = head
        # print(first.val, second.val)
        while second:
            temp = first.next
            first.next = second
            temp2 = second.next
            second.next = temp
            first, second = temp, temp2



