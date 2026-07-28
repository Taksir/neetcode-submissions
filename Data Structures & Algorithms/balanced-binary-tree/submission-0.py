# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, node):
        if node is None:
            return -1
        height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        return height

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        leftB = self.isBalanced(root.left)
        rightB = self.isBalanced(root.right)

        leftH = self.getHeight(root.left)
        rightH = self.getHeight(root.right)

        return (abs(leftH-rightH) < 2) and leftB and rightB
