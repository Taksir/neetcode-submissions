class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        pths = []
        def dfs(l, r):
            if l == n and r == n:
                ans.append(''.join(pths))
                return
            
            if l < n:
                pths.append('(')
                dfs(l + 1, r)
                pths.pop()
            if r < l:
                pths.append(')')
                dfs(l, r + 1)
                pths.pop()

        dfs(0,0)
        return ans