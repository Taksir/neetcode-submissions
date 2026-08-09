class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        subset = []
        ans = []

        def dfs(i, j):
            if len(subset) == 2 * n:
                ans.append("".join(subset.copy()))
                return

            if i < n:
                subset.append('(')
                dfs(i + 1, j)
                subset.pop()

            if j < i:
                subset.append(')')
                dfs(i, j + 1)
                subset.pop()

        
        dfs(0, 0)
        return ans
