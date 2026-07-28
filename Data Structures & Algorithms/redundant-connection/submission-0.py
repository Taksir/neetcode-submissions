from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for f,t in edges:
            adj[f].append(t)
            adj[t].append(f)
        
        visited = set()
        visiting = set()
        parent = dict()

        def dfs(node, p):
            if node in visiting: # cycle detected
                cycle = set([node])
                curr = p
                while curr != node:
                    cycle.add(curr)
                    curr = parent[curr]
                return cycle
            visited.add(node)
            visiting.add(node)
            parent[node] = p
            for nei in adj[node]:
                if nei != p:
                    ccl = dfs(nei, node)
                    if ccl != set():
                        return ccl
            visiting.remove(node)
            return set()

        cycle = dfs(1, -1)
        src, dst = edges[0]
        for f, t in edges:
            if f in cycle and t in cycle:
                src, dst = f, t
        return [src ,dst]
