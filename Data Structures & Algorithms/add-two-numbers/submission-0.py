# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)

        curr = dummy
        carry = 0

        while l1 and l2:
            sum = l1.val + l2.val + carry
            node = ListNode(sum % 10)
            curr.next = node
            carry = sum // 10
            l1, l2 = l1.next, l2.next
            curr = curr.next

        newl = l1 if l1 else l2

        while newl:
            sum = newl.val + carry
            node = ListNode(sum % 10)
            curr.next = node
            carry = sum // 10
            newl = newl.next
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(1)

        return dummy.next