# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, l, r):
        if not root:
            return True

        if not (l < root.val <r): # this case handles everything; better than writing all true cases
            return False
        
        return self.dfs(root.left, l, root.val) and self.dfs(root.right, root.val, r)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:  
        return self.dfs(root, float('-inf'), float('inf'))