class Solution:
    def numDecodings(self, s: str) -> int:
        x = list(range(1, 27))
        valid = set([str(n) for n in x])
        memo = [-1] * (len(s) + 1)
        def dfs(i):
            if i >= len(s):
                return 0
            if i == len(s) - 1:
                return 1
            if memo[i] != -1:
                return memo[i]
            
            onechar = dfs(i + 1) if s[i + 1] in valid else 0
            twochar = dfs(i + 2) if i + 2 < len(s) and s[i+1:i+3] in valid else 0
            memo[i] = onechar + twochar
            return onechar + twochar
        
        total = dfs(-1)
        return total