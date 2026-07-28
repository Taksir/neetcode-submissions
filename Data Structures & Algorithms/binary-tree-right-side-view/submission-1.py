# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        ans = []

        while q:
            last = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    last = node
                    q.append(node.left)
                    q.append(node.right)
                
            if last:
                ans.append(last.val)
                
        return ans