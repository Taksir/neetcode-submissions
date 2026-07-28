# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root, maxSoFar):
            nonlocal ans
            if not root:
                return
            
            if root.val < maxSoFar:
                dfs(root.left, maxSoFar)
                dfs(root.right, maxSoFar)
            else:
                ans += 1
                dfs(root.left, root.val)
                dfs(root.right, root.val)

        dfs(root, root.val)
        return ans