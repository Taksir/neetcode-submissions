class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(l, r, pths):
            if l > n or r > n or r > l:
                return
            elif l == n and r == n:
                ans.append(''.join(pths.copy()))
                return
            
            if l == r:
                pths.append('(')
                dfs(l + 1, r, pths)
                pths.pop()
            elif l > r:
                pths.append(')')
                dfs(l, r + 1, pths)
                pths.pop()
                pths.append('(')
                dfs(l + 1, r, pths)
                pths.pop()

        dfs(0,0,[])
        return ans