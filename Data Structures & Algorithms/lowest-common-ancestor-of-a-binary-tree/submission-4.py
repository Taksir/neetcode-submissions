# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if (left == p and right == q) or (left == q and right == p):
            return root 
        
        return left if left else right

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if root is None or root is p or root is q:
#             return root
#         left = self.lowestCommonAncestor(root.left, p, q)
#         right = self.lowestCommonAncestor(root.right, p, q)
#         if left and right:
#             return root
#         return left if left else right
            

# man i had so many errors. dont forget head is always a possible ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        root2parent = dict()
        foundP, foundQ = False, False
        head = root
        ans = head
        nodeP, nodeQ = None, None
        def dfs(root):
            if not root:
                return
            nonlocal foundP, foundQ, head, ans, nodeP, nodeQ
            if root == p:
                nodeP = root
                foundP = True
            if root == q:
                nodeQ = root
                foundQ = True
            if foundP and foundQ: # main part
                curr = nodeP # either p or q
                traverseSet = set([head])
                while curr != head:
                    traverseSet.add(curr)
                    curr = root2parent[curr]

                curr = nodeQ
                while curr != head:
                    if curr in traverseSet:
                        ans = curr
                        break
                    curr = root2parent[curr]
                return

            if root.left:
                root2parent[root.left] = root
            if root.right:
                root2parent[root.right] = root
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ans