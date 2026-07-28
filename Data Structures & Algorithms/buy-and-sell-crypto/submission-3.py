class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minP = prices[0]

        for p in prices:
            if p < minP:
                minP = p
            else:
                maxP = max(maxP, p - minP)
        return maxP