class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        l, r = 0, 0
        pnths = []

        def dfs(l, r):
            if l == n and r == n:
                ans.append(''.join(pnths))
                return

            if l < n:
                pnths.append('(')
                dfs(l + 1, r)
                pnths.pop()
            if r < l:
                pnths.append(')')
                dfs(l, r + 1)
                pnths.pop()

        dfs(0, 0)
        return ans