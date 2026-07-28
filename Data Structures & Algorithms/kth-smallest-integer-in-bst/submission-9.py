# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# inorder traversal. check base case again
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        found = False
        ans = 0
        def dfs(root):
            nonlocal counter, found, ans
            if not root or found:
                return

            dfs(root.left)
            counter += 1
            if counter == k:
                found = True
                ans = root.val
                return
            dfs(root.right)
        dfs(root)
        return ans



# import heapq
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         heap = []
#         def dfs(root):
#             if not root:
#                 return
#             nonlocal heap
#             heapq.heappush(heap, -root.val)
#             if len(heap) > k:
#                 heapq.heappop(heap)
#             dfs(root.left)
#             dfs(root.right)
#         dfs(root)
#         return -heapq.heappop(heap)