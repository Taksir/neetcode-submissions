class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, idx):
            if idx == len(word):
                return True
            if board[i][j] == word[idx]:
                if idx == len(word) - 1:
                    return True
                visited.add((i, j))
                dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dx,dy in dir:
                    x, y = i + dx, j + dy
                    if x >= 0 and y >= 0 and x < len(board) and y < len(board[0]) and (x, y) not in visited:
                        if dfs(x, y, idx + 1):
                            return True
                visited.remove((i, j))
            return False
            

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False