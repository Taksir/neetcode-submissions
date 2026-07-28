import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        visited = set()
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        def hasCycle(node, parent):
            if node in visited:
                return True
            visited.add(node)
            for nb in adj[node]:
                if nb != parent:
                    if hasCycle(nb, node):
                        return True
            return False
        
        return not hasCycle(0, -1) and len(visited) == n
