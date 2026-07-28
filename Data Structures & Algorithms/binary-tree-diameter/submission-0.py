# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def longestPath(node):
            nonlocal diameter
            if node is None:
                return -1
            leftDiameter = longestPath(node.left)
            rightDiameter = longestPath(node.right)
            diameter = max(diameter, 2 + leftDiameter + rightDiameter)
            return max(leftDiameter, rightDiameter) + 1

        longestPath(root)
        return diameter