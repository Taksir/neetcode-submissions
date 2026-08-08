# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = head = ListNode()

        while list1 and list2:
            dummy.next = list1 if list1.val <= list2.val else list2
            if list1.val <= list2.val:
                list1 = list1.next
            else:
                list2 = list2.next

            dummy = dummy.next

        dummy.next = list2 if not list1 else list1

        return head.next