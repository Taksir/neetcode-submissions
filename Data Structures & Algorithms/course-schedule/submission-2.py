from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cDict = defaultdict(set)
        for i in range(len(prerequisites)):
            cDict[prerequisites[i][0]].add(prerequisites[i][1])
            
        starter = set()
        for curr in range(numCourses):
            if curr in starter:
                continue
            q = set()
            q.add(curr)
            visited = set()
            while q:
                for i in range(len(q)):
                    course = q.pop()
                    if course in visited:
                        return False
                    visited.add(course)
                    starter.add(course)
                    # print(visited, starter, cDict[course])
                    for nxtCrs in cDict[course]:
                        q.add(nxtCrs)
        return True

            