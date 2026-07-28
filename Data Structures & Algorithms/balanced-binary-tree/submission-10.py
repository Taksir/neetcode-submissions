# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            ld = dfs(root.left)
            if ld == -1:
                return -1
            rd = dfs(root.right)
            if rd == -1:
                return -1
            if abs(ld - rd) > 1:
                return -1
            
            return 1 + max(ld, rd)
        
        return dfs(root) != -1