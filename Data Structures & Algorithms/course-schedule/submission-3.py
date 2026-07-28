from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crs2pre = defaultdict(list)
        for crs, pre in prerequisites:
            crs2pre[crs].append(pre)
        
        visiting, completed = set(), set()
        def dfs(node):
            if node in visiting:
                return True
            if node in completed or len(crs2pre[node]) == 0:
                completed.add(node)
                return False
            visiting.add(node)
            for pre in crs2pre[node]:
                if dfs(pre):
                    return True

            completed.add(node)
            visiting.remove(node)
            return False

        for i in range(numCourses):
            if dfs(i):
                return False

        return True