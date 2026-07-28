class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowest = float('infinity')
        p = 0
        while p < len(prices):
            lowest = min(lowest, prices[p])
            maxProfit = max(maxProfit, prices[p] - lowest)
            p += 1

        return maxProfit
