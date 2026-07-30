# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        counter = k
        def dfs(root, k):
            nonlocal counter, ans              
            if not root or ans:
                return
            
            dfs(root.left, counter)
            counter -= 1
            if counter == 0:
                ans = root.val
                return
            
            dfs(root.right, counter)

        dfs(root, counter)
        return ans