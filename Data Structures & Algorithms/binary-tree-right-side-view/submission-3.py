# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        ans = []
        while q:
            l = len(q)
            last = None
            for i in range(l):
                nd = q.popleft()
                if nd:
                    last = nd
                    q.append(nd.left)
                    q.append(nd.right)
            if last:
                ans.append(last.val)

        return ans
