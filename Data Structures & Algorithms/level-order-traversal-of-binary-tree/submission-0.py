# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        deq = collections.deque()
        deq.append(root)
        ans = []

        while deq:
            length = len(deq)
            array = []
            for i in range(length):
                first = deq.popleft()
                if first:
                    deq.append(first.left)
                    deq.append(first.right)
                    array.append(first.val)
            if array:
                ans.append(array)

        return ans

