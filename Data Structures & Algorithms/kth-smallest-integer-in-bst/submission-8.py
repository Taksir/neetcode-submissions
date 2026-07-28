# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def dfs(root):
            if not root:
                return
            nonlocal heap
            heapq.heappush(heap, -root.val)
            if len(heap) > k:
                heapq.heappop(heap)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return -heapq.heappop(heap)