class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        boxs = [list() for _ in range(len(board) // 3)]
        for j in range(3):
            boxs[j] = [set() for _ in range(len(board) // 3)]

        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == '.':
                    continue
                if ch in rows[i] or ch in cols[j] or ch in boxs[i // 3][j // 3]:
                    return False
                rows[i].add(ch)
                cols[j].add(ch)
                boxs[i // 3][j // 3].add(ch)

        return True