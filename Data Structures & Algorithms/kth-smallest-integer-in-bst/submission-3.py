# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 1
        ans = ""
        def dfs(root, k):
            nonlocal n, ans
            
            if not root:
                return
            dfs(root.left, k)
            if n == k:
                ans = root.val
            n += 1
            dfs(root.right, k)
        
        dfs(root, k)
        return ans