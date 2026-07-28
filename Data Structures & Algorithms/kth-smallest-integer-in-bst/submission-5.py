# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = k
        ans = root.val

        def dfs(root):
            nonlocal n, ans

            if not root:
                return
            
            dfs(root.left)
            # if n == 0:
            #     return
            n -= 1
            if n == 0:
                ans = root.val
                return
            dfs(root.right)
        
        dfs(root)
        return ans