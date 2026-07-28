from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        q = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            for i in range(len(q)):
                m, n = q.popleft()
                for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                    x,y = m + dx, n + dy
                    if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x,y))
                        fresh -= 1
            minute += 1

        return minute if not fresh else -1