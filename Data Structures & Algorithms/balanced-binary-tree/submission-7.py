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
                return [True, 0]
            
            l_bal, l_depth = dfs(root.left)
            r_bal, r_depth = dfs(root.right)
            bal = l_bal and r_bal and abs(l_depth - r_depth) < 2
            return [bal, 1 + max(l_depth, r_depth)]

        return dfs(root)[0]