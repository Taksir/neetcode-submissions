# gave me trouble
from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)
        for p, c in edges:
            adj[p].append(c)
            adj[c].append(p)

        def hasCycle(node, parent):
            if node in visited:
                return True
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor != parent and hasCycle(neighbor, node):
                    return True
            return False
        
        return not hasCycle(0, -1) and len(visited) == n