class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        string = []
        def dfs(l, r):
            if l == n and r == n:
                ans.append(''.join(string.copy()))
                return

            if l < n:
                string.append('(')
                dfs(l + 1, r)
                string.pop()

            if r < l:
                string.append(')')
                dfs(l, r + 1)
                string.pop()

        dfs(0, 0)
        return ans