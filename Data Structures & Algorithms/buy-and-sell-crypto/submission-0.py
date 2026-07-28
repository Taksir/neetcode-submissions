class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        curMin = prices[0]
        idx = 0

        while idx < len(prices):
            if prices[idx] < curMin:
                curMin = prices[idx]
                continue

            maxP = max(maxP, prices[idx] - curMin)
            idx += 1

        return maxP