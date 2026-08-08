# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        head2 = slow.next # now reverse
        slow.next = None
        
        prev, curr = None, head2
        while curr:
            temp, curr.next = curr.next, prev
            prev, curr = curr, temp

        head2 = prev
        head1 = head
        #0 1 2 3    -    6 5 4
        while head2:
            tmp1, tmp2 = head1.next, head2.next
            head1.next = head2
            head2.next = tmp1
            head1, head2 = tmp1, tmp2
