# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapper = {val:idx for idx,val in enumerate(inorder)}
        def helper(pre_s, pre_e, in_s, in_e):
            if pre_s > pre_e:
                return None
            header = TreeNode(preorder[pre_s])
            idx = mapper[header.val]
            no_of_items = idx - in_s
            header.left = helper(pre_s + 1,  pre_s + no_of_items, in_s, idx - 1)
            header.right = helper(pre_s + no_of_items + 1, pre_e, idx + 1, in_e)
            return header

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)