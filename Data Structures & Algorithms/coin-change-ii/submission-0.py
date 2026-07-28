class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(i, total):
            if total == amount:
                return 1
            if total > amount:
                return 0
            if (i,total) in dp:
                return dp[(i, total)]

            tot = 0
            for j in range(i, len(coins)):
                tot += dfs(j, total + coins[j])

            dp[(i, total)] = tot
            return tot
        
        ans = dfs(0, 0)
        return ans