from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        nodeset = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
                    nodeset.add((i,j))
            
        level = 0 # remember to increment
        def appender(i,j):
            nonlocal grid, q, nodeset
            if i<0 or j<0 or i>=len(grid) or j>= len(grid[0]) or grid[i][j] == 0 or grid[i][j] == -1 or (i,j) in nodeset:
                return
            q.append((i,j))
            nodeset.add((i,j))

        while q:
            length = len(q)
            for i in range(length):
                x, y = q.popleft()
                grid[x][y] = min(level, grid[x][y])
                appender(x+1, y)
                appender(x-1, y)
                appender(x, y-1)
                appender(x, y+1)
            level += 1


