from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        bools = [[False] * COLS for _ in range(ROWS)]
        q = deque()
        for j in range(COLS):
            if board[0][j] == 'O':
                q.append((0, j))
            if board[ROWS - 1][j] == 'O':
                q.append((ROWS - 1, j))
        for i in range(ROWS):
            if board[i][0] == 'O':
                q.append((i,0))
            if board[i][COLS - 1] == 'O':
                q.append((i, COLS - 1))
        
        while q:
            length = len(q)
            for i in range(length):
                x, y = q.popleft()
                if bools[x][y]:
                    continue
                bools[x][y] = True
                for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                    xx, yy = x + dx, y + dy
                    if xx >= 0 and yy >= 0 and xx < ROWS and yy < COLS and board[xx][yy] == 'O' \
                     and not bools[xx][yy]:
                        q.append((xx, yy))
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and not bools[i][j]:
                    board[i][j] = 'X'
