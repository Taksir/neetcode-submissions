class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crs2pre = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            crs2pre[crs].append(pre)

        res = [] # when we find end of path, add it here
        completed = set()
        visiting = set() # to identify cycles

        def dfs(course):
            if course in visiting:
                return False
            if course in completed:
                return True
            visiting.add(course)

            for pre in crs2pre[course]:
                if not dfs(pre):
                    return False

            completed.add(course)
            res.append(course)
            visiting.remove(course)

            return True
        
        for crs in range(numCourses):
            if crs not in completed and not dfs(crs):
                return []
        
        return res