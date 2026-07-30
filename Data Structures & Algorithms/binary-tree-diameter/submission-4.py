# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root):
            if not root:
                return 0
            
            nonlocal ans
            lchild, rchild = dfs(root.left), dfs(root.right)
            ans = max(ans, lchild + rchild)
            return 1 + max(lchild, rchild)
        
        dfs(root)
        return ans