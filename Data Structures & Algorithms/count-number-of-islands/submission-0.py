class Solution:
    # def marker(self, i, j):
    #     if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
    #         return
    #     grid[i][j] = 0 # mark visited
    #     for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
    #         self.marker(i + dx, j + dy)
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0' # mark visited

            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]: #up down right left
                dfs(i + dx, j + dy)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count