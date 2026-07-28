# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if root is None:
            return (True, -1)
        leftB, leftH = self.helper(root.left)
        if not leftB:
            return (False, 0)
        rightB, rightH = self.helper(root.right)
        if not rightB:
            return (False, 0)
        return (abs(leftH - rightH) < 2, 1 + max(leftH, rightH))
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[0]
