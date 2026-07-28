from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p = deque()
        a = deque()
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        for j in range(len(heights[0])):
            p.append((0, j))
            a.append((len(heights)-1,j))
        for i in range(len(heights)):
            p.append((i,0))
            a.append((i,len(heights[0]) - 1))
        pbool = [[False] * len(heights[0]) for i in range(len(heights))]
        abool = [[False] * len(heights[0]) for i in range(len(heights))]

        while p:
            plen = len(p)
            for i in range(plen):
                x,y = p.popleft()
                pbool[x][y] = True
                for dx, dy in dirs:
                    xx,yy = x + dx, y + dy
                    if xx >=0 and xx < len(heights) and yy>=0 and yy < len(heights[0]) \
                    and heights[xx][yy] >= heights[x][y] and not pbool[xx][yy]:
                        p.append((xx,yy))
        while a:
            alen = len(a)
            for i in range(alen):
                x,y = a.popleft()
                abool[x][y] = True
                for dx, dy in dirs:
                    xx,yy = x + dx, y + dy
                    if xx >=0 and xx < len(heights) and yy>=0 and yy < len(heights[0]) \
                    and heights[xx][yy] >= heights[x][y] and not abool[xx][yy]:
                        a.append((xx,yy))
        ans = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pbool[i][j] and abool[i][j]:
                    ans.append([i,j])
        return ans