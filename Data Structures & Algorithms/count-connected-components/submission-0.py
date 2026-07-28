from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        ans = 0
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        def traverse(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adj[node]:
                traverse(neighbor)
        
        for i in range(n):
            if i not in visited:
                ans += 1
                traverse(i)
        
        return ans