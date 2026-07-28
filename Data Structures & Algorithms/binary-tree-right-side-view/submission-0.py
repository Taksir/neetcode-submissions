# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        deq = deque([root])
        ans = []

        while deq:
            length = len(deq)
            last = None
            for i in range(length):
                node = deq.popleft()
                if node:
                    deq.append(node.left)
                    deq.append(node.right)
                    last = node
            if last:
                ans.append(last.val)

        return ans