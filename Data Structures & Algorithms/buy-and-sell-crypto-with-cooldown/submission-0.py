class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1] * 3 for _ in range(len(prices) + 1)]

        def dfs(i, state): # 0 sell, 1 buy
            if i >= len(prices) - 1:
                return 0
            if dp[i][state] != -1:
                return dp[i][state]

            profit = 0
            if state == 1: # i am buying here
                for j in range(i + 1, len(prices)):
                    if j < len(prices):
                        profit = max(profit, prices[j] - prices[i] + dfs(j, 0))         
            else:
                for j in range(i + 2, len(prices)):
                    if j < len(prices):
                        profit = max(profit, dfs(j, 1)) 
            dp[i][state] = profit
            return dp[i][state]


        maxProfit = 0
        for i,p in enumerate(prices):
            maxProfit = max(maxProfit, dfs(i, 1))

        return maxProfit