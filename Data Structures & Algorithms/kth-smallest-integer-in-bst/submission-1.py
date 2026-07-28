# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k - 1]
# class Solution:
#     arr = []  # pay attention to self.arr / arr etc. stuffs. confusing
#     def dfs(self, root):
#         if not root:
#             return
        
#         self.dfs(root.left)
#         self.arr.append(root.val)
#         self.dfs(root.right)

#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         self.dfs(root)
#         return self.arr[k-1]
        