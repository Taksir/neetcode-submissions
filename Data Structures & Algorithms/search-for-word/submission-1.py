class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(row, col, visited, i):
            if row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1 or tuple([row, col]) in visited or board[row][col] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            visited.add((row, col))

            for m, n in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                node = (row + m, col + m) # down
                if dfs(row + m, col + n, visited, i + 1):
                    return True

            visited.remove((row, col))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i,j,set(), 0):
                    return True
                    
        return False