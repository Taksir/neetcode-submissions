# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        leftb, rightb = float('-inf'), float('inf')

        def dfs(root, leftb, rightb):
            if not root:
                return True
            if leftb >= root.val or rightb <= root.val:
                return False
            
            return dfs(root.left, leftb, root.val) and dfs(root.right, root.val, rightb)

        return dfs(root, leftb, rightb)