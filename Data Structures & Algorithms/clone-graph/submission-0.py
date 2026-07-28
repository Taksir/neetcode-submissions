"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old2new = dict()

        def dfs(root):
            if root in old2new:
                return old2new[root]
            
            old2new[root] = Node(root.val)
            for n in root.neighbors:
                old2new[root].neighbors.append(dfs(n))
            
            return old2new[root]
        
        return dfs(node) if node else None