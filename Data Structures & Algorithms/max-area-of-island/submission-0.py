class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            count = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                count += dfs(i + dx, j + dy)
            
            return count 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    maxArea = max(maxArea, area)

        return maxArea